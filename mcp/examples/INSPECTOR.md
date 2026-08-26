# MCP Inspector examples

These examples use the public Atinamos Evidence MCP with the official MCP Inspector CLI.

## List tools

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/list
```

Expected tool names:

```text
lookup_evidence
service_history
search_services
evaluate_policy
```

## Look up published evidence

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/call \
  --tool-name lookup_evidence \
  --tool-arg endpoint=https://api.x402node.dev/ai/json-repair
```

At the time this example was published, the response included one paid test, one successful fulfilment, zero failed fulfilments and four of four tested assertions passed for the published x402Node JSON Repair observation.

## View service history

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/call \
  --tool-name service_history \
  --tool-arg endpoint=https://api.x402node.dev/ai/json-repair
```

## Search the published evidence corpus

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/call \
  --tool-name search_services \
  --tool-arg query=x402 \
  --tool-arg limit=20
```

## Evaluate a policy expected to pass the published example

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/call \
  --tool-name evaluate_policy \
  --tool-arg endpoint=https://api.x402node.dev/ai/json-repair \
  --tool-arg policy='{"require_known":true,"minimum_successful_fulfilments":1,"maximum_failed_fulfilments":0,"require_paid_evidence":true,"max_evidence_age_days":30,"max_price_usdc":0.01}'
```

At the time of publication, this returned `eligible` under that supplied policy.

## Evaluate a stricter policy

```bash
npx @modelcontextprotocol/inspector --cli https://verify.atinamos.co.uk/mcp \
  --transport http \
  --method tools/call \
  --tool-name evaluate_policy \
  --tool-arg endpoint=https://api.x402node.dev/ai/json-repair \
  --tool-arg policy='{"minimum_successful_fulfilments":5}'
```

At the time of publication, this returned `not_eligible` because the published corpus contained one successful fulfilment for that route, not five.

These examples are timestamped demonstrations of interface behaviour. Evidence counts may change as further observations are published.
