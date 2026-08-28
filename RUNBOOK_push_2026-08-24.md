# RUNBOOK — clear the backlog and unblock the crons

**Written:** 2026-08-24 08:40 EDT · **Run from:** Code mode on the Mac, native filesystem
**Repo:** `/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project`
**HEAD at writing:** `4213237` · working tree 327 dirty (54 modified, 273 untracked)

> **⏰ Hard deadline: 21:00 tonight.** `sync_vault.plist` fires at `Hour 21 / Minute 0`. It died
> last night at 21:01:34 and will die again tonight unless §1 is done first.

Do **not** run any of this from a Cowork session on the mounted repo — the mount forbids
`unlink`, so rebase, merge, checkout and `reset --hard` all fail, and every `git status` leaves a
0-byte `.git/index.lock` behind. See Appendix A.

---

## 0 · Gate — is anything mid-write? (30 seconds)

```sh
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
ls -l .git/index.lock 2>/dev/null && echo "LOCK PRESENT" || echo "no lock"
```

- **No lock** → proceed.
- **0-byte lock** → leftover from a Cowork read. `mkdir -p _to_delete && mv .git/index.lock _to_delete/index.lock.$(date +%s)`
- **Non-empty lock, or a live holder** → stop. Something is genuinely writing. Wait it out.
  Never steal — `sync_vault.sh` refuses to, and so should you.

---

## 1 · ⏰ Unblock tonight's 21:00 sync — do this before anything else

Last night's failure, verbatim from `sync_vault.FAILED`:

```
21:00:18  git lock HELD by a live process: index.lock(pid 56282) — waiting 15s (attempt 2/6)
21:01:34  SYNC FAILED — lock still present after 90s. NOT stealing the lock.
          Nothing committed, nothing pushed.
```

The lock-wait logic worked correctly and still lost, because three tasks stack into the same
evening window:

| 19:50 | weekly sewing agent writes `connectivity_log.csv` |
| 19:57 | weekly sewing agent writes `sewing_agent_log.md` |
| 20:03 | bootstrap audit starts — same vault, **different resolver** |
| 21:00 | `sync_vault` finds the lock held, waits 90 s, dies |

### 1a · Disable the bootstrap task — its own recommendation, item 0

> *"It has fired nine times as a 'ONE-TIME' bootstrap, it now collides with the weekly agent by
> thirteen minutes, and every run since 06-28 has correctly declined to execute its own Phase 3.
> Its residual value — the follow-through audit — belongs in the weekly agent, which already has
> the vault loaded."*

It is a Claude scheduled task, not launchd. Find it:

```sh
ls ~/Library/Application\ Support/Claude/*/*/*/scheduled-tasks.json
grep -il 'bootstrap' ~/Library/Application\ Support/Claude/*/*/*/scheduled-tasks.json
```

Disable it in the same surface that created it. Keep `c2a2-sewing-agent-weekly`; it is the one
that owns `connectivity_log.csv`.

### 1b · Confirm the sync is actually loaded

```sh
launchctl list | grep -iE 'summa-vault-sync|sync_vault'
grep -A4 StartCalendarInterval sync_vault.plist
```

**If §1a slips**, move the sync instead — `Hour 22` buys an hour of clearance. One or the other
must happen today; doing neither guarantees a third dead night.

### 1c · Make the failure audible

`sync_vault.FAILED` has been sitting in the repo root since last night and nothing read it. That
is the same defect that let 08-19…08-22 vanish: *every staleness alarm in the fleet is scoped to
an artifact a running job maintains; none takes a non-event as its subject.* Wire
`sync_vault.FAILED` into `scripts/check_scheduler_health.py` or the morning health check.

---

## 2 · Run the vault sync by hand, now

17 `wiki/vault/synthesis/Day-*.md` plus `vault/refs/index_summary.md` are sitting dirty — that is
exactly the payload last night's sync was reaching for. Its own script is the right tool:

```sh
bash sync_vault.sh 2>&1 | tail -20
```

**Verify:** `git log --oneline -1` shows `Summa vault sync 2026-08-24 (N file(s) updated)`, and
`git status --porcelain wiki/vault | wc -l` returns 0. Then move the stale marker aside:

```sh
mv sync_vault.FAILED _to_delete/sync_vault.FAILED.2026-08-23
```

---

## 3 · Reconcile `pending/` before committing it

