---
proposal_id: PROP-2026-07-13-001
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Alignment Is to a Virtual Governor: A Theory of Coordination in Diverse Intelligence"
source_url: https://www.preprints.org/manuscript/202607.0220
source_date: 2026-07
searched_on: 2026-07-13
status: pending
---

## Summary
Lyons, Pio-Lopez & Levin propose that what a collective intelligence is aligned *to* is not a goal, a utility function, or a leader, but a "virtual governor" — a system-level preference that is not located in any part but is embodied in the relationships among the parts. The paper states the conditions under which such a governor can exist and actually coordinate (the components must be coupled such that what one part does registers on the others), and derives from those conditions a small set of alignment failure modes that apply identically to an economy, a body, or a multi-agent AI system. Notably, one failure mode is *over*-alignment: a virtual governor coordinates by leaving the parts enough room to keep optimizing on their own local landscapes, and forcing the parts into too-complete agreement destroys the very thing that made the collective intelligent.

*Caveat (surfaced, not hidden): the preprints.org abstract page could not be retrieved by this agent (fetch blocked). The summary above is reconstructed from the canonical citation on Levin's lab preprint list plus co-author Benjamin Lyons' own public exposition of the virtual-governor construct. Tom/orchestrator should read the abstract before ingestion.*

## Why This Matters for This Tradition
This is the third entry in the Lyons–Pio-Lopez–Levin alignment arc (after *From Cancer to AI Alignment*, PROP-2026-05-05-001) and it moves the program from a diagnostic frame (misalignment = externality between cognitive light cones) to a constructive one (alignment = the existence conditions for a relational, part-independent governor). It is the most explicitly *political* artifact Levin's program has yet produced: it gives a substrate-independent account of what holds a collective together and of how collectives fail by coordinating too hard.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: In a collective intelligence, what exactly is the thing that the parts are aligned *to*? Utility-function and principal-agent framings both presuppose a locus of preference, but in a body, an economy, or a swarm there is no part that holds the system-level goal.
  Resource: The "virtual governor" — a system-level preference that exists only in the relational structure among the members, together with a stated set of conditions (mutual registration/coupling among components) that must hold simultaneously for it to coordinate anything at all.
  Solution: Alignment is reframed as a relational-existence property rather than a value-transfer property: you do not install a goal into the parts, you establish the coupling conditions under which a governor can exist and be tracked. This makes alignment analyzable in the same vocabulary across cells, markets, and AI collectives.
  Confidence: Medium
  Evidence: The paper's central construct as stated by its authors — "a virtual governor is a system-level preference embodied in the relationships among the members of a system," with three conditions that must hold simultaneously for coordination to occur.

PRS-CANDIDATE-02:
  Problem: Alignment discourse in AI treats more agreement between parts and whole as monotonically better. Is there such a thing as too much alignment?
  Resource: The over-alignment failure mode — the claim that a virtual governor coordinates precisely by leaving the parts enough room to keep optimizing on their own (warped, local) landscapes.
  Solution: A falsifiable prediction that collectives forced into rigid, complete agreement lose the problem-solving competence that made them intelligent — i.e., that there is an interior optimum in the coupling-strength parameter, and that both under- and over-alignment are pathologies with distinct signatures.
  Confidence: Medium
  Evidence: The authors' explicit statement of over-alignment as one of three failure modes falling directly out of what a virtual governor is and what it requires to function.

## Cross-Tradition Signals
Strong and multiple.

- **[[Friston]]** — the virtual governor is very close to the *group-level Markov blanket / emergent group generative model* of "As One and Many" (PROP-2026-06-22-002). Both posit a system-level object that is not reducible to any member yet does real coordinating work; Friston gives it a variational formalism, Levin gives it existence conditions and failure modes. This is the sharpest Levin↔Friston convergence the network has surfaced to date and is a live bridge candidate.
- **[[C2A2 / master]]** — direct methodological relevance to the accelerator itself. The over-alignment failure mode is a first-principles argument that a tradition-interaction system should *not* drive its communities to consensus; it predicts that forcing agreement across traditions destroys the local optimization that makes each tradition productive. That is a testable claim about the C2A2 Rung-2 design and about what "successful" inter-tradition dialogue should look like.
- **[[Wolfram]]** — "preference embodied in relations, not in parts" is a computational-boundary claim; compare Wolfram's observer-boundary work (PROP-2026-07-05).
- **[[Hoffman]]/[[Kastrup]]** — a governor with no part-local seat is a further pressure on locating agency in substrate.
