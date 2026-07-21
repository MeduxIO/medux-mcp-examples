# Contributing

Contributions should add or improve a reproducible Medux MCP workflow.

## Add an example

1. Create a descriptive directory under `examples/codex/` or `examples/claude/`; do not publish one unverified prompt as client-neutral.
2. Add a `README.md` using the structure of an existing example.
3. Include one copyable prompt, the expected tool, an approval checklist, and links to the matching Medux tutorial and API reference.
4. Add the example to the table in the root README.
5. Run `./scripts/check.sh`.

Follow [the verification policy](docs/verification.md). Only add a `Tested with` claim when the matching sanitized verification record is included.

Use the live MCP tool schema and Medux API reference as the source of truth. Examples must not contain credentials, signed URLs, private media, unlicensed assets, or claims that were not verified.

## Pull requests

Keep each pull request focused. Explain what the workflow does, which tool it uses, how you checked it, and any account credits required during testing.
