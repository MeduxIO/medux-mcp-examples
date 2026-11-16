#!/usr/bin/env python3
"""Align generated examples with the tools the Medux MCP server really exposes.

The bulk examples are generated from the published tutorials, some of which name
REST-style operations as MCP tools. The live server only exposes the tools listed
in docs/tools.md. This script rewrites the affected examples and the manifest.
Run it after scripts/generate_examples.py. It is idempotent.
"""
import json
import re
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
manifest_path = repo / "examples/manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

# Tutorial tool name -> real MCP tool(s).
REMAP = {
    "medux_get_task": ["medux_task_query"],
    "medux_get_avatar_task": ["medux_task_query"],
    "medux_get_voice_task": ["medux_task_query"],
    "medux_get_creation_task": ["medux_task_query"],
    "medux_get_process_task": ["medux_task_query"],
    "medux_sync_task": ["medux_task_query"],
    "medux_create_upload_url": ["medux_file_create_upload_url"],
    "medux_video_remove_watermark": ["medux_watermark_removal", "medux_watermark_removal_by_prompt"],
}
# Tutorial tool name -> no MCP equivalent (REST API only).
REST_ONLY = {
    "medux_create_asset", "medux_list_assets", "medux_list_results", "medux_list_tasks",
    "medux_list_voices", "medux_list_avatars", "medux_edit_voice_parameters",
    "medux_create_video_by_project",
}

TASK_FIELDS = [{"name": "task_id", "type": "string", "requirement": "Required",
                "purpose": "Public task id returned by a Medux tool call."}]
UPLOAD_FIELDS = [
    {"name": "media_type", "type": "string", "requirement": "Required",
     "purpose": "One of VIDEO, AUDIO, IMAGE or DOCUMENT."},
    {"name": "extension", "type": "string", "requirement": "Required",
     "purpose": "File extension without the dot, for example mp4."},
]
WATERMARK_FIELDS = [
    {"name": "input_file_id", "type": "string", "requirement": "Required", "purpose": "Input video file_id."},
    {"name": "regions", "type": "array", "requirement": "Required (medux_watermark_removal)",
     "purpose": "Regions to remove, for example [[x, y, width, height]]."},
    {"name": "prompt_text", "type": "string", "requirement": "Required (medux_watermark_removal_by_prompt)",
     "purpose": "Text description of the watermark to remove."},
]
PROMPTS = {
    "task": "Use Medux to check the task {task id} with medux_task_query and report its status. If it has succeeded, give me the output URL.",
    "upload": "Upload {local file} to Medux with medux_file_create_upload_url, PUT the file to the returned URL, and tell me the file_id. Do not start any task.",
    "watermark": "Remove the watermark from the uploaded video {file id}. If the watermark area is known, use medux_watermark_removal with regions [[x, y, width, height]]; otherwise use medux_watermark_removal_by_prompt with a short description of the watermark.",
}
NOTICE = ("> [!NOTE]\n> **No MCP tool.** This operation exists in the Medux REST API but is not exposed over MCP. "
          "See [MCP tool reference]({tools_rel}) for the tools that are, and the [REST API]({api}) for this operation.\n")


def fields_md(fields):
    return "\n".join(f"- `{f['name']}` ({f['requirement'].lower()}): {f['purpose']}" for f in fields)


def rewrite(record):
    tools = record["tools"]
    first = tools[0]
    path = repo / record["example_path"]
    body = path.read_text(encoding="utf-8")
    depth = len(Path(record["example_path"]).parts) - 1
    tools_rel = "../" * depth + "docs/tools.md"

    if first in REMAP:
        new_tools = REMAP[first]
        kind = "task" if new_tools == ["medux_task_query"] else "upload" if "upload" in new_tools[0] else "watermark"
        fields = {"task": TASK_FIELDS, "upload": UPLOAD_FIELDS, "watermark": WATERMARK_FIELDS}[kind]
        record["tools"], record["fields"], record["prompt"] = new_tools, fields, PROMPTS[kind]
        body = re.sub(r"## Expected Medux tools\n\n(?:- .*\n)+",
                      "## Expected Medux tools\n\n" + "".join(f"- `{t}`\n" for t in new_tools), body)
        body = re.sub(r"## Prompt\n\n```text\n.*?\n```", f"## Prompt\n\n```text\n{PROMPTS[kind]}\n```", body, flags=re.S)
        body = re.sub(r"## Review before approval\n\n(?:- .*\n)+",
                      "## Review before approval\n\n" + fields_md(fields) + "\n", body)
    elif first in REST_ONLY:
        notice = NOTICE.format(tools_rel=tools_rel, api=record["api_url"])
        record["tools"] = ["(none: REST API only)"]
        record["mcp_available"] = False
        record["prompt"] = "This operation is not available over MCP. Use the REST API instead."
        body = re.sub(r"## Expected Medux tools\n\n(?:- .*\n)+", "## Expected Medux tools\n\nNone.\n\n" + notice, body)
        body = re.sub(r"## Prompt\n\n```text\n.*?\n```",
                      "## Prompt\n\n```text\nThis operation is not available over MCP. Use the REST API instead.\n```", body, flags=re.S)
        body = re.sub(r"## Review before approval\n\n(?:- .*\n)+\n?", "", body)
    else:
        return
    path.write_text(body, encoding="utf-8")


for rec in manifest["records"]:
    rewrite(rec)
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# INDEX rows: swap the expected-tool cell using the manifest.
for client in ("codex", "claude"):
    index = repo / "examples" / client / "INDEX.md"
    text = index.read_text(encoding="utf-8")
    for rec in manifest["records"]:
        if rec["client"] != client:
            continue
        pattern = re.compile(r"(\]\(" + re.escape(rec["example_path"].split(f"examples/{client}/")[1]) + r"\) \| )([^|]*)( \|)")
        cell = "None (REST only)" if rec.get("mcp_available") is False else ", ".join(f"`{t}`" for t in rec["tools"])
        text = pattern.sub(lambda m: m.group(1) + cell + m.group(3), text)
    index.write_text(text, encoding="utf-8")
print("Applied tool corrections.")
