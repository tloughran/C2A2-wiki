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


# --- node dates come from git, not from st_mtime -------------------------------
#
# The point of build_git_date_map() is that a file whose CONTENT did not change
# keeps its date. mtime cannot do that: git does not record it, so a checkout, the
# 21:00 Summa vault sync and the weekly janitor all stamp "now" on files nobody
# edited, and 1122 node dates moved for that reason alone. So the load-bearing
# assertion is not "the date is right" but "touching the file does not move it".

echo ""
echo "date source, in a throwaway git repo:"

GITVAULT="$(mktemp -d -t determ_git.XXXXXX)"
OUT_G1="$(mktemp -t determ_g1.XXXXXX)"
OUT_G2="$(mktemp -t determ_g2.XXXXXX)"
trap 'cleanup; rm -rf "$GITVAULT" "$OUT_G1" "$OUT_G2"' EXIT

(
  cd "$GITVAULT" || exit 1
  git init -q .
  git config user.email t@example.com
  git config user.name t
  mkdir -p architecture
  printf '# tracked\n\nSee [[somewhere]].\n' > architecture/tracked.md
  git add architecture/tracked.md
  GIT_AUTHOR_DATE="2026-03-14T12:00:00" GIT_COMMITTER_DATE="2026-03-14T12:00:00" \
    git commit -qm "add tracked"
  printf '# untracked\n\nSee [[elsewhere]].\n' > architecture/untracked.md
) >/dev/null 2>&1

read_date() {  # $1 = extraction json, $2 = filepath
  python3 - "$1" "$2" <<'PY'
import json, sys
data = json.load(open(sys.argv[1]))
for f in data["files"]:
    if f["filepath"] == sys.argv[2]:
        print(f["date"]); break
else:
    print("MISSING")
PY
}

python3 "$EXTRACT" "$GITVAULT" > "$OUT_G1" 2>/dev/null
D_TRACKED=$(read_date "$OUT_G1" "architecture/tracked.md")
D_UNTRACKED=$(read_date "$OUT_G1" "architecture/untracked.md")
TODAY=$(date +%Y-%m-%d)

[ "$D_TRACKED" = "2026-03-14" ] \
  && ok "tracked file takes its commit date, not its mtime" \
  || bad "tracked file takes its commit date, not its mtime (got $D_TRACKED)"

# The fallback still has to work, or every untracked file would go undated.
[ "$D_UNTRACKED" = "$TODAY" ] \
  && ok "untracked file falls back to mtime" \
  || bad "untracked file falls back to mtime (got $D_UNTRACKED, expected $TODAY)"

# Drive the exact thing the nightly sync does: rewrite the mtime, leave the bytes.
touch "$GITVAULT/architecture/tracked.md"
python3 "$EXTRACT" "$GITVAULT" > "$OUT_G2" 2>/dev/null
D_AFTER=$(read_date "$OUT_G2" "architecture/tracked.md")

[ "$D_AFTER" = "2026-03-14" ] \
  && ok "touching a tracked file does not move its date" \
  || bad "touching a tracked file does not move its date (got $D_AFTER)"

# A vault outside any git repo must still extract rather than crash or go undated.
python3 "$EXTRACT" "$VAULT" > /dev/null 2>&1 \
  && ok "vault outside a git repo still extracts" \
  || bad "vault outside a git repo still extracts"

echo ""
echo "$PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
