# Atinamos Evidence & Classification Methodology

**Status:** Public methodology  
**Version:** 1.0  
**Published:** 23 August 2026  
**Updated:** 6 September 2026

> **You can pay to be tested. You cannot pay to be trusted.**

Atinamos produces evidence about observed machine-service behaviour. It does not assign a universal trust score and it does not tell every buyer what decision to make.

A buyer, marketplace, registry or agent can use Atinamos evidence as one input to its own procurement policy.

## Core principle

A successful payment is not the same thing as successful delivery, and a successful HTTP response is not the same thing as a valid purchased result.

Atinamos therefore separates a paid machine-service interaction into distinct observable stages:

```text
seller offer
    ↓
payment contract observed
    ↓
payment authorization created
    ↓
authorised request sent
    ↓
settlement observed
    ↓
fulfilment observed
    ↓
output contract validated
```

Evidence is recorded at the furthest stage actually supported by the observation. Later stages are never inferred merely because an earlier stage succeeded.

## Evidence stages

### 1. Seller offer

The seller's public proposition is identified where practical: what service is being sold, what useful result is promised, and any material output format or behaviour that can be objectively tested.

The offer is not treated as evidence that the service works. It defines the proposition against which an observation may be evaluated.

### 2. Payment contract observed

Atinamos records the live machine-facing payment requirement presented by the endpoint, including relevant fields such as protocol version, payment scheme, network and observed amount.

Where a machine-contract anomaly is observed, it may be preserved as evidence. Recording an anomaly does not by itself establish that the anomaly caused a later failure.

### 3. Payment authorization created

This stage means the buyer/verifier was able to construct the authorization required by the observed payment contract.

It does not mean settlement occurred.

### 4. Authorised request sent

This stage means the payment-bearing or otherwise authorised request was sent to the service.

It still does not establish settlement, fulfilment or valid output.

### 5. Settlement observed

Settlement is treated separately from application-layer success. Where available, Atinamos may retain payment-response evidence, transaction references, chain reconciliation or other objective evidence sufficient to support the observed settlement state.

`settlement_observed = true` means evidence supports that value transfer occurred for the observation.

`settlement_observed = false` means evidence supports that no settlement was observed for the tested transaction path.

A missing or unresolved settlement state must not be silently converted into either result.

### 6. Fulfilment observed

Fulfilment means the service returned or completed a result corresponding to the paid request.

HTTP 200 alone is not automatically treated as valid fulfilment of the useful seller proposition. The returned result must still be evaluated against the relevant output contract where objective assertions are available.

### 7. Output contract validated

The returned result is checked against explicit assertions tied to the useful thing the seller offered.

Examples may include:

- required structured fields and values;
- file or artefact signatures;
- expected content type or representation;
- service-specific but objectively testable output conditions.

Atinamos records assertion outcomes rather than converting them into a broad judgement about the provider.

## Scope of independent validation

An independent correctness check applies only to the capability, field, artefact or condition actually tested.

For example, if a service returns:

```text
valid
bic
bank_code
sepa
issuer
risk_indicators
```

and Atinamos independently checks only `valid`, then the correct publication claim is that `valid` was independently checked under the stated method and fixture.

The other returned fields may have been observed, but they must not be promoted to independently verified evidence unless a separate check supports that stronger claim.

The same rule applies to service-level language: verifying an IBAN checksum field does not by itself verify every enrichment capability offered by an IBAN API.

## Observation counts are not reliability percentages

Atinamos may publish counts such as:

```text
successful_fulfilments: 3
failed_fulfilments: 0
```

Those values describe the published observation sample.

They must not be restated by Atinamos as:

```text
100% reliable
```

unless a separate statistical methodology and evidence basis explicitly supports such an estimate.

The correct interpretation is narrower:

> Three seller-attributable successful fulfilments were observed in the published sample and no seller-attributable failed fulfilment was present in that same sample.

Future behaviour remains unestablished.

## Failure and interoperability attribution

Not every unsuccessful path is seller-performance evidence.

Where the evidence supports it, Atinamos distinguishes categories such as:

- seller/service fulfilment failure;
- verifier or system configuration failure;
- payment interoperability issue;
- pre-payment observation where seller performance was not exercised;
- unknown or unresolved attribution.

A verifier-side configuration failure must not be counted as a seller fulfilment failure.

A payment interoperability observation must remain scoped to the tested payment path. One smart-account or wallet-path failure does not establish universal incompatibility with every smart account, wallet implementation or payment route.

Likewise, a pre-payment observation of a payment contract is useful evidence about the contract but is not seller-performance evidence unless the paid fulfilment path was actually exercised.

## Fresh fixtures and implementation claims

Fresh or varied fixtures can reduce the value of memorising a previously known static test input.

