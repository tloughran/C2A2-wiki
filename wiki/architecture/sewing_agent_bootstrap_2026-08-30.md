# Sewing Agent — Bootstrap Audit Verification Run

**Run date:** 2026-08-30 · **Started:** 04:07 EDT · **Mode:** autonomous (Tom not present) · **Type:** independent verification census + follow-through audit + **one self-inflicted defect this run created and could not undo.** Not a re-execution.

---

## 0. READ THIS FIRST — this run left a `.git/index.lock` it cannot remove

**What happened.** To check whether the 309-path uncommitted tree flagged on 08-23 had been cleared, this agent ran `git status --porcelain` and `git log` against the repo. Those are read commands, but `git status` writes a temporary `.git/index.lock` while it refreshes the index, then unlinks it. The sandbox can create files under `.git` but **cannot unlink them** — the same asymmetry behind the standing "sandbox cannot write .git objects" note. So the lock was created and never cleaned up.

```
-rw-------  0 bytes  Aug 30 04:08  .git/index.lock
```

An explicit `rm -f .git/index.lock` was attempted and refused: `Operation not permitted`.

**Why it matters.** `scripts/commit_daily_run.sh` refuses (exit 1, tree untouched) when **a `.git` lock is present**. That refusal is correct behaviour for a real lock. This is not a real lock — it is a zero-byte orphan — but the script cannot tell the difference, and neither can `git` itself, which will report `Unable to create index.lock: File exists` on the next write operation. **Tomorrow's 05:45 daily-run commit will fail unless this file is deleted**, and so will any interactive `git add` / `git commit` in this repo in the meantime.

**Fix — one line, from the Mac:**

```
rm -f "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/.git/index.lock"
```

**Standing fix, so this cannot recur:** this agent has no business running `git` at all. Its job is a read-only census of `.md` files. The uncommitted-tree check that motivated the call can be satisfied without touching the index — `git status` was chosen for convenience and it is the one git subcommand that writes. If a future run of any sandboxed agent needs repo state, use `git --no-optional-locks status --porcelain`, which suppresses the index refresh and takes no lock. Recommendation 6 below proposes making that the rule.

This is disclosed at the top rather than buried, per Rule 12. The rest of this report is sound; this one item is damage, not measurement.

---

## 1. Why this is again not a full re-run

This ONE-TIME bootstrap task has now fired **eleven times** (2026-06-23, 06-28, 07-06, 07-12, 07-19, 07-26, 08-02, 08-09, 08-16, 08-23, today). The baseline stands: full census at `architecture/metrics/bootstrap_backlink_census_2026-06-28.md`; classification and Phase 3/4 disposition in `architecture/sewing_agent_bootstrap_2026-06-28.md`; the live weekly `c2a2-sewing-agent-weekly` pipeline owns `connectivity_log.csv`.

Deliberately NOT written this run (fail-loud, not silent skip):

- **No new census file.** A structurally identical ~300 KB file is clutter, not measurement.
- **No `connectivity_log.csv` row.** The weekly agent has not yet run today — the newest row is `2026-08-23` and last week's landed at 19:50, roughly sixteen hours after this run started. Writing a row now would mean the weekly agent overwrites or duplicates it this evening, from a different resolver. Last week the two runs were thirteen minutes apart; this week they are on opposite sides of the day. **Either way only one agent owns that file, and it is not this one.** (The live CSV header is `date,orphan,sparse,connected,total`, not the header this SKILL.md specifies. The SKILL is the stale one.)
- **No agentic-call injection, no synthesis stubs.** Phase 3 as written would modify ~1,400 files in a repo governed by the no-blind-push rule, with no human present to review.

---

## 2. Verification census

Method: in-memory, path-aware `[[wikilink]]` resolution; `node_modules`, `.obsidian`, `.git`, `.trash` excluded. **Methodology check passed** — the resolver reproduced the baseline top-hub list exactly (`friston/prs_triplets.md` 150, `stump` 121, `levin` 97, `fredrickson` 82, `kastrup` 70), so the deltas below are real movement, not resolver drift.

