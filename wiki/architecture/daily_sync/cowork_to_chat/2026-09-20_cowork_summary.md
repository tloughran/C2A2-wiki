# Cowork Progress Summary — 2026-09-20
*Generated 18:39 EDT for daily walk Chat context*

> ## ⚠ DELIVERY TO CHAT FAILED — read this file directly
> Neither browser path was available. **Read this file on the walk instead of expecting it in Chat.**
> This file is the primary deliverable and is complete.
> **No interactive Cowork session ran today.** Everything below is scheduled-agent output.
> Today's `chat_to_cowork` summary also **failed** (morning scrape: Chrome extension not
> connected; built-in browser signed out). So today has no Chat→Cowork *and* the agents ran
> without any walk context. That is the **eighteenth consecutive day** of the sync blind spot.

## What Was Accomplished Today

Sunday: no human session, six scheduled agents. Three findings are worth the walk.

**1. The sewing-agent bootstrap audit found the instrument contaminating its own measurement.**
Re-running the census twice — once counting everything, once excluding its own report series as a
link source — showed **34% of the vault's broken wikilinks (137 of 403) live inside sewing-agent
reports**, because a quoted `[[Friston]]` *is* a wikilink. The 09-13 report alone contributes 31,
making it the single largest source of broken links in the vault. The rising curve the series has
reported for four weeks (281 → 328 → 371 → 403) is partly the reports themselves.
**Clean rate, instrument excluded: 11.0% (266/2,416), not the reported 15.8%.**

It also **withdrew last week's recommendation 3**: the claim that your RC Sandbox marginalia were
"growing" from 8 to 13 dead links was a false alarm. The corpus files are byte-untouched since
09-05 and still hold exactly 8 links across 4 targets. The five "new" ones were the 09-13 report
quoting the four marginalia. Nothing is re-emitting anything — **do not go hunting that transform.**

**2. The weekly sewing run's best output is a bridge that got weaker on purpose.** The Stump paper
(*Natural Law, Metaphysics, and the Creator*) argues **formal causation and level-specific causal
power**, not final causality — the word "teleology" does not occur, and this is the third source in
which she does not say it. CROSS-008 restated from final → formal is narrower in scope and stronger
in support. Three days earlier and independently, the Levin/Cervera microRNA card reported a
bioelectric–transcriptional loop in which **neither layer is upstream** — a mechanism for the weak
claim. The network's instinct would have been to defend the strong version, and that instinct would
have cost it the evidence.

**3. A 223-day detection lag, measured.** Hoffman and Friston spent 2h40m in one room on
2026-02-04 negotiating at the level of formalism — a homomorphism on the table — whether trace
logic and the FEP describe the same structure. That is precisely the event the accelerator exists
to produce, it was produced by a podcast host, and the wiki noticed on 09-15. `traditions/friston/`
has no record of the source at all. The test for whether this was bad luck is cheap: enumerate the
91 pairs among the fourteen thinkers, sweep public long-form venues for 24 months. Retrieval
watches each thinker's *own* channels; a joint appearance lives on neither.

## Key Decisions Made

**None. No DECISION minted — DECISION-083 (2026-08-27) stands, 24 days attended.**
Review-pass gap is **10 days** (`review/archive/` latest is `2026-09-10_decisions.md`).
Last decision-channel act: the `[C2A2-review-decision]` email of 09-09 — **11 days**.

Agent-made, id-less rules recorded rather than minted continue to accumulate; today's
`decisions.md` index note tail still ends at the 09-17 entry, so today added none to the index.

## New Open Questions

**None raised today.** Register stands at OPEN-244 (four raised 09-19: 241–244).
**OPEN-244 still needs you** — is the scheduled-task sandbox the right substrate for tasks whose
inputs grow without bound? It got a third data point today: the OpenStory refresh failed again at
12:20Z, `OSError: [Errno 28] No space left on device`, 7.0 GB DB against 2.5 G of scratch. Third
consecutive failure on the same wall; `node_edges` now 3 days stale.

