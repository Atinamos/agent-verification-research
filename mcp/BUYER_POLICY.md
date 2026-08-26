# Buyer policy reference

The `evaluate_policy` MCP tool lets the calling agent supply its own deterministic procurement rules.

Atinamos evaluates published evidence against those rules and returns the result. Atinamos does not own the buyer's risk appetite, budget or procurement policy.

## Supported policy fields

### `require_known`

Boolean. Defaults to `true` when omitted.

If true, the service must be represented in the published Atinamos evidence corpus.

### `minimum_successful_fulfilments`

Integer. Minimum number of published successful fulfilments required.

A successful fulfilment currently means a published paid observation where fulfilment was observed and the tested output assertions passed.

### `maximum_failed_fulfilments`

Integer. Maximum number of published failed fulfilments permitted.

### `require_paid_evidence`

Boolean. If true, at least one published paid test must exist.

### `max_evidence_age_days`

Number. Maximum permitted age, in days, of the latest published verification timestamp.

If the evidence age cannot be established, the result may be `insufficient_evidence` rather than silently assuming freshness.

### `max_price_usdc`

Number. Maximum permitted observed price in USDC, derived from the latest published observation when the published receipt contains an amount in USDC microunits.

If the observed price cannot be established from the published evidence, the result may be `insufficient_evidence`.

## Example policy

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

## Decision semantics

### `eligible`

All supplied rules pass and no required evidence value is unknown.

### `not_eligible`

At least one supplied rule fails.

### `insufficient_evidence`

No supplied rule fails, but one or more required values cannot be established from the published evidence.

## Important boundary

`eligible` means **eligible under the supplied policy**.

It does not mean:

- universally trusted;
- safe for every buyer;
- guaranteed to fulfil in future;
- approved by Atinamos for purchase;
- free from provider, contract or operational risk.

Different buyers can legitimately reach different decisions from the same evidence.

A machine-readable version of the current policy shape is available at [`schemas/buyer-policy.schema.json`](schemas/buyer-policy.schema.json).
