# Agent-run issues: review and repair workflow (2026-10-01)

**Scope read:** 43 Routines (all report `SUCCEEDED`), the latest run transcript of 24 of them,
the last 30 GitHub Actions runs, and origin/main history. `SUCCEEDED` means only "the session
ran"; nearly every real problem below sat inside a green run.

**One-line diagnosis:** most C2A2 failures are fallout from moving ~32 jobs from the Mac to
cloud Routines (09-16 to 09-28). The jobs now reach the Mac through a fragile bridge
(`device_bash`), work in a small sandbox disk, and are invisible to the Mac's own watchdogs.
Meanwhile, two days of output have not reached GitHub, and nothing noticed.

Legend: **[V]** verified directly in this review, **[R]** reported by a run transcript and not
re-checked, **[I]** inference.

---

## Phase 0: today, on the Mac (about 20 min). Stops the bleeding.

### 0.1 DONE 2026-10-01 17:14Z: local `main` had diverged from GitHub; two days of output were unpublished
- Resolved by merging `origin/main` (heartbeat-only commits) instead of rebasing, then pushing `2be638ab`
  after a local HTTP review. The 09-30 cause was confirmed: `Your local changes to the following files
  would be overwritten`, meaning `wiki/vault/` Day files changed on disk mid-rebase. The writer is unidentified.
- [V] origin/main has no `C2A2 daily run` commit after 09-29 and no `Summa vault sync` after 09-29.
- [R] Scheduler health: daily-run step "committed 2026-10-01 09:45Z" (locally). `commit_daily_run.sh`
  never pushes, by design.
- [R] `com.tloughran.summa-vault-sync` hit a **rebase conflict 2026-09-30 22:00:27, aborted**, kept
  its local commit, and pushed nothing. Tonight's 22:00 sync will hit the same wall.
- [I] Local main is now ahead by at least 3 commits (daily run 09-30, daily run 10-01, vault sync 09-30).

Inspect first. These commands are read-only:

```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
git fetch origin
git status -sb
git log --oneline origin/main..main
git log --oneline main..origin/main
tail -n 40 sync_vault.log
ls -la sync_vault.FAILED
```

Then, with Claude in a local session: resolve the conflict and do the local HTTP review
(per the no-blind-push rule). Push only after sign-off. Tonight's sync depends on this.

### 0.2 Security: Supabase API-key functions callable by anonymous users (DONE 2026-10-01 17:19Z: migration `lock_broker_functions_to_service_role` applied and verified)
- [V] 9 `SECURITY DEFINER` functions are executable by `PUBLIC` (so `anon` too): `get_byo_key`, `store_byo_key`,
  `get_usage`, `get_web_usage`, `get_rt_usage`, `increment_usage`, `increment_web_usage`, `increment_rt_usage`, `ip_hit`.
- [V] The only caller is `cc-broker`, using the service-role key. `plan_recall`/`plan_store` already
  carry the target grants (`postgres` + `service_role` only). The fix revokes `PUBLIC`/`anon`/`authenticated`.
- [R] 9 `SECURITY DEFINER` functions are exposed to `anon`/`authenticated` over REST, including
  **`get_byo_key` and `store_byo_key`**. Leaked-password protection is off. 7 tables have
  Row-Level Security on but no policies (default-deny, so probably safe; confirm).
- Action: revoke `EXECUTE` from `anon` on those functions, or move them out of the exposed
  schema. A cloud session with the Supabase connector can do this as a reviewed migration.
  The `ND sociogram security review` Routine created today is a natural owner.

### 0.3 DONE 2026-10-01 20:54Z: Live dashboard refresh was stuck on an approval prompt
- Root cause: the prompt updated a Cowork artifact on the Mac (`mcp__remote-devices__*`), which cloud runs cannot reach,
  so each run fell back to publishing a new page and waited for approval. The prompt now reads and republishes
  one fixed claude.ai artifact (`UJxiePX1rbekwncDySfvw7`) in place, with no Mac link. The stuck session is archived.
  Watch: the first unattended run (Fri 07:00 ET) may still pause on publish approval.
- [R] Waiting since 11:18Z on an `Artifact` publish approval. The content was already delivered
  to you. Approve or deny it in the app to release the run.

---

## Phase 1: repair the cloud-move plumbing (root causes; one session each)

