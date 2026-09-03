# Atinamos Agent Verification Research

Public research, schemas and technical evidence for Atinamos independent verification of paid AI agent services.

**Human-readable research:** https://verify.atinamos.co.uk  
**Technical evidence:** this repository

> **You can pay to be tested. You cannot pay to be trusted.**

## Purpose

This repository is the public technical publication layer for Atinamos Verification.

It exists to publish selected, sanitised material that helps developers, researchers, buyer agents, marketplaces and registries understand and consume Atinamos evidence and public machine-service interfaces.

Atinamos produces evidence. Trust is the conclusion the buyer reaches from that evidence.

## Proof #3 — autonomous buyer milestone

**COMPLETE — 28 August 2026.**

An Atinamos-operated bounded buyer was given a task, a maximum spend and a risk policy. It independently searched Coinbase/x402 Bazaar, checked exact invocation-route viability, queried already-published Atinamos evidence, applied its own procurement policy, selected an external seller without a human naming the seller, made a bounded x402 payment, consumed the result and exactly validated the purchased output.

Final clean run:

```text
selected seller: Keyronne JSON Repair
payment: 0.001 USDC on Base
x402: v2 / exact
paid HTTP status: 200
settlement: observed successful
output: exact semantic match
proof3_complete: true
```

The research record deliberately retains the earlier autonomous no-purchase, route-identity issue and first paid validator-envelope failure rather than presenting only the final successful run.

