# How to Generate a Video from Reference Images, Videos and Audio with Claude MCP and Medux

Generate a video that follows reference media (images, videos, audio) within the chosen model's limits.

## Expected Medux tools

- `medux_file_create_upload_url` (once per reference file)
- `medux_video_generate_omni_reference_to_video`
- `medux_task_query`

## Prompt

```text
Use Medux to generate a video from the prompt below and the two reference images in ./refs. Check the model's reference limits first, show me the arguments, then poll the task and save the result.
Prompt: the two characters walk through a night market, handheld camera.
```

## Review before approval

- `image_file_ids`, `video_file_ids`, `audio_file_ids` (optional): only the reference types the model accepts, within its counts.
- `model_id` and `prompt` (required).
- Do not upload references you do not have the right to use.
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
| Playground | [medux.io/playground/video/omni-reference-to-video](https://medux.io/playground/video/omni-reference-to-video) |

- REST API example: [examples/generate/create-omni-reference-to-video](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/generate/create-omni-reference-to-video)
- Codex example: [codex/workshop/create-omni-reference-to-video](../../../codex/workshop/create-omni-reference-to-video/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
