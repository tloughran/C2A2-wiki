# Sewing Agent — C2A2 Wiki Bootstrap Audit Report

**Run date:** 2026-06-28 · **Mode:** autonomous (Tom not present) · **Type:** one-time full survey

This report covers the full-vault backlink census, orphan classification, and the disposition of the agentic-call seeding pass. It is append-only; no existing vault content was modified. Two companion files were written: the full census at `architecture/metrics/bootstrap_backlink_census_2026-06-28.md` and a new row in `architecture/metrics/connectivity_log.csv`.

## Headline finding

The vault is **wikilink-sparse but reference-dense**, and its *thinker content is already well connected*. The orphan population is not a synthesis problem — it is overwhelmingly (a) structural/system pages that are orphaned by design and (b) inbox process residue. Only **9** thinker-tradition pages are under-connected, and most of those are tradition hub files that link outward rather than being linked to. The knowledge graph is sufficient to support meaningful thinker-agent synthesis today; the bottleneck is not connectivity.

A direct consequence: **Phase 3 as written (inject agentic calls into all category A/B/C pages) was deliberately NOT executed.** It would have stamped boilerplate into ~480 files — 456 of them inbox process-artifacts — and conflicts with the project's standing caution/surgical-change rules and the per-session token budget. Rationale and a bounded alternative are in the *Phase 3 disposition* section. This is surfaced loudly rather than partially-done-and-called-complete.

## Phase 1 — Connectivity census

Scope: all `.md` under `wiki/` excluding `node_modules/` (3,031 pages). Edges: explicit `[[wikilinks]]` only — this is a pure backlink census and does **not** count the shared-reference edges that produce the Sociogram's ~70k edges.

| Bucket | Count |
|---|---|
| Orphan (0 backlinks) | 2,337 |
| Sparse (1–2) | 647 |
| Connected (3+) | 47 |
| **Total** | **3,031** |

Distribution: 0 → 2,337 · 1–2 → 647 · 3–5 → 16 · 6–10 → 12 · 10+ → 19. Only 1,836 wikilinks exist across 3,031 files (73 unresolved). The census proportions track the live weekly sewing agent's history closely (its 2026-06-23 row: 2,160 / 608 / 44 / 2,812), confirming methodology consistency.

**CSV note (conflict surfaced):** the task spec proposed the header `date,orphan_count,sparse_count,connected_count,total_pages`, but `connectivity_log.csv` already exists with header `date,orphan,sparse,connected,total` and seven rows of history back to 2026-05-10. Per the project's "match existing conventions" rule I appended to the existing schema rather than forking a second header. The task's premise that this file does "not yet exist" is stale — the maintenance pipeline is already live (see *Bootstrap-vs-maintenance* below).

## Phase 2 — Orphan classification

All 2,984 orphan+sparse pages classified by deterministic path/size heuristics (model not used — Rule 5):

| Category | Count | Meaning |
|---|---|---|
| D — Structural | 2,474 | `architecture/`, `vault/` (Summa refs), `heartbeat/`, `agents/`, system/root pages. Orphaned by design; need no backlinks. |
| B — Inbox residue | 456 | `inbox/**` — proposals, logs, READMEs, processed artifacts. |
| E — Stub (near-empty <200B) | 28 | Need content before they can be connected. |
| C — Synthesis potential | 17 | `synthesis/**` bridge pages with ≤2 backlinks. |
| A — Thinker content | 9 | `traditions/**` under-connected pages. |

The A set is tiny and mostly hub files: `traditions/{carroll,wright,kastrup,stump,fredrickson,arkanihamed,rohr}/wiki.md` (each links outward; nothing links in), one Loughran dialogue, and `traditions/loughran/papers/README.md`. These are navigational gaps in the hub pages, not missing synthesis.

## Phase 3 — Agentic-call seeding: disposition (NOT executed)

Phase 3 instructs injecting agentic calls into **all** A/B/C pages with per-page relevance mapping against 14 thinkers. I did not execute this. Four convergent reasons:

1. **The evidence inverts the premise.** The task's own "most relevant to multiple thinkers" heuristic ranks pages by how many thinker names they mention. Run against the actual vault, the top results are `inbox/PROCESSED_LOG.md` (14 thinkers), `inbox/proposals/approved/2026-05-12_repair_manifest.md` (12), and several inbox READMEs — process artifacts that mention every thinker precisely because they are logs. Seeding agentic calls into these would inject noise, not synthesis hooks.

