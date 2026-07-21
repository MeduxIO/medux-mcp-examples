# Medux MCP Examples

Client-specific prompts and workflows for using [Medux](https://medux.io) media and document tools from Codex and Claude.

Medux provides one hosted MCP service for image, video, voice, avatar, document, asset, and asynchronous task workflows. This repository focuses on reproducible agent instructions: what to prepare, which Medux tool to expect, which arguments to review, and how to verify the result.

## Start here

1. [Get a Medux API key](https://medux.io/overview/mcp).
2. Connect the hosted Medux MCP service using the guide for [Codex](docs/codex.md) or [Claude](docs/claude.md).
3. For Codex or Claude Code, put inputs in the workspace; for claude.ai or Claude Desktop, attach them to the conversation.
4. Choose a workflow under the client for which it was authored and copy its prompt.
5. Review the proposed tool and arguments before approving the call.

> [!IMPORTANT]
> MCP tool schemas and account-specific connection details can change. Treat the Medux MCP integration page and the linked API reference as the source of truth. An example listed under one client is not claimed as tested on the other client.

## Examples

The repository currently maps all **138 published MCP tutorial pages** to client-specific examples: **69 for Codex** and **69 for Claude**.

### Codex examples

These examples use Codex workspace language, local file inspection, explicit command/tool approval, and local result verification.

[Browse all 69 Codex examples](examples/codex/INDEX.md).

| Workflow | Expected tool | Source tutorial |
| --- | --- | --- |
| [Text to video](examples/codex/generate/text-to-video/README.md) | `medux_video_generate_text_to_video` | [Codex tutorial](https://medux.io/tutorials/generate_create_text_to_video_codex_mcp.html) |
| [Image to video](examples/codex/generate/image-to-video/README.md) | `medux_video_generate_image_to_video` | [Codex tutorial](https://medux.io/tutorials/generate_create_image_to_video_codex_mcp.html) |
| [Trim a video](examples/codex/process/trim-video/README.md) | `medux_trim_video` | [Codex tutorial](https://medux.io/tutorials/media_trim_video_codex_mcp.html) |
| [Add a logo to a video](examples/codex/process/add-logo-to-video/README.md) | `add_logo_to_video` | [Codex tutorial](https://medux.io/tutorials/add_logo_codex_mcp.html) |
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

## Resources

- [Medux MCP overview](https://medux.io/overview/mcp)
- [Medux API overview](https://medux.io/overview/api)
- [API reference](https://medux.io/api-reference/)
- [All tutorials](https://medux.io/tutorials/)
- [Pricing](https://medux.io/pricing)

## Contributing

Issues and focused pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding an example. Never commit API keys, signed upload URLs, private input media, or generated output containing personal data.
