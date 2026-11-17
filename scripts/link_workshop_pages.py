#!/usr/bin/env python3
"""Link every Medux Playground and Workshop function page to its examples.

For each page this connects three things, in both directions:
  * the medux.io page,
  * the MCP example (examples/claude/... and examples/codex/...),
  * the REST API example in the sibling checkout ../medux-api-examples.

It (1) writes the few MCP examples that did not exist yet, (2) writes
docs/workshop-pages.json and docs/workshop-pages.md, and (3) injects an
idempotent "Try it on medux.io" block into the mapped MCP READMEs.
The API repo's scripts/link_workshop_pages.py reads docs/workshop-pages.json and
does the same for the API examples. Re-run both after examples are regenerated.

    python3 scripts/link_workshop_pages.py
"""
import json
import os
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
API_ROOT = os.path.normpath(os.path.join(ROOT, "..", "medux-api-examples"))
EX = os.path.join(ROOT, "examples")
SITE = "https://medux.io"
CLIENTS = ("claude", "codex")

# --------------------------------------------------------------------------
# Page table: (site paths, API example slug, MCP tool)
# --------------------------------------------------------------------------
P = "/playground/"
W = "/workshop/"
BRANDS = ["filmora", "heygen", "inshot", "instagram", "kling", "luma", "pika",
          "pixverse", "snapchat", "tiktok", "veo"]
DOCS = ["excel-to-pdf", "images-to-pdf", "jpg-png-to-pdf", "merge-pdf", "pdf-to-docx",
        "pdf-to-excel", "pdf-to-images", "pdf-to-jpg", "pdf-to-png", "pdf-to-ppt",
        "pdf-to-word", "ppt-to-pdf", "split-pdf", "word-to-pdf"]
UTIL_AUDIO = ["adjust-audio-volume", "change-audio-speed", "merge-audio",
              "reverse-audio", "shift-audio-pitch", "trim-audio"]
UTIL_VIDEO = ["add-audio-to-video", "add-logo-to-video", "adjust-video-volume",
              "change-video-speed", "flip-video", "merge-video", "resize-video",
              "rotate-video", "split-video", "trim-video"]

ROWS = []  # (pages, api_slug, tool)


def row(pages, slug, tool):
    ROWS.append(([pages] if isinstance(pages, str) else list(pages), slug, tool))


for s in UTIL_AUDIO:
    row(f"{P}audio/{s}", s, "medux_" + s.replace("-", "_"))
for s in DOCS:
    row(f"{P}document/{s}", s, "medux_" + s.replace("-", "_"))
for s in UTIL_VIDEO:
    row(f"{P}video/{s}", s, "medux_" + s.replace("-", "_"))
row(f"{P}avatar/clone-by-image", "create-avatar-by-image", "medux_avatar_clone_by_image")
row(f"{P}avatar/clone-by-video", "create-avatar-by-video", "medux_avatar_clone_by_video")
row(f"{P}voice/voice-clone", "create-voice", "medux_clone_voice")
row(f"{P}image/background-removal", "create-image-background-removal", "medux_image_remove_background")
row([f"{P}image/face-swap", f"{W}image-face-swap"], "face-swap", "medux_image_face_swap")
row(f"{P}image/head-swap", "head-swap", "medux_image_head_swap")
row([f"{P}image/image-edit-turbo", f"{W}image-edit", f"{W}qwen-image-edit"], "image-edit-turbo", "medux_image_edit")
row([f"{P}image/outfit-swap", f"{W}outfit-swap"], "outfit-swap", "medux_image_outfit_swap")
row([f"{P}image/photo-repair", f"{W}old-photo-repair"], "photo-repair", "medux_photo_repair")
row([f"{P}image/text-to-image", f"{W}seedream"], "create-text-to-image", "medux_image_generate_text_to_image")
row([f"{P}image/text-to-image-turbo", f"{W}krea2-turbo-unlimited", f"{W}moss-image",
     f"{W}z-image", f"{W}qwen-text-to-image", f"{W}minimax-h3-image"],
    "text-to-image-turbo", "medux_text_to_image")
