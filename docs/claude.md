# Connect Medux MCP to Claude

"Claude" means two different MCP environments. Pick the one you use.

Endpoint: `https://medux.io/mcp` (Streamable HTTP). Recommended auth: **OAuth**. See [Connect Medux MCP](connection.md) for the overview.

## Claude Code

OAuth (recommended):

```bash
claude mcp add --transport http medux https://medux.io/mcp
```

Then run `/mcp` inside Claude Code, select `medux`, and choose **Authenticate**. Sign in to Medux and approve access in the browser.

API key instead:

```bash
claude mcp add --transport http medux https://medux.io/mcp \
  --header "Authorization: Bearer sk-medux-..."
```

Scopes: add `--scope user` to make Medux available in every project, or `--scope project` to write `.mcp.json` for the team (never put a literal key in a shared file; use `${MEDUX_API_KEY}` expansion there).

Verify: `claude mcp list`, `claude mcp get medux`, or `/mcp` in a session.

Migrating from `/api/mcp/v1`: `claude mcp remove medux`, add it again with the new URL, and re-authenticate.

## claude.ai and Claude Desktop

1. Open **Customize → Connectors**, select **+**, then **Add custom connector**.
2. Enter `https://medux.io/mcp` and complete the Medux sign-in.
3. In each conversation, use the **+** menu → **Connectors** and enable Medux.

Team and Enterprise workspaces may require an Owner to add the connector under **Organization settings → Connectors** first.

Remote connectors are reached from Anthropic's cloud, even in Claude Desktop, so they cannot read arbitrary files on your computer. Attach input files to the conversation, or use Claude Code for workspace-driven flows.

## Claude-specific workflow behavior

- claude.ai / Claude Desktop: prompts refer to attached files and returned artifacts; Medux must be enabled for the conversation.
- Claude Code: prompts can refer to paths in the working directory and ask for local output verification.
- Review tool arguments before approving uploads, generation, reusable asset creation or paid operations ([Safe tool approval](safe-tool-approval.md)).

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| No `medux_*` tools | Run `/mcp` to see the error; restart the session after changing config; check scope with `claude mcp get medux`; approve project-scoped servers when prompted. |
| 401 / sign-in prompt again | Re-authenticate in `/mcp`, or check the Bearer header format. |
| Connector missing in a chat | Enable it for that conversation via **+ → Connectors**. |

Sources: [Claude custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) and [Claude Code MCP](https://code.claude.com/docs/en/mcp).
