---
proposal_id: PROP-2026-11-23-002
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "A Closed-Loop Robot Scientist for Autonomous Biological Discovery"
source_url: https://doi.org/10.64898/2026.09.11.751076
source_date: 2026-09-18
searched_on: 2026-11-23
status: pending
---

## Summary
This bioRxiv preprint (Bielawski, Srinivasan, Gaylinn, Beaulieu, Brucker, Levin, Lunshof, Bongard, Blackiston) introduces MOMbot, the Multimodal Organismal Modulation Robot. One hardware platform combines four ways of intervening on living material: chemical delivery, electric fields, mechanical vibration and temperature control. It adds high-resolution imaging and an online active-learning algorithm that designs, runs and refines its own interventions. The authors tested it on three kinds of material spanning three orders of magnitude in size: *Xenopus* embryos, motile mucociliary organoids, and loose ectodermal stem cells. Their demonstrations were: thermal control of how fast embryos develop, chemical perturbation read out through behavior, programmable electrical stimulation, and vibration-driven assembly of working organoids from loose cells. The active learner aimed experiments where the outcome was most uncertain, and with few samples it mapped how motile organoids respond to different durations of electrical stimulation.

## Why This Matters for This Tradition
This is the peer-review-track paper behind the "MomBot" robot scientist that Levin described in his ALife keynote (approved 2026-11-09). That proposal captured the idea. This paper captures the working instrument and its first results. It turns TAME's (Technological Approach to Mind Everywhere) call to probe unconventional agents empirically into an automated loop that does not depend on human intuitions about which interventions are worth trying.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The space of physical and chemical interventions that can steer cells, tissues and synthetic organisms (Xenobots, organoids) is combinatorially vast and mostly unexplored. Human-designed experiments sample it sparsely and with an anthropocentric bias.
  Resource: MOMbot, a robot scientist with four intervention modalities on one platform (chemical, electrical, vibrational, thermal), paired with imaging and an online active-learning loop.
  Solution: Autonomous closed-loop experimentation that generates, runs and refines its own interventions. It was validated on embryos, mucociliary organoids and dissociated ectodermal cells.
  Confidence: Medium (preprint; not yet peer reviewed)
  Evidence: Abstract: "a robot scientist that integrates four physical intervention modalities ... paired with high-resolution imaging and an online active learning algorithm that autonomously generates, executes, and refines interventions."

PRS-CANDIDATE-02:
  Problem: How can someone efficiently learn the input–response map of a biological collective whose competencies are unknown in advance?
  Resource: Uncertainty-directed active learning, which concentrates trials near the regions where the outcome is most uncertain.
  Solution: A sample-efficient map of how motile organoids respond to different durations of electrical stimulation, a first concrete case of "communicating with tissues" by automated querying.
  Confidence: Medium
  Evidence: Abstract: "concentrates interventions near regions of maximal outcome uncertainty, yielding sample-efficient discovery of an electrical duration–response relationship for motile organoids."

PRS-CANDIDATE-03:
  Problem: Can physical signals alone, with no genetic modification, drive loose cells to self-assemble into functional bodies?
  Resource: Vibrational (mechanical) modulation delivered by the robot.
  Solution: Vibration-driven assembly of functional mucociliary organoids from loose cells, which adds mechanics to bioelectric and chemical inputs as a non-genetic steering channel.
  Confidence: Medium
  Evidence: Abstract lists "vibrational assembly of functional mucociliary organoids from loose cells" among the demonstrated capabilities.

## Cross-Tradition Signals
- **Friston (active inference):** The robot's loop picks the next experiment to resolve the most uncertainty. That is the "epistemic value" (expected information gain) term of expected free energy, applied to the scientist rather than the organism. Levin's keynote framed discovery itself as an active-inference-like loop, and this paper supplies a working instance. Flag: active inference at the level of the experimenter, aimed at non-neural substrates.
- **Wolfram (computation):** Searching intervention space with an automated explorer parallels Wolfram's "ruliology", the systematic enumeration of what simple rules do. Here the object enumerated is the response space of biological material.
- **C2A2 meta-signal:** MOMbot is a robot/AI-plus-human science team. That is a case study for C2A2's own claim that AI agents can speed up inquiry inside a tradition.

Note on the quality filter: Levin is a co-author (6th of 9; joint ICDO work with the Bongard and Blackiston labs), so this is from the Levin program but not solely by him. It was posted 2026-09-18, which is outside the 30-day window. It is proposed under the "significant work not yet captured" clause: grep found no match for the DOI, "MOMbot" as a paper, or "Bielawski" anywhere in the Levin wiki or the proposals.
