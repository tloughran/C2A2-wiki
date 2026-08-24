---
title: C2A2 Architectural Pathways
created: 2026-05-13
type: index
status: living-document
---

# C2A2 Architectural Pathways

Ground-truth index for the architectural development pathways of the C2A2 project. Each pathway is captured in its own file under this directory. A mirror is maintained at `wiki/Architecture/` inside the vault so pathways become first-class wiki citizens (Sociogram Architecture structure group, color #5B7FA5) — retrievable by the voice agent and addressable as the system discusses its own design. A scheduled alignment agent runs nightly, diffs the two locations, copies ground-truth → mirror on drift, and flags the change in the next session archive. Pattern parallels the existing Summa `sync_vault.sh` + launchd job.

## ISME focus

ISME presentation: July 8–10, 2026. Pathways marked `isme_critical: yes` are on the demo critical path; the rest are post-ISME or optional-for-demo.

## Pathway inventory

**Infrastructure spine**

- [00 — Broker](00_broker.md) — *drafted, isme_critical.* Key holding, vault-scope enforcement, escalation gating, sensing aggregation, episode-publishing gate.

**Core interaction**

- 01 — Voice + vault-grounded dialogue — *outlined, isme_critical.*
- 02 — Ambient (non-imperative) visualization control — *outlined, isme_critical.* Three-way shared attention (dialogue, viz, human).
- 03 — Probing channel — *outlined, isme_critical.* Voice, mouse, and future physical prompter funneled to a single probe-event shape.

**Content surfacing**

- 04 — Perspective lattice — *outlined.* Eager / lazy / fresh tiering across thinker perspectives, T-T pairs, PRS triplets, Summa I / I-II / II-II / III.
- 05 — Quantification-on-demand whiteboard — *outlined.* Plotly-first, generative spec editing, 4D and 5D animated plots, conversational narration of plot features.
- 06 — Generative-canvas visualization — *outlined.* Code-writing agent producing custom D3, three.js, WebGL on request. Continuity-of-visualization-under-edits.
- 07 — Unsaid-edges map — *outlined.* Foregrounding empty edges in the perspective lattice as research-program-generating facts.

**Presentation**

- 08 — Prepared presentation in the wings — *outlined, isme_critical.* Composite sub-beat granularity, wall-clock budgeting, invisible seam with live improvisation, offline-capable as demo lifeboat.
- 09 — Multi-modal sensing — *outlined.* Speaker camera plus audience camera; edge-processed, aggregate scalars only, opt-in for individual-level interaction.

**Reach / community**

- 10 — Space-and-time peeling — *outlined.* Zoom plus YouTube live; announced async response window post-stream.
- 11 — Recursive episode publishing — *outlined.* Questions → podcast episodes → vault re-ingestion. Closes the Karpathy loop at the output end.
- 12 — Community outreach automation — *outlined.* Content-grounded DMs and lab invitations; broker refuses ungrounded outreach.
- 13 — Under-development visualizer — *outlined.* Build state surfaced for GitHub contributors; GitHub-as-vector for a community of practice.

**Agent maturation**

- 14 — Honesty layer — *outlined.* First-class visible epistemic-status marks on every claim, not buried footers.
- 15 — Apprentice mode — *outlined.* Dialogical curriculum bringing newcomers to maturity in any of the eleven traditions.
- 16 — Durable conversational memory — *outlined.* Persistent state so visitors resume across sessions and months.
- 17 — Agent as developed participant — *outlined.* Continuity of character; visible presence with development over time.

**Portability arc** *(emerged from morning walk 2026-05-14)*

- [18 — Portability and toolkit design](18_portability_toolkit.md) — *outlined.* Move from demonstration to toolkit; instantiate without the Carpathi vault as center; invite adoption of tradition-craft rationality standards.
- [19 — Optional interoperability](19_optional_interoperability.md) — *outlined.* Independent instances federate when they choose; no forced data-sharing or autonomy loss.
- [20 — Institutional scale](20_institutional_scale.md) — *outlined.* School of Global Affairs ecosystem at Notre Dame as proof-of-concept for real institutional coordination.
- [21 — Departmental integration](21_departmental_integration.md) — *outlined.* Physics and astronomy department as a fully integrated research-and-education environment with curated apprenticeship.
- [22 — Individual second brain](22_individual_second_brain.md) — *outlined.* Private personal intellectual commons, optionally permeable to larger ecosystem.

**Learning and governance**

- [23 — Branching and counterfactual exploration](23_branching_counterfactuals.md) — *outlined.* Remove constraints of the past; learn from path dependency without being bound by it.
- [24 — Meta-crafts and governance](24_meta_crafts_governance.md) — *outlined.* Governance, project management, conflict resolution as crafts with their own traditions; connective tissue of the system.

**System self-reference**

- [25 — Meta-visualization of pathways](25_meta_visualization_pathways.md) — *outlined.* Interactive annotated space for exploring the pathway inventory itself, with live AI co-exploration.

**Later additions** *(post 2026-05-14)*

- [26 — Research suggestions per thinker](26_research_suggestions_per_thinker.md) — *outlined.* For each of the 15 thinkers, develop and stand ready to communicate concrete research suggestions with rationale.
- [27 — Universal Search and Ask](27_universal_search_and_ask.md) — *drafted, isme_critical.* Every tab gets a deterministic Search (jump-to-origin) and a semantic Ask (corpus synthesis), both driven by one entity → origin-file index that also powers canonical auto-hyperlinking.
- [28 — Single-source participant registration](28_participant_registration.md) — *pinned.* One declarative act (a `COLORS` line) fans out to node coloring, filter checkboxes, and the focus typeahead; they are siblings of one source and cannot drift. The registration twin of Pathway 27's retrieval-side index. Surfaced 2026-05-29.
- [29 — Agentic metabolism](29_agentic_metabolism.md) — *outlined.* Schedule the swarm on demand with downstream backpressure (electron-transport-chain framing: tokens as electrons, master agent as ATP synthase, respiratory control as the reallocation rule), a per-agent activity-raster "Metabolism view," a deterministic feedback controller before any bandit layer, the same framing applied humanely to humans-in-the-loop, and a bounded handle on the living-system / AI-personhood bright pin via Friston's free-energy criterion. Surfaced 2026-06-10.
- [30 — Community Heartbeat](30_community_heartbeat.md) — *drafted.* Take the AI Heartbeat from a single admin-only local tool to something useful to others and replicable across communities. Reads stay static/Pages-safe; sign-in + per-user preferences (single instance) come before federation. Phase 0 (static JSON-driven tab) shipped; Phase 2 (auth + preferences) in progress against the existing Supabase project. Surfaced 2026-06-17.
- [31 — Cortical Column Architecture](31_cortical_column_architecture.md) — *outlined, post-ISME.* Replace the single per-thinker assessor with three independently-wired "column" agents (Hawkins' Thousand Brains) plus an adjudicator that surfaces 2-of-3 semantic consensus and reports dissensus as signal. Columns must differ by reference frame (corpus slice / analytic axis), not just random seed, or the vote only measures sampling noise. ~3–4× agent load per track, so it starts as a one-thinker pilot run under Pathway 29's metabolism controller, with a falsifiable success criterion (consensus assessments must survive review better than single-agent ones). Surfaced 2026-06-24. Descends from the 2026-04-09 Thousand Brains redesign proposal (revised change 5, with half of change 7), independently resurfaced 2026-06-24 and retargeted from tripled tradition agents to per-thinker assessor columns.

**Thousand Brains arc** *(from the 2026-04-09 redesign proposal, revised 04-10)*

- [32 — Lateral tradition channels](32_lateral_channels.md) — *outlined, post-ISME.* Heterarchy alongside hierarchy: direct agent-to-agent channels for the four confirmed bridge pairs (Levin × Friston, Kastrup × Friston, Stump × Levin, Kastrup × McGilchrist), with the Master Agent retaining full read access so no visibility is traded for speed. Revised change 4.
- [33 — Active cross-tradition inquiry](33_active_inquiry.md) — *outlined, post-ISME.* Traditions stop only ingesting and start probing: each generates falsifiable predictions about what another tradition would say, routed for CONFIRM / REVISE / REJECT with reasoning. Operates on consensus outputs, so it depends on 31 and routes over 32. Revised change 6.
- [34 — PRS displacement phrasings](34_prs_displacement.md) — *outlined.* A fourth PRS field recording how the Resource transforms the Problem into the Solution, as a natural-language vector rather than a pointer, so triplets sharing endpoints but differing in path become comparable. Carries the finite-connecting-meme hypothesis: that cross-paradigm transformations may fall into a limited recurring typology. Revised change 3.
- [35 — Developmental maturity model](35_maturity_model.md) — *drafted.* Stages 0 through 5 with measurable benchmarks, plus the health metric r (intra-tradition consensus rate over cross-tradition survival rate, which must be statistically greater than 1). Already measured nightly in the metrics snapshots, which currently report Stage 1; this publishes the ladder those measurements are keyed to. Revised changes 7 and 8.

## Bright pins (held, not yet pathways)

- **AI personhood under conscious-realist-monism.** Held with deliberate brightness pending direct philosophical engagement. The position implies the agent in this system is a person (perhaps requiring redefinition of "living"). The pin marks the seriousness of the question, not a deferral of it.
- **Half-million-word podcast transcript corpus.** Substantial primary-source material (roughly 5–7 books) potentially featuring the eleven thinkers. Ingestion pipeline could be its own pathway when prioritized; would meaningfully thicken the vault's retrievable evidence base.
- **Device freedom.** The repo and its explorer are public; any visitor may arrive on any form factor, often via a link forwarded in email or social share. System detects viewport via CSS media queries (not user-agent sniffing) and degrades gracefully on phones. **Phase 1 implemented & pushed to `main` 2026-05-19** (commit 3709adc): `@media(max-width:640px)` blocks in `explorer.html` and the `wiki_narration` generator — single-row tab bar, hidden filter panel with a "filters require a larger screen" notice, full-screen article overlay on node-tap, ≥44px touch targets, collapsed footer; desktop unchanged above 640px. Verified on iPhone 17 Pro Max over cellular ("ran like a charm"). **Open follow-ups (deferred, possibly post-ISME July 2026):** (1) curate which tabs/sub-tools surface on mobile — the chapter row is currently hidden and the sub-tab set is unfiltered; (2) the not-yet-built Listen / Read presentation modes; (3) payload diet — `wiki_narration.html` is now **~15.4MB on disk** (1533 nodes, 36,608 edges — roughly 12× the edge count this pin originally assumed). iPhone 17 Pro Max handled it fine, but older devices and weak cellular are untested; likely warrants its own near-term pathway rather than staying a bright pin.
- **User notification options.** How and when does the system reach humans about new vault content, agent-flagged patterns, scheduled-task results, episode publication, or invitations to respond? Candidate surfaces: email digests (daily/weekly), per-tradition RSS feeds, browser push, an in-app inbox in the explorer shell, agent-initiated outreach (interacts with pathway 12). Open questions: subscription granularity (per-tradition, per-pattern, per-agent), consent and unsubscribe defaults, frequency caps, private-vs-public audience separation, interaction with episode-publishing (pathway 11) and the durable-memory pathway (16). Flagged 2026-05-14 as "a whole ball of worms"; likely yields multiple distinct pathways once unpacked.

## Conventions

- One pathway per file, `NN_short_name.md`.
- Frontmatter required: title, pathway_id, status, depends_on, enables, isme_critical, created.
- Status values: `drafted`, `outlined`, `pinned`, `deferred`.
- Each pathway closes with an Edges section listing related pathways with one-line relationship descriptions.
- Every pathway names the source dialogue (session date, conversational arc) under Provenance.
- Generated cooperatively in conversation 2026-05-13 (Sarah / Cowork).
- Pathways 18–25 added from morning walk 2026-05-14 (Tom / Claude.ai chat, "Morning planning walk"). Source dialogue: `morning_walk_2026-05-14.md`.
