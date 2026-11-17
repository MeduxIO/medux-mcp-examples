# How to Create a Music Video with MV Director with Codex MCP and Medux

Create a director-style music video from one audio track and one portrait.

## Expected Medux tools

- `medux_file_create_upload_url` (audio, then portrait)
- `medux_mv_director`
- `medux_task_query`

## Prompt

```text
Use Medux MV Director to make a music video from ./song.mp3 and the portrait ./artist.png. Upload both files, show me the arguments, poll the task and save the result.
```

## Review before approval

- `prompt_audio_file_id` (required): the audio track's file ID.
- `prompt_image_file_id` (required): the portrait's file ID.
- `persona` (optional): leave unset unless you want to steer the director style.
- Use audio and a portrait you have the right to use.
- Every local file or attachment maps to the intended Medux file or asset ID.
- Operation order, output settings, and cost-relevant options match the request.

## Codex notes

- Use `/mcp` to confirm that Medux and the expected tool are available.
- Workspace paths must point to the intended local inputs and output directory.
- Review any network, shell, or filesystem approval requested during upload, download, or verification.

## Learn more

- [Medux tutorials](https://medux.io/tutorials/)
- [Tool reference](../../../../docs/tools.md)
- [Medux MCP overview](https://medux.io/overview/mcp)

<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/video/mv-director](https://medux.io/playground/video/mv-director) |
| Workshop | [medux.io/workshop/mv-director](https://medux.io/workshop/mv-director) |

- REST API example: [examples/video/mv-director](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/video/mv-director)
- Claude example: [claude/workshop/mv-director](../../../claude/workshop/mv-director/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
