# Decision Delta v0.1 — Real Scenario Plan

**Status:** DRAFT — candidates are not yet frozen.  
**Snapshot date for current preflight work:** 12 September 2026.  
**No paid calls were made while preparing this plan.**

This document records candidate scenario families before live Decision Delta results exist. Exact scenario JSON files will be frozen only after the candidate-selection rules, current executable contract, buyer policy and evidence snapshot are complete.

## Current zero-spend contract observations

The following exact routes were probed without a payment signature on 12 September 2026. A 402 result means only that the paid contract was exposed; it does not establish fulfilment or correctness.

| Candidate | Exact route | Method | Current preflight | Current Base challenge amount |
|---|---|---:|---:|---:|
| Keyronne JSON Repair | `https://keyronne.com/api/json-repair` | POST | 402 | 0.001 USDC |
| API Acre JSON Repair | `https://apiacre.com/v1/data/json-repair` | POST | 402 | 0.005 USDC |
| Workers JSON Repair | `https://genesis.palsus2023.workers.dev/v1/repair_json` | POST | 402 | 0.003 USDC |
| FenixFoundry JSON Repair | `https://x402.fenixfoundry.com/repair-json` | POST | 402 | 0.003 USDC |
| Hermes JSON Schema Repair | `https://agent.kihustle.tech/services/json-schema-repair/jobs` | POST | 402 | 0.010 USDC |
| x402.direct Service Directory Search | `https://x402.direct/api/search` | GET | 402 | 0.001 USDC |
| Animica Mesh Find | `https://animica.dev/x402/mesh/find` | POST | 402 | 0.001826 USDC for the preflight request |
| x402engine Web Screenshot | `https://x402engine.app/api/web/screenshot` | GET | 402 | 0.010 USDC |
| Hugen Visual Screenshot | `https://visual.hugen.tokyo/visual/screenshot` | GET | 402 | 0.020 USDC |
| 2s IBAN Validate | `https://2s.io/api/validate/iban` | GET | 402 | 0.0025 USDC |
| Macaroon IBAN Validate | `https://api.macaroonnetwork.com/execute/iban-validate-v1` | POST | 402 | 0.002 USDC |

Directory/listing prices are retained separately as provenance. The live payment challenge is authoritative for the frozen experiment price.

## Existing Atinamos evidence relevant to scenario design

Existing historical/public observations include:

- Keyronne JSON Repair — paid fulfilment observed, exact semantic result valid (28 Aug 2026).
- API Acre JSON Repair — paid fulfilment observed, exact semantic result valid (28 Aug 2026).
- FenixFoundry JSON Repair — paid fulfilment observed, exact semantic result valid (28 Aug 2026).
- Hermes JSON Schema Repair — paid fulfilment observed but provider-neutral semantic output validation failed (28 Aug 2026). This is fulfilment evidence and separate failed assertion/correctness evidence, not a failed-fulfilment claim.
- x402engine Web Screenshot — payment settled and HTTP fulfilment returned, but the purchased deliverable failed the tested representation/contract assertion (22 Aug 2026).
- x402.direct Service Directory Search — authorised paid-path request returned HTTP 500 and a later read-only chain check found no settlement (22 Aug 2026). This is pre-settlement paid-path evidence, not fulfilment failure.
- code402 LEI Check — successful EOA paid observations plus a separately attributed Circle smart-account pre-settlement interoperability failure (3 Sep 2026).
- IBANforge — signed deterministic-correctness commissioning evidence using independent ISO 13616 MOD-97 controls (6 Sep 2026).

## Scenario DD-01 — evidence correctly makes no difference

**Family:** JSON repair  
**Status:** READY FOR EXTERNAL-SELECTION SNAPSHOT

Candidate shape:

- Keyronne — current 0.001 USDC; existing successful paid semantic evidence;
- one or more independently discovered executable JSON-repair alternatives.

Purpose:

The control buyer may already select Keyronne on task fit/price. If treatment evidence supports the same choice, the correct result is `no_delta`.

This scenario is mandatory because Decision Delta must not be designed so evidence always changes behaviour.

## Scenario DD-02 — unknown cheaper service remains legitimately explorable

**Family:** JSON repair  
**Status:** READY FOR EXTERNAL-SELECTION SNAPSHOT

Candidate shape currently available:

- Workers JSON Repair — 0.003 USDC; no Atinamos paid evidence identified during preparation;
- API Acre JSON Repair — 0.005 USDC; existing successful paid semantic evidence.

Purpose:

Test the rule `UNKNOWN != UNSAFE`. Under Balanced v0.1 an unknown service below the exploratory cap may remain eligible. Evidence must not automatically force the buyer toward the known provider.

A no-delta or exploratory-cheaper choice is a valid result.

