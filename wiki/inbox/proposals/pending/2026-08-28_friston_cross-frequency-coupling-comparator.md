---
prop_id: PROP-2026-08-28-001
proposal_id: PROP-2026-08-28-001
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Cross-Frequency Coupling as a Neural Substrate for Prediction Error Evaluation: A Laminar Neural Mass Modeling Approach"
source_url: https://direct.mit.edu/neco/article/38/8/1299/137926/Cross-Frequency-Coupling-as-a-Neural-Substrate-for
source_date: 2026-07-27
searched_on: 2026-08-28
status: pending
---

## Summary
Ruffini, Lopez-Sola, Palma, Sanchez-Todo, Vohryzek, Castaldo and Friston ask a question predictive coding has mostly left open: if the brain constantly compares what it predicted against what it received, what physical machinery does the comparing? They answer with a laminar neural mass model (LaNMM) — a computational model of a cortical patch that separates fast and slow cell populations by cortical layer — and show that two forms of cross-frequency coupling do the job. Signal-Envelope Coupling (a slow rhythm modulating the strength of a fast rhythm) performs the subtraction that yields a prediction error, and Envelope-Envelope Coupling (slow envelopes modulating fast envelopes) performs gating, which is how the model implements precision weighting.

The framing is borrowed from AM radio: a slow "carrier" wave transports a fast signal, and comparing the two envelopes recovers the mismatch. The paper then perturbs the model to see what breaks. Weakening fast inhibitory synapses (the deficit seen in Alzheimer's disease) and raising glutamate receptor gain (characteristic of serotonergic psychedelic states) both degrade the Comparator, offering a shared mechanistic account of two very different disruptions of experience.

## Why This Matters for This Tradition
Friston's programme has long asserted that cortex minimises prediction error under precision weighting, but "precision" has often functioned as a free parameter rather than a mechanism. This paper gives precision an explicit oscillatory implementation at the mesoscopic scale and makes it falsifiable against pathology.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Predictive coding requires a Comparator that subtracts prediction from evidence, and a precision term that weights the result, but neither has had a concrete neural implementation at the level of populations rather than single cells.
  Resource: A laminar neural mass model (LaNMM) exhibiting two distinct cross-frequency couplings — Signal-Envelope Coupling (SEC) and Envelope-Envelope Coupling (EEC) — analysed through an amplitude-modulation (AM radio) encoding framework.
  Solution: SEC is identified as the subtraction operation that generates prediction error, and EEC as a slower-timescale gate that implements precision weighting; the pair together constitute a physically realised Comparator.
  Confidence: Medium
  Evidence: The paper states that SEC "generates prediction-error signals by subtracting top-down predictions from bottom-up oscillatory envelopes, while EEC operates at slower timescales to implement gating — a critical mechanism for precision weighting."

PRS-CANDIDATE-02:
  Problem: Accounts of altered states and of neurodegeneration are usually built from separate vocabularies, with no shared computational quantity that both disrupt.
  Resource: Parameter perturbation of the LaNMM — specifically, deficits in fast inhibitory synapses and increased glutamate receptor gain.
  Solution: Both perturbations are shown to compromise the same Comparator function, so Alzheimer's disease and psychedelic states become two failure modes of one inferential mechanism rather than unrelated phenomena.
  Confidence: Speculative
  Evidence: The authors "discuss how deficits in fast inhibitory synapses, as seen in Alzheimer's Disease, and increased glutamate receptor gain, characteristic of serotonergic psychedelic states, may disrupt the Comparator process and compromise effective information processing." The claim is offered as a modelling implication, not an empirical result.

## Cross-Tradition Signals
- McGilchrist: precision weighting as a gating operation is a candidate mechanism for the attentional asymmetry his account rests on — a claim about which mode of attention is granted authority over the other becomes, here, a claim about which envelope gates which.
- Levin: if the Comparator is an oscillatory subtraction rather than anything neuron-specific, the same functional role could in principle be filled by non-neural bioelectric networks — an entry point for Levin's argument that cognition does not require brains.
- Kastrup: the psychedelic-state limb of the model treats altered experience as a quantitative change in gain on an inferential process, which is the kind of mechanistic reduction his analytic idealism contests; worth flagging as a live disagreement rather than a convergence.
