# Convert PDF to Word with Codex and Medux MCP

Convert a PDF into a `.docx` document with Codex. This example is derived from the linked Codex tutorial. The expected tool is `medux_pdf_to_word`.

## Prompt

```text
Using the connected Medux MCP server, convert SOURCE.pdf in this Codex workspace
to a Word document. Inspect and upload the PDF if needed. Show me the source file
ID and exact Medux tool arguments, then wait for my approval.

After completion, download the .docx file into this workspace, report its saved
path, and verify with an available local document tool that the output opens and
has content. Do not overwrite the source PDF.
```

## Review before approval

- Tool: `medux_pdf_to_word`
- `input_file_id`: resolves to the intended PDF
- `model_id`: use the current default unless another supported model is required
- Output will be written to a new `.docx` file

## Codex notes

- Confirm the Medux server and tool with `/mcp`.
- Codex can inspect the local PDF before upload and verify the downloaded `.docx`; it may request command approval for either step.

## Learn more

- [Complete Codex MCP tutorial](https://medux.io/tutorials/document_pdf_to_word_codex_mcp.html)
- [PDF to Word API reference](https://medux.io/api-reference/document/pdf-to-word)
