# How to Edit an Image from a Text Instruction with Claude MCP and Medux

Edit one or more images from a text instruction, then poll the task and save the result.

## Expected Medux tools

- `medux_file_create_upload_url` (once per input image)
- `medux_image_edit`
- `medux_task_query`

## Prompt

```text
Edit ./portrait.png with Medux: change the background to a rainy street at night. Use qwen-image-edit, show me the arguments before submitting, then poll the task and save the result next to the input.
```

## Review before approval

- `image_file_ids` (required): the file IDs of the uploaded images, in the order you intend.
- `prompt` (required): the edit you want, not a description of the whole image.
- `model_id` (optional): `qwen-image-edit`, `qwen-image-21` or `minimax-h3-image`.
- `width` / `height` / `negative_prompt` (optional): leave unset unless you need them.
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
| Playground | [medux.io/playground/image/image-edit-turbo](https://medux.io/playground/image/image-edit-turbo) |
| Workshop | [medux.io/workshop/image-edit](https://medux.io/workshop/image-edit) |
| Workshop | [medux.io/workshop/qwen-image-edit](https://medux.io/workshop/qwen-image-edit) |

- REST API example: [examples/image/image-edit-turbo](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/image/image-edit-turbo)
- Codex example: [codex/workshop/image-edit-turbo](../../../codex/workshop/image-edit-turbo/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
