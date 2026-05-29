---
title: Research Suggestions per Thinker
pathway_id: research_suggestions_per_thinker
status: outlined
created: 2026-05-15
depends_on: [apprentice_mode, honesty_layer, agent_developed_participant, outreach_automation, episode_publishing]
enables: []
isme_critical: no
---

# Pathway 26: Research Suggestions per Thinker

## Purpose

For each of the 15 thinkers in the C2A2 network — Levin, Friston, Hoffman, Kastrup, McGilchrist, Hawkins, Wolfram, Carroll, Arkani-Hamed, Fredrickson, Stump, Rohr, Wright, MacIntyre, Loughran — the project develops and is prepared to communicate concrete research suggestions, together with rationale.

A suggestion is not a recruitment pitch into the project's emerging paradigm. It is a serious, respectful proposal of the form: *given your existing research program, here is a direction the C2A2 synthesis suggests you might productively explore, and here is why — in continuity with your own work, and what it would unlock when read against the wider network.* The suggestions are calibrated to each thinker's actual program, not generic; they emerge from the agent's sustained engagement with the tradition wikis and the cross-program convergences the project has surfaced.

Pathway 26 exists because the project's claim to be an *accelerator/detector system for developing communities into sustained and articulate traditions* is hollow if the system has no productive output back to the thinkers whose traditions it has been articulating. The asymmetry between *we have read all of your work and located convergences across your fields* and *we have nothing to say back to you* is one the system should close. Pathway 26 is the venue where the system addresses each thinker as a genuine interlocutor rather than as a source.

This pathway is the *outbound* face of the project. Pathways 11–13 cover episode publishing, community outreach, and the developer-facing under-development view. Pathway 26 is the analogous outbound channel addressed to the thinkers themselves.

## Function set

*(Outlined; full design awaiting the late-next-week prioritization discussion.)*

The pathway has five expected pieces. Specific commitments to depth, format, and venue are deferred to the scheduling discussion.

1. **Per-thinker dossier.** One file per thinker, structured for serial consumption (introduction → existing program → C2A2-derived suggestions → rationale → 2–3 specific questions the project would want to put to them). Mirrors the `wiki/traditions/{thinker}/` structure so dossiers slot in as `wiki/traditions/{thinker}/research_suggestions.md` alongside the tradition wiki itself.

2. **Cross-thinker network view.** A map of which suggestions implicate which other thinkers — i.e., where Friston's suggested direction touches Levin's, where Wright's touches Rohr's, where Hoffman's touches Arkani-Hamed's. The pathway is not just 15 independent documents but 15 nodes in a graph of suggestions-that-implicate-each-other.

3. **Rationale layer.** Each suggestion carries an explicit rationale of two faces: *continuity with the thinker's existing program* (so the suggestion reads as a natural extension, not an unsolicited reframe) and *unlocked-value for the C2A2 network* (what cross-tradition synthesis the suggestion would enable). The two faces are equally weighted; the project does not subordinate the thinker's research interests to its own synthesis aims.

4. **Epistemic markings.** Every suggestion is honesty-layer-marked (Pathway 14) for its grounding strength: *grounded in the thinker's published positions* vs. *extrapolated from the thinker's program* vs. *speculative*. No suggestion gets to look more authoritative than its grounding.

5. **Communication channels (deferred).** Whether dossiers stay internal as project planning artifacts, get shared selectively with thinkers in advance of meetings, are published openly, or arrive in some other form is part of the late-next-week discussion. Pathway 26 is platform-agnostic at the dossier-content layer.

## Architecture sketch

```
        wiki/traditions/{thinker}/wiki.md   (tradition source)
                            │
                            │  read into
                            ↓
        agent's sustained engagement (Pathway 17)
        + apprentice-mode maturity in tradition (Pathway 15)
                            │
                            ↓
        cross-program convergences from Karpathy Wiki
        (CROSS-NN, FLAG-NN, PRS-NN as already encoded)
                            │
                            ↓
        per-thinker dossier draft
        ├─ existing program summary
        ├─ suggested directions (2–4 per thinker)
        ├─ rationale per suggestion
        │   ├─ continuity face
        │   └─ unlocked-value face
        ├─ specific questions to put to the thinker
        └─ epistemic markings per claim (Pathway 14)
                            │
                            ↓
        cross-thinker network view
        (which suggestions implicate which other thinkers)
                            │
                            ↓
        communication channel (deferred)
```

## Decisions taken

*(Minimal — most commitments deferred to the scheduling discussion.)*

- **One file per thinker, mirroring the tradition wiki structure.** Not a single monolithic document. This makes dossiers maintainable independently and lets each thinker's dossier evolve as their own work and the project's understanding does.

- **Continuity + unlocked-value as a two-faced rationale.** Suggestions are framed to be productive *from the thinker's existing program* as much as for the C2A2 synthesis. The pathway does not subordinate the thinker's research interests to the project's.