## Files Created or Modified

57 files touched, all agent-written:

- `architecture/sewing_agent_bootstrap_2026-09-20.md` — the instrument-contamination audit (§0 above)
- `architecture/sewing_agent_log.md` — weekly run: 10 pages sewn, **61 agentic calls** across 14
  thinkers, **16 bridge notes** (two seeding previously-empty files: `hoffman_loughran`,
  `kastrup_loughran`)
- 16 × `synthesis/*_bridge.md`
- 10 × `inbox/proposals/pending/*.md` (sewn)
- `architecture/metrics/connectivity_log.csv` — row `2026-09-20,4287,744,86,5117`
- `architecture/for_lit_search.md` + `monitor_queue.md` — 15d cycle-1 re-trigger pass (with `.bak`s)
- `deferred/watch_list.md` — Agent 16 run summary
- `inbox/proposals/pending/2026-09-20_rohr_*.md` ×2 — new Rohr cards
- `review/2026-09-20_review.html`, `level2_signal_stream.html`, `review_log.html`, `agents_tab.html`

## Pipeline Status

- Assumptions extracted: **862 distinct** ASSUMPTION ids
- Presumptions surfaced: **988 distinct** PRESUMPTION ids
- Lit search queue: 2,813 QUEUED tags / 4,160 SEARCHED / 2,088 DISPOSITIONED; **7 items QUEUED
  with no search at all**; 15d re-triggered **14 MONITOR items at cycle 1** today
- Monitor queue: **372** MONITOR entries
- Deferred items watching: **1** (WATCH-003 — stale since 08-25; next on-cadence check 09-22, count 11)
- Validated premises: **170 total, 159 ACTIVE** (100 past `Re-check due`, 19 carry no due date)
- Proposals: **pending 27** · approved 414 · denied 1 · needs_review 1
- PRS network: **867 PRS** across 15 tradition files · 135 CROSS ids · 90 FINDING ids (24 Active) —
  **frozen since 09-11**, correctly: nothing can move until a decision arrives
- Ingest: **ninth consecutive zero-yield day**; ledger `total=414 ingested=382 decided-zero=30 OPEN=1`

## What's Next

**The binding constraint is the review queue, not the sweep.** The daily run's own words: "27
proposals span 09-11 to 09-20 with no decision since 09-09 — eleven days. The agents are not short
of material; they are short of decisions." Retrieval is running at ~3 cards/day into a blocked
review step — the shape of problem that looks healthy in every metric until the backlog is
unmanageable.

Immediate, in order of deadline:

1. **LEAKAGE ruling — due 2026-09-24, four days.** Option (b) is one line.
2. **WATCH-003** next on-cadence check 09-22 (twelfth identical check). One retroactive line on the
   INTEGRITY FLAG closes it.
3. **MONITOR-609/-610 and MONITOR-403** fall due 09-21; MONITOR-547/-548 on 09-25.
4. **Monthly INCORPORATED premise re-check** did not fire (day 20) — 100 ACTIVE premises past due.

## For Morning Discussion

**1. The leakage ruling, before Thursday.** Cumulative count is **sixteen**. Five leak-shaped cards
sit on the 24-card page *right now* — PROP-2026-09-11-001, -09-12-001, -09-14-004, -09-16-002,
-09-19-001. **An en-bloc APPROVE swallows all five.** Agent 16 also corrected its own record today
per Rule 12: the "three on the page" figure it carried for three straight runs was wrong — it was
four, and is five — because it restated the number from the flag's text instead of re-deriving it
from the artifacts. Worth a minute on the walk: that failure mode is generic, not Agent-16-specific.

