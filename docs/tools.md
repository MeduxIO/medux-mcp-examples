# Medux MCP tool reference

All 69 tools exposed by `https://medux.io/mcp`, grouped by what they do. Names are exactly what the server returns from `tools/list`; the live schema stays the source of truth (`model_id` enums and defaults change as models are added).

Conventions used by every tool below:

- **Inputs that are files** take a `file_id` from `medux_file_create_upload_url` (see [Concepts](concepts.md)). Reusable voices and avatars take an `asset_id` returned by the clone tools.
- **`title`** is always optional. **`model_id`** is optional unless an enum is shown; omit it to use the default.
- **Task tools** return a `task_id` immediately. Poll `medux_task_query` until the status is `SUCCEEDED`, then read `output_url`. Task tools consume credits.
- Tools marked **free** create no task and cost nothing.

## Account, files and tasks

| Tool | Purpose | Required |
| --- | --- | --- |
| `medux_health_check` (free) | Check the service is reachable and your credential is accepted | none |
| `medux_account_get` (free) | Login email and current subscription plan | none |
| `medux_balance_get` (free) | Credit balance: available, reserved, per-source remaining | none |
| `medux_file_create_upload_url` (free) | Get a signed `upload_url` and `file.file_id`; then `PUT` the raw bytes | `media_type` (`VIDEO`, `AUDIO`, `IMAGE`, `DOCUMENT`), `extension` (no dot) |
| `medux_task_query` (free) | Read one task record: status, `output_url`, errors | `task_id` |

## Image

| Tool | Purpose | Required | Notable options |
| --- | --- | --- | --- |
| `medux_text_to_image` | Fast text to image | `prompt` | `model_id`: `zimage-turbo`, `krea2-turbo`, `moss-image-sft`, `qwen-image-21`, `minimax-h3-image`; `width`, `height`, `negative_prompt` |
| `medux_image_generate_text_to_image` | Text to image with reference images | `model_id`, `prompt` | `model_id`: `seedream-4-0`, `seedream-4-5`, `seedream-5-0`, `seedream-5-0-lite`, `seedream-5-0-pro`; `aspect_ratio`, `clarity`, `quantity`, `image_file_ids` (0 to 8) |
| `medux_image_edit` | Edit images from a text instruction | `image_file_ids`, `prompt` | `model_id`: `qwen-image-edit`, `qwen-image-21`, `minimax-h3-image`; `width`, `height`, `negative_prompt` |
| `medux_image_remove_background` | Remove background | `file_id` | |
| `medux_image_face_swap` | Put a reference face onto an image | `source_image_file_id`, `target_face_image_file_id` | |
| `medux_image_head_swap` | Replace the head, keep body and scene | `source_image_file_id`, `target_head_image_file_id` | |
| `medux_image_outfit_swap` | Transfer an outfit onto a subject | `source_image_file_id`, `target_outfit_image_file_id` | |
| `medux_photo_repair` | Restore an old photo | `source_image_file_id` | |

For the two generation tools, read the chosen model's `generation_options` and estimate credits before submitting.

## Video generation

All five video generation tools below share `model_id`, `prompt`, and optional `aspect_ratio`, `clarity`, `duration_seconds` (a listed discrete value). Supported `model_id`: `seedance-2-0-mini`, `seedance-2-0-fast`, `seedance-2-0`, `seedance-2-5`, `minimax-h3` (plus `wan3-0-video` for image-to-video and omni-reference).

| Tool | Purpose | Extra required input |
| --- | --- | --- |
| `medux_video_generate_text_to_video` | Prompt only | none |
| `medux_video_generate_image_to_video` | Animate one image | `file_id` |
| `medux_video_generate_first_last_frame_to_video` | Video between two frames | `image_file_ids`: exactly two, first then last |
| `medux_video_generate_omni_reference_to_video` | Use reference media, within the model's limits | optional `image_file_ids`, `video_file_ids`, `audio_file_ids` |
| `medux_text_image_to_video` | Video and audio from text with optional image, last frame and driving audio | `prompt_text`; optional `prompt_image_file_id`, `last_image_file_id`, `prompt_audio_file_id`, `resolution`, `seed` |
| `medux_mv_director` | Director-style music video from one track and one portrait | `prompt_audio_file_id`, `prompt_image_file_id`; optional `persona` |

## Talking video and avatars

