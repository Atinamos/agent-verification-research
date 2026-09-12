# Atinamos Decision Delta Protocol v0.1

**Status:** PRE-RUN DRAFT — NOT FROZEN  
**Research question:** Does independent service evidence change an autonomous buyer's purchasing decision?  
**Result status:** No Decision Delta results have yet been collected under this protocol.

## Purpose

This protocol defines a paired control/treatment experiment to test whether independent Atinamos service evidence materially changes an autonomous buyer's purchasing decision. The objective is not to prove Atinamos right. Neutral, negative and no-change outcomes are valid results.

Atinamos provides evidence. The buyer owns the procurement policy and final decision.

## Primary hypothesis

Providing independent service evidence changes the final procurement decision in a measurable proportion of otherwise matched autonomous purchasing situations.

## Null hypothesis

Providing independent service evidence causes no material change in the autonomous buyer's purchasing decision.

## Experimental unit

The unit of experiment is a matched Decision Pair comprising two isolated buyer sessions.

### Control

The buyer receives the same task, budget, buyer policy, candidates, candidate order, machine-facing service information, advertised prices and payment-network information, but no Atinamos evidence.

### Evidence-assisted

The buyer receives the same information plus the Atinamos evidence available at the frozen experiment timestamp.

The sessions must not share conversation history, memory or previous decisions.

## Decision Delta

A Decision Delta occurs when the evidence-assisted condition differs from control in either final action or selected provider.

Allowed final actions are:

- BUY
- ABSTAIN
- REVIEW
- REQUEST_FRESH_EVIDENCE

Decision Delta classifications are:

- provider_delta
- abstention_delta
- fresh_evidence_delta
- price_delta
- risk_response_delta
- no_delta

A change is not automatically classified as an improvement.

## Outcome Delta

Where objective validation is possible, purchased outcomes are recorded separately across:

- PAYMENT
- FULFILMENT
- CORRECTNESS
- QUALITY

Payment settlement is not fulfilment. Fulfilment is not correctness. Correctness is not subjective quality.

## Buyer and policy

Protocol v0.1 uses one fixed buyer implementation and one frozen primary buyer policy. The policy is buyer-owned. It must not simply encode `known service = buy` or `unknown service = reject`.

Unknown services may remain eligible for bounded exploratory purchases where the frozen buyer policy permits them.

The Policy API may return eligibility outcomes such as eligible, not_eligible or insufficient_evidence together with reasons and evidence references. It must not return a universal trust, safety or recommendation score.

## Scenario requirements

Protocol v0.1 should contain approximately 6–8 real scenarios, using independently owned paid machine services where possible. The frozen set should include cases covering:

- lower price with little/no independent evidence;
- recent successful fulfilment evidence;
- prior fulfilment or deliverable failure;
- stale evidence;
- payment success without successful fulfilment;
- deterministic correctness evidence;
- conflicting or path-specific evidence;
- similarly evidenced candidates;
- at least one case where evidence should legitimately make no difference.

The experiment must not be designed so Atinamos evidence always changes the decision.

## Controls against bias

For each matched pair hold constant:

- buyer implementation and model/version;
- model settings where controllable;
- task;
- candidate set;
- candidate order;
- budget;
- buyer policy;
- candidate machine-facing descriptions;
- advertised prices;
- payment network information;
- frozen evidence snapshot time.

Candidate order may be randomised between repetitions but must remain identical within each matched pair.

Control and treatment sessions must be isolated.

## Candidate freeze

Before live runs, preserve for every candidate:

- provider;
- service name;
- endpoint;
- HTTP method;
- discovery source;
- machine contract/description available to the buyer;
- advertised price;
- network;
- contract hash/fingerprint where available;
- snapshot timestamp.

Candidates must not be replaced after results are seen unless recorded as a new protocol version or explicit deviation.

## Run volume

The initial study is exploratory rather than population-representative. A target of roughly 8 scenarios with repeated matched runs is preferred. Repeated runs within one scenario are clustered observations and must not be represented as independent market situations.

Results must be reported both per matched run and per scenario.

## Failure handling

- Buyer/harness crash: retain as technical failure; do not silently overwrite it.
- Evidence API unavailable: record treatment infrastructure failure; the pair is not a valid Decision Delta pair.
- Service contract changes during a pair: record service-changed-during-pair and analyse separately.
- Indeterminate paid request: do not automatically retry when settlement state is uncertain.
- Seller failure: retain it as part of the experimental result rather than excluding it.

## Evidence preserved per run

Preserve enough information for independent inspection or reproduction, including:

- buyer task/prompt;
- candidate descriptions available at decision time;
- prices;
- endpoint and HTTP method;
- policy JSON and policy version;
- Atinamos evidence available at decision time;
- timestamps;
- control decision;
- evidence-assisted decision;
- structured reason codes;
- transaction/payment proof where appropriate;
- settlement evidence;
- fulfilment result;
- correctness checks where applicable;
- signed Atinamos receipts;
- sanitised machine-readable logs;
- deviations/exclusions.

Do not publish hidden chain-of-thought. Publish structured decision reasons instead.

## Public/private boundary

Public material should include the frozen protocol, schemas, candidate snapshots, policy, decision records, sanitised logs, evidence references, receipts, analysis code, exclusions and limitations.

Private material should include credentials, wallet secrets, signing keys, private infrastructure details, anti-abuse secrets, sensitive verifier internals and unreleased adversarial test cases where disclosure would enable gaming or create security risk.

## Analysis

Primary measures include:

- completed Decision Pairs;
- Decision Delta count/rate;
- provider deltas;
- abstention deltas;
- fresh-evidence deltas;
- price deltas;
- no-delta outcomes;
- control vs treatment spend;
- control vs treatment fulfilment outcomes;
- control vs treatment correctness outcomes where independently testable;
- policy eligible/not_eligible/insufficient_evidence outcomes.

A Decision Delta is evidence that independent evidence changed behaviour, not automatically evidence that the changed decision was better.

## Publication boundaries

Protocol v0.1 must not support claims that Atinamos universally makes agents safer, identifies trusted providers, or improves all purchasing decisions.

A defensible result statement should remain bounded to the tested buyer, policy, services, tasks and time period.

## Freeze rule

Before any Decision Delta live run:

1. review this protocol for methodological bias;
2. correct Policy API identity and evidence-dimension handling;
3. freeze the primary buyer policy;
4. build and dry-run the paired experiment harness without live spend;
5. freeze 6–8 scenario definitions and candidate snapshots;
6. version/hash the protocol and scenario package.

Any substantive methodological change after freezing creates a new protocol version or is published as a documented deviation. The frozen v0.1 record is not rewritten after results are observed.