Three concurrent tradition agents each read the queue as **54**; disk held **56**; it is at **60**
now. One collision was caught and self-corrected `-001` → `-002`. The count divergence was caught
by nobody. *Sequential numbering across concurrent agents is a race, not a fact.*

```sh
ls wiki/inbox/proposals/pending | sed -E 's/^([0-9-]+_[a-z]+).*/\1/' | sort | uniq -d
ls wiki/inbox/proposals/pending | grep -oE 'PROP-[0-9-]+-[0-9]+' | sort | uniq -d
```

Resolve any duplicate ID **before** step 4 — once committed it is a permanent provenance defect.
Remember `PROCESSED_LOG` keys on **slug**, not filename: normalize before diffing.

---

## 4 · Commit the daily-run backlog

Use the script, not hand-rolled `git add` — it replicates Phase 6 of the run's own SKILL.md
exactly, including the pathspec, the `community_explorer.html` guard, and the commit-message shape
that `check_scheduled_commits.py` greps for.

```sh
bash scripts/commit_daily_run.sh --dry-run
bash scripts/commit_daily_run.sh
```

**⚠️ Ceiling check.** The script refuses above **400 paths**. The tree is at 327 and the bootstrap
report projects the ceiling inside three weeks at current rate. If it refuses, do not raise the
limit — split the commit by date range (precedent: `664be6f`, `C2A2 daily run — 2026-08-02..08-03`).

**It does not push, and that is deliberate** — CLAUDE.md holds that nothing reaches GitHub without
a human looking first, with the heartbeat's data-only refresh as the sole carve-out. Daily-run
output is wiki prose, which is exactly the class that rule protects. Pushing is §7.

---

## 5 · The Rohr univocity audit — gates every regeneration below

Last night's sewing run found Rohr grounding the Universal Christ in **Scotist univocity of
being**, in his own voice with the Latin supplied. "Univocity" and "Scotus" appear nowhere in the
Rohr tradition before that date. Univocity is the historic alternative to the Thomist **analogy**
the Stump wing is committed to.

> *If Rohr means it metaphysically, several existing Rohr↔Stump convergences are convergences in
> English only* — and the second-personal-knowing entries are the most exposed, because "knowledge
> of a person" applied to God means different things under the two doctrines.

The audit is cheap. Put two questions to each recorded convergence:

1. Does it survive if "is" means the same thing on both sides?
2. Does it survive if it does not?

Note the asymmetry: if Rohr does *not* mean it metaphysically, the Universal Christ loses the
ontological grounding the proposal was captured for and reverts to what the proposal itself calls
"pious re-description." Either answer is informative; no answer is not.

**Blast radius has grown since yesterday** — `rohr_stump_bridge.md` changed again overnight and
eight new bridges landed beside it (`carroll_levin`, `fredrickson_rohr`, `friston_levin`,
`friston_loughran`, `hawkins_hoffman`, `hawkins_levin`, `levin_wolfram`, `mcgilchrist_wolfram`).

**Separately quarantined:** the Levin "cancer as somatic dissociative identity disorder" claim
carries the strongest Levin↔Kastrup bridge on record and rests on a spoken description in an
auto-generated transcript — no paper identified, no numbers, 48 slides unread. The bridge note
self-quarantines and may land; nothing downstream may cite it. **Retrieving that citation is the
highest-value single verification task in the vault.**

---

## 6 · Regenerate derived artifacts — only after §5

The 04:37 run already regenerated `review_log.html` *without* the audit, so that file currently
renders convergences the network has flagged as possibly English-only. Do not push it as-is.

```sh
bash scripts/refresh_review_log.sh
bash scripts/regen_prs_connectome.sh
bash scripts/regen_summa_sociogram.sh --summa    # --summa is NOT optional
bash scripts/regen_level2_signals.sh
```

**Verify before committing:**

- Summa node count **≥ 331** — a bare sociogram call silently drops the Summa layer.
- Regenerate `wiki_narration.html` through the wrapper, never by a bare call, or the agent and
  Summa layers drop.
- Iframe tabs must content-hash or inline their JS/CSS — `stamp_assets.py` enforces this.

Commit as a **second** commit, separate from §4, so the generated churn is reviewable apart from
the agent output.

---

## 7 · Review, rebase, push — the human act

```sh
git fetch origin
git log --oneline origin/main -3
git rebase origin/main          # native FS only; fails on the Cowork mount
git push origin main
```

