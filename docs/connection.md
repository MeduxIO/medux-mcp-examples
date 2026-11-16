# Connect Medux MCP

Medux is a hosted remote MCP service. There is nothing to install or run locally.

| | |
| --- | --- |
| **Endpoint** | `https://medux.io/mcp` (Streamable HTTP) |
| **Authentication** | OAuth sign-in (recommended) **or** `Authorization: Bearer sk-medux-...` |
| **Scope** | Same account, credits, tasks and assets as the Medux API and Workshop |

> [!NOTE]
> **Endpoint change.** The canonical endpoint is now `https://medux.io/mcp`.
> The previous address `https://medux.io/api/mcp/v1` still works, and existing
> API-key setups and OAuth grants keep working, so nothing breaks if you have not
> migrated. New setups should use `/mcp`.

## 1. Pick an authentication method

| Method | Best for | How |
| --- | --- | --- |
| **OAuth** (recommended) | Codex, Claude Code, claude.ai / Claude Desktop, ChatGPT web | Add the URL, then sign in to Medux in your browser and approve access. No key to copy. |
| **API key** | Clients without OAuth, CI, scripts, Cursor, VS Code | Create a key (starts with `sk-medux-`) in your Medux account and send it as a Bearer token. |

Details of the OAuth flow:

- Clients register themselves automatically (dynamic client registration) and use authorization code + PKCE (S256). You do not create an OAuth app.
- OAuth tokens only grant `mcp:tools`. They cannot call account-management APIs.
- Access lasts up to 1 hour and is refreshed automatically; the whole authorization expires after 30 days, after which you sign in again.
- Revoking a token revokes that whole authorization.

Keep API keys in your client's secret or environment-variable facility. Never commit them to a repository.

## 2. Connect your client

| Client | Guide | Recommended auth |
| --- | --- | --- |
| Codex (CLI, IDE extension, desktop app) | [codex.md](codex.md) | OAuth |
| Claude Code, claude.ai, Claude Desktop | [claude.md](claude.md) | OAuth |
| Cursor | [medux-cursor-plugin](https://github.com/MeduxIO/medux-cursor-plugin) | API key |
| VS Code / GitHub Copilot, registry listing | [medux-mcp](https://github.com/MeduxIO/medux-mcp) | API key |
| Anything else | Use the generic config below | Either |

Generic remote-server config (field names vary slightly per client; some use `mcpServers`, others `servers`):

```json
{
  "mcpServers": {
    "medux": {
      "type": "http",
      "url": "https://medux.io/mcp",
      "headers": { "Authorization": "Bearer ${MEDUX_API_KEY}" }
    }
  }
}
```

Omit `headers` when the client signs in with OAuth.

## 3. Verify

Ask your agent:

```text
List the tools exposed by the connected Medux MCP server. Do not call any tool.
Group the tools by image, video, voice, avatar, document, asset, and task operations.
For each tool, show only its name and one-sentence purpose.
```

This checks tool discovery without creating a billable task. Then try the free
account tools: `medux_health_check`, `medux_account_get`, `medux_balance_get`.

## What the server exposes

Every tool is prefixed `medux_`. The set is generated from the live capability catalog, so it grows over time; the connected server's `tools/list` is the source of truth.

| Group | Examples |
| --- | --- |
| Account | `medux_health_check`, `medux_account_get`, `medux_balance_get` |
| Files and tasks | `medux_file_create_upload_url`, `medux_task_query` |
| Video generation | `medux_video_generate_text_to_video`, `..._image_to_video`, `..._first_last_frame_to_video`, `..._omni_reference_to_video`, `medux_mv_director` |
| Video editing | `medux_trim_video`, `medux_merge_video`, `medux_resize_video`, `medux_video_upscale`, `medux_video_remove_subtitle`, `medux_video_face_swap`, `medux_video_character_replacement` |
| Image | `medux_text_to_image`, `medux_image_edit`, `medux_image_remove_background`, `medux_image_face_swap`, `medux_image_outfit_swap`, `medux_photo_repair` |
| Voice and audio | `medux_speech_create_audio`, `medux_clone_voice`, `medux_trim_audio`, `medux_merge_audio` |
| Avatar | `medux_avatar_clone_by_image`, `medux_avatar_clone_by_video` |
| Documents | `medux_pdf_to_word`, `medux_merge_pdf`, `medux_split_pdf`, `medux_ppt_to_pdf`, `medux_word_to_pdf` |

Playground → *For AI Agents* → **MCP** tab shows the exact `mcp_tool_id` and input schema for each capability.

## How a call works

The service is stateless: no `initialize` handshake is required before `tools/call`, and every request is authenticated on its own.

1. If the input is a local file, call `medux_file_create_upload_url` (`media_type`, `extension`), HTTP `PUT` the raw bytes to `upload_url`, and keep the returned `file.file_id`.
2. Call the operation tool with that `file_id`. Generation and processing tools return a `task_id` right away.
3. Poll `medux_task_query` with the `task_id` until the status is `SUCCEEDED`, then use `output_url`. Do not resubmit while a task is still running; image and video jobs can take several minutes.

See [Concepts](concepts.md) for files vs. assets and credits, and [Safe tool approval](safe-tool-approval.md) before approving billable calls.

## Troubleshooting

| Symptom | Likely cause and fix |
| --- | --- |
| `401 Unauthorized` | Missing `Bearer ` prefix, wrong or revoked key, or OAuth sign-in expired. Re-authenticate or re-create the key. |
| Client keeps asking to sign in | Authorization expired (30 days) or was revoked. Sign in again. |
| Works on `/api/mcp/v1`, fails on `/mcp` | Your client may cache the old OAuth resource. Remove the server, add it again with the `/mcp` URL and re-authenticate. |
| No Medux tools appear | Restart or reconnect the client; check its MCP log for the error. |
| `404 NOT_FOUND` on a task | The request reached Medux but the task or resource id does not exist. |
| Tool not found | Refresh the tool list; the live schema may have changed. |
| Local file cannot be used | Let the agent read the file, then run the signed-upload step first. |
| Task does not finish immediately | Expected: ask the agent to check the returned `task_id`. |
