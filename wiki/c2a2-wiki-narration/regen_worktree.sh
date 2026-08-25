#!/usr/bin/env bash
# regen_worktree.sh — regen THIS worktree's sociogram, never the main tree's.
#
# The shipped regen_sociogram.sh hardcodes an absolute WIKI path, so running it
# from a worktree silently rewrites MAIN's wiki_narration.html. This one derives
# WIKI from its own location instead. Everything else — the --summa flag, the
# agent layer, all four guards — is preserved verbatim from the wrapper.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WIKI="$(cd "$HERE/.." && pwd)"

# Summa vault lives outside the repo; find it wherever this is running.
SUMMA=""
for CAND in "$HOME/Documents/Claude/Projects/Summa 2026 in a Year/vault" \
            "$HOME/mnt/Summa 2026 in a Year/vault"; do
  [ -d "$CAND" ] && SUMMA="$CAND" && break
done
[ -n "$SUMMA" ] || { echo "[regen-wt] ERROR: Summa vault not found" >&2; exit 1; }

AGENTS="$WIKI/agents/openstory/agent_node_edges.json"
S="$WIKI/c2a2-wiki-narration/scripts"
OUT="$WIKI/wiki_narration.html"
META="$S/build_meta.json"
VDATA="$(mktemp -t vault_data.XXXXXX).json"

echo "[regen-wt] WIKI  = $WIKI"
echo "[regen-wt] SUMMA = $SUMMA"
echo "[regen-wt] OUT   = $OUT"

PREV_NODES=""; META_BACKUP=""
if [ -f "$META" ]; then
  PREV_NODES=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("nodes",""))' "$META" 2>/dev/null || true)
  META_BACKUP="$(mktemp -t build_meta_prev.XXXXXX)"; cp "$META" "$META_BACKUP"
fi

echo "[regen-wt] extract (with --summa) ..."
python3 "$S/extract_vault_data.py" "$WIKI" --summa "$SUMMA" > "$VDATA"

echo "[regen-wt] generate (with agent layer) ..."
if [ -f "$AGENTS" ]; then
  python3 "$S/generate_visualization.py" "$VDATA" "$OUT" "$AGENTS"
else
  echo "[regen-wt] WARNING: $AGENTS missing — building WITHOUT the agent layer" >&2
  python3 "$S/generate_visualization.py" "$VDATA" "$OUT"
fi

echo "[regen-wt] validate ..."
python3 "$S/validate_html.py" "$OUT" --source-data "$VDATA" || true

NSUMMA=$(grep -o "Contemporary commentary on Summa Question" "$OUT" | wc -l | tr -d ' ')
[ "$NSUMMA" -eq 0 ] && { echo "[regen-wt] ERROR: 0 Summa nodes — NOT trusting this build." >&2; exit 1; }
NAGENT=$(grep -o '"group": *"agent-activity"' "$OUT" | wc -l | tr -d ' ')
if [ -f "$AGENTS" ] && [ "$NAGENT" -eq 0 ]; then
  echo "[regen-wt] ERROR: agent file exists but 0 agent-activity nodes. NOT trusting." >&2; exit 1
fi
if [ -f "$META" ] && [ -n "$PREV_NODES" ]; then
  case "$PREV_NODES" in ''|*[!0-9]*) : ;; *)
    NEW_NODES=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("nodes",""))' "$META")
    if [ "$NEW_NODES" -lt $(( PREV_NODES * 3 / 4 )) ]; then
      [ -n "$META_BACKUP" ] && cp "$META_BACKUP" "$META"
      echo "[regen-wt] ERROR: node count collapsed $PREV_NODES -> $NEW_NODES" >&2; exit 1
    fi
    echo "[regen-wt] node delta OK ($PREV_NODES -> $NEW_NODES)" ;;
  esac
fi

# The whole point of this worktree: confirm the probe survived into the build.
grep -q "END LIFT PROBE" "$OUT" && echo "[regen-wt] LiftProbe present in output" \
                                || { echo "[regen-wt] ERROR: probe missing from output" >&2; exit 1; }

echo "[regen-wt] OK — $NSUMMA Summa nodes, $NAGENT agent-activity nodes"
echo "[regen-wt] open: $OUT"
rm -f "$VDATA"
