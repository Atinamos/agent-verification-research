# Decision Delta Protocol v0.1 — Bias / Method Review

**Status:** pre-freeze review  
**Purpose:** record obvious methodological risks before live results exist.

## Risks identified before execution

1. **Policy-forced treatment effect** — if the buyer simply rejects unknown services, evidence-assisted runs are biased toward known services. Mitigation: permit bounded exploratory purchases below a frozen cap.
2. **Evidence leakage between conditions** — control and treatment must use isolated sessions and may not share prior decisions.
3. **Candidate-order bias** — order may be randomised between repetitions but must be identical within each matched pair.
4. **Atinamos self-preference** — primary scenarios should use independently owned external services wherever possible. Atinamos-owned services must be labelled and excluded from primary external-service claims.
5. **Outcome conflation** — settlement, fulfilment, correctness and quality must remain separate evidence dimensions.
6. **Endpoint identity ambiguity** — evidence identity must include HTTP method as well as endpoint when method changes service semantics.
7. **Stale-evidence bias** — evidence timestamp/freshness must be visible to the buyer policy. Historical positive evidence is not equivalent to current evidence.
8. **Failure-attribution bias** — seller failures, payment-path interoperability failures, verifier failures and buyer/harness failures must be classified separately.
9. **Cherry-picking scenarios** — scenario definitions and candidate snapshots must be frozen before live Decision Delta results are observed.
10. **Run inflation** — repeated runs within one scenario are clustered observations and must not be presented as independent market situations.
11. **Decision-change ≠ decision-improvement** — Decision Delta measures changed purchasing behaviour. Outcome Delta is reported separately where objectively measurable.
12. **Model generalisation** — v0.1 concerns one fixed buyer implementation/model configuration. It must not be generalised to all autonomous buyers.

## Review conclusion

No methodological blocker was found that requires abandoning the paired control/treatment design. The protocol is suitable to proceed to implementation provided the pre-run gates above are enforced before live spending.