| Tool | Purpose | Required |
| --- | --- | --- |
| `medux_avatar_clone_by_image` | Create a reusable avatar from a portrait | `file_id` |
| `medux_avatar_clone_by_video` | Create a reusable avatar from a video | `file_id` |
| `medux_video_create_text_driven` | Avatar video from a script | `avatar_asset_id`, `voice_asset_id`, `text` |
| `medux_video_create_audio_driven` | Avatar video from an audio file | `avatar_asset_id`, `audio_file_id` |
| `medux_image_audio_driven_video` | Talking video from an image, audio and prompt | `prompt_image_file_id`, `prompt_audio_file_id`, `prompt_text` |

## Voice and audio

| Tool | Purpose | Required |
| --- | --- | --- |
| `medux_clone_voice` | Create a reusable voice from audio | `file_id` |
| `medux_speech_create_audio` | Text to speech, optionally with a cloned voice | `text`; optional `voice_asset_id`, `model_id` (`speech-standard`) |
| `medux_trim_audio` | Cut to a time range | `input_file_id` and at least one of `start_time`, `end_time`, `duration` |
| `medux_merge_audio` | Concatenate audio | `input_file_ids` |
| `medux_change_audio_speed` | Speed up or slow down | `input_file_id`, `speed` |
| `medux_adjust_audio_volume` | Change volume | `input_file_id`, `volume` (for example `1.5`, `2dB`) |
| `medux_shift_audio_pitch` | Shift pitch | `input_file_id`, `semitones` |
| `medux_reverse_audio` | Reverse | `input_file_id` |

## Video editing

| Tool | Purpose | Required |
| --- | --- | --- |
| `medux_trim_video` | Cut to a time range | `input_file_id` and at least one of `start_time`, `end_time`, `duration` |
| `medux_split_video` | Split into segments | `input_file_id`, `segments` (`[{"start_time":"00:00:00","end_time":"00:00:05"}]`) |
| `medux_merge_video` | Concatenate videos | `input_file_ids` |
| `medux_resize_video` | Resize | `input_file_id`, `width`, `height` |
| `medux_rotate_video` | Rotate | `input_file_id`, `rotation` (90, 180, 270) |
| `medux_flip_video` | Flip | `input_file_id`, `flip_mode` (`horizontal`, `vertical`, `both`) |
| `medux_change_video_speed` | Change speed | `input_file_id`, `speed` |
| `medux_adjust_video_volume` | Change volume | `input_file_id`, `volume` |
| `medux_add_audio_to_video` | Replace or add an audio track | `video_file_id`, `audio_file_id` |
| `medux_add_logo_to_video` | Overlay a logo | `video_file_id`, `logo_file_id`; optional `x`, `y`, `logo_width` (needs `logo_height`), `logo_height` |
| `medux_video_upscale` | Upscale | `input_file_id`; optional `new_resolution` (longest side: `1920`, `3840`) |
| `medux_video_remove_background` | Remove background | `file_id` |

## Video cleanup

| Tool | Purpose | Required | Notable options |
| --- | --- | --- | --- |
| `medux_video_remove_subtitle` | Remove burned-in subtitles | `file_id` | `model_id`: `video-subtitle-removal-standard`, `video-subtitle-removal-minimax-remover`; `region` `{x,y,width,height}` |
| `medux_video_logo_removal` | Remove a logo using logo references | `input_video_file_id` | `logo_file_id` (list), `logo_type`: `default`, `tiktok`, `heygen`, `veo`, `keling`, `instagram`, `luma`, `pika`, `snapchat`, `pixverse`; `video_size` |
| `medux_watermark_removal` | Remove a watermark by region | `input_file_id`, `regions` (`[[x, y, width, height]]`) | |
| `medux_watermark_removal_by_prompt` | Remove a watermark by description | `input_file_id`, `prompt_text` | |
| `medux_remove_video_object` | Remove an object by region | `input_file_id`, `regions` | |
| `medux_remove_video_object_by_prompt` | Remove an object by description | `input_file_id`, `prompt_text` | |

## Video faces and characters

| Tool | Purpose | Required |
| --- | --- | --- |
| `medux_video_face_swap` | Replace a face in a video | `input_video_file_id`, `source_image_file_id` |
| `medux_video_face_swap_plus` | Face swap with the MiniMax H3 generative workflow | `input_video_file_id`, `source_image_file_id` |
| `medux_video_character_replacement` | Replace the main character | `source_video_file_id`, `target_character_image_file_id` |
| `medux_video_character_replacement_plus` | Character replacement with MiniMax H3 and two references | `source_video_file_id`, `target_character_image_file_id` |
| `medux_animate_head_swap` | Animate a swapped head with a driving video | `face_image_file_id`, `input_video_file_id`; optional `positive_prompt`, `negative_prompt`, `edit_prompt`, `width`, `height` |

