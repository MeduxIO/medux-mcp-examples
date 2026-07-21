# Connect Medux MCP to Claude

“Claude” can mean two different MCP environments. Choose the one you are actually using.

## claude.ai and Claude Desktop remote connector

For an individual plan:

1. Open **Customize > Connectors**.
2. Select **+**, then **Add custom connector**.
3. Enter the remote Medux MCP endpoint shown in your Medux account.
4. Complete the authentication flow Medux specifies.
5. In each conversation, use the **+** menu, open **Connectors**, and enable Medux.

Team and Enterprise workspaces may require an Owner or Primary Owner to add the connector under **Organization settings > Connectors** before members can enable it.

Remote connectors are reached from Anthropic's cloud infrastructure, even when the conversation is opened in Claude Desktop. Do not assume a remote connector can directly read arbitrary files from your computer; attach the input to the conversation or use Claude Code for workspace-driven flows.

## Claude Code

Claude Code can add an HTTP MCP server through its MCP management commands or project configuration. Use the exact endpoint and authentication values supplied by Medux.

Start by reviewing the installed CLI's current syntax:

```bash
claude mcp add --help
```

After configuration, open Claude Code and use `/mcp` to confirm that Medux is connected. Project-scoped MCP configuration may live in `.mcp.json`; never commit literal credentials.

## Claude-specific workflow behavior

- In claude.ai or Claude Desktop, prompts refer to attached files and returned conversation artifacts.
- The Medux connector must be enabled for the current conversation.
- In Claude Code, prompts can refer to paths in the working directory and request local output verification.
- Always review tool arguments before approving file uploads, media generation, reusable asset creation, or paid operations.

Sources: [Claude custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) and [Claude Code MCP documentation](https://code.claude.com/docs/en/mcp).