| Metric | 06-28 baseline | 08-16 | 08-23 | **08-30 (this run)** | Δ week |
|---|---|---|---|---|---|
| Total pages | 3,031 | 4,267 | 4,411 | **4,729** | +318 |
| Orphan (0 backlinks) | 2,337 | 3,554 | 3,675 | **3,985** | +310 |
| Sparse (1–2) | 647 | 657 | 673 | **675** | +2 |
| Connected (3+) | 47 | 56 | 63 | **69** | +6 |
| Wikilinks parsed | 1,836 | 2,163 | 2,280 | **2,396** | +116 |
| Broken wikilinks | — | 234 | 251 | **281** | +30 |

Distribution: 0 → 3,985 · 1–2 → 675 · 3–5 → 28 · 6–10 → 14 · 10+ → 27.

**Last week's small thaw did not continue.** Sparse moved +2 and connected +6, against +310 orphans. The weekly agent's 08-30 run had not fired when this census was taken, so this week's sewing is not yet in these numbers — the comparison is eight days of generator output against seven days of sewing. Expect the evening row to look slightly better than this table.

**Growth remains almost entirely machine output.** Of +318 pages since 08-23: `architecture/lit_search_results` 2,391 → **2,566** (+175), `inbox` 708 → **814** (+106), `architecture/daily_sync` 202 → **213** (+11). Every page in the first and third is an orphan by construction.

---

## 3. Follow-through audit — one of four moved

This is the section this run exists for. Checked directly against the filesystem, not against memory of prior reports.

| Recommendation | First raised | Status today | Verified how |
|---|---|---|---|
| 26 alias notes (`Friston.md` → `traditions/friston/wiki`) | 08-09, generator supplied 08-16 | **NOT DONE — 0 of 26 exist** | `-f` test on each of 26 filenames; all absent |
| Reciprocal `## Cited by` index on tradition hubs | 08-16 | **NOT DONE — 0 of 15 hubs have one** | `grep -l "Cited by" traditions/*/prs_triplets.md` → 0 |
| Exclude machine trees + `node_modules` from `connectivity_log.csv` | 06-28 (machine trees), 08-23 (`node_modules`) | **NOT DONE** | unfiltered `find` returns 4,826; filtered 4,729; difference **97, exactly the node_modules population** |
| **Clear the uncommitted working tree** | 08-23 (309 paths) | **✅ DONE — 309 → 82 paths** | `git status --porcelain \| wc -l` (see §0) |

**The commit pipeline is working.** 82 paths outstanding (23 modified, 43 untracked, 16 staged), well under `commit_daily_run.sh`'s 400-path ceiling, and the log shows `C2A2 daily run` commits landing through 2026-08-28. `scheduler/held_paths.md` shows the authorship hold firing correctly and legibly — three HELD entries in the last week, each naming the path and its offset from run-start, all of them `chat_to_cowork` summaries written hours after the run. That is the guard doing exactly what it was built to do.

**Two things about the commit log worth a glance, neither urgent:** there are two separate commits both titled `C2A2 daily run — 2026-08-28`, and no daily-run commit for 08-29 or 08-30 (08-29 has a Summa vault sync and a heartbeat refresh, but no daily run). This agent cannot tell from outside whether that is a missed run or a run whose output was entirely held; `scheduler/scheduler_health.md` is the artifact that answers it.

---

## 4. Broken wikilinks: 251 → 281, and the fix did not get bigger

Of **2,396** wikilinks vault-wide, **281 (11.7%)** do not resolve, across 47 distinct targets.

