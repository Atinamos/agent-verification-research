# Machine-Evidence Schema Audit — 6 September 2026

**Status:** Public research note  
**Date:** 6 September 2026

> **You can pay to be tested. You cannot pay to be trusted.**

## Purpose

This note records a read-only audit of the current Atinamos machine-readable evidence surfaces after the first end-to-end external Assurance Runner commissioning run and after deliberately giving published evidence to an independent AI consumer to see how it interpreted the record.

No production behaviour, payment policy, signer, evidence record or historical receipt was changed by this audit.

The question was simple:

> Can a buyer agent read Atinamos evidence and reach the narrow conclusion actually supported by the observation without silently broadening the claim?

## What already works well

The current evidence model already separates important execution stages:

```text
seller offer
→ payment contract
→ authorisation
→ authorised request
→ settlement
→ fulfilment
→ output validation
```

The public methodology also already states that:

- evidence is timestamped rather than a permanent reputation score;
- later execution stages must not be inferred from earlier ones;
- no evidence held is not negative evidence;
- buyer procurement policy remains external to Atinamos;
- successful and unsuccessful observations are retained;
- a seller-funded test cannot buy a positive outcome.

The signed Assurance Evidence Receipt format additionally provides canonical signed payloads, content commitments, signing-key identity and integrity metadata.

## Findings from AI-consumer interpretation

### 1. Capability scope can be broadened too easily

A modern paid IBAN test independently checked only the returned `valid` field using ISO 13616 MOD-97.

An AI consumer correctly noticed that limitation, but initially described the service more broadly in terms of IBAN validation, BIC, bank-code and SEPA metadata.

The evidence did **not** independently verify those enrichment fields.

Machine-readable evidence should therefore make the distinction explicit between:

- the capability actually tested;
- the exact output field or fields independently checked;
- fields merely observed in the seller response;
- fields not independently evaluated.

A future additive projection may expose fields such as:

```text
tested_capability
independent_method
verified_output_fields
observed_but_not_independently_verified
```

These names are illustrative until a versioned public schema is defined.

### 2. Observation counts are not reliability percentages

Another AI consumer saw three successful seller-attributable paid observations and described the service as having "100% reliability".

That is stronger than the evidence supports.

Atinamos may publish counts such as:

```text
successful_fulfilments: 3
failed_fulfilments: 0
```

but those counts are observations from the published sample. They are not a statistical estimate of permanent or future reliability unless a separate methodology explicitly establishes such an estimate.

Consumers should read them as:

> 3 observed successful seller-attributable fulfilments in the published sample.

not:

> the service is 100% reliable.

### 3. Failure attribution must remain explicit

The code402 LEI series contained one Circle smart-account pre-settlement interoperability failure and two successful EOA paid controls.

The narrow observed finding was:

- the tested Circle smart-account authorisation independently validated under EIP-1271;
- the observed code402 payment path rejected it before settlement because ordinary signature recovery did not recover to the declared `from` address;
- no paid fulfilment was reached;
- the observation does not establish universal smart-account incompatibility.

An AI consumer initially generalised that result into a broader warning covering smart-contract accounts generally.

Future machine projections should therefore preserve an explicit attribution category, for example:

```text
seller_performance
verifier_failure
payment_interoperability
pre_payment_observation
unknown
```

and should continue to expose whether an observation is seller-performance evidence.

### 4. A fresh fixture is useful evidence, not proof of implementation

For a SHA-256 service, a fresh fixture reduced the chance that the returned result was simply a response to a previously known static test value.

That does not prove the provider's internal implementation, prove arbitrary-input behaviour for all future requests, or establish that verification traffic was indistinguishable from ordinary buyer traffic.

Where relevant, evidence should distinguish:

- fresh or repeated fixture selection;
- the observed output comparison;
- whether implementation mechanism was established;
- whether test-traffic distinguishability was evaluated.

### 5. `output_valid` in the original public receipt v1 is overloaded

The original `atinamos.public-verification-receipt.v1` schema uses:

```text
fulfilment.observed
fulfilment.output_valid
```

That field remains part of an existing public contract and historical receipts must stay valid.

However, current Assurance evidence now needs a clearer machine distinction between:

- whether useful machine output was observed;
- whether an independent correctness check was reached;
- which field or capability was checked;
- the expected and observed values;
- the validation outcome.

A newer additive/versioned format should avoid making one Boolean carry all of those meanings.

### 6. HTTP method is part of evidence identity

The original MCP v1 lookup shape is endpoint-oriented, while the current Verify Evidence API accepts both endpoint and HTTP method.

Method is material evidence. For example:

```text
GET https://service.example/task
POST https://service.example/task
```

may be different machine-service contracts with different payment requirements, request bodies, fulfilment behaviour and evidence histories.

A buyer must not infer that evidence observed for one HTTP method automatically applies to another method at the same URL.

Current exact-route machine evidence therefore uses:

```text
GET /v1/evidence?endpoint=<service-url>&method=<HTTP-method>
```

Future MCP evolution should preserve method-level identity explicitly rather than requiring an AI consumer to infer it from nested historical records.

## Format evolution

Atinamos now has two relevant public generations of evidence representation:

1. the original **Public Verification Receipt v1** projection used by earlier published experiments; and
2. the newer **Signed Assurance Evidence Receipt** used by the production Assurance publication path.

Existing public receipts are historical evidence and must not be rewritten to imitate a newer format.

The preferred direction is therefore additive versioning and backward-compatible projection rather than mutation of old evidence.

## Recommended machine-readable concepts

The audit recommends that a future versioned evidence projection make these concepts first-class where the underlying evidence supports them:

```text
identity
  endpoint
  method

scope
  tested_capability
  verified_output_fields
  observed_only_fields

correctness
  independent_method
  expected
  observed
  result

attribution
  category
  seller_performance_evidence

sample
  observation_counts
  counts_are_not_reliability_estimates

limitations
  future_behaviour_not_established
  implementation_mechanism_not_established
  traffic_indistinguishability_not_established
```

This is a design direction, not a published replacement schema.

## Compatibility rule

Any future schema tightening should preserve the following rules:

- historical receipts remain immutable;
- signed content is never silently rewritten;
- endpoint and method remain material service identity where applicable;
- unknown remains distinct from false;
- no evidence remains distinct from negative evidence;
- seller performance, verifier failure and payment interoperability remain separately attributable;
- a narrow correctness check must not be presented as verification of unrelated response fields;
- counts must not be converted into a reliability percentage by Atinamos;
- procurement policy remains buyer-owned.

## Result

The audit found no reason to replace the core Atinamos evidence architecture.

The main improvement is narrower machine semantics around:

> **identity · scope · correctness · attribution · limitations · observation counts**

The next implementation step should be a read-only comparison against the live Verify evidence builder and signed-receipt projection before any new public schema is introduced. That comparison should identify which of these concepts already exist in retained evidence and merely need exposing, and which would require genuinely new fields.
