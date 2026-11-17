# Clone a voice with Claude and Medux MCP

Create a reusable voice asset with Claude. This example is derived from the linked Claude tutorial. The expected tool is `medux_clone_voice`.

> [!WARNING]
> Clone only your own voice or a voice for which you have explicit authorization. Do not use this workflow to impersonate, deceive, or bypass consent.

## Prompt

```text
Use the connected Medux tool to create a reusable voice asset from the attached
VOICE_SAMPLE. Inspect the audio first and tell me its format and duration.

Upload it to Medux if needed. Before calling the clone tool, show me the exact
Medux tool, source file ID, and proposed title, then wait for my approval. After
approval, monitor the task and report the reusable voice asset ID. Do not
synthesize additional speech unless I ask separately.
```

## Review before approval

- Tool: `medux_clone_voice`
- `file_id`: resolves to the authorized audio sample
- `title`: does not imply a misleading identity
- The account has permission to process and reuse the recording

## Claude notes

- In claude.ai or Claude Desktop, attach the authorized audio and enable the Medux connector in the conversation.
- In Claude Code, keep the sample in the working directory and verify Medux with `/mcp`.
- Review Claude's proposed tool call carefully because cloning creates a reusable identity-linked asset.

## Learn more

- [Complete Claude MCP tutorial](https://medux.io/tutorials/clone_create_voice_claude_mcp.html)
- [Create Voice API reference](https://medux.io/api-reference/clone/create-voice)
- [Medux pricing](https://medux.io/pricing)

<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/voice/voice-clone](https://medux.io/playground/voice/voice-clone) |

- REST API example: [examples/clone/create-voice](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/clone/create-voice)
- Codex example: [codex/clone/clone-create-voice](../../../codex/clone/clone-create-voice/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->
