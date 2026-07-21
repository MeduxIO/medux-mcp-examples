# Example verification policy

An example must not claim support for a client merely because both clients implement MCP.

## Status definitions

- **Documentation-derived:** tool name and fields were taken from a published Medux tutorial or API reference, but the repository has no current execution record.
- **Tested with Codex:** completed through Codex and recorded with Codex version/surface, date, tool name, argument shape, task status, and sanitized output evidence.
- **Tested with Claude:** completed through the named Claude surface and recorded with surface/version, date, tool name, argument shape, task status, and sanitized output evidence.

Claude Code and claude.ai/Claude Desktop remote connectors are recorded separately because their local-file and connector behavior differs.

## Minimum test record

When an example is tested, add a `VERIFICATION.md` beside its README containing:

```markdown
# Verification

- Status: Tested with Codex | Tested with Claude Code | Tested with Claude remote connector
- Date: YYYY-MM-DD
- Client version or surface:
- Medux tool:
- Input type:
- Result: success
- Notes:
```

Do not include API keys, signed URLs, private media, personal data, full account responses, or identifying task IDs.

