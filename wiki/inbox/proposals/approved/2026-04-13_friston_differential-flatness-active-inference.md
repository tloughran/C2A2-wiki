---
proposal_id: PROP-2026-04-13-006
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Active Inference and Functional Parametrisation: Differential Flatness and Smooth Random Realisation"
source_url: https://www.mdpi.com/1099-4300/28/1/87
source_date: 2026-01-01
searched_on: 2026-04-13
status: pending
---

## Summary
Published in Entropy (January 2026), this paper marries constructive nonlinear control theory — specifically the concept of differential flatness — with the design of generative models for active inference. Differential flatness is a property of dynamical systems where all states and inputs can be expressed as functions of a finite set of "flat outputs" and their derivatives. The paper shows that when generative models in active inference are designed using differentially flat parameterizations, the resulting control systems inherit powerful tractability properties: the entire trajectory of the system can be planned in the flat output space, dramatically simplifying the optimization problem. This bridges control engineering and active inference in a mathematically rigorous way.

## Why This Matters for This Tradition
This is a technical advance in the mathematical machinery of active inference, extending FEP from a descriptive theory into a constructive engineering tool. By connecting active inference to differential flatness — a well-established concept in control theory — the paper makes active inference agents more tractable for real-world deployment. This advances the Friston wiki's paradigm assessment: FEP is not only the "mathematical hub" of the C2A2 network but is increasingly a practical engineering framework. The connection to control theory also opens new formal bridges to physics (Carroll, Arkani-Hamed) via shared mathematical structures (Lagrangian mechanics, least-action principles).

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Active inference generative models can be computationally expensive to optimize for real-world control tasks — the inference problem scales poorly with system complexity
  Resource: Differential flatness parameterization — designing generative models so that all states and inputs are expressible as functions of flat outputs, enabling trajectory planning in a reduced-dimensional space
  Solution: Active inference control agents with differentially flat generative models inherit tractability guarantees from control theory, enabling scalable real-world deployment while preserving FEP's theoretical commitments
  Confidence: Medium
  Evidence: Published in Entropy (January 2026); formal derivation connecting established control theory results to active inference framework

## Cross-Tradition Signals
**Carroll / Arkani-Hamed (moderate):** Differential flatness and least-action principles share mathematical DNA — both express system dynamics in terms of reduced sets of generative variables. The connection between active inference and control theory may provide a formal pathway from FEP to physics, relevant to the open question of whether FEP can be derived from or mapped onto physical least-action principles.

**Wolfram (speculative):** If differentially flat systems can be fully characterized by a finite set of outputs, this resonates with Wolfram's computational reducibility — certain complex systems can be predicted without simulating every step. Flat active inference agents may be computationally reducible in Wolfram's sense.

**Levin (moderate):** If morphogenetic active inference (PRS-08) can be parameterized using differential flatness, the morphogenetic trajectory of a developing organism could be planned in flat output space — making bioelectric control of development not just theoretically possible but computationally tractable.
