# Sewing Agent — Bootstrap Audit Report

**Run date:** 2026-06-23
**Type:** One-time full-vault baseline (autonomous scheduled run; Tom not present)
**Vault:** `RC Karpathy Wiki Project/wiki/`
**Companion artifacts:** `architecture/metrics/bootstrap_backlink_census_2026-06-23.md` (per-page census), `architecture/metrics/connectivity_log.csv` (new row appended)

---

## TL;DR for Tom

The vault is **large (2,812 pages) and intentionally hub-and-spoke, not densely cross-linked.** 77% of pages have zero inbound wikilinks, but that number is dominated by two categories that *should not* carry backlinks — `architecture/` system pages (1,676) and `inbox/` residue (436). After setting those aside, the genuine reconnection surface is small and tractable.

**I did not perform Phase 3 (bulk agentic-call injection) or Phase 4 (synthesis stub creation).** Three reasons, detailed below: (1) the task's premise — many high-value content orphans needing seeding — is mostly false once structural/inbox pages are excluded; (2) the naive 14-thinker relevance score surfaces meta-documents as noise, so unattended injection would spam the wrong pages; (3) a weekly maintenance Sewing Agent already owns this metric, and a 1,000-file unattended mutation conflicts with the project's caution rules. This run instead delivers a **trustworthy baseline + a short, ranked, human-reviewable action list.**

**Most important single finding:** the per-tradition `wiki.md` hub pages (e.g. `traditions/kastrup/wiki.md`, `traditions/fredrickson/wiki.md`, `traditions/stump/wiki.md`) are themselves **orphans** — they link outward to their `prs_triplets`, but nothing links back into them. Reconnecting ~15 hub pages would do more for graph health than seeding a thousand leaves.

---

## A note on method (and a resolver bug I caught)

My first pass reported 960 "unresolved" wikilinks and a slightly higher orphan count. On verification I found the cause: **893 of 1,740 wikilinks are path-qualified** (e.g. `[[traditions/friston/prs_triplets]]`), and my initial resolver only matched on basename/title, so it failed every path-style link. After fixing the resolver to match full relative paths, unresolved links dropped from 960 → **67**, and "connected" hubs rose from 21 → 44.

This matters beyond my own script: **the weekly `connectivity_log.csv` shows the same ~79% orphan rate across every prior run.** If the production Sewing Agent resolves links the same (basename-only) way, it may be systematically *under-counting* hub connectivity. Worth a one-line check of the production resolver. (My corrected orphan count, 2,160, is still close to the historical trend, because path-links mostly feed a few hubs rather than rescuing leaf orphans — but the hub/connected counts are materially affected.)

---

## Phase 1 — Connectivity census

| Metric | Value |
|---|---|
| Total `.md` pages | 2,812 |
| Total wikilinks parsed | 1,740 |
| Genuinely broken targets | 67 occurrences / 20 distinct |
| Orphans (0 backlinks) | 2,160 (76.8%) |
| Sparse (1–2) | 608 (21.6%) |
| Connected (3+) | 44 (1.6%) |

**Distribution:** 0 → 2,160 · 1–2 → 608 · 3–5 → 17 · 6–10 → 11 · 10+ → 16

Full per-page census: `architecture/metrics/bootstrap_backlink_census_2026-06-23.md`.
CSV row appended (existing schema `date,orphan,sparse,connected,total`): `2026-06-23,2160,608,44,2812`.

**Broken links are not a problem.** Of 20 distinct broken targets, the overwhelming majority are template/example tokens living in documentation files — `wikilink` (×26), `Agent Name` (×15), `wikilinks` (×4), `Day-N+1` (×4), `Target`, `link`, `file`, `Q.N article M`. Only ~5 are genuine content misses worth a manual fix: `bioelectric_memory`, `free_energy_and_goals`, `predictive_foraging`, `Aquinas`, `Levin thinker node`.

---

## Phase 2 — Orphan + sparse classification

Every one of the 2,768 orphaned/sparse pages was classified by folder + content heuristics:

| Cat | Meaning | Count | Treatment |
|---|---|---|---|
| **D** | Structural / system (architecture, agents, flags, heartbeat, sessions, master, review…) | **1,676** | Backlinks not expected. Exclude from seeding. |
| **A** | Thinker-tradition content | **611** | Reconnection candidates (but see below — mostly `prs_triplets` leaves). |
| **B** | Inbox residue | **436** | Promote / archive / delete via inbox pipeline — *not* agentic seeding. |
| **E** | Stub (<30 words) | **28** | Need content before they can be connected. |
| **C** | Synthesis pages | **17** | Bridge essays; mostly already linked from `master/cross_program_index`. |

The headline is the **D + B split (2,112 of 2,768)**: more than three-quarters of all "orphans" are pages that by design don't take backlinks (system docs) or are unprocessed inbox items. The knowledge-graph health question is really about category A.

---

## Phase 3 — Why I did NOT auto-seed agentic calls

