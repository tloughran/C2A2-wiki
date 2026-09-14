#!/bin/bash
# COMMIT_ME_2026-09-14.sh -- paste into Terminal on the Mac. The sandbox cannot write .git,
# and the mount forbids unlink, so neither the commit nor the cleanups below can be done from
# Cowork. SUPERSEDES COMMIT_ME_2026-09-07.sh, which was written but never run -- its three
# guard fixes are still unstaged and are carried here.
#
# Order: clean stale locks and two probe files; untrack the 13.7 MB workbook; stage exactly
# seven paths; commit. It does NOT push -- review, then push yourself. NOTE: the tree is
# already one commit ahead of origin (975bc7f, the 2026-09-14 daily run); your push sends both.
set -euo pipefail
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"

# 1. Stale .git locks the sandbox could not unlink, plus two zero-byte probe files this
#    session created to test whether unlink was permitted (it is not) and could not remove.
if ! pgrep -f "git " >/dev/null 2>&1; then
  rm -f .git/index.lock .git/index.lock.stale-* .git/*.lock .git/_wtest
fi
rm -f wiki/_wtest

# 2. Untrack the workbook. --cached: the file stays on disk, now gitignored. It has been
#    PUBLIC on GitHub Pages since 91bb78b (2026-09-05); this stops it being served. History
#    still holds it -- a history scrub is a separate decision.
git rm --cached -q "wiki/inbox/Resurrecting Civility Master 9-4-2026.xlsx"

# 3. Stage by name. Nothing else: the tree also carries daily-run output (agents_tab.html,
#    wiki/agents/openstory/) that belongs to its own commit path.
git add -- \
  .gitignore \
  scripts/commit_daily_run.sh \
  scripts/janitor.py \
  wiki/inbox/rc_sandbox/gen_sandbox.py \
  wiki/inbox/rc_sandbox/COMMIT_ME_2026-09-14.sh \
  wiki/rc_sandbox_notebook.html \
  wiki/explorer.html

git commit -q -F - <<'MSG'
RC Sandbox: give the published corpus a front door, and close the inbox leak that published it

The Sandbox thread was never meant to be public. commit_daily_run.sh's mtime authorship
window swept wiki/inbox/rc_sandbox/ into "C2A2 daily run" 91bb78b (2026-09-05) and it was
pushed; pages.yml publishes the repo root, so the corpus, the Quodlibet Notebook and the
13.7 MB master workbook have been served from tloughran.github.io since. Tom ratified the
corpus as published on 2026-09-14 and ruled it should have a front door. The workbook is
untracked here; the corpus stays.

Front door: wiki/rc_sandbox_notebook.html, a copy of the notebook promoted out of the inbox
thread to a stable path, registered as the fifth Education tool in explorer.html in the three
places that convention requires -- the row2-edu button, the showHelp() description, and the
search-keyword registry. Two defects fixed in the promoted copy only: it had no <!DOCTYPE>
(BackCompat quirks mode, measured) and no <meta charset> (mojibake under `python3 -m
http.server`, which is the local review path). Verified in Chromium against the staged tree:
standards mode, 2,191 cells, 43 outline links, 0 page errors, RC Document Explorer unaffected
as control. The inbox copy is left byte-identical to what is on origin.

Carried from the unrun COMMIT_ME_2026-09-07.sh, unchanged:

commit_daily_run.sh: NEVER_RUN_OUTPUT_RE holds wiki/inbox/(rc_sandbox|rc_tome)/ and any
.xlsx unconditionally, reported in held_paths.md like other foreign paths. A first draft
"any inbox subdirectory" was falsified on the fixture: the run legitimately writes
wiki/inbox/proposals/ (445 tracked files). Fixture: proposals commit, threads + xlsx held;
control with the regex neutralised commits all of them.

janitor.py: trailing_whitespace auto-fix had stripped Markdown hard line breaks ("  ") in
tl_sandbox_verbatim.md and TL_sandbox_reordered.md (3 lines each) and 40 in
rc_tome/TOC_v2_proposal.md. VERBATIM_DIRS exempts rc_sandbox/ and rc_tome/ from the fix
only; report-only checks still walk them. Falsifier: guarded 0 hits in those dirs, control
(VERBATIM_DIRS empty) 2 hits.

gen_sandbox.py: rebuilds TL_sandbox_reordered.md from assignments.csv + tl_sandbox_cells.json,
byte-identical to the committed file (cmp). The Quodlibet Notebook HTML is still NOT
regenerable -- its generator was lost to the per-session ~ and has not been rebuilt.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016pziUqQ5VkuRgkSmKMPear
MSG

git show --stat --format='%h %s' HEAD | head -20
echo
echo "Not pushed. Review above, then:  git pull --rebase --autostash origin main && git push origin main"
