# Atinamos Public Verification Receipt Specification v1.0

**Status:** Public technical specification  
**Version:** 1.0  
**Published:** 23 August 2026

> **You can pay to be tested. You cannot pay to be trusted.**

## Purpose

An Atinamos public verification receipt is a deliberately published, sanitised machine-readable record of **one timestamped observation of one machine service invocation**.

A receipt records evidence. It does not assign a permanent trusted/untrusted verdict to a provider.

The JSON representation is defined by:

[`schemas/verification-receipt-v1.schema.json`](../schemas/verification-receipt-v1.schema.json)

The evidence-stage and classification semantics are defined by:

[`methodology/evidence-classification-methodology-v1.md`](../methodology/evidence-classification-methodology-v1.md)

## Interpretation rule

A buyer should read the receipt as an execution history:

```text
seller offer
→ payment contract
→ authorization
→ authorised request
→ settlement
→ fulfilment
→ output validation
```

A later stage must not be inferred merely because an earlier stage succeeded.

Examples:

- HTTP 402 proves that a payment requirement was observed; it does not prove payment settled.
- A payment authorization proves that an authorization was created; it does not prove money moved.
- Settlement proves value transferred; it does not prove useful fulfilment.
- HTTP 200 proves a response was returned; it does not prove the purchased output was valid.
- A passing observation is not a permanent reputation score.

## Top-level fields

### `evidence_version`

Identifier for the public receipt format, currently:

```text
atinamos.public-verification-receipt.v1
```

Consumers should use this field for compatibility decisions rather than assuming all receipts have the same structure forever.

### `observation_id`

Stable public identifier for the published observation.

It identifies a specific evidence record, not a provider, account or long-term reputation profile.

### `observed_at`

UTC timestamp indicating when the observation began or was recorded.

Evidence ages. Buyers should apply their own freshness requirements.

### `provider`

Human-readable name of the observed provider.

Provider identity is contextual metadata. Evidence should be interpreted primarily at the service/route level.

### `service`

Human-readable name of the specific service tested.

## `request`

Describes the invocation against which the evidence applies.

### `request.endpoint`

The public endpoint used for the observation.

A receipt applies to this service route and the stated invocation; it does not imply that every endpoint operated by the provider was tested.

### `request.method`

HTTP method used for the observed invocation.

Method is material evidence. GET and POST against the same path may behave differently.

### `request.test_input_summary`

Human-readable summary of the controlled input used during the observation.

This is intentionally a summary rather than a guarantee that every raw request detail will be made public.

## `payment`

Records payment-path evidence.

### `payment.protocol`

Payment protocol observed, for example `x402`.

### `payment.version`

Observed protocol version.

### `payment.scheme`

Observed payment scheme, for example `exact`.

### `payment.network`

Network selected or observed for the payment path.

Network identifiers are preserved as observed where practical.

### `payment.amount_usdc`

USDC amount associated with the observed payment requirement or transaction.

This field does **not** by itself prove settlement. Use `settlement_observed` and, where present, `transaction`.

### `payment.initial_http_status`

HTTP status returned by the initial no-payment or pre-payment request.

For x402 observations this is commonly `402`, but the receipt format does not assume that every future payment protocol behaves identically.

### `payment.paid_http_status`

HTTP status observed after an authorised paid-path request.

`null` means no such status was available for the published observation.

A `200` value is transport/application evidence only. It does not prove the purchased output passed validation.

### `payment.authorization_created`

`true` means the verifier successfully constructed the required payment authorization.

This does not mean settlement occurred.

### `payment.authorized_request_sent`

`true` means an authorised request was actually submitted to the paid service path.

This separates authorization construction from execution.

### `payment.settlement_observed`

Three-state field:

- `true` — settlement evidence was observed;
- `false` — evidence supports that settlement did not occur for this observation;
- `null` — settlement state was not established from retained/public evidence.

**Unknown must remain unknown.** Consumers must not interpret `null` as either success or failure.

### `payment.transaction`

Public transaction identifier where settlement is represented by a publishable on-chain transaction.

`null` is valid when no transaction exists or no public transaction is available for the observation.

A transaction hash proves a transaction record exists; interpretation still depends on the other receipt fields.

## `contract_anomalies`

Optional array of machine-contract anomalies observed during the run.

Each entry contains:

- `field` — affected machine-contract field;
- `type` — narrow anomaly category;
- `description` — public explanation of what was observed.

