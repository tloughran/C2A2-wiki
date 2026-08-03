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
AGENTS="$WIKI/agents/openstory/agent_node_edges.json"
S="$WIKI/c2a2-wiki-narration/scripts"
VDATA="$(mktemp -t vault_data.XXXXXX).json"
OUT="$WIKI/wiki_narration.html"

META="$S/build_meta.json"
# Read the PREVIOUS build's numbers before the generator overwrites them. The
# delta guard below is the whole point: on 2026-08-03 a namespace rename during
# the Summa dedup orphaned 1162 of 3084 agent-activity substrate edges, and the
# only signal was a "skipped N" line on stdout that a human happened to read.
# Under cron that ships silently, and the graph then renders a falsehood --
# "these agents never touched Summa content" -- with every validator green.
PREV_SKIPPED=""
PREV_NODES=""
META_BACKUP=""
if [ -f "$META" ]; then
  PREV_SKIPPED=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("substrate_skipped",""))' "$META" 2>/dev/null || true)
  PREV_NODES=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("nodes",""))' "$META" 2>/dev/null || true)
  # Keep the last GOOD baseline. The generator rewrites build_meta.json before
  # the guards below run, so without this a rejected build becomes the baseline
  # and a re-run of the same broken code would compare 1164 against 1164 and
  # pass. The baseline must only ever advance on a build we accepted.
  META_BACKUP="$(mktemp -t build_meta_prev.XXXXXX)"
  cp "$META" "$META_BACKUP"
fi

reject() {  # $1 = message; restores the last good baseline, then fails
  echo "[regen] ERROR: $1" >&2
  if [ -n "$META_BACKUP" ] && [ -f "$META_BACKUP" ]; then
    cp "$META_BACKUP" "$META"
    echo "[regen]        build_meta.json restored to the last accepted build." >&2
  fi
  echo "[regen]        NOT trusting this build — $OUT is left on disk but must not be published." >&2
  exit 1
}

echo "[regen] extract (with --summa) …"
python3 "$S/extract_vault_data.py" "$WIKI" --summa "$SUMMA" > "$VDATA"

echo "[regen] generate (with agent layer) …"
if [ -f "$AGENTS" ]; then
  python3 "$S/generate_visualization.py" "$VDATA" "$OUT" "$AGENTS"
else
  echo "[regen] WARNING: $AGENTS missing — building WITHOUT the agent-activity layer" >&2
  python3 "$S/generate_visualization.py" "$VDATA" "$OUT"
fi

echo "[regen] validate …"
python3 "$S/validate_html.py" "$OUT" --source-data "$VDATA" || true

# Guards: refuse to leave a Summa-less (or unexpectedly agent-less) Sociogram
# in place. NB: grep -o|wc -l counts matches, not lines — the artifact's JSON
# is a single line, so `grep -c` would always report 1.
NSUMMA=$(grep -o "Contemporary commentary on Summa Question" "$OUT" | wc -l)
if [ "$NSUMMA" -eq 0 ]; then
  echo "[regen] ERROR: 0 Summa nodes in output — extract may have run without --summa or the Summa index is empty. NOT trusting this build." >&2
  exit 1
fi
NAGENT=$(grep -o '"group": *"agent-activity"' "$OUT" | wc -l)
if [ -f "$AGENTS" ] && [ "$NAGENT" -eq 0 ]; then
  echo "[regen] ERROR: agent telemetry file exists but 0 agent-activity nodes in output. NOT trusting this build." >&2
  exit 1
fi
# DELTA GUARDS against the previous build's build_meta.json. Zero-guards above
# catch a layer vanishing entirely; these catch it being quietly gutted, which
# is the failure that actually happened. Tolerance is deliberately loose (+20
# skips, 25% of nodes): ordinary drift is a handful, a regression is an order
# of magnitude, and a guard that cries wolf gets disabled.
if [ -f "$META" ]; then
  NEW_SKIPPED=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("substrate_skipped",""))' "$META")
  NEW_NODES=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("nodes",""))' "$META")
  case "$PREV_SKIPPED" in
    ''|*[!0-9]*) echo "[regen] no previous substrate_skipped to compare (first build with build_meta.json)" ;;
    *)
      if [ "$NEW_SKIPPED" -gt $(( PREV_SKIPPED + 20 )) ]; then
        echo "[regen]        Edges are dropped for missing wiki targets. Usually a node-id" >&2
        echo "[regen]        namespace change (e.g. vault/ -> summa/) that _resolve_target()" >&2
        echo "[regen]        in generate_visualization.py has not been taught." >&2
        reject "agent substrate edges skipped jumped $PREV_SKIPPED -> $NEW_SKIPPED"
      fi
      echo "[regen] substrate skip delta OK ($PREV_SKIPPED -> $NEW_SKIPPED)"
      ;;
  esac
  case "$PREV_NODES" in
    ''|*[!0-9]*) : ;;
    *)
      if [ "$NEW_NODES" -lt $(( PREV_NODES * 3 / 4 )) ]; then
        reject "node count collapsed $PREV_NODES -> $NEW_NODES (>25% drop)"
      fi
      ;;
  esac
fi

echo "[regen] OK — $NSUMMA Summa commentary nodes, $NAGENT agent-activity nodes in $OUT"
rm -f "$VDATA"
