# How to Swap Faces in a Video with Face Swap Plus using Claude MCP and Medux

Replace the face in a video with a face from a reference image using the Medux Face Swap Plus workflow (MiniMax H3), then poll the task and save the result. Only use faces you have the right to use.

## Expected Medux tools

- `medux_file_create_upload_url` (once per input file)
- `medux_video_face_swap_plus`
- `medux_task_query`

## Prompt

```text
Use Medux to run Face Swap Plus on ./clip.mp4 with the face in ./face.jpg.
Upload both files first, then call the Face Swap Plus tool with the video as the input video and the image as the source face.
Poll the task until it finishes and save the result video next to the inputs.
I have the right to use both the video and the face in the image.
```

## Review before approval

- `input_video_file_id` (required): the file ID returned for `clip.mp4`, not the image.
- `source_image_file_id` (required): the file ID returned for `face.jpg`, not the video.
- `model_id` (optional): `face-swap-plus-default` is the only option.
- Duration and cost: Face Swap Plus is billed per second of input video (about 80 credits per second). Free accounts accept videos up to 10 seconds; Starter up to 60 seconds; Growth up to 15 minutes.
- Use a clear, front-facing face image and a video where the face stays visible.

## Claude notes

- In claude.ai or Claude Desktop, attach the video and image and enable the Medux connector for the conversation.
- In Claude Code, keep inputs in the working directory and confirm Medux with `/mcp`.
- An attachment is not a Medux `file_id`; approve the upload step when the workflow requires one.

## Learn more

- [Face Swap Plus Workshop](https://medux.io/workshop/face-swap-plus)
- [Matching API reference](https://medux.io/api-reference/ai-avatar/face-swap-plus)
- [API example](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/ai-avatar/face-swap-plus)
- [Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/video/face-swap-plus](https://medux.io/playground/video/face-swap-plus) |
| Workshop | [medux.io/workshop/face-swap-plus](https://medux.io/workshop/face-swap-plus) |

- REST API example: [examples/ai-avatar/face-swap-plus](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/ai-avatar/face-swap-plus)
- Codex example: [codex/edit/face-swap-plus](../../../codex/edit/face-swap-plus/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Tested with Claude Code** on 2026-11-17. See the [verification record](VERIFICATION.md) and the repository [verification policy](../../../../docs/verification.md).
