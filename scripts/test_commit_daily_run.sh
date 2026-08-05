#!/bin/bash
#
# test_commit_daily_run.sh -- drive every REFUSAL path of commit_daily_run.sh.
#
# This script commits to a repo automatically and unattended. Its value is
# entirely in what it declines to do, so the cases that matter are the ones where
# it must refuse and leave the tree untouched: mid-merge, wrong branch, a stale
# run, a pathspec that escaped, the personal address, an implausible file count.
# A guard nobody has watched fail is not a guard.
#
# Everything runs in a throwaway repo under a temp dir. The real repo is never
# touched, and no test can push anywhere.
#
#   bash scripts/test_commit_daily_run.sh

set -uo pipefail

SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/commit_daily_run.sh"
PASS=0
FAILED=0
ADDRESS='thomas.loughran@gmail.com'

ok()   { PASS=$((PASS+1)); echo "  ok   $1"; }
bad()  { FAILED=$((FAILED+1)); echo "  FAIL $1"; [ -n "${2:-}" ] && echo "         $2"; }

expect_rc() {  # name, expected_rc, actual_rc, output
  if [ "$2" -eq "$3" ]; then ok "$1"; else bad "$1" "expected exit $2, got $3
$4"; fi
}

# A fresh fixture repo plus a registry saying the daily run just ran.
new_fixture() {
  FIX=$(mktemp -d)
  REG="$FIX/registry"
  mkdir -p "$REG" "$FIX/repo/wiki" "$FIX/repo/prototypes/backlog"
  git -C "$FIX/repo" init -q -b main
  git -C "$FIX/repo" config user.email t@example.com
  git -C "$FIX/repo" config user.name t
  echo "seed" > "$FIX/repo/wiki/seed.md"
  git -C "$FIX/repo" add wiki/seed.md
  git -C "$FIX/repo" commit -q -m "seed"
  stamp=$(python3 -c "
from datetime import datetime, timedelta, timezone
print((datetime.now(timezone.utc)-timedelta(hours=${1:-2})).strftime('%Y-%m-%dT%H:%M:%S.000Z'))")
  cat > "$REG/scheduled-tasks.json" <<JSON
{"scheduledTasks":[{"id":"c282-wiki-agent-daily-run","enabled":true,"lastRunAt":"$stamp"}]}
JSON
}

run() { bash "$SCRIPT" --repo "$FIX/repo" --registry-glob "$REG/*.json" "$@" 2>&1; }

head_count() { git -C "$FIX/repo" rev-list --count HEAD; }

echo "cases that MUST refuse (exit 1, nothing committed):"

new_fixture
echo "new" > "$FIX/repo/wiki/new.md"
touch "$FIX/repo/.git/MERGE_HEAD"
before=$(head_count); out=$(run); rc=$?
expect_rc "mid-merge repo" 1 $rc "$out"
[ "$(head_count)" = "$before" ] && ok "mid-merge left HEAD alone" || bad "mid-merge committed anyway"
rm -f "$FIX/repo/.git/MERGE_HEAD"

new_fixture
echo "new" > "$FIX/repo/wiki/new.md"
git -C "$FIX/repo" checkout -q -b sidebranch
out=$(run); rc=$?
expect_rc "not on main" 1 $rc "$out"

new_fixture
echo "new" > "$FIX/repo/wiki/new.md"
git -C "$FIX/repo" checkout -q --detach
out=$(run); rc=$?
expect_rc "detached HEAD" 1 $rc "$out"

# The run has not run for two days, so the dirty tree belongs to somebody else.
new_fixture 50
echo "new" > "$FIX/repo/wiki/new.md"
before=$(head_count); out=$(run); rc=$?
expect_rc "daily run too stale to own this tree" 1 $rc "$out"
[ "$(head_count)" = "$before" ] && ok "stale run left HEAD alone" || bad "stale run committed anyway"

new_fixture
echo "new" > "$FIX/repo/wiki/new.md"
out=$(bash "$SCRIPT" --repo "$FIX/repo" --registry-glob "$FIX/no-such-dir/*.json" 2>&1); rc=$?
expect_rc "task absent from the registry" 1 $rc "$out"

# The address check. History survives deleting the file, so this must stop at the
# commit, not at the push.
new_fixture
echo "mail me at $ADDRESS" > "$FIX/repo/wiki/leak.md"
before=$(head_count); out=$(run); rc=$?
expect_rc "personal address in the staged diff" 1 $rc "$out"
[ "$(head_count)" = "$before" ] && ok "address leak left HEAD alone" || bad "address leak committed anyway"
case "$out" in *leak.md*) ok "names the offending file" ;; *) bad "does not name the offending file" "$out" ;; esac

