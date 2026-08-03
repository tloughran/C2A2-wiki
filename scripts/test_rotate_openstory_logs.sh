#!/bin/bash
# Exercises rotate_openstory_logs.sh. Every guard is made to FAIL first (the
# "must NOT rotate" and "gzip fails" cases), so none of these is an assertion
# that cannot fail — see [[test-the-guard-not-just-the-happy-path]].
#
# The load-bearing case is #4, the O_APPEND holder. It is the one that would
# catch a future rewrite to rename-and-recreate, which is the obvious-looking
# change that silently breaks rotation under launchd.
SRC="$(cd "$(dirname "$0")" && pwd)/rotate_openstory_logs.sh"
T=$(mktemp -d)
PASS=0; FAIL=0
ok(){ if [ "$1" = "$2" ]; then PASS=$((PASS+1)); echo "  ok   $3"; else FAIL=$((FAIL+1)); echo "  FAIL $3 (want '$2' got '$1')"; fi; }

bash -n "$SRC" || { echo "SYNTAX ERROR"; exit 1; }
echo "syntax: ok"

D="$T/logs"; mkdir -p "$D"
sz(){ stat -f %z "$1" 2>/dev/null || echo missing; }
run(){ LOG_DIR="$D" PATTERN="openstory-*.log" THRESHOLD="$1" KEEP="${2:-5}" bash "$SRC" "${3:-}" >"$T/out" 2>"$T/err"; echo $?; }

# --- 1. under threshold: must NOT rotate ------------------------------------
rm -f "$D"/*; printf 'small\n' > "$D/openstory-a.log"
rc=$(run 1000000)
ok "$rc" "0" "under threshold exits 0"
ok "$(sz "$D/openstory-a.log")" "6" "under threshold leaves the log untouched"
ok "$(ls -1 "$D"/*.gz 2>/dev/null | wc -l | tr -d ' ')" "0" "under threshold writes no archive"

# --- 2. over threshold: rotate, and the archive must round-trip -------------
rm -f "$D"/*; for i in $(seq 1 500); do echo "line $i"; done > "$D/openstory-a.log"
before=$(sz "$D/openstory-a.log")
rc=$(run 100)
ok "$rc" "0" "over threshold exits 0"
ok "$(sz "$D/openstory-a.log")" "0" "live log truncated to 0"
arc=$(ls -1 "$D"/openstory-a.log.*.gz 2>/dev/null | head -1)
ok "$([ -n "$arc" ] && echo yes || echo no)" "yes" "archive written"
ok "$(gzip -dc "$arc" | wc -c | tr -d ' ')" "$before" "archive decompresses to the original bytes"
ok "$(gzip -dc "$arc" | tail -1)" "line 500" "archive holds the last line written"

# --- 3. failure path: gzip fails -> exit non-zero AND do not truncate -------
# This is the ordering guarantee. If it ever regresses, a failed archive
# becomes deleted logs.
rm -f "$D"/*; for i in $(seq 1 500); do echo "line $i"; done > "$D/openstory-a.log"
before=$(sz "$D/openstory-a.log")
FAKE="$T/bin"; mkdir -p "$FAKE"
printf '#!/bin/bash\nexit 1\n' > "$FAKE/gzip"; chmod +x "$FAKE/gzip"
BROKEN="$T/broken.sh"
sed -e 's|^export PATH=.*|export PATH="'"$FAKE"':/usr/bin:/bin"|' "$SRC" > "$BROKEN"
LOG_DIR="$D" PATTERN="openstory-*.log" THRESHOLD=100 bash "$BROKEN" >"$T/out" 2>"$T/err"; rc=$?
ok "$rc" "1" "gzip failure exits non-zero"
ok "$(sz "$D/openstory-a.log")" "$before" "gzip failure leaves the live log intact"
ok "$(ls -1 "$D"/*.gz 2>/dev/null | wc -l | tr -d ' ')" "0" "gzip failure leaves no half-written archive"
ok "$(grep -c 'FAIL' "$T/err")" "1" "gzip failure says so on stderr"

# --- 4. the O_APPEND holder (the launchd case) ------------------------------
# A writer that opened the file with O_APPEND before the rotation must keep
# appending into the SAME inode at offset 0 — not into a renamed file, and
# not at its old 500-line offset (which would leave a sparse hole).
rm -f "$D"/*; for i in $(seq 1 500); do echo "line $i"; done > "$D/openstory-a.log"
exec 9>> "$D/openstory-a.log"
echo "before rotation" >&9
ino_before=$(stat -f %i "$D/openstory-a.log")
rc=$(run 100)
echo "after rotation" >&9
exec 9>&-
ino_after=$(stat -f %i "$D/openstory-a.log")
ok "$rc" "0" "rotation with a live append-holder exits 0"
ok "$ino_after" "$ino_before" "the live log keeps its inode (copy-truncate, not rename)"
ok "$(cat "$D/openstory-a.log")" "after rotation" "post-rotation writes land in the live log"
ok "$(sz "$D/openstory-a.log")" "15" "no sparse hole: file is exactly the new bytes"

# --- 5. prune keeps exactly KEEP newest ------------------------------------
rm -f "$D"/*; printf 'x\n' > "$D/openstory-a.log"
for s in 20260101-000001 20260102-000002 20260103-000003 20260104-000004 20260105-000005 20260106-000006; do
  printf '' | gzip -c > "$D/openstory-a.log.$s.gz"
done
for i in $(seq 1 500); do echo "line $i"; done > "$D/openstory-a.log"
rc=$(run 100 3)
ok "$rc" "0" "prune run exits 0"
# 6 pre-existing + 1 just written = 7; KEEP=3 leaves 3
ok "$(ls -1 "$D"/openstory-a.log.*.gz | wc -l | tr -d ' ')" "3" "prune leaves exactly KEEP archives"
ok "$(ls -1 "$D"/openstory-a.log.2026010*.gz 2>/dev/null | wc -l | tr -d ' ')" "2" "prune deletes oldest first (2 of 6 seeded survive)"

# --- 6. --dry-run changes nothing ------------------------------------------
rm -f "$D"/*; for i in $(seq 1 500); do echo "line $i"; done > "$D/openstory-a.log"
before=$(sz "$D/openstory-a.log")
rc=$(run 100 5 --dry-run)
ok "$rc" "0" "dry-run exits 0"
ok "$(sz "$D/openstory-a.log")" "$before" "dry-run does not truncate"
ok "$(ls -1 "$D"/*.gz 2>/dev/null | wc -l | tr -d ' ')" "0" "dry-run writes no archive"
ok "$(grep -c 'WOULD' "$T/out")" "1" "dry-run reports what it would do"

echo
echo "PASS=$PASS FAIL=$FAIL"
rm -rf "$T"
[ "$FAIL" -eq 0 ]
