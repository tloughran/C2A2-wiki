#!/bin/bash
#
# test_push_daily_run.sh -- drive every gate of push_daily_run.sh.
#
# That script publishes to GitHub unattended, so -- like the commit step -- its
# value is in what it declines to push. Each refusal case below asserts the thing
# that actually matters: the fake origin did NOT move. A refusal that still
# leaked the commit would pass an exit-code-only test, so every case checks the
# origin ref, not just the return code.
#
# Everything runs against a local bare repo standing in for GitHub. The real
# repo and the real remote are never touched.
#
#   bash scripts/test_push_daily_run.sh

set -uo pipefail

SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/push_daily_run.sh"
PASS=0
FAILED=0
DR="C2A2 daily run — 2026-10-05 (committed on the Mac; sandbox cannot write .git)"

ok()  { PASS=$((PASS+1)); echo "  ok   $1"; }
bad() { FAILED=$((FAILED+1)); echo "  FAIL $1"; [ -n "${2:-}" ] && echo "         $2"; }
check() { if [ "$2" = "$3" ]; then ok "$1"; else bad "$1" "expected '$2', got '$3'
$4"; fi; }

# A bare "GitHub", a Mac clone of it, and a second clone playing the heartbeat
# Action that pushes to main behind the Mac's back.
new_fixture() {
  FIX=$(mktemp -d)
  git init -q --bare -b main "$FIX/origin.git"
  git clone -q "$FIX/origin.git" "$FIX/mac" 2>/dev/null
  for r in mac; do
    git -C "$FIX/$r" config user.email t@example.com
    git -C "$FIX/$r" config user.name t
  done
  mkdir -p "$FIX/mac/wiki/heartbeat"
  echo seed > "$FIX/mac/wiki/seed.md"
  echo '{"v":1}' > "$FIX/mac/wiki/heartbeat/digest.json"
  git -C "$FIX/mac" add wiki && git -C "$FIX/mac" commit -q -m seed
  git -C "$FIX/mac" push -q origin main
  git clone -q "$FIX/origin.git" "$FIX/bot" 2>/dev/null
  git -C "$FIX/bot" config user.email bot@example.com
  git -C "$FIX/bot" config user.name bot
}

commit_on_mac() {  # path, content, subject
  mkdir -p "$(dirname "$FIX/mac/$1")"
  printf '%s\n' "$2" > "$FIX/mac/$1"
  git -C "$FIX/mac" add -- "$1"
  git -C "$FIX/mac" commit -q -m "${3:-$DR}"
}

heartbeat_pushes() {  # the daily Action: data-only, lands on origin first
  git -C "$FIX/bot" pull -q --no-rebase origin main
  echo "{\"v\":$RANDOM}" > "$FIX/bot/wiki/heartbeat/digest.json"
  git -C "$FIX/bot" commit -qam "heartbeat: automated refresh"
  git -C "$FIX/bot" push -q origin main
}

origin_head() { git -C "$FIX/origin.git" rev-parse main; }
run() { bash "$SCRIPT" --repo "$FIX/mac" "$@" 2>&1; }

GOOD_HTML='<html><body><script>var x = 1; function f(){ return x; }</script></body></html>'

echo "cases that MUST push (this is the point of the change):"

# The 09-30 failure, reproduced: a daily-run commit sits on the Mac. It must reach
# origin without a human, or the whole decision is not implemented.
new_fixture
commit_on_mac wiki/review_log.html "$GOOD_HTML"
want=$(git -C "$FIX/mac" rev-parse HEAD)
out=$(run); rc=$?
check "daily-run commit pushes" "0" "$rc" "$out"
check "origin now has the commit" "$want" "$(origin_head)"

# The routine case: the heartbeat pushed first, so the Mac is behind. A rebase is
# what failed on 09-30; this must merge and still publish.
new_fixture
heartbeat_pushes
commit_on_mac wiki/review_log.html "$GOOD_HTML"
mine=$(git -C "$FIX/mac" rev-parse HEAD)
out=$(run); rc=$?
check "behind origin: merges and pushes" "0" "$rc" "$out"
git -C "$FIX/origin.git" merge-base --is-ancestor "$mine" main 2>/dev/null; check "  daily-run commit is on origin" "0" "$?"
check "  merged, not rebased (commit id unchanged)" "1" "$(git -C "$FIX/origin.git" log --format=%H main | grep -c "$mine")"

# Status file: the health check reads origin_daily_run_at from it. If this field
# is missing, the new watchdog row is blind on day one.
st=$(python3 -c "import json;d=json.load(open('$FIX/mac/scheduler/daily_push.json'));print(d['verdict'], bool(d['origin_daily_run_at']))")
check "status file records PUSHED + origin date" "PUSHED True" "$st"

# Nothing to do must be a clean no-op that still stamps the status (liveness).
out=$(run); rc=$?
check "nothing ahead: no-op exit 0" "0" "$rc" "$out"
check "  status still written" "OK" "$(python3 -c "import json;print(json.load(open('$FIX/mac/scheduler/daily_push.json'))['verdict'])")"

echo "cases that MUST refuse (exit 1, origin unchanged):"

# Tom's own unpushed work must never ride out under the daily run's push.
new_fixture
commit_on_mac wiki/start_here.html "$GOOD_HTML" "Front door: draft redesign"
commit_on_mac wiki/review_log.html "$GOOD_HTML"
before=$(origin_head)
out=$(run); rc=$?
check "non-daily-run commit ahead" "1" "$rc" "$out"
check "  origin unchanged" "$before" "$(origin_head)"
echo "$out" | grep -q "Front door" && ok "  names the foreign commit" || bad "  names the foreign commit" "$out"

# A forged subject must not widen the scope past the commit step's allowlist.
new_fixture
commit_on_mac scripts/evil.sh "rm -rf /"
before=$(origin_head)
out=$(run); rc=$?
check "path outside allowlist" "1" "$rc" "$out"
check "  origin unchanged" "$before" "$(origin_head)"

new_fixture
commit_on_mac wiki/note.md "contact thomas.loughran@gmail.com"
before=$(origin_head)
out=$(run); rc=$?
check "personal address in outgoing diff" "1" "$rc" "$out"
check "  origin unchanged" "$before" "$(origin_head)"

# The failure the no-blind-push rule was written for: a page whose script breaks.
new_fixture
commit_on_mac wiki/review_log.html '<html><script>function ( { </script></html>'
before=$(origin_head)
out=$(run); rc=$?
check "broken inline JS" "1" "$rc" "$out"
check "  origin unchanged" "$before" "$(origin_head)"
echo "$out" | grep -q "SyntaxError" && ok "  says why (SyntaxError)" || bad "  says why (SyntaxError)" "$out"

# Non-JS script blocks (JSON data islands) must not be fed to node and refused.
new_fixture
commit_on_mac wiki/review_log.html '<html><script type="application/json">{"a": [1,2]}</script><script>var ok=1;</script></html>'
out=$(run); rc=$?
check "JSON data island is not checked as JS" "0" "$rc" "$out"

new_fixture
commit_on_mac wiki/agents/openstory/agent_telemetry.json '{"broken": '
before=$(origin_head)
out=$(run); rc=$?
check "invalid JSON" "1" "$rc" "$out"
check "  origin unchanged" "$before" "$(origin_head)"

# Both sides edit the same file: abort the merge cleanly, leave no MERGE_HEAD for
# the next run (or the next human) to trip on.
new_fixture
git -C "$FIX/bot" pull -q --no-rebase origin main
echo "bot side" > "$FIX/bot/wiki/seed.md"; git -C "$FIX/bot" commit -qam "heartbeat: automated refresh"; git -C "$FIX/bot" push -q origin main
commit_on_mac wiki/seed.md "mac side"
before=$(origin_head)
out=$(run); rc=$?
check "merge conflict with origin" "1" "$rc" "$out"
check "  origin unchanged" "$before" "$(origin_head)"
[ -e "$FIX/mac/.git/MERGE_HEAD" ] && bad "  merge aborted (no MERGE_HEAD left)" || ok "  merge aborted (no MERGE_HEAD left)"

new_fixture
commit_on_mac wiki/review_log.html "$GOOD_HTML"
git -C "$FIX/mac" checkout -q -b feature
before=$(origin_head)
out=$(run); rc=$?
check "not on main" "1" "$rc" "$out"
check "  origin unchanged" "$before" "$(origin_head)"

new_fixture
commit_on_mac wiki/review_log.html "$GOOD_HTML"
before=$(origin_head)
out=$(run --dry-run); rc=$?
check "--dry-run passes the gates" "0" "$rc" "$out"
check "  --dry-run pushes nothing" "$before" "$(origin_head)"

echo
echo "-------------------------------------------"
echo "$PASS passed, $FAILED failed"
[ "$FAILED" -eq 0 ]
