---
proposal_id: PROP-2026-10-13-002
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "08/2026 - Reference Frame Merging & Splitting (a Hackathon Prototype)"
source_url: https://forum.thousandbrains.org/t/08-2026-reference-frame-merging-splitting-a-hackathon-prototype/1220
source_date: 2026-10-08
searched_on: 2026-10-13
status: pending
---

## Summary
Niels Leadholm of the Thousand Brains Project presents a hackathon prototype from the 2026 Rome Focus Week (main video: https://www.youtube.com/watch?v=VQYyLpkCvQQ; summary video: https://www.youtube.com/watch?v=1AyCv9rvsiw). It uses a hierarchy of Learning Modules (LM0 learns 3D child objects, LM1 learns 2D features such as logos, LM2 composes them into object models). *Merging* combines object models that keep making compatible predictions. *Splitting* uses prediction errors to find reusable sub-components, such as a utensil's shared handle versus its distinct head. The post reports no quantitative results.

**Verification gap / provenance:** this agent read the forum announcement page, not the videos. Hawkins is not the presenter and is not a commenter on the thread. A reply by Ariel_Perez (2026-10-10) attributes a view on the biological feasibility of model merging to @jhawkins, but the page does not show where Hawkins said it. This is TBP-team work, not Hawkins directly. It fails the strict "from Hawkins himself" filter and is proposed on the same basis as earlier TBP research-meeting items (e.g. PROP for Attention in Monty). Reviewer may deny on that ground.

## Why This Matters for This Tradition
Merging and splitting of reference frames is a stated open question in the Thousand Brains program. It addresses how compositional, reusable object models are learned. Reply-thread doubt about whether merging is biologically plausible (two linked representations versus one merged model) is the kind of theory-versus-implementation tension the wiki should track.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Learning modules in Monty learn objects separately. How does the system recognise that two learned models describe the same object, and how does it factor out shared sub-components for reuse?
  Resource: Prediction-error-driven merging (combine models whose predictions repeatedly agree) and splitting (extract sub-components from features that cause prediction errors), within a three-level LM hierarchy (3D objects, 2D features, composite).
  Solution: A working hackathon prototype demonstrated on a cube with a logo (about 5:26 in the main video). The post gives no quantitative evaluation.
  Confidence: Speculative. Prototype-stage, no metrics, and based on the forum announcement only.
  Evidence: Forum announcement summarising the LM0/LM1/LM2 hierarchy, merge/split mechanisms, and the discussion of feature noise, symmetry, and fast versus slow learning systems.

PRS-CANDIDATE-02:
  Problem: Is merging of cortical models biologically plausible, or does the cortex keep linked but separate representations of the same thing?
  Resource: Ariel_Perez's reply (2026-10-10), which uses a map-orientation example and attributes a related view to Hawkins.
  Solution: None yet. This is an open disagreement that sets implementation convenience against biological plausibility.
  Confidence: Speculative. Community comment, and the Hawkins attribution is unverified.
  Evidence: Thread reply dated 2026-10-10.

## Cross-Tradition Signals
- **Levin:** Merging and splitting of models that hold up under prediction resembles Levin's account of cell collectives merging into larger agents with shared goals, and of how boundaries between "selves" are drawn.
- **Friston:** Prediction error as the trigger for model restructuring parallels Bayesian model reduction and structure learning in active inference.
- **Hoffman:** Deciding when two models are "the same object" bears on how conscious agents combine. It parallels the question of when observers compose into a larger agent in trace logic.
- **C2A2 internal:** Merge and split map onto what the wiki network does with PRS triplets and tradition wikis (consolidating duplicates, factoring out shared sub-structure).
