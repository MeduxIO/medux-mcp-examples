# Add a logo to a video with Codex and Medux MCP

Place a logo watermark on a source video with Codex. The Codex tutorial currently identifies the workflow tool as `add_logo_to_video`; confirm the live MCP tool name before approval.

## Prepare

Place a source video and a transparent PNG logo in the Codex workspace.

## Prompt

```text
Using the connected Medux MCP server, add LOGO_IMAGE to SOURCE_VIDEO as a subtle watermark in the
top-right corner. Keep a 24-pixel margin from the top and right edges. Preserve
the source video's resolution, duration, audio, and frame rate.

Inspect both local files first. Propose a logo size that is visible without
dominating the frame, show me the exact Medux tool and all placement arguments,
and wait for my approval. After completion, download the result into this
workspace and extract one preview frame so we can verify placement.
```

## Review before approval

- Source video and logo file IDs point to the correct uploads
- Tool name matches the live Medux MCP schema
- Position is top-right with the intended margins
- Logo width and height preserve the logo's aspect ratio
- The workflow preserves source audio and duration

## Codex notes

- Confirm the live tool name through `/mcp`; this workflow predates the standardized `medux_` naming used by many other tools.
- Codex may run local media inspection commands before upload and after download.

## Learn more

- [Complete Codex MCP tutorial with visual examples](https://medux.io/tutorials/add_logo_codex_mcp.html)
- [Medux MCP overview](https://medux.io/overview/mcp)
