---
proposal_id: PROP-2026-09-14-002
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "The Artificial Experimentalist: Discovery and Control of Self-Organizing Phenomena with Autotelic Reinforcement Learning"
source_url: https://arxiv.org/abs/2608.26116
source_date: 2026-08-20
searched_on: 2026-09-14
status: pending
---

## Summary
Cvjetko, Hartl, Levin, Moulin-Frier and Oudeyer introduce CARL, an agent that explores a complex self-organizing system (Lenia, a continuous cellular automaton) in a closed loop: it invents its own goals, then learns a goal-conditioned policy for reaching them by making small, local perturbations while the simulation is still running. That "autotelic" setup — the agent sets the target rather than receiving it — contrasts with the standard open-loop method of setting initial conditions, running to completion, and looking at what came out. CARL finds stable solitons across a wide range of Lenia rules at a higher rate than heuristic baselines, and learns to steer the direction an existing soliton travels using few interventions.

## Why This Matters for This Tradition
Levin's program rests on the claim that many systems can be *controlled* through their own goal-directed competencies rather than micromanaged at the bottom level — the bioelectric interface is the biological case. This paper is the computational case, and it makes the claim testable: control is demonstrated, not just creation. It also supplies a tool for the harder question of how to *find* the intervention that a given self-organizing system will accept.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Exploration of complex self-organizing systems is open-loop — set initial conditions, run, observe — which cannot discover interventions that only work mid-trajectory.
  Resource: CARL, a closed-loop autotelic reinforcement-learning agent that samples its own diverse goals and learns a goal-conditioned policy of minimal local perturbations.
  Solution: Closed-loop autotelic search discovers stable Lenia solitons at a higher rate than heuristic baselines, showing that an agent that chooses its own goals is a better instrument for mapping a morphospace than a designed sweep.
  Confidence: High
  Evidence: Reported result that CARL discovers stable solitons across a wide range of Lenia update rules at a higher rate than heuristic baselines.

PRS-CANDIDATE-02:
  Problem: Can an emergent, self-organized pattern be steered after it exists, or only selected at the moment of creation?
  Resource: Goal-conditioned policy over minimal local perturbations applied to an already-running soliton.
  Solution: CARL learns to change a soliton's heading with few interventions — self-organizing patterns are controllable, not merely generatable. This is the computational analogue of re-specifying a bioelectric target morphology in an intact organism.
  Confidence: High
  Evidence: The authors report CARL learns to steer the movement direction of existing solitons with few interventions, "showing that CARL can control self-organizing patterns, not only create them."

PRS-CANDIDATE-03:
  Problem: What is the right interface to a system whose behavior is not decomposable into the behavior of its parts?
  Resource: The minimal-local-perturbation action space — the agent is forbidden from rewriting the system, only from nudging it.
  Solution: A constrained, low-bandwidth action channel is sufficient for control, which supports the "cognitive glue / competency" reading over the "rewrite the parts" reading of how such systems are steered.
  Confidence: Speculative
  Evidence: Framing of the action space as minimal and local; the generalization to biological control is the Levin program's claim, not this paper's.

## Cross-Tradition Signals
- **Friston / active inference**: an autotelic agent that samples its own goals to reduce uncertainty about a world model is close kin to expected-free-energy policy selection, where epistemic value drives exploration. The difference — intrinsic goal invention versus expected information gain — is a sharp, comparable difference worth a bridge note.
- **Wolfram**: Lenia is a continuous cellular automaton; the paper is effectively an automated search over rule space for rules that support persistent structures. That is computational irreducibility met with a learned heuristic rather than exhaustive enumeration.
- **Hawkins**: goal-conditioned policy learning over a sensorimotor loop is the reference-frame-and-movement story in a non-neural setting.

## Provenance Note
Confirmed by two independent searches. Also appears in the ALIFE 2026 proceedings (doi 10.1162/ISAL.a.971; presented 2026-08-20) and is listed on Levin's own publications page. Data and code reported at https://developmentalsystems.org/carl/. Abstract-level reading only; full text not retrieved.
