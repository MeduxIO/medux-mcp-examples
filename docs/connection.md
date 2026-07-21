# Connect Medux MCP: choose a client

Medux is a hosted remote MCP service. Your account's integration page provides the current endpoint, authentication method, and available tools.

Use the client-specific setup guide:

- [Connect Codex](codex.md)
- [Connect Claude](claude.md)

## Before connecting

- Sign in to Medux and create an API key.
- Open [Medux MCP](https://medux.io/overview/mcp).
- Copy the current connection values from the account integration flow.
- Keep the credential in your agent's secret or environment-variable facility; never paste it into a repository file.

## Client-neutral connection test

Use this prompt after connecting:

```text
List the tools exposed by the connected Medux MCP server. Do not call any tool.
Group the tools by image, video, voice, avatar, document, asset, and task operations.
For each tool, show only its name and one-sentence purpose.
```

This verifies tool discovery without intentionally creating a billable task. Use the client-specific guide to confirm the server connection itself.

## Troubleshooting

- **No Medux tools appear:** follow the client-specific verification steps and restart or reconnect the client.
- **Unauthorized:** create or select a valid API key and check the required authorization format.
- **Tool not found:** refresh the tool list; the live schema may have changed.
- **Local file cannot be used:** allow the agent to read the file and complete the signed-upload step first.
- **Task does not finish immediately:** media operations are asynchronous; ask the agent to check the returned task ID.
