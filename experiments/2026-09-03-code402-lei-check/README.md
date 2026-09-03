# Atinamos Independent Assurance Record — code402 LEI Check

**Observation date:** 2026-09-03  
**Provider:** code402  
**Service:** LEI Check  
**Endpoint:** `POST https://code402.dev/v1/tools/lei-check/call`  
**Payment made:** No  
**Status:** Phase 1 complete — paid fulfilment pending  
**Classification:** `payment_contract_observed`

## Independence statement

DRJ invited Atinamos to test code402 and explicitly welcomed publication of successes or failures.

The invitation did not alter the test method, evidence threshold or result. It is not presented as endorsement.

## Core result

Atinamos independently established the live REST request envelope, observed a correctly scoped free-tier response, inspected current health and x402 discovery metadata, forced the payment-validation path without authorising payment, and then obtained a genuine unsigned HTTP 402 payment challenge after the free-tier allowance was exhausted.

No valid payment authorisation was created and no USDC was spent during Phase 1.

The strongest current conclusion is therefore:

> **payment contract observed; paid fulfilment evidence pending**

## Timestamped observations

### 2026-09-03T08:33:10Z — request shape

An unwrapped POST body returned:

```text
HTTP 400
INPUT_SCHEMA_INVALID
expected { "input": { … } }
```

The live REST call therefore required the outer `input` wrapper.

### 2026-09-03T08:33:48Z — free-tier fulfilment

A correctly formed request returned HTTP 200 and:

```json
{
  "valid": true,
  "normalized": "5493001KJTIIGC8Y1R12",
  "reason": "checksum valid",
  "scope": "structure+checksum only"
}
```

The response reported `tier: free` and `settled: false`.

An XDR-1 receipt was present. Its signature has **not** yet been independently verified. A client-identifying free-tier payer value is deliberately omitted from this public record.

The returned checksum result will also be independently recomputed later rather than accepted as proof of its own correctness.

### Current health

The live `/health` surface reported:

```text
lei-check price: 999 atomic USDC
pricing mode: dynamic-dutch
receipt signer: 0xa036e2e3e19c6d02f30b3a9eb0acd057e6d9a5c8
```

### Current x402 manifest

`/.well-known/x402.json` advertised for the exact route:

```text
scheme: exact
network: eip155:8453
amount: 999
asset: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
payTo: 0xc59c85e661d34084a7769f955d17fd38254a6235
maxTimeoutSeconds: 300
authorization: TransferWithAuthorization (EIP-3009)
signature: EIP-712
free tier: 20 calls/day per client
```

The manifest also reported top-level `x402_version: 1`.

### Payment-validation path

A deliberately empty payment object was rejected:

```text
HTTP 402
MALFORMED_PAYMENT
```

That probe contained no usable authorisation or signature and could not transfer funds.

### 2026-09-03T08:50:49Z — genuine payment challenge

After free-tier exhaustion, an unsigned request returned HTTP 402.

The `payment-options` header advertised:

```json
[
  {
    "x402Version": 2,
    "scheme": "exact",
    "network": "eip155:8453"
  }
]
```

The decoded `payment-required` header contained:

```text
x402Version: 2
scheme: exact
network: eip155:8453
amount: 999
payTo: 0xc59c85e661d34084a7769f955d17fd38254a6235
maxTimeoutSeconds: 300
asset: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
```

The compatibility JSON body simultaneously exposed:

```text
x402Version: 1
network: base
scheme: eip3009
chain_id: 8453
challenge_ttl_seconds: 300
free_tier_remaining: 0
```

This dual representation is recorded, but is **not** currently classified as a defect.

## Scope observation

The free result stated:

```text
scope: structure+checksum only
```

That is an important limitation. The observation does not support interpreting a checksum-valid result as proof that the entity exists in a live LEI registry.

## Current payment contract

| Field | Observed |
| --- | --- |
| Header x402 version | 2 |
| Scheme | exact |
| Network | `eip155:8453` |
| Amount | `999` atomic USDC |
| Asset | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |
| Recipient | `0xc59c85e661d34084a7769f955d17fd38254a6235` |
| Timeout | 300 seconds |
| Payment authorisation | EIP-3009 |
| Signature scheme | EIP-712 |

## What this supports

This Phase-1 record supports that Atinamos independently observed:

- a reachable live service;
- the required REST request envelope;
- narrow structure/checksum scope;
- current machine-readable payment terms;
- a genuine HTTP 402 payment challenge;
- free-tier receipt issuance;
- payment-path rejection of malformed payment material.

## What this does not support

This Phase-1 record does not establish:

- paid settlement;
- paid fulfilment;
- correctness of the LEI result under an independent checksum implementation;
- offline verification of the XDR-1 receipt signature;
- LEI registry existence;
- permanent reliability;
- provider-wide trustworthiness.

## Machine-readable evidence

See [`evidence.json`](evidence.json).

The same sanitised observation is copied into the Atinamos Verification public evidence corpus so buyer agents can retrieve it through:

```text
GET https://verify.atinamos.co.uk/v1/trust?endpoint=https://code402.dev/v1/tools/lei-check/call
```

## Next work

The assurance test will next inspect the documented LEI algorithm, independently construct deterministic valid/invalid test cases, and only then proceed to a bounded paid call after explicit approval.

The paid result and XDR-1 signature verification will be appended to this same record rather than erasing the Phase-1 history.

**You can pay to be tested. You cannot pay to be trusted.**