The task asked me to run 14-thinker relevance mapping on all A/B/C pages (≈1,064) and inject agentic calls wherever score > 0.4. I stopped and surfaced this instead of executing, because:

1. **The premise mostly doesn't hold.** Category A is dominated by `traditions/<thinker>/prs_triplets.md` leaf files — single-tradition, already correctly attached to their own thinker. They aren't disconnected cross-tradition content begging for bridges; they're leaves of a deliberate hub-spoke design.

2. **The relevance heuristic surfaces noise, not signal.** The highest-scoring "multi-thinker" orphans are *meta-documents that simply name every thinker*: `agent_architecture_review.md`, `PETER/THINKERS.md`, `PETER/AGENTS.md`, the `ACPA_2026_*` paper drafts, `inbox/PROCESSED_LOG.md`. Injecting agentic calls into these would be actively wrong. Genuine LLM relevance judgment on 1,000+ pages is also far outside a safe unattended token budget.

3. **Ownership + caution.** A weekly maintenance Sewing Agent already owns orphan detection and the connectivity log. A one-shot, unattended mutation of ~1,000 live vault pages (which feed the published visualization) conflicts with the project's standing caution/surgical-change rules. The correct autonomous output here is a report, not a thousand edits.

**No vault content pages were modified.** Only the two metrics artifacts (census + CSV) and this report were written.

---

## Phase 4 — Synthesis page inventory

The task assumed many bridge/synthesis pages are missing. **They largely already exist.** `synthesis/` holds 45 files, and after the resolver fix, essentially every `[[*_bridge]]` link in the vault resolves to an existing page (only a single bare `[[bridge]]` template token and one already-present `synthesis/friston_levin_bridge` remained flagged, and the latter exists). The vault is **not** signalling unmet demand for new synthesis stubs via broken bridge links. I therefore created **no synthesis stubs** — fabricating them would be speculative content the link graph isn't asking for.

---

## Top reconnection candidates (the actually-useful list)

After excluding meta-docs, inbox duplicates, and sub-60-word stubs, **312 substantive content orphans** touch ≥2 thinkers. The highest-leverage ones:

**Tier 1 — tradition hub pages that are orphaned (fix first):**
`traditions/kastrup/wiki.md`, `traditions/fredrickson/wiki.md`, `traditions/stump/wiki.md` — and likely the rest of the 15 `traditions/<thinker>/wiki.md` hubs. These are the canonical entry points for each tradition yet receive zero inbound links. A single index page (`master/` or `traditions/_index`) linking to all 15 wikis would convert 15 orphans into hubs at once.

**Tier 2 — substantive approved proposals never back-linked:**
`inbox/2026-04-09_hawkins_thousand-brains-deep-read-supplement.md` (6 thinkers, 1,793w), `inbox/2026-04-28_hoffman_stevens-handbook-itp.md` (6, 1,195w), `inbox/2026-05-18_friston_precision-psychiatry-cambridge.md` (5, 1,042w). Note each appears **twice** (`inbox/X` and `inbox/proposals/approved/X`) — a duplication pattern worth de-duping.

---

## Recommended actions for Tom (beyond what the agent should do unattended)

1. **Create a tradition index** linking all 15 `traditions/<thinker>/wiki.md` hubs. Single highest-leverage fix; turns the canonical pages from orphans into hubs.
2. **Check the production Sewing Agent's link resolver** — confirm it resolves path-qualified `[[a/b/c]]` links. If it's basename-only like my first pass, the weekly orphan/connected numbers are skewed.
3. **Run the inbox pipeline on category B (436 pages).** These are residue, not graph problems — promote, archive, or delete. The `inbox/` vs `inbox/proposals/approved/` duplication suggests a stale copy is inflating counts.
4. **Decide the seeding policy explicitly.** If you do want agentic-call injection, scope it to a *reviewed* subset (e.g. the Tier-1/Tier-2 lists), not an unattended full-vault pass. I can execute a bounded pass on your sign-off.
5. **Fix the ~5 genuine broken content links** (`bioelectric_memory`, `free_energy_and_goals`, `predictive_foraging`, `Aquinas`, `Levin thinker node`).

---

## Overall vault-health assessment

**Healthy for its design; not under-connected in the way the raw orphan number implies.** The 77% orphan figure is an artifact of counting 1,676 system pages and 436 inbox items that were never meant to carry backlinks. The genuine knowledge graph — traditions + synthesis — is real and the bridge layer is substantially built out (45 synthesis pages, bridge links resolving). The one true structural weakness is **inbound connectivity to the tradition hub pages**, which is concentrated and cheap to fix (≈15 pages, one index).

The graph is **sufficient to support meaningful thinker-agent synthesis today.** The marginal gain from mass leaf-seeding would be low and noisy; the marginal gain from reconnecting the 15 hubs and clearing inbox residue would be high. Recommend prioritizing the latter.

*— Sewing Agent, bootstrap run 2026-06-23. No vault content pages modified; metrics + report only.*
