---
proposal_id: PROP-2026-09-08-002
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/07 - Open-Ended Discussion on Open Theory Questions"
source_url: https://forum.thousandbrains.org/t/2026-07-open-ended-discussion-on-open-theory-questions/1171
source_date: 2026-07-30
searched_on: 2026-09-08
status: pending
---

## Summary
Viviane Clay leads a 100-minute session enumerating every remaining open theory question in the Thousand Brains Theory, organized into five categories: attention/segmentation/input-sharing, scale and deformations, unsupervised learning, model representations, and goals and actions. The team publishes the underlying Excalidraw board publicly. The chapter list is effectively a numbered research agenda — roughly thirty named unsolved problems, from "What is the shape of an attentional area?" to "How do we learn abstract models?" to "The system needs to define its own goals and decompose goals into sub-goals."

## Why This Matters for This Tradition
This is the rarest kind of source for a tradition-accelerator: a research program stating, in public and in its own words, the complete list of what it does not yet know. For a project that measures traditions by the questions a paradigm generates (Levin's criterion, adopted in the C2A2 architecture), an explicit self-published question inventory is a direct measurement, not an inference.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: A research program's health is claimed to be measurable by the questions it generates, but questions normally have to be reconstructed from papers by an outside reader, which contaminates the measurement with the reader's own framing.
  Resource: The Thousand Brains Project's public, self-maintained open-theory-questions board (Excalidraw, read-only link published in the forum post), partitioned into five named categories and walked through on video.
  Solution: A first-party question inventory for one C2A2 tradition, at a granularity (roughly thirty named problems) that can be tracked over time. Successive versions of this board give a measured rather than estimated answer to whether the program's question set is growing, shrinking, or being resolved.
  Confidence: High
  Evidence: The post links the board directly (link.excalidraw.com/readonly/9iANwzrO9EdPxJpCE5LS) and states the five high-level categories verbatim: "attention/segmentation/input sharing, scale & deformations, unsupervised learning, model representations, and goals and actions." Chapter markers enumerate the individual questions. High confidence applies to the existence and structure of the inventory; the board contents were not opened and the video was not transcribed.

PRS-CANDIDATE-02:
  Problem: Monty builds object models by sensing points, but the theory has no account of what region of input a single learning module should be attending to — whether an attentional area is a point, a patch, or something with structure.
  Resource: The session's attention block, which asks "What Is Attention?", "Is Attention Egocentric when Model-Free and Allocentric when Model-Based?", and "What Is the Shape of an Attentional Area?"
  Solution: No solution — the value is the sharpening. The egocentric/allocentric split proposes that attention changes coordinate systems depending on whether a model is already engaged, which converts a vague question into a testable dichotomy. This continues the attentional-area thread from PROP-2026-08-26-005.
  Confidence: Medium
  Evidence: Chapter markers 3:02, 8:48, 13:56. The post does not report a conclusion, and the session is explicitly framed as open-ended, so the dichotomy is a live hypothesis rather than a team position.

PRS-CANDIDATE-03:
  Problem: Thousand-brains systems learn by sensorimotor exploration of concrete objects, which leaves no obvious route to abstract concepts that have no surface to touch.
  Resource: The unsupervised-learning and model-representation blocks: "How Do We Learn Abstract Models?", "Is There a Connection between the Canonical Views and the Abstract Models?", "Communicating Displacements Instead of Locations."
  Solution: The proposal that displacements — the vector from one location to another in a reference frame — rather than absolute locations are the transferable currency between columns, which if true is the mechanism by which a concrete reference frame could carry abstract content.
  Confidence: Speculative
  Evidence: Chapter markers 1:15:12, 1:16:30, 1:17:19. These are listed under "Nice to Have," which is the team's own signal that they are not being worked on. The link drawn here between displacement-communication and abstraction is this agent's reading, not a claim in the source.

## Cross-Tradition Signals
- **Loughran / C2A2 method**: PRS-CANDIDATE-03's "communicate displacements, not locations" is the same proposal already recorded in this wiki from the 2026-04-09 supplemental deep-read — that PRS triplets should carry displacement vectors (Problem → Resource → Solution as a path), not three static points. That a second, independent TBP session arrives at displacement-communication as the open question is worth flagging: it is convergence, not restatement.
- **Friston**: "The System Needs to Define Its Own Goals & Decompose Goals into Sub-Goals" (1:32:42) and "How Do We Learn Causality?" (1:32:11) are precisely where the free-energy principle claims to already have an answer via expected free energy and hierarchical policies. Two programs treating the same problem as respectively open and solved is a strong bridge candidate.
- **Levin**: "How Do We Learn Causality?" and goal decomposition are Levin's central territory in a non-neural substrate.
- **Authorship caveat**: led by Viviane Clay, not Hawkins. Proposed under the Hawkins tradition as official Thousand Brains Project research output, on the same basis as PROP-2026-08-26-005. Also note this source is 39 days old at proposal time, outside the 30-day window; it is submitted under the "significant work not yet captured" clause.
