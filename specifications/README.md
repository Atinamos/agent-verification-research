# Specifications

Public technical specifications and interfaces for consuming Atinamos verification evidence.

Specifications published here should describe externally consumable contracts and evidence formats without exposing private verifier implementation or operational infrastructure.

## Published specifications

- [Public Verification Receipt Specification v1.0](public-verification-receipt-v1.md) — field semantics, null/unknown handling, interpretation rules, classification use and sanitisation boundaries for the original public Atinamos verification-receipt projection.
- [Verification Receipt v1 JSON Schema](../schemas/verification-receipt-v1.schema.json) — machine-readable schema used by earlier published receipt examples.

Production Assurance also publishes a newer signed Evidence Receipt envelope with canonical signed content, content commitment, signing-key identity and explicit integrity metadata. It is a separate generation of evidence representation rather than a silent replacement of historical v1 records.

Historical receipts remain valid in the format in which they were published. Any future public machine schema should therefore be versioned and additive.

The specification and schema should be read together with the [Evidence & Classification Methodology v1.0](../methodology/evidence-and-classification.md).

For the current review of machine-readable scope, correctness, attribution, limitation and observation-count semantics, see [Machine-Evidence Schema Audit — 6 September 2026](../research/2026-09-06-machine-evidence-schema-audit.md).
