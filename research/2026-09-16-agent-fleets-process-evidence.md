# Agent fleets and process evidence in autonomous commerce

**Published:** 16 September 2026  
**Status:** Public research note  
**Version:** 1.0  
**Canonical article:** https://atinamoslabs.co.uk/research/agent-fleets-process-evidence/

> **Atinamos records evidence. The buyer decides what that evidence means.**

## Summary

AI-agent workflows are beginning to operate at a scale where one human can supervise hundreds or thousands of concurrent or delegated agent tasks. That observation does not itself prove large-scale autonomous commerce. It does make a related machine-commerce question important: when software can discover, choose and pay machine services, what evidence should exist before and after the spend?

This note connects that question to already-published Atinamos experiments. It does not claim that thousands of agents are currently using Atinamos, and it does not claim that the complete Atinamos raw-URL-to-purchase product journey is already unattended.

## Source hygiene: the agent-scale claim

The verifiable public source used here is **Boris Cherny, creator of Claude Code at Anthropic**, not the separate social-media attribution to Sam Altman / GPT-6 Astra that has circulated online.

Primary/official references:

- Sequoia Capital, **Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next**, published 4 May 2026: https://www.youtube.com/watch?v=SlGRN8jh2RI
- Coatue Management, **Thomas Laffont & Boris Cherny**, describing a few thousand agents running at a time, often overnight, and agents prompting other agents: https://www.linkedin.com/posts/coatue_thomas-laffont-boris-cherny-activity-7465917780773601280-5DfT

These references concern software-engineering workflows. They are not evidence that those agents were autonomously purchasing machine services.

## Why the commerce question is different

x402 is explicitly designed for programmatic payment by software, including autonomous agents. Its buyer documentation describes discovering payment requirements, signing a payment and accessing a paid resource, with optional service discovery for autonomous-agent use:

- https://docs.x402.org/getting-started/quickstart-for-buyers

The ability to transact does not by itself answer:

- what exact service route was selected;
- what evidence existed before the decision;
- what buyer policy permitted or rejected the purchase;
- what amount and operation were authorised;
- whether payment independently settled;
- what the seller returned;
- whether fulfilment, correctness or quality were actually evaluated.

Those are distinct evidence dimensions.

## Independent research context

The August 2026 **Agentic Commerce World** paper reports that process-level evidence is necessary because final state alone can miss evaluated errors and incomplete trajectories can still retain useful process signals:

- Fan et al., *Agentic Commerce World: An Auditable and Verifiable Environment for Vibe Commerce*: https://arxiv.org/abs/2608.02441

Anthropic's August 2026 multiagent-systems research separately argues that real-world agent-agent interaction is increasing and that behaviour at multiagent scale may not be well captured by assumptions designed around human-speed oversight:

- Anthropic, *Patterns and problems in emerging multiagent systems*: https://www.anthropic.com/research/multiagent-systems

These are external research references. They do not validate Atinamos specifically.

## What Atinamos has already demonstrated

### 1. Evidence-informed autonomous procurement

Proof #3 on 28 August 2026 demonstrated an Atinamos-operated buyer receiving a task, maximum spend and fixed risk policy, then:

```text
external marketplace discovery
→ exact-route non-paying preflight
→ published Atinamos evidence lookup
→ buyer-owned procurement policy
→ autonomous seller selection
→ bounded x402 payment
→ seller fulfilment
→ exact result validation
```

Final seller: Keyronne JSON Repair. Final purchase: **0.001 USDC on Base**.

The experiment also produced an earlier legitimate no-purchase outcome when no discovered candidate satisfied the unchanged evidence policy.

Evidence:

