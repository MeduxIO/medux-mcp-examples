# Medux MCP Examples

Client-specific prompts and workflows for using [Medux](https://medux.io) media and document tools from Codex and Claude.

Medux provides one hosted MCP service for image, video, voice, avatar, document, asset, and asynchronous task workflows. This repository focuses on reproducible agent instructions: what to prepare, which Medux tool to expect, which arguments to review, and how to verify the result.

## Start here

1. Connect the hosted Medux MCP service at `https://medux.io/mcp`. Start with [Connect Medux MCP](docs/connection.md), then follow the guide for [Codex](docs/codex.md) or [Claude](docs/claude.md). Codex and Claude sign in with OAuth; no API key is needed. For clients that use a Bearer header, [create a Medux API key](https://medux.io/overview/mcp).
3. Skim [Concepts](docs/concepts.md) so you can read a proposed tool call: files vs. assets, upload URLs, the async task lifecycle, and credits.
4. For Codex or Claude Code, put inputs in the workspace; for claude.ai or Claude Desktop, attach them to the conversation.
5. Choose a workflow under the client for which it was authored and copy its prompt.
6. Review the proposed tool and arguments before approving the call.

> [!NOTE]
> The MCP endpoint is now `https://medux.io/mcp`. The old `https://medux.io/api/mcp/v1` keeps working, so existing setups do not break.

> [!IMPORTANT]
> MCP tool schemas and account-specific connection details can change. Treat the Medux MCP integration page and the linked API reference as the source of truth. An example listed under one client is not claimed as tested on the other client.

## Examples

The repository currently maps all **138 published MCP tutorial pages** to client-specific examples: **69 for Codex** and **69 for Claude**.

Some tutorials describe REST operations that the MCP server does not expose (listing assets, tasks, results, voices and avatars, editing voice parameters, creating assets, creating a video by project). Those 8 examples per client are marked **REST only** and link to the REST API instead. For the tools that really exist, see the [tool reference](docs/tools.md).

### Workshop examples

Examples written for a Medux Workshop page rather than a published tutorial. They are not part of the generated tutorial indexes above.

| Workflow | Claude | Codex | Workshop page |
| --- | --- | --- | --- |
| Face Swap Plus (video) | [Claude example](examples/claude/edit/face-swap-plus/README.md) — tested with Claude Code | [Codex example](examples/codex/edit/face-swap-plus/README.md) — documentation-derived | [medux.io/workshop/face-swap-plus](https://medux.io/workshop/face-swap-plus) |

### Codex examples

These examples use Codex workspace language, local file inspection, explicit command/tool approval, and local result verification.

[Browse all 69 Codex examples](examples/codex/INDEX.md).

| Workflow | Expected tool | Source tutorial |
| --- | --- | --- |
| [Text to video](examples/codex/generate/text-to-video/README.md) | `medux_video_generate_text_to_video` | [Codex tutorial](https://medux.io/tutorials/generate_create_text_to_video_codex_mcp.html) |
| [Image to video](examples/codex/generate/image-to-video/README.md) | `medux_video_generate_image_to_video` | [Codex tutorial](https://medux.io/tutorials/generate_create_image_to_video_codex_mcp.html) |
| [Trim a video](examples/codex/process/trim-video/README.md) | `medux_trim_video` | [Codex tutorial](https://medux.io/tutorials/media_trim_video_codex_mcp.html) |
| [Add a logo to a video](examples/codex/process/add-logo-to-video/README.md) | `medux_add_logo_to_video` | [Codex tutorial](https://medux.io/tutorials/add_logo_codex_mcp.html) |
| [PDF to Word](examples/codex/documents/pdf-to-word/README.md) | `medux_pdf_to_word` | [Codex tutorial](https://medux.io/tutorials/document_pdf_to_word_codex_mcp.html) |

### Claude examples

These examples distinguish chat attachments and per-conversation connectors in claude.ai/Claude Desktop from working-directory files and `/mcp` in Claude Code.

[Browse all 69 Claude examples](examples/claude/INDEX.md).

| Workflow | Expected tool | Source tutorial |
| --- | --- | --- |
| [Remove an image background](examples/claude/process/remove-image-background/README.md) | `medux_image_remove_background` | [Claude tutorial](https://medux.io/tutorials/process_create_image_background_removal_claude_mcp.html) |
| [Clone a voice](examples/claude/voice/clone-voice/README.md) | `medux_clone_voice` | [Claude tutorial](https://medux.io/tutorials/clone_create_voice_claude_mcp.html) |
| [Merge PDFs](examples/claude/documents/merge-pdfs/README.md) | `medux_merge_pdf` | [Claude tutorial](https://medux.io/tutorials/document_merge_pdf_claude_mcp.html) |

## Verification status

The current examples are documentation-derived from published Medux tutorials. They have not been marked as live-tested in this repository because a test record, client version, Medux endpoint, and successful task evidence have not yet been committed. See [verification policy](docs/verification.md).

## Regenerate from the tutorial source

The bulk examples and client indexes are generated from the published tutorial HTML. Eight flagship examples remain manually curated and are protected from overwrite.

```bash
./scripts/generate_examples.py \
  --tutorial-dir /path/to/medux/tutorials \
  --expected-count 138
./scripts/check.sh
```

Some tutorials name REST operations as MCP tools. Re-apply the corrections after every regeneration (they map task getters to `medux_task_query`, and mark operations with no MCP tool as REST-only):

```bash
./scripts/apply_tool_corrections.py
```

The generator writes [the tutorial-to-example manifest](examples/manifest.json), which is used to verify one-to-one coverage.

## How the workflows work

Most file-based workflows follow the same service pattern, although file selection differs by client:

1. Codex/Claude Code locates workspace files, or claude.ai/Claude Desktop receives conversation attachments.
2. Medux creates signed upload targets when needed.
3. The agent uploads the files and receives Medux file or asset IDs.
4. The agent proposes the operation-specific MCP tool call.
5. You verify the tool, inputs, cost-relevant options, and output settings.
6. Medux creates an asynchronous task.
7. The agent checks task status and downloads the completed result.

See [Safe tool approval](docs/safe-tool-approval.md) before running a workflow with valuable or sensitive media.

## Documentation

- [Tool reference](docs/tools.md) — all 69 MCP tools with required inputs, plus prompts for tools without a tutorial example.
- [Concepts](docs/concepts.md) — Medux terms used across the examples.
- [Connect Medux MCP](docs/connection.md) — client-neutral setup and troubleshooting, with [Codex](docs/codex.md) and [Claude](docs/claude.md) guides.
- [Safe tool approval](docs/safe-tool-approval.md) — review checklist before a billable or identity-linked call.
- [Verification policy](docs/verification.md) — how examples move from documentation-derived to tested.

See the [docs index](docs/README.md) for the full reading order.

## Resources

- [Medux MCP overview](https://medux.io/overview/mcp)
- [Medux API overview](https://medux.io/overview/api)
- [API reference](https://medux.io/api-reference/)
- [All tutorials](https://medux.io/tutorials/index.html)
- [Pricing](https://medux.io/pricing)

## Contributing

Issues and focused pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding an example. Never commit API keys, signed upload URLs, private input media, or generated output containing personal data.
