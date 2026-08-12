# Sewing Agent — Bootstrap Audit Verification Run

**Run date:** 2026-08-09 · **Mode:** autonomous (Tom not present) · **Type:** verification + two new measurements, one prior-report correction. Not a re-execution.

## Why this is again not a full re-run

This ONE-TIME bootstrap task has now fired **seven times** (2026-06-23, 06-28, 07-06, 07-12, 07-26, 08-02, today). The baseline stands: full census at `architecture/metrics/bootstrap_backlink_census_2026-06-28.md`; classification and Phase 3/4 disposition in `architecture/sewing_agent_bootstrap_2026-06-28.md`; a live weekly `c2a2-sewing-agent-weekly` pipeline owns `connectivity_log.csv`.

Deliberately NOT written (fail-loud, not silent skip):

- **No new census file.** A structurally identical 300 KB file is clutter, not measurement.
- **No `connectivity_log.csv` row.** The weekly agent owns that file; a second row from a different in-memory resolver adds noise to the trend line. (Note: the live CSV header is `date,orphan,sparse,connected,total`, not the header this SKILL.md specifies. The SKILL is the stale one.)
- **No agentic-call injection, no synthesis stubs.** Phase 3 as written would modify ~1,300 files in a repo governed by the no-blind-push rule, with no human present to review.

## Verification census

Method: in-memory, path-aware `[[wikilink]]` resolution, `node_modules` and `.obsidian` excluded. **Methodology check passed** — the resolver reproduced the baseline top-hub list exactly (`friston/prs_triplets.md` 150, `stump` 121, `levin` 96, `fredrickson` 82, `kastrup` 70), so the deltas below are real movement, not resolver drift.

| Metric | 06-28 baseline | 07-26 | 08-02 | **08-09** | Δ since 08-02 |
|---|---|---|---|---|---|
| Total pages | 3,031 | 3,666 | 3,806 | **3,994** | +188 |
| Orphan (0 backlinks) | 2,337 | 2,953 | 3,093 | **3,281** | +188 |
| Sparse (1–2) | 647 | 657 | 657 | **657** | 0 |
| Connected (3+) | 47 | 56 | 56 | **56** | 0 |
| Wikilinks parsed | 1,836 | 2,071 | 2,071 | **2,116** | +45 |

Distribution: 0 → 3,281 · 1–2 → 657 · 3–5 → 20 · 6–10 → 11 · 10+ → 25.

**Headline, second week running: every one of the 188 new pages is an orphan.** The sparse and connected buckets have not moved a single page in two weeks. The top-hub counts are identical to the digit.

The +45 wikilinks are not good news either — see the broken-link section below. No new link landed anywhere that changed a page's bucket.

Growth source for the +188: `architecture/lit_search_results` 1,996 → 2,082 (+86), `inbox` 582 → 652 (+70), `architecture/daily_sync` 167 → 181 (+14), remainder ~18 scattered across `architecture/`.

## NEW FINDING 1 — the Summa corpus is 307 closed two-page islands

Last week's report identified the 307 `vault/synthesis/Day-NNN … Contemporary.md` pages as the richest under-connected material in the vault, at "1–2 backlinks, almost certainly one from an index page."

**That guess was wrong, and the truth is worse.** Tracing the actual link:

- All 307 Contemporary pages have **exactly 1** backlink. Not 1–2. Exactly 1.
- That backlink is **not** from an index. It comes from the page's own paired transcript, `vault/transcripts/Day-NNN … .md`.
- Each of the 307 transcripts has **exactly 1 outbound wikilink** — to its Contemporary twin — and nothing else.
- 306 of the 307 transcripts have exactly 1 backlink (from that twin); one has 0.
- **No index, hub, or tradition page links either half.** Grepping for any inbound reference to a sample pair returns only the two files themselves and this audit's own prior reports.

So `vault/` — 614 pages, **15% of the whole vault** — is not sparsely connected to the knowledge graph. It is **307 disconnected dyads**, each a closed loop of two pages pointing at each other and at nothing else. On a graph-connectivity measure they are indistinguishable from orphans; the "sparse" classification is an artifact of the twin link.

This matters because these are the pages that cite 9–10 of the 14 thinkers apiece, in prose, by name — and they are `git`-active: the daily `sync_vault.sh` rewrote 282 of the 307 since 08-02 (commits `1b4f2bb`, `f19f2b3`, `e2b0035`, 74–117 files each). **The sync is actively maintaining content it never wires in.** Every day it runs, the islands get better written and stay islands.

This is the single highest-value connectivity target in the vault, and it is bounded: 307 pages, already written, needing inbound links from 14 tradition hubs.

## NEW FINDING 2 — 106 broken wikilinks are bare thinker names

First broken-link measurement taken by this audit. Of **2,116** wikilinks vault-wide, **188 (8.9%) do not resolve**, spread across 42 distinct targets.

**106 of those 188 (56%) are references to the thinkers themselves**, in 24 spelling variants:

| Target | Count | | Target | Count |
|---|---|---|---|---|
| `[[Friston]]` | 12 | | `[[Wolfram]]` | 5 |
| `[[Kastrup]]` | 12 | | `[[Steven Wolfram]]` | 5 |
| `[[Karl Friston]]` | 8 | | `[[Stump]]` | 4 |
| `[[Tom Loughran]]` | 8 | | `[[Hoffman Agent]]` | 4 |
| `[[Levin]]` | 8 | | `[[McGilchrist]]` | 3 |
| `[[Hawkins]]` | 6 | | `[[Bernardo Kastrup]]` | 3 |
| `[[Hoffman]]` | 5 | | + 11 more variants | 18 |

