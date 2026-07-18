---
proposal_id: PROP-2026-07-13-004
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Topographic Variation in Human Neurotransmitter Receptor Densities Explains Differences in Intracranial EEG Spectra"
source_url: https://onlinelibrary.wiley.com/doi/10.1002/hbm.70393
source_date: 2025 (journal version; recirculating mid-2026 — see caveat)
searched_on: 2026-07-13
status: pending
---

## Summary
Stoof, Friston, Tisdall, Cooray & Rosch fit biophysically informed neural mass models to a normative intracranial EEG dataset using dynamic causal modelling (DCM), and show that regional variation in neurotransmitter *receptor density* explains a substantial share of the variance in cortical population dynamics — i.e., in the local iEEG spectrum. Supplying receptor-distribution maps as priors improves model evidence. The output is a cortical atlas of neurobiologically informed intracortical synaptic connectivity parameters, offered as a normative resource for future DCM studies.

*Caveat (surfaced, not hidden): this is a work-not-yet-captured rather than a clean within-30-days item. It surfaced in search as a June-2026 Friston publication, but the verifiable record shows a 2025 journal version (Human Brain Mapping, doi 10.1002/hbm.70393) with an earlier bioRxiv preprint. The date field above is therefore hedged. It passes the filter on the "significant work not yet in the wiki" clause, not on recency. Tom/orchestrator should confirm the version before ingestion.*

## Why This Matters for This Tradition
Friston's program is often criticized as unfalsifiable metaphysics with a Bayesian veneer. This is the counter-evidence line: a concrete, empirically-fit DCM in which the free-energy machinery is used to *infer synaptic parameters from data* and is scored by model evidence against real intracranial recordings. It also does load-bearing work for the theoretical arc the wiki has been tracking. The precision-psychiatry talk (PROP-2026-05-18-003) claims that neuromodulation encodes precision and that psychopathology is aberrant precision-weighting. That claim needs receptor density to actually determine population dynamics. This paper is the empirical hinge on which that theoretical claim swings.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Precision-weighting accounts of perception and psychopathology assign a central role to neuromodulatory receptor systems, but the explanatory gap between cortical microarchitecture (receptor expression) and mesoscopic electrophysiology (the signals we actually record) has been unbridged. Without that bridge, "precision" is a free parameter.
  Resource: DCM with biophysically informed neural mass models fit to a normative intracranial EEG dataset, using PET/autoradiography-derived receptor-density maps as empirical priors on synaptic connectivity.
  Solution: Receptor-density variation is shown to explain regional variance in cortical population dynamics, with receptor-informed priors *improving model evidence* — i.e., the microarchitecture-to-signal link is established variationally rather than assumed. Precision acquires a measurable neurochemical substrate.
  Confidence: High
  Evidence: "Incorporating prior information on receptor distributions further improved model evidence, indicating that variability in receptor density explains some variance in cortical population dynamics."

PRS-CANDIDATE-02:
  Problem: DCM studies of electrophysiology have lacked a normative baseline — each study re-estimates synaptic parameters from scratch, so no one can say whether an individual patient's inferred connectivity is anomalous.
  Resource: A cortical atlas of neurobiologically informed intracortical synaptic connectivity parameters, released as a normative resource.
  Solution: Individual-difference and patient studies can now be scored against a normative synaptic connectome — the precondition for the "computational psychiatry as deviation from normative precision" program to be run at all.
  Confidence: High
  Evidence: The paper explicitly frames its output as "a normative resource for future DCM studies of electrophysiology" and "a methodological foundation to integrate multimodal data."

## Cross-Tradition Signals
- **[[Levin]]** — the interesting inversion. Here Friston's tradition grounds an abstract informational quantity (precision) in a *material* substrate (receptor density), while Levin's tradition (this same cycle, PROP-2026-07-13-002) drives in the opposite direction, showing a material variable (nuclear membrane voltage) doing informational, memory-like work. Two traditions crossing in opposite directions through the same matter/information boundary is worth the master agent's attention.
- **[[Hawkins]]** — receptor-density topography as the microarchitectural correlate of cortical-column heterogeneity; Hawkins' thousand-brains framework assumes a repeated canonical circuit, and this paper quantifies how far from canonical the real cortex is.
- **[[C2A2 / master]]** — methodological, not thematic: this is a worked example of a tradition earning credibility by making its central abstraction *measurable*. That is the same move C2A2 is attempting with PRS-chain and listening metrics.

## Programmatic Flag (not a PRS — for the master agent)
Two institutional events in Friston's research program occurred within this cycle's 30-day window and are recorded here because they bear on the program's track record even though they generate no PRS triplet:
- 2026-06-18: VERSES AI, the company built on active inference (the "Genius" platform), halted all AI research and development.
- 2026-06-27: Karl Friston resigned as Chief Science Officer of VERSES AI.

These are *commentary/reportage about* Friston, not material *from* him, so per the standing quality filter no proposal is made from them. But the C2A2 measurement framework explicitly treats a research program's track record — the questions it generates and whether its institutional carriers survive — as evidence about the program. The collapse of the flagship commercial instantiation of active inference is a data point of exactly that kind, and the master agent should decide whether the framework wants to register it. Recommend Tom rule on whether "institutional/programmatic events" become a first-class node type in the wiki, distinct from PRS triplets.
