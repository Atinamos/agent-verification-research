# First Observed External Commercial Purchase of an Atinamos Service

**Published:** 28 August 2026  
**Status:** CONFIRMED EXTERNAL COMMERCIAL PURCHASE

> **You can pay to be tested. You cannot pay to be trusted.**

## Summary

On 28 August 2026, Atinamos observed a paid x402 purchase of its JSON Repair service from an external client that was not part of the controlled Atinamos buyer experiments.

The observed sequence was:

```text
external request
→ HTTP 402 payment requirement
→ Coinbase x402 verification succeeded
→ Coinbase x402 settlement succeeded
→ paid service request returned HTTP 200
→ 0.005 USDC settlement observed on Base
```

The public record deliberately redacts the client IP address and does not publish Atinamos payment-recipient account details.

## Observed transaction

```text
Service: Atinamos JSON Repair
Route: /agent/json-repair
Network: Base mainnet (eip155:8453)
Asset: USDC
Amount: 0.005 USDC
Transaction: 0x00482f136e90f01053699dd6c48b8c0e6e7f0b3598510c83654a1b77a562316b
Base block: 50572244
```

The Base transaction succeeded and transferred 0.005 USDC to the configured Atinamos payment destination.

## Server-side evidence

The retained server logs show the following timestamps in UTC:

```text
16:17:11.481  external client POST /agent/json-repair → 402 Payment Required
16:17:12.429  Coinbase CDP x402 /verify → 200 OK
16:17:13.610  Coinbase CDP x402 /settle → 200 OK
16:17:13.850  external client POST /agent/json-repair → 200 OK
```

The corresponding Base settlement was recorded seconds later.

The source IP is retained privately as part of the raw operational evidence but is redacted from this public record.

## Why this is classified as external commercial use

Atinamos checked the event against its controlled buyer/test activity and documented wallets.

The payment was not identified as one of the known controlled ACP buyer flows, and the payer associated with the on-chain transfer did not match the documented Atinamos experimental buyer wallets reviewed during the investigation.

The server log also records the characteristic x402 sequence expected from a real paid client: an initial 402 response, successful payment verification and settlement, followed by a successful HTTP 200 service response.

For that reason, the narrow classification supported by the evidence is:

> **confirmed external commercial purchase**

## Earlier probing from the same external source

Before the successful purchase, the same external source had probed several Atinamos paid service routes and received HTTP 402 responses, including JSON Repair, Technical SEO Crawl and Buyer Check.

Later, that source returned to JSON Repair and completed the paid request.

This is consistent with a machine client inspecting available paid services before selecting one, but the logs do not prove how the selection decision was made.

## What this supports

This observation supports the statement that:

- an unrelated external client reached an Atinamos paid x402 service;
- the client supplied a valid payment authorisation;
- Coinbase x402 verification and settlement succeeded;
- 0.005 USDC settlement was observed on Base;
- Atinamos returned the paid JSON Repair service with HTTP 200;
- the event was not identified as one of the documented Atinamos controlled buyer tests.

This is therefore the first Atinamos record classified as **external commercial use** rather than a controlled buyer experiment.

## What this does not support

This observation does **not** establish that:

- the external client was definitely an independently autonomous AI agent;
- the client independently discovered Atinamos through a particular marketplace;
- an LLM or other AI system made the final procurement decision;
- the same client will purchase again;
- Atinamos has broad market adoption;
- JSON Repair will always fulfil successfully.

The evidence establishes external commercial use. Autonomous-agent identity or decision provenance remains unproven.

## Relationship to Proof #3

Earlier on 28 August 2026, Atinamos completed Proof #3: an **Atinamos-operated** autonomous buyer independently discovered external sellers, applied published verification evidence and buyer-owned policy, selected a seller, paid and validated the result.

That Proof #3 record explicitly left a separate market-adoption question open: whether an unrelated external buyer would independently purchase an Atinamos service.

This observation closes the narrower commercial-use part of that question: **an unrelated external client did purchase Atinamos**.

It does not yet close the stronger autonomous-agent provenance question.

## Publication boundary

This public record intentionally omits:

- source IP address;
- Atinamos payment-recipient account details;
- private runtime configuration;
- internal filesystem paths;
- credentials or authentication material;
- unpublished operational or anti-gaming techniques.

The private Atinamos operational repositories and raw logs remain the source of truth.

## Public artefacts

- [Sanitised experiment record](../experiments/2026-08-28-external-json-repair-purchase/README.md)
- [Sanitised machine-readable evidence](../experiments/2026-08-28-external-json-repair-purchase/public-evidence.json)
- Human-readable research: https://verify.atinamos.co.uk/research/first-external-commercial-purchase/

## Conclusion

> **On 28 August 2026, Atinamos observed its first confirmed external commercial purchase: an unrelated external client paid 0.005 USDC via x402 for Atinamos JSON Repair, settlement completed on Base, and the paid service returned HTTP 200.**

The stronger claim — that an independently autonomous AI agent made the procurement decision — remains open pending evidence of buyer identity or decision provenance.
