# External Assurance Runner commissioning — IBANforge

**Date:** 6 September 2026  
**Status:** completed external commissioning observation  
**Service:** `POST https://api.ibanforge.com/v1/iban/validate`

> **You can pay to be tested. You cannot pay to be trusted.**

## Purpose

This record documents the first completed end-to-end external commissioning run of the current Atinamos Assurance Runner publication path against a paid third-party machine service.

The run was **human-triggered commissioning using Runner-controlled bounded execution logic**. It should not be described as unattended production autonomy.

The goal was to prove the complete path:

```text
controlled test definition
→ bounded x402 purchase
→ independent Base settlement observation
→ fulfilment capture
→ independent deterministic correctness comparison
→ immutable verification package
→ signed Assurance Evidence Receipt publication
→ public buyer lookup
```

## Tested capability

The independently tested capability was deliberately narrow:

```text
IBAN checksum validation
```

The independent method was:

```text
ISO 13616 MOD-97
```

Only the seller response field:

```text
valid
```

was independently validated.

Other fields returned by the service, including enrichment or bank metadata, may have been observed in the response but were **not** independently verified by this commissioning run.

## Controlled fixtures

Positive control:

```text
DE89370400440532013000
expected valid = true
observed valid = true
```

Negative control:

```text
DE90370400440532013000
expected valid = false
observed valid = false
```

The negative control deliberately expects `valid=false`; that is a passing correctness result for the negative fixture, not a service failure.

## Paid execution

Two paid x402 calls were made under the commissioning policy.

```text
positive control: 0.005 USDC
negative control: 0.005 USDC
total observed test spend: 0.010 USDC
network: Base mainnet / chain 8453
```

Independent settlement references retained by the Runner:

Positive control:

```text
transaction: 0x60d6747a566f8e820d44fa075126dd415990334bef2b36c944840fb6b7eacd45
block: 50962836
amount: 0.005 USDC
settlement status: CONFIRMED
```

Negative control:

```text
transaction: 0x73261a10bdfc03db1203897d4f86a158698b14280a44894b749c2f8fee5a17f9
block: 50963382
amount: 0.005 USDC
settlement status: CONFIRMED
```

For both paid controls:

- settlement was independently observed on Base;
- fulfilment was observed;
- the returned `valid` value matched the independently precomputed expectation;
- the validation result was terminal and publishable.

The transaction references are public chain references. They are included so the settlement claims can be independently inspected; they do not by themselves prove fulfilment or correctness.

## Signed Assurance Evidence Receipts

Two signed production Assurance Evidence Receipts were published under Ed25519 key id:

```text
atinamos-assurance-ed25519-202609-002
```

Negative control:

```text
receipt id: atinamos:receipt:c9f7dc76-898d-5d95-9dfc-388055750c58
human: https://verify.atinamos.co.uk/assurance/receipts/atinamos:receipt:c9f7dc76-898d-5d95-9dfc-388055750c58/
json:  https://verify.atinamos.co.uk/assurance/receipts/atinamos:receipt:c9f7dc76-898d-5d95-9dfc-388055750c58.json
```

Positive control:

```text
receipt id: atinamos:receipt:a6caf2c0-4f56-545b-ba8a-e62d0379b085
human: https://verify.atinamos.co.uk/assurance/receipts/atinamos:receipt:a6caf2c0-4f56-545b-ba8a-e62d0379b085/
json:  https://verify.atinamos.co.uk/assurance/receipts/atinamos:receipt:a6caf2c0-4f56-545b-ba8a-e62d0379b085.json
```

## Publication recovery observation

The first publication request reached the receiver while the receiver write gate was disabled and returned HTTP 503 before write confirmation.

The Runner correctly treated the dispatch outcome as indeterminate rather than automatically replaying it.

A GET-only reconciliation found no published record. After receiver publication/signing was intentionally enabled and idempotency behaviour was inspected, one explicit operator-approved exact replay was performed. Publication then returned HTTP 200 and GET-only reconciliation confirmed the record.

This commissioning event is useful evidence for the fail-closed publication/recovery path. It does not justify automatic replay after uncertain dispatch outcomes.

## Public lookup result

The production human Assurance evidence lookup for the exact service now exposes:

```text
observations: 2
paid tests: 2
successful fulfilments: 2
failed fulfilments: 0
signed Assurance receipts: 2
independently evaluated controls passed: 2 / 2
independent method: ISO 13616 MOD-97
verified output field: valid
total observed test spend: 0.010 USDC
```

Human lookup:

```text
https://assurance.atinamos.co.uk/evidence/
```

Exact machine evidence is available from Verify using the endpoint and method.

## Supports

This commissioning record supports the following narrow claims:

- the current bounded Runner path completed two real paid calls against the stated external endpoint;
- Base settlement was independently observed for both paid controls;
- useful fulfilment was observed for both controls;
- the returned `valid` field matched independent MOD-97 expectations for one valid and one invalid German IBAN fixture;
- the current production publication path produced two signed Assurance Evidence Receipts;
- the resulting evidence is available to buyer-facing lookup surfaces.

## Does not support

This record does **not** establish:

- permanent or provider-wide reliability;
- universal IBAN correctness across all countries or inputs;
- correctness of BIC, SEPA, bank, LEI or other enrichment fields returned by the service;
- the provider's internal implementation mechanism;
- that test traffic was indistinguishable from ordinary buyer traffic;
- unattended production autonomy;
- a universal recommendation to buy the service;
- a trust score or certification.

## Interpretation

This is evidence from two timestamped, bounded controls against one exact service route.

It is intentionally stronger than merely observing HTTP 200 or payment settlement because the returned `valid` field was independently compared against an objective checksum method.

It is intentionally narrower than a provider-wide quality judgement.
