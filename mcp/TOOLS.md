# MCP tool reference

## `lookup_evidence(endpoint)`

Returns the published Atinamos evidence held for the canonical service route corresponding to the supplied endpoint.

Input:

```json
{
  "endpoint": "https://api.x402node.dev/ai/json-repair"
}
```

Typical response content includes:

- whether the route is known to Atinamos;
- provider and service name when published;
- public study path when available;
- verification counts;
- successful and failed fulfilment counts;
- first and last verification timestamps;
- latest published observation;
- settlement evidence when published;
- assertion counts;
- response hash;
- evidence source.

## `service_history(endpoint)`

Returns the timestamped published observation history for one canonical service route.

Input:

```json
{
  "endpoint": "https://api.x402node.dev/ai/json-repair"
}
```

If the service route is unknown, the response contains `known: false` and an empty observation list.

## `search_services(query, limit)`

Searches provider name, service name and canonical service route across the published Atinamos evidence corpus.

Input:

```json
{
  "query": "x402",
  "limit": 20
}
```

`limit` defaults to 20 and is capped by the server.

The response identifies its scope as:

```text
published_atinamos_evidence
```

This is important: MCP v1 search is not a claim to expose the complete private Atinamos service catalogue.

## `evaluate_policy(endpoint, policy)`

Evaluates the published evidence for a service against procurement rules supplied by the caller.

Input:

```json
{
  "endpoint": "https://api.x402node.dev/ai/json-repair",
  "policy": {
    "require_known": true,
    "minimum_successful_fulfilments": 1,
    "maximum_failed_fulfilments": 0,
    "require_paid_evidence": true,
    "max_evidence_age_days": 30,
    "max_price_usdc": 0.01
  }
}
```

Possible decision values:

- `eligible` — the available evidence satisfies the supplied rules and no required value is unknown;
- `not_eligible` — one or more supplied rules fail;
- `insufficient_evidence` — no supplied rule fails, but a required evidence value cannot be established from the published evidence.

The response also returns:

- `reasons` — rules or conditions that were satisfied;
- `failures` — rules that were not satisfied;
- `unknowns` — evidence fields that could not be established;
- the supplied `policy`;
- the evidence summary used for the evaluation.

`evaluate_policy` is not a universal trust score and is not a purchase instruction.
