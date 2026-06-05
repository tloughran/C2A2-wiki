# Community Explorer — Recent Work & Way Forward

*Last updated: 2026-06-05*

---

## What Was Done

### 1. Architecture Audit
Read the full existing Community Explorer codebase (`community/index.html`, `data.js`, `app.js`, and six supporting files). Mapped how the tab is invoked from `explorer.html`, what data it holds, and how it relates to the rest of the system.

Key finding: the existing 855 records were bulk-scraped artifacts (500 universities from a domain list, 242 SpaceAPI nodes) with no edges between communities and no substantive PRS. Good enough for a card/search interface; not enough for a graph.

### 2. Architecture Design Document
Written and saved to `wiki/architecture/community_explorer_redesign.md`.

Covers: the unifying design principle (one navigational grammar across all tabs), the edge problem and four strategies for solving it, three node-file architecture options, checkbox filter dimensions, the three-script build pipeline, explorer shell integration, and a phased implementation plan with open decisions.

### 3. Taxonomy Decision
Eight community types confirmed:

| Type | Description |
|------|-------------|
| Tradition-Constituted Enquiry | Academic communities organized around an identifiable intellectual tradition |
| Practice Communities | Communities organized around a shared practice with internal standards of excellence |
| Contemplative & Spiritual | Communities of religious or contemplative practice with articulated truth-seeking |
| Civic & Political | Communities organized around a conception of the common good |
| Scientific Frontier | Research communities at the edges of established paradigms |
| Interdisciplinary Synthesis | Communities explicitly bridging traditions or disciplines |
| Local & Embodied | Geographically rooted communities practicing forms of shared life |
| Professional Guilds | Communities organized around a profession with apprenticeship and tradition-transmission |

Subtypes are emergent — assigned when they genuinely clarify, skipped otherwise.

### 4. Community Curation — First Pass
Search agent ran targeted semantic searches for all 8 types. Results saved to:
- `wiki/community/curated_communities.json` — 157 records
- `wiki/community/curation_report.md` — full breakdown, exemplary PRS samples, gap analysis

| Type | Count | Notes |
|------|-------|-------|
| Tradition-Constituted Enquiry | 24 | On target |
| Scientific Frontier | 23 | On target |
| Civic & Political | 21 | On target |
| Contemplative & Spiritual | 21 | On target |
| Local & Embodied | 19 | Close |
| Interdisciplinary Synthesis | 18 | Close |
| Practice Communities | 17 | Needs second pass |
| Professional Guilds | 14 | Hardest type — needs targeted search |

Quality split: 46 exemplary (Q3) / 111 good (Q2). All 157 meet the bar (prs_quality ≥ 2).

---

## Confirmed Design Decisions

- **Primary edge type:** PRS keyword similarity — edges between communities tackling similar problems. Only where PRS is substantive.
- **Node files:** Per-community `.md` stubs (hybrid Option C) — graph view over the curated subset (~157 nodes now), cards view kept for broader browsing. Community files live in `wiki/community/nodes/`, separate from the vault thinker space.
- **Subtypes:** Emergent, not imposed.
- **Explorer integration:** Community Explorer stays as its own separate tab. The new visualization loads as `community_explorer.html` into the existing iframe — no change to tab structure or row2 behavior.
- **Not connected to the sociogram:** Community graph is self-contained. Nodes do not appear in `wiki_narration.html`.
- **ISME scope:** Decision deferred.

---

## Way Forward

### Phase 1 — Data Foundation (1 session)
**Goal:** Produce `community_graph.json` — the node/edge dataset that feeds the visualization.

Steps:
1. Write `scripts/generate_community_graph.py`
   - Reads `curated_communities.json`
   - Computes TF-IDF keyword overlap across PRS fields (problem + resource + solution)
   - Builds weighted edge list (threshold: overlap score ≥ 0.15 recommended; tune after seeing edge density)
   - Outputs `community_graph.json` with nodes array + edges array
2. Run the script and inspect output
   - Check edge density (target: average 3–8 edges per node)
   - Check that edges cluster by genuine thematic similarity, not just shared boilerplate words
   - Tune threshold if needed
3. Optional top-up: run a second search pass for Professional Guilds (currently 14, target 20+) and Practice Communities (17, target 20+)

**Deliverable:** `wiki/community/community_graph.json` validated and ready to feed a D3 layout.

### Phase 2 — Graph Visualization (2–3 sessions)
**Goal:** Build `community_explorer.html` — a self-contained D3 force-directed graph that replaces the current cards/search interface.

Steps:
1. Write `scripts/generate_community_explorer.py`
   - Reads `community_graph.json`
   - Generates self-contained HTML (mirroring `wiki-narration/scripts/generate_visualization.py`)
   - Dark theme (`#0a0a0f`), D3.js v7, node colors by type
   - Left panel: checkbox filters by Type (8 values) + Subtype (emergent labels)
   - Node click → right panel with rendered community markdown (name, description, PRS)
   - Edge display: lines between nodes, weighted by PRS overlap score
2. Generate and validate locally (`python3 -m http.server 8080` from `wiki/`)
3. Update `explorer.html` to load `community_explorer.html` in the Community tab iframe

**Deliverable:** `wiki/community_explorer.html` rendering correctly in local HTTP review, ready for push sign-off.

### Phase 3 — Polish (1–2 sessions, after Phase 2 review)
- Geographic filter layer (country/region toggle)
- Edge-type toggles (show/hide PRS similarity / structural / geographic independently)
- Quality filter (show only Q3 exemplary nodes, or Q2+Q3)
- Second-pass curation to fill thin types and add new communities as they're discovered
- Periodic regeneration pipeline (cron or manual trigger)

---

## Files to Know

| File | Description |
|------|-------------|
| `wiki/community/curated_communities.json` | 157 curated community records with PRS |
| `wiki/community/curation_report.md` | Quality breakdown, exemplars, gap analysis |
| `wiki/architecture/community_explorer_redesign.md` | Full architecture decision document |
| `wiki/community/NEXT_STEPS.md` | This file |
| `community/index.html` | Current Community Explorer (cards/search — preserved until Phase 2 ships) |
| `community/data.js` | Original 855-record dataset (preserved as source for cards view) |

---

## Start Phase 1?
Phase 1 is unblocked. Say the word and I'll write `generate_community_graph.py`, run it, and report on edge density and cluster quality before touching any UI.
