# Atinamos Agent Verification Research

Public research, schemas and technical evidence for Atinamos independent verification of paid AI agent services.

**Human-readable research:** https://verify.atinamos.co.uk  
**Technical evidence:** this repository

> **You can pay to be tested. You cannot pay to be trusted.**

## Purpose

This repository is the public technical publication layer for Atinamos Verification.

It exists to publish selected, sanitised material that helps developers, researchers, buyer agents, marketplaces and registries understand and consume Atinamos evidence.

Atinamos produces evidence. Trust is the conclusion the buyer reaches from that evidence.

## Public evidence index

- [Atinamos Public Evidence Index](EVIDENCE_INDEX.md) — one place to review the currently published direct verification observations, classifications, study links and technical receipts.

## Methodology and specifications

- [Evidence & Classification Methodology v1.0](methodology/evidence-and-classification.md) — defines observable evidence stages, current public classifications, unknown-evidence handling and interpretation rules.
- [Public Verification Receipt Specification v1.0](specifications/public-verification-receipt-v1.md) — explains every public receipt field, null/unknown semantics, buyer interpretation and sanitisation boundaries.
- [Public Verification Receipt v1 JSON Schema](schemas/verification-receipt-v1.schema.json) — machine-readable receipt contract.

## Published evidence

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
- private filesystem or host details;
- unpublished anti-abuse techniques;
- internal challenge-generation logic;
- private operational documentation;
- material that would materially assist gaming of verification.

GitHub is not where Atinamos Verification runs. It is where Atinamos publishes selected technical evidence about what the verifier observed.

## Repository structure

- `schemas/` — public machine-readable evidence schemas.
- `examples/` — sanitised example requests, responses and receipts.
- `methodology/` — public verification methodology and evidence interpretation.
- `experiments/` — deliberately published experiment records.
- `datasets/` — deliberately published public datasets.
- `specifications/` — public technical specifications and interfaces.

See `PUBLICATION_POLICY.md` before adding any material.

## Licensing

Copyright © 2026 MotionFil-AI.

- Research, methodology, written evidence, findings, specifications and datasets are licensed under **CC BY 4.0** unless a file states otherwise.
- Schemas, machine-readable receipts/examples and future source code are licensed under the **MIT License** unless a file states otherwise.

See [LICENSE.md](LICENSE.md) for the full split-licence terms and suggested attribution.

## Human-readable research

The canonical human-readable publication layer is **verify.atinamos.co.uk**. Public website findings may link to supporting technical material in this repository where useful.
