# How to Generate an Image with Seedream (Reference Images Optional) with Codex MCP and Medux

Generate an image with a Seedream model, optionally guided by up to 8 reference images.

## Expected Medux tools

- `medux_file_create_upload_url` (only when using reference images)
- `medux_image_generate_text_to_image`
- `medux_task_query`

## Prompt

```text
Use Medux medux_image_generate_text_to_image with seedream-5-0 for "a lighthouse at dawn, film still", 16:9. Show me the model's supported options and the credit estimate first, then generate and save the result.
```

## Review before approval

- `model_id` (required): `seedream-4-0`, `seedream-4-5`, `seedream-5-0`, `seedream-5-0-lite` or `seedream-5-0-pro`.
- `prompt` (required).
- `aspect_ratio`, `clarity`, `quantity` (optional): read the chosen model's `generation_options` first.
- `image_file_ids` (optional): 0 to 8 uploaded reference images.
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
| Playground | [medux.io/playground/image/text-to-image](https://medux.io/playground/image/text-to-image) |
| Workshop | [medux.io/workshop/seedream](https://medux.io/workshop/seedream) |

- REST API example: [examples/generate/create-text-to-image](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/generate/create-text-to-image)
- Claude example: [claude/workshop/create-text-to-image](../../../claude/workshop/create-text-to-image/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
