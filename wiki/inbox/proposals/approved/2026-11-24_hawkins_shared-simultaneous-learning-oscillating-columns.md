---
proposal_id: PROP-2026-11-24-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/10 - Shared Simultaneous Learning Across Multiple Learning Modules"
source_url: https://forum.thousandbrains.org/t/2026-10-shared-simultaneous-learning-across-multiple-learning-modules/1265
source_date: 2026-11-19
searched_on: 2026-11-24
status: pending
---

## Summary
Recorded TBP research meeting in which Hawkins himself presents (main video https://www.youtube.com/watch?v=zn4MIdwuPHg, ~32 min; summary video https://www.youtube.com/watch?v=kZ6EO7tSyV8). He asks how learning is shared across many learning modules once compositional models extend beyond the current two-region parent/child hierarchy, including what columns with no direct sensory input can learn and how features are shared across sensory modalities. His proposed answer is that every learning module alternates between inferring parent objects and inferring child objects, so no fixed dividing line between "parent" and "child" regions is needed. Niels Leadholm suggests that hippocampal memory consolidation during sleep might coordinate these alternating learning cycles.

**Provenance:** Hawkins is the named presenter (@jhawkins). This passes the "from Hawkins himself" filter directly, unlike most recent TBP forum proposals. Content below comes from the forum post description and chapter list; the video itself was not transcribed.

## Why This Matters for This Tradition
The wiki's compositional-hierarchy entries (PRS-20 and the 2026-10/11 Monty compositional results) all assume a two-level parent/child split between learning modules. This is Hawkins's own statement that the split does not scale, and his first proposed general mechanism for it. It also returns to the hippocampus/cortex fast-vs-slow learning split already in the wiki from the Q4 roadmap (PROP-2026-11-17-004), now offered as possible *evidence* for the theory rather than only as an engineering choice.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Compositional learning works for a two-region parent/child pair, but it is unclear how it scales to many regions, or what columns without direct sensory input learn.
  Resource: Hawkins's proposal that all learning modules switch back and forth between inferring parent objects and inferring child objects, learning feedforward and feedback connections in alternation (chapters "Proposed Solution: All Learning Modules Switch Between Inferring Parent and Child Objects," "Learning Feedback & Feedforward Connections," "No Dividing Line Needed").
  Solution: A role-alternation mechanism that removes the need for a fixed parent/child dividing line and needs no specific prewired connectivity ("Flexibility & No Specific Connectivity Required"), with shared learning itself compositional.
  Confidence: Medium (Hawkins's stated proposal, per the post); Speculative on mechanism detail, which was not verified from the recording
  Evidence: Forum description: "@jhawkins presents a possible solution where cortical columns oscillate between inferring parent objects and child objects."

PRS-CANDIDATE-02:
  Problem: The oscillation proposal needs an empirical anchor and a timing coordinator: when do the columns learn, and what keeps the cycles in step?
  Resource: Leadholm's suggestion that hippocampal memory consolidation during sleep coordinates the cycles; chapters "Where is the Evidence for this Idea? Perhaps in Sleep Memory Consolidation!" and "Fast vs Slow Learning: Hippocampus & Cortex."
  Solution: A candidate testable link: if the theory is right, sleep-consolidation dynamics should show alternating parent/child-style replay between hippocampus and cortex.
  Confidence: Speculative (raised as an idea in discussion, chapter titles only)
  Evidence: Forum description credits @nleadholm with the sleep-consolidation idea.

PRS-CANDIDATE-03:
  Problem: How can representations be learned across different sensory modalities if each column models only its own input?
  Resource: Segment "Feature Sharing Across Sensory Modalities."
  Solution: Open question surfaced; no resolution stated in the post.
  Confidence: Speculative (chapter title only)
  Evidence: Forum description lists cross-modal learning as one of the questions explored.

## Cross-Tradition Signals
- **Friston:** alternation between inferring parents (top-down) and children (bottom-up) is close to the ascending/descending message passing of hierarchical predictive coding. The difference to record: Hawkins alternates *roles over time* within each column, while predictive coding runs both directions at once. Flag against the Hawkins-Friston structural-alignment question; do not merge.
- **Levin:** "no specific connectivity required" and role-switching modules echo Levin's claim that collective cellular agents re-assign roles flexibly without a fixed blueprint. A possible non-neural instance of the same principle.
- **Hoffman:** weak signal only. Columns that infer at one level while hiding the level beneath have a family resemblance to trace logic's visible/hidden partition. Too loose to dispatch on its own.
