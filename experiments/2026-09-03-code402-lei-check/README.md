# Atinamos Independent Assurance Record — code402 LEI Check

**Observation date:** 2026-09-03  
**Provider:** code402  
**Service:** LEI Check  
**Endpoint:** `POST https://code402.dev/v1/tools/lei-check/call`  
**Status:** completed assurance series for the tested LEI scope

## Independence statement

DRJ invited Atinamos to test code402 and explicitly welcomed publication of successes or failures.

The invitation did not alter the test method, evidence threshold or result. It is recorded as provenance, not endorsement.

## Core result

The completed series contains four distinct observations:

```text
1 × payment contract observation
1 × Circle smart-account pre-settlement interoperability issue
2 × settled paid EOA controls with independently validated outputs
```

Current buyer-facing summary:

```text
observations: 4
paid tests: 2
successful fulfilments: 2
failed fulfilments: 0
payment interoperability issues: 1
```

The interoperability issue is deliberately not counted as a failed fulfilment because no settlement occurred and paid fulfilment was never reached.

## Service scope

Every tested result retained:

```text
scope: structure+checksum only
```

The service validates LEI structure and ISO 7064 MOD-97-10 checksum. This record does **not** establish that a checksum-valid LEI exists in a live registry or belongs to a particular entity.

## Phase 1 — payment contract

An initial schema probe established that the live REST route required an outer `input` object.

After free-tier exhaustion, an unsigned request returned HTTP 402 at `2026-09-03T08:50:49Z` with:

```text
x402Version: 2
scheme: exact
network: eip155:8453
amount: 999 atomic USDC
asset: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
recipient: 0xc59c85e661d34084a7769f955d17fd38254a6235
timeout: 300 seconds
authorization: EIP-3009 TransferWithAuthorization
payment signature: EIP-712
```

The compatibility JSON body also exposed x402 v1 / `base`. Atinamos records that as a dual representation observed, not as a defect in itself.

The original Phase-1 machine record is preserved as [`evidence-phase1.json`](evidence-phase1.json).

## Independently predetermined fixtures

Before the paid result was accepted, Atinamos independently calculated:

```text
529900T8BM49AURSDO55 → MOD-97 remainder 1 → expected valid=true
529900T8BM49AURSDO56 → MOD-97 remainder 2 → expected valid=false
```

A malformed 19-character fixture was prepared during planning but was not exercised on the paid path and is not claimed as a paid result.

## Circle smart-account observation

A Circle buyer at:

```text
0xe03ce3a34913f1a2245854fca79e4fbba789e10c
```

was confirmed to be a deployed smart-contract account on Base.

A 999-atomic-USDC authorization was created and submitted. code402 returned HTTP 402:

```text
BAD_SIGNATURE
voucher signature does not recover to `from`
```

Atinamos independently checked the exact authorization. Ordinary EOA recovery did not recover the smart-account address, but EIP-1271 `isValidSignature` returned the magic value:

```text
0x1626ba7e
```

for the exact EIP-712 digest. Base USDC `authorizationState` for the exact buyer and nonce remained unused.

The narrow conclusion is therefore:

> **The observed Circle smart-account authorization independently validated under EIP-1271, but code402 rejected it before settlement because the payment path required ordinary signature recovery to the smart-account `from` address.**

This does not support claiming that the Circle signature itself was invalid or that code402 is universally incompatible with smart accounts.

## Paid positive control

Input:

```text
529900T8BM49AURSDO55
```

Observed result:

```text
valid: true
reason: checksum valid
scope: structure+checksum only
```

This matched the independent expectation.

Settlement:

```text
999 atomic USDC / 0.000999 USDC
transaction: 0xf0213ebd5c8fcbe8fc41d03663cf6c2b5043117b361d523b41d821a1b98ae64b
block: 50821506
status: 1
```

The paid XDR-1 receipt independently recovered to published signer:

```text
0xa036e2e3e19c6d02f30b3a9eb0acd057e6d9a5c8
```

and its input/output hashes matched the exact paid input and returned result.

## Paid negative control

Input:

```text
529900T8BM49AURSDO56
```

Observed result:

```text
valid: false
reason: checksum failed
scope: structure+checksum only
```

This matched the independent expectation.

The fresh preflight quote was 1391 atomic USDC and the buyer authorised that as the maximum. Dynamic pricing decayed before settlement, so the actual payment was:

```text
1371 atomic USDC / 0.001371 USDC
transaction: 0x5fe5fb57fa4e19cddc82c5c728e0eda5d110d41f9afd5d436a52f1a39c16d40c
block: 50821772
status: 1
```

The second XDR-1 receipt independently recovered to the same published signer, and its exact input/output hashes matched.

`output_valid=true` for this negative control means the service correctly reported the intentionally checksum-invalid LEI as invalid.

## Successful spend and dynamic pricing

Successful settled spend:

```text
999 + 1371 = 2370 atomic USDC = 0.002370 USDC
```

The Circle smart-account attempt settled zero.

Observed dynamic-price sequence:

```text
999 → fresh quote 1391 → actual second settlement 1371 atomic USDC
```

Price is retained as a timestamped observation rather than treated as a permanent contract field.

## XDR-1 limitation retained

Both paid XDR-1 receipt signatures were independently verified. However, the accompanying receipt-signer authorization object contained:

```text
attestation_sig: ""
```

The documentation describes that attestation as seller-wallet authorization of the receipt signer. Because the signature was empty, Atinamos did not independently cryptographically establish that seller-wallet delegation.

The receipt input/output hash binding was reproducible using compact JSON. The public metadata does not fully specify the JSON canonicalization rule, and output field order affected the reproduced output hash.

## What this supports

For these timestamped observations:

- the exact payment contract was machine readable;
- two bounded EOA purchases settled on Base;
- the positive and negative paid results matched independent checksum expectations;
- both paid XDR-1 receipt signatures recovered to the published signer;
- both paid receipts bound the exact tested input and returned output;
- one Circle smart-account authorization independently validated under EIP-1271 but was rejected before settlement by the observed payment path.

## What this does not support

This record does not establish:

- LEI registry existence;
- permanent reliability;
- provider-wide trustworthiness;
- universal smart-account incompatibility;
- invalidity of the Circle-created signature;
- failed fulfilment on the Circle path;
- seller-wallet delegation to the receipt signer while the attestation signature is empty;
- a paid malformed-length result;
- a universal purchase recommendation.

## Machine-readable evidence

The completed sanitised series is in [`evidence.json`](evidence.json).

The current live buyer-facing evidence is available through:

```text
GET https://verify.atinamos.co.uk/v1/evidence?endpoint=https%3A%2F%2Fcode402.dev%2Fv1%2Ftools%2Flei-check%2Fcall&method=POST
```

Human-readable study:

```text
https://verify.atinamos.co.uk/studies/study-code402-lei-check/
```

## Conclusion

> **Two bounded EOA purchases settled and returned the independently expected positive and negative LEI checksum results, with independently verified XDR-1 receipt signatures and input/output binding. A separate Circle smart-account authorization independently validated under EIP-1271 but was rejected before settlement by the observed code402 payment path.**

That is evidence about the tested observations, not permanent trust.

**You can pay to be tested. You cannot pay to be trusted.**
