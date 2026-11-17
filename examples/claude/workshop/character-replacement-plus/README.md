# How to Replace the Main Character in a Video with Character Replacement Plus with Claude MCP and Medux

Replace the main character of a video with a character from a reference image using the MiniMax H3 workflow.

## Expected Medux tools

- `medux_file_create_upload_url` (once per input file)
- `medux_video_character_replacement_plus`
- `medux_task_query`

## Prompt

```text
Use Medux Character Replacement Plus to replace the main character in ./clip.mp4 with the character in ./character.png. Upload both files first, poll until the task finishes, and save the result. I have the right to use both inputs.
```

## Review before approval

- `source_video_file_id` (required): the video whose main character is replaced.
- `target_character_image_file_id` (required): the replacement character image.
- A second reference image is accepted by the tool; check its live schema before adding one.
- Billing is per second of input video; check your plan's length limit.
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
| Playground | [medux.io/playground/video/character-replacement-plus](https://medux.io/playground/video/character-replacement-plus) |
| Workshop | [medux.io/workshop/character-replacement-plus](https://medux.io/workshop/character-replacement-plus) |

- REST API example: [examples/ai-avatar/character-replacement-plus](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/ai-avatar/character-replacement-plus)
- Codex example: [codex/workshop/character-replacement-plus](../../../codex/workshop/character-replacement-plus/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
