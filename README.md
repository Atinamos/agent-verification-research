# Atinamos Agent Verification Research

Public research, schemas and technical evidence for Atinamos independent verification of paid AI-agent and machine services.

**Human-readable research:** https://verify.atinamos.co.uk  
**Technical evidence:** this repository

> **You can pay to be tested. You cannot pay to be trusted.**

Atinamos produces scoped evidence. The buyer decides what that evidence means under its own policy.

Atinamos does **not** issue a universal trust score, certification, approval, safe/unsafe verdict or permanent provider rating.

## Current state — 7 September 2026

Read the canonical public status first:

- [Current Assurance / Verification state](CURRENT_STATE_2026-09-07.md)
- [Public Evidence Index](EVIDENCE_INDEX.md)

The main technical milestone is now the first **unattended generic external Assurance execution from an already-frozen plan**.

### Keyronne JSON Repair

```text
service: POST https://keyronne.com/api/json-repair
run:     1b5bc844-368c-445a-8f84-e62be6d88baa
adapter: generic-transaction-fulfilment v1.0
state:   PLAN_FROZEN → COMPLETE
spend:   0.001 USDC
```

One internal production coordinator invocation handled the routine paid execution stages without an operator manually stepping x402 challenge acquisition, payment signing, paid dispatch, settlement observation, fulfilment evaluation or Verification publication.

Independent Base settlement:

```text
transaction: 0xc42bb177c41d21a56e9d3c02546fa8ebeda911cff3bc1139169a61c89f7b495c
block:       50996015
```

Signed evidence:

```text
atinamos:receipt:10e40afd-f6b1-57bd-9c1e-0a4a1695a428
```

Observed evidence layers:

```text
PAYMENT       SETTLED
FULFILMENT    FULFILLED
CORRECTNESS   NOT_EVALUATED
QUALITY       NOT_EVALUATED
```

The service returned the advertised kind of JSON deliverable. Atinamos did not infer semantic correctness or quality from that fulfilment.

- [Keyronne unattended generic Assurance experiment](experiments/2026-09-07-keyronne-unattended-generic-assurance/README.md)
- Human-readable record: https://verify.atinamos.co.uk/research/unattended-generic-assurance-keyronne/

### Important boundary

The Keyronne run began at `PLAN_FROZEN`.

It proves:

```text
frozen independent plan
→ real bounded external purchase
→ independent Base settlement observation
→ fulfilment evidence
→ immutable Verification package
→ signed receipt
→ COMPLETE
```

It does **not yet** prove the complete public seller journey:

```text
raw seller URL
→ non-spending discovery
→ scope explanation
→ independent frozen plan
→ seller funding
→ durable queue
→ proven Runner
→ signed evidence
```

That seller product journey is now the main development lane.

## Current development priority

```text
PROVEN ENGINE
      ↓
SELLER PRODUCT
      ↓
FIRST USERS
      ↓
REVENUE / MARKET FEEDBACK
```

Human seller productisation comes first. A later AI-seller API/MCP should use the same underlying Assurance run/order model rather than introducing another execution engine.

## Earlier production milestone — IBANforge deterministic commissioning

On **6 September 2026**, Atinamos completed the first end-to-end external deterministic commissioning of the current Assurance Runner → Verification publication path against:

```text
POST https://api.ibanforge.com/v1/iban/validate
```

Two bounded x402 calls were made at 0.005 USDC each. Settlement was independently observed on Base, useful fulfilment returned, and the returned `valid` field matched independently derived ISO 13616 MOD-97 expectations for one valid and one invalid fixture.

```text
total observed test spend:    0.010 USDC
Base settlements observed:    2
successful fulfilments:       2
independent controls passed:  2 / 2
signed Assurance receipts:    2
```

That run was **human-triggered commissioning**. It remains an important earlier milestone and should not be retroactively described as unattended.

- [IBANforge external commissioning experiment](experiments/2026-09-06-ibanforge-assurance-commissioning/README.md)

## Earlier autonomous buyer milestone — Proof #3

On **28 August 2026**, an Atinamos-operated bounded buyer was given a task, maximum spend and buyer policy. It independently searched an external x402 marketplace, checked exact-route viability, queried published Atinamos evidence, applied its own policy, selected an external seller without the human naming the seller, made a bounded payment, consumed the result and validated the purchased output.

Final clean run:

```text
selected seller: Keyronne JSON Repair
payment:         0.001 USDC on Base
x402:            v2 / exact
paid HTTP:       200
proof3_complete: true
```

