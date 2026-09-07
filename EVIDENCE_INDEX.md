# Atinamos Public Evidence Index

**Published:** 23 August 2026  
**Updated:** 7 September 2026

> **You can pay to be tested. You cannot pay to be trusted.**

This index links the public technical evidence produced from Atinamos direct verification and Assurance observations.

Each entry is a timestamped record of specific tested behaviour. It is not a permanent provider rating, certification, approval or safe/unsafe verdict.

## Current evidence summary

| Date | Exact service / experiment | Settlement | Fulfilment | Independent interpretation |
| --- | --- | --- | --- | --- |
| 7 Sep 2026 | `POST https://keyronne.com/api/json-repair` | 0.001 USDC independently observed on Base | Advertised JSON deliverable observed; `FULFILLED` | Generic fulfilment only; correctness and quality `NOT_EVALUATED`; signed receipt published |
| 6 Sep 2026 | `POST https://api.ibanforge.com/v1/iban/validate` | 0.010 USDC total across 2 paid controls, independently observed on Base | 2/2 observed | Returned `valid` matched independent ISO 13616 MOD-97 expectations for positive + negative controls; 2 signed receipts |
| 3 Sep 2026 | `POST https://code402.dev/v1/tools/lei-check/call` | Two bounded EOA settlements observed | 2 successful paid fulfilments | Positive + negative ISO 7064 MOD-97-10 controls matched expectations; separate smart-account interoperability observation retained |
| 22 Aug 2026 | x402Node JSON Repair | 0.006 USDC observed | observed | 4/4 published assertions passed |
| 22 Aug 2026 | x402.direct Service Directory Search | no 0.001 USDC settlement observed after authorised paid-path failure | not observed; HTTP 500 | validation not reached |
| 22 Aug 2026 | x402engine Web Screenshot | 0.01 USDC observed | observed; HTTP 200 | primary screenshot artefact failed strict base64/PNG validation |

Observation counts are sample counts, not reliability percentages.

---

## 7 September 2026 — Keyronne unattended generic Assurance

Atinamos completed its first unattended generic external Assurance execution from an already-prepared frozen plan against:

```text
POST https://keyronne.com/api/json-repair
```

Runner record:

```text
run:     1b5bc844-368c-445a-8f84-e62be6d88baa
adapter: generic-transaction-fulfilment v1.0
state:   PLAN_FROZEN → COMPLETE
```

One internal production coordinator invocation handled the routine execution stages without an operator manually stepping challenge acquisition, signing, payment, settlement observation, fulfilment evaluation or Verification publication.

Observed paid execution:

```text
amount:    0.001 USDC
network:   Base / eip155:8453
x402:      v2 exact
paid HTTP: 200
```

Independent Base settlement:

```text
transaction: 0xc42bb177c41d21a56e9d3c02546fa8ebeda911cff3bc1139169a61c89f7b495c
block:       50996015
```

Observed evidence layers:

```text
PAYMENT       SETTLED
FULFILMENT    FULFILLED
CORRECTNESS   NOT_EVALUATED
QUALITY       NOT_EVALUATED
```

The public contract advertised JSON fields including `repairs` and `value`; the paid response returned the advertised kind of JSON deliverable. No independent semantic-correctness method was applied.

Signed Evidence Receipt:

```text
atinamos:receipt:10e40afd-f6b1-57bd-9c1e-0a4a1695a428
```

- [Technical experiment record](experiments/2026-09-07-keyronne-unattended-generic-assurance/README.md)
- Human-readable research record: `https://verify.atinamos.co.uk/research/unattended-generic-assurance-keyronne/`
- Signed receipt: `https://verify.atinamos.co.uk/assurance/receipts/atinamos:receipt:10e40afd-f6b1-57bd-9c1e-0a4a1695a428/`

**Supports:** one real third-party x402 purchase, independent Base settlement observation, observed advertised deliverable shape, unattended progression of an already-frozen run through routine paid execution/publication, and signed evidence publication.

**Does not support:** factual/semantic correctness of the repaired JSON, subjective quality, permanent reliability, provider-wide trust, certification, approval, or proof that the complete raw-URL seller journey is already unattended.

---

## 6 September 2026 — IBANforge deterministic commissioning

Exact service:

```text
POST https://api.ibanforge.com/v1/iban/validate
```

This was the first complete external deterministic commissioning of the current Assurance Runner → Verification publication path.

Controlled fixtures:

```text
DE89370400440532013000 → expected valid=true  → observed valid=true
DE90370400440532013000 → expected valid=false → observed valid=false
```

Independent method:

```text
ISO 13616 MOD-97
```

Observed:

```text
0.005 USDC per control
total observed test spend:    0.010 USDC
Base settlements observed:    2
successful fulfilments:       2
independent controls passed:  2 / 2
signed Assurance receipts:    2
```

Signed receipts:

```text
atinamos:receipt:a6caf2c0-4f56-545b-ba8a-e62d0379b085
atinamos:receipt:c9f7dc76-898d-5d95-9dfc-388055750c58
```

- [Technical experiment record](experiments/2026-09-06-ibanforge-assurance-commissioning/README.md)

**Supports:** two timestamped paid external controls, independent settlement observation, useful fulfilment, narrow independent MOD-97 correctness comparison of the returned `valid` field and signed publication.

**Does not support:** universal IBAN correctness, correctness of unrelated enrichment fields, permanent reliability, provider-wide trust or unattended autonomy for this specific 6 September commissioning run.