row([f"{P}speech/text-to-speech-audio", f"{W}tts", f"{W}voice"], "create-audio", "medux_speech_create_audio")
row([f"{P}video/audio-driven-lip-sync", f"{W}lipsync"], "create-audio-driven-video", "medux_video_create_audio_driven")
row(f"{P}video/text-driven-lip-sync", "create-text-driven-video", "medux_video_create_text_driven")
row([f"{P}video/image-audio-driven-video"], "image-audio-driven-video", "medux_image_audio_driven_video")
row(f"{P}video/background-removal", "create-video-background-removal", "medux_video_remove_background")
row(f"{P}video/subtitle-removal", "create-video-subtitle-removal", "medux_video_remove_subtitle")
row([f"{P}video/video-logo-removal"] + [f"{W}remove/{b}-video-logo-removal" for b in BRANDS]
    + [f"{W}remove"], "video-logo-removal", "medux_video_logo_removal")
row(f"{P}video/watermark-removal", "watermark-removal", "medux_watermark_removal")
row(f"{P}video/watermark-removal-by-prompt", "watermark-removal-by-prompt", "medux_watermark_removal_by_prompt")
row(f"{P}video/remove-video-object", "remove-video-object", "medux_remove_video_object")
row(f"{P}video/remove-video-object-by-prompt", "remove-video-object-by-prompt", "medux_remove_video_object_by_prompt")
row([f"{P}video/character-replacement", f"{W}character-replacement"], "character-replacement", "medux_video_character_replacement")
row([f"{P}video/character-replacement-plus", f"{W}character-replacement-plus"], "character-replacement-plus", "medux_video_character_replacement_plus")
row([f"{P}video/face-swap-plus", f"{W}face-swap-plus"], "face-swap-plus", "medux_video_face_swap_plus")
row([f"{P}video/video-face-swap", f"{W}face-swap"], "video-face-swap", "medux_video_face_swap")
row(f"{P}video/video-head-swap", "video-head-swap", "medux_animate_head_swap")
row(f"{P}video/video-upscale", "video-upscale", "medux_video_upscale")
row([f"{P}video/text-to-video", f"{W}seedance25"], "create-text-to-video", "medux_video_generate_text_to_video")
row([f"{P}video/image-to-video", f"{W}image-to-video", f"{W}wan3"], "create-image-to-video", "medux_video_generate_image_to_video")
row([f"{P}video/first-last-frame-to-video", f"{W}first-last-frame-to-video"], "create-first-last-frame-to-video", "medux_video_generate_first_last_frame_to_video")
row(f"{P}video/omni-reference-to-video", "create-omni-reference-to-video", "medux_video_generate_omni_reference_to_video")
row([f"{P}video/text-image-to-video", f"{W}minimax-h3-unlimited"], "text-image-to-video", "medux_text_image_to_video")
row([f"{P}video/mv-director", f"{W}mv-director"], "mv-director", "medux_mv_director")
row([f"{W}remove/image-background"], "create-image-background-removal", "medux_image_remove_background")
row([f"{W}remove/video-background"], "create-video-background-removal", "medux_video_remove_background")
row([f"{W}remove/video-subtitles"], "create-video-subtitle-removal", "medux_video_remove_subtitle")
row([f"{W}remove/video-object"], "remove-video-object", "medux_remove_video_object")
row([f"{W}remove/video-object-by-prompt"], "remove-video-object-by-prompt", "medux_remove_video_object_by_prompt")
row([f"{W}remove/video-watermark-by-prompt"], "watermark-removal-by-prompt", "medux_watermark_removal_by_prompt")
# Programmatic page families: one example for the whole family.
row([f"{W}avatar", f"{W}avatar/*"], "create-text-driven-video", "medux_video_create_text_driven")
row([f"{W}voice/*"], "create-audio", "medux_speech_create_audio")

# Pages whose workflow is not available through MCP yet.
NO_MCP = {f"{P}video/ltx-dub-it": "LTX-2.3 Dub-It video dubbing"}

# Overview pages: linked to the example indexes instead of a single example.
HUBS = [f"/playground", f"/workshop"]