Non-fast-forward on first attempt is routine — the heartbeat cron pushes underneath you. Fetch,
rebase, retry. Confirm with `git ls-remote origin main`, not with the push output: a silent-publish
gap has bitten this repo before.

---

## 8 · Hygiene — safe to defer, cheap to do while you are here

**Stashes.** `stash@{0}: autostash` duplicates state that already landed in `d5397ce` — **drop it,
do not pop it.** `stash@{1}: wip-vault-mods-before-main-reconcile` holds architecture registers;
inspect with `git stash show -p stash@{1}` before deciding.

**Worktrees.** Four prunable under `.claude/worktrees/`, plus `C2A2-dev [voice-guide-v2]`.
`/tmp/c2a2_wt` is locked detached — unlock deliberately or leave it.

```sh
git worktree list
git worktree prune -v
```

**The `.git` lock museum.** `index.lock.bak` (05-04), `index.lock.sandbox-stale` (06-19),
`index.lock.sandbox-stale-1781890114`, `HEAD.lock.stale.1784363968` (07-09), `ORIG_HEAD.lock`
(08-16), plus three files in `_to_delete/`. All 0 bytes, all inert, all evidence of Appendix A.

**Redundant root drafts.** These are sources for work that shipped in `d5397ce` — archive, do not
commit: `what_is_saying_DRAFT.html`, `whats_this_two_lenses_spec.md`, `start_here_section1_patch.md`,
`doing_structure_function_v2.md`, `doing_function_clauses_draft.md`.

---

## 9 · Cheap wins the bootstrap report costed for you

| # | Action | Cost | Payoff |
|---|--------|------|--------|
| 1 | Paste the 26-line alias generator | 30 s, reversible | closes **58%** of broken links, all targets verified |
| 2 | Add `node_modules` to the weekly agent's exclusion set | one line | removes 97 phantom orphans; stops `npm install` moving the curve |
| 5 | Split `connectivity_log.csv` into curated/machine columns, or insert a break-marker row | small | the series has spent two months measuring `lit_search_results` growth and reporting it as disconnection |

The structural one is **generator asymmetry**: `architecture/lit_search_results` has produced 2,391
pages and **one** wikilink; `vault/synthesis` has produced 307 pages and **1,143**. Two generators
in the same vault, three orders of magnitude apart in whether they wire their output in. No orphan
sweep can close that — it is fixed at the generator, by having each producer emit at write time the
one or two links it already knows about.

---

## 10 · Holds — not this pass

- `commentary-apparatus/` — reconcile (step 3) still outstanding
- Appendix G Stage 1 — stage, do not publish
- Summa publish repo — `.summa-publish.git` still sits at its single "Initial public commit" with a
  corrupt index; its own session, its own runbook
- `test_voice_shell.cjs` (329 rows) has never run — its `CHROME` const is a hardcoded macOS path.
  You are on the Mac now, so it will run. A `process.env.CHROME` override closes the hole for good.

---

## Appendix A · The Cowork lock hazard

`git status` on the mounted repo leaves a **0-byte `.git/index.lock`** behind, because the mount
forbids the unlink. Confirmed twice on 08-23 and 08-24, each stamped at the exact minute of a read.
Always clear it before ending a Cowork session on this repo:

```sh
L=.git/index.lock
[ -f "$L" ] && [ ! -s "$L" ] && mkdir -p _to_delete && mv "$L" "_to_delete/index.lock.cowork-$(date +%s)"
```

Only ever move a **0-byte** lock. A non-empty lock, or a live holder, means a real write is in
flight — leave it. Use `mv`, never `rm`: the mount refuses deletes.

This is *not* what killed last night's sync — that holder was live, with a real PID, almost
certainly the 20:03 bootstrap run still working. Two different problems wearing the same symptom.

---

## Appendix B · One decision only you can make

Ten consecutive runs of the sewing agent have disclosed the same Rule 6 breach and none has
changed anything:

> *"No run of this agent has ever been within budget, and the SKILL's protocol and the CLAUDE.md
> budget are not compatible as written. Recommend scoping the budget per interactive session and
> exempting scheduled agents, or deriving the batch cap from the budget rather than from a page
> count."*

Disclosure without remedy is where a good rule goes to become decoration. Either amend CLAUDE.md
or amend the agents — but the fourth cycle of citing Rule 12 about breaching Rule 6 is not a
third option.