They do not, by themselves, prove the provider's internal implementation mechanism, prove all arbitrary future inputs, or establish that verifier traffic was indistinguishable from ordinary buyer traffic.

A publication should therefore distinguish the observed result from any stronger implementation claim.

## Current public classifications

The classification describes the observed execution state of one timestamped verification. It is not a permanent provider rating.

### `payment_contract_observed`

Evidence supports that Atinamos independently captured and parsed a live payment requirement for the service route.

This classification does **not** mean a valid payment authorisation was created, payment settled, paid fulfilment occurred or the service output was correct. It is deliberately useful as a pre-payment evidence state so a buyer can distinguish **"we observed the contract"** from **"we paid and verified fulfilment"**.

### `settled_fulfilment_valid`

Evidence supports that:

- settlement occurred;
- fulfilment was observed; and
- the tested output assertions passed.

This does **not** prove permanent reliability, universal trustworthiness or future success.

### `pre_settlement_paid_path_failure`

Evidence supports that the interaction reached an authorised paid path but did not reach observed settlement or successful fulfilment.

This classification must not be described as "seller took payment and failed to deliver" unless settlement evidence actually supports that stronger statement.

### `settled_fulfilment_contract_invalid`

Evidence supports that:

- settlement occurred;
- a response or fulfilment was observed; but
- the useful purchased output did not satisfy the tested output contract.

This classification exists specifically to prevent payment settlement or HTTP 200 from being mistaken for valid delivery.

Newer Assurance evidence may also publish narrower execution or interoperability classifications. Consumers should interpret the accompanying stage, attribution, scope and limitation fields rather than treating any classification string as a provider-wide verdict.

## Timestamped observations, not permanent ratings

Every verification result is an observation of a specific service invocation at a particular time and under a defined test.

A single successful observation does not prove that a service will always succeed. A single unsuccessful observation does not prove that a provider generally fails or is unsafe.

Recency, repetition, value at risk and the buyer's own policy remain relevant.

## Unknown or absent evidence

Atinamos distinguishes **no evidence held** from negative evidence.

If Atinamos has no observation for a service, the correct interpretation is only that Atinamos currently holds no relevant evidence. It is not evidence that the service is unsafe.

Similarly, an evidence field that was not observed or could not be established should remain unknown or null rather than being inferred.

## Evidence integrity

Public verification receipts may include hashes, transaction references, timestamps, assertion outcomes, contract anomalies and other deliberately selected evidence that allows the observation to be scrutinised.

The public record is sanitised. It does not include wallet secrets, credentials, private infrastructure, verifier implementation, unpublished challenge logic or anti-gaming techniques.

Production Assurance also publishes signed Evidence Receipts with canonical signed content, content commitment, signing-key identity and explicit integrity metadata. Historical public verification-receipt v1 records remain valid evidence in the format in which they were originally published.

## Buyer decision remains external

Atinamos intentionally separates evidence generation from procurement policy.

A buyer may use the same observation to:

- proceed;
- reject;
- request a fresher verification;
- require repeated evidence;
- impose a lower spend cap;
- prefer an alternative provider;
- accept additional risk for another reason.

Those are buyer decisions, not Atinamos trust verdicts.

## Public examples

Published studies demonstrate different evidence stages and execution states:

| Observation | Settlement | Fulfilment | Output validation | Interpretation |
| --- | --- | --- | --- | --- |
| IBANforge IBAN Validate — 6 Sep 2026 | 2 paid controls independently observed on Base | 2/2 observed | returned `valid` matched independent MOD-97 expectation for both controls | signed Assurance commissioning evidence; only `valid` independently checked |
| code402 LEI Check — 3 Sep 2026 | 2 EOA payments observed; 1 smart-account path did not settle | 2 paid EOA fulfilments observed | positive and negative checksum expectations matched; separate smart-account interoperability issue | mixed evidence series; interoperability issue is not universal smart-account incompatibility |
| x402Node JSON Repair — 22 Aug 2026 | observed | observed | valid | `settled_fulfilment_valid` |
| x402.direct Search — 22 Aug 2026 | not observed | not observed | not reached | `pre_settlement_paid_path_failure` |
| x402engine Web Screenshot — 22 Aug 2026 | observed | observed | invalid | `settled_fulfilment_contract_invalid` |

The associated public evidence and experiment records are available in this repository under `experiments/`.

## Methodology limits

This public methodology explains the evidence model and interpretation rules needed to scrutinise Atinamos results.

It intentionally does not publish:

- future test cases;
- challenge selection logic;
- anti-gaming heuristics;
- private verifier implementation;
- operational infrastructure;
- wallet or credential material.

That boundary protects test independence without changing the meaning of the published evidence.

For the current machine-readable semantics review, see [Machine-Evidence Schema Audit — 6 September 2026](../research/2026-09-06-machine-evidence-schema-audit.md).
