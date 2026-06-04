---
proposal_id: PROP-2026-06-01-002
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Online Generalised Predictive Coding"
source_url: https://arxiv.org/abs/2605.02675
source_date: 2026-05-04
searched_on: 2026-06-01
status: pending
---

## Summary
Bazargani, Urbas, Razi, Murphy & Friston extend generalised filtering (Dynamic Expectation Maximisation / generalised predictive coding) to *online* data assimilation. By separating temporal scales, the scheme lets slow updating of parameters and precisions contextualise fast Bayesian belief-updating about dynamic hidden states — performing "triple estimation" (states, parameters, and uncertainty) continuously rather than in batch.

## Why This Matters for This Tradition
This is a concrete formal advance in the FEP/active-inference machinery from Friston's own group: it makes generalised predictive coding usable in streaming, real-time settings, closing part of the gap between FEP-as-theory and FEP-as-deployable-algorithm. It sharpens the program's claim that perception, learning, and action share one variational substrate.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Generalised filtering / DEM jointly infers states, parameters, and uncertainty, but in its standard form is batch-oriented — how can the same variational principle run online, assimilating data as it arrives?
  Resource: A separation-of-temporal-scales formulation: slow updating of parameters and precisions wrapped around fast belief-updating of hidden states.
  Solution: An online generalised predictive coding scheme that performs continuous triple estimation, extending generalised filtering to streaming applications.
  Confidence: High
  Evidence: The paper's stated contribution — specializing DEM for "online" data assimilation via a separation of temporal scales so that slow parameter/precision updates contextualise fast Bayesian updating of dynamic hidden states.

PRS-CANDIDATE-02:
  Problem: Predictive-coding accounts of brains posit nested timescales (fast inference, slow learning) but often lack a single algorithm realising both at once.
  Resource: The unified variational treatment of fast states vs. slow parameters/precisions in one filter.
  Solution: A formal demonstration that the timescale hierarchy falls naturally out of the generalised-filtering variational principle.
  Confidence: Medium
  Evidence: The temporal-scale separation is presented as intrinsic to the variational procedure rather than an add-on.

## Cross-Tradition Signals
The fast-states / slow-parameters timescale hierarchy maps onto **Hawkins'** cortical hierarchy and onto **Levin's** bioelectric dynamics (fast voltage signaling vs. slow morphogenetic memory) — a candidate Levin-Friston bridge where "slow precision updating" could be the formal analogue of morphogenetic target-state memory. The online/streaming framing also has **C2A2 relevance**: continuous belief-updating under bounded resources is the formal shape of an agent maintaining a tradition wiki in real time.
