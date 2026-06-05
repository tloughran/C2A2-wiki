# Community Explorer Redesign: Sociogram-Pattern Graph Architecture

**Status:** Proposal — awaiting decisions on §8 before Phase 1 begins
**Date:** 2026-06-04
**Author:** Claude (Cowork session, RC Karpathy Wiki Project)
**Related:** `wiki_narration.html` sociogram, `community/index.html`, `explorer.html`

---

## 1. Design Principle

The C2A2 Explorer shell hosts several interactive tools across a tab bar: the sociogram (wiki graph), the Community Explorer, the Summa Explorer, and others. Each tab currently has its own navigational grammar — the sociogram navigates by checkbox filter plus node-click, while the Community Explorer navigates by card-browse, map, or overview mode. A visitor stepping from one tab to the other must context-switch not just the data but the entire interaction model.

The redesign is premised on a single unifying principle: **one navigational grammar across all tabs**. That grammar is: nodes as entities, edges as relationships, checkbox filters as cuts through the space. A user who learns to navigate the sociogram — click a node to read it, use the left panel to filter by tradition or structure group, follow edges to discover related nodes — should be able to sit down at the Community Explorer and navigate it without instruction. The mechanics are identical; only the ontology changes.

This matters acutely for ISME, where the Explorer will be used as a live-presentation tool in front of an audience unfamiliar with either dataset. Every second spent explaining "this tab works differently" is a second lost. Consistency is not an aesthetic goal here; it is a functional one.

The shared pattern that achieves this consistency is: a self-contained, single-file HTML document generated offline by a Python build pipeline, rendering a D3.js v7 force-directed graph on a dark `#0a0a0f` background, with a left-panel checkbox filter system and a right-panel markdown renderer triggered by node click. The sociogram implements this pattern for the wiki vault. The Community Explorer redesign implements it for the 855-community dataset.

---

## 2. The Edge Problem

The sociogram's graph is useful because it is a genuine graph: 1,533 nodes connected by approximately 36,000 edges derived from wikilinks and shared references. The force simulation has real topology to work with, and the clusters that emerge reflect actual intellectual proximity in the vault. Filtering by tradition or structure group reveals coherent subgraphs because the edges encode real relationships.

The Community Explorer, as currently built, has **no edges**. The 855 community records are standalone objects. They share type taxonomies and geographic metadata, but those attributes live in columns of a CSV — they are not encoded as graph relationships. If the current data were fed directly into a D3 force simulation, the result would be 855 dots scattered by gravity with no clustering structure whatsoever. The graph would be visually indistinguishable from noise.

Edges must therefore be synthesized. Four realistic strategies exist, each with different tradeoffs.

**A. Structural edges** connect communities that share a Type + Subtype combination. Implementation is trivial: iterate the dataset, group by (Type, Subtype), and emit edges between all pairs within each group. Runtime is negligible, cost is zero, and the result is immediately available. The problem is density and discrimination. With 528 Academic communities, a naive structural approach produces roughly 139,000 edges among academics alone — the graph becomes an undifferentiated blob. Structural edges are useful as a secondary weight (communities of the same subtype get a baseline affinity) but are too coarse to be the primary relationship signal. They should be included but downweighted, and edge limits may need to be enforced by sampling the k nearest within-subtype neighbors rather than connecting all pairs.

**B. PRS keyword edges** exploit the narrative content already present in the data. Each community record has Problem_Statement, Resource_Statement, and Solution_Statement fields — three short paragraphs describing what the community does and why. TF-IDF vectorization over the concatenated PRS text, followed by cosine similarity computation between all 855×855 pairs, produces a similarity matrix tractable on a laptop in under a minute. Edges are emitted where similarity exceeds a threshold (0.25–0.35 works well empirically for TF-IDF on short texts), optionally weighted by the similarity score. The result is thematically grounded: communities tackling similar problems, deploying similar resources, or proposing similar solutions cluster together, regardless of their formal type or country. This is the most intellectually meaningful edge type available without external APIs, and it is fully reproducible from the source data. The main weakness is that it cannot bridge communities with short or poor-quality PRS text — roughly 150–200 records have sparse or boilerplate narratives, and those will be underconnected.

**C. Geographic/regional edges** connect communities in the same country, or within a defined regional grouping (e.g., EU, Latin America, Anglosphere). These edges are obvious and interpretable — an audience immediately understands why two nodes are connected — and they reveal regional clustering that is genuinely informative. The limitation is that geographic proximity does not imply intellectual proximity. A libertarian think tank in London and a complexity-science institute in London have nothing in common except their city. Geographic edges are best implemented as an optional filter layer: visually dormant by default, togglable via the checkbox panel, useful when the question being explored is "what is happening in this region."

