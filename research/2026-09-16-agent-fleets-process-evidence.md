# Agent fleets and process evidence in autonomous commerce

**Published:** 16 September 2026  
**Status:** Public research note  
**Version:** 1.1  
**Canonical article:** https://atinamoslabs.co.uk/research/agent-fleets-process-evidence/

> **Atinamos records evidence. The buyer decides what that evidence means.**

## Research question

Large agent fleets are becoming operationally feasible for some frontier users. That does not prove autonomous commerce at the same scale.

This note asks a narrower question:

> **As agents become more autonomous and numerous, does a seller-independent, machine-readable evidence layer make machine commerce measurably easier to inspect without becoming the authority that decides whom buyers should trust?**

Atinamos has demonstrated components of such an architecture in bounded experiments. It has **not** yet demonstrated a complete unattended raw-URL-to-purchase journey, broad external adoption, fleet-scale economics or that using Atinamos evidence improves purchasing outcomes.

## Source hygiene: the agent-scale claim

The verifiable public source used here is **Boris Cherny, creator of Claude Code at Anthropic**, not the separate social-media attribution to Sam Altman / GPT-6 Astra that has circulated online.

References:

- Sequoia Capital, **Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next**, published 4 May 2026: https://www.youtube.com/watch?v=SlGRN8jh2RI
- Coatue Management post reporting a later conversation with Cherny: https://www.linkedin.com/posts/coatue_thomas-laffont-boris-cherny-activity-7465917780773601280-5DfT

These references concern frontier software-engineering workflows. They are not evidence that those agents were autonomously purchasing machine services.

## Why process evidence is relevant

x402 is explicitly designed for programmatic payment by software:

- https://docs.x402.org/getting-started/quickstart-for-buyers

The ability to transact does not by itself answer:

- which exact service route was selected;
- what evidence existed before the decision;
- what buyer policy permitted or rejected the purchase;
- what amount and operation were authorised;
- whether payment settled;
- what the seller returned;
- whether fulfilment, correctness or quality were actually evaluated.

A payment record and an HTTP response are useful facts, but neither alone explains why a particular autonomous buyer was permitted to make the purchase.

## Adjacent research context

The August 2026 **Agentic Commerce World** paper reports that final state alone can miss evaluated errors and that incomplete trajectories can retain useful process information:

- Fan et al., *Agentic Commerce World: An Auditable and Verifiable Environment for Vibe Commerce*: https://arxiv.org/abs/2608.02441

Anthropic's August 2026 multiagent-systems research separately discusses increasing agent-agent interaction, many-agent behaviour and the limits of human-speed oversight assumptions:

- Anthropic, *Patterns and problems in emerging multiagent systems*: https://www.anthropic.com/research/multiagent-systems

These sources do **not** validate Atinamos or establish that a third-party pre-purchase evidence layer is necessary. They support the narrower point that process-level observability becomes more important as autonomous systems become more complex and numerous.

## What “independent” means here

In this research, **independent evidence** means **seller-independent observation**: the observer is separate from the service provider and is not simply repeating the seller's own claim about payment, fulfilment or correctness.

It does **not** imply that Atinamos is institutionally independent of an Atinamos-operated research experiment.

That distinction is material:

- Proof #3 used an Atinamos-operated buyer and the Atinamos evidence system.
- The Keyronne Assurance experiment used the Atinamos Runner, Atinamos observation logic and Atinamos publication.

## What Atinamos has demonstrated

### 1. An Atinamos-operated buyer can consume evidence under policy

Proof #3 on 28 August 2026 used an Atinamos-operated buyer with a task, maximum spend and fixed risk policy.

The final bounded sequence was:

```text
external marketplace discovery
→ exact-route non-paying preflight
→ published Atinamos evidence lookup
→ buyer-owned procurement policy
→ seller selection without human seller selection
→ bounded x402 payment
→ seller fulfilment
→ exact result validation
```

The experimental history matters.

The first successful dry run produced a legitimate **no-purchase** because all eight externally discovered candidates lacked qualifying Atinamos evidence. Atinamos then froze that candidate set and performed an evidence-acquisition round against those external services. A later fresh buyer run rediscovered Keyronne, found qualifying evidence generated during that round, selected it under the unchanged policy and purchased the service for **0.001 USDC on Base**.