new_fixture
python3 -c "
import os
for i in range($((401))): open(os.path.join('$FIX/repo/wiki', 'f%04d.md' % i),'w').write('x')"
out=$(run); rc=$?
expect_rc "over the staged-file ceiling" 1 $rc "$out"

echo
echo "refusals must leave a clean index, not a half-built one:"
new_fixture
echo "mail me at $ADDRESS" > "$FIX/repo/wiki/leak.md"
run >/dev/null 2>&1
staged_after=$(git -C "$FIX/repo" diff --cached --name-only | wc -l | tr -d ' ')
[ "$staged_after" = "0" ] && ok "index reset after a refusal" || bad "left $staged_after path(s) staged"

echo
echo "the community_explorer guard:"
new_fixture
git -C "$FIX/repo" rm -q --cached wiki/seed.md >/dev/null 2>&1
echo "generated" > "$FIX/repo/wiki/community_explorer.html"
git -C "$FIX/repo" add wiki/community_explorer.html
git -C "$FIX/repo" commit -q -m "add explorer"
echo "CLOBBERED" > "$FIX/repo/wiki/community_explorer.html"
echo "real output" > "$FIX/repo/wiki/report.md"
out=$(run); rc=$?
expect_rc "runs with a clobbered explorer present" 0 $rc "$out"
if git -C "$FIX/repo" show --name-only --pretty=format: HEAD | grep -q community_explorer; then
  bad "committed community_explorer.html" "$out"
else
  ok "did NOT commit community_explorer.html"
fi
git -C "$FIX/repo" show --name-only --pretty=format: HEAD | grep -q report.md \
  && ok "still committed the real output alongside it" || bad "dropped the real output too"

echo
echo "cases that MUST succeed:"
new_fixture
before=$(head_count)
echo "new" > "$FIX/repo/wiki/new.md"
echo '{"a":1}' > "$FIX/repo/prototypes/level2_build_meta.json"
echo "stray" > "$FIX/repo/unrelated_stray.md"
out=$(run); rc=$?
expect_rc "normal daily-run output" 0 $rc "$out"
[ "$(head_count)" = "$((before+1))" ] && ok "made exactly one commit" || bad "commit count wrong"
files=$(git -C "$FIX/repo" show --name-only --pretty=format: HEAD | grep -v '^$' | sort | tr '\n' ' ')
[ "$files" = "prototypes/level2_build_meta.json wiki/new.md " ] \
  && ok "committed wiki/ and the named prototypes path, nothing else" \
  || bad "wrong file set" "$files"
case "$files" in *unrelated_stray*) bad "swept up an unrelated root stray" ;; *) ok "left the unrelated root stray alone" ;; esac
subject=$(git -C "$FIX/repo" log -1 --format=%s)
case "$subject" in
  "C2A2 daily run"*) ok "subject still matches check_scheduled_commits' '^C2A2 daily run' grep" ;;
  *) bad "subject would break the commit assertion" "$subject" ;;
esac

# A no-op must be exit 0. If it were 1, the launchd agent would report a failure
# every single day the run legitimately produced nothing.
new_fixture
out=$(run); rc=$?
expect_rc "clean tree is a no-op, not a failure" 0 $rc "$out"

new_fixture
echo "new" > "$FIX/repo/wiki/new.md"
before=$(head_count); out=$(run --dry-run); rc=$?
expect_rc "--dry-run exits clean" 0 $rc "$out"
[ "$(head_count)" = "$before" ] && ok "--dry-run committed nothing" || bad "--dry-run committed"
[ "$(git -C "$FIX/repo" diff --cached --name-only | wc -l | tr -d ' ')" = "0" ] \
  && ok "--dry-run left no staged residue" || bad "--dry-run left the index staged"

echo
echo "it must never push:"
new_fixture
git -C "$FIX/repo" remote add origin "$FIX/nonexistent-remote.git"
echo "new" > "$FIX/repo/wiki/new.md"
out=$(run); rc=$?
expect_rc "commits with an unreachable remote configured" 0 $rc "$out"
case "$out" in *push*ing*|*"To $FIX"*) bad "attempted a push" "$out" ;; *) ok "no push attempted" ;; esac

echo
echo "-------------------------------------------"
echo "$PASS passed, $FAILED failed"
[ "$FAILED" -eq 0 ] || exit 1