- [Proof #3 public research note](research/2026-08-28-proof3-autonomous-buyer.md)
- [Proof #3 experiment record](experiments/2026-08-28-proof3-autonomous-buyer/README.md)
- [Sanitised final buyer receipt](experiments/2026-08-28-proof3-autonomous-buyer/public-receipt.json)

This proves the controlled Atinamos buyer experiment. It does **not** prove unrelated external-agent adoption of Atinamos, a universal safe/unsafe verdict or permanent provider reliability.

## Public evidence index

- [Atinamos Public Evidence Index](EVIDENCE_INDEX.md) — one place to review the currently published direct verification observations, classifications, study links and technical receipts.

## Public Evidence MCP

AI agents and developers can query selected published Atinamos evidence through the read-only Atinamos Evidence MCP.

**Endpoint:** `https://verify.atinamos.co.uk/mcp`

- [MCP documentation and index](mcp/README.md)
- [Quick start](mcp/QUICKSTART.md)
- [Tool reference](mcp/TOOLS.md)
- [Buyer policy reference](mcp/BUYER_POLICY.md)
- [Security and scope](mcp/SECURITY.md)

The MCP exposes deliberately published evidence and caller-supplied policy evaluation. It does not expose wallet access, payment signing, verification-triggering writes, the full private harvest registry or a universal trust verdict.

## Public Market Search

Atinamos now exposes a bounded, read-only search projection of the wider machine-service harvest registry.

**Search:** `GET https://verify.atinamos.co.uk/v1/market/search?q=<query>&limit=<1-50>`  
**Service detail:** `GET https://verify.atinamos.co.uk/v1/market/service/<service_id>`

- [Market Search documentation](market/README.md)

Market Search reports services observed by Atinamos harvesters, their source provenance and `last_observed_at`. Observation does not establish current availability, safety, trust or independent verification. **UNKNOWN is not UNSAFE.**

Market Search and the Evidence MCP are intentionally different surfaces: Market Search supports discovery across a bounded public projection of the harvested registry; Evidence MCP exposes selected published verification evidence. A Market Search result does not imply that published verification evidence exists for that service.

The private PostgreSQL database remains private. The public Verify deployment reaches Market Search through a bounded GET-only proxy rather than receiving database credentials.

## Methodology and specifications

- [Evidence & Classification Methodology v1.0](methodology/evidence-and-classification.md) — defines observable evidence stages, current public classifications, unknown-evidence handling and interpretation rules.
- [Public Verification Receipt Specification v1.0](specifications/public-verification-receipt-v1.md) — explains every public receipt field, null/unknown semantics, buyer interpretation and sanitisation boundaries.
- [Public Verification Receipt v1 JSON Schema](schemas/verification-receipt-v1.schema.json) — machine-readable receipt contract.

## Public research notes

### 28 August 2026 — Proof #3 Autonomous Buyer

A controlled buyer experiment completed the full external-discovery → evidence → policy → selection → payment → fulfilment-validation sequence without a human naming the seller. The same research trail also exposed useful failure modes: autonomous no-purchase when evidence was absent, endpoint transcription/identity drift, marketplace routes returning 404/405, live price drift, paid-but-invalid fulfilment, and a buyer-side validator-envelope defect that was fixed and rerun rather than hidden.

- [Proof #3 — A Bounded Autonomous Buyer With External Discovery](research/2026-08-28-proof3-autonomous-buyer.md)

### 24 August 2026 — Machine-Service Market Snapshot

At snapshot time the private Atinamos evidence catalogue contained 60,234 canonical machine services, 69,220 resolved marketplace/source records and 71,817 longitudinal source observations. The underlying PostgreSQL registry remains private; since 27 August 2026 a bounded read-only public projection can be searched through Atinamos Market Search. The published snapshot remains a timestamped aggregate research record.

- [Machine-Service Market Snapshot — 24 August 2026](research/2026-08-24-machine-service-market-snapshot.md)
- Human-readable article: https://verify.atinamos.co.uk/research/machine-service-market-snapshot-2026-08-24/

The figures are timestamped Atinamos observations and are not presented as the total size of the global machine-service market.

### 24 August 2026 — Observed ≠ Resolved

A controlled x402.jobs ingestion test showed why an observed marketplace listing may contain useful evidence without yet establishing a canonical executable service identity. Atinamos retained unresolved listings rather than inventing missing HTTP methods.

- [Observed ≠ Resolved: Why a Marketplace Listing Is Not Yet a Canonical Machine Contract](research/2026-08-24-observed-does-not-mean-resolved.md)
- Human-readable article: https://verify.atinamos.co.uk/research/observed-does-not-mean-resolved/

The controlled sample was 10 listings and is not presented as an estimate of the full x402.jobs catalogue.

## Published evidence

### 3 September 2026 — code402 LEI Check assurance series

Atinamos completed a four-observation independent assurance series for `POST https://code402.dev/v1/tools/lei-check/call`.

The series retained the original payment-contract observation, two bounded EOA purchases whose positive and negative checksum results matched independent ISO 7064 MOD-97-10 expectations, and one Circle smart-account payment-path interoperability observation.

The two EOA purchases settled **999 atomic USDC** and **1371 atomic USDC** on Base. Both paid XDR-1 receipt signatures independently recovered to the published receipt signer, and both receipts' input/output hashes matched the exact paid inputs and returned results.

The Circle smart-account authorization did not settle. It independently validated under EIP-1271, but code402 rejected the request because ordinary signature recovery did not recover to the smart-account `from` address. This is recorded as a pre-settlement payment interoperability issue rather than a failed fulfilment.

Current live evidence summary:

```text
observations: 4
paid tests: 2
successful fulfilments: 2
failed fulfilments: 0
payment interoperability issues: 1
```

- [Completed technical experiment record](experiments/2026-09-03-code402-lei-check/README.md)
- [Completed machine-readable evidence series](experiments/2026-09-03-code402-lei-check/evidence.json)
- [Preserved original Phase-1 evidence](experiments/2026-09-03-code402-lei-check/evidence-phase1.json)

**Supports:** these timestamped payment-contract, settlement, deterministic-output, receipt-verification and interoperability observations.

**Does not support:** LEI registry existence, permanent reliability, provider-wide trustworthiness, universal smart-account incompatibility or a universal purchase recommendation.

### 22 August 2026 — x402Node JSON Repair

Atinamos independently exercised and paid the externally owned x402Node JSON Repair service, observed fulfilment and checked four objective output assertions. All four passed.

- [Technical experiment record](experiments/2026-08-22-x402node-json-repair/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402node-json-repair/verification-receipt.json)

**Classification:** `settled_fulfilment_valid`

### 22 August 2026 — x402.direct Service Directory Search

Atinamos observed a live x402 v1 payment requirement, recorded a malformed `payTo` field, created and sent the payment authorization, and received HTTP 500 on the authorised request. A subsequent read-only chain reconciliation found no 0.001 USDC settlement, and no fulfilment result was returned.

- [Technical experiment record](experiments/2026-08-22-x402direct-search/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402direct-search/verification-receipt.json)

**Classification:** `pre_settlement_paid_path_failure`

### 22 August 2026 — x402engine Web Screenshot

Atinamos paid 0.01 USDC for the externally owned Web Screenshot service. Settlement was observed and the paid request returned HTTP 200 with metadata matching the controlled target, but the primary screenshot value failed strict base64/PNG validation.

- [Technical experiment record](experiments/2026-08-22-x402engine-web-screenshot/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402engine-web-screenshot/verification-receipt.json)

**Classification:** `settled_fulfilment_contract_invalid`

These are timestamped observations, not permanent trust ratings. Successful and unsuccessful observations are deliberately retained.

## This repository may contain

- public evidence schemas;
- sanitised verification receipts;
- sample API responses;
- public Market Search interface documentation;
- methodology suitable for technical scrutiny;
- experiment datasets selected for publication;
- public research Markdown;
- integration and buyer evidence-query examples;
- public specifications;
- later, potentially a small open-source evidence client.

## This repository does not contain

- Atinamos operational source code;
- verifier implementation;
- Render Check implementation;
- credentials, secrets or wallet material;
- private infrastructure information;
- the private PostgreSQL registry;
- raw private source payloads;
- unpublished anti-abuse techniques;
- internal challenge-generation logic;
- private operational documentation;
- material that would materially assist gaming of verification.

GitHub is not where Atinamos Verification runs. It is where Atinamos publishes selected technical evidence and documentation for its public machine interfaces.

## Repository structure

- `mcp/` — public Atinamos Evidence MCP endpoint documentation, tool reference, buyer-policy schema and tested examples.
- `market/` — public Market Search endpoint, scope and interpretation documentation.
- `schemas/` — public machine-readable evidence schemas.
- `examples/` — sanitised example requests, responses and receipts.
- `methodology/` — public verification methodology and evidence interpretation.
- `experiments/` — deliberately published experiment records.
- `datasets/` — deliberately published public datasets.
- `research/` — public technical research notes derived from controlled Atinamos observations.
- `specifications/` — public technical specifications and interfaces.

See `PUBLICATION_POLICY.md` before adding any material.

## Licensing

Copyright © 2026 MotionFil-AI.

- Research, methodology, written evidence, findings, specifications and datasets are licensed under **CC BY 4.0** unless a file states otherwise.
- Schemas, machine-readable receipts/examples and future source code are licensed under the **MIT License** unless a file states otherwise.

See [LICENSE.md](LICENSE.md) for the full split-licence terms and suggested attribution.

## Human-readable research

The canonical human-readable publication layer is **verify.atinamos.co.uk**. Public website findings may link to supporting technical material in this repository where useful.
