# Cowork Progress Summary — 2026-09-14
*Generated at 18:40 EDT for daily walk Chat context*

> ## ⚠ DELIVERY FAILED — read this file directly
>
> **This summary was NOT delivered to the daily walk Chat conversation.** Two routes were tried at
> 18:41 EDT and both are down:
>
> 1. **Claude in Chrome:** `tabs_context_mcp` returned "Claude in Chrome is not connected" on two
>    consecutive attempts — the same failure the 08:52 inbound sync hit. Extension not installed,
>    Chrome not running, or side panel not signed in as `thomas.loughran@gmail.com`.
>    Extension: https://chromewebstore.google.com/detail/fcoeoabgfenejglbffodgkkbkcdhcgfn
> 2. **Built-in browser pane (fallback):** `claude.ai` loaded this time — the site grant is no longer
>    the blocker — but the pane's browser profile **is signed out**, landing on the sign-in page.
>    Signing in is not something an unattended run may do. Aborted rather than proceeding.
>
> **New information vs. the morning notice:** the browser pane can now reach `claude.ai` without a
> per-site approval. The only remaining obstacle on that route is that its profile has no session.
> **Signing the pane in once, by hand, would repair the outbound leg permanently** — that is a
> cheaper fix than reconnecting the Chrome extension, and it is now the shortest path to closing a
> sync gap standing at six days outbound / twelve inbound.

> **Inbound sync was down again this morning.** `2026-09-14_chat_summary.md` (08:52) is a failure
> notice, not a summary — Claude in Chrome not connected, browser pane refused `claude.ai` for want
> of a site grant. **Twelfth consecutive day with Channel 3 deaf.** Nothing in today's Cowork work
> carried over from a walk conversation, because no walk conversation was readable.

## What Was Accomplished Today

**Two distinct bodies of work: the overnight automated pipeline (00:47–04:40), and an interactive
session late morning (11:28–11:46).**

**Overnight — the lit-search pipeline ran a full FOR/AGAINST cycle on six items and the cycle
indicted itself.** Agents 15a/15b searched PRESUMPTION-982, -983, -988, -989, -991 and
ASSUMPTION-1369 — the complete 2026-09-13 evening intake cohort, not a sample. Agent 15c found that
**all six were already answered by ACTIVE premises the intake pre-check failed to find.** Twelve
literature searches produced zero new premises. This was filed as a **SYSTEMIC-RISK FLAG (High)**
and adopted as DISPOSITION-963 / PREMISE-205 / REVISE-474.

The flag's decisive datum does not depend on judgment: **PREMISE-116 contains the word "Propagation"
twice inside the two sentences the PRESUMPTION-989 intake states it grepped `propagat` for.** The
pre-check was contradicted by its own stated command — discoverable only because that one intake
happened to record the command. Structural cause: **the pre-check searches the register by topic
keyword while the register indexes premises by inference type.** Six ACTIVE premises cover
ASSUMPTION-1369; not one contains the word "stale." The register is ~700 KB and 205 premises and
has outgrown the instrument used to search it. Combined with 2026-09-13's three-of-five, the rate is
**nine of eleven across two consecutive complete cohorts.**

Five new pending proposals were filed (3 Levin, 2 Friston). The review page
`2026-09-14_review.html` was generated at 04:37 and the master wiki rebuilt at 04:40.

**Late morning — the RC Sandbox got a front door, and the leak that published it was closed.**
`wiki/rc_sandbox_notebook.html` was promoted out of the inbox thread to a stable path and registered
as the fifth Education tool in `explorer.html` in all three places convention requires (row2-edu
button, `showHelp()` description, search-keyword registry). Two defects were fixed in the promoted
copy only: missing `<!DOCTYPE>` (measured BackCompat quirks mode) and missing `<meta charset>`
(mojibake under `python3 -m http.server`). Verified in Chromium against the staged tree: standards
mode, 2,191 cells, 43 outline links, 0 page errors, RC Document Explorer unaffected as control.

The underlying leak: `commit_daily_run.sh`'s mtime authorship window swept `wiki/inbox/rc_sandbox/`
into commit `91bb78b` (2026-09-05), and `pages.yml` publishes the repo root — so the corpus, the
Quodlibet Notebook and a 13.7 MB master workbook **have been served publicly from
tloughran.github.io since 09-05**. `COMMIT_ME_2026-09-14.sh` untracks the workbook and carries
forward the three unrun guard fixes from `COMMIT_ME_2026-09-07.sh`.

Agent 16's daily pass ran clean: 0 checks due, 0 run, 1 active item (WATCH-003), and — for the first
time in twelve days — yesterday's filings were clean, with a real base rate at last (three Rohr
cards, full deferral vocabulary grepped, zero matches).

## Key Decisions Made

- **No new DECISION id minted. DECISION-083 still stands — sixth consecutive day.** The designer's
  last recorded speech act in the review channel is now thirty-seven days back.
- **Ratified (yours, today, recorded in the commit message):** the RC Sandbox corpus is published
  and should have a front door. The 13.7 MB workbook is untracked; the corpus stays.
- **Agent-made, id-less, recorded so the distinction stays visible:** DISPOSITION-963 adopted
  PREMISE-205 at Moderate confidence and raised REVISE-474 — a schema change to the intake gate,
  made by the pipeline about itself.

## New Open Questions

