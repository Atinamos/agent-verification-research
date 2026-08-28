# Proof #3 — A Bounded Autonomous Buyer With External Discovery

**Published:** 28 August 2026  
**Status:** COMPLETE

> **You can pay to be tested. You cannot pay to be trusted.**

## Summary

On 28 August 2026, an Atinamos-operated autonomous buyer completed a bounded paid procurement experiment in which the human supplied only a task, a maximum spend and a risk policy.

The buyer independently searched the Coinbase/x402 Bazaar, evaluated the externally ranked candidates, queried already-published Atinamos verification evidence, applied its own policy, selected a seller without a human naming the seller, completed an x402 payment, consumed the returned result and objectively validated the output.

The final receipt recorded:

```text
purchase_allowed = true
selected = keyronne.com / JSON Repair
payment = 0.001 USDC on Base
HTTP = 200
settlement = observed
output validation = exact match
proof3_complete = true
```

This is the Atinamos **Proof #3** milestone.

It is not the same as independent market adoption. The buyer in this experiment was operated by Atinamos. An unrelated external agent independently discovering and purchasing an Atinamos service remains a separate milestone.

## The question

Can a buyer receive only a goal, budget and risk policy, then independently:

1. discover paid services from an external marketplace;
2. compare the externally ranked candidates;
3. query independent evidence where available;
4. apply its own procurement policy;
5. select or reject a seller without a human supplying the endpoint;
6. make a bounded payment if policy permits;
7. consume and validate the result?

Proof #3 required the entire sequence to occur in one clean live run.

## Pre-registered task

The task was deliberately small and objectively measurable:

```text
Repair the malformed JSON-like input:
{foo: 'bar', broken: true,}
```

The required semantic result was exactly:

```json
{
  "foo": "bar",
  "broken": true
}
```

The small fixture kept the experiment inexpensive and avoided subjective output scoring.

## Buyer policy

The buyer policy was fixed before the final purchase:

- maximum total spend: **0.02 USDC**;
- Base mainnet only;
- Base USDC only;
- x402 version 2 only;
- `exact` payment scheme only;
- published Atinamos evidence required;
- at least one successful paid fulfilment observation required;
- zero failed paid fulfilments allowed;
- evidence no older than 30 days;
- public HTTPS target only;
- redirects disabled;
- the paid invocation had to remain bound to the exact route returned by external discovery.

If no candidate satisfied policy, the correct outcome was no purchase.

## External discovery

The buyer used Coinbase/x402 Bazaar through an AWS AgentCore integration. Atinamos evidence was not supplied to the discovery step and did not determine marketplace ranking.

The discovery process produced eight JSON-repair candidates. Atinamos itself did not appear in this JSON-repair candidate set.

The first successful dry run therefore demonstrated a legitimate autonomous no-purchase: all eight externally discovered candidates lacked qualifying published Atinamos evidence at that point, so the buyer refused to spend rather than weakening its policy.

## Evidence-acquisition round

Instead of relaxing the buyer policy, Atinamos froze the eight discovered services and independently tested all eight under the same medium-difficulty malformed-JSON semantic target. Provider-specific request wrappers were used only where the advertised machine contract required different field names.

The observed results were:

| Provider / service | Paid? | Observed result |
| --- | --- | --- |
| Keyronne — JSON Repair | yes | settled, fulfilment observed, exact semantic validation passed |
| AgentProof — JSON Repair | no | TLS transport failure before payment |
| FenixFoundry / agent-reader — JSON Repair | yes | settled, fulfilment observed, exact semantic validation passed |
| Hermes Commerce — JSON Schema Repair | yes | settled and fulfilment returned, but semantic validation failed |
| API Acre — JSON Repair | yes | settled, fulfilment observed, exact semantic validation passed |
| BitBooth — JSON Repair | no | live payment terms exceeded the advertised-price verification cap; payment blocked |
| toolbelt402 — JSON Repair | no | exact advertised route returned HTTP 404 at verification time |
| NetIntel — JSON Repair | no | exact advertised route returned HTTP 404 at verification time |

Four payments were made during this evidence-acquisition round. Three services produced **settled, semantically valid fulfilments under this test**. One settled service returned a result that failed the semantic assertion.

The results were retained as evidence observations rather than converted into a provider-wide rating.

## Route identity finding

A later fresh discovery run exposed a separate problem: some returned invocation paths differed from previously tested exact routes by punctuation or path structure. Non-paying preflight checks showed examples where the verified route returned an x402 payment challenge while the altered discovered route returned HTTP 404 or 405.

