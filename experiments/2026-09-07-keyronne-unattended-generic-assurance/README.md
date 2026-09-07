# First Unattended Generic External Assurance Proof — Keyronne

**Date:** 7 September 2026  
**Service:** `POST https://keyronne.com/api/json-repair`  
**Status:** COMPLETE

> **You can pay to be tested. You cannot pay to be trusted.**

## Why this experiment matters

This is the first production proof that the Atinamos Assurance Runner can take an already-prepared and frozen Assurance Run and progress it through the routine paid execution path to signed public evidence without an operator manually stepping the individual execution stages.

It is a milestone in the transition from a commissioned verification engine to a productisable Assurance service.

## Run identity

```text
run id:      1b5bc844-368c-445a-8f84-e62be6d88baa
adapter:     generic-transaction-fulfilment v1.0
state before: PLAN_FROZEN
state after:  COMPLETE
```

The production command was invoked once for the existing run:

```text
atinamos-assurance-execute 1b5bc844-368c-445a-8f84-e62be6d88baa
```

The operator did not manually step routine challenge acquisition, signing, payment, Base settlement observation, fulfilment evaluation or Verification publication.

## Paid transaction

The Runner purchased the external JSON Repair service for:

```text
0.001 USDC
```

Network:

```text
Base / eip155:8453
```

Settlement transaction:

```text
0xc42bb177c41d21a56e9d3c02546fa8ebeda911cff3bc1139169a61c89f7b495c
```

Block:

```text
50996015
```

Settlement was independently observed rather than inferred from seller/facilitator output.

## Fulfilment result

The generic Assurance methodology asks a deliberately narrow question:

> **We bought what this service advertised. Did the seller deliver that kind of thing?**

The advertised JSON response shape included the fields:

```text
repairs
value
```

The paid response returned the advertised kind of JSON machine deliverable.

Observed classification:

```text
Payment:               SETTLED
Advertised deliverable: DELIVERED / FULFILLED
Correctness:           NOT_EVALUATED
Quality:               NOT_EVALUATED
```

Seller output was not treated as proof of factual correctness.

## Verification publication

The Runner created the immutable Verification package and published it to Atinamos Verification.

Signed receipt:

```text
atinamos:receipt:10e40afd-f6b1-57bd-9c1e-0a4a1695a428
```

Keyronne is now represented in the live Atinamos Verification evidence database and is available through buyer-facing evidence lookup.

## What the experiment proves

The following production path is now demonstrated:

```text
prepared / frozen Assurance Run
→ fixed Atinamos Buyer Policy
→ bounded x402 challenge acquisition
→ constrained payment signing
→ real external purchase
→ independent Base settlement observation
→ fulfilment capture
→ explicit correctness boundary
→ immutable Verification package
→ signed Evidence Receipt
→ COMPLETE
```

The practical consequence is that the Assurance Runner is no longer the principal development problem.

## What the experiment does not prove

The run began at `PLAN_FROZEN`.

It therefore does **not yet** prove the complete public seller journey:

```text
raw URL
→ discovery
→ scope explanation
→ plan freeze
→ commercial quote / funding
→ queue
→ autonomous execution
→ signed evidence
```

Discovery and test-plan preparation had already happened before the one-command unattended execution started.

It also does not establish permanent reliability, universal correctness, subjective quality, seller-wide trust, certification, approval or a recommendation to purchase.

## Safe-idle restoration

After the proof, temporary Runner and Verification signing/spending/publication authority was returned to OFF while read-only evidence surfaces and reconciliation remained available.

## Next milestone

The next project milestone is **Assurance v1 seller productisation**:

```text
seller enters endpoint
→ non-spending discovery
→ Atinamos explains what it can test
→ independent plan / quote
→ seller funding
→ durable queue
→ existing unattended coordinator
→ signed Verification evidence
```

The human seller journey should be implemented first. AI sellers should later use the same underlying run model through API/MCP rather than a separate execution path.