---
title: Departmental Integration
pathway_id: departmental_integration
status: drafted
created: 2026-05-14
depends_on: [portability_toolkit, institutional_scale, apprentice_mode]
enables: [individual_second_brain]
isme_critical: no
---

# Pathway 21: Departmental Integration

## Purpose

Physics and astronomy department at Notre Dame as a model of what a fully integrated research-and-education environment looks like when you build specific tools and curated preparation where students and faculty can develop in directions they've chosen.

Pathway 21 is the zoom-in counterpart to Pathway 20's institutional zoom-out. Where 20 addresses coordination across scattered communities at the university level, 21 asks what the framework looks like when applied within a single, tightly-focused department. Physics and astronomy is an intentional choice — not interdisciplinary in the broad sense, but with rich internal sub-disciplinary diversity (HEP, astrophysics, condensed matter, AMO, biophysics, nuclear, instrumentation) and a clean apprenticeship structure already embedded in graduate training.

The goal is a system where research and education are genuinely integrated: students and faculty can see the landscape of current research, track where the department's traditions of inquiry are going, find the unsaid edges of work in adjacent sub-disciplines, and develop along pathways they have chosen with full visibility into the intellectual terrain. This is closer to "a second brain for a department" — a shared intellectual commons where the tools are curated for the specific problems, methods, and traditions of physics and astronomy, not for global affairs or theology. The specificity is the point: showing that the framework generalizes by building a genuinely tailored instantiation, with Tom's existing role as instructional resources program manager as the social entry point.

## Function set

*(Cowork-drafted 2026-05-14; not yet validated in walk dialogue.)*

Five pieces:

1. **Physics-tailored PRS axes.** Problems are open questions and unsolved puzzles in the department's research programs. Resources are methods, instruments (the demo program's own holdings included), datasets, collaborations, prior results. Solutions are experimental and theoretical advances, with explicit attestation links to publications and internal seminars. Sub-discipline boundaries are explicit but porous.

2. **Sub-discipline lattice.** Where Carpathi has thinkers, the physics instance has sub-disciplines and their key researchers — both internal department members and external figures the department converses with. The perspective lattice (Pathway 04) is reinstantiated: HEP, astrophysics, condensed matter, AMO, biophysics, nuclear all get eager-tier overviews suitable for someone coming in cold.

3. **Apprenticeship integration.** Pathway 15 (Apprentice Mode) is particularly relevant here. Graduate-student apprenticeship in physics has well-defined structure (qualifying exams, group rotations, dissertation committees). The system supports that structure rather than replacing it: diagnostic conversations, adaptive readings, comprehension testing through dialogue, frontier surfacing at the threshold where the student is ready to identify a thesis problem.

4. **Instrument and demo integration.** Tom's day-job role — instructional resources, undergrad labs, demo program — is a unique affordance. The vault can include the demo holdings as a tangible resource layer: which demos illuminate which concepts, which experiments are runnable in the undergrad lab, what instrument time is available. This is rare and valuable; most departmental knowledge systems do not have the physical-instrument layer.

5. **Faculty-as-thinkers integration.** Department faculty become first-class nodes in the local Sociogram, with their published work, current research, and (with consent) their open questions visible to graduate students seeking advisors and to colleagues looking for collaborators. Optional, consent-based, but transformative if adopted.

## Architecture sketch

*(Cowork-drafted 2026-05-14.)*

```
       c2a2-framework (toolkit)
                  │
                  │  instantiate
                  ↓
       physics-astronomy-instance
       ├─ vault/
       │   ├─ sub-disciplines/
       │   │   ├─ HEP/
       │   │   ├─ astrophysics/
       │   │   ├─ condensed-matter/
       │   │   ├─ AMO/
       │   │   ├─ biophysics/
       │   │   ├─ nuclear/
       │   │   └─ instrumentation/
       │   ├─ faculty/             (consent-based participation)
       │   ├─ prs/
       │   │   ├─ problems/        (open puzzles by sub-discipline)
       │   │   ├─ resources/       (methods, instruments, datasets)
       │   │   └─ solutions/       (publications, results)
       │   ├─ demos/               (Tom's instructional-resources layer)
       │   ├─ undergrad-labs/      (curricular layer)
       │   └─ apprenticeship/      (Pathway 15 integration)
       ├─ broker/
       │   └─ department-policy-overlay
       └─ visualization/
           └─ sociogram (nodes = sub-disciplines + faculty)
                  │
                  │  optional federation
                  ↓
       (Notre Dame SGA instance, peer physics departments)
```

