---
title: Apprentice Mode (Dialogical Curriculum)
pathway_id: apprentice_mode
status: drafted
created: 2026-05-13
depends_on: [voice_dialogue, perspective_lattice, durable_memory, honesty_layer]
enables: []
isme_critical: no
---

# Pathway 15: Apprentice Mode

## Purpose

A dialogical curriculum that brings newcomers to maturity in any of the eleven traditions. A graduate student from Levin's lab arrives cold. A McGilchrist reader wants to climb into Friston. An interested colleague wants to ramp into MacIntyre. The system co-builds a path that proposes readings, tests understanding, retraces when something didn't take, and surfaces the harder questions when readiness allows.

This is the c282 program in concrete form, and it is what makes the outreach pathway (Pathway 12) actually pay off. The graduate student who shows up — invited from Levin's lab — has a way to *engage*, not just observe.

## Function set

Five pieces:

1. **Tradition selection.** The newcomer picks a tradition to learn (any of the eleven, or the C2A2 framework itself). The system loads that tradition's perspective lattice (Pathway 04) as the curriculum scaffolding.

2. **Diagnostic conversation.** Before proposing readings, the system has a brief conversation to gauge the newcomer's starting point: prior reading, conceptual familiarity, related traditions they already know, the kind of question that drew them here. This conversation calibrates the curriculum.

3. **Adaptive path proposal.** The system proposes a sequence of readings, conversations, and probes — drawn from the perspective lattice's eager-tier overviews, supplemented by primary-source links where vault attestation calls for them. The path is not pre-canned; it adapts to what the newcomer engages with and what they bypass.

4. **Comprehension testing through dialogue.** Rather than quizzes, the system asks the newcomer to articulate concepts back, to apply them to fresh examples, to compare them with their existing conceptual furniture. The honesty layer (Pathway 14) is teaching material here — the newcomer learns to mark their own claims with epistemic status as they engage.

5. **Frontier surfacing.** Once the newcomer reaches a threshold of maturity in the tradition, the system surfaces the unsaid-edges map (Pathway 07) entries relevant to their tradition. The frontier is the live research-program candidates: Low × High empty edges where the newcomer could plausibly contribute.

## Architecture sketch

```
newcomer arrives
        ↓
   tradition selection
        ↓
   diagnostic conversation
   ├─ prior reading
   ├─ conceptual familiarity
   └─ entry question
        ↓
   adaptive curriculum
   ├─ readings (from perspective lattice + primary sources)
   ├─ dialogical engagement (Pathway 01)
   ├─ comprehension via dialogue (no quizzes)
   └─ honesty layer practice
        ↓
   durable memory checkpoint (Pathway 16)
        ↓
   on maturity threshold: frontier surfacing (Pathway 07)
   ├─ relevant Low × High empty edges
   └─ candidate research directions
```

## Decisions taken

- **Dialogical, not pre-canned.** Curricula adapt to the newcomer. The system uses its full dialogue grammar; the path is built in conversation, not selected from a menu.

- **The perspective lattice is the scaffolding.** Eager-tier overviews provide the structure; the apprentice walks through them in an order calibrated to their starting point.

- **Comprehension through dialogue, not quiz.** Quizzes test recall; dialogue tests understanding. The newcomer learns by articulating, applying, and revising under the system's response.

- **Honesty layer as pedagogical material.** Learning to mark one's own claims with epistemic status is itself part of becoming mature in a tradition. The newcomer practices the discipline alongside the content.

- **Frontier surfacing is the graduation move.** When the newcomer reaches a threshold, the system shows them where the tradition's live research-program candidates are. Apprenticeship ends in invitation to contribution.

## Open questions

- **Maturity threshold criteria.** What counts as "ready for the frontier"? Some mix of curriculum completion + dialogue depth + honest engagement with the honesty layer. Probably tunable per tradition.

- **Multi-tradition apprenticeship.** Can a newcomer apprentice in two traditions simultaneously, becoming a "second-first-language" speaker in the MacIntyrean sense? Architecturally yes — two perspective lattices loaded — but the path-design becomes more complex.

- **Time horizon.** An apprenticeship in a tradition might take weeks or months. Durable memory (Pathway 16) provides the substrate; what's the cadence of engagement? Daily nudges? Weekly check-ins? Probably user-controlled.

- **Assessment for credit.** Could the system's apprenticeship eventually be accepted as a credentialed pathway (a graduate course, a certificate)? Worth future thought; not for ISME, but a real direction.

## Edges

- **voice_dialogue (01):** apprenticeship runs through the dialogue layer; comprehension is tested in conversation.
- **perspective_lattice (04):** primary content scaffolding; the lattice is the curriculum's structure.
- **unsaid_edges (07):** frontier surfacing at maturity threshold; apprentice graduates into research-program candidacy.
- **durable_memory (16):** apprenticeship persists across sessions and months; visitor returns and resumes.
- **honesty_layer (14):** epistemic-status taxonomy is part of what the apprentice learns to use.
- **outreach_automation (12):** invitations from Levin's lab and similar communities land in apprenticeship; this is where outreach pays off.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork), in the dream-along: "A dialogical curriculum: someone arrives cold — graduate student, interested colleague, the daughter who's just heard about MacIntyre — and the system co-builds a path that brings them to maturity in any of the eleven traditions. Not pre-canned modules; an adaptive conversation that proposes readings, tests understanding, retraces when something didn't take, surfaces the harder questions when readiness allows." Tom: "you've nailed it." This is the c282 program in concrete form.

## Status

Drafted in prose. Implementation order: (a) tradition selection UI, (b) diagnostic conversation script, (c) adaptive curriculum engine over the perspective lattice, (d) comprehension-through-dialogue protocols, (e) frontier-surfacing integration with Pathway 07. Substantial but builds incrementally on existing pathways.
