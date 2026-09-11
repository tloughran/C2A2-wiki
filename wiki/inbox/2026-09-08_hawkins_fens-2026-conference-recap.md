---
proposal_id: PROP-2026-09-08-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "07/2026 - FENS Conference Recap"
source_url: https://forum.thousandbrains.org/t/07-2026-fens-conference-recap/1174
source_date: 2026-08-06
searched_on: 2026-09-08
status: pending
---

## Summary
A Thousand Brains Project research meeting in which Tristan Slominski reports back from the FENS (Federation of European Neuroscience Societies) 2026 conference, walking the team through recent experimental neuroscience on spatial representation. The headline findings he brings back: a fixed number of grid-like modules emerges regardless of spatial scale; place-cell remapping requires specific identified circuitry; the superior colliculus has cylindrical modules defining an egocentric action-spatial map; spatial salience can be framed as motor readiness; and place cells turn up throughout the neocortex, not only in the hippocampal formation. The session closes with an explicit 12-minute segment asking "Does this apply to Monty?" plus a treatment of the Vector-HaSH model, in which grid-cell/place-cell interaction supports error correction, pattern completion, movement-based prediction, and sequence memory.

## Why This Matters for This Tradition
Hawkins' program stakes its central empirical bet on reference frames implemented by grid-cell-like machinery repeated throughout the neocortex; a conference report finding place cells "everywhere throughout the neocortex" is direct external evidence bearing on that bet. This continues the grid-cell thread the agent has been tracking since PROP-2026-08-17-011/012, but from outside sources rather than internal brainstorming.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The Thousand Brains Theory claims cortical columns use grid-cell-like reference frames, but the theory has needed independent neuroscience showing that hippocampal-formation spatial machinery is in fact generic across cortex rather than special to navigation.
  Resource: FENS 2026 results reported to the team, including the finding that place cells are found throughout the neocortex, and that a fixed number of grid-like modules emerges regardless of the spatial scale being represented.
  Solution: External empirical support for treating reference frames as the cortex-wide organizing principle, and a scale-invariance constraint on how many modules a column-level reference frame needs — a number the theory can now try to predict rather than assume.
  Confidence: Medium
  Evidence: Chapter markers on the main video: 2:12 "Fixed Number of Grid-like Modules Emerge Regardless of Scale"; 44:19 "Place Cells Are Found Everywhere throughout the Neocortex". The forum post's own summary names these as the reported findings. The video was not transcribed; the substance here rests on the official post text and chapter titles, not on quoted speech, and the underlying FENS papers are not named in the post.

PRS-CANDIDATE-02:
  Problem: Monty currently treats sensor movement as exploration policy, without a principled account of what makes one location worth moving to next — the attention/saliency problem the team has been circling since the 2026/06 visual-saliency session.
  Resource: A FENS theory presented as "spatial salience as motor readiness," together with superior-colliculus cylindrical modules defining an egocentric action-spatial map.
  Solution: Saliency reframed as a motor quantity rather than a visual one: what is salient is what the system is prepared to act on. If adopted, this makes Monty's next-move policy a readout of readiness in an egocentric map, and gives the egocentric/allocentric split raised in the open-theory-questions session a concrete neural locus.
  Confidence: Speculative
  Evidence: Chapter markers 29:44 (superior colliculus cylindrical modules / egocentric action-spatial map) and 33:09 ("Spatial Salience as Motor Readiness"). The forum summary names the theory but the post does not state that the team adopted it; the "Does this Apply to Monty?" discussion at 1:37:32 is where that would be settled, and was not transcribed. The reframing in the Solution above is this agent's reading, not a quoted TBP claim — flagged so a reviewer can strike it.

PRS-CANDIDATE-03:
  Problem: A reference frame that is merely a coordinate system does no work; the theory needs a mechanism by which location codes actively correct errors and complete partial patterns.
  Resource: The Vector-HaSH model, in which interactions between grid cells and place cells support error correction, pattern completion, movement-based prediction, and sequence memory.
  Solution: A named, published computational candidate for the grid/place interaction inside a learning module — one that delivers four capabilities Monty needs (error correction, pattern completion, movement-based prediction, sequence memory) from a single mechanism rather than four bolted-on ones.
  Confidence: Medium
  Evidence: The forum post's summary paragraph names Vector-HaSH and lists exactly those four capabilities; chapter marker 49:30 gives it 48 minutes of the meeting, the largest single block. A community reply from user Falco (2026-08-20) corrects the presentation on a detail — that grid-to-place connections are fixed random while the return connections are fixed Hebbian-learned — citing a talk by S. Chandra. That correction stands uncontested in the thread, so the team's in-video account of the connectivity should be treated as provisional.

## Cross-Tradition Signals
- **Friston**: "Spatial salience as motor readiness" is close in shape to active inference's claim that perception and action are the same inferential process — salience as expected information gain under a policy. Whether TBP's motor-readiness framing is the free-energy claim in other words, or a genuinely different account, is a checkable question and a candidate bridge.
- **Levin**: Place cells appearing throughout the neocortex, rather than in a dedicated navigation organ, is the same move Levin makes with cognition — a competence assumed to be specialized turns out to be generic across the substrate.
- **Authorship caveat**: this source is a TBP team meeting led by Tristan Slominski, not Hawkins speaking. It is proposed under the Hawkins tradition on the same basis as PROP-2026-08-26-005 and PROP-2026-08-17-011/012 (official Thousand Brains Project research output). A reviewer who wants the tradition restricted to Hawkins' own voice should reject on that ground and say so, so the standing rule gets fixed rather than re-litigated.