## Scenario DD-03 — known delivered output problem

**Family:** screenshot capture  
**Status:** READY, BUT HIGHER-PRICE ALTERNATIVE CURRENTLY UNKNOWN TO ATINAMOS

Candidate shape:

- x402engine Web Screenshot — 0.010 USDC; historical settled/fulfilled observation with failed deliverable-contract assertion;
- Hugen Visual Screenshot — 0.020 USDC; currently executable 402 contract, but no Atinamos paid evidence identified during preparation.

Purpose:

Test whether historical independent negative output evidence changes the decision.

Under the current Balanced v0.1 unknown-service exploratory cap (0.01 USDC), Hugen is above the cap. Therefore an evidence-assisted buyer may legitimately `REVIEW` or `ABSTAIN` rather than pay more for an unevidenced alternative.

A stronger price-premium version becomes possible if a fresh independent Hugen verification is acquired **before scenario freeze**. That would be a separate evidence-acquisition action and must not be performed merely to force a desired Decision Delta.

## Scenario DD-04 — two positively evidenced services

**Family:** JSON repair  
**Status:** READY FOR EXTERNAL-SELECTION SNAPSHOT

Candidate shape:

- Keyronne — 0.001 USDC; successful semantic evidence;
- FenixFoundry — 0.003 USDC; successful semantic evidence;
- API Acre — 0.005 USDC; successful semantic evidence.

Purpose:

Test whether evidence correctly stops being decisive once multiple candidates satisfy the buyer's evidence requirements. Price, external relevance order and contract fit should remain legitimate deciding factors.

Expected interpretation is not pre-registered as a required outcome; `no_delta` is entirely acceptable.

## Scenario DD-05 — deterministic correctness can justify a different choice

**Family:** IBAN validation  
**Status:** REQUIRES FRESH EVIDENCE ACQUISITION BEFORE FREEZE

Current executable external candidates include:

- Macaroon IBAN Validate — 0.002 USDC;
- 2s IBAN Validate — 0.0025 USDC.

Both expose current Base payment challenges. No current Atinamos paid correctness evidence for these exact routes has yet been frozen into Decision Delta.

Purpose:

The task explicitly requires deterministic correctness. A fresh independent MOD-97 observation for one candidate could test whether correctness evidence justifies selecting a slightly higher-priced service.

Any verification purchase used to seed this scenario must occur before scenario freeze, be published as evidence in its own right, and must not be chosen or repeated based on the subsequent Decision Delta result.

## Scenario DD-06 — pre-settlement failure evidence without mislabelling fulfilment

**Family:** service-directory / agent-service discovery  
**Status:** METHODOLOGY PENDING

Candidate shape:

- x402.direct Service Directory Search — current 0.001 USDC challenge; historical pre-settlement paid-path failure with no settlement;
- Animica Mesh Find — current executable paid discovery contract; current preflight request quoted 0.001826 USDC.

Purpose:

Potentially test whether a buyer reacts to a prior paid-path failure without describing it as seller non-fulfilment.

This scenario is **not ready to freeze** because Balanced v0.1 does not yet define whether or how pre-settlement failures affect eligibility. The rule must be decided before observing Decision Delta results, or this scenario must be excluded from v0.1.

## Scenario DD-07 — path-specific conflicting evidence

**Family:** LEI validation  
**Status:** HOLD / DO NOT FREEZE YET

Existing evidence for code402 includes successful EOA paid observations and a separate Circle smart-account interoperability failure. On 12 September 2026 the previously evidenced code402 route returned HTTP 308 to a different host during redirect-disabled preflight.

Purpose:

This is scientifically useful evidence that freshness and exact-route identity matter. However, the changed current route means the historical exact-route record should not simply be attached to a new route.

The scenario remains on hold unless a new current candidate identity is selected under the normal external-selection rules.

## Scenario DD-08 — historical evidence no longer matches a paid contract

**Family:** IBAN validation / contract freshness  
**Status:** EXCLUDE FROM PRIMARY DECISION PAIRS; RETAIN AS PRE-RUN FINDING

IBANforge has strong signed paid deterministic-correctness evidence from 6 September 2026. During 12 September preparation, the same validation route returned HTTP 200 to an unsigned/non-paying request instead of an x402 402 challenge.

This means it currently fails the Decision Delta paid-candidate preflight rule.

It must not be kept in the paid candidate set merely because Atinamos has favourable historical evidence. This is a useful example of why executable contract freshness is checked independently from historical evidence.

## Current assessment

We already have enough material for credible control/no-delta and negative-evidence scenarios. The most valuable missing primary scenario is a clean deterministic-correctness/price-premium pair. Acquiring that requires a small real verification purchase before freeze and therefore is a separate, explicit spend step.
