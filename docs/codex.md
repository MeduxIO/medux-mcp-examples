# Connect Medux MCP to Codex

Codex CLI, the Codex IDE extension and the Codex desktop app on the same machine share one MCP configuration (`config.toml`), so you only connect once.

Endpoint: `https://medux.io/mcp` (Streamable HTTP). Recommended auth: **OAuth**, so there is no API key to manage. See [Connect Medux MCP](connection.md) for the overview.

## Option A: OAuth (recommended)

### Desktop app or IDE extension

1. Open **Settings → MCP servers → Add server**.
2. Name it `medux`, choose **Streamable HTTP**, and enter `https://medux.io/mcp`.
3. **Save**, then restart the app or extension.
4. Find `medux` in the server list and select **Authenticate**. Sign in to Medux and approve access in the browser.

### Terminal

```bash
codex mcp add medux --url https://medux.io/mcp
codex mcp login medux
```

`codex mcp list` shows configured servers and their auth status. Run `codex mcp login medux` again if sign-in expires (authorizations last up to 30 days).

### `config.toml`

The same server written by hand in `~/.codex/config.toml`:

```toml
[mcp_servers.medux]
url = "https://medux.io/mcp"
```

Then run `codex mcp login medux`.

## Option B: API key

Use this for headless or CI environments where a browser sign-in is not possible.

```toml
[mcp_servers.medux]
url = "https://medux.io/mcp"
bearer_token_env_var = "MEDUX_API_KEY"
```

```bash
export MEDUX_API_KEY=<your-medux-api-key>   # in the environment that launches Codex
```

Do not replace `bearer_token_env_var` with a literal key. A project-level `.codex/config.toml` is fine for the URL, but never put the key in a repository.

## Migrating from `/api/mcp/v1`

The old URL still works. To move over, change `url` to `https://medux.io/mcp` (or run `codex mcp remove medux` and add it again) and run `codex mcp login medux` if you use OAuth.

## Verify

1. Open Codex in your workspace and type `/mcp`.
2. Confirm `medux` is enabled and shows its `medux_*` tools.
3. Ask: *"Use Medux to check my balance."* (calls `medux_balance_get`, which creates no task).
4. Then try a real workflow from [`examples/codex`](../examples/codex/INDEX.md).

## Codex-specific workflow behavior

- Local paths refer to files inside the current workspace; Codex can inspect them before upload and verify outputs afterwards with local commands.
- Network, shell and filesystem actions may need approval depending on your sandbox and approval policy.
- Ask Codex to save outputs to an explicit workspace path.
- Review the tool name and arguments before approving paid operations ([Safe tool approval](safe-tool-approval.md)).

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `medux` not listed in `/mcp` | Restart Codex; check `codex mcp list` and that `config.toml` parses. |
| 401 / "Auth required" | Run `codex mcp login medux` (OAuth), or check `MEDUX_API_KEY` is set where Codex was launched. |
| Browser sign-in does not return to Codex | Codex listens on a local loopback port for the callback; make sure nothing blocks `127.0.0.1` and retry login. |

Source: [OpenAI Codex MCP documentation](https://developers.openai.com/codex/mcp).
