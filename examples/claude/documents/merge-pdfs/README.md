# Merge PDFs with Claude and Medux MCP

Combine multiple PDF files with Claude. This example is derived from the linked Claude tutorial. The expected tool is `medux_merge_pdf`.

## Prompt

```text
Use the connected Medux tool to merge the attached FIRST.pdf, SECOND.pdf, and
THIRD.pdf in that exact order. Upload each source file to Medux if needed.

Before calling the merge tool, show me the ordered list of source file IDs and
the exact Medux arguments, then wait for my approval. After approval, monitor the
task and return the merged PDF. Verify, when the client supports it, that its
page count equals the sum of the input page counts. Do not modify the sources.
```

## Review before approval

- Tool: `medux_merge_pdf`
- `input_file_ids`: contains every intended PDF in the correct order
- `model_id`: use the current default unless another supported model is required
- The output title is descriptive and contains no sensitive information

## Claude notes

- In claude.ai or Claude Desktop, attach the PDFs in the intended order and enable the Medux connector.
- In Claude Code, put the PDFs in the working directory and verify the server with `/mcp`.
- Confirm the ordered `input_file_ids` list; attachment display order is not a safe substitute for checking tool arguments.

## Learn more

- [Complete Claude MCP tutorial](https://medux.io/tutorials/document_merge_pdf_claude_mcp.html)
- [Merge PDF API reference](https://medux.io/api-reference/document/merge-pdf)

<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/document/merge-pdf](https://medux.io/playground/document/merge-pdf) |

- REST API example: [examples/document/merge-pdf](https://github.com/MeduxIO/medux-api-examples/tree/main/examples/document/merge-pdf)
- Codex example: [codex/documents/document-merge-pdf](../../../codex/documents/document-merge-pdf/README.md)
- All pages: [Playground and Workshop pages](../../../../docs/workshop-pages.md)
<!-- medux-pages:end -->