- **Honesty-layer markings on every claim.** No suggestion appears without its grounding strength visible. Pathway 14's machinery applies here.

- **Soft thinker-voice convention applies (M criterion).** Per `summa_thinker_voice_convention.md`, the dossiers cite the thinker's work as a resource; they do not classify the thinker into hard role-categories ("X is THE authority on Y"). The same principle that governs the Summa 2026 synthesis prose governs the research-suggestions dossiers.

## Open questions

*(All deferred to the late-next-week prioritization and scheduling discussion.)*

- **Interpretation A vs. B.** Outbound (calibrated as if conceivably shareable with each thinker) vs. internal map (private to the project, for planning later syntheses and conference encounters). The two have different tones. Possibly both, as paired companion documents.

- **Depth per thinker.** Executive summary (~200 words), serious paragraph plus rationale (~500–700 words), or full mini-essay (~1500 words). Materially different time budgets at 15 thinkers.

- **Sequencing across the 15.** Which thinker is drafted first as a calibration sample? Candidates: Stump (the thinker-voice work is freshest), Friston (most-cited in the formal-architecture syntheses), Wright (the scriptural-historical pole). A reasonable choice is one thinker from each substantive cluster (formal / metaphysical / theological / experimental) as initial calibration.

- **Communication channel.** Internal-only, selective sharing in advance of meetings, public publication, or in-person dialogue. Each carries different epistemic responsibilities and different review processes.

- **Update cadence.** A dossier is not a once-and-done document. As the C2A2 network's understanding of each tradition deepens, and as each thinker's published work progresses, the dossier needs to evolve. Whose responsibility, on what cadence, with what review.

- **Loughran's own dossier.** Tom is one of the 15. The pathway's structure suggests a Loughran-tradition dossier exists; what does that look like, what does it say, and what is its purpose given that Tom is the project's curator rather than an external interlocutor.

- **Relation to the C2A2 podcast (Pathway 11).** Some research suggestions may best be communicated via episode rather than dossier. The two channels are not exclusive; the relationship needs design.

- **ISME bearing.** Is Pathway 26 part of what ISME sees? Or is it post-ISME work? The current `isme_critical: no` flag is provisional; the demo may benefit from showing one or two dossiers as evidence of the project's outbound stance.

## Edges

- **apprentice_mode (15):** the agent's mature understanding of each tradition is the prerequisite for productive suggestions; the dossier-drafting stage is downstream of apprentice maturity.
- **honesty_layer (14):** every suggestion carries explicit epistemic markings; this pathway is one of the natural homes for honesty-layer machinery.
- **agent_developed_participant (17):** the agent's continuity with each thinker's tradition over months is what makes suggestions trustworthy; query-mode generation would produce shallow output.
- **outreach_automation (12):** if dossiers are shared with thinkers, they pass through the broker's content-grounded outreach gate; suggestions without verifiable C2A2 substance behind them do not get issued.
- **episode_publishing (11):** some research suggestions are best communicated through a podcast episode rather than a written dossier; the channels overlap.
- **under_development_visualizer (13):** progress on dossiers (drafted / under-review / shared / responded-to) is one of the development streams the visualizer can surface.
- **meta_visualization_pathways (25):** the cross-thinker network view of suggestions-that-implicate-each-other is a natural overlay on the meta-visualization.
- **branching_counterfactuals (23):** for some thinkers the productive question is "what would your program have looked like if you'd encountered Levin's work before Friston's" — counterfactual exploration applies at the per-thinker level.
- **community_outreach (12):** same channel; dossiers are content-grounded outreach in the project's outreach-automation sense.

## Provenance / source dialogue

- Session: 2026-05-15 Cowork conversation with Claude on Project Mac Mini, in the context of a longer working session that opened with Summa 2026 QC work (frontmatter audit, schedule forecast, QC-on-QC, readability audit) and arrived at the soft-thinker-voice convention (criterion M).

- Originating prompt from Tom: *"Dev Pathway 26 (or so): Develop and communicate research suggestions for each thinker, together with rationale."*

- Tom's framing constraint: *"All I want for Dev Pathway 26 is an md file conformal to the full pathway set. We've yet to have a prioritization or scheduling discussion; we should have that late next week if possible."*

- The pathway emerged immediately after the criterion M work, which had established that the project's relationship to the 15 thinkers is one of citing their work as a resource without classifying them into hard role-categories. Pathway 26 is the natural complement: having done the work of *receiving* each tradition carefully, the project now has something productive to *send back*. The continuity from criterion M to Pathway 26 is direct.

## Status

Outlined. Full elaboration deferred to the late-next-week prioritization and scheduling discussion. The pathway is well-posed enough to enter the inventory; the open questions above name what that discussion needs to settle.

Calibration-sample drafting (one thinker first, reviewed before the others) is the obvious first concrete step. Three candidates for the calibration sample are noted in the open questions; choice deferred. No dossiers exist yet.
