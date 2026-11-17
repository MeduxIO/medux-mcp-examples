# How to Create a Video with Minimax H3 from Text and Optional Images with Claude MCP and Medux

Create a video and audio from text, optionally with a first image, a last image and driving audio.

## Expected Medux tools

- `medux_file_create_upload_url` (only for optional inputs)
- `medux_text_image_to_video`
- `medux_task_query`

## Prompt

```text
Use Medux medux_text_image_to_video with the prompt "a paper boat drifting down a rainy street, cinematic" and ./first.png as the first image. Show me the arguments and the credit estimate before submitting, then poll the task and save the result.
```

## Review before approval

- `prompt_text` (required).
- `prompt_image_file_id`, `last_image_file_id`, `prompt_audio_file_id` (optional): uploaded file IDs.
- `resolution`, `seed` (optional).
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
| Playground | [medux.io/playground/video/text-image-to-video](https://medux.io/playground/video/text-image-to-video) |
| Workshop | [medux.io/workshop/minimax-h3-unlimited](https://medux.io/workshop/minimax-h3-unlimited) |

- REST API example: [examples/video/text-image-to-video](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/video/text-image-to-video)
- Codex example: [codex/workshop/text-image-to-video](../../../codex/workshop/text-image-to-video/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