**D. LLM-synthesized similarity** runs each community's full narrative (PRS text plus any additional description) through an embedding model (e.g., `text-embedding-3-small`), computes cosine similarity between all pairs, and emits edges above a threshold. This produces the highest semantic quality: it handles synonymy, recognizes related concepts expressed in different vocabularies, and finds non-obvious connections across type and country boundaries that TF-IDF cannot surface. The cost is real but bounded — 855 records at roughly 150 tokens each is approximately 128K tokens, under $0.02 at current pricing. The result can be cached to disk as a JSON similarity matrix and never needs to be regenerated unless the source data changes. The pipeline requires an OpenAI API key and adds a generation step, which introduces an external dependency.

**Recommended approach:** PRS keyword edges as the backbone, structural edges as a downweighted secondary signal, geographic edges as an optional toggle layer. LLM embeddings are worth running once the data pipeline is stable, as a quality upgrade to the PRS edges — but Phase 1 should not wait on them. The PRS keyword approach is fast enough to iterate on and good enough to reveal genuine structure in the data.

---

## 3. Node File Architecture

The sociogram achieves its "click → rendered markdown" interaction because every node corresponds to a `.md` file in the vault. The content panel on the right renders that file's markdown when a node is selected. For the Community Explorer to offer the same interaction, it needs a markdown representation for each community.

Three architectures are available.

**Option A: Generate per-community `.md` files** creates one file per community in `wiki/community/nodes/`, generated from the source CSV by a script. The file for each community would contain its name, type, country, PRS fields, and URL as structured markdown. This is maximally consistent with the sociogram pattern. It enables the right-panel markdown renderer without any special-casing in the visualization code. It also means 855 new files appear in the vault, which has second-order effects: the sociogram would need to either index or explicitly exclude `community/nodes/`, the janitor would need to know about them, and any vault-wide scripts would encounter a new file type. 855 files is not a large number, but it is a non-trivial addition to a vault currently at ~1,533 nodes.

**Option B: Keep flat data, add edges JSON** leaves the source data as `data.js` and generates a separate `community_graph.json` at build time containing a nodes array and an edges array. The visualization HTML reads this JSON at load time rather than reading per-file markdown. The right-panel content renderer would display structured HTML built from the node's data object rather than rendering a markdown file. This is architecturally lighter — it does not touch the vault — but it diverges from the sociogram pattern in the one place most visible to users: the content panel. It also creates a dependency on the JSON file being present, which partially undermines the goal of a self-contained HTML artifact.

**Option C: Hybrid** generates per-community `.md` stubs only for communities that meet a quality threshold — defined as: has at least one non-boilerplate PRS field populated, has a verified external URL, and is not flagged as a duplicate. Based on the current dataset's distribution, approximately 300–400 of the 855 communities are likely to meet this bar. The graph visualization is built over this curated subset. The full 855 records remain accessible through the cards view (preserved as a secondary tab within the community explorer). Per the sociogram pattern, node click renders the `.md` file; cards view reads from `data.js` as before.

**Recommendation: Option C.** It delivers the sociogram interaction pattern for the portion of the data worth presenting at ISME — the curated, narrative-rich communities — while keeping the vault growth bounded and the full dataset accessible. The quality filter also serves an incidental curatorial function: surfacing which communities need data enrichment before they can be promoted to the graph view.

---

## 4. Checkbox Filter Dimensions

The sociogram's left panel has two filter groups: tradition (14 thinkers, by color) and structure group (10 semantic categories). Both are meaningful cuts through the intellectual topology. The Community Explorer needs equivalent filter dimensions that are both semantically meaningful and consistent with the graph's edge structure.

**Primary filter — Community Type.** Academic / Ideological / Corporate maps cleanly onto tradition as the first filter group. Three values, mutually exclusive, visually distinguishable by color. The type is already clean in the data. This is the equivalent of "which tradition does this node belong to." Recommended colors: Academic in `#5A8EAF` (cool blue, connotes research), Ideological in `#8B5DAB` (purple, connotes vision), Corporate in `#4E8A5E` (green, connotes production).

**Secondary filter — Subtype.** This is the equivalent of structure group, but the current subtype taxonomy is not usable as-is. "Interdisciplinary institution" accounts for 500 of 528 Academic records, and "Libertarian maker network" accounts for 242 of 302 Ideological records. Filtering on these labels produces either almost-all-included or almost-all-excluded states, which is informationally useless. Before building the secondary filter UI, the subtypes need to be rationalized into 8–10 meaningful categories with roughly comparable group sizes. Candidate re-categories: Research University, Independent Institute, Think Tank (market), Think Tank (civic), Maker Network, Foundation, Corporate Lab, Media/Publishing, Movement/Organizing, Other. This re-categorization can be done as a small enrichment pass on the source CSV — either manually or semi-automatically using the community names and PRS text as signals. This is a prerequisite for Phase 2, not Phase 1.