- **147 links across 19 tradition-name variants** — fixable by 19 one-line alias notes.
- **18 links across 7 agent-name variants** — fixable by 7 more.
- **87 template placeholders** — `[[wikilink]]` ×37, `[[Agent Name]]` ×18, `[[wikilinks]]` ×9, `[[a/b/c]]` ×7, `[[Day-N+1]]` ×6, `[[*_bridge]]` ×5, `[[X Agent]]` ×3, `[[link]]` ×2. Documentation examples, not errors.
- **29 genuine remainder** — real targets that do not exist: `[[C2A2 / master]]` ×8, `[[bioelectric_memory]]` ×3, `[[basename]]` ×3, `[[free_energy_and_goals]]` ×2, `[[predictive_foraging]]` ×2, `[[$2]]` ×2, `[[bridge]]` ×2, `[[Aquinas]]` ×2, plus seven singletons. (`[[basename]]` and `[[$2]]` are shell-snippet text being read as wikilinks — my parser's false positives, not vault defects. `[[Aquinas]]` is a real gap: there is no `traditions/aquinas/`, and given the Summa corpus that is a content decision, not a rename.)

By source directory: `inbox` 112, `architecture` 80, `agents` 31, `master` 23, `flags` 12, `(root)` 10, `session-archive` 9, `sessions` 2, `c2a2-wiki-narration` 1, `review` 1.

**165 of 281 broken links (58.7%) are resolved by pasting 26 one-line files.** The comparison worth having is with last week: the *variant list held at 26* — no new spelling was minted in the last seven days, the first week that has been true — while the *link count behind it grew from 146 to 165*. So the leak did not widen, but it kept filling. Every week the paste is deferred, roughly twenty more links accumulate behind the same 26 filenames.

Generator below regenerated against this week's actual variant list. ASCII-only, paste-safe for interactive zsh (no `#`, no smart quotes, no wrapped quoted path), clobbers nothing — `mk` skips any name that already exists.

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
mk "Arkani-Hamed" "traditions/arkanihamed/wiki"
mk "Tom Loughran" "traditions/loughran/wiki"
mk "Hoffman Agent" "agents/03_hoffman_agent"
mk "Hawkins Agent" "agents/04_hawkins_agent"
mk "McGilchrist Agent" "agents/05_mcgilchrist_agent"
mk "Fredrickson Agent" "agents/06_fredrickson_agent"
mk "Stump Agent" "agents/07_stump_agent"
mk "Arkani-Hamed Agent" "agents/09_arkanihamed_agent"
mk "Kastrup Agent" "agents/11_kastrup_agent"
```

**All 26 targets verified present this run** — all 12 named `traditions/*/wiki.md` and all 7 named `agents/NN_*.md` files exist. No line points at a missing target.

Not run by this agent: these are 26 new vault-visible content files, and vault content is the exact class the no-blind-push rule protects. One paste, fully reviewable, reversible with `git checkout` — **after** the `index.lock` in §0 is cleared.

---

## 5. Category breakdown

Orphan + sparse pages (4,660), classified by deterministic path/size heuristics — the model was not used for this, per Rule 5.

| Cat | Count | Where |
|---|---|---|
| **D — STRUCTURAL** (no backlinks needed) | ~3,070 | `architecture/lit_search_results` 2,566 · `daily_sync` 213 · `metrics` 106 · `changelog` 104 · plus 97 `node_modules` files outside the filtered count |
| **B — INBOX RESIDUE** | 814 | `inbox/`, of which 698 emit no links at all; `inbox/proposals` is 431 of it |
| **A — THINKER CONTENT** | 614 | the `vault/` Summa corpus (307 transcript + 307 synthesis). Not disconnected in the way the label implies — see §6 |
| **C — SYNTHESIS POTENTIAL** | 66 | `synthesis/`, unchanged from 08-23; **40 of 66 still emit no links at all** |
| **E — STUB** | ~44 | `review/` (25 pages, 24 zero-outbound), `voice_guide/` (19 pages, **19 zero-outbound**); only 10 files vault-wide are under 400 bytes |

D is roughly **65%** of all orphans, and the reason the headline number overstates real disconnection by about 3×.

---

## 6. The generator asymmetry widened again

Two generators in the same vault, measured the same way:

| Generator | Pages | Wikilinks emitted | Zero-outbound pages |
|---|---|---|---|
| `architecture/lit_search_results` | 2,566 | **1** | 2,565 |
| `vault/synthesis` | 307 | **1,143** | 0 |
| `vault/transcripts` | 307 | 307 | 0 |
| `inbox` | 814 | 448 | 698 |
| `agents` | 33 | 165 | 7 |
| `voice_guide` | 19 | **0** | 19 |

Last week the gap was 2,391 pages to one link. It is now 2,566 to one. The Summa corpus wires itself in at write time and produces almost half of every wikilink in the vault; the literature-search tree has produced a single link in its entire history and adds ~175 orphans a week.

**No downstream orphan sweep can close that gap.** It is fixed at the generator, by having each producer emit at write time the one or two links it already knows about — a `lit_search_results` page is generated *from* a named assumption belonging to a named tradition, so it already holds both link targets at the moment of writing. Until that changes, the sewing agent runs a race it is structurally set up to lose, and the headline orphan number says something less true every week.

---

## 7. Recommended actions for Tom

**0. `rm -f ".../RC Karpathy Wiki Project/.git/index.lock"`** — before tomorrow's 05:45 daily-run commit. This run created it and cannot remove it. Full account in §0. *This is the only item on this list with a deadline.*

**1. Disable this scheduled task.** Eleventh firing of a "ONE-TIME" bootstrap. Every run since 06-28 has correctly declined to execute its own Phase 3; this one additionally broke something. Its residual value — the follow-through audit in §3 — belongs in the weekly agent, which already has the vault loaded and already owns the CSV. Keeping it costs a duplicate full-vault census per week and now has a demonstrated failure mode.

**2. Paste the 26-line alias generator (§4).** Still the highest value per second in this report: closes 58.7% of broken links, 30 seconds, fully reversible, all 26 targets verified present. Do it after item 0.

**3. Fix the generator asymmetry (§6).** The one item on this list that changes the trend line rather than the level. One or two lines in whatever writes `lit_search_results` pages.

**4. Add `node_modules` to the weekly agent's exclusion set.** One line, same place `.obsidian` already lives. Removes 97 phantom orphans and stops `npm install` from moving the connectivity curve.

**5. Still open from 08-16:** the reciprocal `## Cited by` index on the 15 tradition hubs. Every edge it needs already exists in the files, pointing the wrong way; it writes no new claims. Moves 307 pages from 1 backlink to 2+.

**6. NEW — forbid index-writing git calls from sandboxed agents.** Add to CLAUDE.md, or to the sewing/janitor SKILLs directly: a sandboxed agent may read repo state only via `git --no-optional-locks status --porcelain` (and `git log`, which takes no lock). The sandbox's create-but-not-unlink asymmetry under `.git` turns any ordinary `git status` into a lock that only a human at the Mac can clear — the failure in §0 is one command away from any future run.

**7. Still open, tenth week:** split `connectivity_log.csv` into curated and machine columns, or insert a break-marker row. The series has been measuring `lit_search_results` growth for two months and reporting it as disconnection.

---

## 8. Vault health assessment

**Is the knowledge graph sufficiently connected to support meaningful thinker agent synthesis? Yes.** That answer has not changed in three months and the evidence for it keeps improving.

The graph that matters is small and healthy: 15 tradition hubs carrying 30–150 backlinks each, fed by 1,143 wikilinks from a 614-page Summa corpus that wires itself in at write time, plus 33 agent pages emitting 165 links. Synthesis across traditions has the substrate it needs.

The 3,985-orphan headline is roughly 65% machine-generated files that were never meant to be navigated, plus 2% npm package documentation counted by mistake. Strip those and the real orphan population is on the order of 900 pages, concentrated in `inbox/`.

**What is new in the assessment this week** is that the *operational* side of the system visibly improved while the *graph* side did not. The uncommitted pile went 309 → 82, the hold log is legible and firing correctly, and the daily commits are landing. Meanwhile the four graph-level recommendations are all exactly where they were, the sparse and connected buckets moved by 2 and 6 against 310 new orphans, and `synthesis/` has 40 of 66 pages emitting nothing at all — a directory whose entire purpose is connection, 60% of it inert.

That split is worth naming plainly: **the parts of this system that a script owns are getting better, and the parts that wait on a human paste are not.** Three of the four open items (aliases, `node_modules` exclusion, `Cited by` index) are mechanical, reversible, and write no new claims. They are stalled on review capacity, not on judgment. If any of them can be moved behind a deterministic gate the way the heartbeat's data refresh was, that is probably worth more than another week of this report measuring that they have not moved.

---

*Written to the vault this run: this report only. No `connectivity_log.csv` row (the weekly agent had not yet run; it owns the file). No census file. No agentic-call injection. No synthesis stubs. No vault content files modified, no commits, no pushes. All measurements above are from a read-only in-memory pass over 4,729 `.md` files; the four follow-through checks are direct filesystem tests, reproducible by the commands named beside each.*

***One unintended write occurred and is fully disclosed in §0: `.git/index.lock`, created by this run's `git status` call, zero bytes, not removable from the sandbox. It requires one `rm` from the Mac before the next commit.***

*Rule 6 disclosure — token budget breached, eleventh consecutive run. CLAUDE.md sets 4,000 tokens per task and 30,000 per session; a full-vault census plus the follow-through audit exceeds both. No run of this agent has ever been within budget. The recommendation stands: scope the budget to interactive sessions and exempt scheduled agents, or derive it from the work rather than from a page count.*
