# Verification

- Status: Tested with Claude Code
- Date: 2026-11-17
- Client version or surface: Claude Code in the Claude desktop app (Code tab), Medux connected as a remote MCP server; version not recorded
- Medux tool: `medux_file_create_upload_url` (x3), `medux_video_face_swap_plus`, `medux_task_query`
- Input type: 5-second MP4 (720x1280) plus a PNG face image; both subjects were AI-generated fictional people, so no real person's likeness was used
- Result: success
- Notes:
  - Arguments: `input_video_file_id` (video file ID), `source_image_file_id` (image file ID), `model_id: face-swap-plus-default`.
  - The task went `QUEUED` -> `PROCESSING` -> `SUCCEEDED` in about 6 minutes. The input was billed as 6 seconds (5.04 s rounded up), 480 credits.
  - The output was a 448x768 MP4 of about 4.9 s with an audio track. The target person was replaced by the person in the source image, including hair and clothing, which is expected for the generative workflow. Output resolution is lower than the input.
  - Local files had to be uploaded with `PUT` to the returned `upload_url` before the tool call; passing a URL or a local path is not accepted.
  - Only the Claude example was tested. The Codex example remains documentation-derived.
