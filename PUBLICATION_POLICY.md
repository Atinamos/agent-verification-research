# Public Repository Publication Policy

This repository contains only deliberately selected and sanitised Atinamos technical publication material.

## Source of truth

The private Atinamos repository is the source of truth. Nothing is copied automatically from private repositories into this public repository.

Every public item must be reviewed and explicitly classified for publication before it is added here.

## Allowed material

Suitable material may include:

- public evidence schemas;
- sanitised verification receipts;
- sample API responses;
- public methodology;
- public experiment datasets;
- public research notes;
- integration examples;
- buyer evidence-query examples;
- interface/specification documents.

## Prohibited material

Do not publish:

- operational Atinamos source code;
- verifier implementation;
- Render Check implementation;
- passwords, API keys or authentication tokens;
- wallet seed phrases or private keys;
- database credentials or private database details;
- private hostnames or internal IP addresses;
- unnecessary filesystem paths;
- private configuration;
- secrets contained in Git history;
- private transaction/account information;
- unpublished test techniques;
- challenge selection or challenge-generation logic;
- anti-gaming heuristics;
- internal anomaly detection;
- private recovery or operational documentation;
- implementation details intentionally retained to reduce manipulation risk.

## Public methodology boundary

Publish enough methodology that an independent reader can understand what an Atinamos verification means, what was observed, and the limitations of the evidence.

Do not necessarily publish future test cases, challenge selection, anti-gaming heuristics, or implementation details that would make manipulation easier.

A seller should understand the rules of the examination without receiving tomorrow's examination paper.

## Required safety check before every public push

Check specifically for:

- passwords;
- API keys;
- wallet seed/private keys;
- authentication tokens;
- database credentials;
- private hostnames;
- internal IP addresses;
- private database details;
- unnecessary filesystem paths;
- private email addresses;
- private configuration;
- secrets in Git history;
- private transaction/account information;
- unpublished test techniques;
- intentionally private implementation detail.

If uncertain, do not publish.

## Core principle

**Atinamos produces evidence. Trust is the conclusion the buyer reaches from that evidence.**

**You can pay to be tested. You cannot pay to be trusted.**
