# Safe tool approval

Review every proposed MCP call before approval. If a term below is unfamiliar, see [Concepts](concepts.md).

## Check the operation

- The tool name matches the requested workflow.
- The source file or asset ID belongs to the intended input.
- Prompts and titles contain no secrets or unnecessary personal information.
- Duration, resolution, model, and other cost-relevant options are intentional.
- Crop regions, timestamps, output formats, and placement coordinates are correct.

## Protect credentials and media

- Never include an API key in a prompt, screenshot, issue, or committed file.
- Treat signed upload and download URLs as temporary secrets.
- Do not commit private source media or generated results without permission.
- Obtain appropriate consent before cloning a person's voice or likeness.
- Keep the returned task ID so the agent can resume status checks safely.

## Verify the output

After completion, ask the agent to report:

- final task status;
- output file type and location;
- important dimensions, duration, or page count;
- any warning returned by Medux;
- whether the output passed the workflow-specific visual or document check.

