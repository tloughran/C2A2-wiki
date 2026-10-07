---
proposal_id: PROP-2026-10-06-003
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/08 - Rome Focus Week Final Presentations"
source_url: https://www.youtube.com/watch?v=QsTJY-83EUg (discussion: https://forum.thousandbrains.org/t/2026-08-rome-focus-week-final-presentations/1215)
source_date: 2026-09-29 (forum post date per forum page; event August 2026)
searched_on: 2026-10-06
status: pending
---

## Summary
Final presentations of three teams from the Thousand Brains Project Rome Focus Week. Team Mighty Mouse integrated Monty with ARC-AGI-3 through a game-engine API for custom tasks, built an ARC-AGI simulator and a sensor module that detects environmental changes, and demonstrated learning of compositional game maps and sprites. Team Fate Attenzione built the attention prototype (see PROP-2026-10-06-002) with model-free and model-based attention, percept filtering, soft attention, salience detection and dynamic voxel sizing. Team Janus implemented object merging and splitting in Monty, plus a web-based GUI visualization tool, validated through sensorimotor exploration and model ablations. A forum commenter singled out the attention system and the GUI, and said merge/split addresses object-identity persistence.

**Provenance caveats:** Only the forum summary was read, and the video was not watched. No quantitative results (such as ARC-AGI-3 scores) were visible. The video URL is taken from the forum page. Today's PROP-2026-10-06-001 covers the pre-event proposals for the same week. This proposal concerns the delivered results and the team-level detail, so there is partial overlap on the headline outcomes. Consider approving only the Janus triplet if the attention triplet is taken from -002.

## Why This Matters for This Tradition
It records what the program built, not what it proposed. Merge/split bears directly on the compositional-model questions in the wiki (PRS-20, Q8: what happens when a lower model is revised). ARC-AGI-3 integration makes the gap analysis (PROP-2026-09-01-001) measurable.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Monty's per-object models could not be combined into wholes or split into reusable parts, so object identity could not persist as models were revised (wiki Q8: re-binding when a lower model changes).
  Resource: Object merging and splitting in Monty (Team Janus), with a web GUI for inspecting models, tested by sensorimotor exploration and model ablations.
  Solution: Models can be merged when two are found to be the same object and split into reusable parts. This is a mechanism candidate for compositional reuse and for re-binding, not yet shown to resolve Q8.
  Confidence: Medium
  Evidence: Forum summary: "object merging and splitting abilities in Monty... web-based GUI visualization tool... sensorimotor exploration and model ablations for experimental validation."

PRS-CANDIDATE-02:
  Problem: Monty could not be evaluated on abstract, interactive reasoning benchmarks, so claims about sensorimotor-first reasoning stayed untested.
  Resource: ARC-AGI-3 integration via a game-engine API, an ARC-AGI simulator, and a sensor module for environment changes (Team Mighty Mouse).
  Solution: A test bed for compositional learning of game maps and sprites. No performance numbers were reported in what was readable.
  Confidence: Speculative
  Evidence: Forum summary: "ARC-AGI-3 integration with a game engine API... learning compositional game maps and sprites."

## Cross-Tradition Signals
- **Wolfram:** Merge/split of object models resembles identifying equivalent states in a multiway system. This is speculative.
- **Levin:** Merging and splitting of models resembles the merging and splitting of cognitive light-cones in collective agents. This is an analogy only.
- **Friston:** Model merging is structure learning, and the same question applies as for the thalamus (derive versus accommodate; wiki Q13).
- **C2A2 architecture:** Merge/split is relevant to how tradition wikis are consolidated or divided. The wiki's own caution (Q11) applies: do not treat this as something Hawkins says about knowledge communities.
