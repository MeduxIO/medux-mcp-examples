# Remove an image background with Claude and Medux MCP

Remove the background from an uploaded image with Claude. This example is derived from the linked Claude tutorial. The expected tool is `medux_image_remove_background`.

## Prompt

```text
Use the connected Medux tool to remove the background from the attached
SOURCE_IMAGE.
Process the full image and preserve fine edges around the subject.

Show me the uploaded file ID and proposed Medux tool arguments and wait for my
approval. After the task completes, return the transparent-background result
and report its file type and dimensions.
```

## Review before approval

- Tool: `medux_image_remove_background`
- `file_id`: resolves to the correct image
- `region`: omit it for the whole image, or verify `x`, `y`, `width`, and `height`
- `title`: optional descriptive task title

## Claude notes

- In claude.ai or Claude Desktop, attach the image to the conversation and enable the Medux connector for that conversation.
- In Claude Code, place the image in the working directory and confirm Medux with `/mcp`.
- A chat attachment does not imply that Medux already has a `file_id`; Claude must complete the Medux upload step when required.

## Learn more

- [Complete Claude MCP tutorial](https://medux.io/tutorials/process_create_image_background_removal_claude_mcp.html)
- [Image Background Removal API reference](https://medux.io/api-reference/process/create-image-background-removal)
