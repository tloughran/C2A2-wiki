---
proposal_id: PROP-2026-06-22-002
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "As One and Many: Relating Individual and Emergent Group-Level Generative Models in Active Inference"
source_url: https://www.mdpi.com/1099-4300/27/2/143
source_date: 2025-02-12
searched_on: 2026-06-22
status: pending
---

## Summary
A formal active-inference treatment (Entropy, Waade, Olesen, et al., with Friston) of when a collective of individual active-inference agents itself constitutes a larger, group-level active-inference agent. The key condition is that the collective maintains a *group-level Markov blanket*: if the group as a whole maintains a statistical boundary separating its internal from external states, the same variational machinery that describes a single agent applies to the collective, enabling one formalism to span scales from cells to human communities.

## Why This Matters for This Tradition
This is a significant Friston-authored formalization not yet captured in the wiki, and it is the most directly C2A2-relevant Friston result to date. It supplies a mathematically explicit account of the individual↔collective transition — precisely the move C2A2 needs to model a tradition/community as a single inquiring agent. It also tightens the Friston↔Levin bridge: Levin's "cognitive glue" (see PROP-2026-06-22-001) and this paper's group-level Markov blanket are two framings of the same problem — what binds sub-agents into a super-agent.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Active inference describes individual agents, but it is unclear under what conditions a group of such agents is itself a single agent rather than merely a crowd.
  Resource: The group-level Markov blanket — a statistical boundary maintained by the collective as a whole, distinct from the blankets of its members.
  Solution: When a collective sustains a group-level Markov blanket, it satisfies the formal conditions to be modeled as one active-inference agent; "one" and "many" descriptions become two consistent levels of the same generative model.
  Confidence: High
  Evidence: The paper's central thesis — a collective constitutes a larger group-level active-inference agent iff it maintains a group-level Markov blanket.

PRS-CANDIDATE-02:
  Problem: C2A2 needs a principled, in-principle-measurable criterion for when a community of inquirers behaves as a unified tradition vs. a loose aggregate.
  Resource: Nested generative models — individual member models embedded within an emergent group-level generative model under shared free-energy minimization.
  Solution: The framework gives a candidate operationalization: a tradition is "one agent" to the degree it sustains a group-level blanket and a shared generative model; degradation of that boundary marks fragmentation. This is a measurable target for the accelerator-detector.
  Confidence: Medium
  Evidence: The paper's nesting of individual within group-level generative models across spatiotemporal scales (cells → human collectives); application to traditions is C2A2's extension, not the paper's claim.

## Cross-Tradition Signals
- **Levin (cross-tradition flag — explicit):** group-level Markov blanket ≈ "cognitive glue." Both ask when sub-agents become a super-agent; one answers in FEP/variational terms, the other in bioelectric terms. Strong paradigm-bridge candidate worth a dispatch to the master agent.
- **C2A2 core relevance:** supplies the formal backbone for treating a tradition/community as a single inferring agent, and a measurable fragmentation criterion (group-blanket integrity) for the detector side of the system.
- **Wolfram:** group-level Markov blanket as a computational boundary connects to Wolfram's notion of emergent boundaries in computational systems.
- **Fredrickson (speculative):** "positivity resonance" as a coupling mechanism that helps sustain a group-level blanket (mechanism for shared-attractor alignment).
