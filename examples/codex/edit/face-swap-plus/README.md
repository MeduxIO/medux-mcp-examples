# How to Swap Faces in a Video with Face Swap Plus using Codex MCP and Medux

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

## Codex notes

- Use `/mcp` to confirm that Medux and `medux_video_face_swap_plus` are available.
- Workspace paths must point to the intended local inputs and output directory.
- Review any network, shell, or filesystem approval requested during upload, download, or verification.

## Learn more

- [Face Swap Plus Workshop](https://medux.io/workshop/face-swap-plus)
- [Matching API reference](https://medux.io/api-reference/ai-avatar/face-swap-plus)
- [API example](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/ai-avatar/face-swap-plus)
- [Medux MCP overview](https://medux.io/overview/mcp)

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
