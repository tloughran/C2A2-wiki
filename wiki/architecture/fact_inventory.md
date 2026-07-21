---
title: Fact Inventory — Source-of-Truth Drift Audit
pathway_id: fact_inventory
status: drafted
created: 2026-07-20
depends_on: [voice_guide_state_bus]
enables: [single_source_discipline, drift_detection]
isme_critical: no
---

# Fact Inventory — Source-of-Truth Drift Audit

Triggered by the voice guide's fabrication problem. The guide was found reading from four
competing sources; the question was whether that was a one-off or a **structural signature**.
It is structural. This is the audit.

Scope: facts that **more than one component reads**. Not a census of every string.

## The generating mechanism (confirmed)

The constitutional inline rule — iframe-loaded tabs must inline their JS/CSS — exists for a real
reason (cache correctness) and is correct. But inlining **structurally manufactures copies**:
every self-contained HTML file becomes a place where facts live. The drift is not carelessness;
it is the predictable output of a rule we chose on purpose.

The resolution is not "remove copies." It is **"make every copy generated."**

## Four classes of duplication

| Class | Meaning | Verdict |
|---|---|---|
| **A. Canonical + generated** | One authoring home, build step inlines it | ✅ Safe — the target pattern |
| **B. Hand-copied twin** | Same literal maintained by hand in N places | ⚠️ Drifts silently |
| **C. Prose asserting volatile data** | Counts/state frozen into text | ❌ Guaranteed to rot |
| **D. Orphaned artifact** | Dead file still carrying facts | ☠️ Worst — reads as truth, answers to no one |

Class D was not predicted before the audit. It is the most dangerous because a future human or
agent cannot tell a frozen snapshot from a live source.

## We already have the right pattern in-repo

`wiki/community/index.html` + `app.js` load `../lib/c2a2-search.js` via `<script src>` and read
`window.C2A2Search.BROKER_URL` **live** — zero duplication. This is the exemplar to propagate.
Per Rule 11, the fix is spreading an existing convention, not inventing one.

---

## Family 1 — Schedules & agent roster (worst structural drift)

**Systematic pattern, ~20 agents affected:** the human-readable `schedule` string disagrees with
that agent's own machine fields, *inside the same object*.

- `c2a2-wiki-janitor-weekly`: `agents_tab.html:465` `schedule:"Sun 05:53"` vs `:466` `hour:5,
  minute:45` vs TELEMETRY `cron:"45 5 * * 0"` vs `CLAUDE.md:144` "Sunday 05:45".
- `c2a2-agent-wright-rohr`: TELEMETRY string "Sun 03:13" vs **its own adjacent** `cron:"4 3 * * 0"`.
- `morning-walk-cowork-handoff`: `AGENTS` says `days:[0..6]` (daily); TELEMETRY + canonical map say
  **Mon–Fri**. Semantic, not cosmetic.
- Name drift: `c2a2-wiki-agent-daily-run` (AGENTS, CLAUDE.md) vs `c282-wiki-agent-daily-run`
  (actual taskId) — papered over by a `TELEMETRY_ALIAS` at `agents_tab.html:452`.
- Category drift: `execution-assistant` `project` vs `infrastructure`; both summa agents `summa`
  vs `project`.

**Roster counts disagree four ways:** `AGENTS` array 36 · `FRIENDLY_NAMES` 34 · TELEMETRY
`roster_size` 33 · static page subtitle "35 Agents" (`agents_tab.html:289`).

**Why it drifts:** there is **no authoritative live source to reconcile against**. The roster's
agents run under OpenStory/launchd (proof: `c282-wiki-agent-daily-run` committed `64eede6` at
04:39 on 2026-07-18), while `list_scheduled_tasks` only sees Cowork tasks and returns exactly one
(`c2a2-voice-faq-weekly`). Two scheduling worlds, no reconciliation — so the published roster is
hand-maintained prose about a system nothing checks it against. **Class B.**

Also: launchd job `com.tloughran.summa-weekly-review` (Sun 20:00) is documented **nowhere**.

## Family 2 — Counts (worst rot; unfixable by prose)

