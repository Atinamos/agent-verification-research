# Technical SEO Crawl — controlled paid production run

**Observed:** 28 August 2026  
**Service:** Atinamos Technical SEO Crawl  
**Endpoint:** `https://agent.atinamos.co.uk/agent/technical-seo-crawl`

> **Evidence class:** controlled Atinamos seller/runtime experiment. This is not an independent Atinamos Verification classification and is not evidence of unrelated external buyer demand.

## Question

Can the live Atinamos Technical SEO Crawl complete the full machine-commerce path from x402 payment through asynchronous execution to publicly retrievable, hash-verifiable crawl evidence?

## Live contract observed

The production endpoint returned an x402 v2 payment requirement with:

```text
scheme: exact
network: eip155:8453 (Base mainnet)
asset: USDC
amount: 0.05 USDC
method: POST
settlement policy: settles_on_job_acceptance
```

The Bazaar extension described JSON input containing one required `url` field and an asynchronous response containing a job ID and `status_url`.

## Controlled payment

A bounded Atinamos-operated buyer made one production payment capped at 0.05 USDC.

```text
HTTP after paid retry: 202
payment: 0.05 USDC
transaction: 0x73f0b51abb0b7129c5b4f07cc14d5e0ef6162135b153176a2cc54e1dd9fa54b3
job: xr-e6143412c6084a999710fd0fbcfdbe64
```

The test target was `https://atinamos.co.uk/`.

The payment settled when the job was accepted. Later crawl completion is therefore a separate fulfilment observation; it is not implied by settlement.

## Fulfilment

The asynchronous worker completed the job:

```text
job status: completed
mission_status: COMPLETED
report_complete: true
failure_class: null
technical_result: PASS_WITH_WARNINGS
```

Coverage returned:

```text
crawl target limit: 250
pages processed: 17
HTML pages audited: 17
remaining URLs: 0
rate-limited targets: 0
other inaccessible targets: 0
coverage status: COMPLETE
```

The website findings contained zero errors and four warnings: one `META_DESCRIPTION_LENGTH` warning and three `TITLE_LENGTH` warnings.

A `PASS_WITH_WARNINGS` website result is not a seller-execution failure. Service fulfilment is represented by `mission_status=COMPLETED` together with `report_complete=true`.

## Public artifacts and integrity check

The worker published both artifacts:

- `https://atinamos.co.uk/render-results/xr-e6143412c6084a999710fd0fbcfdbe64-b9686859/result.json`
- `https://atinamos.co.uk/render-results/xr-e6143412c6084a999710fd0fbcfdbe64-b9686859/report.html`

A later public retrieval returned HTTP 200 for both files.

The downloaded `result.json` was 33,306 bytes and its SHA-256 matched the hash emitted by the worker exactly:

```text
df7230bc1c457cc4bf9d676d8a3ec3ff84a809070fec0501a02fc41e5f495ac6
```

## Machine-facing publication

Following deployment, the Atinamos Agent Shop homepage showed Technical SEO Crawl as live at 0.05 USDC. The public catalogue contained four live Shop services and exposed the MCP tool name `technical_seo_crawl` for this service.

The four live catalogue entries observed were:

```text
render-check         0.25 USDC
buyer-check          0.10 USDC
json-repair          0.005 USDC
technical-seo-crawl  0.05 USDC
```

## Coinbase Bazaar status at the recorded check

A read-only Coinbase Bazaar discovery query performed shortly after the first settled Technical SEO transaction returned `FOUND: NO` for this exact endpoint.

That observation is retained as-is. It does **not** establish that the resource will remain absent. Bazaar discovery is an external indexed/cached surface and should be checked again independently rather than inferred from the successful payment or local catalogue state.

No additional payment was made merely to influence indexing.

## What this run supports

This controlled run directly supports that, under the recorded production conditions:

```text
live x402 contract
→ bounded Base-mainnet USDC payment
→ job accepted
→ Ubuntu worker execution
→ bounded 17-page crawl
→ completed result
→ public JSON + HTML artifacts
→ exact SHA-256 integrity verification
```

It also supports that Technical SEO Crawl is exposed through the live Atinamos Shop catalogue and MCP catalogue.

## What this run does not support

This run does **not** prove:

- unrelated third-party buyer adoption;
- autonomous external demand for the service;
- Coinbase Bazaar indexing at the time of the recorded check;
- permanent future availability or performance;
- an independent Atinamos Verification classification for this Atinamos-owned seller endpoint;
- a universal trust or quality verdict about the target website.

The transaction was a deliberately controlled self-funded production test. It should not be counted as external revenue or independent customer demand.
