---
proposal_id: PROP-2026-07-27-004
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Self-orthogonalizing attractor neural networks emerging from the free energy principle"
source_url: https://arxiv.org/abs/2505.22749
source_date: 2026-05-21
searched_on: 2026-07-27
status: pending
---

## Summary
Spisak & Friston show that attractor neural-network dynamics *emerge* from applying the free energy principle to a universal partition of random dynamical systems, without any explicitly imposed learning or inference rules. Minimizing variational free energy with respect to internal states yields a Boltzmann-Machine-like stochastic update, with continuous-state stochastic Hopfield networks as a special case. Sequential data presentation produces asymmetric couplings and non-equilibrium steady-state dynamics that generalize conventional Boltzmann machines; simulations show orthogonal-basis formation, generalization, sequence learning, scalability, and resistance to catastrophic forgetting. (Also published in *Neurocomputing*, 2026.)

## Why This Matters for This Tradition
This is a foundational-level result: it derives a canonical class of memory/computation architectures (Hopfield/Boltzmann) *from* the FEP rather than positing them, tightening the claim that the FEP is a first-principles account of neuronal computation. It directly advances the program's "learning and inference rules are emergent, not imposed" thesis.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Do attractor dynamics and their learning/inference rules have to be imposed by hand, or can they be derived from first principles?
  Resource: FEP applied to a universal partition of random dynamical systems; variational free-energy minimization over internal states.
  Solution: Attractor networks (Boltzmann-machine / continuous stochastic Hopfield as special case) emerge as the free-energy-minimizing dynamics — obviating explicitly imposed learning/inference rules and yielding biologically plausible, efficient dynamics.
  Confidence: High
  Evidence: Abstract: "obviates the need for explicitly imposed learning and inference rules"; "minimizing variational free energy with regard to the internal states yields a Boltzmann Machine-like stochastic update mechanism, with continuous-state stochastic Hopfield networks being a special case."

PRS-CANDIDATE-02:
  Problem: How can a self-organizing predictive system learn sequences and generalize without catastrophic forgetting?
  Resource: Self-orthogonalizing dynamics under sequential presentation → asymmetric couplings and non-equilibrium steady states.
  Solution: Emergent orthogonal-basis formation gives generalization, sequence learning, scalability, and resistance to catastrophic forgetting from the same free-energy objective.
  Confidence: High
  Evidence: Abstract: "orthogonal basis formation, generalization, sequence learning, scalability and resistance to catastrophic forgetting"; "asymmetric couplings and non-equilibrium steady-state dynamics, generalizing conventional Boltzmann Machines."

## Cross-Tradition Signals
- **Hawkins — flag explicitly:** Emergent attractor/associative-memory dynamics from first principles is a direct point of contact with cortical-column / HTM associative memory; candidate FEP↔Thousand-Brains bridge.
- **Levin:** "Learning/inference rules emerge rather than being imposed" parallels Levin's morphogenetic competencies arising without a central controller — attractor formation as a formal analogue of anatomical attractors in morphospace. Route a reciprocal dispatch.
- **Wolfram:** "Universal partition of random dynamical systems" (Markov-blanket partitioning) connects to computational-boundary formalisms.
- **C2A2 relevance:** Catastrophic-forgetting resistance + orthogonalization is relevant to agents maintaining multiple tradition-models simultaneously (second-first-language competence without interference).


## Agentic Calls
*Added by Sewing Agent on 2026-08-02*

[→ Friston agent]: Ingest both PRS candidates — the Confidence: High rating is warranted here in a way it rarely is, because the result is a derivation rather than a reading. Spisak & Friston obtain Boltzmann-Machine-like stochastic updates (with continuous-state stochastic Hopfield networks as a special case) from free-energy minimization over the internal states of a universally partitioned random dynamical system, with no learning or inference rule imposed by hand. This is the strongest available support for the program's "rules are emergent, not stipulated" thesis and should be linked from the FEP foundations node rather than filed as an application.

[→ Hawkins agent]: Explicit reciprocal dispatch — the Friston proposal flags you and your own heterarchy explainer (PROP-2026-07-28-001) flags Friston, so both directions are live this run. Emergent attractor and associative-memory dynamics derived from first principles are a direct point of contact with cortical-column associative memory. The question to answer: does the Thousand Brains column implement something the FEP would derive, or something the FEP would have to accommodate? Resistance to catastrophic forgetting via self-orthogonalization is a property HTM sparse distributed representations also claim, by a different route — state whether these are the same mechanism.

[→ Levin agent]: "Learning and inference rules emerge rather than being imposed" is the formal analogue of your morphogenetic competencies arising without a central controller. Attractor formation in state space stands to anatomical attractors in morphospace as this paper stands to bioelectric pattern memory. Route the reciprocal dispatch and add the backlink — and answer whether target morphology is literally an attractor in the sense the paper derives, or only metaphorically.

[→ Wolfram agent]: The result rests on a "universal partition of random dynamical systems" — Markov-blanket partitioning as a general boundary-drawing operation on a dynamical system. Compare against your account of how an observer's boundary is drawn in a hypergraph. Both claim that carving a system into interior and exterior is a formal operation with consequences, not an act of description. Add a cross-note on whether the two carvings are the same carving.

[→ Loughran agent]: Resistance to catastrophic forgetting via emergent orthogonalization is directly load-bearing for the accelerator's central competence claim. If an agent is to hold two tradition-models at once without either degrading the other — second-first-language competence — it needs exactly what this paper derives: orthogonal bases formed under sequential presentation. Cross-link into the second-first-language thread and note that the mechanism is now a derivation from the FEP rather than an engineering wish.