| Subject | Asserted values | Reality | Verdict |
|---|---|---|---|
| Sociogram nodes | 1,500+ (README) · 1,600+ (`explorer.html:829`) · 1,647 (STATE_OF_PROJECT, memory) · 2,638 (`CLAUDE.md:109`) · 3,547 (handoff, verified 2026-06-25) · 3,992 (live counter) | ~3,725 `.md` files today | ❌ six values |
| PRS triples | 282 (`CLAUDE.md:222`, w/ provenance) · 447 (sum of live review_log) | 447 | ❌ |
| Agents | "35 Agents" subtitle | 36 in array | ❌ |
| Curated communities | "156" everywhere | **155** in `curated_communities.json` | ❌ off-by-one |
| TRV annotations/pages | 1,819 / 156 | matches `bundle.json._meta` | ✅ |
| RC doc | 471 pp / 679 sections / 9 programs | consistent | ✅ |
| Physics | 75 concepts / 6 physicists | matches arrays | ✅ |
| Summa episodes | 308 | matches | ✅ |

Pattern: **counts over slow-moving curated corpora stay true; counts over living data rot.** The
living ones must never be asserted in prose — they belong to the state bus. **Class C.**

## Family 3 — Palette & tradition roster

- **Real hex drift:** MacIntyre `#7A6B8A` (`generate_visualization.py:113` → `wiki_narration.html`)
  vs `#7A6A8A` (`extract_prs_data.py:36` → `prs_3d.html`). One nibble; two independent pipelines.
- **Roster 14 vs 15:** CLAUDE.md + `memory/c2a2-wiki.md` list 14 (no MacIntyre); three pipelines
  list 15. `build_bundle.py` also uses 14 — but **intentionally**, with a documented rationale
  ("MacIntyre is the book's author — no satellite"). The exclusion is correct; the *reason* is
  recorded only in that script, so the docs read as simply wrong.
- **Class D instance:** `commentary-explorer/data/bundle.json` has 0 MacIntyre nodes but **3
  dangling edges** referencing `thinker-macintyre` — a stale artifact from before the exclusion.

Three independently hand-maintained palette copies (`generate_visualization.py`,
`extract_prs_data.py`, `build_bundle.py`) + CLAUDE.md/memory as a fourth. **Class B.**

## Family 4 — Tabs & descriptions (the voice guide's own family)

- **Missing descriptions:** `interT_study.html` and `start_here.html` are live tabs with **no entry**
  in the `descriptions` map — their "?" falls back to generic text. The FAQ has Q&A for both only
  because I authored it directly, not derived it.
- **A ghost tab explains a real bug:** `site_guide.html:155` claims six chapters "and this Site
  Guide," but `explorer.html` has five and no Site Guide button. That is the origin of the
  undefined `chapGuide` reference at `explorer.html:511,514` — the latent bug flagged earlier in
  the handoff. **Documentation drift and a code bug with one shared root cause.**
- **`site_guide.html` is largely counterfactual:** Community Explorer, Community Education,
  Community Interactions and all four Education tools are still tagged `planned` / "To be sourced
  and written" though all are built and wired.
- Naming: button "Metabolism" vs description/FAQ title "Agent Metabolism".
- Enumerations disagree: buttons 13 · `descriptions` 12 · `TABS` 13 · FAQ features 14.

## Family 5 — Shared config (healthiest)

**No live value differs today.** But structure is mixed:

- ✅ **Class A:** `c2a2-search.js` → `wiki_narration.html`, `community_explorer.html` (real build steps).
  `template_prs_3d.html` → `prs_3d.html`.
- ⚠️ **Class B:** broker URL + `c2a2_device_id` hand-copied into `physics_explorer.html:753`,
  `rc_document_explorer.html:3861`, and `explorer.html:982` (the voice guide re-declares them).
  Their own comments say "edit THERE and re-inline" — a manual step with no enforcement.
- ⚠️ `tts_api_key` has **no canonical definer** — ad hoc in ~8 files.
- ☠️ **Class D:** `combined_wiki.html`, `wiki_narration_roundtrip.html` (frozen 2026-05-07, no
  generator, still contain endpoints/keys/model names), plus `.bak.html` files under `c2a2-prs-3d/`.

---

## Recommendations

**R1 — Adopt the exemplar.** Where a page can load `c2a2-search.js` by `<script src>` (like
`community/index.html`), do that instead of inlining. Reserve inlining for pages that genuinely
need to be single-file, and make those generated.

**R2 — Delete or quarantine Class D.** `combined_wiki.html`, `wiki_narration_roundtrip.html`,
`.bak.html` files, and the stale `bundle.json` MacIntyre edges. Dead files carrying facts are the
highest-risk, lowest-cost fix in this audit.

