#!/usr/bin/env bash
# test_regen_level2.sh — drive regen_level2_signals.sh's FAILURE paths.
#
# A guard nobody has watched fail is not a guard. Each case below makes the
# wrapper reject, then asserts the thing that actually matters: that the
# previously accepted wiki/level2_signal_stream.html and level2_build_meta.json
# are byte-identical afterwards. Temp-then-promote is only worth anything if a
# rejected build really leaves the accepted one alone.
#
# Usage:  bash scripts/test_regen_level2.sh     (about 30s; runs the chain 3x)
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REGEN="$ROOT/scripts/regen_level2_signals.sh"
OUT="$ROOT/wiki/level2_signal_stream.html"
META="$ROOT/prototypes/level2_build_meta.json"

PASS=0; FAIL=0
ok()   { echo "  PASS  $1"; PASS=$((PASS+1)); }
bad()  { echo "  FAIL  $1"; FAIL=$((FAIL+1)); }
check(){ if [ "$2" = "$3" ]; then ok "$1"; else bad "$1 (want '$3', got '$2')"; fi; }

SAVE="$(mktemp -d -t level2_test.XXXXXX)"
[ -f "$OUT" ]  && cp "$OUT"  "$SAVE/out.html"
[ -f "$META" ] && cp "$META" "$SAVE/meta.json"
restore() {
  [ -f "$SAVE/out.html" ]  && cp "$SAVE/out.html"  "$OUT"
  [ -f "$SAVE/meta.json" ] && cp "$SAVE/meta.json" "$META"
  rm -rf "$SAVE"
}
trap restore EXIT

echo "=== 0. baseline: a good build must pass ==="
bash "$REGEN" >"$SAVE/good.log" 2>&1; rc=$?
check "good build exits 0" "$rc" "0"
grep -q "OK —" "$SAVE/good.log" && ok "good build promoted" || bad "good build did not promote"
cp "$OUT" "$SAVE/accepted.html"; cp "$META" "$SAVE/accepted.meta"

echo "=== 1. collapse guard: baseline claims far more signals than exist ==="
python3 - "$META" <<'PY'
import json,sys
p=sys.argv[1]; d=json.load(open(p)); d["signals"]=d["signals"]*10
json.dump(d,open(p,"w"),indent=1)
PY
bash "$REGEN" >"$SAVE/collapse.log" 2>&1; rc=$?
check "collapse build exits non-zero" "$([ $rc -ne 0 ] && echo yes || echo no)" "yes"
grep -q "signal count collapsed" "$SAVE/collapse.log" && ok "message names the collapse" \
  || bad "message does not name the collapse"
grep -q "NOTHING promoted" "$SAVE/collapse.log" && ok "message says nothing was promoted" \
  || bad "message omits the not-promoted line"
cmp -s "$OUT" "$SAVE/accepted.html" && ok "accepted HTML untouched by the rejected build" \
  || bad "REJECTED BUILD OVERWROTE THE ACCEPTED HTML"
cp "$SAVE/accepted.meta" "$META"

echo "=== 2. empty-dataset guard: a vault with no signal sources ==="
EMPTY="$(mktemp -d -t level2_emptyvault.XXXXXX)"
mkdir -p "$EMPTY/flags" "$EMPTY/master" "$EMPTY/inbox/proposals/approved"
: > "$EMPTY/flags/pattern_detector_findings.md"
: > "$EMPTY/master/cross_program_index.md"
: > "$EMPTY/flags/cross_signals_2026-04-16_batch1.md"
: > "$EMPTY/flags/cross_signals_2026-04-16_batch2.md"
# harvest_signals.py indexes qc_rows[0] to get its CSV header, so an empty
# manifest is its own distinct failure — either way the run must not promote.
LEVEL2_VAULT="$EMPTY" bash -c '
  set -e
  sed "s#VAULT=\"\$ROOT/wiki\"#VAULT=\"$LEVEL2_VAULT\"#" '"$REGEN"' > '"$SAVE"'/regen_empty.sh
  bash '"$SAVE"'/regen_empty.sh
' >"$SAVE/empty.log" 2>&1; rc=$?
check "empty-vault build exits non-zero" "$([ $rc -ne 0 ] && echo yes || echo no)" "yes"
cmp -s "$OUT" "$SAVE/accepted.html" && ok "accepted HTML untouched by the empty-vault build" \
  || bad "EMPTY-VAULT BUILD OVERWROTE THE ACCEPTED HTML"
rm -rf "$EMPTY"

echo "=== 3. staleness WARN fires but does NOT block a correct rebuild ==="
LAG_WARN_DAYS=0 bash "$REGEN" >"$SAVE/stale.log" 2>&1; rc=$?
check "stale-threshold build still exits 0" "$rc" "0"
grep -q "WARN: newest cross-tradition signal is" "$SAVE/stale.log" && ok "staleness WARN printed" \
  || bad "staleness WARN did not print"
grep -q "OK —" "$SAVE/stale.log" && ok "correct rebuild still promoted despite WARN" \
  || bad "WARN wrongly blocked promotion"

echo
echo "=== $PASS passed, $FAIL failed ==="
[ "$FAIL" -eq 0 ]
