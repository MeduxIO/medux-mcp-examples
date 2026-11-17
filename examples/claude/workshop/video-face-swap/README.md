# How to Swap a Face in a Video with Claude MCP and Medux

Replace a face in a video with the face in a reference image, then poll the task and save the result. Only use faces you have the right to use.

## Expected Medux tools

- `medux_file_create_upload_url` (once per input file)
- `medux_video_face_swap`
- `medux_task_query`

## Prompt

```text
Use Medux to replace the face in ./clip.mp4 with the face in ./face.jpg. Upload both files first, run the video face swap, poll the task until it finishes and save the result. I have the right to use both the video and the face in the image.
```

## Review before approval

- `input_video_file_id` (required): the video's file ID, not the image's.
- `source_image_file_id` (required): the face image's file ID, not the video's.
- Use a clear, front-facing face image and a video where the face stays visible.
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
| Playground | [medux.io/playground/video/video-face-swap](https://medux.io/playground/video/video-face-swap) |
| Workshop | [medux.io/workshop/face-swap](https://medux.io/workshop/face-swap) |

- REST API example: [examples/video/video-face-swap](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/video/video-face-swap)
- Codex example: [codex/workshop/video-face-swap](../../../codex/workshop/video-face-swap/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
