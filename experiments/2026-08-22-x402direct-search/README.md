# x402.direct Service Directory Search — Pre-Settlement Paid-Path Failure

**Observed:** 22 August 2026  
**Classification:** `pre_settlement_paid_path_failure`

> **You can pay to be tested. You cannot pay to be trusted.**

This package records one Atinamos verification attempt against the paid `GET /api/search` service at x402.direct.

The service exposed a live x402 payment requirement for **0.001 USDC on Base**. The payment challenge contained a trailing newline in its `payTo` field. Atinamos retained that anomaly as evidence and normalised surrounding whitespace only so the legacy x402 v1 authorization could be constructed.

The authorization was created successfully and the authorised request was sent. The endpoint then returned **HTTP 500 Internal Server Error**.

A subsequent read-only Base USDC balance and transfer-log reconciliation found **no 0.001 USDC settlement** for this attempt. No fulfilment result was returned and no output assertions could be evaluated.

## Observed sequence

1. Initial request returned HTTP 402.
2. Live payment contract advertised x402 v1, exact scheme, Base and 0.001 USDC.
3. A trailing newline was observed in `accepts[0].payTo`.
4. Surrounding whitespace only was normalised for authorization construction.
5. The legacy payment authorization was created.
6. The authorised request was sent.
7. The endpoint returned HTTP 500.
8. No settlement was observed.
9. No fulfilment was observed.
10. No search output existed to validate.

## Evidence hashes

Raw payment challenge SHA-256:

```text
293f5d56f90bac1d5246cd0fea0c142f218b7ab0f1c461aae1fbb5875ae74390
```

Normalised payment challenge SHA-256:

```text
847721997fbe35289cbcc4997b553d545a82d874da5f87fa453cfaa6c98a6195
```

## Interpretation

The evidence supports a narrow conclusion: **the paid search path did not reach settlement or the advertised post-payment search-result stage in this invocation.**

It does not support the stronger statement that the seller took payment and failed to deliver, because no settlement was observed.

The payment-contract anomaly and a documentation/live-header naming mismatch were also recorded in the underlying study. Neither is asserted to be the cause of the HTTP 500.

## What this does not prove

This observation does not prove that:

- x402.direct generally fails;
- the provider is unsafe or untrustworthy;
- the malformed `payTo` caused the server error;
- the documentation/header mismatch caused the server error;
- a later invocation would produce the same result;
- the service's search-result quality is poor, because no search result was returned to inspect.

Atinamos publishes the observation. A buyer decides how much weight to give it based on recency, repetition, value at risk and its own procurement policy.

## Machine-readable record

- [`verification-receipt.json`](verification-receipt.json)
- Schema: [`../../schemas/verification-receipt-v1.schema.json`](../../schemas/verification-receipt-v1.schema.json)

No Atinamos verifier implementation, wallet secret, payer address, authorization header or internal anti-abuse logic is published in this package.
