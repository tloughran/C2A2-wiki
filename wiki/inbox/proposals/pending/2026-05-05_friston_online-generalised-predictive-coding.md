---
proposal_id: PROP-2026-05-05-003
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Online Generalised Predictive Coding"
source_url: https://arxiv.org/abs/2605.02675
source_date: 2026-05
searched_on: 2026-05-05
status: pending
---

## Summary
Bazargani, Urbas, Razi, Murphy & Friston (arXiv 2605.02675, May 2026) extend generalised filtering — Friston's joint scheme for inferring latent states, learning model parameters, and estimating uncertainty (variational Kalman-Bucy filtering / generalised predictive coding / Dynamic Expectation Maximisation / DEM) — to *online* operation. They specialise DEM through a separation of temporal scales: fast Bayesian belief-updating about hidden states is contextualised by slow updating of parameters and precisions. Numerical studies on a non-linear, potentially chaotic generative model demonstrate that "online DEM" (ODEM) can perform inference, learning, and uncertainty estimation simultaneously in dynamic environments — a long-standing open problem in active-inference engineering.

## Why This Matters for This Tradition
This is a fresh, technically substantive Friston paper inside the past 30 days. It addresses a known scaling problem for the active-inference research program: how to deploy variational schemes online without sacrificing the joint inference-learning-uncertainty estimation that distinguishes them from standard filtering approaches. This is the engineering plumbing that turns the "FEP as universal law" claim (PRS-07) into deployable systems — and it is exactly the Friston/Razi/UCL-FIL line, not a Verses press release. Should be captured as PRS-15 (or next).

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Active inference and generalised predictive coding offer joint inference, learning, and uncertainty estimation in principle, but the implementations available (DEM and variants) have been offline / batch — unable to assimilate streaming data while also updating parameters and noise estimates without retraining.
  Resource: ODEM — Online Dynamic Expectation Maximisation — built by separating temporal scales: fast updates over hidden states, slow updates over parameters and precisions, all variationally consistent.
  Solution: A biologically-inspired, theoretically-grounded online inference scheme that performs triple estimation (states, parameters, precisions) on streaming data, validated on non-linear and potentially chaotic generative models — closing the gap between FEP's theoretical claims and deployable inference.
  Confidence: High
  Evidence: The paper's core technical contribution is the temporal-scale separation derivation and its numerical demonstration on a non-linear chaotic system.

PRS-CANDIDATE-02:
  Problem: Engineering and neuroscience have parallel literatures on the same mathematical object (variational Kalman-Bucy filtering / generalised predictive coding / DEM), but these have not been unified under one online procedure usable across disciplines.
  Resource: Recognition that the engineering, neuroscience, and time-series-analysis traditions describe the *same* generalised filtering scheme; ODEM as the cross-disciplinary online variant.
  Solution: A single online algorithmic specification that engineers, neuroscientists, and statisticians can all deploy — making FEP's claim of substrate independence operational at the level of *implementation* rather than only at the level of formal proof.
  Confidence: Medium-High
  Evidence: The paper explicitly notes the disciplinary multi-naming and proposes ODEM as the unified specialisation.

## Cross-Tradition Signals
- **Levin (medium-strong):** ODEM provides a candidate computational substrate for the morphogenetic active-inference bridge (PRS-08). If cells perform something like online generalised filtering on bioelectric signals, ODEM is the formal specification of what their inference looks like at the algorithmic level. Worth flagging — this is the implementation layer Levin's program currently lacks.
- **Hawkins (medium):** Hawkins' cortical-column model implies many local predictive systems each performing online inference on their reference frames. ODEM is a candidate algorithmic instantiation — the temporal-scale separation matches Hawkins' fast/slow distinction between perception and reference-frame learning.
- **Wolfram (speculative):** The temporal-scale separation maps onto Wolfram's distinction between fast computational dynamics and slow rule-evolution. Joint formulation possible: ODEM as variational counterpart to the Ruliad's multi-rate evolution.
- **Carroll/Arkani-Hamed (speculative-medium):** Generalised filtering on chaotic non-linear generative models is exactly the regime where the FEP-physics connection becomes interesting. If ODEM works on chaotic systems, it is a candidate for modeling physical observers — bears on the FEP-as-physics speculation in PRS-07.
- **Loughran/C2A2 (medium):** The temporal-scale separation in ODEM is structurally analogous to the C2A2 Wiki agent network: fast belief updates inside each tradition agent (ingestion of new sources), slow parameter updates at the Master Agent level (cross-tradition synthesis). Worth flagging as a potential design pattern for the Wiki itself.
