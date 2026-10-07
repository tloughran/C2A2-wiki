---
proposal_id: PROP-2026-10-06-002
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "08/2026 - Attention in Monty (a Hackathon Prototype)"
source_url: https://forum.thousandbrains.org/t/08-2026-attention-in-monty-a-hackathon-prototype/1219
source_date: 2026-10-05 (forum post; talk given at the August 2026 Rome Focus Week)
searched_on: 2026-10-06
status: pending
---

## Summary
Scott Knudstrup (@sknudstrup) presents the attention system prototype built by Team "Fate Attenzione" at the Rome Focus Week. It combines bottom-up salience with top-down signals from learning modules. The immediate goal is to constrain movement and sensory input to a specific object or sub-object until it has been recognized. Technical elements listed on the forum page: 3D attentional regions, voxel-based representations, excitatory and inhibitory signaling, and hard versus soft filtering of motor control. Discussion covered scale adjustment, tracking moving objects, inhibition of return, and how unexpected stimuli interrupt ongoing attention. The video runs about 1h24m.

**Provenance caveats:** Only the forum summary was read. The video was not watched, and no code or PR links appear on the page. The presenter is a TBP team member, not Hawkins, and the source is team-channel material of the kind accepted in earlier runs. Confidence in specifics beyond the forum summary is limited.

## Why This Matters for This Tradition
This is the first built prototype of the attention arc already in the wiki (PROP-2026-09-15-001, PROP-2026-09-22-001, PROP-2026-09-15-002). It turns attention from a theory topic into running code. It also operationalizes the "attention gates votes and inputs" framing within the Thousand Brains architecture.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Monty's learning modules can receive input from anywhere in the sensory field, so recognition of a specific object or sub-object is not protected from distraction or premature movement.
  Resource: A prototype attention system combining bottom-up salience with top-down learning-module signals, using 3D voxel attentional regions with excitatory and inhibitory signaling.
  Solution: Sensory input and movement are held on a target object or part until it is recognized, with hard or soft filtering as the control choice. Inhibition of return and interruption by unexpected stimuli are named as design questions.
  Confidence: Medium
  Evidence: Forum summary: "integrates bottom-up salience with top-down signals from learning modules... constrain movement and sensory input to a specific object or sub-object until it has been recognized."

PRS-CANDIDATE-02:
  Problem: It is unsettled whether attention should be implemented as a filter on input only or as a controller of sensorimotor movement.
  Resource: The hard-versus-soft motor filtering distinction in the prototype.
  Solution: The prototype keeps both options open. Which is correct is left as a testable design question, not claimed as resolved.
  Confidence: Speculative
  Evidence: Forum summary lists "hard versus soft filtering approaches for motor control" as a technical element, without results.

## Cross-Tradition Signals
- **Friston:** Top-down signals gating bottom-up salience is close to precision-weighting in active inference. This is a candidate bridge or a productive disagreement, as with the thalamus (wiki Q9). Do not record as convergence without a source stating it.
- **McGilchrist:** Attention is central to his account of the hemispheres. A narrow, constrained "hold on one object until recognized" regime may be worth comparing with his claims on narrow versus broad attention. This is speculative.
- **Fredrickson:** The wiki already asks whether positivity widens reference-frame access. Attention-as-constraint is the opposite pole of that question (broaden-and-build).
