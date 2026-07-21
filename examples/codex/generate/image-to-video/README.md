# Generate video from an image with Codex and Medux MCP

Animate a local image with Codex. This example is derived from the linked Codex tutorial. The expected tool is `medux_video_generate_image_to_video`.

## Prepare

Put one source image in the Codex workspace and replace `SOURCE_IMAGE` below with its path.

## Prompt

```text
Using the connected Medux MCP server, animate SOURCE_IMAGE into a 5-second,
16:9 video. Preserve the
subject's identity and composition. Add subtle natural motion and a slow camera
push-in; avoid sudden deformations.

Inspect the local file and upload it if needed. Before generation, inspect the
live MCP schema and show me the selected source file ID, exact Medux tool, and
proposed arguments. Wait for my approval. Then monitor the task, download the
result into this workspace, and report the saved path.
```

## Review before approval

- Tool: `medux_video_generate_image_to_video`
- `file_id`: resolves to the intended uploaded image
- `prompt`: describes motion and explicitly states what must be preserved
- `aspect_ratio`, `clarity`, and `duration_seconds`: match the intended output
- `model_id`: valid in the live MCP schema

## Codex notes

- Use `/mcp` to confirm that the Medux server and expected tool are available.
- Codex can inspect a local image in the workspace before upload.
- A network or shell approval may appear when Codex uploads or downloads a file.

## Learn more

- [Complete Codex MCP tutorial](https://medux.io/tutorials/generate_create_image_to_video_codex_mcp.html)
- [Create Image to Video API reference](https://medux.io/api-reference/generate/create-image-to-video)
