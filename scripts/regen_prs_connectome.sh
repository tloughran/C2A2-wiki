#!/usr/bin/env bash
#
# regen_prs_connectome.sh
# Regenerate the Narrative (PRS) Connectome (wiki/prs_3d.html) from the current
# vault PRS triplets, validate it, and write it in place.
#
# IMPORTANT (learned 2026-06-07): scheduled tasks run in a flattened-mount Linux
# sandbox that has NO git credentials and CANNOT modify .git lock files. So this
# script does NO git operations at all — no commit, no push, no worktree. It only
# regenerates + validates + writes the file. Publishing to origin/main is a
# MANUAL step done by Tom on the Mac (see the printed RESULT for the commands).
#
# Usage:  regen_prs_connectome.sh [REPO_ROOT]
#   REPO_ROOT defaults to `git rev-parse --show-toplevel` (read-only; works even
#   when index.lock is present). Pass it explicitly if running outside the repo.
#
# Fail loud: any extract/generate/validate error aborts before the file is
# overwritten (validation runs on a temp copy first).

set -euo pipefail

REPO="${1:-$(git rev-parse --show-toplevel)}"
WIKI="$REPO/wiki"
S="$WIKI/c2a2-prs-3d/scripts"
TPL="$WIKI/c2a2-prs-3d/template_prs_3d.html"
CF="$WIKI/c2a2-prs-3d/prs_pub_years.json"
OUT="$WIKI/prs_3d.html"

count() { grep -oE '"id"[[:space:]]*:[[:space:]]*"[a-z]+-PRS-[0-9]+' "$1" 2>/dev/null | wc -l | tr -d ' '; }

TMPDATA="$(mktemp)"; TMPHTML="$(mktemp)"
trap 'rm -f "$TMPDATA" "$TMPHTML"' EXIT

echo "=== PRS connectome regen — $(date '+%Y-%m-%d %H:%M:%S') ==="
echo "Repo: $REPO"

OLD="$(count "$OUT")"

# Regenerate + validate on a temp copy first (carryforward preserves curated pub_years)
python3 "$S/extract_prs_data.py" "$WIKI" --carryforward "$CF" --out "$TMPDATA"
python3 "$S/generate_prs_3d.py" "$TMPDATA" "$TPL" "$TMPHTML"
python3 "$S/validate_prs_3d.py" "$TMPHTML" --source-data "$TMPDATA"   # non-zero exit aborts (set -e)
NEW="$(count "$TMPHTML")"

# Only the file write — no git
cp "$TMPHTML" "$OUT"

cat <<EOF
RESULT: REGENERATED in place: ${OLD} -> ${NEW} triplets, validated PASS.
NOT pushed (the task sandbox has no git credentials). To publish to the live site,
run on the Mac:
  cd "$REPO"
  rm -f .git/index.lock .git/refs/heads/main.lock 2>/dev/null
  git checkout main && git add wiki/prs_3d.html \\
    && git commit -m "Regen PRS connectome: ${OLD} -> ${NEW} triplets (validated)" \\
    && git push origin main \\
    && git checkout -
EOF