| # | Issue | Evidence | Fix direction |
|---|---|---|---|
| 1.1 | `device_bash` bridge wedges | [R] Janitor 09-27 and sewing 09-27 did not run at all (5 failures each, even on `true`); periodic monitor, connector health, commentary reviewer and morning health were degraded | Make Desktop Commander the stated fallback in every prompt, or fail loud with one notification; find the contention (suspected concurrent MCP) |
| 1.2 | Sandbox disk too small for the 7.5 GB `open-story.db` copy | [R] Telemetry refresh died with ENOSPC; morning health died the same way; daily-run Phase 5.6 `mktemp` ENOSPC on 09-30 | Run the extractors **on the Mac** via the bridge, or read the db in place (read-only) instead of copying it |
| 1.3 | Metabolism regen cannot find the db | [R] `db not found: /sessions/.../Documents/Non-Claude Projects/OpenStory/...`: `~` resolves to the sandbox home | Pass an absolute Mac path, or run it on the Mac. Note that OpenStory moved to `Non-Claude Projects` [R] |
| 1.4 | Watchdogs blind to the cloud | [R] run_stall FAIL daily since 09-20 ("no transcript after 09-15"); 32 tasks are "moved to cloud, cannot tell if it fires"; morning status sees 20 tasks; self-awareness has no `list_sessions` (3rd day) | Feed `check_scheduler_health.py` from the Routines API (`last_run`), not the Mac registry/transcripts |
| 1.5 | No watchdog compares local main with origin | [V] 0.1 went unflagged by every watchdog | Add an artifact row: "newest `C2A2 daily run` commit on **origin** <= 26h old", and a `main...origin/main` ahead/behind check |
| 1.6 | Pages deploy check cannot fetch | [R] All 3 WebFetch calls returned `PROVENANCE_REQUIRED` unattended; an older note says Pages is "wedged" | Use the GitHub Actions API (Pages runs **are** green through 09-30 [V]) or pre-approve the domain. The "wedged" diagnosis looks stale [I] |
| 1.7 | Duplicate firings | [R] The daily run fired twice on 10-01; the repeat re-stamped run-start, which skews the 45-min authorship hold. Mh inbox double-fired on 09-30 and is now disabled (reason unknown) | Make the run-start stamp write-once per day; check for a duplicate Routine or a Mac and cloud overlap |

## Phase 2: rebuild stale C2A2 artifacts (after Phase 1, so they stay fresh)

- [R] **Agent telemetry / Agents tab**: not refreshed 10-01 (needs 1.2).
- [R] **Metabolism**: last publish 09-27, regen failing (needs 1.3).
- [R] **PRS connectome** `prs_3d.html`: built 09-25; the template changed 09-29.
- [R] **Janitor**: newest findings 09-20 (337 broken wikilinks; community_explorer count 156 vs 155).
  Re-run by hand once 1.1 is fixed. Sewing agent likewise.
- [R] **Level-2 signals**: newest signal 2026-09-23 (`stale_days 8`). Check whether upstream is quiet or extraction is broken.
- [R] **Voice-shell suite RED**: 12/371 at `bd1f7de` (09-28). Commits since then cite 7 known "pending" rows,
  so 5 rows are unaccounted for. Run `bash scripts/check_voice_shell.sh --force`.
- [R] `com.tomloughran.openstory.ui` launchd agent exits 127 (command not found); likely the
  OpenStory folder move [I].
- [V] Leftover `stash@{0}: autostash` on the Mac holds 12 files of unrestored work (`metabolism_data.json`,
  `metabolism_view.html`, `start_here.html`, `voice_guide/manifests.json`, ...). Inspect it; do not drop it blind.
- [R] Sociogram: 23 KSGA references still in `wiki_narration.html`; regen via `regen_sociogram.sh`.

## Phase 3: decisions only you can make (batch them in one sitting)

- DEFECT-I: escalated 18 straight runs; about 353 items wait on it.
- Wright PROP-2026-08-14-033: approved but OPEN since August.
- 12 pending proposals (oldest: Fredrickson PROP-2026-09-24-001, 7 days); `pending/` holds 11 cards.
- INTEGRITY FLAG ruling; WATCH-003 (stale since 08-25).
- Held paths since 09-27: `wiki/inbox/rc_sandbox/COMMIT_ME_2026-09-07.sh`, `cell_dates.json`.
- Summa: Day-076 transcript-drift hold; Day-086 "Friston's PRS" wording; Day-129 single voice;
  Day-212 tier mismatch; 257 length violations.
- Retire `summa-2026-daily-batch`? 307/307 done, 16 consecutive no-op runs.

## Phase 4: lower priority / non-C2A2

- Summa qc sweep prompt bug: `qc_sweep.py --max 6` should be `report --max 6` (fails every run).
- Mh master sent a false "could not complete" alert and did not retract it.
- Connectors needing re-auth: Composio, Wolfram; Gmail was flaky through 09-30.
- Cost tracker cannot write local Reports without "Require this computer"; pipeline about 6 months stale.
- GitHub Actions on deprecated Node 20 (`checkout@v4`, `setup-node@v4`, `setup-python@v5`).
- Mac swap at 7.4/8 GB; 6 stranded git `tmp_obj` files from 09-15/16.
- Lit-search: about 150 bare `[QUEUED]` items untouched.
- [V] Not an issue: heartbeat failure on 09-23 was a one-off GitHub 500 on push and has self-healed.

---

**Gaps in this review:** for each Routine I read only its latest run, not earlier runs.
`scheduler/*.md` and `held_paths.md` live on the Mac and were not readable from the cloud.
No [R] item has been re-verified on the Mac.
