# How to Remove an Object from a Video by Describing It with Claude MCP and Medux

Remove an object from a video by describing it in text instead of drawing a region.

## Expected Medux tools

- `medux_file_create_upload_url`
- `medux_remove_video_object_by_prompt`
- `medux_task_query`

## Prompt

```text
Use Medux to remove "the red bicycle on the left" from ./clip.mp4. Upload the file, show me the arguments, poll the task and save the result.
```

## Review before approval

- `input_file_id` (required): the uploaded video's file ID.
- `prompt_text` (required): describe exactly one object, with a position or colour.
- Check the result for leftover artifacts before using it.
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
| Playground | [medux.io/playground/video/remove-video-object-by-prompt](https://medux.io/playground/video/remove-video-object-by-prompt) |
| Workshop | [medux.io/workshop/remove/video-object-by-prompt](https://medux.io/workshop/remove/video-object-by-prompt) |

- REST API example: [examples/video/remove-video-object-by-prompt](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/video/remove-video-object-by-prompt)
- Codex example: [codex/workshop/remove-video-object-by-prompt](../../../codex/workshop/remove-video-object-by-prompt/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
