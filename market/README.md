# Atinamos Market Search

Atinamos Market Search is a public, read-only search surface over a bounded projection of the Atinamos machine-service harvest registry.

It is designed for AI agents, developers and researchers that need to discover observed machine services and then decide what additional evidence they require before spending.

## Live endpoints

```text
GET https://verify.atinamos.co.uk/v1/market/search?q=<query>&limit=<1-50>
GET https://verify.atinamos.co.uk/v1/market/service/<service_id>
```

The same market capability is also available through the Atinamos Agent Shop:

```text
GET https://agent.atinamos.co.uk/agent/market/search?q=<query>&limit=<1-50>
GET https://agent.atinamos.co.uk/agent/market/service/<service_id>
```

## What the search returns

Search results may include:

- canonical Atinamos service ID;
- observed provider and service names;
- endpoint and HTTP method;
- number and names of discovery sources;
- observed categories;
- `last_observed_at` timestamp;
- a link to the separate Atinamos evidence lookup for that endpoint.

The response schema is currently:

```text
atinamos.market-search.v0.1
atinamos.market-service.v0.1
```

## Scope and interpretation

Market Search reports services **observed by Atinamos harvesters** across external machine-service discovery sources. It is not a directory of approved services and it does not issue a universal trust score.

`last_observed_at` means the listing was observed at that time. It does not establish that the service is currently reachable, purchasable, safe, trusted or independently verified.

**UNKNOWN is not UNSAFE.**

Multiple source observations can be useful provenance, but source overlap does not automatically prove independent corroboration because marketplaces and registries may syndicate one another.

## Market Search is not the Evidence MCP

These are deliberately separate public surfaces.

**Market Search** exposes a bounded read-only projection of the wider harvested service registry for discovery and provenance.

**Atinamos Evidence MCP** exposes selected, deliberately published verification evidence and buyer-supplied policy evaluation.

A service appearing in Market Search does **not** mean Atinamos holds published independent verification evidence for it. Buyers should use the returned evidence URL, Evidence MCP or other evidence sources when their policy requires more than discovery metadata.

## Security boundary

The public Verify deployment does not receive direct PostgreSQL credentials. Market Search is served through a bounded GET-only proxy to a dedicated read-only market service connected to the private Atinamos registry.

The private database, operational records, raw source payloads, credentials and unpublished verification material are not exposed by this interface.

## Example

```text
GET https://verify.atinamos.co.uk/v1/market/search?q=screenshot&limit=2
```

A buyer can use the returned candidate services as the start of a procurement flow:

```text
search market
    ↓
compare observed candidates
    ↓
query evidence where required
    ↓
apply buyer policy
    ↓
decide whether to spend
```

Atinamos provides evidence and observed market data. The buyer owns the purchasing policy and final decision.
