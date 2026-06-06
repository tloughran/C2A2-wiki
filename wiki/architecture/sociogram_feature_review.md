# Sociogram Feature Review → Community Explorer Integration Analysis

*Date: 2026-06-05. Basis: control inventory extracted from the shipped `wiki_narration.html` (2026-06-02 regen), `community_explorer.html` v2 (commit 1514b88), and the cards app (`community/index.html` + `app.js`).*

**Purpose:** For every sociogram feature, decide whether it belongs in the Community Explorer graph view, and why. Then compare a "grown-up" (fully featured) Community Explorer graph against the Cards view, and lay out the pathways for their relationship.

---

## 1. Feature-by-feature review table

Status key: **SHIPPED** = already in CE v2 · **YES** = integrate · **ADAPT** = integrate in modified form · **DEFER** = integrate later, blocked on data/feature · **NO** = do not integrate.

| # | Sociogram feature | What it does there | CE verdict | Why / why not |
|---|---|---|---|---|
| 1 | Force-directed graph, zoom/pan, drag | Core topology display | **SHIPPED** | The unifying grammar itself. |
| 2 | Node click → right content panel | Renders the node's markdown article | **SHIPPED** | CE renders structured PRS from JSON instead of .md — same interaction, different source (see §3, node-file question). |
| 3 | Edge click → both endpoints in panel | Shows the relationship's two sides | **SHIPPED** | Identical value: an edge IS the inter-community claim. |
| 4 | Checkbox filters: traditions (14) / structure (10) | Cuts through the space | **SHIPPED** | CE analogue: 8 community types + Q3 toggle. |
| 5 | Hold Forces / Hover Names / Fit All | View stabilization & orientation | **SHIPPED** | Ported 1:1 for grammar consistency. |
| 6 | Search box with `focus:` / bare-guess grammar | **Transient highlight lens, NOT a filter** (LOCKED design decision 2026-05-29) | **YES — next increment** | 156 unlabeled dots already need name lookup. Inherit the locked semantics exactly: search highlights, checkboxes filter, the two never sync. Highest value-per-effort of anything in this table. |
| 7 | Ask AI semantic search (Pathway-00 broker) + "Allow wider search" (web_enrich) | NL queries answered from corpus, optionally web-grounded | **YES — via shared module** | `lib/c2a2-search.js` was built precisely for this (one broker client, multiple surfaces). The cards app already carries the broker-ready seam. This is also the first concrete *integration point* between graph and cards: one search pipeline, two renderings (§4, P1). |
| 8 | Edge-type checkboxes (wikilink / mention / reference; crosses / within category) | Toggle edge layers independently | **DEFER → YES** | CE has exactly one edge type today (PRS similarity), so the control would be vacuous. It becomes the natural UI the moment the redesign doc's strategies A (structural, downweighted) and C (geographic, dormant-by-default) land. Build the layers first, then this control. |
| 9 | Tag checkboxes (finding / decision / cross / open) | Filter by wiki-authoring tags | **NO** | Tags are artifacts of wiki authorship; community records have no tag taxonomy. The analogue CE actually needs — quality tier — already shipped (Q3 toggle). Inventing tags here would be speculative structure. |
| 10 | Score modes (Balanced / Connected / Cross-tradition / Editorial) | Re-weights node prominence | **ADAPT** | Port as Balanced / Connected / **Cross-type**. Cross-type emphasis surfaces bridge communities — the C2A2 thesis made visible, and a strong ISME beat ("these are the communities already doing inter-tradition work"). Editorial mode has no CE meaning yet (no editorial layer). Low cost: it's a node-scoring function. |
| 11 | Layout modes (Free / Discipline × Year) | Structured vs organic layout | **DEFER → ADAPT** | CE analogue: Free / **Type × Geography**. Year is impossible today — records carry no founding dates. Type × Geography needs no new data and reads instantly for an audience. Worth doing before ISME; Year variant only if a curation pass adds dates. |
| 12 | Date slider ("Since") | Temporal cut over node dates | **DEFER** | No date metadata on community records. Two candidate date semantics, decide when adding: *founding year* (history of the communities) vs *date-added* (growth replay of the directory — a nice live-demo narrative). Phase 3. |
| 13 | Brightness slider | Cosmetic edge/node luminance | **YES — trivial** | Ten lines, and dense graphs genuinely need it for projection screens. |
| 14 | Narration tracks (History/Recent/Latest × Brief/Deep) + TTS (browser + OpenAI voices) + settings gear | Self-narrating graph | **DEFER** | Narration is generated from the wiki's changelog — a temporal record CE doesn't have. Prerequisite chain: date-added metadata (#12) → curation log per pass → "Recent additions" track. Genuinely powerful for ISME if it lands, but it's the most expensive item here and sits behind two dependencies. Don't start with it. |
| 15 | Help "?" popovers per control group | In-place explanation | **YES — cheap** | ISME audience will be cold; every control group should explain itself. Same pattern, same CSS. |
| 16 | Panel go-to / come-back navigation | Jump to linked node, return | **ADAPT** | CE already chains through "Connected communities" clicks but has no back-stack. Add a simple history stack + back button in the right panel. Cheap, completes the grammar. |
| 17 | Crash-proofing (MAX_NODES 20000 / MAX_EDGES 30000, 80% warnings) | Guard against runaway regen | **NO — not yet** | 156 nodes / 640 edges is two orders of magnitude below danger. Add the guard only if the graph ever ingests the full 855+ or edge strategies multiply edge count past ~5k. |
| 18 | On-load narrator (~3s intro) | Spoken orientation on open | **NO** (and it's currently a known regression in the sociogram itself, backlog item 4) | Fix it where it lives first; revisit for CE only after #14 exists. |
| 19 | Record button | Capture demo sessions | **SHIPPED** (shell-level) | Lives in `explorer.html` row 1; CE inherits it for free. |
| 20 | Per-node `.md` files in the vault | Sociogram nodes ARE wiki files | **OPEN QUESTION** | The redesign doc chose hybrid Option C (md stubs for curated communities in `wiki/community/nodes/`) but v2 shipped JSON-injection instead, which works and is lighter. Generating the stubs buys: agent-editable community pages, janitor coverage, and (if ever wanted) sociogram ingestion — but the standing decision says community nodes stay OUT of the sociogram. Recommend: revisit only when an agent actually needs to *write* to a community page (e.g. claim/refinement workflow). Don't generate 156 files nobody edits. |

**Suggested build order for the YES/ADAPT set:** 6 → 7 (shared pipeline) → 13 → 15 → 16 → 10 → 11, with 8 unlocking after edge-layer work. Items 6+7 together are roughly one session given `c2a2-search.js` exists.

---

## 2. The grown-up graph vs the Cards view

Assume the YES/ADAPT column lands. What does each surface then do better?

| Dimension | Grown-up CE graph | Cards view |
|---|---|---|
| Primary verb | **Explore / relate / discover** | **Find / browse / register** |
| Question it answers | "Who is near whom, and why?" | "What exists, and what exactly is it?" |
| Data coverage | 156 curated (Q2+) | All 855, including seed-quality records |
| Relationships | Its whole point (PRS edges, cross-type bridges) | None — records are islands |
| Faceted query (country, subtype, source, free text) | Weak — checkboxes only | Its whole point |
| Reading a full record | Good (right panel) | Better (purpose-built cards, GPRS reader) |
| Self-articulation seam (claim / refine / progress-tracking stubs) | Absent | Present — built search-first 2026-05-21 for exactly this |
| Audience presentation (ISME) | Strong — clusters are arguments | Weak — a directory doesn't perform |
| Agent interaction surface | Read-mostly | The claim/refinement seam is the broker-ready write path |

The decisive observation: **these are not two versions of one tool; they are two verbs over one dataset.** The cards view is the instrument a community uses *on itself* (per the community model: self-first GPRS articulation, opt-in visibility). The graph is the instrument the *network* uses to understand inter-community structure. Killing either loses a function the other cannot absorb.

---

## 3. Relationship pathways

**P1 — Federated sub-tabs (shipped v2, + shared services).** Keep Graph and Cards as sub-tabs; unify what's behind them: one search pipeline (`c2a2-search.js`) so the same query box works on both surfaces, and cross-navigation hand-offs — a "show in graph" button on any curated card, a "view full card" link in the graph's right panel (keyed by shared `community_id`). Cost: small. This is the pre-ISME move.

> **CORRECTION (2026-06-05, P1 build session):** the "shared `community_id`" premise was false in the data at that time. The graph's 156 curated communities (`curated_communities.json`, ids `CC-001`…) and the Cards directory's 855 records (`data.js`, ids `C0001`…) were disjoint id spaces — 0 id matches, 3 name matches, 5 url-host matches. Cross-navigation hand-offs were therefore deferred, and P1 shipped as search box + shared Ask AI pipeline only.
>
> **UPDATE (2026-06-06):** resolved. The 156 curated communities were merged into the Cards directory under their own `CC-xxx` ids (`scripts/generate_community_cards_data.py`; cards now 1006, dedupe of 5 bulk overlaps), so the graph is now a literal id-subset of the cards. This was prompted by two falsehoods Tom flagged in the "?" popover: (1) no community has approved any record — all data is from public web pages (now disclosed in the popover + `explorer_tabs_complementarity.md`); (2) the graphed set was not a subset of the carded set (now it is). The cross-navigation hand-off is now mechanically possible on the shared key; its UI remains a future increment.

**P2 — Graph-primary shell.** Graph is the landing view; "Browse all" raises the cards as an overlay pre-filtered to the current graph cut (checked types, search hits). Cards become a drawer of the graph rather than a sibling. Cost: medium. Gain over P1 is mostly aesthetic; defers the real question.

**P3 — One app, two projections (the architecture target).** Single dataset (all 855, quality-tiered), single state model; cards and graph are two *renderings* of the same filtered selection. The bridge between them becomes a **promotion pipeline**: a record enters as seed (cards-only) → a community claims it and articulates GPRS → quality crosses Q2 → it *appears in the graph* and grows edges. Graph membership stops being a curatorial fiat and becomes something a community earns by self-articulation — which makes the graph itself a measurement surface (who has articulated, who is connecting). This is the version aligned with the C2A2 long game, and the version where agents have a natural write-path. Cost: largest; touches data model, both UIs, and the broker seam.

**P4 — Keep only one.** Not recommended. Graph-only orphans 699 seed records and the registration seam; cards-only forfeits the relational evidence that justifies the whole accelerator/detector framing.

**DECIDED 2026-06-05 (Tom): P1 now; P3 is the someday target.**

**Recommendation (ratified):** P1 now — it is cheap, ISME-safe, and every piece of it (shared pipeline, id-keyed hand-offs) is load-bearing in P3 later. Declare P3 the target architecture and let the promotion pipeline be designed as its own increment, because that pipeline — not the UI — is the actual integration: the quality gate is the membrane between directory and graph.

---

*Carried decisions honored: search = highlight lens, never filter (2026-05-29 LOCK); community graph stays disconnected from the sociogram; subtype filters dropped (140 subtypes / 156 nodes — badge, not checkbox).*
