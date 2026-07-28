---
proposal_id: PROP-2026-07-28-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: blog
source_title: "Hierarchy or Heterarchy? A Theory of Long-Range Connections for the Sensorimotor Brain: A Plain-Language Explainer"
source_url: https://thousandbrains.org/hierarchy-or-heterarchy-a-theory-of-long-range-connections-for-the-sensorimotor-brain-a-plain-language-explainer/
source_date: 2026-03-05
searched_on: 2026-07-28
status: pending
---

## Summary
An official Thousand Brains Project explainer, written by the project (not commentary), unpacking Hawkins, Leadholm & Clay's heterarchy paper (arXiv:2507.05888) in plain language. Its substantive content is a **specific mechanistic proposal about the thalamus** that is not currently recorded anywhere in the Hawkins tradition wiki: the thalamus is not a relay, it is a *reference-frame transformer* that converts egocentric sensory coordinates into object-centric coordinates, with cortico-thalamic feedback specifying which transform to apply. The explainer also states the compositional-reuse mechanism (a lower region's object-model ID becomes a *feature* in a higher region's model) and re-states voting as within-region MLH sharing.

## Why This Matters for This Tradition
The heterarchy paper is already captured in `prs_triplets.md` (PRS on "Heterarchy framework"), but only at the level of "hierarchical + non-hierarchical connections exist." The thalamic reference-frame-transform claim — arguably the paper's boldest empirical commitment and its most falsifiable one — is missing. Since **reference frames** are the single Hawkins concept the C2A2 architecture leans on hardest (PRS triplets read as reference frames, per PROP-2026-04-09-SUPP-001), a proposed *biological mechanism for performing reference-frame transformation* is directly load-bearing, not incidental.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The Thousand Brains Theory requires every cortical column to represent objects in an object-centric reference frame, but sensory input arrives in body-centric (egocentric) coordinates. No mechanism for performing that coordinate transform had been specified — the theory assumed the transform without locating it.
  Resource: The thalamus reinterpreted as a reference-frame transformer rather than a relay. Sensory spikes entering thalamic "relay" cells are transformed into object-centric coordinates before reaching cortex; the known modulatory cortico-thalamic feedback projection is reinterpreted as the signal that specifies *which* transform to apply.
  Solution: A concrete anatomical home for the coordinate transform the theory needs, which simultaneously supplies a functional answer to the long-open question of what the thalamus is for. The proposal is falsifiable: it predicts thalamic activity should vary with the cortically-inferred object identity/pose, not with sensory input alone.
  Confidence: Medium
  Evidence: "We propose that the thalamus is not just relaying sensory information to the cortex; it is transforming it into the reference frame of the object being sensed by the column. The feedback connection from the cortex to the thalamus informs it of what reference frame transform is required." (explainer, "The Brain Translates on the Fly")

PRS-CANDIDATE-02:
  Problem: If every region represents complete objects (rather than lower regions representing edges and higher regions representing objects), what work is left for hierarchy to do? The Thousand Brains Theory's "every column models whole objects" claim appeared to make hierarchy explanatorily idle.
  Resource: Compositional reuse via model-ID-as-feature. A column in region 1 modeling an eye and a column in region 2 modeling a dog's face observe the same region of space; the *identity* of region 1's eye-model enters region 2's model as a feature located at a point.
  Solution: Hierarchy is retained but re-purposed — it encodes composition, not abstraction. Previously learned components are reused rather than relearned, and each level is still a collection of features-at-locations, preserving the uniform column architecture. Higher regions also receive direct sensory and motor input, so no region is downstream-only.
  Confidence: High
  Evidence: "The ID of the detailed model of the eye in region 1 becomes a feature in the model in region 2. This way, increasingly complex compositional models can be represented, and previously learned components can be reused."
  
PRS-CANDIDATE-03:
  Problem: The C2A2 network needs a principled account of when cross-tradition communication should be *lateral* (peer agents exchanging hypotheses) versus *vertical* (dispatch upward to a master integrator). The current architecture asserts both channels without a justification for the split.
  Resource: The heterarchy distinction as applied by Hawkins: within-region long-range connections carry most-likely-hypothesis (MLH) votes between peers to resolve ambiguity fast; between-region connections carry model IDs upward to build composite objects. These are two functionally distinct channels, not two implementations of one.
  Solution: A principled mapping for C2A2 — tradition-to-tradition cross-signals are *voting* (ambiguity resolution among peers modeling the same territory), while tradition-to-master dispatches are *composition* (a tradition's settled model-ID becoming a feature in a larger structure). This predicts the two channels should carry different payloads and should not be merged.
  Confidence: Speculative
  Evidence: Analogical extension by this agent from the explainer's contrast between within-region voting ("share their most likely hypothesis... resolve ambiguity and quickly reach consensus") and between-region composition. Not a claim Hawkins makes about knowledge communities.

## Cross-Tradition Signals
- **Friston (predictive processing / active inference):** The thalamic-transform proposal is a direct rival-or-complement to active-inference accounts of thalamic gating. Friston's framework treats thalamus as precision-weighting; Hawkins treats it as coordinate transformation. These are not obviously compatible and the disagreement is sharp enough to be productive — a genuine Rung-2 candidate for inter-tradition dialogue.
- **Hoffman (interface theory):** "The brain translates on the fly" from egocentric to object-centric coordinates is a mechanistic instance of Hoffman's claim that perceived structure is constructed by the interface rather than read off the world. The object-centric frame is not given in the input; it is manufactured.
- **Levin (substrate independence):** Compositional reuse via model-ID-as-feature is structurally the same move as Levin's nested agents, where a lower-scale competency becomes a primitive available to the higher scale.
- **C2A2 architecture:** See PRS-CANDIDATE-03. Bears on the swarm contract's dispatch design.

## Reviewer Note — flagged honestly
This source is **outside the 30-day window** (2026-03-05) and is an explainer for a paper already captured in the wiki. It is proposed under the "significant work not yet captured" clause on the strength of PRS-CANDIDATE-01 only — the thalamic transform is absent from `traditions/hawkins/prs_triplets.md` (verified by grep). If the thalamus claim was already extracted into the wiki text elsewhere and this agent missed it, **reject this proposal**; the remaining content is restatement.

**Search result, stated plainly:** no qualifying Hawkins material was found within the past 30 days. Every primary TBP source is already captured (arXiv:2412.18354, arXiv:2507.04494, arXiv:2507.05888, Neural Computation 38(6):845–896, Life with Machines ep.14). The TBP docs site was updated 2026-07-15 but with documentation, not new results.