- [Proof #3 research note](2026-08-28-proof3-autonomous-buyer.md)
- [Proof #3 experiment record](../experiments/2026-08-28-proof3-autonomous-buyer/README.md)
- [Sanitised final buyer receipt](../experiments/2026-08-28-proof3-autonomous-buyer/public-receipt.json)

### 2. Unattended paid execution from a frozen Assurance plan

On 7 September 2026, the Atinamos Assurance Runner progressed an already-prepared Keyronne run from:

```text
PLAN_FROZEN → COMPLETE
```

One internal coordinator invocation handled routine x402 challenge acquisition, bounded payment signing, paid execution, independent Base settlement observation, fulfilment evaluation and Verification publication without an operator manually stepping those stages.

Observed public facts:

```text
service:      POST https://keyronne.com/api/json-repair
spend:        0.001 USDC
payment:      SETTLED
fulfilment:   FULFILLED
correctness:  NOT_EVALUATED
quality:      NOT_EVALUATED
```

Signed receipt:

```text
atinamos:receipt:10e40afd-f6b1-57bd-9c1e-0a4a1695a428
```

Evidence:

- [Keyronne unattended generic Assurance experiment](../experiments/2026-09-07-keyronne-unattended-generic-assurance/README.md)
- https://verify.atinamos.co.uk/research/unattended-generic-assurance-keyronne/
- https://verify.atinamos.co.uk/assurance/receipts/atinamos:receipt:10e40afd-f6b1-57bd-9c1e-0a4a1695a428/

### 3. Independent correctness where a deterministic method exists

On 6 September 2026, the IBANforge commissioning experiment made two paid external controls. Settlement was independently observed on Base and the returned `valid` field matched independently computed ISO 13616 MOD-97 expectations for one valid and one deliberately invalid IBAN fixture.

Evidence:

- [IBANforge commissioning experiment](../experiments/2026-09-06-ibanforge-assurance-commissioning/README.md)
- [Public Evidence Index](../EVIDENCE_INDEX.md)

## What the evidence supports

The published experiments support a bounded architecture in which these can remain separate:

```text
DISCOVERY
EVIDENCE LOOKUP
BUYER POLICY
AUTHORISATION
PAYMENT
SETTLEMENT OBSERVATION
FULFILMENT
CORRECTNESS
QUALITY
PUBLICATION
```

They also demonstrate that a policy can legitimately produce **no purchase**, and that a fulfilled purchase need not be described as correct or high quality unless those dimensions were independently evaluated.

## What the evidence does not support

This note does **not** establish that:

- thousands of agents are currently using Atinamos;
- Boris Cherny's agent fleet is using Atinamos or x402;
- unrelated external agents have adopted Atinamos as their evidence layer;
- the complete public seller journey from raw URL through discovery, quote/funding, queue, execution and publication is already unattended;
- any observed provider is permanently reliable, safe, trusted, approved or certified;
- a signed Atinamos receipt is a universal recommendation to buy.

The Keyronne unattended Runner proof began from an already-frozen plan. That boundary remains material.

## Research proposition

Atinamos is testing a narrow proposition:

> **Independent evidence for agentic commerce.**

A payment rail can move value. An agent framework can orchestrate work. A wallet can authorise a transaction. An independent evidence layer has a different job: preserve scoped observations that a buyer can inspect under its own policy.

The intended semantics remain:

```text
UNKNOWN != UNSAFE
SETTLED != FULFILLED
FULFILLED != CORRECT
CORRECT != HIGH QUALITY
SIGNED RECEIPT != PERMANENT TRUST
```

## Related public evidence

- [Atinamos Public Evidence Index](../EVIDENCE_INDEX.md)
- [Proof #3 — bounded autonomous buyer](2026-08-28-proof3-autonomous-buyer.md)
- [Keyronne unattended generic Assurance](../experiments/2026-09-07-keyronne-unattended-generic-assurance/README.md)
- [IBANforge deterministic commissioning](../experiments/2026-09-06-ibanforge-assurance-commissioning/README.md)

## Canonical human-readable article

https://atinamoslabs.co.uk/research/agent-fleets-process-evidence/
