#!/usr/bin/env bash
# test_sync_vault_rebase.sh — drives the reconcile guard in sync_vault.sh through every
# path it can take, including the ones that fail.
#
# Run:  bash scripts/test_sync_vault_rebase.sh
#
# Why this exists (2026-08-03): the guard's failure branch had never been watched failing.
# It reported "rebase onto origin/main conflicted" for a `git pull --rebase` that refused to
# start at all, and the refusal itself ("You have unstaged changes") happens on any dirty
# tree — which is this repo's normal nightly state. Both defects were invisible because only
# the happy path was ever exercised.
#
# The block under test is EXTRACTED FROM sync_vault.sh AT RUN TIME, between the
# RECONCILE-BLOCK markers, so this test can never drift from the shipped code. It runs
# against throwaway repos in a temp dir; it never touches the real repo or origin.

set -uo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)/sync_vault.sh"
BLOCK=$(awk '/^# >>> RECONCILE-BLOCK/{f=1;next} /^# <<< RECONCILE-BLOCK/{f=0} f' "$SRC")
if [ -z "$BLOCK" ]; then
  echo "FAIL: could not extract RECONCILE-BLOCK from $SRC (markers missing?)"
  exit 1
fi

SANDBOX=$(mktemp -d "${TMPDIR:-/tmp}/sync_vault_test.XXXXXX")
trap 'rm -rf "$SANDBOX"' EXIT

PASS=0
FAIL=0

ok()   { PASS=$((PASS+1)); printf '  ok   %s\n' "$1"; }
bad()  { FAIL=$((FAIL+1)); printf '  FAIL %s\n' "$1"; }
check(){ if [ "$2" = "$3" ]; then ok "$1"; else bad "$1 (want '$3', got '$2')"; fi; }
has()  { if printf '%s' "$2" | grep -q "$3"; then ok "$1"; else bad "$1 (missing '$3' in: $2)"; fi; }

# Build a bare origin + a working clone + a second clone used to advance origin.
make_pair() {
  local n="$1"
  git init --bare -b main -q "$SANDBOX/$n.git"
  git init -b main -q "$SANDBOX/$n"
  (
    cd "$SANDBOX/$n"
    git config user.name t; git config user.email t@t
    echo line1 > file.txt; echo other > other.txt; echo dirty > dirty.txt
    git add -A; git commit -qm seed
    git remote add origin "$SANDBOX/$n.git"
    git push -q -u origin main
  )
  git clone -q "$SANDBOX/$n.git" "$SANDBOX/$n.up"
  (cd "$SANDBOX/$n.up" && git config user.name u && git config user.email u@u)
}

# Advance origin/main from the second clone.
origin_commit() {
  local n="$1" f="$2" c="$3"
  (cd "$SANDBOX/$n.up" && printf '%s\n' "$c" > "$f" && git add "$f" \
     && git commit -qm "upstream $f" && git push -q origin main)
}

local_commit() {
  local n="$1" f="$2" c="$3"
  (cd "$SANDBOX/$n" && printf '%s\n' "$c" > "$f" && git add "$f" && git commit -qm "local $f")
}

# Run the extracted block against a repo, with log()/fail_loud() stubbed. Returns the
# block's exit status; the fail_loud message (if any) lands in $SANDBOX/failmsg.
run_block() {
  local repo="$SANDBOX/$1"
  rm -f "$SANDBOX/failmsg"
  (
    set -euo pipefail
    REPO="$repo"
    LOG="$repo/.testlog"
    log()       { echo "[log] $*" >>"$LOG"; }
    fail_loud() { printf '%s' "$1" >"$SANDBOX/failmsg"; exit 1; }
    cd "$repo"
    eval "$BLOCK"
  ) >>"$SANDBOX/harness.log" 2>&1
  return $?
}

failmsg() { cat "$SANDBOX/failmsg" 2>/dev/null || true; }

# ── 1. HAPPY PATH: clean tree, origin ahead ──────────────────────────────────
echo "1. clean tree, origin ahead — must rebase and succeed"
make_pair clean
origin_commit clean file.txt upstream
local_commit  clean other.txt localwork
run_block clean; rc=$?
check "exit status 0" "$rc" "0"
check "upstream content present" "$(cat "$SANDBOX/clean/file.txt")" "upstream"
check "local commit replayed on top" \
  "$(cd "$SANDBOX/clean" && git log -1 --pretty=%s)" "local other.txt"

