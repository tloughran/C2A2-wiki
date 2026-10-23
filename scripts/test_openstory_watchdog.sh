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
echo "CASE 6 — the witness must NOT credit -wal activity as ingest progress"
# Retired the wal component 2026-07-30: at 13:13 the db grew 53 MB and the wal
# mtime advanced while committed events stayed pinned at 768692, because the
# backend was writing patterns/FTS. A wal witness reports that as "progressing"
# and cannot distinguish it from ingest.
fw(){ bash -c 'OS_DB="'"$1"'"; '"$(sed -n '/^frontier_now()/,/^  2>\/dev\/null | tr -d .*$/p' "$W")"'; frontier_now'; }
DB="$T/fake.db"
sqlite3 "$DB" "CREATE TABLE sessions(last_event TEXT); CREATE TABLE events(id INTEGER);
               INSERT INTO sessions VALUES('2026-07-30T16:07:52.076Z');" >/dev/null 2>&1
printf 'aaaa' > "$DB-wal"
A=$(fw "$DB")
printf 'aaaabbbbcccc' > "$DB-wal"      # wal churns; NOTHING committed
B=$(fw "$DB")
ok "$([ -n "$A" ] && [ "$A" = "$B" ] && echo same || echo changed)" "same" \
   "wal churn with no commit must NOT read as progress"
ok "$(fw "$DB" | grep -c 'wal=')" "0" "witness carries no wal component"
sqlite3 "$DB" "INSERT INTO events VALUES(1);" >/dev/null 2>&1
ok "$([ "$(fw "$DB")" != "$A" ] && echo changed || echo same)" "changed" \
   "a real committed row DOES read as progress"

echo
echo "CASE 7 — the leash depends on WHICH failure it is"
ok "$(grep -c 'MAX_STORE_VETOES=36' "$W")" "1" "healthy-port leash is ~3h, not 15 min"
ok "$(grep -c 'if \[ "\$SERVING" = "1" \]; then LEASH=\$MAX_STORE_VETOES; else LEASH=\$MAX_VETOES; fi' "$W")" "1" \
   "leash selected by whether the port answered"
# The long leash must still terminate: a store that never catches up IS a fault.
ok "$(grep -c 'no longer a long transaction' "$W")" "1" "long leash still ends in a restart"

echo
echo "CASE 8 — the marker's subject is OPENSTORY, not the volume"
# Why this case exists. From 2026-10-14 to 10-23 openstory_precondition.FAILED was
# rewritten every run and could never clear: marker_clear was gated on
# `[ -d "$ARCHIVE" ]`, and the drive was the thing that was missing. So the alarm
# repeated for nine days with no path to resolution, and check_scheduler_health
# reported it as a fresh FAIL each morning until it stopped meaning anything.
#
# The same run also proved the two facts are independent in the other direction:
# on 10-23 the drive dropped at 11:16 while the backend stayed up and ingested
# 2,746 events, and the marker still asserted "ingest is STOPPED".
#
# A test that only checked the marker gets written would have passed throughout.
# These two assert the clear path exists with the drive absent, and that the text
# no longer claims something the script cannot observe.
W8="$T/watchdog_case8.sh"
mkdir -p "$T/repo"
sed -e 's|^REPO=.*|REPO="'"$T"'/repo"|' "$W" > "$W8"
chmod +x "$W8"
bash -n "$W8" || { echo "  FAIL CASE 8 harness syntax"; FAIL=$((FAIL+1)); }
M8="$T/repo/openstory_precondition.FAILED"

# A healthy, ingesting backend with the drive STILL ABSENT must clear the marker.
cat > "$FAKE/curl" <<'EOF'
#!/bin/bash
echo "200"
EOF
cat > "$FAKE/python3" <<'EOF'
#!/bin/bash
echo "ingest lag OK (fake)"
exit 0
EOF
chmod +x "$FAKE/curl" "$FAKE/python3"
reset
rm -rf "$T/archive"                 # drive absent, exactly as it is today
printf '[2026-10-14 05:18:51] stale alarm from nine days ago\n' > "$M8"
FAKE_PID=4242 FAKE_ETIME="99:99:99" FAKE_CPU=" 41:12.30" bash "$W8" >/dev/null 2>&1
ok "$([ -f "$M8" ] && echo present || echo cleared)" "cleared" \
   "healthy backend clears a stale marker even with the drive absent"

# And the inverse, so the clear is not simply unconditional: an unhealthy backend
# with the drive absent must still RAISE the marker.
cat > "$FAKE/curl" <<'EOF'
#!/bin/bash
echo "000"
EOF
chmod +x "$FAKE/curl"
reset
rm -rf "$T/archive"
rm -f "$M8"
FAKE_PID="" FAKE_ETIME="" FAKE_CPU="" bash "$W8" >/dev/null 2>&1
ok "$([ -f "$M8" ] && echo present || echo cleared)" "present" \
   "unhealthy backend with the drive absent still raises the marker"
# The text must not assert a thing this script cannot see. It has no view of
# whether ingest is flowing -- on 10-23 it was, while this said it was not.
ok "$(grep -c 'ingest is STOPPED' "$M8" 2>/dev/null)" "0" \
   "marker no longer claims 'ingest is STOPPED' (it cannot observe that)"
ok "$(grep -c 'unsupervised' "$M8" 2>/dev/null)" "1" \
   "marker reports the supervision gap, which is what it CAN observe"
# last_frontier is the one genuinely useful measurement here; it must survive.
ok "$(grep -c 'frontier' "$M8" 2>/dev/null)" "1" \
   "marker still carries the frontier measurement"

echo
echo "=== $PASS passed, $FAIL failed ==="
rm -rf "$T"
[ "$FAIL" -eq 0 ]