2. **Scale vs. token budget (surfaced, not silently overrun — Rule 6/12).** ~482 actionable A/B/C pages, each requiring a read + 14-way relevance judgment + a write, is roughly two orders of magnitude beyond the per-session token budget. Doing a silent partial pass would violate fail-loud.

3. **Surgical-change rule (Rule 3).** 456 of the 482 are inbox residue owned by the inbox pipeline. The correct disposition for un-promoted inbox pages is a pipeline decision (process / archive / delete), not stamping an identical `[→ C2A2 Orchestrator]` boilerplate into 456 files in one unreviewed automated blast.

4. **Redundancy.** A live `c2a2-sewing-agent-weekly` task already owns orphan/sparse detection and writes `connectivity_log.csv`. Thinker content is already connected (9 sparse pages), so there is no synthesis-connectivity emergency to bootstrap against.

**Bounded alternative recommended (for a reviewed session, not an unattended cron):** wire the ~9 tradition hub pages into their neighbors (add inbound links from each tradition's child notes to its `wiki.md`), and triage the 456 inbox pages through the inbox pipeline in dated batches. Both are small, reviewable, and high-signal.

## Phase 4 — Synthesis inventory

14 thinkers → 91 possible pairs. **45 bridge pages exist; 46 are absent.** Loughran (the integrator tradition) already has all 13 of its bridges. No synthesis stubs were auto-created — many of the 46 absent pairs are plausibly intentional (not every pair warrants a bridge), and mass-creating 46 stub files repeats the Phase 3 anti-pattern. The 46 missing pairs are listed in the companion data for Tom to prioritize; the highest-value candidates are pairs where both traditions already have rich, mutually-referencing content (a judgment call best made interactively).

## Top 10 highest-potential under-connected pages

By thinker-keyword breadth, filtered to genuine content (process logs excluded):

1. `traditions/carroll/wiki.md` (10 thinkers, bl=2) — hub needing inbound links
2. `traditions/wright/wiki.md` (8, bl=1)
3. `traditions/kastrup/wiki.md` (8, bl=1)
4. `traditions/arkanihamed/wiki.md` (bl=2)
5. `traditions/rohr/wiki.md` (bl=2)
6. `traditions/stump/wiki.md` (bl=1)
7. `traditions/fredrickson/wiki.md` (bl=1)
8. `traditions/loughran/papers/README.md` (bl=0)
9. `traditions/loughran/dialogues/.../2026-05-20_narrative-connectome-and-the-form-of-partnership.md` (bl=1)
10. The 17 C-category `synthesis/*_bridge.md` pages with ≤2 backlinks — wire each into both parent tradition hubs.

## Recommended actions for Tom (beyond the agent)

- **Reconcile bootstrap-vs-maintenance.** This "one-time bootstrap before moving to a maintenance schedule" ran *after* the maintenance pipeline was already live (7 CSV rows since 2026-05-10). Decide whether this bootstrap task should be retired or repurposed, so it doesn't double-count against the weekly sewing agent.
- **Decide inbox-residue policy.** 456 un-promoted inbox pages dominate the orphan count. A one-time pipeline triage (process/archive/delete) would shrink the orphan number far more than any link-seeding.
- **Treat the 9 hub pages as a navigation fix,** not a synthesis fix — add inbound links from child notes.
- **Confirm the wikilink-vs-reference framing.** Connectivity here looks alarming (2,337 orphans) only because shared-reference edges are excluded. If wikilink backlinks aren't the intended health metric, the maintenance agent's orphan definition may be measuring the wrong thing.

## Vault health assessment

**Healthy enough for thinker-agent synthesis.** The traditions are richly populated and mutually referencing; 45 bridges already exist; the integrator tradition is fully bridged. The large orphan count is an artifact of (a) excluding shared-reference edges and (b) inbox/structural pages that should not carry backlinks — not a deficit in the substantive knowledge graph. The single most useful next move is inbox-residue triage, not link injection.

---
*Files written this run: `architecture/metrics/bootstrap_backlink_census_2026-06-28.md`, `architecture/metrics/connectivity_log.csv` (+1 row), this report. No vault content pages were modified. No git push performed (constitutional rule: no blind pushes).*
