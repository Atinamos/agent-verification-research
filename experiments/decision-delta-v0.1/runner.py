#!/usr/bin/env python3
"""Decision Delta v0.1 paired experiment runner.

The runner does not pay services itself. It constructs two isolated decision
conditions from one frozen scenario and invokes the same buyer adapter for both.
A fixture buyer exists only to validate experiment plumbing before live research.
Fixture output is never eligible for the research dataset.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import shlex
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any


ACTIONS = {"BUY", "ABSTAIN", "REVIEW", "REQUEST_FRESH_EVIDENCE"}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def digest(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def candidate_map(scenario: dict[str, Any]) -> dict[str, dict[str, Any]]:
    candidates = scenario.get("candidates")
    if not isinstance(candidates, list) or len(candidates) < 2:
        raise ValueError("scenario must contain at least two candidates")
    result: dict[str, dict[str, Any]] = {}
    for item in candidates:
        if not isinstance(item, dict) or not item.get("candidate_id"):
            raise ValueError("every candidate requires candidate_id")
        candidate_id = str(item["candidate_id"])
        if candidate_id in result:
            raise ValueError(f"duplicate candidate_id: {candidate_id}")
        result[candidate_id] = item
    return result


def build_payload(
    scenario: dict[str, Any],
    policy: dict[str, Any],
    condition: str,
) -> dict[str, Any]:
    payload = {
        "protocol_version": scenario["protocol_version"],
        "scenario_id": scenario["scenario_id"],
        "condition": condition,
        "task": scenario["task"],
        "budget_usdc": scenario["budget_usdc"],
        "task_requirements": scenario["task_requirements"],
        "policy": policy,
        "candidates": scenario["candidates"],
    }
    if condition == "evidence_assisted":
        payload["evidence_snapshot"] = scenario.get("evidence_snapshot") or {}
    return payload


def validate_decision(decision: dict[str, Any], candidates: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if not isinstance(decision, dict):
        raise ValueError("buyer output must be a JSON object")
    action = decision.get("action")
    if action not in ACTIONS:
        raise ValueError(f"invalid buyer action: {action!r}")
    selected = decision.get("selected_candidate_id")
    if selected is not None and selected not in candidates:
        raise ValueError(f"buyer selected unknown candidate: {selected}")
    if action == "BUY" and selected is None:
        raise ValueError("BUY requires selected_candidate_id")
    if action != "BUY" and selected is not None:
        raise ValueError(f"{action} must not select a candidate")
    reasons = decision.get("reason_codes")
    if not isinstance(reasons, list) or not all(isinstance(item, str) for item in reasons):
        raise ValueError("reason_codes must be an array of strings")
    notes = decision.get("notes", [])
    if not isinstance(notes, list) or not all(isinstance(item, str) for item in notes):
        raise ValueError("notes must be an array of strings")
    return {
        "action": action,
        "selected_candidate_id": selected,
        "reason_codes": reasons,
        "notes": notes,
    }


def run_command_buyer(command: str, payload: dict[str, Any]) -> dict[str, Any]:
    completed = subprocess.run(
        shlex.split(command),
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=False,
        timeout=120,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"buyer command exited {completed.returncode}: {completed.stderr.strip()}"
        )
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("buyer command did not emit valid JSON") from exc
    if not isinstance(result, dict):
        raise RuntimeError("buyer command output must be one JSON object")
    return result


def fixture_buyer(payload: dict[str, Any]) -> dict[str, Any]:
    """Deterministic plumbing-only buyer; never use its output as research data."""
    policy = payload["policy"]
    allowed_networks = set(policy["payment"]["allowed_networks"])
    service_cap = Decimal(policy["budget"]["max_service_price_usdc"])
    task_budget = Decimal(payload["budget_usdc"])
    cap = min(service_cap, task_budget)

    candidates = [
        item
        for item in payload["candidates"]
        if item["network"] in allowed_networks and Decimal(item["price_usdc"]) <= cap
    ]
    if not candidates:
        return {
            "action": "ABSTAIN",
            "selected_candidate_id": None,
            "reason_codes": ["NO_CANDIDATE_WITHIN_GLOBAL_POLICY"],
        }

    if payload["condition"] == "evidence_assisted":
        evidence = payload.get("evidence_snapshot") or {}
        permitted: list[dict[str, Any]] = []
        review_needed = False
        exploratory_cap = Decimal(policy["unknown_service"]["exploratory_cap_usdc"])
        for item in candidates:
            observed = evidence.get(item["candidate_id"], {})
            state = observed.get("policy_decision")
            if state == "eligible":
                permitted.append(item)
            elif state == "insufficient_evidence":
                review_needed = True
            elif state == "not_eligible":
                continue
            elif observed.get("known") is False and Decimal(item["price_usdc"]) <= exploratory_cap:
                permitted.append(item)
            else:
                review_needed = True
        if not permitted:
            if review_needed:
                return {
                    "action": "REVIEW",
                    "selected_candidate_id": None,
                    "reason_codes": ["NO_POLICY_ELIGIBLE_CANDIDATE_WITH_COMPLETE_EVIDENCE"],
                }
            return {
                "action": "ABSTAIN",
                "selected_candidate_id": None,
                "reason_codes": ["EVIDENCE_POLICY_REJECTED_ALL_CANDIDATES"],
            }
        candidates = permitted

    selected = min(candidates, key=lambda item: (Decimal(item["price_usdc"]), item["candidate_id"]))
    return {
        "action": "BUY",
        "selected_candidate_id": selected["candidate_id"],
        "reason_codes": [
            "WITHIN_BUDGET_AND_NETWORK_POLICY",
            "LOWEST_PRICE_AMONG_PERMITTED_CANDIDATES",
        ],
    }


def invoke_buyer(
    payload: dict[str, Any],
    candidates: dict[str, dict[str, Any]],
    buyer_command: str | None,
) -> dict[str, Any]:
    raw = run_command_buyer(buyer_command, payload) if buyer_command else fixture_buyer(payload)
    return validate_decision(raw, candidates)


def classify_delta(
    control: dict[str, Any],
    treatment: dict[str, Any],
    candidates: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    changed = (
        control["action"] != treatment["action"]
        or control["selected_candidate_id"] != treatment["selected_candidate_id"]
    )
    if not changed:
        return {"changed": False, "classifications": ["no_delta"]}

    classes: list[str] = []
    if control["selected_candidate_id"] != treatment["selected_candidate_id"]:
        if control["action"] == treatment["action"] == "BUY":
            classes.append("provider_delta")
            c_price = Decimal(candidates[control["selected_candidate_id"]]["price_usdc"])
            t_price = Decimal(candidates[treatment["selected_candidate_id"]]["price_usdc"])
            if c_price != t_price:
                classes.append("price_delta")
    if "ABSTAIN" in {control["action"], treatment["action"]}:
        classes.append("abstention_delta")
    if "REQUEST_FRESH_EVIDENCE" in {control["action"], treatment["action"]}:
        classes.append("fresh_evidence_delta")
    if control["action"] == "BUY" and treatment["action"] in {
        "ABSTAIN",
        "REVIEW",
        "REQUEST_FRESH_EVIDENCE",
    }:
        classes.append("risk_response_delta")
    if not classes:
        classes.append("risk_response_delta")
    return {"changed": True, "classifications": list(dict.fromkeys(classes))}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True, type=Path)
    parser.add_argument("--policy", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--buyer-command",
        help="Command invoked separately for each condition; reads one JSON payload on stdin and writes one decision JSON object on stdout.",
    )
    parser.add_argument("--seed", type=int)
    parser.add_argument(
        "--condition-order",
        choices=["random", "control-first", "evidence-first"],
        default="random",
    )
    args = parser.parse_args()

    scenario = load_json(args.scenario)
    policy = load_json(args.policy)
    if scenario.get("policy_id") != policy.get("policy_id"):
        raise ValueError("scenario policy_id does not match supplied policy")
    candidates = candidate_map(scenario)

    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(1, 2**63)
    rng = random.Random(seed)
    if args.condition_order == "control-first":
        order = ["control", "evidence_assisted"]
    elif args.condition_order == "evidence-first":
        order = ["evidence_assisted", "control"]
    else:
        order = ["control", "evidence_assisted"]
        rng.shuffle(order)

    started = utcnow()
    pair_id = str(uuid.uuid4())
    results: dict[str, dict[str, Any]] = {}

    for condition in order:
        payload = build_payload(scenario, policy, condition)
        decision = invoke_buyer(payload, candidates, args.buyer_command)
        results[condition] = {
            "condition": condition,
            "input_sha256": digest(payload),
            "decision": decision,
            "payment_attempted": False,
            "purchase_result": None,
        }

    delta = classify_delta(
        results["control"]["decision"],
        results["evidence_assisted"]["decision"],
        candidates,
    )

    record = {
        "pair_id": pair_id,
        "scenario_id": scenario["scenario_id"],
        "protocol_version": scenario["protocol_version"],
        "execution_mode": "decision_only" if args.buyer_command else "dry_run_fixture",
        "eligible_for_analysis": bool(args.buyer_command),
        "seed": seed,
        "condition_order": order,
        "started_at": started,
        "completed_at": utcnow(),
        "scenario_sha256": digest(scenario),
        "policy_sha256": digest(policy),
        "control": results["control"],
        "evidence_assisted": results["evidence_assisted"],
        "decision_delta": delta,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
