---
title: Institutional Scale at the University Level
pathway_id: institutional_scale
status: drafted
created: 2026-05-14
depends_on: [portability_toolkit, optional_interoperability]
enables: [departmental_integration]
isme_critical: no
---

# Pathway 20: Institutional Scale at the University Level

## Purpose

Build specific tools for the School of Global Affairs ecosystem — all those scattered communities doing global work across different schools — to prove the concept works for real coordination and knowledge-sharing at scale within a real institution.

The University of Notre Dame's School of Global Affairs is a particularly rich test case. Many communities doing globally-oriented work are scattered across different schools and disciplines, with genuine coordination challenges and a shared institutional context that already supplies the affiliative substrate for federation. SGA is not a single department but an umbrella, which means the coordination problem is real, not hypothetical: people who would benefit from each other's work do not currently have a low-friction way to find each other, share intellectual context, or co-develop on shared questions.

Pathway 20 takes the Carpathi Wiki methodology and instantiates it specifically for this environment. The point is not generic institutional deployment but a purpose-built instantiation: tools tailored to the kinds of problems global affairs communities face, the types of thinkers and traditions they draw on, and the specific coordination challenges that arise when work is distributed across schools. The deliverable is proof-of-concept at institutional scale: showing that the framework is not just useful for a single researcher or a single tradition, but can handle real coordination and knowledge-sharing challenges in a large, complex institution.

## Function set

*(Cowork-drafted 2026-05-14; not yet validated in walk dialogue.)*

Five pieces:

1. **SGA-tailored PRS axes.** The Problem-Resource-Solution framework gets reinstantiated for global-affairs work. Problems are the specific coordination failures and substantive challenges SGA communities face. Resources include cross-school methods, datasets, partner organizations, funding lines. Solutions are documented past projects, deployable models, and current initiatives. The PRS axes are configured per the SGA context, not inherited unchanged from Carpathi.

2. **Community-of-practice mapping.** The Sociogram is reused but the nodes are SGA communities (research clusters, study programs, partner organizations) rather than thinkers. Edges are coordination opportunities, shared methods, overlapping problem domains. The agent ecosystem treats each community as roughly analogous to a tradition in the Carpathi sense.

3. **Cross-school PRS bridge.** Where Carpathi connects traditions, the SGA instance connects schools. The "SUPER-BRIDGE" pattern (FINDING-011) is the architectural prior: a cross-school PRS connection is structurally identical to a cross-tradition one. Discovery is the same problem at a different scale.

4. **Institutional governance overlay.** Notre Dame has existing institutional structures (IRB, sponsored research, communications policy) that any deployed system must respect. The instance includes an explicit overlay specifying what data is shareable, with whom, under what terms — drawing from the selective-sharing controls in Pathway 19 but scoped to institutional policy.

5. **Tom's relationship surface.** Pathway 20 leverages Tom's existing relationships in the SGA ecosystem (Notre Dame AI acceleration team, international development work, philosophy / physics intersections) as the initial point of contact and the social substrate for adoption. The deployment is not a cold start; it is an extension of existing collaborations into instrumented form.

## Architecture sketch

*(Cowork-drafted 2026-05-14.)*

```
       c2a2-framework (toolkit)
                  │
                  │  instantiate
                  ↓
       sga-notre-dame-instance
       ├─ vault/
       │   ├─ communities/        (instead of thinkers/)
       │   │   ├─ kellogg-institute/
       │   │   ├─ keough-school/
       │   │   ├─ pulte-institute/
       │   │   └─ ...
       │   ├─ prs/
       │   │   ├─ problems/       (sga-tailored axes)
       │   │   ├─ resources/
       │   │   └─ solutions/
       │   └─ perspectives/       (cross-school)
       ├─ broker/
       │   └─ institutional-policy-overlay
       └─ visualization/
           └─ sociogram (nodes = communities)
                  │
                  │  optional federation
                  ↓
       (other Notre Dame instances, peer universities)
```

