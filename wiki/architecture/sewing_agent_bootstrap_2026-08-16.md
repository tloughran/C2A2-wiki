# Sewing Agent — Bootstrap Audit Verification Run

**Run date:** 2026-08-16 · **Mode:** autonomous (Tom not present) · **Type:** verification + one **correction of last week's headline finding** + one new measurement. Not a re-execution.

## Why this is again not a full re-run

This ONE-TIME bootstrap task has now fired **eight times** (2026-06-23, 06-28, 07-06, 07-12, 07-26, 08-02, 08-09, today). The baseline stands: full census at `architecture/metrics/bootstrap_backlink_census_2026-06-28.md`; classification and Phase 3/4 disposition in `architecture/sewing_agent_bootstrap_2026-06-28.md`; the live weekly `c2a2-sewing-agent-weekly` pipeline owns `connectivity_log.csv`.

Deliberately NOT written (fail-loud, not silent skip):

- **No new census file.** A structurally identical ~300 KB file is clutter, not measurement.
- **No `connectivity_log.csv` row.** The weekly agent owns that file; a second row from a different in-memory resolver adds noise to the trend line. (The live CSV header is `date,orphan,sparse,connected,total`, not the header this SKILL.md specifies. The SKILL is the stale one.)
- **No agentic-call injection, no synthesis stubs.** Phase 3 as written would modify ~1,300 files in a repo governed by the no-blind-push rule, with no human present to review.

## Verification census

Method: in-memory, path-aware `[[wikilink]]` resolution; `node_modules`, `.obsidian`, `.git` excluded. **Methodology check passed** — the resolver reproduced the baseline top-hub list exactly (`friston/prs_triplets.md` 150, `stump` 121, `levin` 96, `fredrickson` 82, `kastrup` 70), so the deltas below are real movement, not resolver drift.

| Metric | 06-28 baseline | 08-02 | 08-09 | **08-16** | Δ since 08-09 |
|---|---|---|---|---|---|
| Total pages | 3,031 | 3,806 | 3,994 | **4,267** | +273 |
| Orphan (0 backlinks) | 2,337 | 3,093 | 3,281 | **3,554** | +273 |
| Sparse (1–2) | 647 | 657 | 657 | **657** | 0 |
| Connected (3+) | 47 | 56 | 56 | **56** | 0 |
| Wikilinks parsed | 1,836 | 2,071 | 2,116 | **2,163** | +47 |

Distribution: 0 → 3,554 · 1–2 → 657 · 3–5 → 20 · 6–10 → 11 · 10+ → 25.

**Headline, third week running: every one of the 273 new pages is an orphan.** The sparse and connected buckets have not moved a single page in three weeks — 657 and 56, to the digit, three weeks in a row.

Growth source for the +273: `architecture/lit_search_results` 2,082 → 2,283 (+201), `inbox` 652 → 689 (+37), `architecture/daily_sync` 181 → 194 (+13), `synthesis` 62 → 66 (+4), remainder ~18 scattered across `architecture/`.

## CORRECTION — last week's "307 closed dyads" was wrong in the direction that matters

Last week this report claimed the Summa corpus (`vault/`, 614 pages) was "307 disconnected dyads, each a closed loop of two pages pointing at each other and at nothing else," and recommended giving `sync_vault.sh` an outbound-link step.

**The outbound links already exist, and they are the largest link source in the vault.** The error was measuring only what points *at* those pages and inferring what they point *to*.

Measured this week, by link direction:

- The 307 `vault/synthesis/Day-NNN … Contemporary.md` pages emit **1,143 wikilinks** — **53% of all 2,163 wikilinks in the vault**.
- **1,138 of those 1,143 land on the 14 `traditions/*/prs_triplets.md` hubs.** Friston 149, Stump 121, Levin 96, Fredrickson 82, Kastrup 70, Hoffman 64, Wright 58, McGilchrist 58, Rohr 51, Hawkins 30, Wolfram 27, Carroll 18, MacIntyre 5, Arkani-Hamed 4, Loughran 3.
- Compare the hub backlink totals in the table above: `friston/prs_triplets.md` has **150** backlinks, of which **149 are from the Summa corpus**. The same holds down the list. **The tradition hubs' connectivity is the Summa corpus, almost in its entirety.**

Confirmation of the other half: all 307 Contemporary pages still have **exactly 1** backlink, all 307 from their paired transcript, and **zero** from any index, hub, or tradition page.

So the corpus is not an island. It is a **one-way feeder**: it pours richly into the hubs and nothing returns. Removing `vault/` as a link source drops the vault's 10+-backlink bucket from **25 pages to 13** — nearly half of everything well-connected in this graph is well-connected only because the Summa corpus links to it.

