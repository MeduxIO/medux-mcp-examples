# How to Generate a Video Between a First and a Last Frame with Claude MCP and Medux

Generate a video that starts at one image and ends at another, then poll the task and download the result.

## Expected Medux tools

- `medux_file_create_upload_url` (twice)
- `medux_video_generate_first_last_frame_to_video`
- `medux_task_query`

## Prompt

```text
Use Medux to generate a video that starts at ./start.png and ends at ./end.png, prompt "a slow dolly push-in", model seedance-2-0-fast. Show the model options and credit estimate before submitting.
```

## Review before approval

- `image_file_ids` (required): exactly two file IDs, first frame then last frame.
- `model_id` and `prompt` (required).
- `duration_seconds`, `clarity`, `aspect_ratio` (optional): must be values the chosen model lists.
- Estimate credits before submitting; video generation is billed by duration.
- Every local file or attachment maps to the intended Medux file or asset ID.
- Operation order, output settings, and cost-relevant options match the request.

## Claude notes

- In claude.ai or Claude Desktop, attach inputs and enable the Medux connector for the conversation.
- In Claude Code, keep inputs in the working directory and confirm Medux with `/mcp`.
- An attachment is not a Medux `file_id`; approve the upload step when the workflow requires one.

## Learn more

- [Medux tutorials](https://medux.io/tutorials/)
- [Tool reference](../../../../docs/tools.md)
- [Medux MCP overview](https://medux.io/overview/mcp)

<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/video/first-last-frame-to-video](https://medux.io/playground/video/first-last-frame-to-video) |
| Workshop | [medux.io/workshop/first-last-frame-to-video](https://medux.io/workshop/first-last-frame-to-video) |

- REST API example: [examples/generate/create-first-last-frame-to-video](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/generate/create-first-last-frame-to-video)
- Codex example: [codex/workshop/create-first-last-frame-to-video](../../../codex/workshop/create-first-last-frame-to-video/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
