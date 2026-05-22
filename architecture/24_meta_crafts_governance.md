---
title: Meta-Crafts and Governance
pathway_id: meta_crafts_governance
status: drafted
created: 2026-05-14
depends_on: [agent_developed_participant, optional_interoperability, institutional_scale]
enables: [meta_visualization_pathways]
isme_critical: no
---

# Pathway 24: Meta-Crafts and Governance

## Purpose

Governance as one example of a craft with its own community of practice, standards, and apprenticeship structure. Same for project management, conflict resolution, facilitation, evaluation. These connective crafts nest inside other crafts and run through the whole system, holding it together.

The C2A2 framework is built on MacIntyre's model of tradition-constituted rational inquiry — traditions as crafts with their own standards, practices, and apprenticeship structures. Pathway 24 recognizes that some crafts are meta-crafts: they don't have a specific substantive domain but instead enable the functioning of all the other crafts. Governance is the paradigm case. Project management is another. Conflict resolution, facilitation, and evaluation are others.

The architectural point is that these meta-crafts are not peripheral to substantive traditions and are not bolted-on infrastructure. They are first-class traditions with their own internal critics, their own debates about standards, their own apprenticeship structures, and their own PRS framings. Recognizing them as such — rather than treating them as policy layers or operational scaffolding — is what allows the C2A2 system to host genuine inter-tradition dialogue at scale. Without explicit governance-as-craft, federation (Pathway 19) becomes informal, institutional deployments (Pathway 20) reproduce existing institutional pathologies, and the agent's own development (Pathway 17) lacks a community-of-practice it is accountable to.

## Function set

*(Cowork-drafted 2026-05-14; not yet validated in walk dialogue.)*

Five pieces:

1. **Meta-craft tradition registration.** Each meta-craft (governance, project management, conflict resolution, facilitation, evaluation, and others to be identified) is registered as a first-class tradition in the perspective lattice (Pathway 04). Each gets its own eager-tier overview, its own key thinkers, its own internal-debate map, its own apprenticeship trajectory.

2. **Connective-layer rendering in the Sociogram.** Meta-crafts appear visually distinct from substantive traditions: a connective layer overlaid on all traditions, with edges to every substantive tradition rather than only to thinkers in their own column. The visualization makes the cross-cutting nature explicit.

3. **Meta-craft PRS framings.** Each meta-craft has its own Problem-Resource-Solution framework. Governance problems are coordination failures and legitimacy crises; governance resources are procedural norms, institutional structures, historical precedents; governance solutions are governance innovations attestable in the literature.

4. **Operational integration.** Meta-crafts inform the system's own operation. The framework's own governance — how DECISIONs are canonized, how PRESUMPTIONs are escalated, how federation peers are admitted, how agent behavior is held accountable — is itself a case of governance-as-meta-craft, with its practices documented in the same lattice the rest of the wiki uses.

5. **Cross-craft mediation registry.** When two substantive traditions meet in inter-tradition dialogue and find themselves disagreeing about something procedural rather than substantive, the relevant meta-craft (typically conflict resolution or facilitation) supplies the framework for the meta-conversation. The system can surface the relevant meta-craft material on demand.

## Architecture sketch

*(Cowork-drafted 2026-05-14.)*

```
                substantive traditions
   ┌─────────┬─────────┬─────────┬─────────┐
   │ Levin   │ Friston │ Hoffman │ ...     │
   │ Aquinas │ Wright  │ Rohr    │         │
   └────┬────┴────┬────┴────┬────┴────┬────┘
        │         │         │         │
        │         │         │         │  ← edges to thinkers
        │         │         │         │
   ┌────┴─────────┴─────────┴─────────┴────┐
   │       meta-crafts (connective)         │
   │  ┌───────────────────────────────────┐ │
   │  │  governance                        │ │
   │  │  project management                │ │
   │  │  conflict resolution               │ │
   │  │  facilitation                      │ │
   │  │  evaluation                        │ │
   │  └───────────────────────────────────┘ │
   └────────────────────────────────────────┘
        │
        │  edges to every substantive tradition
        │  + internal apprenticeship structure
        ↓
   operational integration
   ├─ system's own DECISION-canonization governance
   ├─ federation admission process (Pathway 19)
   ├─ agent accountability community (Pathway 17)
   └─ inter-tradition mediation when needed
```

## Decisions taken

