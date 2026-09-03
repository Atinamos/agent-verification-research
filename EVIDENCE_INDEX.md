# Atinamos Public Evidence Index

**Published:** 23 August 2026  
**Updated:** 3 September 2026

> **You can pay to be tested. You cannot pay to be trusted.**

This index links the public technical evidence produced from Atinamos direct verification observations.

Each direct-verification entry is a timestamped record of tested machine-service behaviour. It is not a permanent provider rating or certification.

| Date | Service | Settlement | Fulfilment | Output validation | Classification |
| --- | --- | --- | --- | --- | --- |
| 22 Aug 2026 | x402Node — JSON Repair | 0.006 USDC observed | observed | 4/4 assertions passed | `settled_fulfilment_valid` |
| 22 Aug 2026 | x402.direct — Service Directory Search | no 0.001 USDC settlement observed after authorised paid-path failure | not observed; HTTP 500 | not reached | `pre_settlement_paid_path_failure` |
| 22 Aug 2026 | x402engine — Web Screenshot | 0.01 USDC observed | observed; HTTP 200 | screenshot artefact failed strict base64/PNG validation | `settled_fulfilment_contract_invalid` |

## Completed assurance series — code402 LEI Check

On 3 September 2026 Atinamos completed a four-observation assurance series for:

```text
POST https://code402.dev/v1/tools/lei-check/call
```

Current live evidence summary:

```text
observations: 4
paid tests: 2
successful fulfilments: 2
failed fulfilments: 0
payment interoperability issues: 1
```

### Contract and scope

The authoritative pre-payment observation recorded x402 v2 in the payment header, `exact`, Base `eip155:8453`, 999 atomic USDC at that time, Base USDC asset `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`, recipient `0xc59c85e661d34084a7769f955d17fd38254a6235` and a 300-second timeout.

The service result scope remained:

```text
structure+checksum only
```

No registry-existence claim is inferred.

### Two settled deterministic paid controls

Atinamos independently precomputed:

```text
529900T8BM49AURSDO55 → MOD-97 remainder 1 → expected valid=true
529900T8BM49AURSDO56 → MOD-97 remainder 2 → expected valid=false
```

The first EOA purchase settled **999 atomic USDC** on Base and returned `valid=true` as expected.

Transaction:

```text
0xf0213ebd5c8fcbe8fc41d03663cf6c2b5043117b361d523b41d821a1b98ae64b
```

The second EOA purchase was authorised up to **1391 atomic USDC**; dynamic pricing decayed before settlement and **1371 atomic USDC** settled. The service returned `valid=false` / `checksum failed` as independently expected.

Transaction:

```text
0x5fe5fb57fa4e19cddc82c5c728e0eda5d110d41f9afd5d436a52f1a39c16d40c
```

For both paid controls, the XDR-1 receipt signature independently recovered to the published signer and the receipt input/output hashes matched the exact tested input and returned result.

### Circle smart-account interoperability observation

A separate Circle smart-contract buyer submitted a 999-atomic-USDC authorization. code402 rejected it before settlement with `BAD_SIGNATURE`, reporting that the voucher signature did not recover to the declared `from` address.

Atinamos independently checked the exact authorization against the buyer contract. EIP-1271 `isValidSignature` returned the magic value `0x1626ba7e`, while Base USDC authorization state for the exact nonce remained unused.

The current Evidence API classifies this specifically as:

```text
pre_settlement_payment_interoperability_failure
```

This is not counted as a failed fulfilment because settlement and paid fulfilment were never reached. It does not establish that the Circle signature was invalid or that code402 is universally incompatible with smart accounts.

### Retained receipt limitation

The paid XDR-1 receipt signatures were independently verified, but the accompanying seller-wallet authorization object contained an empty `attestation_sig`. Atinamos therefore does not claim to have independently cryptographically verified seller-wallet delegation to the receipt signer.

- [Completed technical experiment record](experiments/2026-09-03-code402-lei-check/README.md)
- [Completed machine-readable evidence series](experiments/2026-09-03-code402-lei-check/evidence.json)
- [Original preserved Phase-1 evidence](experiments/2026-09-03-code402-lei-check/evidence-phase1.json)
- Human-readable study: `https://verify.atinamos.co.uk/studies/study-code402-lei-check/`
- Live evidence: `https://verify.atinamos.co.uk/v1/evidence?endpoint=https%3A%2F%2Fcode402.dev%2Fv1%2Ftools%2Flei-check%2Fcall&method=POST`

**Supports:** the exact timestamped contract observation, two settled deterministic paid EOA controls with independently verified outputs and receipt binding, plus the observed Circle smart-account pre-settlement interoperability issue.

**Does not support:** LEI registry existence, permanent reliability, provider-wide trustworthiness, universal smart-account incompatibility or a universal purchase recommendation.

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

The direct-verification entries above are derived from Atinamos observations backed by retained internal evidence and sanitised public records. The code402 section is an evidence series rather than a single invocation and intentionally preserves both successful and problematic observations.

Material obtained from external registries, marketplaces, payment systems or third-party evidence sources must be labelled as externally sourced and must not be presented as an Atinamos direct observation.

If Atinamos has no relevant observation for a service, the correct statement is: **Atinamos holds no evidence.**
