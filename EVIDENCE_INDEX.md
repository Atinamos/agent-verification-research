# Atinamos Public Evidence Index

**Published:** 23 August 2026

> **You can pay to be tested. You cannot pay to be trusted.**

This index links the public technical evidence produced from Atinamos direct verification observations.

Each entry is a timestamped record of one tested machine-service invocation. It is not a permanent provider rating or certification.

| Date | Service | Settlement | Fulfilment | Output validation | Classification |
| --- | --- | --- | --- | --- | --- |
| 22 Aug 2026 | x402Node — JSON Repair | 0.006 USDC observed | observed | 4/4 assertions passed | `settled_fulfilment_valid` |
| 22 Aug 2026 | x402.direct — Service Directory Search | no 0.001 USDC settlement observed after authorised paid-path failure | not observed; HTTP 500 | not reached | `pre_settlement_paid_path_failure` |
| 22 Aug 2026 | x402engine — Web Screenshot | 0.01 USDC observed | observed; HTTP 200 | screenshot artefact failed strict base64/PNG validation | `settled_fulfilment_contract_invalid` |

## x402Node — JSON Repair

- [Technical experiment record](experiments/2026-08-22-x402node-json-repair/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402node-json-repair/verification-receipt.json)
- Human-readable study: `https://verify.atinamos.co.uk/studies/study-x402node-json-repair/`

**Supports:** this specific paid invocation settled, returned fulfilment and passed the four published checks.

**Does not support:** permanent reliability or provider-wide trustworthiness.

## x402.direct — Service Directory Search

- [Technical experiment record](experiments/2026-08-22-x402direct-search/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402direct-search/verification-receipt.json)
- Human-readable study: `https://verify.atinamos.co.uk/studies/study-x402direct-search/`

**Supports:** this observed authorised paid path failed before successful fulfilment and without observed settlement.

**Does not support:** that x402.direct always fails, that payment was taken without delivery, or that the observed whitespace anomaly caused the HTTP 500.

## x402engine — Web Screenshot

- [Technical experiment record](experiments/2026-08-22-x402engine-web-screenshot/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402engine-web-screenshot/verification-receipt.json)
- Human-readable study: `https://verify.atinamos.co.uk/studies/study-x402engine-web-screenshot/`

**Supports:** this invocation settled and returned a response, but the primary purchased screenshot artefact failed the published validation check.

**Does not support:** that x402engine always returns invalid screenshots or that the provider as a whole is unsafe or untrustworthy.

## Interpretation and format

- [Evidence & Classification Methodology v1.0](methodology/evidence-and-classification.md)
- [Public Verification Receipt Specification v1.0](specifications/public-verification-receipt-v1.md)
- [Verification Receipt v1 JSON Schema](schemas/verification-receipt-v1.schema.json)

The evidence chain is deliberately separated:

```text
payment contract observed
→ authorization created
→ authorised request sent
→ settlement observed
→ fulfilment observed
→ output contract validated
```

A later stage is never inferred simply because an earlier stage succeeded.

## Provenance rule

The three entries above are derived from Atinamos direct verification observations backed by retained internal evidence and sanitised public receipts.

Material obtained from external registries, marketplaces, payment systems or third-party evidence sources must be labelled as externally sourced and must not be presented as an Atinamos direct observation.

If Atinamos has no relevant observation for a service, the correct statement is: **Atinamos holds no evidence.**