No new OPEN-NNN ids were minted today; OPEN-209 (2026-09-13) remains the most recent. But REVISE-474
carries three unowned recommendations that function as open questions:

1. **Pre-check records the command run AND the premise IDs returned, not a conclusion.** Recommended
   2026-09-13, not adopted, restated 09-14 as a schema forcing function.
2. **Calibration loop — one pass, runnable today.** Take the last N intake items claiming "no
   covering premise," re-run each stated grep, record the hit count.
3. **A standing inference-type term list alongside topic terms.**

**OWNER: unassigned** — on a flag whose second finding is that unassigned remedies are not remedies.
The 2026-09-13 flag carried the same sentence and the same empty field.

## Files Created or Modified

- `architecture/lit_search_results/against/SYSTEMIC-RISK-FLAG_2026-09-14_pre-check-instrument-fails-silently_982-983-988-989-991-1369.md` — the day's most important artefact
- `architecture/lit_search_results/{for,against}/` — 12 search reports (982, 983, 988, 989, 991, 1369)
- `architecture/validated_premises.md` (PREMISE-205), `lit_search_returns.md`, `for_lit_search.md`, `monitor_queue.md`, `revision_flags.md` (REVISE-474) — all backed up pre-15c
- `wiki/rc_sandbox_notebook.html` (new, promoted), `wiki/explorer.html` (three-site registration)
- `wiki/inbox/rc_sandbox/COMMIT_ME_2026-09-14.sh` (supersedes the unrun 09-07 script)
- `inbox/proposals/pending/` — 5 new cards (Levin ×3, Friston ×2)
- `review/2026-09-14_review.html`, `review_log.html`, `level2_signal_stream.html`, `master/C2A2_master_wiki.md`
- `deferred/watch_list.md` (Agent 16 run), `agents/openstory/` telemetry + `agents_tab.html` (REFRESH_STATUS PASS, 33 agents, DB age 0h)

## Pipeline Status

- **Intake items total: 1,723** — 883 assumptions (14a), 840 presumptions (14b)
- **Lit search queue: 157 awaiting search · 16 searched but not dispositioned · 2,066 dispositioned**
- **Validated premises: 205** (PREMISE-205 filed today, at Moderate confidence, by the pipeline about itself)
- **Deferred items watching: 1 active** (WATCH-003, 10 checks, next on-cadence 2026-09-15)
- **Proposals:** pending 8 · approved 414 · denied 1 · needs_review 1 (tombstone)
- **Review-pass gap: 5 days** · **Ingest gap: 2 days** · `PROCESSED_LOG.md` unchanged at 1,159 lines
- **Network:** 867 PRS triplets · 108 CROSS entries · 91 distinct FINDING ids — unchanged since 09-12
- **Rulings owed: twenty-one**, one answered without being ruled (OPEN-196)

## What's Next

1. **Run `COMMIT_ME_2026-09-14.sh` on the Mac.** It is written, superseding, and unrun. The sandbox
   cannot write `.git` and the mount forbids unlink, so nothing here can execute it. The tree is
   already one commit ahead of origin (`975bc7f`); your push sends both. **The 13.7 MB workbook
   stays publicly served until this runs.**
2. **The calibration loop (REVISE-474 item 2)** is the cheapest high-value item on the board — one
   pass, re-run N stated greps, count hits. If the contradiction rate is materially above zero, every
   standing claim in the queue is uncalibrated.
3. **`review/2026-09-14_review.html`** now carries the whole queue. Two cards in the 09-13 page were
   self-declared retrieval instructions; an en-bloc APPROVE is the twelfth and thirteenth leak.
4. **WATCH-003 on-cadence check fires tomorrow (2026-09-15)**, eleventh.
5. **DEFERRED-CONDITION LEAKAGE ruling — deadline 2026-09-24, now ten days.**

## For Morning Discussion

**One thing dominates, and it is not the sandbox work.**

**The pipeline spent a full cycle establishing that it cannot search its own register, and then filed
that finding into the register it cannot search.** The flag names this itself — "produced by the
pipeline it indicts, from evidence gathered by that pipeline's search stage, checked by that
pipeline's dispositioner, in an estate with no external arbiter." PREMISE-096 says that is not
certification. That is a MacIntyre-shaped problem about a tradition's internal standards of
rationality showing up as a grep failure, and it may be the most interesting thing the estate has
produced about itself. **Worth the walk.**

Three concrete asks that need one line each from you:

- **Who owns REVISE-474?** Two consecutive flags have carried the same empty OWNER field and the
  same sentence about unassigned remedies not being remedies.
- **The claude.ai `scope: site` grant for the browser pane.** Sixth consecutive day outbound down,
  twelfth inbound. Every morning summary since 09-03 is a failure notice, and one of them wrongly
  directs sessions to treat an earlier failure notice as context.
- **The public-workbook question has two halves.** Untracking stops it being served; a history
  scrub is a separate decision the commit message deliberately leaves to you.

One item worth naming because it bears on the above: the estate has now spent **fifteen consecutive
days generating exclusively agent-stated items with the designer's sync channel down in both
directions** — which is, on its face, one of the observables the Sole/Krakauer/Levin dependence
reading predicts (OPEN-208). The pre-registration that would make that measurable is still unwritten,
and the instrument that would measure it — the metabolism snapshot — has been frozen since 09-03.