**2. Approve `youtube.com` for the browser pane — one approval unblocks two stuck retrievals.**
`vshC_TxwrVo` (Wright, **eight** consecutive failures) and `zF5enEPkoNA` (Wolfram). The Wolfram path
has now failed **three times running** — YouTube renders descriptions via JS, so `web_fetch` returns
an empty body, and a scheduled run cannot obtain a site approval. This is infrastructure, not
tradition, and it is costing Wolfram its primary feedstock at the exact moment he named a new
Institute-level research programme — the first since the Physics Project.

**3. Gated sources are biasing the sample, not just shrinking it — third consecutive flag.** Three
of Kastrup's last five captures and two of McGilchrist's now carry gated caveats, and what sits
behind the walls is disproportionately the **unrehearsed** material: members' Q&As, live sessions,
where a thinker answers questions they did not frame. What stays free is the lecture and the
broadcast interview. Three defensible options — budget the memberships (bounded, probably small),
adopt a documented no-gated-sources policy, or set a hard confidence ceiling on gated material.
**The status quo is a fourth option nobody chose.**

**4. Stop reporting a single orphan count — thirteenth flag, now escalated.** `architecture/`
supplies 3,348 of 4,287 orphans (78%), `inbox/` another 796; together 96.6% of the headline, almost
none of it content a human will ever link. The *curated* vault's real orphan population is ~143
pages and has been improving for weeks, invisibly, behind a number that rises no matter what the
agent does. Twelve identical recommendations produced no action, so the agent has stopped re-filing
it: split the CSV into `curated_orphans` / `machine_orphans`, or exclude `architecture/` by rule and
say so in the header — or delete the column.

**5. OPEN-244 (sandbox substrate) got its third data point.** Two tasks died on this wall 09-19;
OpenStory died on it again today. Every proposed fix so far has been scoped to its own task and no
run has named another's failure. The estate already made this move once — the daily-run commit step
went to launchd on the Mac for exactly this reason. Architectural call, not a command.

**6. Two smaller ones.** The Rohr specialist files Saturdays against the *closed* week's summary, so
the current week is structurally invisible to it — OPEN-243 asks which *other* specialists have the
same shape of hole, and it is one table and one afternoon to answer for all fifteen at once. And
the run-log archival split is at its **fifteenth** consecutive recommendation; `watch_list.md` is now
~711 KB / 6,000 lines. Agent 16 will act on one word.

**7. Fix the Chat sync itself.** Eighteen days blind. Either install/sign in the Claude in Chrome
extension, or sign in once to claude.ai in the desktop app's built-in browser pane — its profile
persists, which would give both the morning scrape and this evening sync a working path.

## Unrelated: connector health

Need re-authorization (OAuth, interactive session required): Atlassian, Figma, Intercom, Linear,
Notion, Slack, Datadog. Failed to connect ("does not support dynamic client registration"): Asana,
GitHub, PagerDuty.

---

**Delivery: FAILED — 2026-09-20 18:42 EDT.** Both paths attempted, both dead:

1. **Claude in Chrome** — `list_connected_browsers` returned `[]`. No extension instance is
   connected to this account. Same condition the morning scrape hit at ~08:52.
2. **Built-in browser pane** (fallback, not in the skill) — opened `claude.ai/recents` fine, but
   the pane's profile is **signed out**; it landed on the sign-in page. Signing in is not an action
   an unattended run performs, so the attempt stopped there.

**Both of today's syncs therefore failed in both directions** — the morning `chat_to_cowork` scrape
and this evening `cowork_to_chat` delivery, for the same two reasons. That is the **eighteenth
consecutive day** of the blind spot Agent 16 carries as open item 8.

**One fix closes all of it:** sign in to claude.ai once in the desktop app's built-in browser pane.
That profile persists across sessions, which gives both scheduled tasks a working path without
requiring Chrome to be running. (The Chrome extension route also works if preferred:
https://chromewebstore.google.com/detail/fcoeoabgfenejglbffodgkkbkcdhcgfn)
