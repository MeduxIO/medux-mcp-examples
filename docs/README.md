# Documentation

Reference material for using the Medux hosted MCP service with the examples in
this repository. Read them roughly in this order.

- [Concepts](concepts.md) — Medux terms the examples use: files vs. assets, upload
  URLs, the asynchronous task lifecycle, credits, and common request fields.
- [Connect Medux MCP](connection.md) — endpoint (`https://medux.io/mcp`), OAuth vs. API key, tool overview, call flow, troubleshooting.
  - [Connect Codex](codex.md)
  - [Connect Claude](claude.md)
- [Tool reference](tools.md) — every MCP tool, grouped, with required inputs.
- [Safe tool approval](safe-tool-approval.md) — what to check before you approve a
  billable or identity-linked call.
- [Verification policy](verification.md) — what "documentation-derived" vs. "tested"
  means and the record required to claim a client was tested.

The live MCP schema and the [Medux API reference](https://medux.io/api-reference/)
are the source of truth; anything here can lag behind the current service.