## Documents

| Tool | Purpose | Required | Notable options |
| --- | --- | --- | --- |
| `medux_pdf_to_word` / `medux_pdf_to_docx` | PDF to `.docx` | `input_file_id` | |
| `medux_pdf_to_excel` | Extract tables to `.xlsx` | `input_file_id` | `flavor` (`stream`, `lattice`), `pages` |
| `medux_pdf_to_ppt` | PDF to `.pptx` | `input_file_id` | `render_scale` (default 2.0) |
| `medux_pdf_to_images` | Pages to a zip of images | `input_file_id` | `image_format` (`jpeg`, `png`) |
| `medux_pdf_to_jpg` / `medux_pdf_to_png` | Pages to a zip of JPEG or PNG | `input_file_id` | |
| `medux_merge_pdf` | Merge PDFs | `input_file_ids` | |
| `medux_split_pdf` | Extract pages into a new PDF | `input_file_id`, `page_range` (`1-3`, `1,3,5`) | |
| `medux_word_to_pdf` / `medux_ppt_to_pdf` / `medux_excel_to_pdf` | Office to PDF | `input_file_id` | |
| `medux_images_to_pdf` / `medux_jpg_png_to_pdf` | Images to one PDF | `input_file_ids` | |

## Prompts for tools added recently

These tools have no tutorial-derived example in [`examples/`](../examples/codex/INDEX.md). Each prompt below works in Codex, Claude Code and claude.ai (attach files in claude.ai). They are documentation-derived, not live-tested; see the [verification policy](verification.md).

| Tool | Example prompt |
| --- | --- |
| `medux_health_check` | `Use Medux to run a health check and tell me whether my credential is accepted.` |
| `medux_account_get` | `Use Medux to show which account and plan I am connected as.` |
| `medux_balance_get` | `Use Medux to show my credit balance before we start.` |
| `medux_file_create_upload_url` | `Upload ./clip.mp4 to Medux (media_type VIDEO, extension mp4) and tell me the file_id. Do not start any task.` |
| `medux_image_generate_text_to_image` | `Use Medux medux_image_generate_text_to_image with seedream-5-0 for "a lighthouse at dawn, film still", 16:9. Show the model's supported options and credit estimate first.` |
| `medux_image_edit` | `Edit ./portrait.png with Medux: change the background to a rainy street. Use qwen-image-edit and show me the arguments before submitting.` |
| `medux_video_generate_first_last_frame_to_video` | `Use Medux to generate a video that starts at ./start.png and ends at ./end.png, prompt "a slow dolly push-in", model seedance-2-0-fast.` |
| `medux_video_generate_omni_reference_to_video` | `Use Medux to generate a video from the prompt and the two reference images in ./refs. Check the model's reference limits first.` |
| `medux_text_image_to_video` | `Use Medux medux_text_image_to_video with prompt "a street musician at night" and ./cover.png as the reference image.` |
| `medux_mv_director` | `Use Medux medux_mv_director with ./song.mp3 and ./artist.png to create a music video. Tell me the credit cost before submitting.` |
| `medux_add_logo_to_video` | `Add ./logo.png to the top-right of ./clip.mp4 using Medux. Logo width 160, height 80.` |
| `medux_video_face_swap` / `medux_video_face_swap_plus` | `Use Medux to replace the face in ./clip.mp4 with the face in ./face.jpg. Only use faces I have the right to use.` |
| `medux_video_character_replacement_plus` | `Use Medux to replace the main character in ./scene.mp4 with the character in ./character.png using the plus workflow.` |
| `medux_watermark_removal` | `Remove the watermark in ./clip.mp4 with Medux. The watermark is at x=20, y=20, 180 by 60 pixels.` |
| `medux_watermark_removal_by_prompt` | `Remove the corner watermark from ./clip.mp4 with Medux by prompt: "the semi-transparent logo in the bottom-right corner".` |
| `medux_remove_video_object_by_prompt` | `Remove the person in the red jacket from ./clip.mp4 with Medux by prompt.` |

## REST-only operations

Listing and managing assets, results and tasks (`list assets`, `list tasks`, `list results`, list voices and avatars, edit voice parameters, create video by project) exist in the [REST API](https://github.com/MeduxIO/medux-api-examples) but are **not** exposed as MCP tools. Over MCP, use `medux_task_query` to check a task and the clone tools' task output to obtain reusable voice and avatar `asset_id`s.