- [Proof #3 research note](research/2026-08-28-proof3-autonomous-buyer.md)
- [Proof #3 experiment record](experiments/2026-08-28-proof3-autonomous-buyer/README.md)
- [Sanitised final buyer receipt](experiments/2026-08-28-proof3-autonomous-buyer/public-receipt.json)

This proves the controlled Atinamos buyer experiment. It does not establish widespread external-agent adoption of Atinamos evidence.

## First confirmed external commercial purchase of an Atinamos service

Also on **28 August 2026**, Atinamos observed an unrelated external client purchase Atinamos JSON Repair for 0.005 USDC through x402 and receive successful HTTP fulfilment.

- [Research note](research/2026-08-28-first-external-commercial-purchase.md)
- [Sanitised experiment record](experiments/2026-08-28-external-json-repair-purchase/README.md)
- [Sanitised public evidence](experiments/2026-08-28-external-json-repair-purchase/public-evidence.json)

This establishes external commercial use of an Atinamos machine service. It does not establish that the purchaser was definitely an autonomous AI agent.

## Other published direct evidence

The repository deliberately retains successful and unsuccessful observations, including:

- [code402 LEI Check assurance series](experiments/2026-09-03-code402-lei-check/README.md)
- [x402Node JSON Repair](experiments/2026-08-22-x402node-json-repair/README.md)
- [x402.direct Service Directory Search](experiments/2026-08-22-x402direct-search/README.md)
- [x402engine Web Screenshot](experiments/2026-08-22-x402engine-web-screenshot/README.md)

See [EVIDENCE_INDEX.md](EVIDENCE_INDEX.md) for the current consolidated index.

## Evidence semantics

Atinamos keeps these evidence layers separate:

```text
PAYMENT
Did payment settle?

FULFILMENT
Did the advertised kind of deliverable return?

CORRECTNESS
Was the returned content independently checked?

QUALITY
Was subjective quality independently evaluated?
```

Guardrails:

```text
UNKNOWN != UNSAFE
SETTLED != FULFILLED
FULFILLED != CORRECT
CORRECT != HIGH QUALITY
SIGNED RECEIPT != PERMANENT TRUST
SAMPLE COUNT != RELIABILITY PERCENTAGE
```

Endpoint and HTTP method are material evidence identity where applicable.

## Public Evidence MCP

AI agents and developers can query selected published Atinamos evidence through the read-only Atinamos Evidence MCP:

```text
https://verify.atinamos.co.uk/mcp
```

- [MCP documentation and index](mcp/README.md)
- [Quick start](mcp/QUICKSTART.md)
- [Tool reference](mcp/TOOLS.md)
- [Buyer policy reference](mcp/BUYER_POLICY.md)
- [Security and scope](mcp/SECURITY.md)

The MCP exposes published evidence and buyer-supplied policy evaluation. It does not expose wallet access, payment signing, verification-triggering writes or a universal trust verdict.

## Public Market Search

Atinamos exposes a bounded read-only projection of machine-service discovery observations:

```text
GET https://verify.atinamos.co.uk/v1/market/search?q=<query>&limit=<1-50>
GET https://verify.atinamos.co.uk/v1/market/service/<service_id>
```

- [Market Search documentation](market/README.md)

Market Search reports observed listings and provenance. A market listing is not verification evidence.

## Assurance evidence reads

Current signed Assurance evidence can be read using:

```text
GET https://verify.atinamos.co.uk/v1/assurance/receipts/<receipt_id>
GET https://verify.atinamos.co.uk/v1/assurance/evidence?endpoint=<service-url>&method=<HTTP_METHOD>
```

Endpoint **and HTTP method** are material evidence identity.

## Methodology and specifications

- [Evidence & Classification Methodology v1.0](methodology/evidence-and-classification.md)
- [Public Verification Receipt Specification v1.0](specifications/public-verification-receipt-v1.md)
- [Public Verification Receipt v1 JSON Schema](schemas/verification-receipt-v1.schema.json)
- [Machine-Evidence Schema Audit — 6 September 2026](research/2026-09-06-machine-evidence-schema-audit.md)

Historical evidence should remain valid in the format in which it was issued rather than being silently rewritten.

## Repository purpose

This repository is the deliberately sanitised public technical publication layer for Atinamos Verification and Assurance research.

It may contain:

- public evidence schemas;
- sanitised verification receipts;
- methodology suitable for technical scrutiny;
- deliberately published experiment records;
- public research notes;
- machine-interface documentation;
- examples and specifications.

It does **not** contain:

- Atinamos operational source code;
- private signing/wallet material;
- private infrastructure credentials;
- the private operational database;
- unpublished anti-abuse techniques;
- material that would materially assist gaming of Assurance tests.

GitHub is not where Atinamos Verification runs. It is where Atinamos publishes selected technical evidence and documentation for public scrutiny and machine consumption.

## Licensing

Copyright © 2026 MotionFil-AI.

- Research, methodology, written evidence, findings, specifications and datasets are licensed under **CC BY 4.0** unless a file states otherwise.
- Schemas, machine-readable receipts/examples and future source code are licensed under the **MIT License** unless a file states otherwise.

See [LICENSE.md](LICENSE.md) for details.
