#!/usr/bin/env bash
# tidy_repo.sh -- retire worktrees and branches that are fully absorbed into
# origin/main, and repair worktree registrations pointing at dead paths.
#
# REPORT-ONLY by default. --apply is the only thing that deletes.
#
# Safety contract:
#   - never touches a branch that is not an ancestor of origin/main
#   - never touches a remote
#   - never removes a worktree with modified or untracked files
#   - refuses to run on a dirty tree, off main, or with a lock present
#
# Rationale (2026-08-28): 59 local branches, 32 of them fully merged and inert;
# two worktrees registered at paths that no longer exist. The pile is not a disk
# problem, it is a legibility problem -- you cannot find live work inside it.

set -euo pipefail

REPO="${REPO:-/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project}"
APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1

cd "$REPO"

say() { printf '%s\n' "$*"; }
act() { if [ "$APPLY" = 1 ]; then say "  DO   $*"; eval "$@"; else say "  WOULD $*"; fi; }

PROTECTED="main"

say "=== tidy_repo $( [ "$APPLY" = 1 ] && echo APPLY || echo DRY-RUN ) ==="

# ---- guards -------------------------------------------------------------
for lk in .git/index.lock .git/HEAD.lock; do
  if [ -e "$lk" ]; then
    say "REFUSE: $lk present. Clear it first (scripts/verify_lock_fix.sh)."
    exit 1
  fi
done

BR=$(git rev-parse --abbrev-ref HEAD)
if [ "$BR" != "main" ]; then
  say "REFUSE: HEAD is on '$BR', not main."
  exit 1
fi

# Only APPLY needs a clean tree; a report must always be runnable.
if [ "$APPLY" = 1 ] && [ -n "$(git status --porcelain)" ]; then
  say "REFUSE: working tree is dirty. Commit or stash first."
  exit 1
fi

git rev-parse --verify -q origin/main >/dev/null || { say "REFUSE: no origin/main."; exit 1; }
MAIN=$(git rev-parse origin/main)
say "origin/main = ${MAIN:0:9}"
say ""

# ---- phase 1: worktrees at dead paths ------------------------------------
say "--- worktrees registered at paths that do not exist ---"
DEAD=0
while read -r wt; do
  [ -z "$wt" ] && continue
  if [ ! -d "$wt" ]; then
    DEAD=$((DEAD+1))
    say "  dead: $wt"
    if git worktree list --porcelain | grep -A3 -F "worktree $wt" | grep -q '^locked'; then
      act "git worktree unlock \"$wt\""
    fi
  fi
done < <(git worktree list --porcelain | awk '/^worktree /{print substr($0,10)}')
[ "$DEAD" = 0 ] && say "  none"
act "git worktree prune -v"
say ""

# ---- phase 2: live worktrees ---------------------------------------------
say "--- live worktrees ---"
SELF=$(git rev-parse --show-toplevel)
while read -r wt; do
  [ -z "$wt" ] && continue
  [ "$wt" = "$SELF" ] && continue
  [ -d "$wt" ] || continue
  head=$(git -C "$wt" rev-parse HEAD 2>/dev/null) || { say "  BROKEN  $wt"; continue; }
  name=$(basename "$wt")
  dirty=$(git -C "$wt" status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  case "$wt" in
    "$SELF"/.claude/worktrees/*) ;;
    *) say "  KEEP    $name -- outside .claude/worktrees; a named directory, not ours to remove"
       continue;;
  esac
  if git merge-base --is-ancestor "$head" "$MAIN" 2>/dev/null; then
    if [ "$dirty" != 0 ]; then
      say "  KEEP    $name -- merged, but $dirty uncommitted path(s). Rescue them first:"
      git -C "$wt" status --porcelain | sed 's/^/            /'
    else
      say "  RETIRE  $name -- merged into origin/main, clean"
      act "git worktree remove \"$wt\""
    fi
  else
    ahead=$(git rev-list --count "$MAIN".."$head" 2>/dev/null || echo '?')
    say "  KEEP    $name -- $ahead commit(s) NOT in origin/main"
  fi
done < <(git worktree list --porcelain | awk '/^worktree /{print substr($0,10)}')
say ""

# ---- phase 3: branches ----------------------------------------------------
say "--- branches ---"
# branches currently checked out anywhere must not be deleted
CHECKED=" $(git worktree list --porcelain | awk '/^branch /{sub("refs/heads/","",$2); print $2}' | tr '\n' ' ') "

MERGED=(); LIVE=()
while read -r b; do
  case " $PROTECTED " in *" $b "*) continue;; esac
  case "$CHECKED" in *" $b "*) say "  SKIP    $b -- checked out in a worktree"; continue;; esac
  tip=$(git rev-parse "$b")
  if git merge-base --is-ancestor "$tip" "$MAIN"; then
    MERGED+=("$b")
  else
    LIVE+=("$b")
  fi
done < <(git for-each-ref --format='%(refname:short)' refs/heads)

say "  ${#MERGED[@]} fully merged into origin/main -- deleting these loses nothing:"
for b in "${MERGED[@]:-}"; do [ -n "$b" ] && say "      $b"; done
say ""
say "  ${#LIVE[@]} NOT merged -- untouched, each needs a human decision:"
for b in "${LIVE[@]:-}"; do
  [ -n "$b" ] || continue
  n=$(git rev-list --count "$MAIN".."$b")
  # pipefail + a grep that matches nothing exits 1 and, under set -e, kills the
  # whole report. A branch on no remote is the NORMAL case here, not an error.
  rem=$(git for-each-ref --contains "$(git rev-parse "$b")" --format='%(refname:short)' refs/remotes 2>/dev/null | grep -v '^origin$' | head -1 || true)
  say "      $b  (+$n, remote=${rem:-NONE})"
done
say ""

for b in "${MERGED[@]:-}"; do
  [ -n "$b" ] && act "git branch -d \"$b\" || say \"      REFUSED (left in place): $b\""
done

say ""
say "=== done ==="
[ "$APPLY" = 0 ] && say "Nothing was changed. Re-run with --apply to act."
exit 0