Atinamos did not silently treat `_`, `-` or path variations as equivalent.

That produced an important architecture finding:

> **A machine-service endpoint is part of the executable contract, not cosmetic text.**

The buyer was hardened so a discovered invocation route had to survive an exact, redirects-disabled, non-paying HTTP 402 contract preflight before it could proceed to evidence lookup and possible payment.

This did not change the buyer's trust or spend policy.

## First paid execution — validator-envelope failure

The first live execution independently rediscovered Keyronne at the correct route, found qualifying evidence, selected it and made a settled **0.001 USDC** purchase.

The seller returned HTTP 200 and the correct repaired semantic value under a response field named `value`.

The buyer's local validator, however, did not yet recognise that response envelope and therefore recorded `proof3_complete = false` even though the returned semantic value was correct.

This was retained as an implementation failure rather than rewritten as a successful Proof #3 run.

The validator was corrected to recognise the documented envelope while requiring an **exact** semantic object match. The relevant regression and safety suite then passed 19/19 tests before another paid run was attempted.

## Final clean live run

A completely fresh live run was then executed.

External discovery again ranked Keyronne JSON Repair first at **0.001 USDC**. The exact route passed the non-paying 402 preflight. Published Atinamos evidence showed one paid successful fulfilment and zero failed paid fulfilments, satisfying the unchanged buyer policy.

Other externally discovered services were evaluated independently; FenixFoundry and API Acre also satisfied the evidence policy, while candidates without qualifying evidence or paid success remained ineligible.

The buyer selected the highest-ranked eligible service: **Keyronne JSON Repair**.

Observed payment and fulfilment:

```text
Endpoint: https://keyronne.com/api/json-repair
Method: POST
x402 version: 2
Scheme: exact
Network: eip155:8453 (Base mainnet)
Asset: Base USDC
Amount: 0.001 USDC
Paid HTTP status: 200
Settlement: observed successful
Transaction: 0x241358fc7223a80fd2803bb49438a47da684ab01b49afc5a0a99736c74fdffca
```

The returned repaired value was exactly:

```json
{
  "foo": "bar",
  "broken": true
}
```

The final machine receipt recorded:

```text
fulfilment_validation.valid = true
fulfilment_validation.reason = exact repaired data matched
proof3_complete = true
```

## What this supports

This experiment directly supports the statement that an Atinamos-operated buyer can:

```text
receive task + budget + policy
→ independently discover external sellers
→ check exact invocation-route viability
→ query published independent evidence
→ apply buyer-owned procurement policy
→ select an eligible seller without human seller selection
→ make a bounded live x402 payment
→ consume the seller result
→ objectively validate the purchased output
→ complete the task
```

It also demonstrates that evidence can legitimately produce either a purchase or a no-purchase outcome depending on the buyer's policy.

## What this does not support

This experiment does **not** establish that:

- Keyronne, FenixFoundry, API Acre or any other provider will always succeed in the future;
- an endpoint that returned 404 during one observation is permanently broken;
- Atinamos provides a universal safe/unsafe verdict;
- every autonomous buyer should use the same procurement policy;
- an unrelated external buyer has independently adopted or purchased Atinamos in the wild;
- Atinamos JSON Repair was discoverable in Bazaar at the time of this experiment.

A separate read-only Bazaar check performed after the Proof #3 candidate search found **Atinamos Render Check** indexed, but did not find the newer Atinamos JSON Validate / Repair service. That is a seller-discoverability issue and is separate from the validity of Proof #3.

## Publication boundary

This public record deliberately omits private credentials, buyer wallet identity, payment-recipient account details, internal hostnames, AWS authentication details, private database/runtime information, operational source code and unpublished verification/challenge-generation techniques.

The private Atinamos repositories remain the operational source of truth. This repository contains the deliberately sanitised public research record.

## Public artefacts

- [Sanitised Proof #3 experiment record](../experiments/2026-08-28-proof3-autonomous-buyer/README.md)
- [Sanitised final buyer receipt](../experiments/2026-08-28-proof3-autonomous-buyer/public-receipt.json)
- Human-readable research: https://verify.atinamos.co.uk/

## Conclusion

> **Proof #3 is complete: an Atinamos-operated autonomous buyer independently discovered external sellers, used published verification evidence and its own policy to select one, made a bounded real payment, consumed the result and exactly validated the purchased output without a human naming the seller.**

The separate market-adoption question remains open: will unrelated external agents independently discover and buy Atinamos services without Atinamos operating the buyer?