*(Cowork-derived from walk description; subject to Tom's amendment.)*

- **Meta-crafts are first-class traditions, not policy layers.** Governance, project management, conflict resolution, facilitation, evaluation get the same lattice treatment as substantive traditions. They are not subordinate.

- **Connective rendering in the Sociogram.** Visually distinct overlay, edges to every substantive tradition. Makes the cross-cutting nature visible at a glance.

- **Operational integration is non-optional.** The system's own governance is held to the same standards it asks substantive traditions to meet. Self-application closes a credibility loop that arms-length theorizing leaves open.

- **Mediation is available on demand.** When two substantive traditions disagree procedurally, the relevant meta-craft is surfaced. The framework does not impose a meta-craft, but it makes the relevant material accessible.

- **The agent participates in governance.** Pathway 17's continuity-of-character commits the agent to being a participant whose conduct is accountable to a community of practice. That community of practice is itself a meta-craft. The agent's accountability is therefore not a separate question but a case of meta-craft membership.

## Open questions

- How do meta-crafts appear in the Sociogram in practice — as a separate tradition-group? as a connective layer overlaid on all traditions? as a toggle the user can show or hide? The visualization design needs to be prototyped.
- What does the PRS framework look like for governance as a craft in detail? (Sketch: Problems are coordination failures and legitimacy crises; Resources are procedural norms and institutional structures and historical precedents; Solutions are governance innovations. But each axis needs to be populated by someone with governance expertise.)
- How does this interact with FINDING-011 (SUPER-BRIDGE) and the cross-tradition connection architecture? Are meta-crafts the natural carrier of super-bridges, or are super-bridges substantive even when cross-cutting?
- Is governance a thinker-tradition with named central figures (Madison, Habermas, Ostrom...) or a structural category populated by practices rather than authors? Probably both, depending on which meta-craft.
- Who, in the wiki's own social structure, is the apprentice and who is the journeyman in governance-as-meta-craft? Tom? Anyone working on the framework?
- The boundary between meta-craft and substantive tradition is unclear in some cases (theology is substantive but has a strong governance dimension; political philosophy is even more porous). How are boundary cases handled?

## Edges

- **agent_developed_participant (17):** the agent itself participates in meta-crafts; the agent's accountability is a case of governance-as-meta-craft membership.
- **optional_interoperability (19):** inter-instance federation requires governance crafts to function (federation registry governance, admission process, dispute resolution).
- **institutional_scale (20):** institutional deployment will need explicit governance structures; Notre Dame's existing institutional governance is the substrate.
- **meta_visualization_pathways (25):** governance of the pathway system is itself a case of meta-crafts — Pathway 25 reflexively visualizes both substantive and meta-craft pathways.
- **perspective_lattice (04):** meta-crafts get their own perspective-lattice entries with eager-tier overviews and apprenticeship trajectories.
- **honesty_layer (14):** meta-crafts have their own honesty-layer disciplines; what counts as a well-formed claim in governance is different from what counts in physics.

## Provenance / source dialogue

- Session: 2026-05-14 morning walk, Tom on phone in Chat mode, conversation `https://claude.ai/chat/ed8b7056-407d-4a71-8fae-62b08e9613e0`. Source dialogue captured in `morning_walk_2026-05-14.md` and `2026-05-14_pathways_18-25_review.md`.
- Originating framing from the walk: "Governance as one example of a craft with its own community of practice, standards, and apprenticeship structure. Same for project management, conflict resolution, facilitation, evaluation. These connective crafts nest inside other crafts and run through the whole system, holding it together."
- The pathway extends MacIntyre's craft-tradition model into the connective domain: not all traditions are substantive in the way physics or theology are, but the architectural treatment is unified.

## Status

*(Implementation outline drafted by Cowork 2026-05-14; sequencing subject to Tom's amendment.)*

Drafted in prose. Implementation order: (a) enumerate the initial meta-craft set (governance, project management, conflict resolution, facilitation, evaluation, plus any others Tom identifies); (b) seed eager-tier overviews of each in the perspective lattice — likely a candidate for collaborative drafting with subject-matter colleagues; (c) prototype the connective-layer rendering in the Sociogram; (d) document the framework's own governance practices in the same lattice, closing the self-application loop; (e) build the cross-craft mediation surface as a small affordance attached to inter-tradition dialogue. Not ISME-critical; the conceptual case can be presented at ISME without the full implementation. The pathway becomes structurally important once federation (Pathway 19) and institutional deployment (Pathway 20) are live.