## Decisions taken

*(Cowork-derived from walk description; subject to Tom's amendment.)*

- **Pick SGA specifically, not "the university."** A purpose-built instance for one well-bounded community is more useful than a generic university-wide deployment. The SGA scope is large enough to demonstrate institutional scale and small enough to be feasible.

- **The Sociogram nodes become communities, not thinkers.** The visualization spine is reused but the unit of analysis shifts. This validates the framework's portability claim — same architecture, different ontology, same affordances.

- **Tom's existing relationships are the initial substrate.** No cold-call adoption pitch. The first SGA-instance users are people Tom already works with, who can be invited into the system as collaborators rather than as subjects of a deployment.

- **Institutional policy is part of the instance, not a bolt-on.** IRB, sponsored research, communications policy, FERPA — these get encoded into the selective-sharing controls and the broker's policy enforcement, not handled as afterthoughts.

- **Adoption is voluntary at every level.** Communities opt in, faculty opt in, no community is asked to surrender autonomy to the institutional instance. The federation model (Pathway 19) means communities can stay distinctly themselves while plugged in.

## Open questions

- Which communities within SGA / Notre Dame's global-work ecosystem would benefit most from this? (Probably starts with two or three, not all at once.)
- What are the specific coordination failures the current state creates that this could address? (Concrete examples drive adoption; vague claims do not.)
- How does this connect to Tom's existing relationships in the SGA ecosystem? (Which specific colleagues are first conversations? Notre Dame AI acceleration team is one candidate.)
- What does the toolkit look like for this specific instantiation vs. the general portability toolkit (Pathway 18)? (How much SGA-specific code is needed vs. configuration?)
- IRB and institutional approval: at what point does an opt-in research-coordination tool become something the IRB cares about?
- Funding and sustainability: is this a side-project of Tom's, or does it become a sponsored initiative once it shows value?

## Edges

- **portability_toolkit (18):** SGA deployment is the first major institutional portability test case; lessons feed back into the toolkit.
- **optional_interoperability (19):** communities within SGA might want optional federation with each other and with peer universities.
- **departmental_integration (21):** physics & astronomy is the zoom-in counterpart; SGA is the zoom-out version of the same exercise.
- **outreach_automation (12):** institutional deployment requires policy-respecting outreach; the broker enforces.
- **meta_crafts_governance (24):** institutional governance is a meta-craft case — SGA's existing governance structures are the substrate the instance must respect.
- **honesty_layer (14):** institutional contexts have particular stakes around claim-marking; honesty-layer discipline matters more, not less, at this scale.

## Provenance / source dialogue

- Session: 2026-05-14 morning walk, Tom on phone in Chat mode, conversation `https://claude.ai/chat/ed8b7056-407d-4a71-8fae-62b08e9613e0`. Source dialogue captured in `morning_walk_2026-05-14.md` and `2026-05-14_pathways_18-25_review.md`.
- Originating framing from the walk: "Build specific tools for the School of Global Affairs ecosystem — all those scattered communities doing global work across different schools — to prove the concept works for real coordination and knowledge-sharing at scale within a real institution."
- The choice of SGA specifically (rather than a generic university-wide instance) reflects the framework's commitment to purpose-built, community-specific deployment rather than top-down rollout.

## Status

*(Implementation outline drafted by Cowork 2026-05-14; sequencing subject to Tom's amendment.)*

Drafted in prose. Implementation order: (a) identify two or three initial SGA communities through Tom's existing relationships; (b) hold informal conversations with potential first users to validate the coordination-failure premise and pick concrete shared problems; (c) configure an SGA instance from the toolkit (Pathway 18) with SGA-tailored PRS axes; (d) seed the vault with content from the initial communities, in collaboration; (e) deploy the visualization layer and run the first cross-community discovery exercise; (f) gather feedback and iterate on the toolkit. Not ISME-critical; this is a post-prototype expansion. ISME may, however, surface SGA-adjacent attendees who want to be first adopters.
