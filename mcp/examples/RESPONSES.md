# Example MCP responses

The examples below are abbreviated for readability. They show the shape and interpretation of the public MCP responses rather than replacing the canonical published evidence records.

## `lookup_evidence`

Example request target:

```text
https://api.x402node.dev/ai/json-repair
```

Abbreviated response shape:

```json
{
  "known": true,
  "service": {
    "provider_name": "x402Node",
    "service_name": "JSON Repair",
    "service_route": "https://api.x402node.dev/ai/json-repair",
    "public_study": "/studies/study-x402node-json-repair/"
  },
  "evidence_summary": {
    "verification_runs": 1,
    "completed_runs": 1,
    "paid_tests": 1,
    "successful_fulfilments": 1,
    "failed_fulfilments": 0,
    "pre_settlement_failures": 0,
    "first_verified": "2026-08-22T11:54:40.898097+00:00",
    "last_verified": "2026-08-22T11:54:40.898097+00:00"
  },
  "buyer_context": {
    "principle": "Atinamos publishes evidence, not a universal trust verdict."
  }
}
```

The full live response also includes the latest observation and the published observations array.

## `search_services`

Abbreviated response shape:

```json
{
  "query": "x402",
  "count": 3,
  "services": [
    {
      "provider_name": "x402engine",
      "service_name": "Web Screenshot",
      "service_route": "https://x402engine.app/api/web/screenshot",
      "observations": 1
    },
    {
      "provider_name": "x402.direct",
      "service_name": "Service Directory Search",
      "service_route": "https://x402.direct/api/search",
      "observations": 1
    },
    {
      "provider_name": "x402Node",
      "service_name": "JSON Repair",
      "service_route": "https://api.x402node.dev/ai/json-repair",
      "observations": 1
    }
  ],
  "scope": "published_atinamos_evidence"
}
```

The count shown here reflects the published corpus at the time this example was recorded and may change.

## `evaluate_policy` — eligible

Example policy:

```json
{
  "require_known": true,
  "minimum_successful_fulfilments": 1,
  "maximum_failed_fulfilments": 0,
  "require_paid_evidence": true,
  "max_evidence_age_days": 30,
  "max_price_usdc": 0.01
}
```

Abbreviated result:

```json
{
  "decision": "eligible",
  "reasons": [
    "service_known_to_atinamos",
    "minimum_successful_fulfilments_met",
    "failed_fulfilments_within_policy",
    "paid_evidence_present",
    "evidence_fresh_enough",
    "observed_price_within_policy"
  ],
  "failures": [],
  "unknowns": []
}
```

## `evaluate_policy` — not eligible

Example policy:

```json
{
  "minimum_successful_fulfilments": 5
}
```

Abbreviated result at the time of publication:

```json
{
  "decision": "not_eligible",
  "reasons": [
    "service_known_to_atinamos"
  ],
  "failures": [
    "minimum_successful_fulfilments_not_met"
  ],
  "unknowns": []
}
```

These examples demonstrate that the same Atinamos evidence can produce different outcomes under different buyer-supplied policies.
