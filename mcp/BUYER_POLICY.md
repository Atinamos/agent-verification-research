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

This is a **count of published observations**, not a reliability percentage. For example, three successful fulfilments and zero failed fulfilments in the published sample must not be restated as "100% reliable" or as a guarantee of future success.

### `maximum_failed_fulfilments`

Integer. Maximum number of published failed fulfilments permitted.

A failed-fulfilment rule applies to the published fulfilment evidence used by the evaluator. Verifier/system failures, payment-interoperability observations and pre-payment observations should remain separately attributable where the evidence projection exposes that distinction rather than being silently described as seller fulfilment failures.

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
- statistically proven reliable;
- guaranteed to fulfil in future;
- approved by Atinamos for purchase;
- free from provider, contract, interoperability or operational risk.

Likewise, `not_eligible` means one or more caller-supplied rules did not pass. It is not an Atinamos declaration that the service is unsafe, fraudulent or untrustworthy.

Different buyers can legitimately reach different decisions from the same evidence.

A machine-readable version of the current policy shape is available at [`schemas/buyer-policy.schema.json`](schemas/buyer-policy.schema.json).

For interpretation guardrails around scope, attribution and observation counts, see [Machine-Evidence Schema Audit — 6 September 2026](../research/2026-09-06-machine-evidence-schema-audit.md).
