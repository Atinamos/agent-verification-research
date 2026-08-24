# Observed ≠ Resolved: Why a Marketplace Listing Is Not Yet a Canonical Machine Contract

**Published:** 24 August 2026  
**Evidence status:** controlled engineering observation  
**Marketplace:** x402.jobs  
**Controlled sample:** 10 listings

> **Do not promote evidence to a stronger claim than the observation supports.**

## Finding

An AI-agent marketplace listing can contain useful commercial and technical evidence without containing enough information to establish a canonical executable service identity.

During controlled x402.jobs ingestion tests on 24 August 2026, Atinamos processed 10 listings before the full catalogue harvest. Five could be associated with an existing canonical service record while preserving identity evidence. Five could not be safely resolved because the HTTP method was not disclosed in the marketplace data inspected and there was no unique existing endpoint identity that allowed a method-preserving association.

Atinamos did not infer GET or POST simply to make those records fit the canonical service table. The unresolved records were retained separately as observed marketplace evidence.

This result is a small controlled engineering observation. It does **not** establish that half of x402.jobs listings are incomplete or that the same proportion applies to the full catalogue.

## Identity rule used in this test

For the current Atinamos HTTP-service model, canonical executable identity includes at least:

```text
endpoint + HTTP method
```

Earlier marketplace ingestion had already shown why endpoint alone is insufficient: the same URL can legitimately represent separate GET and POST services.

Therefore:

```text
GET  https://example.com/api/task
POST https://example.com/api/task
```

may represent two different executable contracts even though the URL string is identical.

## Resolution logic

The controlled x402.jobs test used the following conservative rule:

1. If an explicit HTTP method was available, resolve using endpoint + method.
2. If no method was available, associate the listing only when exactly one existing canonical Atinamos service already used that endpoint.
3. If method evidence was absent and the endpoint could not be uniquely associated, retain the listing as unresolved rather than inventing a method.

## Controlled result

| Outcome | Count | Interpretation |
| --- | ---: | --- |
| Safely associated with an existing canonical service | 5 | Existing evidence allowed canonical identity to be preserved |
| Observed but unresolved | 5 | Marketplace evidence was retained, but not promoted into a canonical identity |

“Unresolved” means only that Atinamos did not hold enough identity evidence to attach the marketplace listing safely to a canonical endpoint + method record.

It does **not** mean the service was unavailable, invalid, unsafe or incorrectly listed.

## Why retain unresolved evidence?

Discarding an unresolved listing would lose useful marketplace evidence. Guessing a missing method would create stronger data than the observation supports.

The implemented evidence model therefore distinguishes:

```text
Marketplace listing observed
        ↓
Canonical identity sufficiently evidenced?
        ├── yes → resolved service source
        └── no  → unresolved source listing
```

An unresolved listing can still retain marketplace identity, endpoint, descriptions, payment metadata, provider metadata, schemas, marketplace claims, timestamps and sanitised raw evidence while leaving the missing identity field unresolved.

## Longitudinal test

Atinamos also tested repeat ingestion of unresolved evidence.

One x402.jobs listing with no resolved HTTP method was ingested twice without a material marketplace change. The first pass created one unresolved listing and one immutable observation. The second pass created neither a duplicate unresolved row nor a duplicate immutable observation. The method remained unresolved.

A subsequent repeat of the 10-record controlled sample also produced zero new observations where the material state had not changed.

This supports the implementation decision that unresolved evidence can be retained longitudinally without forcing it into the canonical service table.

## What the observation supports

The narrow design conclusion is:

> **Observation and resolution are different evidence states.**

A marketplace can be a valid source of evidence even when the evidence it exposes is insufficient for another system's canonical identity requirements.

This matters for machine-service intelligence because discovery, identity, payment terms, execution and fulfilment are separate questions. A buyer or verifier should be able to state “this listing was observed” without silently upgrading that statement to “the exact executable contract is known”.

## What this observation does not establish

This controlled sample does not establish:

- the proportion of the full x402.jobs catalogue that lacks HTTP method evidence;
- that unresolved listings are defective services;
- that x402.jobs should adopt Atinamos's identity model;
- that endpoint + method is sufficient for every machine-service protocol;
- that a resolved identity demonstrates service quality or fulfilment;
- that the controlled sample was statistically representative.

The sample was collected during harvester development rather than through a formal random-sampling design.

## Full-harvest boundary

At the time this note was first prepared, the full x402.jobs catalogue harvest was still running. Later full-catalogue measurements must be reported separately with their complete sample size and method rather than retrofitted into this controlled 10-record result.

## Commercial relevance

Atinamos is developing commercial machine-service verification and marketplace-distribution tooling, and Atinamos services are themselves listed in the marketplaces being studied.

For verification, the observed/resolved distinction prevents marketplace presence from being presented as stronger identity evidence than Atinamos actually holds.

For marketplace distribution, it suggests that successful submission and public discoverability are still not necessarily enough: a distributor may also need to verify what machine-contract information became publicly visible after indexing.

These are product implications derived from the engineering observation, not evidence that a commercial market for those services has been established.

## Human-readable publication

Canonical human-readable article:  
https://verify.atinamos.co.uk/research/observed-does-not-mean-resolved/

## Licence

This research note is licensed under CC BY 4.0 under the repository's split-licence policy.
