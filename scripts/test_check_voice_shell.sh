#!/bin/bash
# test_check_voice_shell.sh -- drives check_voice_shell.sh through its verdict paths
# with a STUB harness in a throwaway fixture repo. Every path here is a failure
# path of the real job: a RED suite, a suite that dies before its summary, and
# the recovery (GREEN clears the marker). Also the gate: no-op when nothing is
# newer than the last verdict, and --dry-run writing nothing.
#
#   bash scripts/test_check_voice_shell.sh
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$HERE/check_voice_shell.sh"
FIX="$(mktemp -d -t vsfix.XXXXXX)"
export VOICE_SHELL_REPO="$FIX/repo"
export VOICE_SHELL_HARNESS="stub.js"
export VOICE_SHELL_LOCK="$FIX/lock"
export VOICE_SHELL_LOG="$FIX/suite.log"
export CHROME="/usr/bin/true"
mkdir -p "$FIX/repo/wiki" "$FIX/repo/scheduler"
echo "x" > "$FIX/repo/wiki/explorer.html"
touch -t 202001010000 "$FIX/repo/wiki/explorer.html"   # old: clears the quiet period
pass=0; fail=0
ok()   { pass=$((pass+1)); echo "  PASS  $1"; }
bad()  { fail=$((fail+1)); echo "  FAIL  $1 -- $2"; }
check(){ if eval "$2"; then ok "$1"; else bad "$1" "$3"; fi; }
stub() {  # $1 = body (printed to stdout)  $2 = exit code -- a node script, because the wrapper runs `node <harness>`
  printf '%s' "$1" > "$FIX/body.txt"
  printf 'process.stdout.write(require("fs").readFileSync(%s, "utf8") + "\\n"); process.exit(%s);\n' "\"$FIX/body.txt\"" "$2" > "$FIX/repo/stub.js"
  touch -t 202001010000 "$FIX/repo/stub.js" "$FIX/body.txt"   # the harness is itself a gated source; keep it out of the quiet period
}
run() { (cd "$FIX/repo" && bash "$SCRIPT" "$@" >"$FIX/out.txt" 2>&1); echo $?; }
J="$FIX/repo/scheduler/voice_shell.json"; MK="$FIX/repo/voice_shell.FAILED"; LN="$FIX/repo/scheduler/voice_shell.md"

echo "1. RED suite"
stub $'  FAIL  A1 something   -- detail\n  PASS  A2 fine\nrows: 3   passed: 2   failed: 1\nSHELL TEST RED' 1
rc=$(run --force)
check "RED exits 3 (a verdict, not a script error)" "[ \"$rc\" = 3 ]" "exit=$rc: $(cat "$FIX/out.txt")"
check "RED writes the marker with a stamped first line" "[ -f \"$MK\" ] && head -1 \"$MK\" | grep -qE '^\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9:]{8}\] voice-shell suite RED'" "$(head -1 "$MK" 2>&1)"
check "RED marker names the failed row" "grep -q 'A1 something' \"$MK\"" "$(cat "$MK")"
check "state verdict RED with the counts" "python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if d[\"verdict\"]==\"RED\" and d[\"rows\"]==3 and d[\"failed\"]==1 and d[\"exit\"]==1 else 1)' \"$J\"" "$(cat "$J")"
check "one RED line appended" "grep -c '^.* RED rows: 3' \"$LN\" | grep -qx 1" "$(cat "$LN")"

echo "2. harness dies before its summary"
stub $'Error: something exploded' 1
rc=$(run --force)
check "died exits 1 (broken check, not a verdict)" "[ \"$rc\" = 1 ]" "exit=$rc"
check "died writes a marker saying it could not complete" "grep -q 'could not complete' \"$MK\"" "$(cat "$MK" 2>&1)"
check "died is said on stdout with the log tail" "grep -q 'no summary line' \"$FIX/out.txt\" && grep -q 'something exploded' \"$FIX/out.txt\"" "$(cat "$FIX/out.txt")"

echo "3. GREEN clears it"
stub $'  PASS  A1\nrows: 3   passed: 3   failed: 0\nSHELL TEST GREEN' 0
rc=$(run --force)
check "GREEN exits 0" "[ \"$rc\" = 0 ]" "exit=$rc"
check "GREEN removes the marker" "[ ! -e \"$MK\" ]" "marker still present"
check "state verdict GREEN, ran_at_epoch set" "python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if d[\"verdict\"]==\"GREEN\" and d[\"failed\"]==0 and d.get(\"ran_at_epoch\",0)>0 else 1)' \"$J\"" "$(cat "$J")"

