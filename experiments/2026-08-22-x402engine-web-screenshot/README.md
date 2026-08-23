# x402engine Web Screenshot — settled fulfilment, contract-invalid artefact

**Observed:** 22 August 2026  
**Provider:** x402engine  
**Service:** Web Screenshot  
**Classification:** `settled_fulfilment_contract_invalid`

Atinamos independently exercised the paid x402engine Web Screenshot endpoint using a controlled request for `https://example.com`.

The x402 payment settled successfully for **0.01 USDC on Base**. The paid request returned **HTTP 200** and metadata matching the target page, but the primary purchased screenshot artefact failed the tested output contract: the returned `screenshot` value did not pass strict base64 decoding and therefore could not satisfy the advertised base64-PNG representation in this observation.

## Observed chain

1. HTTP 402 payment challenge received.
2. x402 v2 exact payment contract observed on Base.
3. Payment authorization created and sent.
4. **0.01 USDC settlement observed.**
5. Paid endpoint returned **HTTP 200**.
6. Page title assertion passed.
7. Upstream status-code assertion passed.
8. Screenshot base64/PNG assertion failed.
9. Output classified as contract-invalid for this observation.

## Objective assertions

- `metadata.title == "Example Domain"` — **PASS**
- `metadata.statusCode == 200` — **PASS**
- `screenshot` is valid base64 and begins with the PNG signature after decoding — **FAIL**

## Settlement proof

Base transaction:

`0x362e2520619063c42fddbcb9dc0db62052e460fd8ba02daab1c56dcb3ea47e2b`

The retained evidence records independent settlement confirmation matching the payment response.

## Response evidence

Canonical response SHA-256:

`d8bb1c27d507b693926972bd1bf1c10ce74d76ee4b2d316481fefd331f7c906d`

## Interpretation

This is deliberately **not** recorded as a successful verification merely because payment settled and HTTP 200 was returned.

The useful product was the screenshot artefact. In this timestamped observation, the advertised primary output representation did not pass validation.

This does **not** prove that x402engine always fails, that the provider is unsafe, or that every request would behave the same way. It records one independently observed paid outcome.

Atinamos produces evidence. The buyer decides what that evidence means for its own procurement policy.

## Machine-readable record

See [`verification-receipt.json`](verification-receipt.json).

Schema: [`../../schemas/verification-receipt-v1.schema.json`](../../schemas/verification-receipt-v1.schema.json)
