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

echo "Repository checks passed."