echo "4. the gate"
rc=$(run)
check "nothing newer than the last verdict -> no-op, exit 0" "[ \"$rc\" = 0 ] && grep -q 'no-op' \"$FIX/out.txt\"" "$(cat "$FIX/out.txt")"
check "no-op still stamps checked_at (liveness) and keeps the GREEN verdict" "python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if d[\"verdict\"]==\"GREEN\" and d[\"note\"].startswith(\"no-op\") else 1)' \"$J\"" "$(cat "$J")"
sleep 1; touch "$FIX/repo/wiki/explorer.html"
rc=$(run)
check "a source touched just now -> deferred (quiet period), exit 0" "[ \"$rc\" = 0 ] && grep -q 'deferring' \"$FIX/out.txt\"" "$(cat "$FIX/out.txt")"
touch -t 202001010000 "$FIX/repo/wiki/explorer.html"; python3 - "$J" <<'PY'
import json,sys; p=sys.argv[1]; d=json.load(open(p)); d["ran_at_epoch"]=0; json.dump(d,open(p,"w"))
PY
before=$(md5 -q "$J" 2>/dev/null || md5sum "$J" | cut -d' ' -f1); n0=$(wc -l < "$LN")
rc=$(run --dry-run)
after=$(md5 -q "$J" 2>/dev/null || md5sum "$J" | cut -d' ' -f1); n1=$(wc -l < "$LN")
check "--dry-run says it WOULD run and writes nothing" "[ \"$rc\" = 0 ] && grep -q 'WOULD run' \"$FIX/out.txt\" && [ \"$before\" = \"$after\" ] && [ \"$n0\" = \"$n1\" ]" "$(cat "$FIX/out.txt")"
mkdir "$FIX/lock"; rc=$(run --force)
check "a held lock -> exits 0 without running" "[ \"$rc\" = 0 ] && grep -q 'another check_voice_shell is running' \"$FIX/out.txt\"" "$(cat "$FIX/out.txt")"
rmdir "$FIX/lock"
CHROME="/nonexistent/chrome" rc=$(CHROME=/nonexistent/chrome run --force)
check "no Chrome -> exits 2 and says so" "[ \"$rc\" = 2 ] && grep -q 'Chrome not found' \"$FIX/out.txt\"" "$(cat "$FIX/out.txt")"

echo "5. the declared baseline"
export CHROME="/usr/bin/true"   # section 4's last case left this pointing at nothing
# WHY THESE EXIST (Rule 9 -- a test must encode why the behavior matters):
# the suite has a by-design roster of `pending` failures. Scoring RED on
# `failed != 0` made the check cry wolf every morning at a state Tom had
# declared good, and on 2026-11-06 a real seventh failure arrived looking
# exactly like the week of false alarm before it. So the baseline must make
# the known roster GREEN -- AND must still go RED on an unmarked failure at
# ANY count, because an unmarked row means the roster shrank and a new defect
# took the slot. A test that only checked "6 is allowed" would pass a build
# where all six pending tabs landed and six fresh regressions replaced them.
PEND='  FAIL  X %s -- pending: tab does not expose c2a2Find/c2a2Clear/c2a2ReadCut yet   -- {"find":false}\n'
pending_rows() { for t in "$@"; do printf "$PEND" "$t"; done; }
KNOWN_EXC="  EXCEPTION  TypeError: Cannot read properties of undefined (reading 'toFixed')"
suite() {  # $1 = FAIL/EXCEPTION block  $2 = rows $3 = passed $4 = failed  $5 = "exc cerr"
  set -- "$1" "$2" "$3" "$4" "${5:-0 0}"
  local body; body="$1"$'\n'"rows: $2   passed: $3   failed: $4"$'\n'"page exceptions: ${5%% *}   console errors: ${5##* }"
  printf -v body '%s\n%s' "$body" "SHELL TEST RED"
  stub "$body" 1
}
SIX=$(pending_rows prs_3d agents_tab rc_document_explorer physics_explorer rc_sandbox_notebook heartbeat)

