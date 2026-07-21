# Trim a video with Codex and Medux MCP

Cut a video to a specific time range with Codex. This example is derived from the linked Codex tutorial. The expected tool is `medux_trim_video`.

## Prompt

```text
Using the connected Medux MCP server, trim SOURCE_VIDEO in this Codex workspace
from 00:00:05 to 00:00:30.
Do not reframe or otherwise edit the video.

Inspect and upload the source if needed. Show me the file ID, exact tool, start
time, end time, and proposed arguments, then wait for my approval. After
completion, download the trimmed video into this workspace and use a local media
inspection tool, if available, to verify that its duration is about 25 seconds.
```

## Review before approval

- Tool: `medux_trim_video`
- `input_file_id`: resolves to the intended video
- `start_time`: `00:00:05`
- `end_time`: `00:00:30`
- `duration`: omit when start and end already define the cut
- `model_id`: use the live default unless a different supported model is needed

## Codex notes

- Check tool discovery with `/mcp`.
- Codex may use a local command such as `ffprobe` to verify the result; review that command if approval is requested.

## Learn more

- [Complete Codex MCP tutorial](https://medux.io/tutorials/media_trim_video_codex_mcp.html)
- [Trim Video API reference](https://medux.io/api-reference/media/trim-video)