**Tertiary filter — Country/Region.** A third filter panel showing top countries by node count, plus regional groupings (Europe, North America, APAC, etc.). Unlike the sociogram's structure group, this filter is orthogonal to the graph's edge topology (if geographic edges are disabled), which means it reduces the visible node set without changing the graph's clustering structure. This is useful for geographically-framed questions but can be disorienting if the user does not expect it. Implement as a collapsible third panel or as an append to the secondary panel.

**Edge visibility toggles.** Because the Community Explorer will have multiple synthesized edge types — PRS similarity, structural affinity, geographic proximity — the UI should offer per-type edge visibility controls. A small toggle strip above or below the checkbox panels, labeled "Show: PRS similarity / Structural / Geographic," lets the presenter configure the graph's relational layer in real time. This is an important interaction for a live-presentation context: "now let me show you just the geographic connections" is a compelling demo moment.

---

## 5. Build Pipeline Design

The sociogram is built by three scripts run in sequence: `extract_vault_data.py` reads the vault and emits JSON, `generate_visualization.py` reads that JSON and emits the HTML, and `validate_html.py` checks the result. The Community Explorer's build pipeline mirrors this structure exactly.

**`generate_community_graph.py`** is the data layer. It reads the source CSV (or parses `data.js` as fallback), computes PRS keyword edges via TF-IDF cosine similarity, optionally applies structural and geographic edge layers, and writes `community_graph.json`. The output format should match the sociogram's internal data schema as closely as possible: a `nodes` array where each object has `id`, `label`, `type`, `subtype`, `country`, `url`, `prs_summary`, and `content_file` (path to the `.md` stub, if generated); an `edges` array where each object has `source`, `target`, `type` (prs/structural/geographic), and `weight`. The script should also optionally generate per-community `.md` stubs into `wiki/community/nodes/`. Flags: `--output-json PATH`, `--generate-md-stubs`, `--edge-threshold FLOAT` (default 0.25), `--max-edges-per-node INT` (default 15, to prevent hub nodes from dominating). Estimated implementation: one focused session.

**`generate_community_explorer.py`** is the visualization layer. It reads `community_graph.json` and produces a self-contained `community_explorer.html` that embeds the data inline, matching the sociogram's architectural pattern: no external file dependencies, no CORS constraints, deployable by double-click. The visual template should copy the sociogram's D3 force setup, dark theme, checkbox panel layout, and right-panel markdown renderer, parameterized for the community dataset's filter dimensions (Type + Subtype + Country toggles + edge-type toggles). The template rules from the sociogram apply here without exception: regular Python strings, not f-strings; data injection via concatenation; single braces in CSS/JS. Estimated implementation: two to three sessions, depending on how much of the sociogram template can be factored into a shared base.

**`validate_community.py`** checks the output HTML for integrity: verifiable node count against the source JSON, edge count within expected density bounds (too sparse suggests a threshold problem; too dense suggests a filtering bug), JavaScript syntax via `node --check` on the extracted script, and cross-reference of `content_file` paths to confirm that any `.md` stubs listed in the JSON actually exist on disk. This script can be a thin adaptation of the existing `validate_html.py` with Community Explorer–specific checks added.

The three scripts live in a `community-explorer/scripts/` directory in the Cowork session, parallel to `wiki-narration/scripts/`. The generated outputs — `community_graph.json` and `community_explorer.html` — live in the wiki repo at `wiki/community/` (replacing or alongside the current multi-file structure).

---

## 6. Integration with Explorer Shell

`explorer.html` hosts the tab bar and loads tab content via iframes. The current Community Explorer tab loads `community/index.html`, which in turn loads its 7-file JS/CSS bundle and `data.js`. The redesigned Community Explorer would load `community/community_explorer.html` — a single self-contained file — in exactly the same iframe slot. From `explorer.html`'s perspective, the change is a one-line `src` update.

The iframe architecture is the right choice here and should be preserved. Iframes keep each tool's JS and CSS scope isolated, prevent accidental state collisions between the sociogram's D3 instance and the Community Explorer's, and allow each tool to be opened standalone (e.g., `file:///.../community/community_explorer.html` in a presentation context where the full explorer shell is not needed). Consistency with the sociogram's deployment model is an additional argument: both tools are self-contained HTML files loaded in iframes.

The D3.js version must match the sociogram's: D3 v7, loaded from the CDN or embedded inline. Mixing v6 and v7 in sibling iframes is not a problem because iframes are scoped, but having both tools on v7 makes template reuse and debugging simpler.