suite "$SIX"$'\n'"$KNOWN_EXC" 403 397 6 "1 0"
rc=$(run --force)
check "6 pending + only the KNOWN exception -> GREEN at baseline, exit 0" "[ \"$rc\" = 0 ] && grep -q 'GREEN at declared baseline' \"$FIX/out.txt\"" "exit=$rc: $(cat "$FIX/out.txt")"
check "GREEN at baseline still names the outstanding roster (Rule 12: green must not hide it)" "grep -q 'pending 6/6, unmarked 0' \"$FIX/out.txt\"" "$(cat "$FIX/out.txt")"
check "GREEN at baseline clears the marker" "[ ! -e \"$MK\" ]" "marker still present"
check "state records the roster, not just a count" "python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if d[\"verdict\"]==\"GREEN\" and d[\"pending_failed\"]==6 and d[\"unmarked_failed\"]==0 and d[\"pending_baseline\"]==6 else 1)' \"$J\"" "$(cat "$J")"

suite "$(pending_rows prs_3d agents_tab rc_document_explorer physics_explorer rc_sandbox_notebook heartbeat interT_study)"$'\n'"$KNOWN_EXC" 403 396 7 "1 0"
rc=$(run --force)
check "7 pending failures -> RED (over the declared roster), exit 3" "[ \"$rc\" = 3 ]" "exit=$rc: $(cat "$FIX/out.txt")"
check "over-baseline RED says which bound it broke" "grep -q 'exceeds declared pending baseline 6' \"$MK\"" "$(cat "$MK" 2>&1)"

# THE CLAUSE THAT MATTERS: count is AT the baseline, but one row is unmarked.
# A bare `failed <= 6` comparison passes this. It must not.
suite "$(pending_rows prs_3d agents_tab rc_document_explorer physics_explorer rc_sandbox_notebook)"$'\n''  FAIL  interT_study.html built from its markdown (pre-push gate)   -- missing'$'\n'"$KNOWN_EXC" 403 397 6 "1 0"
rc=$(run --force)
check "6 failures, one WITHOUT 'pending' -> RED even at the baseline count" "[ \"$rc\" = 3 ]" "exit=$rc: $(cat "$FIX/out.txt")"
check "unmarked RED names the regression, not the roster" "grep -q \"not marked 'pending'\" \"$MK\" && grep -q 'interT_study' \"$MK\"" "$(cat "$MK" 2>&1)"

# ... and far UNDER the baseline. An unmarked failure is a regression at any count.
suite '  FAIL  some brand-new assertion   -- detail'$'\n'"$KNOWN_EXC" 403 402 1 "1 0"
rc=$(run --force)
check "1 unmarked failure, far under the baseline -> still RED" "[ \"$rc\" = 3 ] && grep -q \"not marked 'pending'\" \"$MK\"" "exit=$rc: $(cat "$MK" 2>&1)"

# Exceptions are matched by TEXT: a swap hides behind an unchanged count.
suite "$SIX"$'\n''  EXCEPTION  ReferenceError: c2a2Find is not defined' 403 397 6 "1 0"
rc=$(run --force)
check "a DIFFERENT page exception at the same count -> RED" "[ \"$rc\" = 3 ] && grep -q 'undeclared page exception' \"$MK\"" "exit=$rc: $(cat "$MK" 2>&1)"

suite "$SIX"$'\n'"$KNOWN_EXC"$'\n''  CONSOLE    [network] 404 on lib/c2a2-commandline.js' 403 397 6 "1 1"
rc=$(run --force)
check "a console error at the baseline -> RED" "[ \"$rc\" = 3 ] && grep -q 'console error' \"$MK\"" "exit=$rc: $(cat "$MK" 2>&1)"

# A PARTIAL run must never be scored against the baseline. The harness withholds
# the `rows:` line on purpose; six FAIL rows already printed before the throw
# must not be read as "the roster, therefore green".
stub "$SIX"$'\nPARTIAL (no verdict): ran 403 rows, 397 passed, 6 failed before the throw\n  FAILED-BEFORE-THROW  X prs_3d\n\nHARNESS ERROR: Error: CDP timeout' 2
rc=$(run --force)
check "PARTIAL with 6 pending rows printed -> exit 1 (broken check), never GREEN" "[ \"$rc\" = 1 ] && ! grep -q 'GREEN' \"$FIX/out.txt\"" "exit=$rc: $(cat "$FIX/out.txt")"
check "PARTIAL marker says it could not complete, not a verdict" "grep -q 'could not complete' \"$MK\" && ! grep -q 'baseline' \"$MK\"" "$(cat "$MK" 2>&1)"
check "PARTIAL state verdict is DIED, and the counts are not scored" "python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if d[\"verdict\"]==\"DIED\" else 1)' \"$J\"" "$(cat "$J")"

rm -rf "$FIX"
echo; echo "check_voice_shell: $pass passed, $fail failed"
[ "$fail" = 0 ]
