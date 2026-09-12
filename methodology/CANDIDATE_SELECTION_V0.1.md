# Decision Delta v0.1 — Candidate Selection Rules

**Status:** PRE-FREEZE DRAFT  
**Purpose:** prevent provider cherry-picking after Atinamos evidence is inspected.

## Principle

Candidate services are selected from an external machine-service discovery source **before** Atinamos evidence is used in the buyer decision.

Atinamos evidence must not determine marketplace relevance order or which provider is placed first.

## Primary selection process

For each task family:

1. define the buyer task and maximum service price before selecting providers;
2. query an external x402 discovery/directory source using a frozen neutral search phrase;
3. do not provide Atinamos provider names, evidence history or preferred endpoints to discovery;
4. retain the externally returned order;
5. filter only for objective executable requirements:
   - service materially fits the task;
   - public HTTPS invocation route;
   - method and required request shape are available;
   - Base mainnet (`eip155:8453`) is supported;
   - current price is within the scenario/buyer cap;
6. perform a **zero-spend exact-route preflight** with redirects disabled;
7. accept an executable paid candidate only when the exact route returns the expected payment challenge;
8. record rejected candidates and the rejection reason rather than silently replacing them;
9. freeze the accepted candidate set, order, machine contract, price, method, network, route and snapshot time;
10. only after that freeze may the treatment evidence snapshot be joined to candidate identities.

## Current executable-contract rule

Directory price is not authoritative for the experiment.

The frozen candidate price must come from the exact route's current payment challenge where it can be parsed. A directory/listing price is retained as provenance but is not allowed to overwrite a different live challenge price.

A redirect is not silently followed during candidate contract preflight. A changed route is recorded as changed/invalid for that exact candidate identity.

## Evidence identity

At minimum, Decision Delta binds evidence to:

```text
endpoint + HTTP method
```

Where query/path values materially identify the service contract, the frozen invocation route is also retained. Evidence from one route must not be attached to a textually different route merely because the provider name is similar.

## Candidate count

Each scenario should normally contain two to four credible candidates. More may be retained in the discovery snapshot, but the analysed comparison set must be fixed before results are observed.

## External-service preference

Primary scenarios should use independently owned external services. Atinamos-owned services may be used only as explicitly labelled engineering controls and are excluded from primary external-service claims.

## No evidence-based pruning

A provider must not be removed from the control candidate set because Atinamos already holds negative evidence about it. If it passed the frozen external-selection and zero-spend executable checks, it remains visible to both conditions.

Likewise, a service must not be added merely because Atinamos has favourable evidence for it.

## Change after freeze

If an exact service route, method, price or contract changes after scenario freeze:

- do not silently update the frozen scenario;
- preserve the original snapshot;
- classify the run according to the protocol's service-change rule;
- create a new scenario/version if a new current contract is required.

## Current discovery implementation note

Atinamos already has a proven seller-neutral Coinbase/x402 Bazaar discovery path from Proof #3. That implementation deliberately performs discovery before evidence lookup and zero-spend preflights exact returned routes. Decision Delta may reuse/generalise that implementation rather than creating an Atinamos-ranked market.