**This changes the fix.** Last week's item 2 (add an outbound-link step to the sync) would have duplicated work already done. The correct fix is the **reciprocal index**, and it is cheaper: every edge needed already exists in the files, pointing the wrong way. A script that inverts them and appends a `## Cited by` section to each `traditions/*/prs_triplets.md` moves 307 pages from 1 backlink to 2+, makes the corpus reachable by navigation, and writes **no new prose and no new claims** — it only states, in the hub, links the Summa pages already assert.

## NEW MEASUREMENT — 81% of the vault emits no links at all

The orphan count is a symptom; this is closer to the cause. Pages with **zero outbound wikilinks: 3,470 of 4,267 (81.3%)**.

| Directory | Pages | Links emitted | Zero-outbound | % zero |
|---|---|---|---|---|
| `architecture/lit_search_results` | 2,283 | **1** | 2,282 | 100% |
| `inbox` | 689 | 300 | 596 | 87% |
| `vault/synthesis` | 307 | **1,143** | 0 | **0%** |
| `vault/transcripts` | 307 | 307 | 0 | **0%** |
| `architecture/daily_sync` | 194 | 7 | 191 | 98% |
| `architecture/metrics` | 99 | 2 | 97 | 98% |
| `architecture/changelog` | 97 | 2 | 95 | 98% |
| `synthesis` | 66 | 17 | 52 | 79% |
| `traditions` | 34 | 79 | 12 | 35% |
| `agents` | 33 | 165 | 7 | 21% |
| `review` | 23 | 0 | 23 | 100% |
| `voice_guide` | 7 | 0 | 7 | 100% |

Read the first and third rows together. `lit_search_results` has produced **2,283 pages and one wikilink**. `vault/synthesis` has produced **307 pages and 1,143 wikilinks**. The two generators sit in the same vault and differ by three orders of magnitude in whether they wire their output in.

This is why the sparse and connected buckets are frozen while the total climbs: **the directories that are growing are the directories that emit nothing.** No orphan sweep can fix that downstream. It is fixed at the generator, by having each producer emit the one or two links it already knows about at write time.

## Broken wikilinks: 188 → 234, and 145 of them are still bare thinker names

Of **2,163** wikilinks vault-wide, **234 (10.8%)** do not resolve, across 44 distinct targets — up from 188/8.9% last week. **145 of the 234 (62%) are references to the thinkers themselves**, now in **25** spelling variants (was 106 across 24). The cause is unchanged and mechanical: there is no `Friston.md`; the hub lives at `traditions/friston/wiki.md`, so every bare-name link dead-ends.

Broken links by source directory: `inbox` 94, `architecture` 52, `agents` 31, `master` 23, `flags` 12, `(root)` 10, `session-archive` 9, `sessions` 2, `c2a2-wiki-narration` 1.

The remaining 89 are template placeholders (`[[wikilink]]` ×33, `[[Agent Name]]` ×16, `[[a/b/c]]` ×5, `[[Day-N+1]]` ×4, `[[*_bridge]]` ×3) and are noise, not error.

**Correction to last week's fix as well:** it lumped the seven `[[X Agent]]` variants in with the bare names. They should point at `agents/NN_x_agent.md`, not the tradition wiki. Split correctly: **127 links to 18 tradition-name aliases, 18 links to 7 agent-name aliases.** All 12 tradition `wiki.md` targets and all 7 agent targets were verified present this run.

Ready-to-paste generator, ASCII-only and paste-safe for interactive zsh. It writes 25 one-line alias notes and clobbers nothing (`-f` test on each):

```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki"
mk() { if [ -f "$1.md" ]; then echo "skip $1"; else printf '%s\n' "[[$2]]" > "$1.md"; echo "made $1"; fi }
mk "Friston" "traditions/friston/wiki"
mk "Karl Friston" "traditions/friston/wiki"
mk "Kastrup" "traditions/kastrup/wiki"
mk "Bernardo Kastrup" "traditions/kastrup/wiki"
mk "Levin" "traditions/levin/wiki"
mk "Michael Levin" "traditions/levin/wiki"
mk "Levin thinker node" "traditions/levin/wiki"
mk "Levin-tradition wiki" "traditions/levin/wiki"
mk "Hoffman" "traditions/hoffman/wiki"
mk "Wolfram" "traditions/wolfram/wiki"
mk "Steven Wolfram" "traditions/wolfram/wiki"
mk "Hawkins" "traditions/hawkins/wiki"
mk "McGilchrist" "traditions/mcgilchrist/wiki"
mk "Iain McGilchrist" "traditions/mcgilchrist/wiki"
mk "Stump" "traditions/stump/wiki"
mk "Fredrickson" "traditions/fredrickson/wiki"
mk "Carroll" "traditions/carroll/wiki"
mk "Tom Loughran" "traditions/loughran/wiki"
mk "Hoffman Agent" "agents/03_hoffman_agent"
mk "Hawkins Agent" "agents/04_hawkins_agent"
mk "McGilchrist Agent" "agents/05_mcgilchrist_agent"
mk "Fredrickson Agent" "agents/06_fredrickson_agent"
mk "Stump Agent" "agents/07_stump_agent"
mk "Arkani-Hamed Agent" "agents/09_arkanihamed_agent"
mk "Kastrup Agent" "agents/11_kastrup_agent"
```

