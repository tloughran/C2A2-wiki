---
proposal_id: PROP-2026-10-23-006
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "08/2026 - Recent Changes to Monty's Cortical Message Protocol and Reference Frames"
source_url: https://forum.thousandbrains.org/t/08-2026-recent-changes-to-monty-s-cortical-message-protocol-and-reference-frames/1228
source_date: 2026-10-22
searched_on: 2026-10-23
status: pending
---

## Summary
Ramy Mounir of the Thousand Brains Project presents two architectural changes to Monty (main video: https://www.youtube.com/watch?v=sRH_kqK0IqY, ~1h10m; summary video: https://www.youtube.com/watch?v=4g_TJg-kNAw). First, the Cortical Messaging Protocol (CMP, the message format learning modules use to talk to each other) now carries sensory *features* and *location/movement* separately, so a learning module can update its location alone, which is path integration (tracking where you are from your own movements). Second, a simplified reference-frame buffer places incoming features in one shared reference frame. Object-part relationships travel up the hierarchy as "hierarchical bindings" instead of as multiple coordinate systems. The talk then discusses how to keep higher-level object models from becoming too dense (feature-change filters, voxel averaging, event-driven thresholds).

**Verification gap / provenance:** this agent read the forum announcement and chapter list, not the video. Mounir presents. Hawkins' participation in the discussion is unconfirmed. This is TBP-team work and fails the strict "from Hawkins himself" filter. It is proposed on the same basis as earlier TBP research-meeting items. The reviewer may deny on that ground.

## Why This Matters for This Tradition
Separating "what" (features) from "where" (location) mirrors a classic distinction in neuroscience and in Hawkins' own column model, where grid-cell-like location signals and sensory input arrive by different routes. It also makes P19 (thalamus as a reference-frame transformer) and P20 (composition through hierarchy) concrete as engineering.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: When features and locations travel bundled in one message, a learning module cannot keep track of where it is during movements that bring no new sensory feature.
  Resource: A decoupled CMP in which location/movement messages and feature messages are sent and processed independently.
  Solution: Learning modules can do location-only updates for path integration and spatial tracking, which is closer to how location is thought to be maintained in cortex.
  Confidence: High that the change was made, since the announcement states it as implemented ("Code Changes" chapter at 27:28).
  Evidence: Forum summary; chapters "Features and Locations in CMP Messages are Now Decoupled" (3:03) and "Discussion on Path Integration in Monty and the Brain" (5:27).

PRS-CANDIDATE-02:
  Problem: Learning modules that receive 2D data and those that receive 3D data need compatible reference frames. Passing several coordinate systems up the hierarchy is complex and brittle.
  Resource: A single shared reference frame in a simplified buffer, with parent-child object relations sent as hierarchical bindings.
  Solution: The announcement says a single reference frame "solves the 2D vs 3D reference frame problem".
  Confidence: Medium. This is the team's claim, not yet evaluated in this source.
  Evidence: Chapters "2D vs 3D Reference Frame Problem" (11:50) and "A Single Reference Frame Solves the 2D vs 3D Reference Frame Problem" (24:47).

PRS-CANDIDATE-03:
  Problem: As the hierarchy gets deeper, higher-level object models can fill with redundant points. Is lower resolution at higher levels a requirement or just a convenience?
  Resource: Proposals for feature-change filtering, voxel averaging, time/event-driven thresholds, and moving the "percept filter" to the receiving learning module, discussed against biological constraints such as connection pruning and propagation delay.
  Solution: None yet. These are listed as future work. The session links coarser higher-level models to generalisation.
  Confidence: Speculative.
  Evidence: Chapters from 28:41 to 1:10:32 ("Generalization Through Coarser Models", "Proposal: Move the Percept Filter to the Receiving LM", "Propagation Delay").

## Cross-Tradition Signals
- **Friston:** Separating "where" from "what" and filtering messages by salience and prediction error ("Salience and Prediction Error", 39:29) parallels precision-weighting in predictive coding, where only informative errors are passed on.
- **Hoffman:** A single shared reference frame that is built, not given, fits the interface claim that spatial structure is a format the perceiver constructs, not a copy of the world.
- **Carroll / Arkani-Hamed:** Coarser models at higher levels that generalise better resemble coarse-graining and effective theories in physics.
- **C2A2 internal:** The decoupling suggests a design note for the dispatch layer: send "where in the discourse" (context/position) separately from "what was claimed" (content).
