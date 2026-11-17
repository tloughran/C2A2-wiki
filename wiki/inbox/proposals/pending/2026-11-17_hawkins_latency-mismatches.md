---
proposal_id: PROP-2026-11-17-002
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/09 - Latency Mismatches"
source_url: https://forum.thousandbrains.org/t/2026-09-latency-mismatches/1240
source_date: 2026-11-03
searched_on: 2026-11-17
status: pending
---

## Summary
Recorded TBP research meeting (presenter: sknudstrup) on a timing problem in Monty's hierarchy: object information reaches a higher learning module after the sensor has already moved, so features get stored at the wrong locations. Three fixes are on the table: configurable delays between learning modules, an inner loop letting modules exchange information before the next observation, and efference copies. Choosing among them is the stated open item.

**Provenance caveat:** TBP team meeting implementing Hawkins' theory; Hawkins is not a listed presenter. Same provenance class as earlier approved TBP forum proposals.

## Why This Matters for This Tradition
This gives content to the Q4 roadmap item "Inner LM Loop to Address Temporal Mismatches," which the wiki currently holds as Speculative (chapter title only, PROP-2026-10-23-003). It is also a real-world constraint on compositional hierarchy (PRS-20): composition across levels only works if levels agree on *when* and *where* a feature was sensed.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: In a hierarchy of learning modules, higher-level information arrives after the sensor has moved, so features are bound to the wrong locations.
  Resource: Three candidate mechanisms — inter-module delays, an inner exchange loop before the next observation, and efference copies of motor commands
  Solution: Problem identified and characterised; mechanisms proposed but not yet chosen
  Confidence: Medium (problem); Speculative (which fix)
  Evidence: Page summary lists all three fixes and names prioritisation as open.

## Cross-Tradition Signals
- Friston: efference copy is a central construct in active inference (predicting the sensory consequences of one's own action). If TBP adopts the efference-copy route, that is a concrete convergence point to record against Hawkins Question 6 — flag, don't merge.
- Upgrades the existing Speculative "inner LM loop" resource; reviewer may prefer to fold this into that entry rather than add a new triplet.
