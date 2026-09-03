# Atinamos Independent Assurance Record — Ashlar Blue

**Observation date:** 2026-09-03  
**Provider:** Ashlar Blue  
**Scope:** Public x402 discovery, facilitator, MCP, deterministic evidence and hardware-attestation assurance path  
**Payment made:** No  
**Classification:** `independent_assurance_partial`

## Independence statement

Ashlar Blue invited Atinamos to test its public facilitator infrastructure and inspect its hardware-attested evidence model. The invitation did not alter the test method, evidence threshold or result.

Atinamos applied the same rule used for unrelated services: claims were separated from direct observations, independently reproducible verification, inference and unavailable evidence.

## Core result

Atinamos independently confirmed Ashlar's x402 DNS discovery record, public x402 manifest and substantive published `@ashlar-blue/x402-trust` SDK.

At the observation time, Atinamos did not independently reproduce a live facilitator capability response, operational advertised MCP endpoint or independently checkable current Intel TDX attestation from the public evidence path.

Ashlar's own published resolver returned:

```text
via: dns-txt
attestationUsable: false
liveCheck: unreachable
```

## Timestamped observations

### 2026-09-03T07:10:59Z — public x402 manifest

`https://ashlar.blue/.well-known/x402` returned HTTP 200 JSON.

Observed facilitator block:

```text
baseUrl: https://ashlar.blue/api
supported: /supported
verify: /verify
settle: /settle
```

Advertised kinds:

```text
exact / eip155:14
exact / eip155:114
exact / xrpl:mainnet
```

The manifest also advertised an `attested-identity` extension and an allowed measurement root:

```text
0x7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069
```

### 2026-09-03T07:12:24Z — live `/supported`

Manifest-derived URL:

```text
https://ashlar.blue/api/supported
```

returned HTTP 200 with `text/html` containing the public Ashlar website rather than a machine-readable `kinds[]` capability response.

### 2026-09-03T07:15:52Z to 07:17:30Z — invited API hostname

`https://api.ashlar.blue/supported` could not be resolved.

Independent A and CNAME DNS queries for:

```text
api.ashlar.blue
```

returned `NXDOMAIN` from the Atinamos test environment.

### 2026-09-03T07:18:36Z — MCP manifest

`https://ashlar.blue/.well-known/mcp.json` returned HTTP 200 JSON and advertised:

```text
endpoint: https://ashlar.blue/api/mcp
protocol: jsonrpc-2.0
```

### 2026-09-03T07:19:10Z — MCP GET

`GET https://ashlar.blue/api/mcp` returned HTTP 200 `text/html` containing the public website.

### 2026-09-03T07:20:29Z — MCP JSON-RPC POST

A harmless JSON-RPC `initialize` POST to the advertised endpoint returned:

```text
HTTP/2 405
content-length: 0
```

No MCP tool was invoked and no state-changing operation was attempted.

## Published SDK preservation

Package:

```text
@ashlar-blue/x402-trust 0.5.2
```

Npm archive SHA-256 retained by Atinamos:

```text
81129897dc41171c01ab8766317761a3e4bdcb951c7b09f71f9432b497188f1a
```

The package contains implementations for discovery, evidence references, facilitator configuration, registry badges, Merkle transcripts, MCP and trust evaluation.

## `x402ev/1`

The published package implements:

```text
x402ev/1; digest=<alg>:<hex>[; anchor=<caip2>:<contract>:<record>][; ref=<uri>]
```

Observed implementation properties include:

- mandatory digest;
- canonical field ordering;
- SHA-256/SHA-384/SHA-512 digest parsing;
- digest-based evidence identity rather than URL identity;
- canonical JSON hashing intended for RFC 8785/JCS evidence processing.

Atinamos confirmed the implementation exists. RFC 8785 conformance across all edge cases was not independently certified in this observation.

A current live `x402ev/1` evidence artefact suitable for independent digest recomputation was not reached through the tested public path.

## Ashlar resolver against Ashlar

Atinamos executed the preserved Ashlar `resolveX402()` implementation against `ashlar.blue` with cache disabled.

The package successfully resolved the DNS record and public manifest, then returned:

```json
{
  "manifestUrl": "https://ashlar.blue/.well-known/x402",
  "via": "dns-txt",
  "attestationUsable": false,
  "liveCheck": "unreachable"
}
```

This independently reproduced, using Ashlar's own published resolver, the live facilitator condition previously observed manually.

## Hardware-attestation claims

The public Ops page exposed claims including:

