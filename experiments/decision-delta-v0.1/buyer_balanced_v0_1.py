#!/usr/bin/env python3
"""Frozen-shape Decision Delta buyer adapter for Balanced v0.1.

Reads one condition payload from stdin and emits one structured decision object.
It performs no network calls and no payments. Candidate relevance order is the
frozen external order supplied by the scenario. The treatment condition may use
the frozen evidence snapshot; the control condition never receives it.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from typing import Any


def money(value: Any) -> Decimal:
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"invalid monetary value: {value!r}") from exc


def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def evidence_age_ok(summary: dict[str, Any], max_days: float, now: datetime) -> tuple[bool, str]:
    last = parse_time(summary.get("last_verified"))
    if last is None:
        return False, "EVIDENCE_AGE_UNKNOWN"
    age = (now - last).total_seconds() / 86400
    if age > max_days:
        return False, "EVIDENCE_TOO_OLD"
    return True, "EVIDENCE_FRESH_ENOUGH"


def evaluate_candidate(
    candidate: dict[str, Any],
    *,
    condition: str,
    evidence: dict[str, Any] | None,
    policy: dict[str, Any],
    task_requirements: dict[str, Any],
    task_budget: Decimal,
    now: datetime,
) -> tuple[str, list[str]]:
    reasons: list[str] = []

    max_service = money(policy["budget"]["max_service_price_usdc"])
    price = money(candidate["price_usdc"])
    if price > min(max_service, task_budget):
        return "not_eligible", ["PRICE_ABOVE_BUDGET"]
    reasons.append("PRICE_WITHIN_BUDGET")

    allowed_networks = {str(x) for x in policy["payment"]["allowed_networks"]}
    if str(candidate["network"]) not in allowed_networks:
        return "not_eligible", reasons + ["PAYMENT_NETWORK_NOT_ALLOWED"]
    reasons.append("PAYMENT_NETWORK_ALLOWED")

    # In control, evidence is deliberately unavailable. This is equivalent to an
    # evidence-unknown candidate under the same buyer-owned policy, not to a bad service.
    known = condition == "evidence_assisted" and isinstance(evidence, dict) and evidence.get("known") is True
    if not known:
        cap = money(policy["unknown_service"]["exploratory_cap_usdc"])
        handling = policy["unknown_service"]["handling"]
        if handling == "allow_below_exploratory_cap" and price <= cap:
            # A task that explicitly requires deterministic correctness cannot be
            # satisfied merely by absence of contrary evidence.
            if task_requirements.get("deterministic_correctness_required") is True:
                return "review", reasons + ["CORRECTNESS_EVIDENCE_REQUIRED_BUT_UNKNOWN"]
            return "eligible", reasons + ["UNKNOWN_ALLOWED_WITHIN_EXPLORATORY_CAP"]
        return "review", reasons + ["UNKNOWN_ABOVE_EXPLORATORY_CAP"]

    reasons.append("PUBLISHED_EVIDENCE_PRESENT")
    summary = evidence.get("evidence_summary")
    if not isinstance(summary, dict):
        return "review", reasons + ["EVIDENCE_SUMMARY_MISSING"]

    req = policy["known_evidence_requirements"]
    if bool(req.get("require_paid_evidence", False)) and int(summary.get("paid_tests") or 0) < 1:
        return "not_eligible", reasons + ["PAID_EVIDENCE_REQUIRED"]

    if int(summary.get("successful_fulfilments") or 0) < int(req["minimum_successful_fulfilments"]):
        return "not_eligible", reasons + ["MINIMUM_SUCCESSFUL_FULFILMENTS_NOT_MET"]
    reasons.append("MINIMUM_SUCCESSFUL_FULFILMENTS_MET")

    if int(summary.get("failed_fulfilments") or 0) > int(req["maximum_failed_fulfilments"]):
        return "not_eligible", reasons + ["MAXIMUM_FAILED_FULFILMENTS_EXCEEDED"]
    reasons.append("FAILED_FULFILMENTS_WITHIN_POLICY")

    fresh, freshness_reason = evidence_age_ok(summary, float(req["max_evidence_age_days"]), now)
    reasons.append(freshness_reason)
    if not fresh:
        return "review", reasons

    if task_requirements.get("deterministic_correctness_required") is True:
        correctness = policy["deterministic_correctness"]
        if int(summary.get("successful_assertion_evaluations") or 0) < int(
            correctness["minimum_successful_assertion_evaluations"]
        ):
            return "not_eligible", reasons + ["MINIMUM_CORRECTNESS_EVIDENCE_NOT_MET"]
        if int(summary.get("failed_assertion_evaluations") or 0) > int(
            correctness["maximum_failed_assertion_evaluations"]
        ):
            return "not_eligible", reasons + ["FAILED_CORRECTNESS_EVIDENCE_EXCEEDS_POLICY"]
        reasons.append("DETERMINISTIC_CORRECTNESS_POLICY_MET")

    return "eligible", reasons


def decide(payload: dict[str, Any]) -> dict[str, Any]:
    condition = str(payload["condition"])
    if condition not in {"control", "evidence_assisted"}:
        raise ValueError("invalid condition")
    policy = payload["policy"]
    candidates = payload["candidates"]
    evidence_snapshot = payload.get("evidence_snapshot") if condition == "evidence_assisted" else {}
    if not isinstance(evidence_snapshot, dict):
        evidence_snapshot = {}
    task_requirements = payload.get("task_requirements") or {}
    task_budget = money(payload["budget_usdc"])

    # The scenario snapshot time is deliberately supplied to the buyer adapter by
    # the runner payload when scenarios are frozen. Until then use current UTC.
    now_value = payload.get("decision_time")
    now = parse_time(now_value) or datetime.now(timezone.utc)

    evaluations: list[tuple[dict[str, Any], str, list[str]]] = []
    for candidate in candidates:
        cid = str(candidate["candidate_id"])
        status, reasons = evaluate_candidate(
            candidate,
            condition=condition,
            evidence=evidence_snapshot.get(cid),
            policy=policy,
            task_requirements=task_requirements,
            task_budget=task_budget,
            now=now,
        )
        evaluations.append((candidate, status, reasons))

    # Preserve the frozen external discovery order. Evidence controls eligibility;
    # it does not create a new Atinamos relevance ranking.
    for candidate, status, reasons in evaluations:
        if status == "eligible":
            return {
                "action": "BUY",
                "selected_candidate_id": candidate["candidate_id"],
                "reason_codes": ["FIRST_EXTERNALLY_RANKED_ELIGIBLE_CANDIDATE", *reasons],
                "notes": [],
            }

    if any(status == "review" for _, status, _ in evaluations):
        review_reasons = [
            reason
            for _, status, reasons in evaluations
            if status == "review"
            for reason in reasons
        ]
        return {
            "action": "REVIEW",
            "selected_candidate_id": None,
            "reason_codes": ["NO_ELIGIBLE_CANDIDATE_REVIEW_REQUIRED", *list(dict.fromkeys(review_reasons))],
            "notes": [],
        }

    rejected = [reason for _, _, reasons in evaluations for reason in reasons]
    return {
        "action": "ABSTAIN",
        "selected_candidate_id": None,
        "reason_codes": ["NO_ELIGIBLE_CANDIDATE", *list(dict.fromkeys(rejected))],
        "notes": [],
    }


def main() -> int:
    payload = json.load(sys.stdin)
    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")
    print(json.dumps(decide(payload), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