# --------------------------------------------------------------------------
# New examples (no tutorial-derived MCP example exists for these tools)
# --------------------------------------------------------------------------
NEW = {
    "image-edit-turbo": dict(
        title="Edit an Image from a Text Instruction",
        intro="Edit one or more images from a text instruction, then poll the task and save the result.",
        tools=["medux_file_create_upload_url (once per input image)", "medux_image_edit", "medux_task_query"],
        prompt="Edit ./portrait.png with Medux: change the background to a rainy street at night. Use qwen-image-edit, show me the arguments before submitting, then poll the task and save the result next to the input.",
        review=["`image_file_ids` (required): the file IDs of the uploaded images, in the order you intend.",
                "`prompt` (required): the edit you want, not a description of the whole image.",
                "`model_id` (optional): `qwen-image-edit`, `qwen-image-21` or `minimax-h3-image`.",
                "`width` / `height` / `negative_prompt` (optional): leave unset unless you need them."]),
    "create-text-to-image": dict(
        title="Generate an Image with Seedream (Reference Images Optional)",
        intro="Generate an image with a Seedream model, optionally guided by up to 8 reference images.",
        tools=["medux_file_create_upload_url (only when using reference images)", "medux_image_generate_text_to_image", "medux_task_query"],
        prompt='Use Medux medux_image_generate_text_to_image with seedream-5-0 for "a lighthouse at dawn, film still", 16:9. Show me the model\'s supported options and the credit estimate first, then generate and save the result.',
        review=["`model_id` (required): `seedream-4-0`, `seedream-4-5`, `seedream-5-0`, `seedream-5-0-lite` or `seedream-5-0-pro`.",
                "`prompt` (required).",
                "`aspect_ratio`, `clarity`, `quantity` (optional): read the chosen model's `generation_options` first.",
                "`image_file_ids` (optional): 0 to 8 uploaded reference images."]),
    "create-first-last-frame-to-video": dict(
        title="Generate a Video Between a First and a Last Frame",
        intro="Generate a video that starts at one image and ends at another, then poll the task and download the result.",
        tools=["medux_file_create_upload_url (twice)", "medux_video_generate_first_last_frame_to_video", "medux_task_query"],
        prompt='Use Medux to generate a video that starts at ./start.png and ends at ./end.png, prompt "a slow dolly push-in", model seedance-2-0-fast. Show the model options and credit estimate before submitting.',
        review=["`image_file_ids` (required): exactly two file IDs, first frame then last frame.",
                "`model_id` and `prompt` (required).",
                "`duration_seconds`, `clarity`, `aspect_ratio` (optional): must be values the chosen model lists.",
                "Estimate credits before submitting; video generation is billed by duration."]),
    "create-omni-reference-to-video": dict(
        title="Generate a Video from Reference Images, Videos and Audio",
        intro="Generate a video that follows reference media (images, videos, audio) within the chosen model's limits.",
        tools=["medux_file_create_upload_url (once per reference file)", "medux_video_generate_omni_reference_to_video", "medux_task_query"],
        prompt="Use Medux to generate a video from the prompt below and the two reference images in ./refs. Check the model's reference limits first, show me the arguments, then poll the task and save the result.\nPrompt: the two characters walk through a night market, handheld camera.",
        review=["`image_file_ids`, `video_file_ids`, `audio_file_ids` (optional): only the reference types the model accepts, within its counts.",
                "`model_id` and `prompt` (required).",
                "Do not upload references you do not have the right to use."]),
    "character-replacement-plus": dict(
        title="Replace the Main Character in a Video with Character Replacement Plus",
        intro="Replace the main character of a video with a character from a reference image using the MiniMax H3 workflow.",
        tools=["medux_file_create_upload_url (once per input file)", "medux_video_character_replacement_plus", "medux_task_query"],
        prompt="Use Medux Character Replacement Plus to replace the main character in ./clip.mp4 with the character in ./character.png. Upload both files first, poll until the task finishes, and save the result. I have the right to use both inputs.",
        review=["`source_video_file_id` (required): the video whose main character is replaced.",
                "`target_character_image_file_id` (required): the replacement character image.",
                "A second reference image is accepted by the tool; check its live schema before adding one.",
                "Billing is per second of input video; check your plan's length limit."]),
    "mv-director": dict(
        title="Create a Music Video with MV Director",
        intro="Create a director-style music video from one audio track and one portrait.",
        tools=["medux_file_create_upload_url (audio, then portrait)", "medux_mv_director", "medux_task_query"],
        prompt="Use Medux MV Director to make a music video from ./song.mp3 and the portrait ./artist.png. Upload both files, show me the arguments, poll the task and save the result.",
        review=["`prompt_audio_file_id` (required): the audio track's file ID.",
                "`prompt_image_file_id` (required): the portrait's file ID.",
                "`persona` (optional): leave unset unless you want to steer the director style.",
                "Use audio and a portrait you have the right to use."]),
    "text-image-to-video": dict(
        title="Create a Video with Minimax H3 from Text and Optional Images",
        intro="Create a video and audio from text, optionally with a first image, a last image and driving audio.",
        tools=["medux_file_create_upload_url (only for optional inputs)", "medux_text_image_to_video", "medux_task_query"],
        prompt='Use Medux medux_text_image_to_video with the prompt "a paper boat drifting down a rainy street, cinematic" and ./first.png as the first image. Show me the arguments and the credit estimate before submitting, then poll the task and save the result.',
        review=["`prompt_text` (required).",
                "`prompt_image_file_id`, `last_image_file_id`, `prompt_audio_file_id` (optional): uploaded file IDs.",
                "`resolution`, `seed` (optional)."]),
    "video-face-swap": dict(
        title="Swap a Face in a Video",
        intro="Replace a face in a video with the face in a reference image, then poll the task and save the result. Only use faces you have the right to use.",
        tools=["medux_file_create_upload_url (once per input file)", "medux_video_face_swap", "medux_task_query"],
        prompt="Use Medux to replace the face in ./clip.mp4 with the face in ./face.jpg. Upload both files first, run the video face swap, poll the task until it finishes and save the result. I have the right to use both the video and the face in the image.",
        review=["`input_video_file_id` (required): the video's file ID, not the image's.",
                "`source_image_file_id` (required): the face image's file ID, not the video's.",
                "Use a clear, front-facing face image and a video where the face stays visible."]),
    "remove-video-object-by-prompt": dict(
        title="Remove an Object from a Video by Describing It",
        intro="Remove an object from a video by describing it in text instead of drawing a region.",
        tools=["medux_file_create_upload_url", "medux_remove_video_object_by_prompt", "medux_task_query"],
        prompt='Use Medux to remove "the red bicycle on the left" from ./clip.mp4. Upload the file, show me the arguments, poll the task and save the result.',
        review=["`input_file_id` (required): the uploaded video's file ID.",
                "`prompt_text` (required): describe exactly one object, with a position or colour.",
                "Check the result for leftover artifacts before using it."]),
}

