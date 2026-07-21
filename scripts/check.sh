#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

if rg -n --hidden --glob '!.git/**' --glob '!scripts/check.sh' '(sk-[A-Za-z0-9_-]{16,}|MEDUX_API_KEY\s*=\s*[^<[:space:]][^[:space:]]*)'; then
  echo "Potential credential found. Remove it before committing." >&2
  exit 1
fi

missing=0
while IFS= read -r readme; do
  if [[ "$readme" == examples/* ]] && ! rg -q '^## Prompt$' "$readme"; then
    echo "$readme: missing Prompt section" >&2
    missing=1
  fi
  if [[ "$readme" == examples/* ]] && ! rg -q 'https://medux\.io/tutorials/' "$readme"; then
    echo "$readme: missing Medux tutorial link" >&2
    missing=1
  fi
  if [[ "$readme" == examples/* ]] && [[ "$readme" != examples/codex/* ]] && [[ "$readme" != examples/claude/* ]]; then
    echo "$readme: examples must be scoped to codex or claude" >&2
    missing=1
  fi
done < <(find . -name README.md -print | sed 's#^./##' | sort)

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

python3 - <<'PY'
import json
import re
from collections import Counter
from pathlib import Path

repo = Path.cwd()
manifest_path = repo / "examples/manifest.json"
if not manifest_path.exists():
    raise SystemExit("examples/manifest.json is missing")
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
records = manifest.get("records", [])
if len(records) != 138 or manifest.get("tutorial_count") != 138:
    raise SystemExit(f"expected 138 mapped tutorials, found {len(records)}")
clients = Counter(record["client"] for record in records)
if clients != {"codex": 69, "claude": 69}:
    raise SystemExit(f"unexpected client coverage: {dict(clients)}")
tutorials = [record["tutorial_file"] for record in records]
paths = [record["example_path"] for record in records]
if len(tutorials) != len(set(tutorials)):
    raise SystemExit("duplicate tutorial mapping in manifest")
if len(paths) != len(set(paths)):
    raise SystemExit("multiple tutorials map to the same example path")
for record in records:
    path = repo / record["example_path"]
    if not path.exists():
        raise SystemExit(f"mapped example is missing: {path}")
    body = path.read_text(encoding="utf-8")
    if record["tutorial_url"] not in body:
        raise SystemExit(f"mapped tutorial link is missing from {path}")
    if not record.get("tools"):
        raise SystemExit(f"tool mapping is missing for {record['tutorial_file']}")
for markdown in repo.rglob("*.md"):
    body = markdown.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", body):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        local_target = target.split("#", 1)[0]
        if local_target and not (markdown.parent / local_target).exists():
            raise SystemExit(f"broken local Markdown link in {markdown}: {target}")
print("Manifest covers 138 tutorials: 69 Codex and 69 Claude.")
PY

echo "Repository checks passed."
