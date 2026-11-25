---
proposal_id: PROP-2026-11-24-002
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/10 - Consistent Orientation of Child Objects (COCO)"
source_url: https://forum.thousandbrains.org/t/2026-10-consistent-orientation-of-child-objects-coco/1258
source_date: 2026-11-17
searched_on: 2026-11-24
status: pending
---

## Summary
Recorded TBP research meeting (presenter: @hlee; main video https://www.youtube.com/watch?v=74WUPb8yV-s, ~63 min; summary video https://www.youtube.com/watch?v=vC4bsI42HpY). What started as work on symmetry turned into a broader finding: Monty can finish recognizing an object while many candidate poses are still in play. The proposed approach is top-down feedback from a parent learning module, which would help lower-level modules choose child poses that fit the larger object. The meeting also reviews how Monty represents rotations.

**Provenance caveat:** TBP team meeting implementing Hawkins's theory; Hawkins is not the presenter, though the chapter list shows a hand-off to "Jeff's Upcoming Topic" (51:17), which appears to be PROP-2026-11-24-001. Same provenance class as earlier approved TBP forum proposals. Strictly, this does not meet the "from Hawkins himself" filter; it is included on that precedent, and the reviewer may reject on provenance alone.

## Why This Matters for This Tradition
The wiki holds symmetry as an open problem (2027/07 "Ideas on Representing Symmetry," posted 2026-09) and holds negative-evidence hypothesis testing (PROP-2026-10-23-005). COCO reframes the symmetry issue as a more general one, namely unresolved pose hypotheses at the end of recognition, and proposes top-down feedback as the fix. That gives the thousand-brains feedback pathway a concrete job in Monty for the first time in the wiki's record.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Monty can declare an object recognized while many pose hypotheses remain, largely because of object symmetry ("Terminal Conditions: Why Do We Have So Many Hypotheses Left?", "Symmetry: The Core Issue").
  Resource: Top-down connections from a parent learning module carrying the larger object's context ("Approach: Top-Down Connections", "Q&A: Top-Down Message Content").
  Solution: Proposed: lower-level modules select the child pose that is consistent with the parent object, rather than resolving pose bottom-up alone.
  Confidence: Medium (problem); Speculative (mechanism, from post summary and chapter titles)
  Evidence: Forum description: "Monty can finish recognizing an object with many possible poses still under consideration... top-down feedback from a parent learning module could help lower-level modules select poses consistent with the larger object."

PRS-CANDIDATE-02:
  Problem: Top-down pose feedback creates a dependency loop: the parent needs child poses to recognize itself, and the children need the parent to settle their poses.
  Resource: Segments "Chicken & Egg Problem Between Learning Modules Discussion" and "Temporal Continuity & Hysteresis."
  Solution: Open; temporal continuity and hysteresis named as candidate stabilizers. Scope initially limited to 2D orientation.
  Confidence: Speculative (chapter titles only)
  Evidence: Chapter list, 40:13-50:30 and 1:02:08.

## Cross-Tradition Signals
- **Friston:** parent-to-child pose constraint is a direct case of top-down priors settling lower-level ambiguity in hierarchical predictive processing. The chicken-and-egg loop is the problem iterative message passing is built to solve; worth asking whether TBP converges on something equivalent.
- **Hawkins internal:** pairs with PROP-2026-11-24-001 (same week, Hawkins's oscillating parent/child inference). Reviewer may want to read the two together.
