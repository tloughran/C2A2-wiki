---
proposal_id: PROP-2026-09-21-002
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "A platform for automated training of mammalian cell physiology"
source_url: https://www.biorxiv.org/content/10.64898/2026.08.13.744473v1
source_date: 2026-08-13
searched_on: 2026-09-21
status: pending
---

## Summary

Erickson and colleagues (Allen Discovery Center at Tufts + Wyss Institute, with Levin as senior author) present the **Cell Trainer**: a device that runs automated behavioral-training experiments on *non-neural* mammalian cells. Timed pulses of drugs are the stimulus; a moving fluorescence microscope reading genetically encoded reporters is the behavioural readout. It runs open-loop (a pre-scheduled pulse programme) or closed-loop (the controller decides what to dispense from the cells' own live response, under one second after each image). An analysis pipeline segments and tracks every individual cell, so population heterogeneity — "good vs. poor learners" — is measurable rather than averaged away. Hardware schematics and software are being released openly.

Two demonstrations. **Feedforward:** C2C12 mouse myoblasts expressing the calcium reporter GCaMP6f were given three trains of five 2-minute DMSO pulses. Response magnitude rose significantly across trains (replicate-level one-sample t-test between first and third train, p = 0.0404) — dynamics *consistent with* sensitization — without a rising baseline, which argues against cumulative photodamage or cell rounding as the explanation. **Feedback:** NRK-49F rat kidney fibroblasts expressing the pH/voltage reporter ArcLight were held below a fluorescence setpoint by controller-issued 30-second pulses of acidic medium, in two chambers controlled simultaneously.

## Why This Matters for This Tradition

This is the instrument Levin's diverse-intelligence programme has been missing. The claim that non-neural cells possess learning-like competencies has rested on scattered single-system results (*Stentor*, HEK293, PC12, *Physarum*) obtained with bespoke, largely manual rigs. A general, open, closed-loop training platform converts that claim from a collection of anecdotes into a **standardised experimental protocol other labs can run** — which is exactly the move that turns a provocative thesis into a research programme with a track record. It also operationalises the "training rather than rewiring" thesis: control cell physiology by giving cells experiences, the way one trains an animal, instead of editing the molecular pathway.

Note the authors' own restraint, which should be preserved in any triplet: they explicitly say the biological findings are **preliminary**, that these metrics "alone are insufficient to declare the presence of learning," and that replicate counts were small (3 chambers for C2C12, 1 for PC-3, 4 for NRK-49F).

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Claims that non-neural cells learn have been made from a scattering of one-off systems and hand-run protocols, with no shared instrument — so results cannot be compared across labs, cell types, or stimulus regimes, and the field cannot accumulate a track record.
  Resource: The Cell Trainer — a fluidic cell-culture platform with computer-timed drug perfusion, a mobile fluorescence microscope, open-loop and closed-loop modes, and openly released schematics and software.
  Solution: Cell training becomes a repeatable, transferable experimental protocol rather than a bespoke demonstration, which is the precondition for the diverse-intelligence claim to be tested (and falsified) outside Levin's own lab.
  Confidence: High
  Evidence: "we present a device, the Cell Trainer, capable of performing a wide variety of automated training experiments on non-neural mammalian cells... To accelerate research in the field of cell training, learning, and memory, we are openly sharing the Cell Trainer schematics and software with the research community." High confidence is about the *instrument and its release*, not about any learning claim.

PRS-CANDIDATE-02:
  Problem: Population-averaged readouts cannot tell a uniformly modest change across all cells from a strong change in a competent subpopulation — so "did these cells learn?" is unanswerable at the level the question is actually asked.
  Resource: A single-cell segmentation, tracking and normalisation pipeline (Cellpose-based) that traces every cell's fluorescence across the whole experiment, plus per-cell metrics for habituation, sensitization, and anticipation tested against order-shuffled null distributions by permutation test.
  Solution: Behavioural heterogeneity within an isogenic culture becomes a measurable quantity — responders vs. non-responders, spatial correlation structure, per-cell learning scores — moving the unit of analysis from "the culture" to "the cell."
  Confidence: High
  Evidence: Habituation and sensitization score distributions differ significantly from shuffled-order nulls by permutation test; pairwise response correlation falls significantly with inter-cell distance among responders (slope −1.12e-04 Δr/μm, fit r = −0.168, 1047 cell pairs, replicate-level Mantel p = 0.013).

PRS-CANDIDATE-03:
  Problem: Controlling cell physiology by rewiring pathways is defeated by the cells' own adaptive competence — chemoresistance, transgene silencing — because the intervention is static and the cell is not.
  Resource: Real-time closed-loop control: the device computes mean cell fluorescence from each image and chooses the next perfusion within a second, holding an ArcLight reporter below a user-set setpoint with acid pulses, in two chambers at once.
  Solution: A demonstration that cell physiological state can be *steered* by feedback, which is the substrate on which reinforcement-learning-style training of cells (reward/punishment schedules, later model-predictive or learned controllers) could be built.
  Confidence: Medium
  Evidence: The controller reliably fires a pulse whenever the setpoint is crossed (Fig 9). Medium because the demonstration is control of a reporter, not of a *learned* state, n = 1 chamber per trace, and acid exposure killed cells during the runs — the authors note the population sometimes could not return to setpoint as a result.

PRS-CANDIDATE-04:
  Problem: Is the response change observed across repeated stimulation actually learning, or an artefact (accumulating membrane damage, photodamage, morphological change)?
  Resource: Two discriminating observations — resting fluorescence after train 1 ≈ after train 2 despite clearly rising peaks; and cell-line-dependent response *shape* (C2C12 peaks are biphasic/"notched", PC-3 peaks rounded) under an identical pulse schedule.
  Solution: The rise is not simply accumulating damage, and the underlying calcium release/sequestration dynamics differ by cell type — so the effect has structure a pure-artefact account does not predict.
  Confidence: Speculative
  Evidence: The authors are explicit that this is not settled: additional defining features of sensitization "were not tested or quantified," the anticipation results after trains 1 and 2 point in *opposite* directions and require "additional interpretation," and simpler explanations such as membrane damage accumulation have yet to be ruled out. Treat as an open experimental question, not a finding.

## Cross-Tradition Signals

**Friston / active inference — strong, and it is the closed loop that carries it.** The setpoint-holding controller is an external active-inference loop wrapped around a cell population: sense (image), compare to a preferred state, act (perfuse) to keep the sensed state within a bounded range. The paper builds the homeostat *in the apparatus* while asking whether the cells run one *internally*. That framing gives the long-standing Levin–Friston question ("is active inference present in non-neural substrates?") an experimental handle: the same setpoint architecture can be moved across the membrane, in increments, and the division of labour measured. Note the contrast with the planarian and bioelectric-setpoint work already in the vault, where the setpoint is endogenous and bioelectrically stored — here it is imposed by the experimenter, which is a cleaner control condition than anything yet in the Levin file. Worth an explicit dispatch.

**Hawkins.** The paper's own argument that single cells may be tractable model systems for mechanisms shared with neural tissue ("molecular components and functional algorithms shared between neural tissues and their ancient unicellular precursors") runs against the grain of a cortical-column-specific account of learning. If sensitization and anticipation-like signatures are confirmed in myoblasts, the substrate-specificity of the cortical-column story needs restating rather than assuming.

**C2A2 / AI alignment.** The authors propose, as a future direction, an LLM-based controller that translates natural-language commands into stimulus schedules for "two-way communication with cells," and speak of *persuading* rather than programming them. That is a live instance of the C2A2 question about what counts as membership in a communicative community, and it connects to the Levin-tradition alignment material already held (Lyons/Pio-Lopez "Alignment Is to a Virtual Governor"; "From Cancer to AI Alignment"). Flag as forward-looking, not demonstrated.

**Kastrup / McGilchrist.** The paper closes by saying this research programme "has implications for philosophy of mind and questions about the utility of recognizing cognition in unconventional entities." The word doing the work is *utility* — a pragmatic, instrument-first criterion for ascribing cognition. That is a different justification from Kastrup's metaphysical one, and the divergence is worth recording rather than smoothed over: two traditions can endorse "cognition in non-neural matter" for reasons that do not compose.

## Provenance Note

This source was identified as a **known gap** in the 2026-09-17 daily run, which located the citation on Levin's preprints page but could not card it: `web_fetch` refused the bioRxiv URL under the provenance restriction and the browser-pane request was auto-declined, so no card was written (correctly — a title-only card is the Wright mistake). Today the URL was surfaced through a WebSearch result, which cleared the provenance restriction, and the full text was read before this card was written. The gap is closed.
