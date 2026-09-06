# Schemas

Public machine-readable schemas for deliberately published Atinamos verification evidence.

Only reviewed public schemas belong here. Internal verifier models, implementation-specific database schemas and anti-gaming fields remain private.

## Current public formats

`verification-receipt-v1.schema.json` defines the original public verification-receipt projection used by earlier published experiments.

Production Assurance now also publishes a newer signed Evidence Receipt envelope with canonical signed content, content commitment, signing-key identity and explicit integrity metadata. That newer production format is intentionally treated as a distinct generation rather than silently rewriting historical v1 receipts.

Historical receipts remain valid evidence in the format in which they were published.

## Versioning rule

Future machine-evidence tightening should be additive and versioned. In particular:

- signed historical evidence must not be mutated to imitate a newer schema;
- `true`, `false`, `null` and absent must remain distinct;
- fulfilment and independent correctness should remain separate concepts;
- the exact tested capability and verified output field(s) should be machine-readable where published evidence supports them;
- seller-performance evidence, verifier/system failure and payment interoperability should remain separately attributable;
- observation counts must not be represented by Atinamos as a permanent reliability percentage;
- buyer procurement policy remains external to the evidence record.

See [Machine-Evidence Schema Audit — 6 September 2026](../research/2026-09-06-machine-evidence-schema-audit.md) for the current compatibility and scope findings.
