# Medux concepts for MCP workflows

This page explains the terms the examples in this repository use, so an agent's
proposed tool call is easy to review. Medux organizes its tools around the same
four product modules used on the [tutorials site](https://medux.io/tutorials/):
**Clone**, **Generate**, **Process**, and **Infra**. The live MCP schema and the
[API reference](https://medux.io/api-reference/) are always the source of truth;
names and accepted values below can change.

## Account, credits, and billing

Every workflow runs against your Medux account and requires an API key created
from the [Medux MCP page](https://medux.io/overview/mcp). Generation and
processing operations consume account **credits** and are billable, so an
approved tool call can cost money. Discovery and listing calls (for example
listing tools, avatars, voices, tasks, or results) are the cheap, non-billable
way to explore. Check current rates on the [pricing page](https://medux.io/pricing)
before approving expensive video or avatar jobs.

## Files vs. assets

Medux distinguishes a one-off uploaded **file** from a reusable **asset**.

A **file** is raw input you upload for a single operation. Uploading returns a
`file_id` (some tools take a list such as `input_file_ids`). A file is the input
to a Generate or Process job; it is not automatically reusable or named.

An **asset** is a persistent, reusable resource created through the Clone module,
most commonly a cloned **voice** or a cloned **avatar**. An asset has its own ID
(for example a voice or avatar ID) and can be reused across many later Generate
calls. Because an asset can be identity-linked, only create one from media you
are authorized to use, and give it a title that does not imply a misleading
identity.

## Uploading local input

Remote MCP connectors (claude.ai, Claude Desktop) cannot read arbitrary files
from your computer, and even local clients must hand bytes to Medux before a job
can run. The pattern is: the agent requests a **signed upload URL** from Medux,
uploads the bytes to it, and receives the `file_id` used by later tool calls.
Treat signed upload and download URLs as temporary secrets — they grant access
without further authentication and should never be committed or shared.

## Tasks: the async lifecycle

Most Generate and Process operations are **asynchronous**. Creating the job does
not return the finished media; it returns a **`task_id`**. The agent then polls a
task-status tool (for example `medux_get_task` / `medux_task_query`, or the
module-specific `medux_get_voice_task` and `medux_get_avatar_task`) until the
task reports success or failure, and only then downloads the result. Two
consequences worth checking when you review a call: keep the returned `task_id`
so a status check can be resumed, and expect a completed job to expose a result
you can download rather than inline media. Listing tools (`medux_list_tasks`,
`medux_list_results`) let you find earlier jobs and their outputs.

## Common request fields

These fields recur across the examples. Confirm each one matches your intent
before approving, since several affect cost or the final output:

`prompt` — the text description driving a Generate job (subject, motion, framing,
style).

`model_id` — which underlying model runs the job. Leaving it unset usually
applies the Medux default; set it only to a currently supported model.

`aspect_ratio` — output shape, e.g. `16:9` or `9:16`.

`clarity` / resolution — output quality tier, e.g. `720P`. Higher tiers can cost
more.

`duration_seconds` — output length for video or audio; longer output can cost
more.

`title` — an optional human-readable label for the task or asset. Keep secrets
and unnecessary personal information out of it.

## Where each term is defined authoritatively

- Tool names and exact argument schemas: the live MCP tool list (`/mcp` in Codex
  or Claude Code) and the [API reference](https://medux.io/api-reference/).
- Connection endpoint and authentication: your [Medux MCP account page](https://medux.io/overview/mcp).
- Pricing and credit costs: the [pricing page](https://medux.io/pricing).

Review each proposed call against these before approval — see
[Safe tool approval](safe-tool-approval.md).
