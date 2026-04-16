---
proposal_id: PROP-2026-04-08-005
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: paper
source_title: "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence"
source_url: https://arxiv.org/abs/2412.18354
source_date: 2024-12-24
searched_on: 2026-04-08
status: pending
---

## Summary
This white paper by Viviane Clay, Niels Leadholm, and Jeff Hawkins introduces the Thousand Brains Project's first concrete AI implementation — a sensorimotor agent system called "Monty" (named for Vernon Mountcastle). The paper formalizes the transition from Hawkins' theoretical Thousand Brains framework into a working AI architecture built around repeating computational units called "learning modules," each modeled on a cortical column. Sensorimotor interaction with the environment — not passive data ingestion — is the foundational knowledge acquisition mechanism.

## Why This Matters for This Tradition
This is the first formal publication from Hawkins' team translating Thousand Brains Theory into a runnable AI system, bridging the gap between neuroscientific theory (cortical columns as reference-frame builders) and implemented machine intelligence. It is the program's most significant empirical step since the 2021 book and belongs in the wiki as a core PRS resource.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Deep learning systems cannot learn efficiently from sensorimotor interaction with the real world — they require massive labeled datasets and cannot transfer knowledge across tasks in the way biological agents do.
  Resource: The Thousand Brains Project's "learning module" — a cortical-column-inspired unit that builds CAD-like spatial models through active sensorimotor exploration, enabling rapid continual learning without catastrophic forgetting.
  Solution: Monty demonstrates that sensorimotor agents built on cortical column principles can perform 3D object recognition and pose estimation with dramatically less data than deep learning — and do so continuously, without retraining from scratch.
  Confidence: High
  Evidence: Paper demonstrates recognition and pose estimation results; explicitly contrasts data efficiency with deep learning baselines.

PRS-CANDIDATE-02:
  Problem: HTM and Thousand Brains Theory have remained largely theoretical since Hawkins' 2021 book — no sufficiently complete implementation has existed to test whether the principles actually produce robust AI behavior.
  Resource: Monty open-source framework (github.com/thousandbrainsproject/tbp.monty) — the first working instantiation of a thousand-brains system, with full documentation and reproducible experiments.
  Solution: A concrete, testable platform for validating and extending Thousand Brains Theory in AI research, now released under an open-source license with Gates Foundation support.
  Confidence: High
  Evidence: GitHub repository active; Numenta spun the project out as an independent nonprofit in January 2025 with dedicated team.

## Cross-Tradition Signals
**Friston**: Monty's sensorimotor learning loop — perception → prediction → action → update — maps closely onto Friston's active inference cycle. Flag for Friston Agent: both systems treat action as part of the inferential loop, not downstream of it. This is the strongest empirical convergence yet between HTM and FEP.
**Levin**: Monty's learning modules are semi-independent units that vote on a shared world model — structurally identical to Levin's distributed cellular agents forming collective behavior. Flag for Levin Agent: the implemented architecture of Monty is the AI version of basal cognition.
**Wolfram**: Reference frames as CAD-model-like structures for world modeling — resonates with Wolfram's computational space as the medium in which structures unfold.
