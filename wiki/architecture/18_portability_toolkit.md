---
title: Portability and Toolkit Design
pathway_id: portability_toolkit
status: drafted
created: 2026-05-14
depends_on: [broker, voice_dialogue, ambient_viz, probing_channel, perspective_lattice, durable_memory]
enables: [optional_interoperability, institutional_scale, departmental_integration, individual_second_brain]
isme_critical: no
---

# Pathway 18: Portability and Toolkit Design

## Purpose

How does someone see what we've built, recognize the value of the framework itself, and instantiate their own version without needing the Carpathi vault as the center? Pathway 18 addresses portability: the move from demonstration to toolkit.

The Carpathi Wiki is currently instantiated around a specific vault (the RC Karpathy Wiki) and a specific set of fifteen-plus-Aquinas thinkers. The framework — the PRS structure, the agent ecosystem, the perspective lattice, the honesty layer, the visualization spine — is in principle separable from that substantive content. Pathway 18 is the engineering and documentation work that makes the framework actually instantiable by another community, with their own traditions, their own thinkers, their own problems.

This is not about forking the content. It is about packaging the methodology so that someone watching the ISME demo or reading the public site can recognize the value of the rationality standards built into tradition-craft inquiry and adopt them for their own community. The reason this matters at the architectural level is that everything later in the 18 → 25 arc — federation (19), institutional scale (20), departmental zoom-in (21), individual second brain (22) — presupposes a toolkit that other people can actually pick up.

## Function set

*(Cowork-drafted 2026-05-14; not yet validated in walk dialogue.)*

Five pieces:

1. **Framework / content separation.** Identify and document the seam between the framework code (broker, retrieval, agent ecosystem, visualization engine, governance protocols) and the Carpathi-specific content (vault, thinker list, perspective lattice fillings, decisions register). The seam must be clean enough that swapping content does not require touching framework code.

2. **Vault scaffolding.** A template repository that a new community clones to get started: empty vault structure, frontmatter conventions, PRS-skeleton files, blank perspective lattice, empty decisions register, agent skill stubs that the community fills in with their own thinkers and traditions.

3. **Configuration surface.** A single configuration file (or small set) that lets a new community specify their thinkers, their PRS axes, their ISME-equivalent target, their broker provider, and their visualization style without editing framework code.

4. **Onboarding documentation.** A getting-started guide that walks a community through the conceptual model (tradition-constituted inquiry, PRS, honesty layer, perspective lattice), the framework architecture, and the practical steps of instantiating their own version. The documentation is itself an invitation to the rationality standards, not just a technical README.

5. **Demonstration instance retention.** The Carpathi Wiki remains live as the reference implementation, but with explicit signposting that it is one instance of the framework rather than the framework itself. New adopters can study it as an exemplar without inheriting its content.

## Architecture sketch

*(Cowork-drafted 2026-05-14.)*

```
       carpathi-wiki (reference instance)
                  │
                  │  packages
                  ↓
       c2a2-framework (toolkit repo)
       ├─ framework/
       │   ├─ broker/
       │   ├─ retrieval/
       │   ├─ agents/
       │   ├─ visualization/
       │   └─ governance/
       ├─ template-vault/
       │   ├─ perspectives/
       │   ├─ decisions.md (skeleton)
       │   ├─ assumptions/ presumptions/ premises/
       │   └─ pathways/ (skeleton)
       ├─ config/
       │   └─ instance.yaml  (thinkers, PRS axes, broker provider, etc.)
       └─ docs/
           ├─ getting-started.md
           ├─ tradition-constituted-inquiry.md
           └─ instantiation-guide.md
                  │
                  │  clone + configure
                  ↓
       community-instance-N
       (their thinkers, their vault, their broker)
```

## Decisions taken