The returned repaired JSON matched the required semantic result exactly.

**Seller selected in this bounded run:** Keyronne JSON Repair. This is not an endorsement or a claim of future reliability.

Evidence:

- [Proof #3 research note](2026-08-28-proof3-autonomous-buyer.md)
- [Proof #3 experiment record](../experiments/2026-08-28-proof3-autonomous-buyer/README.md)
- [Sanitised final buyer receipt](../experiments/2026-08-28-proof3-autonomous-buyer/public-receipt.json)

This proves that an autonomous buyer can consume a seller-independent evidence corpus under a fixed policy. It does **not** prove that an external evidence ecosystem already exists or that using Atinamos evidence produces better outcomes than an equivalent buyer without it.

### 2. Single-invocation unattended execution of an already-frozen Assurance run

On 7 September 2026, the Atinamos Assurance Runner progressed an already-prepared Keyronne run from:

```text
PLAN_FROZEN → COMPLETE
```

After one coordinator invocation, routine x402 challenge acquisition, constrained signing/payment, Base settlement observation, fulfilment evaluation and Verification publication proceeded without an operator manually stepping those stages.

Observed public facts:

```text
service:      POST https://keyronne.com/api/json-repair
spend:        0.001 USDC
payment:      SETTLED
fulfilment:   FULFILLED
correctness:  NOT_EVALUATED
quality:      NOT_EVALUATED
```

Temporary spending/signing/publication authority was restored to OFF after the proof.

Evidence:

- [Keyronne frozen-plan Assurance experiment](../experiments/2026-09-07-keyronne-unattended-generic-assurance/README.md)
- https://verify.atinamos.co.uk/research/unattended-generic-assurance-keyronne/
- https://verify.atinamos.co.uk/assurance/receipts/atinamos:receipt:10e40afd-f6b1-57bd-9c1e-0a4a1695a428/

This should be described precisely as **single-invocation unattended execution of an already-frozen run**. It does not establish the complete unattended public path from raw URL through discovery, plan preparation, quote/funding, queue, execution and publication.

### 3. A two-fixture deterministic correctness check

On 6 September 2026, the IBANforge commissioning experiment made two paid external controls. Settlement was observed on Base and the returned `valid` field matched independently computed ISO 13616 MOD-97 expectations for one valid and one deliberately invalid IBAN fixture.

Evidence:

- [IBANforge commissioning experiment](../experiments/2026-09-06-ibanforge-assurance-commissioning/README.md)
- [Public Evidence Index](../EVIDENCE_INDEX.md)

This is a narrow two-fixture correctness observation for one field under a deterministic method. It is not evidence of universal IBAN correctness or general service quality.

## What a signed receipt establishes

A signed Atinamos receipt provides cryptographic integrity and provenance for the published Atinamos statement.

It does not mean that every underlying operational fact can be independently reconstructed by a third party. Public receipts are sanitised; some raw operational material remains private or is represented publicly by hashes and commitments.

Therefore:

```text
SIGNED RECEIPT INTEGRITY
!=
THIRD-PARTY RECONSTRUCTION OF EVERY UNDERLYING OBSERVATION
```

See:

- [Atinamos Public Verification Receipt Specification v1.0](../specifications/public-verification-receipt-v1.md)

## What is not claimed as novel

Atinamos does not claim to have invented:

- API contracts;
- assertions;
- policy engines;
- cryptographic signatures;
- audit logs;
- provenance records;
- payment-settlement checks;
- distributed workflow patterns.

The research question is compositional: how should these mechanisms be separated and represented when autonomous software discovers, selects and purchases machine services without transaction-by-transaction human review?

Atinamos is an experimental implementation of that question, not a claim to have invented transaction auditing.

## Hard open problems

### Economics and evidence reuse

Evidence has a cost. A fresh Assurance process may cost more than a micro-transaction. A viable model cannot assume that every buyer should retest every service before every purchase.

A possible research direction is proportional assurance: reusable timestamped evidence, buyer-defined freshness requirements and assurance effort that rises with value at risk. The economics remain unproven.

### Non-deterministic correctness

Deterministic checks work for narrow tasks such as checksums or exact JSON repair. Many useful agent services produce subjective or non-deterministic outputs. A second evaluator model can add cost and simply move uncertainty into another model.

Where no independent correctness method exists, the correct evidence state may remain:

```text
CORRECTNESS: NOT_EVALUATED
QUALITY:     NOT_EVALUATED
```

while narrower facts such as settlement, delivery, latency, format or provenance are still recorded.

### Gameability and evidence pollution

Evidence quantity is not reliability. Seller-controlled buyers, related identities, repeated self-purchases and third-party claims must not automatically acquire the same weight as a seller-independent observation.

Any future ingestion of broader external evidence will require provenance, relationship and anti-gaming controls. Atinamos has not demonstrated resistance to sophisticated sybil or evidence-pollution attacks at ecosystem scale.

### Bootstrap, staleness and who pays

Pre-purchase evidence often exists because someone previously paid to test a service.

Seller-funded assurance creates incentive questions. Buyer-funded assurance creates duplication and cost questions. Verifier-funded coverage has scale limits. Evidence ages and may require retesting.

These are central open questions rather than solved details.

## Atinamos positioning

Atinamos is not proposed as a mandatory intermediary and is not trying to replace x402, wallets, agent frameworks, API testing or observability systems.

A buyer may use Atinamos evidence, another evidence source, its own observations or no external evidence at all.

The research proposition is:

> **Seller-independent evidence for agentic commerce.**
>
> **Atinamos records evidence. The buyer decides what that evidence means.**

The intended semantics remain:

```text
UNKNOWN != UNSAFE
SETTLED != FULFILLED
FULFILLED != CORRECT
CORRECT != HIGH QUALITY
SIGNED RECEIPT != PERMANENT TRUST
SAMPLE COUNT != RELIABILITY PERCENTAGE
```

## Next experiment: does evidence improve procurement?

Proof #3 shows that a buyer can consume evidence. It does not show that doing so improves outcomes.

A stronger experiment would compare matched buyers using the same tasks, candidate services, budgets and failure conditions:

```text
Buyer A:
marketplace metadata + service contract + price

Buyer B:
same inputs + Atinamos evidence under a pre-declared policy
```

Potential outcome measures:

- bad purchases;
- successful fulfilments;
- validation failures;
- no-purchase decisions;
- total cost;
- latency;
- evidence overhead.

That would begin to test whether seller-independent evidence provides measurable utility rather than merely proving that an agent can consume it.

## What this note does not establish

This note does **not** establish that:

- thousands of agents are currently using Atinamos;
- Boris Cherny's agent fleet is using Atinamos or x402;
- unrelated external agents have adopted Atinamos as their evidence layer;
- Atinamos evidence improves autonomous purchasing outcomes;
- the complete public seller journey is unattended;
- the economics work at fleet scale;
- Atinamos has solved non-deterministic output evaluation;
- Atinamos is resistant to sophisticated evidence gaming or sybil attacks;
- any observed provider is permanently reliable, safe, trusted, approved or certified.

## Related public evidence

- [Atinamos Public Evidence Index](../EVIDENCE_INDEX.md)
- [Proof #3 — bounded autonomous buyer](2026-08-28-proof3-autonomous-buyer.md)
- [Keyronne frozen-plan Assurance experiment](../experiments/2026-09-07-keyronne-unattended-generic-assurance/README.md)
- [IBANforge deterministic commissioning](../experiments/2026-09-06-ibanforge-assurance-commissioning/README.md)
- [Public Verification Receipt Specification](../specifications/public-verification-receipt-v1.md)

## Revision history

**v1.1 — 16 September 2026**  
Defined seller-independent evidence; disclosed the Proof #3 evidence-acquisition round; narrowed the unattended Runner description; clarified receipt integrity/provenance; added economics, non-deterministic evaluation, provenance/gaming and bootstrap limitations; and reframed the conclusion as a falsifiable research question with a proposed matched control experiment.

**v1.0 — 16 September 2026**  
Initial publication.

## Canonical human-readable article

https://atinamoslabs.co.uk/research/agent-fleets-process-evidence/
