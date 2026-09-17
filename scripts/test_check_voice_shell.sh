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

rm -rf "$FIX"
echo; echo "check_voice_shell: $pass passed, $fail failed"
[ "$fail" = 0 ]
