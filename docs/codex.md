# Connect Medux MCP to Codex

Codex CLI, the Codex IDE extension, and the Codex desktop app on the same host share MCP configuration through `config.toml`.

## Desktop app or IDE extension

1. Open **Settings** (or the gear menu in the extension).
2. Select **MCP servers** and **Add server**.
3. Name the server `medux`.
4. Choose **Streamable HTTP**.
5. Enter the remote endpoint shown by the Medux account integration page.
6. Configure authentication using the mechanism Medux specifies.
7. Save, then restart the app or extension.

## `config.toml`

Codex user configuration normally lives at `~/.codex/config.toml`. A trusted repository can instead use `.codex/config.toml`, but credentials must remain outside the repository.

Use this shape only after replacing the endpoint and confirming that Medux accepts a bearer token:

```toml
[mcp_servers.medux]
url = "MEDUX_MCP_ENDPOINT_FROM_ACCOUNT"
bearer_token_env_var = "MEDUX_API_KEY"
```

Set `MEDUX_API_KEY` in the environment that launches Codex. Do not replace `bearer_token_env_var` with a literal secret.

If the Medux account page specifies OAuth or a different header, follow that live configuration instead of this bearer-token template.

## Verify in Codex

1. Open Codex in the target workspace.
2. Type `/mcp` to inspect connected servers and tools.
3. Confirm that `medux` is enabled and the expected workflow tool appears.
4. Ask Codex to list Medux tool names without calling them.

## Codex-specific workflow behavior

- Local paths refer to files inside the current workspace.
- Codex can inspect files before upload and verify outputs with local commands.
- Network, shell, or filesystem operations may require approval depending on the active sandbox and policy.
- Ask Codex to save outputs under an explicit workspace path.

Source: [OpenAI Codex MCP documentation](https://learn.chatgpt.com/docs/extend/mcp).