CLIENT_NOTES = {
    "claude": """- In claude.ai or Claude Desktop, attach inputs and enable the Medux connector for the conversation.
- In Claude Code, keep inputs in the working directory and confirm Medux with `/mcp`.
- An attachment is not a Medux `file_id`; approve the upload step when the workflow requires one.""",
    "codex": """- Use `/mcp` to confirm that Medux and the expected tool are available.
- Workspace paths must point to the intended local inputs and output directory.
- Review any network, shell, or filesystem approval requested during upload, download, or verification.""",
}

BEGIN, END = "<!-- medux-pages:start -->", "<!-- medux-pages:end -->"


# --------------------------------------------------------------------------
def norm_tool(t):
    t = t.strip("` ")
    return t if t.startswith("medux_") else "medux_" + t


def read_index(client):
    """tool -> example dir (relative to examples/<client>), preferring single-tool rows."""
    rows = []
    for line in open(f"{EX}/{client}/INDEX.md"):
        m = re.match(r"\| \[.*?\]\((.*?)/README\.md\) \| (.*?) \|", line)
        if m:
            tools = [norm_tool(x) for x in re.findall(r"`([^`]+)`", m.group(2))]
            rows.append((m.group(1), tools))
    out = {}
    for d, tools in sorted(rows, key=lambda r: len(r[1])):
        for t in tools:
            if t != "medux_task_query":
                out.setdefault(t, d)
    return out


def api_dirs():
    """slug -> examples/<cat>/<slug> in the API repo (skipping 'Moved' stubs)."""
    out = {}
    for cat in sorted(os.listdir(f"{API_ROOT}/examples")):
        base = f"{API_ROOT}/examples/{cat}"
        if not os.path.isdir(base):
            continue
        for slug in sorted(os.listdir(base)):
            p = f"{base}/{slug}/README.md"
            if os.path.exists(p) and not open(p).read().startswith("# Moved:"):
                out.setdefault(slug, f"examples/{cat}/{slug}")
    return out


def write_new(slug, spec, client):
    d = f"{EX}/{client}/workshop/{slug}"
    os.makedirs(d, exist_ok=True)
    tools = "\n".join(f"- `{t.split(' (')[0]}`" + (f" ({t.split(' (',1)[1]}" if " (" in t else "") for t in spec["tools"])
    review = "\n".join(f"- {r}" for r in spec["review"])
    text = f"""# How to {spec['title']} with {client.capitalize()} MCP and Medux

{spec['intro']}

## Expected Medux tools

{tools}

## Prompt

```text
{spec['prompt']}
```

## Review before approval

{review}
- Every local file or attachment maps to the intended Medux file or asset ID.
- Operation order, output settings, and cost-relevant options match the request.

## {client.capitalize()} notes

{CLIENT_NOTES[client]}

## Learn more

- [Medux tutorials](https://medux.io/tutorials/)
- [Tool reference](../../../../docs/tools.md)
- [Medux MCP overview](https://medux.io/overview/mcp)

## Verification

Status: **Documentation-derived**. See the repository [verification policy](../../../../docs/verification.md).
"""
    open(f"{d}/README.md", "w").write(text)
    return f"workshop/{slug}"


