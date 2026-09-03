# Atinamos Public Evidence Index

**Published:** 23 August 2026  
**Updated:** 3 September 2026

> **You can pay to be tested. You cannot pay to be trusted.**

This index links the public technical evidence produced from Atinamos direct verification observations.

Each direct-verification entry is a timestamped record of one tested machine-service invocation. It is not a permanent provider rating or certification.

| Date | Service | Settlement | Fulfilment | Output validation | Classification |
| --- | --- | --- | --- | --- | --- |
| 22 Aug 2026 | x402Node — JSON Repair | 0.006 USDC observed | observed | 4/4 assertions passed | `settled_fulfilment_valid` |
| 22 Aug 2026 | x402.direct — Service Directory Search | no 0.001 USDC settlement observed after authorised paid-path failure | not observed; HTTP 500 | not reached | `pre_settlement_paid_path_failure` |
| 22 Aug 2026 | x402engine — Web Screenshot | 0.01 USDC observed | observed; HTTP 200 | screenshot artefact failed strict base64/PNG validation | `settled_fulfilment_contract_invalid` |

## Active assurance test — code402 LEI Check

Phase 1 was completed on 3 September 2026 with **no payment made**.

Atinamos independently observed:

```text
POST https://code402.dev/v1/tools/lei-check/call
HTTP 402
header x402Version: 2
scheme: exact
network: eip155:8453
amount: 999 atomic USDC
asset: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
recipient: 0xc59c85e661d34084a7769f955d17fd38254a6235
timeout: 300 seconds
```

A preceding free-tier response stated:

```text
scope: structure+checksum only
```

and included an XDR-1 receipt. Receipt-signature verification and paid fulfilment remain pending.

- [Technical experiment record](experiments/2026-09-03-code402-lei-check/README.md)
- [Machine-readable Phase-1 evidence](experiments/2026-09-03-code402-lei-check/evidence.json)
- Human-readable study: `https://verify.atinamos.co.uk/studies/study-code402-lei-check/`

**Classification:** `payment_contract_observed`

**Supports:** this exact live payment contract and scope representation were independently observed at the stated time.

**Does not support:** paid settlement, paid fulfilment, independently verified checksum correctness, verified XDR-1 authenticity or permanent trustworthiness.

This active pre-payment record is intentionally not inserted into the completed paid-verification table above.

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

## Related autonomous-buyer milestone — Proof #3

Proof #3 is intentionally indexed separately from the direct-verification table above because it is a **buyer/procurement experiment**, not another provider-wide verification classification.

On 28 August 2026, an Atinamos-operated buyer completed:

```text
external marketplace discovery
→ exact-route non-paying preflight
→ published Atinamos evidence lookup
→ buyer-owned procurement policy
→ autonomous seller selection
→ bounded x402 payment
→ seller fulfilment
→ exact result validation
```

The final buyer selected Keyronne JSON Repair, paid 0.001 USDC on Base and exactly validated the purchased semantic result. The clean final receipt recorded `proof3_complete = true`.

- [Proof #3 research note](research/2026-08-28-proof3-autonomous-buyer.md)
- [Proof #3 experiment record](experiments/2026-08-28-proof3-autonomous-buyer/README.md)
- [Sanitised final buyer receipt](experiments/2026-08-28-proof3-autonomous-buyer/public-receipt.json)

This supports the controlled Atinamos autonomous-buyer sequence. It does not establish unrelated external-agent adoption, permanent seller reliability or a universal trust verdict.

## External market-adoption milestone — first confirmed commercial purchase

Later on 28 August 2026, Atinamos observed an unrelated external client complete a paid x402 purchase of **Atinamos JSON Repair**.

The retained evidence records:

```text
external POST /agent/json-repair → 402 Payment Required
→ Coinbase x402 verify → 200 OK
→ Coinbase x402 settle → 200 OK
→ paid POST /agent/json-repair → 200 OK
→ 0.005 USDC Base settlement observed
```

Transaction:

```text
0x00482f136e90f01053699dd6c48b8c0e6e7f0b3598510c83654a1b77a562316b
```

The event was checked against the documented controlled Atinamos buyer/test flows and was not identified as one of them. The public record redacts the external source IP and omits Atinamos payment-recipient account details.

- [Research note](research/2026-08-28-first-external-commercial-purchase.md)
- [Sanitised experiment record](experiments/2026-08-28-external-json-repair-purchase/README.md)
- [Sanitised machine-readable evidence](experiments/2026-08-28-external-json-repair-purchase/public-evidence.json)
- Human-readable research: `https://verify.atinamos.co.uk/research/first-external-commercial-purchase/`

**Supports:** confirmed external commercial use of an Atinamos paid service, successful x402 verification and settlement, and successful HTTP fulfilment.

**Does not support:** that the external buyer was definitely an independently autonomous AI agent, that an AI system made the procurement decision, or that a particular marketplace caused the purchase.

This milestone is intentionally kept outside the direct-verification provider table because it is a **market-adoption observation about Atinamos itself**, not an Atinamos verification classification of its own service.

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

The completed direct-verification entries above are derived from Atinamos direct verification observations backed by retained internal evidence and sanitised public receipts. The code402 Phase-1 entry is also a direct observation, but is explicitly marked as pre-payment evidence until later stages are completed.

Material obtained from external registries, marketplaces, payment systems or third-party evidence sources must be labelled as externally sourced and must not be presented as an Atinamos direct observation.

If Atinamos has no relevant observation for a service, the correct statement is: **Atinamos holds no evidence.**
