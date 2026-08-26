# Security and scope

The public Atinamos Evidence MCP is intentionally read-only.

Its purpose is to let external AI agents and developers consume selected published evidence without exposing Atinamos operational systems.

## Public MCP boundary

The MCP does not expose tools that:

- access wallet private keys or seed material;
- create payment authorisations;
- sign or submit payments;
- trigger paid verification runs;
- create, edit or delete services;
- mutate evidence records;
- write to the verification database;
- expose private infrastructure details;
- expose unpublished anti-abuse or challenge-generation logic.

## Data scope

MCP v1 reads the published Atinamos evidence corpus.

That corpus is deliberately narrower than the private Atinamos registry and operational evidence systems. Public records are selected and sanitised for publication.

A service being absent from MCP search therefore means only that no matching published Atinamos evidence is currently exposed through this interface. It does not establish that Atinamos has never observed the service elsewhere.

## Evidence semantics

Atinamos reports what was observed under recorded test conditions.

A published observation should not be promoted to a stronger claim than the evidence supports. In particular:

- a successful run is not a permanent reliability guarantee;
- a failed run is not a permanent declaration that a service is unsafe;
- repeated Atinamos tests are not evidence of independent customer demand;
- unknown evidence is not evidence of failure;
- an eligibility result is only an evaluation against the caller's supplied policy.

## No purchase authority

The public MCP cannot spend funds and cannot make purchases.

An external buying agent remains responsible for its own wallet controls, budgets, payment permissions and procurement decisions.

## Endpoint

```text
https://verify.atinamos.co.uk/mcp
```

The endpoint is hosted as part of the existing Atinamos Verification web service. The public backend implementation is not published in this repository.
