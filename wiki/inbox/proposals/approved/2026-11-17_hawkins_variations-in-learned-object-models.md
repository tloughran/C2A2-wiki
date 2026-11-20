---
proposal_id: PROP-2026-11-17-003
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/09 - Exploring How Cortical Columns Handle Variations in Learned Object Models"
source_url: https://forum.thousandbrains.org/t/2026-09-exploring-how-cortical-columns-handle-variations-in-learned-object-models/1243
source_date: 2026-11-06
searched_on: 2026-11-17
status: pending
---

## Summary
Recorded TBP research meeting (presenter: rmounir) asking which properties an object model should keep invariant and which variations should be represented separately — covering allocentric reference frames, rotation and scale invariance, and modelling variability outside the core representation. It proposes a "3-Model Solution" and discusses affordances. Deformations are flagged as a case that "would require handcrafted solutions."

**Provenance caveat:** TBP team meeting; Hawkins not a listed presenter. The internals of the "3-Model Solution" were not extracted — verify before ingesting that triplet's Resource line.

## Why This Matters for This Tradition
This is the theory-side answer to Active Research Question 8 (what happens to a model when its object changes). The move to "model variability outside the representation" is a design commitment: invariance is achieved by keeping the core model fixed and representing variation separately, rather than by blurring the model.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Which properties should a column's object model hold invariant, and which variations (pose, scale, state, deformation) belong elsewhere?
  Resource: Allocentric reference frames plus a proposed "3-Model Solution" that represents variability outside the core object model
  Solution: Proposed architecture separating identity from variation; deformation explicitly unsolved
  Confidence: Speculative (architecture named, internals not verified)
  Evidence: Page summary: "3-Model Solution"; deformations "would require handcrafted solutions."

PRS-CANDIDATE-02:
  Problem: How do learned object models connect to what can be done with an object?
  Resource: Affordances discussed as part of the object-variation question
  Solution: Raised, not resolved
  Confidence: Speculative
  Evidence: Affordances listed among session topics.

## Cross-Tradition Signals
- Pairs with PROP-2026-11-17-001: two separate October–November sessions independently name deformation as the hard open case. That convergence is the signal; the PRS chain is "scale → variation → deformation."
- McGilchrist / Hoffman (weak): affordance talk moves object models toward action-relative meaning, which both of those traditions stress. Low confidence; note only.
