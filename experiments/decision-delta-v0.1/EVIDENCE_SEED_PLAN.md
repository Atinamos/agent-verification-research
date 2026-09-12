# Decision Delta v0.1 — Evidence Seed Plan

**Status:** PRE-RUN / PRE-PAYMENT DECLARATION  
**Declared:** 12 September 2026  
**Purpose:** acquire one fresh independent observation needed to complete the sixth primary Decision Delta scenario. The observation is evidence preparation, not a Decision Delta result.

## Selection rule

The target was selected before its verification outcome was known.

For the screenshot-artefact task, use the frozen external `web screenshot` search and objective task-fit filtering already documented in the Decision Delta candidate-selection rules.

Among the retained candidates, select the first externally ranked service which:

- has no applicable Atinamos evidence for the exact endpoint/method identity;
- is priced above the Balanced v0.1 unknown-service exploratory cap of 0.01 USDC;
- exposes a deterministic image artefact contract that can be independently checked;
- is executable on Base mainnet under the global service-price cap.

Under that predeclared rule the selected evidence-seed target is **Toolsmith / toolcall.click Web Screenshot**.

## Frozen target

- Provider: Toolsmith / toolcall.click
- Service: Web Screenshot
- Endpoint identity: `GET https://toolcall.click/t/web/screenshot`
- Test invocation: `https://toolcall.click/t/web/screenshot?full=1&url=https%3A%2F%2Fexample.com&width=1280`
- Network: `eip155:8453` (Base mainnet)
- Observed pre-payment challenge at preparation time: 0.015 USDC
- Maximum authorised service price for this seed: **0.015 USDC**
- Redirects: disabled
- Automatic paid retry after an indeterminate payment outcome: prohibited

If the live payment challenge is higher than 0.015 USDC, the seed attempt must stop before payment and the price drift must be recorded. It must not silently raise the cap.

## Assertions fixed before outcome

If a paid response is obtained, the verifier will separately record PAYMENT, FULFILMENT and CORRECTNESS/CONTRACT assertions.

The intended assertions are:

1. the paid invocation returns a successful service response;
2. the response contains an `imageBase64` value;
3. `imageBase64` is valid strict base64;
4. decoded bytes begin with the PNG signature `89 50 4E 47 0D 0A 1A 0A`;
5. the response identifies the image format as PNG where the field is present;
6. the returned URL corresponds to `https://example.com` where the field is present;
7. a non-zero artefact is returned.

These assertions test the advertised screenshot artefact contract. They do not claim aesthetic or rendering quality.

## Outcome handling

**Pass and failure are equally admissible.**

The seed observation must be retained if:

- payment settles and all assertions pass;
- payment settles but fulfilment fails;
- fulfilment occurs but an assertion fails;
- the payment path fails before settlement;
- the live contract has changed;
- settlement becomes indeterminate.

The observed outcome will not be rewritten to make the later Decision Delta scenario more interesting.

## Intended DD-06 candidate context

The predeclared screenshot candidate context is:

1. Toolsmith / toolcall.click — 0.015 USDC — currently no applicable Atinamos evidence;
2. x402engine — 0.010 USDC — historical Atinamos observation: settlement and fulfilment observed, screenshot artefact contract assertion failed;
3. Orthogonal — 0.030 USDC — currently no applicable Atinamos evidence.

The eventual DD-06 evidence snapshot will include the Toolcall seed observation exactly as observed, together with the already-held x402engine observation and the contemporaneous status of the remaining candidate. The buyer policy and candidate order will not be changed in response to the seed result.

## Research boundary

This paid verification is **not itself a Decision Delta pair** and must not be counted as a Decision Delta result. Its sole purpose is to create a fresh independent evidence observation before the sixth scenario is frozen.