**R3 — One canonical roster (identity), NOT one canonical palette (encoding).** *Revised 2026-07-20.*
Single JSON read by all three pipelines for **identity only**: which categories exist, which
taxonomy each belongs to, and `has_satellite: false` for MacIntyre so the intentional exclusion
stops looking like an error.

🛑 **Do not fold the current colours into that file.** The palette is an artifact of construction
haste — 17 categories from two orthogonal taxonomies (thinker tradition + structure group) on a
single hue channel, leaving eight pairs under ΔE 15 (Friston/Architecture at 7.7 is the closest).
Consolidating as-is would canonise the flaw. **Identity is data; encoding is a revisable policy**,
and the visual language (shape × colour) is 🔒 reserved to Tom — see
`voice_guide_state_bus.md` → "Color is NOT an identifier".

**R4 — Never assert living counts in prose.** Remove/soften them in CLAUDE.md, README, tab help,
and the FAQ. They belong to the state bus. This is the voice-guide contract applied repo-wide.

**R5 — Generalize the janitor into a drift detector.** The janitor already runs
`src_pub_refs_drift` and `reindexer_freshness` — the pattern exists. Add report-only checks:
- schedule string vs its own `hour`/`minute`/`cron` fields
- roster count agreement across `AGENTS` / `FRIENDLY_NAMES` / TELEMETRY / subtitle
- palette hex agreement across pipelines
- asserted counts vs computed reality (nodes, communities, triples)
- tabs with no `descriptions` entry

One-time cleanup re-accretes. A recurring detector does not. **This is the durable fix.**

**R6 — Reconcile the two scheduling worlds,** or state plainly in `agents_tab.html` that its
roster is a hand-maintained description of OpenStory/launchd agents with no live reconciliation.
Right now it reads as authoritative and is not.

## ⚠️ READ BEFORE ACTING ON ANY RECOMMENDATION ABOVE

This audit was produced by one model, in one harness, reading one repo. All three are variables.
**Do not execute the recommendations literally.** Specific hazards, in priority order:

**H1 — Some listed "discrepancies" are INTENTIONAL. Do not "fix" them.**
The 14-vs-15 tradition roster is deliberate: `build_bundle.py` excludes MacIntyre because he is
the book's *author* and has no satellite page. An agent reading the drift table without this
paragraph would "correct" 14→15 and break the commentary bundle. **Intentional variance must be
encoded as machine-readable data next to the code** (e.g. `has_satellite: false`), never as prose
in an audit. Until that encoding exists, this table is an attractive nuisance.

**H2 — "Orphaned" (Class D) was asserted on repo-local evidence and is WRONG as stated.**
Verified 2026-07-20: `combined_wiki.html` is referenced by `wiki/combined_morning_assembly.md`
**and by a separate project** (`Projects/Resurrecting Civility Whole/`). Three launchd jobs
(`summa-vault-sync`, `metabolism-publish`, `summa-weekly-review`) write into `wiki/` from outside
this repo. **The repo is not the system boundary.** R2 is downgraded from *delete* to *verify
cross-boundary, then tombstone*. Never delete on repo-local evidence alone.

**H3 — Build-orphan ≠ archive-orphan.** The historical record (`daily_sync/**`, `changelog/**`,
and the vault content embedded in `wiki_narration.html`) references these files by name. Removing
a file does not remove the references; it creates dangling links in the archive. A file may be
dead to the *build* and still load-bearing for the *record*.

**H4 — Documentation is not enforcement.** The agent that next reads this will be a different
model with no memory of the session that wrote it, and CLAUDE.md is already long enough that
partial compliance is likely. Any rule that matters must be a **gate that runs** (janitor check,
build step that fails loud), not a convention that must be remembered.

**H5 — Tool visibility varies by harness; do not mistake it for ground truth.** During this audit
a sub-agent correctly reported that the live scheduler holds only one task — true for the Cowork/
Code scheduler, false for the system, because the roster's agents run under OpenStory/launchd
(proof: `c282-wiki-agent-daily-run` committed `64eede6` at 04:39, 2026-07-18). Acting on that view
would have "corrected" an accurate roster to match a harness-limited window.

**H6 — Concurrency is real here.** A crashed agent left a stale `.git/HEAD.lock` that silently
blocked another agent for ~17 hours (2026-07-18). Any new build step adds another writer. Build
steps must be idempotent, lock-aware, and centralized rather than scattered.

## Note on this document

Per R4, this file deliberately records counts **as evidence of drift, with dates and sources** —
not as current fact. It is an audit snapshot, not a source of truth. Re-run the audit rather than
trusting these numbers.
