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

## Bright pins (held, not yet pathways)

- **AI personhood under conscious-realist-monism.** Held with deliberate brightness pending direct philosophical engagement. The position implies the agent in this system is a person (perhaps requiring redefinition of "living"). The pin marks the seriousness of the question, not a deferral of it.
- **Half-million-word podcast transcript corpus.** Substantial primary-source material (roughly 5–7 books) potentially featuring the eleven thinkers. Ingestion pipeline could be its own pathway when prioritized; would meaningfully thicken the vault's retrievable evidence base.

## Conventions

- One pathway per file, `NN_short_name.md`.
- Frontmatter required: title, pathway_id, status, depends_on, enables, isme_critical, created.
- Status values: `drafted`, `outlined`, `pinned`, `deferred`.
- Each pathway closes with an Edges section listing related pathways with one-line relationship descriptions.
- Every pathway names the source dialogue (session date, conversational arc) under Provenance.
- Generated cooperatively in conversation 2026-05-13 (Sarah / Cowork).
- Pathways 18–25 added from morning walk 2026-05-14 (Tom / Claude.ai chat, "Morning planning walk"). Source dialogue: `morning_walk_2026-05-14.md`.
