# Atinamos Evidence MCP

The Atinamos Evidence MCP is the public, read-only machine interface to selected published Atinamos verification evidence.

**MCP endpoint:** `https://verify.atinamos.co.uk/mcp`  
**Official MCP Registry name:** `uk.co.atinamos/evidence`  
**Registry version:** `1.0.0`  
**Registry status:** `active`

The server was published to the official Model Context Protocol Registry on 26 August 2026 using HTTP domain verification for `atinamos.co.uk`.

It is intended for AI agents, agent frameworks and developers that want to query Atinamos evidence before making their own procurement or risk decision.

> **Atinamos provides the evidence. The buyer owns the policy and decision.**

The MCP does not return a universal trust or safety rating. It exposes timestamped observations and can evaluate those observations against procurement rules supplied by the caller.

## Important scope boundary — read this before using MCP v1

> **MCP v1 does not query the full private Atinamos registry or operational database.**
>
> It currently reads only the **selected, sanitised evidence that Atinamos has deliberately published**. This is an intentional production boundary while the public interface, evidence semantics and buyer-policy behaviour are being proven in live use.
>
> **A result of `known: false`, an empty search result, or a policy result caused by missing published evidence does not mean Atinamos has never observed the service. It means the service is not represented in the current published MCP evidence corpus.**

The private Atinamos catalogue is broader than the public MCP corpus. Private catalogue presence, marketplace observations and unpublished verification material are not automatically exposed through MCP v1.

This boundary prevents the public interface from silently exposing internal research, operational records or evidence that has not crossed the publication boundary.

As the interface is proven, the intended direction is for MCP to expose an approved public subset of the wider Atinamos evidence registry. Until then, callers should treat MCP results as **published-evidence results**, not as an exhaustive search of everything Atinamos may hold privately.

## Current tools

- `lookup_evidence(endpoint)` — return the published Atinamos evidence held for a service route.
- `service_history(endpoint)` — return timestamped published observations for a service route.
- `search_services(query, limit)` — search services represented in the published Atinamos evidence corpus.
- `evaluate_policy(endpoint, policy)` — evaluate the published evidence against caller-supplied procurement rules.

## Start here

- [Quick start](QUICKSTART.md)
- [Tool reference](TOOLS.md)
- [Buyer policy reference](BUYER_POLICY.md)
- [Security and scope](SECURITY.md)
- [MCP Inspector examples](examples/INSPECTOR.md)
- [Example responses](examples/RESPONSES.md)
- [Buyer policy JSON Schema](schemas/buyer-policy.schema.json)
- [Official Registry metadata](server.json)

## What this MCP currently reads

MCP v1 reads the **published Atinamos evidence corpus**. It does not expose every private registry or operational database record.

Published evidence is selected and sanitised according to the repository publication policy. The public evidence corpus intentionally retains both successful and unsuccessful observations.

## What it does not do

The public MCP does not:

- hold or expose wallet credentials;
- create or sign payments;
- trigger paid verification runs;
- mutate verification evidence;
- write to the Atinamos verification database;
- make a purchase on behalf of the calling agent;
- declare a service permanently trusted or safe;
- provide an exhaustive search of the private Atinamos catalogue.

## Evidence interpretation

A returned observation supports only the claims demonstrated by that observation and its recorded test conditions. A successful observation is not a permanent reliability guarantee, and an unsuccessful observation is not a permanent declaration that a service is unsafe.

Likewise, **absence from MCP v1 is not negative evidence about a service**. It may simply mean Atinamos has not selected and published evidence for that service through the public MCP corpus.

For the evidence model and classifications, see the repository's public methodology and verification receipt specification.
