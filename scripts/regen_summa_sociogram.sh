#!/usr/bin/env bash
# regen_summa_sociogram.sh — regenerate + validate the C2A2 Sociogram
# (wiki/wiki_narration.html) with current Summa transcript+synthesis nodes.
# Pattern mirrors regen_prs_connectome.sh: reindex -> extract(--summa) ->
# generate -> validate -> overwrite ONLY on PASS. No git (publish is manual).
# Usage: regen_summa_sociogram.sh <RCK_REPO_ROOT> <SUMMA_VAULT_ROOT>
set -uo pipefail

RCK="${1:?need RCK repo root}"
SUMMA="${2:?need Summa vault root}"
WIKI="$RCK/wiki"
TARGET="$WIKI/wiki_narration.html"

# Locate the extractor (its subdir has moved before — don't hardcode).
EXTRACT="$(find "$RCK" -name extract_vault_data.py -not -path '*/.claude/worktrees/*' -print 2>/dev/null | head -1)"
[ -n "$EXTRACT" ] || { echo "FAIL: extract_vault_data.py not found under $RCK"; exit 1; }
SCRIPTS="$(dirname "$EXTRACT")"
echo "scripts dir: $SCRIPTS"

# 1) Reindex the Summa article index (summa_index.json + index_summary.md) in place.
if [ -f "$SUMMA/refs/build_index.py" ]; then
  echo "reindexing Summa article index ..."
  python3 "$SUMMA/refs/build_index.py" --vault "$SUMMA" || { echo "FAIL: build_index"; exit 1; }
else
  echo "WARN: $SUMMA/refs/build_index.py not found — skipping article reindex"
fi

# Count current Summa synthesis nodes in the live file (for the delta).
OLD=$(grep -o "Contemporary commentary on Summa Question" "$TARGET" 2>/dev/null | wc -l | tr -d ' ')

# 2) Extract WITH --summa (mandatory: without it the Sociogram emits 0 Summa nodes).
echo "extracting (--summa) ..."
python3 "$SCRIPTS/extract_vault_data.py" "$WIKI" --summa "$SUMMA" > /tmp/summa_vault_data.json \
  || { echo "FAIL: extract"; exit 1; }

# 3) Generate to a TEMP file (never clobber the live file before validation).
echo "generating ..."
python3 "$SCRIPTS/generate_visualization.py" /tmp/summa_vault_data.json /tmp/wiki_narration.new.html \
  || { echo "FAIL: generate"; exit 1; }

# 4) Validate.
echo "validating ..."
python3 "$SCRIPTS/validate_html.py" /tmp/wiki_narration.new.html --source-data /tmp/summa_vault_data.json \
  | tee /tmp/summa_sociogram_validate.log
grep -q "PASS" /tmp/summa_sociogram_validate.log \
  || { echo "FAIL: validation did not PASS — live file untouched"; exit 1; }

# 5) Guard against a forgotten --summa (would yield 0 Summa nodes).
NEW=$(grep -o "Contemporary commentary on Summa Question" /tmp/wiki_narration.new.html | wc -l | tr -d ' ')
[ "${NEW:-0}" -gt 0 ] \
  || { echo "FAIL: 0 Summa nodes in regenerated file (SUMMA=$SUMMA) — live file untouched"; exit 1; }

# 6) Promote.
mv /tmp/wiki_narration.new.html "$TARGET"
echo "RESULT: REGENERATED  Summa synthesis nodes ${OLD:-0} -> ${NEW}   (file: $TARGET)"
