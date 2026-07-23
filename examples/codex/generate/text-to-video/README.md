# Generate video from text with Codex and Medux MCP

Use Codex to create a video from a text prompt. This example is derived from the linked Codex tutorial. The expected Medux tool is `medux_video_generate_text_to_video`.

## Prompt

```text
Using the connected Medux MCP server, generate a 16:9, 720P, 5-second video of a small paper boat
crossing a rain puddle at dusk. Use a cinematic close-up with realistic water
reflections and gentle camera movement.

Before calling the generation tool, inspect the live MCP schema and show me the
exact Medux tool and proposed arguments. Wait for my approval. Then monitor the
asynchronous task, download the final video into this Codex workspace, and
report its path and duration.
```

## Review before approval

- Tool: `medux_video_generate_text_to_video`
- `prompt`: contains the intended subject, motion, framing, and style
- `aspect_ratio`: `16:9`
- `clarity`: `720P`
- `duration_seconds`: `5`
- `model_id`: use a current supported model or let Medux apply its default
- `title`: optional descriptive task title

Generation availability and accepted values can change. Review the live schema before approval.

## Codex notes

- Confirm the Medux server in Codex with `/mcp` before starting.
- Keep the source workspace writable if you want Codex to save the output locally.
- Codex may request approval for network access or the download command, depending on the active sandbox and approval policy.

## Learn more

- [Complete Codex MCP tutorial](https://medux.io/tutorials/generate_create_text_to_video_codex_mcp.html)
- [Create Text to Video API reference](https://medux.io/api-reference/generate/create-text-to-video)
- [More Medux tutorials](https://medux.io/tutorials/index.html)