The `lib/c2a2-search.js` search broker is shared across tabs via the explorer shell's parent frame. The redesigned Community Explorer should register its nodes with the broker on load, allowing cross-tab search to surface Community Explorer nodes alongside wiki nodes. The registration interface is already defined in the broker; the Community Explorer just needs to call `c2a2Search.register({ source: 'community', nodes: [...] })` after its graph data is initialized.

One open question worth flagging: the sociogram currently causes `explorer.html` to hide row 2 (the sub-tab bar) when the sociogram tab is active, because the sociogram has its own internal navigation. Whether the Community Explorer should do the same — or whether it should keep row 2 visible, or have its own row 2 with sub-tabs for graph vs. cards view — is a design decision that depends on how Tom wants to use the tool in a presentation context. This is flagged as Decision 4 in §8.

---

## 7. Phased Implementation Plan

The redesign is scoped into three phases, each producing a testable deliverable. The phases are ordered to surface data-quality issues early and to allow course correction before significant UI investment.

**Phase 1 — Data Foundation** (estimated: 1 session).

The deliverable is `community_graph.json`: a validated graph data file with nodes and synthesized edges, ready to be fed into a visualization. Work: write `generate_community_graph.py`; implement TF-IDF vectorization over PRS fields; tune the edge threshold to produce a graph with 3,000–10,000 edges (roughly 4–12 per node on average); inspect the resulting clusters manually to confirm they are semantically coherent; run structural edge generation as a secondary layer. No UI changes. The session ends with a JSON file on disk and a brief report on cluster quality: what groupings emerged, whether the PRS edges are doing meaningful work, and whether the data needs any cleaning before Phase 2.

No vault files are generated in Phase 1 unless the cluster inspection reveals that per-community `.md` stubs are needed to interpret the graph (unlikely at this stage).

**Phase 2 — Graph Visualization** (estimated: 2–3 sessions).

The deliverable is `community_explorer.html`: a working sociogram-pattern graph view of the curated community subset. Work: write `generate_community_explorer.py` using the sociogram's template as the base; adapt checkbox panels for Type + rationalized Subtype; implement right-panel content display (JSON-sourced structured HTML, or `.md` stub rendering if Option C stubs have been generated); run the full build pipeline; validate with `validate_community.py`. The cards view is preserved as a secondary interaction accessible from within the community explorer HTML (e.g., a toggle at the top), not removed.

Phase 2 is the ISME-ready milestone. If the July timeline requires cutting scope, the Phase 2 deliverable should be treated as the ship target and Phase 3 deferred.

**Phase 3 — Polish and Integration** (estimated: 1–2 sessions).

Deliverables: geographic filter layer added to the checkbox panel; edge-type visibility toggles implemented; per-community `.md` stubs generated for the top 300–400 quality nodes (enabling proper markdown rendering in the right panel); `explorer.html` integration updated if the iframe `src` was not already switched in Phase 2; cross-tab search broker registration implemented. This phase also includes the subtype re-categorization pass if that was deferred from Phase 2 — it is a prerequisite for the secondary filter panel to be useful, so it cannot remain deferred past Phase 3.

---

## 8. Open Decisions

The following questions require Tom's input before build work begins. They are listed in rough priority order — the first two block Phase 1, the rest block Phase 2 or Phase 3.

**Decision 1: Primary edge type.** This document recommends PRS keyword edges (TF-IDF cosine similarity) as the backbone. The alternative is to lead with LLM embedding edges for higher semantic quality, at the cost of an API call and a more complex pipeline. Confirm: PRS keyword edges for Phase 1, with LLM embeddings as an optional Phase 3 upgrade?

**Decision 2: Vault node generation.** Should per-community `.md` files be generated in `wiki/community/nodes/`? This adds 300–855 new files to the vault, which will appear as nodes in the sociogram if that tool indexes `community/` (it currently does not, but the indexer scope would need to be checked). Confirm Option C (curated subset, ~300–400 files), Option A (all 855), or Option B (no vault files, JSON-only)?

**Decision 3: Subtype re-categorization.** The current subtype taxonomy is not useful as a filter dimension. Should the re-categorization happen before Phase 2 (blocking but cleaner) or should Phase 2 ship with a degraded secondary filter and the re-categorization land in Phase 3? This affects presentation quality at ISME if Phase 2 is the ship target.

**Decision 4: Row 2 visibility in explorer shell.** When the Community Explorer tab is active, should `explorer.html` hide row 2 (matching the sociogram's current behavior), keep row 2 visible, or give the Community Explorer its own row 2 sub-tabs for graph vs. cards views? The last option is the most powerful but adds complexity to `explorer.html`.

**Decision 5: ISME scope.** Is Phase 2 sufficient for the July presentation, or is Phase 3 (geographic filter, edge toggles, markdown stubs) needed? If Phase 3 is needed by July, the timeline is tight; if Phase 2 is sufficient, there is comfortable runway.
