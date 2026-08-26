# Quick start

The public Atinamos Evidence MCP endpoint is:

```text
https://verify.atinamos.co.uk/mcp
```

It uses Streamable HTTP and is read-only.

## Discover the available tools

Using the official MCP Inspector CLI:

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/list
```

The current tool set is:

```text
lookup_evidence
service_history
search_services
evaluate_policy
```

## Look up evidence for a known service

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/call \
  --tool-name lookup_evidence \
  --tool-arg endpoint=https://api.x402node.dev/ai/json-repair
```

A successful response returns the evidence summary and latest published observation held by Atinamos for that service route.

## Search the published evidence corpus

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/call \
  --tool-name search_services \
  --tool-arg query=x402 \
  --tool-arg limit=20
```

## Apply a buyer policy

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/call \
  --tool-name evaluate_policy \
  --tool-arg endpoint=https://api.x402node.dev/ai/json-repair \
  --tool-arg policy='{"require_known":true,"minimum_successful_fulfilments":1,"maximum_failed_fulfilments":0,"require_paid_evidence":true,"max_evidence_age_days":30,"max_price_usdc":0.01}'
```

The result is eligibility under the supplied policy. It is not an Atinamos instruction to buy the service.

## Important interpretation rule

The same evidence may produce different decisions under different buyer policies. That is deliberate.

Atinamos supplies evidence. The caller remains responsible for its own procurement, risk and spending rules.