Broken links by source directory: `inbox/` 76, `agents/` 31, `architecture/` 24, `master/` 23, `flags/` 12, `session-archive/` 9.

The cause is mechanical: there is no `Friston.md`. The hub lives at `traditions/friston/wiki.md`, so every bare-name link dead-ends. **The fix is 14–24 one-line alias notes** (`Friston.md` containing a redirect to `traditions/friston/wiki.md`, and so on for each variant). That single change would convert 106 dead links into live inbound edges — more new connectivity than the entire vault has produced in five weeks.

The remaining 82 broken links are mostly template placeholders (`[[wikilink]]` ×28, `[[Agent Name]]` ×15) and are noise, not error.

## Category breakdown

Orphan + sparse pages (3,938), classified by deterministic path/size heuristics — the model was not used for this, per Rule 5:

| Category | Count |
|---|---|
| D structural (system/architecture; backlinks not expected) | 2,514 |
| B inbox residue | 651 |
| A/C thinker + synthesis content (`vault/`) | 616 |
| C synthesis (`synthesis/`) | 51 |
| Other (review, agents, heartbeat, traditions, flags, …) | 106 |

## Carried-over litter (verified present this run)

- **Metric inflation — seventh consecutive flag, still unactioned.** `architecture/lit_search_results/` (2,082 `.md`) + `architecture/daily_sync/` (181) = **2,263 pages, 57% of the 3,994 total.** Excluding both, the census reads **1,731 pages / 1,018 orphans / 657 sparse / 56 connected** instead of 3,994 / 3,281. These machine dumps are why every report's headline is "+N orphans." Fix is one config line plus a break-marker in the series.
- **Zero-byte `*_bridge.md` stubs: 9 → 8.** `carroll_loughran_bridge.md` was populated this week. Remaining: `arkanihamed_loughran`, `carroll_hawkins`, `hawkins_loughran`, `hawkins_wolfram`, `hoffman_loughran`, `kastrup_loughran`, `loughran_mcgilchrist`, `mcgilchrist_wright`. Six of eight are `loughran_*` — consistent with the standing read that the set was scaffolded from a full pairwise matrix and never populated. (Of the 62 files in `synthesis/`, 29 have zero backlinks.)
- **Inbox: 652 pages, up from 582** (+70 in one week — the fastest-growing content directory). 346 in `proposals/` (301 approved, 4 pending).
- **Seven tradition hub pages** (`{arkanihamed,carroll,fredrickson,kastrup,rohr,stump,wright}/wiki.md`) all exist, 8.7–15.8 KB each, and still await the navigation fix wiring them into their child notes. They are the natural link source for both new findings above.

## Vault health assessment

**Downgraded from "affirmative" to "affirmative with one named structural defect."**

The aggregate picture is unchanged and still sound: the 14 `prs_triplets.md` hubs hold the top backlink counts, and the orphan population is overwhelmingly structural and pipeline residue rather than failed synthesis. The graph supports thinker-agent synthesis *for the tradition material*.

What changed this week is that the defect has a shape. It is not "3,281 orphans." It is that **the vault's two richest cross-tradition assets are both severed by mechanical, not editorial, causes**: 614 Summa pages sealed into closed dyads by a sync that writes no outbound links, and 106 thinker references dead-ending because no alias file exists. Neither is a content problem. Both are small, deterministic fixes. Together they are worth more than any further orphan sweep.

## Recommended actions for Tom

1. **Create the thinker alias notes.** Highest ratio of connectivity gained to effort spent in the whole audit — 14–24 one-line files, 106 links restored, fully reviewable in one sitting. New this week.
2. **Give the Summa sync an inbound-link step.** `sync_vault.sh` already rewrites these pages daily; having it also append each `Day-NNN` page to the relevant tradition hub index converts 614 island pages into graph members with no new prose. Supersedes last week's item 2, which under-diagnosed the problem.
3. **Retire or reschedule `c2a2-sewing-agent--c2a2-wiki-bootstrap-audit`.** Seventh run of a task its own SKILL.md calls "a ONE-TIME run." Fold a quarterly "delta vs. bootstrap baseline" section into the weekly agent instead. (Second time recommended.)
4. **Decide the census definition** (exclude `lit_search_results/` and `daily_sync/`, or keep them and stop reading the orphan trend as signal). Seven reports have now flagged this.
5. **Wire the seven tradition hub pages into their child notes.** Small, reviewed, and the natural landing site for items 1 and 2.
6. **Triage the 652 inbox pages** in dated batches. Growing ~70/week; it is now the fastest-growing content directory in the vault.

Empty-stub cleanup command, if you want the bridge noise gone:

```
cd "wiki/synthesis"
find . -name '*_bridge.md' -size 0 -delete
```

---

*Autonomous scheduled run. Append-only; no vault content modified. No census file, CSV row, or agentic-call injection written this run — by design, matching the 07-06, 07-12, 07-26 and 08-02 precedent. Two new measurements added (Summa dyad structure; broken-wikilink census) and one prior-report reading corrected.*
