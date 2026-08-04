#!/usr/bin/env bash
# regen_level2_signals.sh — the ONLY supported way to rebuild the Level-2
# cross-tradition signal stream (wiki/level2_signal_stream.html).
#
# Why this exists: the stream was built ONCE by hand on 2026-06-28 and copied
# into wiki/. Nothing ever rebuilt it. Its newest signal stayed 2026-06-23 while
# the vault kept producing — by 2026-08-04 that was 192 signals across 23 days,
# invisible. Worse, wiki/metabolism reads this file for its "cross-tradition
# signals/day" axis, so the metabolism view drew an honest-looking flat zero for
# six weeks. A frozen artifact and a dead pipeline look identical downstream.
#
# The chain is fully deterministic (Rule 5 — no model passes):
#   extract_signals.py   vault flags/ + master/ index      -> signals.json
#   build_manifest.py    approved cards not yet covered    -> backlog_manifest.json
#   harvest_signals.py   each card's "## Cross-Tradition Signals" section
#                                                          -> signals_grown.json
#   build_prototype.py   inline the data into one HTML     -> level2_signal_stream.html
#
# Everything is built in a temp dir and PROMOTED only after the guards pass, so
# a rejected build never overwrites the accepted one (the stronger form of the
# sociogram wrapper's reject()).
#
# Usage:  bash scripts/regen_level2_signals.sh
set -euo pipefail

# Derived from this script's own location, not hardcoded: a copy running in a
# worktree must rebuild THAT worktree's wiki/, never silently write the primary
# tree. Under launchd the script path is the primary tree, so this resolves the
# same way regen_sociogram.sh's hardcoded path does.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VAULT="$ROOT/wiki"
P="$ROOT/prototypes"
META="$P/level2_build_meta.json"
OUT_WIKI="$VAULT/level2_signal_stream.html"

# How stale the newest signal may get before we say so out loud. This is a WARN,
# not a rejection: a correct rebuild of a quiet upstream is still a correct
# rebuild. The failure this catches is the one that actually happened — nobody
# noticing that new signals stopped arriving.
LAG_WARN_DAYS=${LAG_WARN_DAYS:-21}

WORK="$(mktemp -d -t level2_regen.XXXXXX)"
trap 'rm -rf "$WORK"' EXIT

reject() {  # $1 = message. Nothing has been promoted at this point, by design.
  echo "[level2] ERROR: $1" >&2
  echo "[level2]        NOTHING promoted — $OUT_WIKI still holds the last accepted build." >&2
  exit 1
}

PREV_TOTAL=""
if [ -f "$META" ]; then
  PREV_TOTAL=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("signals",""))' "$META" 2>/dev/null || true)
fi

echo "[level2] extract (findings + cross-program index + April batch files) …"
python3 "$P/extract_signals.py" "$VAULT" "$WORK" | sed 's/^/[level2]   /'

echo "[level2] manifest (approved cards not already carrying signals) …"
python3 "$P/backlog/build_manifest.py" "$VAULT" "$WORK" "$WORK/signals.json" | sed 's/^/[level2]   /'

echo "[level2] harvest (each card's ## Cross-Tradition Signals section) …"
python3 "$P/harvest_signals.py" "$WORK/backlog_manifest.json" "$VAULT" \
        "$WORK/signals.json" "$WORK" > "$WORK/harvest.log" 2>&1 || \
  { sed 's/^/[level2]   /' "$WORK/harvest.log" >&2; reject "harvest_signals.py failed"; }
sed 's/^/[level2]   /' "$WORK/harvest.log"

# GUARD 1 — the harvester's own coverage gate. Every card in the manifest must
# get a qc_trace row; a card silently skipped is a signal silently lost.
grep -q "GATE: PASS" "$WORK/harvest.log" || reject "harvest coverage gate did not PASS"

echo "[level2] build viz …"
python3 "$P/build_prototype.py" "$WORK/signals_grown.json" "$WORK/level2_signal_stream.html" \
  | sed 's/^/[level2]   /'

# GUARDS 2-4 — read the built HTML the way every consumer does (parse the inline
# SIG array), not the way the builder wrote it. This is what catches a build that
# produced a file but not a dataset.
python3 - "$WORK/level2_signal_stream.html" "$WORK/signals_grown.json" "$WORK/meta.json" \
         "${PREV_TOTAL:-}" "$LAG_WARN_DAYS" <<'PY' || reject "built HTML failed its own data checks"
import json, sys, datetime, re
html_p, grown_p, meta_p, prev_s, lag_days = sys.argv[1:6]
html = open(html_p, encoding="utf-8").read()
j = html.index("const SIG = ") + len("const SIG = ")
sig, _ = json.JSONDecoder().raw_decode(html, j)
grown = json.load(open(grown_p))

if not sig:
    sys.exit("SIG array in the built HTML is EMPTY")
if len(sig) != len(grown):
    sys.exit("SIG in HTML has %d records but signals_grown.json has %d" % (len(sig), len(grown)))

prev = int(prev_s) if prev_s.strip().isdigit() else None
if prev is not None and len(sig) < prev * 9 // 10:
    sys.exit("signal count collapsed %d -> %d (>10%% drop)" % (prev, len(sig)))

dates = sorted(d for d in (r.get("date") or "" for r in sig)
               if re.match(r"^\d{4}-\d{2}-\d{2}$", d))
if not dates:
    sys.exit("no record carries a parseable date — the metabolism yield axis would read 0")
newest = dates[-1]
stale = (datetime.date.today() - datetime.date.fromisoformat(newest)).days

json.dump({"signals": len(sig), "pairs": len(set((r["a"], r["b"]) for r in sig)),
           "span_first": dates[0], "span_last": newest, "stale_days": stale,
           "by_source": {s: sum(1 for r in sig if r.get("source") == s)
                         for s in sorted(set(r.get("source", "") for r in sig))}},
          open(meta_p, "w"), indent=1)

print("[level2]   %d signals, %d pairs, %s -> %s"
      % (len(sig), len(set((r["a"], r["b"]) for r in sig)), dates[0], newest))
if stale > int(lag_days):
    # Deliberately not fatal — see LAG_WARN_DAYS above.
    sys.stderr.write("[level2] WARN: newest cross-tradition signal is %d days old (%s). "
                     "Upstream (pattern_detector_findings / cross_program_index / approved "
                     "cards) may have stopped producing.\n" % (stale, newest))
PY

echo "[level2] promote …"
cp "$WORK/level2_signal_stream.html" "$OUT_WIKI"
cp "$WORK/level2_signal_stream.html" "$P/level2_signal_stream.html"
cp "$WORK/signals.json"              "$P/signals.json"
cp "$WORK/signals_grown.json"        "$P/signals_grown.json"
cp "$WORK/backlog_manifest.json"     "$P/backlog/backlog_manifest.json"
cp "$WORK/qc_trace.csv"              "$P/backlog/qc_trace.csv"
# Written LAST so the baseline can never describe a build that did not finish.
cp "$WORK/meta.json" "$META"

echo "[level2] OK — $OUT_WIKI updated. Baseline: $(cat "$META" | tr -d '\n ')"
echo "[level2] wiki/metabolism reads this file; run scripts/metabolism_monitor.py --regen-only to refresh the yield axis."
