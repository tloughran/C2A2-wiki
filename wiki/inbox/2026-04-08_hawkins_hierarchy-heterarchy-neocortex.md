---
proposal_id: PROP-2026-04-08-006
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: paper
source_title: "Hierarchy or Heterarchy? A Theory of Long-Range Connections for the Sensorimotor Brain"
source_url: https://arxiv.org/abs/2507.05888
source_date: 2025-07-01
searched_on: 2026-04-08
status: pending
---

## Summary
A Thousand Brains Project paper co-authored by Hawkins challenges the long-standing hierarchical model of neocortical organization, arguing that many anatomical long-range connections in the brain do not conform to strict hierarchy — regions sometimes respond in parallel rather than sequentially. The paper proposes reframing neocortical architecture as "heterarchical": a system with both hierarchical and non-hierarchical processing, unified by the Thousand Brains principle that every cortical column is its own sensorimotor learning system rather than a node in a feed-forward processing chain.

## Why This Matters for This Tradition
This paper extends and significantly refines Hawkins' core architectural claims. If the neocortex is heterarchical rather than strictly hierarchical, the Thousand Brains model gains even stronger support — each column's autonomy is not just a theory but an anatomical necessity. This has direct implications for how AI architectures based on HTM should be designed.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Neuroscience has long assumed the neocortex is organized as a strict processing hierarchy (V1 → V2 → V4 → IT for vision, etc.), but anatomical data shows many long-range connections that are non-hierarchical — regions respond in parallel in ways a strict hierarchy cannot explain.
  Resource: Heterarchy framework: the proposal that neocortical organization is a mix of hierarchical and non-hierarchical structure, with cortical columns as the repeating sensorimotor unit that makes lateral and cross-regional processing coherent.
  Solution: A unified account of neocortical long-range connectivity that preserves the Thousand Brains architecture while explaining anatomical anomalies — and implies that AI systems based on HTM should use heterarchical, not purely hierarchical, connectivity between modules.
  Confidence: High
  Evidence: Paper documents specific anatomical connections inconsistent with hierarchical models; proposes heterarchy as organizing principle.

PRS-CANDIDATE-02:
  Problem: Deep learning architectures are strictly hierarchical (layer 1 → layer 2 → … → output) — if the brain's power comes from heterarchical processing, current AI architectures are missing a fundamental design principle.
  Resource: Hawkins' heterarchy insight applied to AI: distributed reference-frame-building modules with both hierarchical and lateral connections, not feed-forward pipelines.
  Solution: New AI architectural design principle: build lateral, cross-module connections alongside hierarchical ones — the analogue of long-range cortical connections — to support richer world-model integration across simultaneously active learning modules.
  Confidence: Medium
  Evidence: Implied by paper's anatomical argument; not yet demonstrated in silicon.

## Cross-Tradition Signals
**Friston**: Hierarchical predictive processing (Friston's core model) may need revision if the neocortex is heterarchical — both hierarchical and lateral predictions may occur simultaneously. Flag for Friston Agent: does free energy minimization work heterarchically, or does FEP assume strict hierarchy?
**McGilchrist**: McGilchrist's hemispheric model proposes that the right hemisphere holds a broader, more integrated view while the left processes narrowly — this may map onto the heterarchy/hierarchy distinction. Flag for McGilchrist Agent.
**Levin**: Heterarchy at the neural level mirrors Levin's observation that biological cognition is not top-down hierarchical — goal-directedness emerges from lateral interactions among semi-autonomous agents at every scale.