*(Cowork-derived from walk description; subject to Tom's amendment.)*

- **Toolkit separation is non-optional.** Without it the project remains a single demonstration rather than a methodology others can adopt. The 18 → 25 arc collapses if 18 fails.

- **Framework / content separation must be clean enough to swap content without touching code.** No hardcoded references to Aquinas, Levin, MacIntyre, or any specific thinker in the framework layer. Configuration drives all substantive choices.

- **The framework is GitHub-public; instance vaults are at the community's discretion.** Some communities will want public-by-default vaults like ours; others will not. The framework supports both.

- **Documentation carries the rationality standards.** Not just a technical guide — the onboarding documentation invites adopters into MacIntyrean tradition-constituted inquiry as the system's normative shape. Adopting the framework without engaging the rationality standards produces a different (and weaker) instance.

- **Reference instance retention.** Carpathi Wiki stays live as the exemplar. New adopters can study, fork, and learn from it, but the framework repo is the canonical entry point.

## Open questions

- What is the minimal toolkit a community needs to instantiate their own version? Probably less than the Carpathi Wiki's full feature set, but the minimum-viable set has not been characterized.
- How do we separate the Carpathi-specific content from the framework-level architecture? Which files in the current repo belong to "framework" and which to "instance"? A line-by-line audit is owed.
- What documentation, templates, and scaffolding does a new community need? The shape of the getting-started experience determines whether anyone actually adopts.
- How do we invite adoption of the tradition-craft rationality standards without imposing the specific substantive content? The framework's normative commitments (honesty layer, PRS, perspective lattice) need to come with the toolkit, not be opt-in afterthoughts.
- Licensing: what license fits a framework intended to be adopted, modified, and federated? (Tentatively: permissive on framework, community choice on content.)

## Edges

- **broker (00):** broker architecture must be portable, not tightly coupled to the Carpathi vault; configuration drives provider selection (Cloudflare Workers default, alternatives possible).
- **voice_dialogue (01), ambient_viz (02), probing_channel (03):** these user-facing pathways must be content-agnostic; they currently work for Carpathi but should work identically for any conforming vault.
- **perspective_lattice (04):** the lattice is the curriculum scaffolding for apprenticeship; the framework supplies an empty lattice, each community fills it.
- **durable_memory (16):** memory is per-instance; cross-instance memory only via Pathway 19 federation, opt-in.
- **optional_interoperability (19):** portability is the precondition for federation; can't federate instances that don't exist independently.
- **institutional_scale (20), departmental_integration (21), individual_second_brain (22):** each is a portability test case at a different scale.

## Provenance / source dialogue

- Session: 2026-05-14 morning walk, Tom on phone in Chat mode, conversation `https://claude.ai/chat/ed8b7056-407d-4a71-8fae-62b08e9613e0`. Source dialogue captured in `morning_walk_2026-05-14.md` and `2026-05-14_pathways_18-25_review.md`.
- Originating framing from the walk: "How does someone see what we've built, recognize the value of the framework itself, and instantiate their own version without needing the Carpathi vault as the center? Moving from demonstration to toolkit while inviting adoption of the rationality standards built into tradition-craft inquiry."
- Continuous with the dream-pass commitment (2026-05-13) that the system is to be radically open: showing how it works, inviting others to build their own instances, and creating conditions for genuine inter-tradition dialogue.

## Status

*(Implementation outline drafted by Cowork 2026-05-14; sequencing subject to Tom's amendment.)*

Drafted in prose. Implementation order: (a) line-by-line audit of the current repo to identify the framework / content seam, (b) extract framework code into a separate `c2a2-framework` repo with the Carpathi vault becoming the reference instance, (c) build template-vault scaffolding, (d) draft `instance.yaml` configuration surface, (e) write onboarding documentation including the tradition-constituted-inquiry primer, (f) test the toolkit by instantiating a second small instance internally before any external adopter touches it. Not ISME-critical, but ISME-supporting: the demo benefits from being able to point at the framework as a thing others can pick up.
