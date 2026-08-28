# Proof #3 — Autonomous Buyer Experiment

**Date:** 28 August 2026  
**Status:** COMPLETE  
**Type:** bounded autonomous buyer / external discovery / evidence-informed procurement

This directory contains the deliberately sanitised public record for Atinamos Proof #3.

## Experiment objective

Demonstrate that a buyer can receive only a task, a maximum spend and a risk policy, then independently:

1. discover paid machine services from an external marketplace;
2. check whether the exact discovered invocation route is live enough to present an x402 payment challenge;
3. query already-published Atinamos evidence;
4. apply its own procurement policy;
5. select or reject a seller without a human naming the seller;
6. make one bounded live payment if permitted;
7. consume and objectively validate the purchased result.

## Task

```text
Repair malformed JSON-like input while preserving the supplied data.
```

Controlled input:

```text
{foo: 'bar', broken: true,}
```

Expected semantic result:

```json
{
  "foo": "bar",
  "broken": true
}
```

## Fixed buyer policy

- maximum spend: 0.02 USDC;
- Base mainnet only;
- Base USDC only;
- x402 v2 only;
- `exact` payment scheme only;
- published Atinamos evidence required;
- at least one successful paid fulfilment observation required;
- zero failed paid fulfilments allowed;
- evidence no older than 30 days;
- public HTTPS invocation only;
- redirects disabled;
- payment invocation bound to the exact externally discovered route.

## Experiment history

The experiment deliberately retained unsuccessful stages.

### 1. Initial discovery parser failure

External discovery ran and returned candidate services, but the local parser failed on mixed explanatory text plus JSON. No evidence lookup, seller selection or payment occurred.

### 2. Successful autonomous no-purchase

After a provider-neutral parser correction, a fresh external search returned eight JSON-repair candidates. None had the published Atinamos evidence required by the fixed policy, so the buyer selected no seller and made no payment.

This was a valid policy outcome, not a failed decision.

### 3. Evidence-acquisition round

The eight discovered candidates were frozen and independently tested under the same medium malformed-JSON semantic target. Four paid paths were exercised. Three produced settled, semantically valid fulfilments under that test. One settled response failed the semantic assertion. Four candidates were not paid because of transport failure, live price drift beyond the verification cap, or an exact route returning 404 at observation time.

The buyer policy was not weakened to manufacture eligibility.

### 4. Exact-route identity issue

A later fresh marketplace search returned some endpoint variants that differed from previously verified routes. Non-paying exact-route preflight showed that altered paths could return 404/405 while the verified route returned 402.

The buyer therefore rejected automatic punctuation/path aliasing and required an exact, redirects-disabled 402 preflight before evidence lookup.

### 5. First live paid attempt

A fresh run independently rediscovered Keyronne on its correct route and selected it under the unchanged policy. The buyer paid 0.001 USDC and received the correct semantic result, but the buyer-side validator did not recognise the seller's documented `value` response envelope.

The receipt therefore remained incomplete. The validator was fixed and regression-tested rather than rewriting the original outcome.

### 6. Final clean live run

A fresh external discovery again ranked Keyronne first. The exact route passed preflight, published Atinamos evidence met policy, and the buyer selected Keyronne without a human supplying the seller endpoint.

The buyer paid 0.001 USDC on Base using x402 v2 `exact`, received HTTP 200, observed successful settlement and exactly validated the repaired data.

Final result:

```text
proof3_complete = true
```

## Public evidence

- [Sanitised final buyer receipt](public-receipt.json)
- [Full public research note](../../research/2026-08-28-proof3-autonomous-buyer.md)

## Interpretation

This proves the controlled Atinamos buyer experiment. It does not prove provider-wide reliability, a universal trust verdict, or unrelated external-agent adoption of Atinamos.

The public artefacts omit buyer wallet identity, payment-recipient account information, credentials, internal infrastructure, private runtime details, operational source code and unpublished anti-gaming/challenge-generation techniques in accordance with the repository publication policy.
