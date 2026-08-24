# Machine-Service Market Snapshot — 24 August 2026

## Summary

This note publishes an aggregate snapshot of the private Atinamos machine-service evidence catalogue as observed on **24 August 2026**.

The underlying catalogue is not published. This file contains aggregate counts and methodology only.

These figures are Atinamos observations, not claims about the total size of the global agent-service market.

## Aggregate snapshot

| Measure | Observed |
|---|---:|
| Canonical machine services | 60,234 |
| Resolved marketplace/source records | 69,220 |
| Longitudinal source observations | 71,817 |
| Unresolved source listings retained separately | 749 |
| Canonical services observed in 2+ sources | 8,596 |
| Canonical services observed in 3+ sources | 388 |
| Canonical services observed in 4 sources | 2 |
| Catalogue/index/search-exposure source types represented | 6 |
| Ranked discovery runs | 9 |
| Ranked discovery results | 90 |

Counts reflect records held at snapshot time. Marketplaces and indexes can change between observations.

## Resolved source coverage

| Source | Resolved source records |
|---|---:|
| PayAnAgent | 45,350 |
| Coinbase Bazaar | 16,636 |
| x402.direct | 3,998 |
| x402.jobs | 2,664 |
| The402 | 485 |
| 402.ad | 87 |

These values must not be added together and described as unique services because the same canonical service may appear in multiple sources.

Coverage is also not equivalent across sources. Some expose catalogue-style interfaces, some indexes, and some ranked/search surfaces.

During Atinamos testing, 402.ad reported a larger search total than its exposed search surface returned. It is therefore treated as **search-exposure evidence**, not as an exhaustive catalogue.

Virtuals ACP is tracked separately as ranked discovery evidence rather than as an exhaustive catalogue. This snapshot contains **9 discovery runs and 90 ranked results**.

## Cross-source presence

| Number of observed sources | Canonical services |
|---|---:|
| 1 source | 51,638 |
| 2 sources | 8,208 |
| 3 sources | 386 |
| 4 sources | 2 |

A service appearing in multiple sources is evidence of distribution. It is not, by itself, independent verification of service quality or fulfilment.

## Observed methods in the canonical register

| Method | Services |
|---|---:|
| GET | 39,682 |
| POST | 20,483 |
| HEAD | 36 |
| DELETE | 14 |
| PATCH | 8 |
| PUT | 7 |
| GET\|HEAD | 1 |
| GET OR POST | 1 |
| MESSAGE/SEND | 1 |
| TOOLS/CALL | 1 |

Atinamos does not invent a precise HTTP method where the source evidence does not support one.

At snapshot time the unresolved evidence register contained:

| Source | Unresolved listings |
|---|---:|
| x402.jobs | 738 |
| 402.ad | 11 |

Total unresolved listings: **749**.

This follows the Atinamos evidence rule:

> **Observed does not mean resolved.**

Missing contract identity is retained as missing evidence rather than filled by assumption.

## Marketplace-supplied category labels

The source data contained **3,495 distinct non-empty marketplace-supplied category labels**.

The most frequent labels included:

| Source-supplied label | Listing appearances |
|---|---:|
| other | 28,945 |
| web | 1,694 |
| x402 | 1,623 |
| data | 1,404 |
| ai | 870 |
| crypto | 661 |
| public-records | 436 |
| finance | 355 |
| glassnode | 297 |
| agent-ops | 265 |

Category coverage varied materially by source:

| Source | Listings carrying a category |
|---|---:|
| PayAnAgent | 45,350 / 45,350 |
| Coinbase Bazaar | 0 / 16,636 |
| x402.direct | 3,998 / 3,998 |
| x402.jobs | 1,032 / 2,664 |
| The402 | 485 / 485 |
| 402.ad | 87 / 87 |

For that reason these labels remain marketplace provenance rather than an Atinamos-assigned canonical taxonomy.

A future normalized taxonomy should preserve each original marketplace label alongside any derived classification.

## Longitudinal evidence

At snapshot time Atinamos had retained **71,817 resolved source observations**.

The history layer is intended to support observations such as:

- appearance or disappearance from a source;
- price changes;
- contract or schema changes;
- provider metadata changes;
- marketplace-supplied reputation changes;
- changes in ranked discoverability.

## What this snapshot does not prove

This publication does not claim that:

- 60,234 represents every machine service in existence;
- every observed listing is currently operational;
- marketplace presence proves fulfilment quality;
- multiple listings constitute independent trust evidence;
- marketplace reputation scores are Atinamos verification;
- an unresolved listing is unsafe.

External marketplace claims retain source provenance. Independent Atinamos verification is recorded separately.

## Publication boundary

**Public:** aggregate counts, methodology and selected findings.

**Private:** the underlying catalogue, full cross-market mapping, longitudinal raw evidence, provider clustering/entity-resolution logic, internal analysis and unpublished verification material.

This boundary exists so the research can be scrutinised without publishing the commercial intelligence asset itself.

## Human-readable publication

Canonical human-readable version:

https://verify.atinamos.co.uk/research/machine-service-market-snapshot-2026-08-24/

---

**Snapshot date:** 24 August 2026  
**Canonical services:** 60,234  
**Underlying catalogue:** private  
**Published data:** aggregate observations and methodology only

> **You can pay to be tested. You cannot pay to be trusted.**