```text
Node: tdx-us-east-01
Status: TDX MKTME ACTIVE
Silicon: Intel Xeon Scalable 4th Gen (TDX v4)
MRTD Hash: 0x7f83...9069
Quote Authority: Intel Root CA (Verified)
Ledger DA Anchor: Flare DA Block #18492810
```

These claims were directly observed in Ashlar's HTML. Atinamos did not locate through the tested path:

- raw TDX quote bytes;
- Intel PCS/PCK collateral;
- a full certificate/quote-validation chain;
- a current verifier URL capable of independent reproduction;
- a complete evidence reference tying the displayed node claim to an independently retrievable artefact.

The public manifest did not contain the top-level `attestation` structure required by the published resolver for `attestationUsable = true`.

## Historical badge model

The package documents the Coston2 registry:

```text
0xb02f83e994830C4954c89C10482665A3963229c5
```

and badge kind:

```text
x402-facilitator-attested
```

The SDK appropriately separates:

```text
verified        — historical registry verification
liveAttestation — current manifest state
attestedNow     — both conditions true
```

The documented example requires:

```text
r.manifest.badges.subject
```

as the subject address. The observed live manifest contained no `badges` block, and the inspected package did not expose the Ashlar subject address elsewhere. The historical registry lookup therefore could not be independently reproduced from the current discovery chain alone.

## Public UI verification controls

### Ops “Re-Verify All Quotes”

Inspection of the live page JavaScript showed that the button performs no quote retrieval or cryptographic verification. It uses `setTimeout()` and unconditionally changes its label to:

```text
✓ All 4 Clusters Verified Valid
```

This was recorded as a presentation-layer action, not a quote-verification result.

### Developer Lab

The live source explicitly labels the implementation:

```text
Sandbox Audit Simulator Logic
```

`runSandboxAudit()` selects predefined `genuine`, `tampered` and `replay` scenarios and emits predetermined Intel CA, MRTD, JCS and verdict messages after timers.

No observable network request, quote parsing, certificate-chain validation, MRTD derivation, nonce computation, signature verification or Flare lookup occurred in that function.

The lab was therefore classified as a simulation of verification outcomes, not evidence that cryptographic verification occurred.

## MCP attestation-entry tool

The published MCP handler `x402_verify_attestation_entry` accepts:

```text
entry
index
size
proof
outputRoot
```

and invokes `verifyEntry(...)` to verify Merkle inclusion.

This can prove that a supplied record belongs to a committed Merkle tree. It does not independently validate the underlying raw Intel TDX quote.

A package-wide search of the published runtime distribution did not identify a separate raw Intel TDX quote parser/verifier implementing Intel collateral, QE identity, TDREPORT/MRTD derivation or quote-freshness verification.

## Claim / observation / result summary

| Claim area | Independent observation | Result |
| --- | --- | --- |
| x402 DNS discovery | TXT record retrieved and parsed | Confirmed |
| Public x402 manifest | HTTP 200 JSON retrieved | Confirmed |
| Advertised `/supported` | Returned website HTML; Ashlar resolver reports `unreachable` | Not confirmed live |
| `api.ashlar.blue` | A and CNAME returned NXDOMAIN | Not reachable at observation time |
| Advertised MCP endpoint | GET website HTML; JSON-RPC POST HTTP 405 | Not operational as advertised |
| Current independently checkable attestation | Ashlar resolver reports `attestationUsable: false` | Not confirmed |
| Active Intel TDX state | Node/status/authority/anchor displayed by Ashlar | Claim observed; not independently verified |
| Historical badge | Registry and kind documented; subject not derivable from current manifest | Partially reproducible |
| `x402ev/1` format | Implemented in npm package | Confirmed implementation |
| Live evidence digest | No suitable current artefact reached for independent recomputation | Not tested |
| Ops re-verification UI | Timer-driven unconditional success | Not a cryptographic verifier |
| Developer Lab audit | Explicit simulator with predetermined results | Simulation |
| MCP attestation-entry verification | Merkle membership verification | Confirmed, narrower than raw TDX verification |

## Atinamos conclusion

> **Ashlar Blue publishes meaningful x402 discovery and evidence-verification architecture, but the public deployment observed on 3 September 2026 did not provide Atinamos with a complete reproducible path to several of its strongest live facilitator and Intel TDX assurance claims.**

This record does not assert dishonesty, intent, permanent failure or universal untrustworthiness. It records the public evidence path an unrelated verifier could independently reach at the stated observation time.

**You can pay to be tested. You cannot pay to be trusted.**
