#!/bin/bash
# Exercises the watchdog's new boot gate. Every assertion is made to FAIL first
# (see the "must NOT fire" cases) so none of them is a test that cannot fail.
SRC="$(cd "$(dirname "$0")" && pwd)/openstory-watchdog.sh"
T=$(mktemp -d)
FAKE="$T/bin"; mkdir -p "$FAKE" "$T/archive"
PASS=0; FAIL=0
ok(){ if [ "$1" = "$2" ]; then PASS=$((PASS+1)); echo "  ok   $3"; else FAIL=$((FAIL+1)); echo "  FAIL $3 (want '$2' got '$1')"; fi; }

# --- fakes -------------------------------------------------------------------
cat > "$FAKE/curl" <<'EOF'
#!/bin/bash
echo "000"
EOF
cat > "$FAKE/pgrep" <<'EOF'
#!/bin/bash
[ -n "$FAKE_PID" ] && echo "$FAKE_PID"
EOF
cat > "$FAKE/ps" <<'EOF'
#!/bin/bash
for a in "$@"; do
  case "$a" in
    etime=) echo "$FAKE_ETIME"; exit 0 ;;
    time=)  echo "$FAKE_CPU";   exit 0 ;;
  esac
done
EOF
cat > "$FAKE/launchctl" <<'EOF'
#!/bin/bash
echo KICKSTART >> "$MARKER"
EOF
cat > "$FAKE/osascript" <<'EOF'
#!/bin/bash
exit 0
EOF
cat > "$FAKE/sleep" <<'EOF'
#!/bin/bash
exit 0
EOF
chmod +x "$FAKE"/*

# --- script under test, with PATH and ARCHIVE redirected ---------------------
W="$T/watchdog.sh"
sed -e 's|^export PATH=.*|export PATH="'"$FAKE"':/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"|' \
    -e 's|^ARCHIVE=.*|ARCHIVE="'"$T"'/archive"|' "$SRC" > "$W"
chmod +x "$W"

bash -n "$W" || { echo "SYNTAX ERROR"; exit 1; }
echo "syntax: ok"

export HOME="$T/home"
STATE="$HOME/Library/Application Support/openstory-watchdog"
LOG="$HOME/Library/Logs/openstory-watchdog.log"
export MARKER="$T/marker"

reset(){ rm -rf "$HOME" "$MARKER"; mkdir -p "$STATE" "$HOME/Library/Logs"; }
run(){ FAKE_PID="$1" FAKE_ETIME="$2" FAKE_CPU="$3" bash "$W" >/dev/null 2>&1; }
lastlog(){ tail -1 "$LOG" 2>/dev/null; }
kicked(){ [ -f "$MARKER" ] && echo yes || echo no; }

echo
echo "CASE 1 — booting, CPU advancing: must veto every time, forever"
reset
run 4242 "09:07:23" " 41:12.30"
ok "$(lastlog | grep -c 'BOOTING, not restarting')" "1" "first check vetoes"
run 4242 "09:12:23" " 46:30.11"
run 4242 "09:17:23" " 52:01.87"
run 4242 "09:22:23" "1:02:44.02"
ok "$(lastlog | grep -c 'BOOTING, not restarting')" "1" "still vetoing after 4 checks"
ok "$(kicked)" "no" "never restarted"
ok "$(cat "$STATE/consecutive_failures" 2>/dev/null || echo 0)" "0" "failure counter untouched"

echo
echo "CASE 2 — booting, CPU flat: must escalate to a restart (the gate must fail loud)"
reset
run 4242 "09:07:23" "41:12.30"
run 4242 "09:12:23" "41:12.30"
ok "$(lastlog | grep -c 'Stall 1/3')" "1" "flat CPU -> stall 1"
run 4242 "09:17:23" "41:12.30"
ok "$(lastlog | grep -c 'Stall 2/3')" "1" "flat CPU -> stall 2"
ok "$(kicked)" "no" "not restarted yet"
run 4242 "09:22:23" "41:12.30"
ok "$(grep -c 'boot is WEDGED' "$LOG")" "1" "flat CPU -> declared wedged"
ok "$(kicked)" "yes" "wedged boot DOES restart"

echo
echo "CASE 3 — pid HAS served before: boot gate must NOT fire (real hang still restarts)"
reset
echo 4242 > "$STATE/healthy_pid"
run 4242 "09:07:23" "41:12.30"
ok "$(grep -c 'BOOTING' "$LOG")" "0" "no boot claim for a pid that served"
ok "$(kicked)" "yes" "a served-then-hung backend still restarts"

echo
echo "CASE 4 — CPU advancing but pid CHANGED: prior pid's cpu must not be credited"
reset
run 4242 "09:07:23" "50:00.00"
run 9999 "00:20:00" "00:10.55"   # new pid, much LOWER cpu than the old one
ok "$(lastlog | grep -c 'BOOTING, not restarting')" "1" "new pid vetoes on its own baseline, not the old pid's"

echo
echo "CASE 5 — ps_time_secs parsing"
p(){ bash -c 'source_fn(){ :; }; '"$(sed -n '/^ps_time_secs()/,/^}/p' "$W")"'; ps_time_secs "$1"' _ "$1"; }
ok "$(p '06:42')"        "402"    "MM:SS"
ok "$(p '1:02:03')"      "3723"   "HH:MM:SS"
ok "$(p '2-03:04:05')"   "183845" "DD-HH:MM:SS"
ok "$(p '  41:12')"      "2472"   "leading spaces (ps -o time= pads)"
ok "$(p ' 82:16.43')"    "4936"   "ps -o time= hundredths (LIVE format, was 999999)"
ok "$(p '1-02:03:04.99')" "93784" "days AND hundredths together"
ok "$(p 'etimes: keyword not found')" "999999" "garbage -> 999999, not a small number"

echo
echo "CASE 6 — WAL witness: an uncommitted transaction is progress"
# frontier_now must report a CHANGE when only the -wal file moves, because the
# 2026-07-30 backend held a long transaction with the committed count frozen.
fw(){ bash -c 'OS_DB="'"$1"'"; '"$(sed -n '/^WAL=/,/^}/p' "$W")"'; frontier_now'; }
DB="$T/fake.db"
# A REAL store, so the db half resolves and the -wal half is the only variable.
# (An empty file has no `sessions` table, the read returns empty, and
# frontier_now then correctly emits nothing -- which is the "cannot read the
# store" path, not the case under test here.)
sqlite3 "$DB" "CREATE TABLE sessions(last_event TEXT); CREATE TABLE events(id INTEGER);
               INSERT INTO sessions VALUES('2026-07-30T16:07:52.076Z');" >/dev/null 2>&1
printf 'aaaa' > "$DB-wal"
A=$(fw "$DB")
printf 'aaaabbbb' > "$DB-wal"          # wal grew
B=$(fw "$DB")
ok "$([ -n "$A" ] && [ "$A" != "$B" ] && echo changed || echo same)" "changed" \
   "growing -wal reads as progress even with the store frozen"
ok "$(fw "$DB" | grep -c 'wal=')" "1" "witness carries a wal= component"
rm -f "$DB-wal"
ok "$(fw "$DB" | grep -c 'wal=0:0')" "1" "absent -wal degrades to 0:0, not to empty"

echo
echo "CASE 7 — the leash depends on WHICH failure it is"
ok "$(grep -c 'MAX_STORE_VETOES=36' "$W")" "1" "healthy-port leash is ~3h, not 15 min"
ok "$(grep -c 'if \[ "\$SERVING" = "1" \]; then LEASH=\$MAX_STORE_VETOES; else LEASH=\$MAX_VETOES; fi' "$W")" "1" \
   "leash selected by whether the port answered"
# The long leash must still terminate: a store that never catches up IS a fault.
ok "$(grep -c 'no longer a long transaction' "$W")" "1" "long leash still ends in a restart"

echo
echo "=== $PASS passed, $FAIL failed ==="
rm -rf "$T"
[ "$FAIL" -eq 0 ]