Not run by this agent: these are 25 new vault-visible content files, and vault content is the exact class the no-blind-push rule protects. One paste, fully reviewable, reversible with `git checkout`.

## Category breakdown

Orphan + sparse pages (4,211), classified by deterministic path/size heuristics — the model was not used for this, per Rule 5:

| Category | Count |
|---|---|
| D structural (system/architecture; backlinks not expected) | 2,744 |
| B inbox residue | 689 |
| A/C thinker + synthesis content (`vault/`) | 616 |
| C synthesis (`synthesis/`) | 55 |
| Other (review, agents, heartbeat, traditions, flags, …) | 107 |

## Carried-over litter (verified present this run)

- **Metric inflation — eighth consecutive flag, still unactioned.** `architecture/lit_search_results/` (2,283 `.md`) + `architecture/daily_sync/` (194) = **2,477 pages, 58% of the 4,267 total.** Excluding both, the census reads **1,790 pages / 1,077 orphans / 657 sparse / 56 connected** instead of 4,267 / 3,554. These machine dumps are why every report's headline is "+N orphans." Fix is one config line plus a break-marker in the series.
- **Zero-byte `*_bridge.md` stubs: 8 → 5.** Progress: `hawkins_loughran`, `hawkins_wolfram`, and `loughran_mcgilchrist` were populated this week. Remaining: `arkanihamed_loughran`, `carroll_hawkins`, `hoffman_loughran`, `kastrup_loughran`, `mcgilchrist_wright`.
- **Inbox: 689 pages, up from 652** (+37; growth rate roughly halved from last week's +70).
- **Seven tradition hub pages** (`{arkanihamed,carroll,fredrickson,kastrup,rohr,stump,wright}/wiki.md`) all exist and still await the navigation fix wiring them into their child notes.

## Vault health assessment

**Upgraded from "affirmative with one named structural defect" to "affirmative; the defect is narrower and better located than last week's reading."**

Last week's downgrade rested on a claim now shown to be false in its load-bearing half. The Summa corpus is not severed — it is the most densely linking body of writing in the vault and the reason the tradition hubs have any connectivity at all. The knowledge graph does support thinker-agent synthesis, and it supports it *because of* the 614 pages last week's report wrote off.

The real defect is asymmetry, in two places, both mechanical:

1. **Links flow one way.** The Summa corpus feeds the hubs; nothing feeds back. Fixable by inverting edges that already exist.
2. **The growing directories emit nothing.** 2,283 lit-search pages have produced one wikilink between them. Fixable at the generator, not by any sweep downstream.

Neither is an editorial problem. Neither requires new prose. Both are the same shape as the alias fix: connectivity that is already implicit in the vault's contents and simply not written down as links.

## Recommended actions for Tom

1. **Run the alias-note block above.** 25 one-line files, 145 dead links restored — more new connectivity than the vault has produced organically in six weeks. Third week recommended; now with a corrected split (tradition names vs. agent names) and a paste-safe generator.
2. **Build the reciprocal `## Cited by` index on the 14 `prs_triplets.md` hubs.** Supersedes and corrects last week's item 2, which asked for outbound links that already exist. Inverts 1,138 existing edges; no new prose; moves 307 pages out of the 1-backlink bucket. New this week.
3. **Make `lit_search_results` emit links at write time.** 2,283 pages, one wikilink. Every one of those pages was generated *for* a thinker and *about* a claim; the generator knows both at write time and writes neither. This is the largest single source of orphan growth in the vault and it is fixed upstream in one place.
4. **Retire or reschedule `c2a2-sewing-agent--c2a2-wiki-bootstrap-audit`.** Eighth run of a task its own SKILL.md calls "a ONE-TIME run." Fold a quarterly "delta vs. bootstrap baseline" section into the weekly agent instead. (Third time recommended.)
5. **Decide the census definition** (exclude `lit_search_results/` and `daily_sync/`, or keep them and stop reading the orphan trend as signal). Eight reports have now flagged this.
6. **Triage the 689 inbox pages** in dated batches. Also the source of 94 of the 234 broken links.

Empty-stub cleanup command, if you want the bridge noise gone:

```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/synthesis"
find . -name '*_bridge.md' -size 0 -delete
```

---

*Autonomous scheduled run. Append-only; no vault content modified. No census file, CSV row, or agentic-call injection written this run — by design, matching the 07-06, 07-12, 07-26, 08-02 and 08-09 precedent. One prior-report headline finding corrected (Summa link direction), one prior-report fix corrected (agent-name aliases split out), one new measurement added (outbound-link poverty by directory).*