## Decisions taken

*(Cowork-derived from walk description; subject to Tom's amendment.)*

- **Physics & Astronomy specifically.** Tom's home department, his existing day-job role, his demo program, his relationships with faculty and graduate students. The social substrate for adoption is already present.

- **Sub-disciplines, not thinkers, as primary nodes.** Reflects how physics organizes intellectually. Faculty are first-class nodes too, but participation is opt-in and consent-based.

- **Demo and instrument layer is unique to this instance.** Tom's instructional resources role gives the department a physical-instrument layer most knowledge systems do not have. Surface it.

- **Apprenticeship integration leans heavily on Pathway 15.** Graduate-student preparation is the highest-value early use case. The system supports the existing apprenticeship structure rather than competing with it.

- **Faculty participation is opt-in, consent-based, granular.** No faculty member is enrolled without explicit consent. Consent is per-feature (publications visible vs. open questions visible vs. office-hour-readiness visible) and revocable.

## Open questions

- What does the PRS framework look like for a physics/astronomy department in detail? (Problems: open puzzles; Resources: methods/instruments/datasets/prior results; Solutions: advances. But the granularity within each axis needs to be designed with someone in each sub-discipline.)
- Who are the "thinkers" in this instantiation — department faculty, key external researchers, historical figures? Probably a mix; the lattice can hold all three categories.
- How does pedagogical apprenticeship manifest differently here than in the humanities-centered Carpathi Wiki? (Quals, rotations, committee structure, thesis problem identification — all different from MacIntyrean tradition apprenticeship.)
- What does the Sociogram look like for this community? Sub-disciplines as colors? Faculty as nodes? Publications as edges? Multiple views?
- How does the department reception go? (Some faculty enthusiastic, some indifferent, some skeptical — what's the engagement strategy?)
- Demo and undergrad-lab data as part of the vault: is this within Tom's authority to surface, or does it need departmental approval?

## Edges

- **portability_toolkit (18):** departmental deployment is a portability test case at a tighter scope than institutional.
- **institutional_scale (20):** the departmental instance might optionally federate with the institutional instance once both exist.
- **individual_second_brain (22):** individual faculty's personal second brains can be private extensions of the departmental instance — or fully detached.
- **apprentice_mode (15):** graduate-student apprenticeship in physics has well-defined structure that Pathway 15 was designed to support.
- **unsaid_edges (07):** the frontier-surfacing function is particularly useful here — students at the maturity threshold need to see open empirical and theoretical edges in their sub-discipline.
- **agent_developed_participant (17):** an agent with continuity becomes a recognized presence in the department over years, not sessions.

## Provenance / source dialogue

- Session: 2026-05-14 morning walk, Tom on phone in Chat mode, conversation `https://claude.ai/chat/ed8b7056-407d-4a71-8fae-62b08e9613e0`. Source dialogue captured in `morning_walk_2026-05-14.md` and `2026-05-14_pathways_18-25_review.md`.
- Originating framing from the walk: "Physics and astronomy department at Notre Dame as a model of what a fully integrated research-and-education environment looks like when you build specific tools and curated preparation where students and faculty can develop in directions they've chosen."
- The choice of Tom's home department reflects the pattern across the 20–22 arc: build for communities Tom is already part of, where the social substrate is real, rather than for hypothetical adopters.

## Status

*(Implementation outline drafted by Cowork 2026-05-14; sequencing subject to Tom's amendment.)*

Drafted in prose. Implementation order: (a) informal conversations with the department chair and one or two interested faculty about the concept; (b) configure a physics & astronomy instance from the toolkit (Pathway 18) with sub-discipline-tailored PRS axes; (c) seed the lattice with eager-tier overviews of each sub-discipline (probably co-drafted with one collaborator per area); (d) integrate the demo and undergrad-lab data as a unique resource layer; (e) prototype apprenticeship-mode integration with a willing graduate student; (f) consent-based faculty onboarding as adoption grows. Not ISME-critical; this is a longer-arc deployment that benefits from being able to point at the ISME demo as the validating prior.