def main():
    idx = {c: read_index(c) for c in CLIENTS}
    apis = api_dirs()
    # FSP was tested by hand and lives under edit/.
    for c in CLIENTS:
        idx[c]["medux_video_face_swap_plus"] = "edit/face-swap-plus"

    pages = {}
    for page_list, slug, tool in ROWS:
        mcp = {}
        for c in CLIENTS:
            d = idx[c].get(tool)
            if d is None:
                if slug not in NEW:
                    raise SystemExit(f"no MCP example for {tool} ({slug}) and no NEW spec")
                d = write_new(slug, NEW[slug], c)
            mcp[c] = f"examples/{c}/{d}"
        api = apis.get(slug)
        if api is None:
            raise SystemExit(f"no API example for {slug}")
        for pg in page_list:
            pages[pg] = {"tool": tool, "api": api, "claude": mcp["claude"], "codex": mcp["codex"]}
    json.dump({"pages": pages, "no_mcp": NO_MCP}, open(f"{ROOT}/docs/workshop-pages.json", "w"), indent=2, sort_keys=True)
    open(f"{ROOT}/docs/workshop-pages.json", "a").write("\n")

    # docs/workshop-pages.md
    gh = "https://github.com/MeduxIO"
    lines = ["# Playground and Workshop pages",
             "",
             "Every Medux Playground and Workshop function page, with its MCP examples and REST API example.",
             "Generated by `scripts/link_workshop_pages.py`; do not edit by hand.",
             "",
             "Pages ending in `/*` stand for a family of generated pages (the voice library and the avatar professions) that share one example.",
             "",
             "| Page | Tool | Claude example | Codex example | API example |",
             "| --- | --- | --- | --- | --- |"]
    for pg in sorted(pages):
        e = pages[pg]
        lines.append(
            f"| [{pg}]({SITE}{pg.replace('/*', '')}) | `{e['tool']}` "
            f"| [Claude](../{e['claude']}/README.md) | [Codex](../{e['codex']}/README.md) "
            f"| [API]({gh}/medux-api-examples/tree/main/{e['api']}) |")
    for pg, title in sorted(NO_MCP.items()):
        lines.append(f"| [{pg}]({SITE}{pg}) | none yet ({title}) | — | — | — |")
    open(f"{ROOT}/docs/workshop-pages.md", "w").write("\n".join(lines) + "\n")

    # Inject the block into each mapped MCP README.
    by_dir = {}
    for pg, e in pages.items():
        for c in CLIENTS:
            by_dir.setdefault(e[c], []).append((pg, e))
    for d, items in by_dir.items():
        readme = f"{ROOT}/{d}/README.md"
        client = d.split("/")[1]
        other = "codex" if client == "claude" else "claude"
        rows = []
        for pg, e in sorted(items):
            kind = "Playground" if pg.startswith("/playground") else "Workshop"
            rows.append(f"| {kind} | [{SITE.split('//')[1]}{pg}]({SITE}{pg.replace('/*', '')}) |")
        first = items[0][1]
        depth = "../" * (d.count("/") + 1)
        api_url = f"{gh}/medux-api-examples/tree/main/{first['api']}"
        other_rel = os.path.relpath(f"{ROOT}/{first[other]}", os.path.dirname(readme))
        block = "\n".join([
            BEGIN, "## Try it on medux.io", "",
            "| Type | Page |", "| --- | --- |", *dict.fromkeys(rows), "",
            f"- REST API example: [{first['api']}]({api_url})",
            f"- {other.capitalize()} example: [{first[other].split('examples/')[1]}]({other_rel}/README.md)",
            f"- All pages: [Playground and Workshop pages]({depth}docs/workshop-pages.md)", END, ""])
        text = open(readme).read()
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?", "", text, flags=re.S)
        m = re.search(r"^## Verification", text, flags=re.M)
        text = (text[:m.start()] + block + "\n" + text[m.start():]) if m else (text.rstrip("\n") + "\n\n" + block)
        open(readme, "w").write(text)

    print(f"pages={len(pages)} injected={len(by_dir)} dirs, new examples={len(NEW)*2}")


if __name__ == "__main__":
    main()
