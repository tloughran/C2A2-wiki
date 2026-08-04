#!/usr/bin/env bash
# test_extract_determinism.sh — the extract stage must be byte-reproducible.
#
# Run:  bash wiki/c2a2-wiki-narration/test_extract_determinism.sh
#
# Why: wiki_narration.html is one ~40MB blob, so ANY byte that moves rewrites the
# whole thing in git. Until 2026-08-04 extract_wikilinks() returned
# `list(set(...))`, and iteration order of a set of strings is randomised per
# process by PYTHONHASHSEED. Two extractions seconds apart, same inputs, differed
# in 1499 leaves (1262 in files[].wikilinks plus the 237 wikilink_edges derived
# from them) -- so every single regen committed 40MB whether or not one character
# of content had changed.
#
# Two default-seed runs are a weak test: they only differ because the seeds
# happened to differ. This drives the condition deliberately instead, running the
# same input under two fixed, different PYTHONHASHSEEDs. If any set or dict
# iteration order reaches the output, those two runs disagree. Same idea as
# test_regen_guard.sh: force the failure, do not wait for it.
#
# Cheap -- a synthetic 6-file vault, no full regen, about a second.

set -uo pipefail

AGD="$(cd "$(dirname "$0")" && pwd)"
EXTRACT="$AGD/scripts/extract_vault_data.py"
VAULT="$(mktemp -d -t determ_vault.XXXXXX)"
OUT_A="$(mktemp -t determ_a.XXXXXX)"
OUT_B="$(mktemp -t determ_b.XXXXXX)"

cleanup() { rm -rf "$VAULT" "$OUT_A" "$OUT_B"; }
trap cleanup EXIT

PASS=0; FAIL=0
ok()  { PASS=$((PASS+1)); echo "  ok   $1"; }
bad() { FAIL=$((FAIL+1)); echo "  FAIL $1"; }

[ -f "$EXTRACT" ] || { echo "no extract_vault_data.py at $EXTRACT"; exit 2; }

# Twelve wikilinks per file. If order were still random, two runs would agree
# only by 1-in-12! chance per file, so a pass here is not luck.
mkdir -p "$VAULT/architecture" "$VAULT/agents"
i=0
for name in alpha beta gamma delta epsilon zeta; do
  i=$((i+1))
  dir="architecture"; [ $((i % 2)) -eq 0 ] && dir="agents"
  {
    echo "# ${name}"
    echo ""
    echo "Refs FINDING-1 CROSS-2 DECISION-3."
    for link in mu nu xi omicron pi rho sigma tau upsilon phi chi psi; do
      echo "See [[${link}_${name}]] for more."
    done
  } > "$VAULT/$dir/${name}.md"
done

echo "extract stage, two fixed and different hash seeds:"

PYTHONHASHSEED=0     python3 "$EXTRACT" "$VAULT" > "$OUT_A" 2>/dev/null
RC_A=$?
PYTHONHASHSEED=12345 python3 "$EXTRACT" "$VAULT" > "$OUT_B" 2>/dev/null
RC_B=$?

[ "$RC_A" -eq 0 ] && ok "extract exits 0 under PYTHONHASHSEED=0" \
                  || bad "extract exits 0 under PYTHONHASHSEED=0 (got $RC_A)"
[ "$RC_B" -eq 0 ] && ok "extract exits 0 under PYTHONHASHSEED=12345" \
                  || bad "extract exits 0 under PYTHONHASHSEED=12345 (got $RC_B)"

# extraction_date is datetime.now() and is expected to move. It never reaches the
# HTML -- generate_visualization.py reads only total_files and date_range from
# metadata -- so it is excluded here rather than frozen.
python3 - "$OUT_A" "$OUT_B" <<'PY'
import json, sys
a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
a["metadata"].pop("extraction_date", None); b["metadata"].pop("extraction_date", None)
sys.exit(0 if a == b else 1)
PY
if [ $? -eq 0 ]; then
  ok "two hash seeds produce identical extraction (order does not leak)"
else
  bad "two hash seeds produce identical extraction (order does not leak)"
fi

# The specific field that carried the bug, asserted directly so a regression names
# itself rather than showing up as an opaque whole-document mismatch.
python3 - "$OUT_A" <<'PY'
import json, sys
data = json.load(open(sys.argv[1]))
bad = [f["filepath"] for f in data["files"]
       if f["wikilinks"] != sorted(f["wikilinks"])]
if bad:
    print("    unsorted wikilinks in: " + ", ".join(bad[:5]))
sys.exit(1 if bad else 0)
PY
if [ $? -eq 0 ]; then
  ok "files[].wikilinks is sorted"
else
  bad "files[].wikilinks is sorted"
fi

echo ""
echo "$PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