# ── 2. THE REGRESSION: dirty tree ────────────────────────────────────────────
# This is the case that killed the 2026-07-23 run. Pre-fix, git refuses outright.
echo "2. DIRTY tree (unstaged tracked change), origin ahead — must still succeed"
make_pair dirty
origin_commit dirty file.txt upstream
local_commit  dirty other.txt localwork
echo "uncommitted agent output" > "$SANDBOX/dirty/dirty.txt"
run_block dirty; rc=$?
check "exit status 0" "$rc" "0"
check "upstream content present" "$(cat "$SANDBOX/dirty/file.txt")" "upstream"
check "dirty file restored, not lost" \
  "$(cat "$SANDBOX/dirty/dirty.txt")" "uncommitted agent output"
check "dirty file still uncommitted" \
  "$(cd "$SANDBOX/dirty" && git diff --name-only)" "dirty.txt"
check "no stash left behind" "$(cd "$SANDBOX/dirty" && git stash list | wc -l | tr -d ' ')" "0"

# ── 3. REAL CONFLICT: must say conflicted, and must actually abort ───────────
echo "3. genuine rebase conflict — must report a conflict AND leave no rebase in progress"
make_pair conflict
origin_commit conflict file.txt upstream-version
local_commit  conflict file.txt local-version
run_block conflict; rc=$?
check "exit status 1" "$rc" "1"
has   "message names a conflict" "$(failmsg)" "conflicted and was aborted"
check "rebase actually aborted" \
  "$([ -d "$SANDBOX/conflict/.git/rebase-merge" ] || [ -d "$SANDBOX/conflict/.git/rebase-apply" ] \
     && echo in-progress || echo clean)" "clean"
check "local commit kept" \
  "$(cd "$SANDBOX/conflict" && git log -1 --pretty=%s)" "local file.txt"

# ── 4. REBASE NEVER STARTS: must NOT claim a conflict ────────────────────────
# Real instance: the repo sat in an unconcluded merge for two days (2026-08-01).
echo "4. rebase refuses to start (unconcluded merge) — must NOT call it a conflict"
make_pair nostart
origin_commit nostart file.txt upstream
local_commit  nostart other.txt localwork
(
  cd "$SANDBOX/nostart"
  git checkout -q -b side HEAD~1
  printf 'side\n' > other.txt; git add other.txt; git commit -qm side
  git checkout -q main
  git merge --no-commit side >/dev/null 2>&1 || true
)
run_block nostart; rc=$?
check "exit status 1" "$rc" "1"
has   "message says no rebase started" "$(failmsg)" "never started a rebase"
has   "message quotes what git said"   "$(failmsg)" "git said:"
if printf '%s' "$(failmsg)" | grep -q "conflicted"; then
  bad "message must NOT claim a conflict (the 2026-07-23 defect)"
else
  ok "message does not claim a conflict"
fi

# ── 5. AUTOSTASH RESTORE CONFLICTS: git exits 0 here, so we must catch it ────
# Verified 2026-08-03: `git pull --rebase --autostash` returns SUCCESS when the rebase
# lands but the autostash restore conflicts. It leaves `UU` unmerged files in the tree and
# the changes in the stash. Nothing in git's exit status says so.
echo "5. rebase succeeds but autostash restore conflicts — must be caught despite exit 0"
make_pair stashconf
origin_commit stashconf file.txt upstream-version
local_commit  stashconf other.txt localwork
echo "locally-edited, conflicts with upstream" > "$SANDBOX/stashconf/file.txt"
run_block stashconf; rc=$?
check "exit status 1" "$rc" "1"
has   "message names the unmerged tree" "$(failmsg)" "unmerged files"
has   "message points at the stash"     "$(failmsg)" "git stash list"
check "tree really is unmerged" \
  "$(cd "$SANDBOX/stashconf" && git status --porcelain file.txt)" "UU file.txt"
check "changes really are in the stash" \
  "$(cd "$SANDBOX/stashconf" && git stash list | wc -l | tr -d ' ')" "1"

echo
echo "passed: $PASS   failed: $FAIL"
[ "$FAIL" -eq 0 ] || { echo "--- harness output ---"; cat "$SANDBOX/harness.log"; exit 1; }