An anomaly records evidence. Its presence does not automatically establish the cause of a later failure.

## `evidence_hashes`

Optional hashes of evidence inputs or normalized representations retained for integrity comparison.

### `payment_challenge_sha256`

SHA-256 of the retained payment challenge representation used as evidence.

### `normalized_payment_challenge_sha256`

SHA-256 of a compatibility-normalised representation when a narrow normalization was required.

Publishing both values allows the observation to preserve that a change occurred without exposing private execution mechanics.

## `fulfilment`

Records whether the seller returned or completed work and whether the useful output passed the tested contract.

### `fulfilment.observed`

`true` means fulfilment was observed in the tested invocation.

This does not automatically mean the output was valid.

### `fulfilment.output_valid`

`true` means the published assertions relevant to the purchased output passed.

`false` may mean:

- fulfilment was returned but an output assertion failed; or
- fulfilment/output validation was not successfully reached.

The `classification`, `assertions`, payment state and study record provide the necessary context.

### `fulfilment.seller_final_status`

Seller/service final status where the protocol exposes one, for example `completed`.

`null` means no final seller status was established or applicable.

## `assertions`

Array of deliberately published objective checks applied to the returned result.

Each assertion contains:

### `description`

Plain-language description of what was checked.

### `passed`

Boolean result of that check.

A receipt may contain an empty assertions array when output validation was not reached. Empty assertions must not be interpreted as a successful validation.

Public receipts expose enough information to understand the claim tested without publishing future challenge-selection logic or anti-gaming implementation.

## `response_hash_sha256`

SHA-256 of the canonical retained response representation used for the observation.

`null` is valid when no successful response suitable for hashing was obtained.

The hash is an integrity reference, not a claim that the response was correct.

## `classification`

Narrow label describing the observed execution state.

Current published classifications include:

### `settled_fulfilment_valid`

Settlement observed, fulfilment observed, and tested output assertions passed.

### `pre_settlement_paid_path_failure`

The authorised paid path failed before observed settlement and successful fulfilment.

### `settled_fulfilment_contract_invalid`

Settlement and fulfilment were observed, but the purchased output failed the tested output contract/assertions.

Future classifications may be introduced as new evidence states are demonstrated. Consumers should not hard-code an assumption that these are the only possible values forever.

A classification describes **this observation**. It is not a provider-wide trust score.

## `limitations`

Array of explicit boundaries on what the evidence supports.

Limitations are part of the receipt, not optional editorial commentary. They prevent a narrow observation being inflated into a broader claim.

Typical limitations include:

- one timestamped invocation only;
- no claim of permanent reliability;
- no provider-wide safety/untrustworthiness claim;
- no causal claim where only correlation was observed;
- no claim about outputs that were never returned or tested.

## Null, false and absent are different

Consumers must preserve these distinctions.

- `true` = evidence supports the state occurred.
- `false` = evidence supports the state did not occur or the relevant check failed.
- `null` = state was not established.
- absent optional field = that evidence dimension was not published/applicable in this receipt format.

A buyer must not convert unknown into negative evidence.

## Sanitisation boundary

Public receipts may include:

- service endpoint;
- observed payment amount/network/protocol;
- public transaction references;
- HTTP-stage observations;
- contract anomalies;
- assertion outcomes;
- evidence hashes;
- classification;
- limitations.

They intentionally do not require publication of:

- wallet private material;
- secrets or authentication material;
- internal infrastructure;
- private payer/account metadata where not necessary;
- raw payment authorization headers;
- verifier source code;
- future challenge-generation logic;
- anti-gaming heuristics;
- private operational records.

## Buyer-agent use

A buyer agent can treat the receipt as input to its own procurement policy.

Example policy actions could include:

- accept sufficiently recent `settled_fulfilment_valid` evidence;
- require a fresh observation before purchase;
- lower a spend cap after a failure observation;
- reject an execution path after `pre_settlement_paid_path_failure`;
- avoid paying for an output contract with recent `settled_fulfilment_contract_invalid` evidence;
- combine Atinamos evidence with other registries, identity systems or marketplace history.

Atinamos does not prescribe which action is correct for every buyer.

## Published examples

The public repository contains receipts demonstrating materially different states:

- x402Node JSON Repair — `settled_fulfilment_valid`;
- x402.direct Service Directory Search — `pre_settlement_paid_path_failure`;
- x402engine Web Screenshot — `settled_fulfilment_contract_invalid`.

These examples are evidence records, not certification badges.
