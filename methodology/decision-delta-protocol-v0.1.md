# Atinamos Decision Delta Protocol v0.1 — Pre-run Draft

**Status:** Draft for technical review. Not frozen. No Decision Delta results have been collected under this protocol.

## Research question

> Does independent service evidence change an autonomous buyer's purchasing decision?

Atinamos publishes evidence. The buyer owns the procurement policy and decides what the evidence means.

This study does not test whether Atinamos can force a buyer to prefer services with Atinamos evidence. It tests whether independently observed service evidence becomes decision-relevant when all other material conditions are held constant.

## Experimental unit

Each experimental unit is a matched pair of isolated buyer runs.

### Control

The buyer receives the same task, budget, buyer policy, candidate services, service descriptions, prices, payment-network information and candidate order, but it cannot consult Atinamos evidence.

### Evidence-assisted

The buyer receives the same information plus the Atinamos evidence available for the candidates at the frozen experiment timestamp.

The buyer sessions must not share memory, conversation history or prior decisions.

## Decision Delta

A Decision Delta occurs when the evidence-assisted condition changes either the final action or the selected provider relative to the control condition.

Possible final actions are:

- `BUY`
- `ABSTAIN`
- `REVIEW`
- `REQUEST_FRESH_EVIDENCE`

A Decision Delta is descriptive, not automatically beneficial. A changed decision may later prove helpful, neutral or unhelpful.

## Outcome observation

Where an actual purchase is made, the study separately records:

- payment outcome;
- settlement outcome;
- fulfilment outcome;
- correctness outcome where independently testable;
- quality outcome only where a defensible method exists.

Payment, fulfilment, correctness and quality remain separate evidence dimensions.

## Buyer

Protocol v0.1 uses one fixed buyer implementation. The buyer version, model/version where applicable, prompt template, model settings and execution configuration are frozen for the study.

The buyer receives a task, bounded budget, candidate set and buyer-owned procurement policy. It may purchase, abstain, request review or request fresher evidence according to that policy.

## Buyer policy

One primary policy is frozen before live experimental purchases begin. It must not automatically equate unknown services with unsafe services.

Initial controls may include:

- maximum service price;
- allowed payment networks;
- evidence freshness;
- minimum recent successful fulfilment observations;
- recent failed-fulfilment tolerance;
- unknown-service handling;
- deterministic correctness requirement where the task permits objective validation.

The policy belongs to the buyer. Atinamos does not issue a universal trust score or recommendation.

## Candidate selection

The primary study should use independently owned paid machine services where possible. Atinamos-owned services may appear only as clearly labelled secondary or control cases and should not dominate the primary result.

Candidate eligibility and scenario definitions are frozen before results are observed.

For each candidate the study preserves the information available at decision time, including:

- provider/service identity;
- exact endpoint;
- HTTP method;
- advertised price;
- payment network;
- machine-readable description/contract where available;
- discovery source;
- timestamp;
- contract fingerprint/hash where available.

## Planned scenario classes

Protocol v0.1 aims for approximately 6–8 useful scenarios covering a mixture of:

- cheaper service with no independent evidence;
- recent successful paid fulfilment evidence;
- known prior fulfilment or output-contract failure;
- stale positive evidence;
- settlement without successful fulfilment;
- deterministic correctness evidence;
- conflicting or path-specific evidence;
- similarly evidenced services;
- at least one case where evidence should reasonably make no difference;
- an unknown low-cost service that remains eligible for bounded exploration under the buyer policy.

The experiment is not designed so Atinamos evidence must always change the decision.

## Run controls

Within each matched pair, the following remain identical:

- buyer implementation;
- model/version and settings where applicable;
- buyer prompt template;
- task;
- candidate metadata;
- candidate order;
- budget;
- policy;
- candidate snapshot/evidence timestamp.

Candidate order may vary between repetitions, but must remain identical within a matched pair. Condition execution order may also vary, while sessions remain isolated.

## Failure handling

Technical buyer/harness failures are retained and marked as technical failures rather than silently replaced.

Evidence-service outages are recorded as treatment infrastructure failures.

Seller failures are retained as experimental outcomes rather than excluded.

If a service contract materially changes during a matched pair, the pair is marked as changed-during-pair and analysed separately.

No automatic retry is permitted after an indeterminate paid request where settlement status is unknown.

## Evidence preserved

Each run should preserve enough information for inspection or reproduction, including:

- buyer task/prompt;
- candidate snapshot;
- candidate prices;
- policy JSON and version;
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
- sanitised machine-readable logs.

Private credentials, payment authority secrets, verifier private keys, anti-gaming details and sensitive implementation material are not published.

## Primary measures

The study reports at minimum:

- completed matched pairs;
- Decision Delta count/rate;
- provider-selection deltas;
- abstention deltas;
- fresh-evidence/review deltas;
- no-delta outcomes;
- control vs evidence-assisted spend;
- control vs evidence-assisted fulfilment outcomes;
- control vs evidence-assisted correctness outcomes where measurable.

Repeated runs within one scenario are reported as clustered observations, not represented as independent market situations.

## Interpretation boundaries

This experiment can establish whether independent evidence affected the defined buyer under the defined conditions.

It does not by itself establish that:

- Atinamos makes agents universally safer;
- Atinamos determines which services are trustworthy;
- independent evidence always improves purchasing decisions;
- all autonomous buyers behave in the same way;
- a commercial market for evidence queries is proven.

Neutral and negative findings are valid results.

## Relationship with MCO

> MCO helps an agent understand what a service claims. Independent verification helps establish what was actually observed.

Decision Delta tests the next link: whether that independent observation changes what the buyer does.

## Freeze rule

Before live experimental purchases begin, the protocol, primary buyer policy, candidate-selection rules, scenario definitions, outcome definitions, exclusions and failure handling are versioned and frozen.

Any substantive methodological change after results are observed creates a new protocol version. The historical frozen version is not rewritten.

---

**Pre-run status:** This document is intentionally public before results are collected so the methodology can be criticised before it is frozen and used for live Decision Delta runs.
