#!/usr/bin/env bash
# regen_sociogram.sh — the ONLY supported way to regenerate wiki_narration.html.
#
# Why this exists: the Sociogram graph must include the Summa companion nodes,
# which only appear when extract_vault_data.py is run WITH `--summa`. That flag
# is easy to forget — and forgetting it silently drops every Summa node from the
# graph (happened twice on 2026-05-19: the original Q.2-8 outage and again during
# the mobile-readability pass). This wrapper hardcodes the correct invocation so
# the flag can never be dropped. NEVER call generate_visualization.py directly.
#
# Usage:  bash wiki/c2a2-wiki-narration/regen_sociogram.sh
set -euo pipefail

WIKI="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki"
SUMMA="$HOME/Documents/Claude/Projects/Summa 2026 in a Year/vault"
S="$WIKI/c2a2-wiki-narration/scripts"
VDATA="$(mktemp -t vault_data.XXXXXX).json"
OUT="$WIKI/wiki_narration.html"

echo "[regen] extract (with --summa) …"
python3 "$S/extract_vault_data.py" "$WIKI" --summa "$SUMMA" > "$VDATA"

echo "[regen] generate …"
python3 "$S/generate_visualization.py" "$VDATA" "$OUT"

echo "[regen] validate …"
python3 "$S/validate_html.py" "$OUT" --source-data "$VDATA" || true

# Guard: refuse to leave a Summa-less Sociogram in place.
N=$(grep -c "Contemporary commentary on Summa Question" "$OUT" || true)
if [ "$N" -eq 0 ]; then
  echo "[regen] ERROR: 0 Summa nodes in output — extract may have run without --summa or the Summa index is empty. NOT trusting this build." >&2
  exit 1
fi
echo "[regen] OK — $N Summa commentary nodes present in $OUT"
rm -f "$VDATA"