The later Keyronne run supplied the subsequent unattended generic proof.

---

## 3 September 2026 — code402 LEI Check assurance series

Exact service:

```text
POST https://code402.dev/v1/tools/lei-check/call
```

The series retained:

- the original payment-contract observation;
- two bounded EOA purchases whose positive and negative checksum results matched independent ISO 7064 MOD-97-10 expectations;
- one Circle smart-account pre-settlement payment-interoperability observation.

Current retained summary:

```text
observations: 4
paid tests: 2
successful fulfilments: 2
failed fulfilments: 0
payment interoperability issues: 1
```

- [Completed technical experiment record](experiments/2026-09-03-code402-lei-check/README.md)
- [Machine-readable evidence series](experiments/2026-09-03-code402-lei-check/evidence.json)
- [Preserved original Phase-1 evidence](experiments/2026-09-03-code402-lei-check/evidence-phase1.json)

A pre-settlement smart-account interoperability issue is not counted as seller fulfilment failure.

---

## 22 August 2026 — x402Node JSON Repair

Atinamos independently exercised and paid the externally owned x402Node JSON Repair service, observed settlement and fulfilment and applied four objective output assertions. All four passed.

- [Technical experiment record](experiments/2026-08-22-x402node-json-repair/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402node-json-repair/verification-receipt.json)

Classification:

```text
settled_fulfilment_valid
```

---

## 22 August 2026 — x402.direct Service Directory Search

Atinamos observed a live x402 v1 payment requirement and sent the authorised request. HTTP 500 was returned; subsequent read-only chain reconciliation found no 0.001 USDC settlement and no fulfilment result was returned.

- [Technical experiment record](experiments/2026-08-22-x402direct-search/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402direct-search/verification-receipt.json)

Classification:

```text
pre_settlement_paid_path_failure
```

This does not establish that the provider always fails or that payment was taken without delivery.

---

## 22 August 2026 — x402engine Web Screenshot

Atinamos paid 0.01 USDC, independently observed settlement and received HTTP 200 with metadata matching the controlled target. The primary screenshot value failed the published strict base64/PNG artefact assertion.

- [Technical experiment record](experiments/2026-08-22-x402engine-web-screenshot/README.md)
- [Sanitised verification receipt](experiments/2026-08-22-x402engine-web-screenshot/verification-receipt.json)

Classification:

```text
settled_fulfilment_contract_invalid
```

This is an observation about that invocation, not a provider-wide unsafe/untrustworthy claim.

---

## Related buyer/procurement proof — Proof #3

Proof #3 is intentionally separate from the provider evidence table because it was a controlled buyer/procurement experiment.

On 28 August 2026, an Atinamos-operated bounded buyer completed:

```text
external marketplace discovery
→ exact-route non-paying preflight
→ published Atinamos evidence lookup
→ buyer-owned procurement policy
→ autonomous seller selection
→ bounded x402 payment
→ seller fulfilment
→ exact result validation
```

Final seller: Keyronne JSON Repair. Final spend: 0.001 USDC.

- [Proof #3 research note](research/2026-08-28-proof3-autonomous-buyer.md)
- [Proof #3 experiment record](experiments/2026-08-28-proof3-autonomous-buyer/README.md)
- [Sanitised final buyer receipt](experiments/2026-08-28-proof3-autonomous-buyer/public-receipt.json)

This demonstrates the controlled Atinamos buyer flow. It does not establish broad external-agent adoption.

---

## External commercial-use observation — Atinamos JSON Repair

On 28 August 2026, Atinamos observed an unrelated external client purchase Atinamos JSON Repair for 0.005 USDC through x402 and receive HTTP 200 fulfilment.

- [Research note](research/2026-08-28-first-external-commercial-purchase.md)
- [Sanitised experiment record](experiments/2026-08-28-external-json-repair-purchase/README.md)
- [Sanitised public evidence](experiments/2026-08-28-external-json-repair-purchase/public-evidence.json)

This establishes external commercial use of an Atinamos machine service. It does not establish that the buyer was definitely an autonomous AI agent.

---

## Interpretation rules

The current Assurance evidence model keeps these layers separate:

```text
PAYMENT
FULFILMENT
CORRECTNESS
QUALITY
```

Do not infer a later layer from an earlier one.

```text
UNKNOWN != UNSAFE
SETTLED != FULFILLED
FULFILLED != CORRECT
CORRECT != HIGH QUALITY
SIGNED RECEIPT != PERMANENT TRUST
SAMPLE COUNT != RELIABILITY PERCENTAGE
```

Endpoint and HTTP method are material evidence identity where applicable.

## Machine-readable Assurance evidence

```text
GET https://verify.atinamos.co.uk/v1/assurance/evidence?endpoint=<service-url>&method=<HTTP_METHOD>
GET https://verify.atinamos.co.uk/v1/assurance/receipts/<receipt_id>
```

The read-only Evidence MCP is available at:

```text
https://verify.atinamos.co.uk/mcp
```

## Provenance rule

Direct-verification records above are Atinamos observations backed by retained internal evidence and deliberately published technical records or signed receipts.

Material obtained from third-party marketplaces, registries or external evidence sources must be labelled as external and must not be presented as an Atinamos direct observation.

If Atinamos has no relevant published observation for a service, the correct statement is only:

> **Atinamos holds no evidence.**
