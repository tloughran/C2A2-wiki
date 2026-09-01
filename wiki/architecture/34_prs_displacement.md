---
title: PRS Displacement Phrasings — The Path, Not Just the Endpoints
pathway_id: prs_displacement
status: outlined
created: 2026-09-01
depends_on: []
enables: [maturity_model]
isme_critical: no
---

# Pathway 34: PRS Displacement Phrasings

## Purpose

Hawkins' reference frames encode not only *locations* but **displacements** — the
movement from one location to another. A PRS triplet today records three static points:
Problem, Resource, Solution. It does not record the reasoning path that connects them.

Two triplets can share a Problem and a Solution and yet represent completely different
intellectual moves. As recorded, they are indistinguishable. The path is the part that
carries the transfer, and it is the part currently thrown away.

## The change

Add a fourth field, `Displacement`, to the PRS structure:

```
PRS-[number]:
  Problem: [...]
  Resource: [...]
  Solution: [...]
  Displacement: [semantic phrasing of how R transforms P into S — the inferential
                 movement, expressed as a natural-language vector, e.g.,
                 "from substrate-dependent cognition → through bioelectric signaling
                 evidence → toward substrate-independent goal-directedness"]
```

**A phrasing, not a pointer.** This is the design commitment. A pointer (an id, an edge,
a type code) would say *that* a transformation occurred; a phrasing says *what* it was.
The way R transforms P into S is itself meaningful content, and compressing it to a
label destroys exactly the information the field exists to keep.

## The connecting-memes hypothesis

The interesting possibility: there may be a **finite typology** of such displacement
phrasings — a limited set of cross-paradigm transformation patterns that recur across
otherwise unrelated traditions. If that holds, it is a structural discovery about how
knowledge moves between paradigms, not merely a better annotation scheme.

The hypothesis is explicitly assigned, not left floating:

- **Agent 14a tracks it** — logging candidate recurrences as they appear.
- **Agents 15a / 15b test it** — searching for external corroboration and attempting
  to falsify the claim that the typology is bounded.

Recorded as an open hypothesis; the pathway is worth doing whether or not it holds,
because comparability is a gain on its own.

## Cost and risk

- **~30% length added to every PRS entry.** Real and recurring, across 282 existing
  triples and everything after.
- **Quality is prompt-dependent.** Phrasing a displacement well is a genuine skill, and
  a bad phrasing is worse than none — it looks like content and is not. This is a place
  where model judgment is correctly used (Rule 5: phrasing is drafting, not routing).
- No infrastructure dependency; this is a template and prompt change.

## Success criterion (Rule 4)

**Displacement phrasings must make triplets discriminable that were previously
identical.** Concretely: find triplets in the existing corpus that share Problem and
Solution endpoints, add displacements, and check that the phrasings distinguish them in
a way a reader agrees is real. If the Pattern Detector cannot use displacement to
separate triplets it previously conflated, the field is decoration and the 30% cost is
not warranted. The connecting-memes typology is a *further* payoff and must not be used
to justify the field on its own — it is unproven.

## Edges

- **Pattern Detector:** shared displacement patterns across traditions become a
  detectable signal, which is the main near-term use.
- **Agent 14a (assumption tracking):** owns the connecting-memes hypothesis log.
- **Agents 15a / 15b (external search and testing):** own its falsification.
- **Pathway 31 (Cortical column architecture):** columns decomposing by
  problem-first / solution-first / resource-first are decomposing along the very axis
  displacement records; the two pathways inform each other.
- **Pathway 35 (Developmental maturity model):** displacement vectors implemented is a
  named Stage 1 benchmark, and an emerging connecting-meme typology is a Stage 5 one.

## Provenance

Lifted from **revised change 3** of the 2026-04-09 Thousand Brains redesign proposal
(revised 2026-04-10), which specified the `Displacement` field, the phrasing-not-pointer
commitment, the finite-connecting-memes hypothesis, and the 14a / 15a / 15b assignment
for tracking and testing it. Elevated to a Dev Pathway on 2026-09-01 during the
incorporation audit, which found no `Displacement` or `Path` field in any PRS template.
This pathway adds the falsifiable success criterion and separates the field's own
justification from the unproven typology claim.

Source document: [C2A2 Redesign Proposal (revised)](../review/C2A2_redesign_proposal_2026-04-09_revised.md)

Related: [Pathway 31 — Cortical column architecture](31_cortical_column_architecture.md) · [Pathway 35 — Developmental maturity model](35_maturity_model.md) · [Pathway inventory](pathways.md)
