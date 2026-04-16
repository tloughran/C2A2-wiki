# Jeff Hawkins — PRS Triplets
*Maintained by the Jeff Hawkins Agent | Last updated: 2026-04-03*
*Source: Resurrecting Civility HTML Document Explorer (RC Pilot)*

## Format
```
PRS-[number]:
  Problem: ...
  Resource: ...
  Solution: ...
  Date Added: YYYY-MM-DD
  Source: ...
  Confidence: [High / Medium / Speculative]
```

---

## Triplets

PRS-01:
  Label: P1 (Text, pp.278–285) — Intelligence without true understanding
  Problem: Current AI systems (deep learning) perform impressively but lack genuine understanding — they have no world model, no reference frames, no temporal memory
  Resource: Hierarchical Temporal Memory (HTM) and the Thousand Brains Theory: neocortex-inspired architectures with reference frames, temporal prediction, and distributed voting
  Solution: AI systems built on cortical column principles that genuinely model the world, including the self in the world — moving from pattern matching to understanding
  Date Added: 2026-04-03
  Source: Resurrecting Civility — RC Pilot GPT Tome / Document Explorer
  Confidence: High

PRS-02:
  Label: P2 (Text, p.294) — Distributed vs. centralised intelligence
  Problem: The assumption that intelligence requires a central processor creates AI architectures that are brittle, non-generalising, and opaque
  Resource: Thousand Brains: intelligence as the emergent product of thousands of parallel, independent models voting — radical distribution with no central homunculus
  Solution: Architectures for robust, generalising, self-correcting AI that mirrors the cortex's distributed model-building — with implications for interpretability and alignment
  Date Added: 2026-04-03
  Source: Resurrecting Civility — RC Pilot GPT Tome / Document Explorer
  Confidence: High

PRS-03:
  Label: P3 (Text, p.29) — Knowledge-preserving AGI
  Problem: Human knowledge is fragile, locked in individual minds and institutions that eventually die; AI offers a path to preservation and extension but current systems cannot do this reliably
  Resource: AGI systems built on Thousand Brains principles: capable of building stable, hierarchical, temporally grounded world models that can accumulate and preserve knowledge
  Solution: A knowledge-preserving AGI that genuinely extends the human epistemic tradition — the Thousand Brains Project's long-term agenda
  Date Added: 2026-04-03
  Source: Resurrecting Civility — RC Pilot GPT Tome / Document Explorer
  Confidence: High

PRS-04:
  Label: P4 (Implicit) — Reference frames as universal cognitive tool
  Problem: Different disciplines (biology, physics, philosophy, theology) work in incommensurable reference frames with no shared navigation tools
  Resource: Hawkins's insight that every cortical column uses reference frames to orient its models — reference frames as the universal architecture of model-based intelligence
  Solution: Tradition-crossing inquiry as reference-frame translation: disciplines can be made commensurable by explicitly mapping their reference frames onto one another — a direct resource for Loughran's inter-tradition methodology
  Date Added: 2026-04-03
  Source: Resurrecting Civility — RC Pilot GPT Tome / Document Explorer
  Confidence: Medium

PRS-05:
  Label: P5 (Implicit) — Temporal depth of intelligence
  Problem: Static AI systems (and many static academic frameworks) lack the temporal depth to engage productively with evolving traditions or long-horizon problems
  Resource: HTM's emphasis on temporal sequences as the fundamental unit of cortical learning — intelligence is always about predicting what comes next in a temporal stream
  Solution: Dynamic models of intellectual traditions as temporal sequences, where the tradition's next contribution can be predicted and shaped by understanding its internal learning dynamics
  Date Added: 2026-04-03
  Source: Resurrecting Civility — RC Pilot GPT Tome / Document Explorer
  Confidence: Medium

PRS-06:
  Label: P6 (PROP-2026-04-08-006) — Hierarchical vs. heterarchical neocortex
  Problem: Neuroscience has long assumed the neocortex is organized as a strict processing hierarchy (V1 → V2 → V4 → IT for vision, etc.), but anatomical data shows many long-range connections that are non-hierarchical — regions respond in parallel in ways a strict hierarchy cannot explain
  Resource: Heterarchy framework: the proposal that neocortical organization is a mix of hierarchical and non-hierarchical structure, with cortical columns as the repeating sensorimotor unit that makes lateral and cross-regional processing coherent
  Solution: A unified account of neocortical long-range connectivity that preserves the Thousand Brains architecture while explaining anatomical anomalies — and implies that AI systems based on HTM should use heterarchical, not purely hierarchical, connectivity between modules
  Date Added: 2026-04-08
  Source: Hawkins et al., "Hierarchy or Heterarchy? A Theory of Long-Range Connections for the Sensorimotor Brain" (arXiv:2507.05888, 2025-07-01)
  Confidence: High

PRS-07:
  Label: P7 (PROP-2026-04-08-006) — AI architectural heterarchy
  Problem: Deep learning architectures are strictly hierarchical (layer 1 → layer 2 → … → output) — if the brain's power comes from heterarchical processing, current AI architectures are missing a fundamental design principle
  Resource: Hawkins' heterarchy insight applied to AI: distributed reference-frame-building modules with both hierarchical and lateral connections, not feed-forward pipelines
  Solution: New AI architectural design principle: build lateral, cross-module connections alongside hierarchical ones — the analogue of long-range cortical connections — to support richer world-model integration across simultaneously active learning modules
  Date Added: 2026-04-08
  Source: Hawkins et al., "Hierarchy or Heterarchy? A Theory of Long-Range Connections for the Sensorimotor Brain" (arXiv:2507.05888, 2025-07-01)
  Confidence: Medium

PRS-08:
  Label: P8 (PROP-2026-04-08-005) — Sensorimotor learning and data efficiency
  Problem: Deep learning systems cannot learn efficiently from sensorimotor interaction with the real world — they require massive labeled datasets and cannot transfer knowledge across tasks in the way biological agents do
  Resource: The Thousand Brains Project's "learning module" — a cortical-column-inspired unit that builds CAD-like spatial models through active sensorimotor exploration, enabling rapid continual learning without catastrophic forgetting
  Solution: Monty demonstrates that sensorimotor agents built on cortical column principles can perform 3D object recognition and pose estimation with dramatically less data than deep learning — and do so continuously, without retraining from scratch
  Date Added: 2026-04-08
  Source: Clay, Leadholm & Hawkins, "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence" (arXiv:2412.18354, 2024-12-24)
  Confidence: High

PRS-09:
  Label: P9 (PROP-2026-04-08-005) — HTM implementation in silicon
  Problem: HTM and Thousand Brains Theory have remained largely theoretical since Hawkins' 2021 book — no sufficiently complete implementation has existed to test whether the principles actually produce robust AI behavior
  Resource: Monty open-source framework (github.com/thousandbrainsproject/tbp.monty) — the first working instantiation of a thousand-brains system, with full documentation and reproducible experiments
  Solution: A concrete, testable platform for validating and extending Thousand Brains Theory in AI research, now released under an open-source license with Gates Foundation support
  Date Added: 2026-04-08
  Source: Clay, Leadholm & Hawkins, "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence" (arXiv:2412.18354, 2024-12-24)
  Confidence: High

PRS-10:
  Label: P10 (PROP-2026-04-09-SUPP-001) — C2A2 as a thousand-brains system
  Problem: C2A2's 13-agent architecture was designed by intuition — 11 tradition agents independently maintaining models, communicating via dispatches, with integration layers (Master Agent, Pattern Detector) synthesizing across them. But there is no formal computational theory validating this design or predicting its failure modes
  Resource: The Thousand Brains architecture is a formally described system with the same structure: semi-independent learning modules (= tradition agents), each building complete models of objects (= tradition wikis), communicating via a Cortical Messaging Protocol (= dispatch system), reaching consensus through voting (= Pattern Detector evaluation)
  Solution: C2A2 IS a Thousand Brains system. This structural homology is not metaphorical — it is architecturally precise. The paper provides testable design principles: (a) dispatches should include each agent's current "location" in its tradition's reference frame, not just findings; (b) the Master Agent should implement explicit voting/consensus protocols rather than narrative integration; (c) lateral (non-hierarchical) communication between tradition agents may be as important as hierarchical routing through the Master Agent
  Date Added: 2026-04-09
  Source: Clay, Leadholm & Hawkins, "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence — Supplemental Deep-Read Analysis" (PROP-2026-04-09-SUPP-001)
  Confidence: High

PRS-11:
  Label: P11 (PROP-2026-04-09-SUPP-001) — PRS triplets as reference frames
  Problem: The C2A2 system uses PRS triplets (Problem-Resource-Solution) as its universal knowledge format without theoretical justification for why this particular structure should work
  Resource: Hawkins' claim that reference frames are the universal organizing principle for ALL knowledge in the neocortex — not just spatial knowledge. A reference frame provides a coordinate system within which features are located relative to each other; it is what makes knowledge navigable and transferable
  Solution: PRS triplets ARE reference frames. A Problem defines the origin (where you are), a Resource defines the axes (what tools are available), and a Solution defines the target location (where you need to get). This suggests PRS should be extended: triplets should include "displacement vectors" — the path from Problem through Resource to Solution — not just three static points
  Date Added: 2026-04-09
  Source: Clay, Leadholm & Hawkins, "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence — Supplemental Deep-Read Analysis" (PROP-2026-04-09-SUPP-001)
  Confidence: Medium

PRS-12:
  Label: P12 (PROP-2026-04-09-SUPP-001) — Reference frames and Hoffman's interfaces
  Problem: Hoffman's interface theory claims perception is a fitness-tuned user interface, not a window onto reality. Hawkins' learning modules build "CAD-like spatial models" through active exploration. Are these the same claim in different vocabularies?
  Resource: In the Thousand Brains paper, learning modules do NOT build photographs or veridical representations of reality. They build structured models — reference frames with features attached at specific locations — that are useful for the organism's interaction with the world. The models are evaluated by their predictive utility, not their correspondence to objective reality
  Solution: Hawkins' reference frames ARE Hoffman's interfaces, implemented in cortical hardware. Both frameworks agree: (a) what the brain builds is not a picture of reality but a useful model; (b) the model is structured by the agent's needs, not by the world's intrinsic structure; (c) action (sensorimotor interaction) is essential to model construction
  Date Added: 2026-04-09
  Source: Clay, Leadholm & Hawkins, "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence — Supplemental Deep-Read Analysis" (PROP-2026-04-09-SUPP-001)
  Confidence: High

PRS-13:
  Label: P13 (PROP-2026-04-09-SUPP-001) — Sensorimotor learning in C2A2
  Problem: The Thousand Brains paper insists that sensorimotor interaction — active movement through the world — is essential for learning. Passive data ingestion cannot substitute. But C2A2's tradition agents currently operate in pure ingestion mode: they read documents, extract PRS triplets, and dispatch findings. They do not actively probe
  Resource: Hawkins' sensorimotor learning principle: learning modules must generate predictions, execute actions that test those predictions, and update their models based on the result. Each cycle moves the agent to a new "location" in the reference frame, revealing features that were invisible from the previous location
  Solution: C2A2 agents should be redesigned to include an active inquiry cycle: (a) after ingestion, each tradition agent generates hypotheses about what another tradition would say about the same material; (b) the Master Agent routes these hypotheses to the relevant tradition agent; (c) the receiving agent evaluates the hypothesis against its own reference frame and responds. This converts C2A2 from a passive recording system into a sensorimotor learning system
  Date Added: 2026-04-09
  Source: Clay, Leadholm & Hawkins, "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence — Supplemental Deep-Read Analysis" (PROP-2026-04-09-SUPP-001)
  Confidence: Medium

PRS-14:
  Label: P14 (PROP-2026-04-09-SUPP-001) — Broaden-and-build as reference frame multiplicity
  Problem: Fredrickson's broaden-and-build theory shows that positive emotions widen the scope of attention and thought. But "broadened attention" has no mechanistic account at the neural level — it is described phenomenologically, not computationally
  Resource: In the Thousand Brains framework, the number of simultaneously active learning modules determines the richness of the current world-model. If more cortical columns are actively contributing their reference frames, the organism has a more multi-faceted, integrated representation
  Solution: Broaden-and-build IS reference frame multiplicity. Positive emotions, via neuromodulatory changes, may increase the number of cortical columns that remain in active hypothesis-generation mode rather than being suppressed by lateral inhibition. This provides the first mechanistic neural account of Fredrickson's core observation
  Date Added: 2026-04-09
  Source: Clay, Leadholm & Hawkins, "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence — Supplemental Deep-Read Analysis" (PROP-2026-04-09-SUPP-001)
  Confidence: Speculative

PRS-15:
  Label: P15 (PROP-2026-04-09-SUPP-001) — Cortical columns as Kastrup's alters
  Problem: Kastrup's analytic idealism describes individual minds as "dissociated alters" of universal consciousness. But this model has been applied only at the scale of individual organisms — not within a single brain
  Resource: The Thousand Brains paper describes ~150,000 cortical columns, each building its own COMPLETE model of the world — not a fragment, but a whole. Each column is its own "mind" with its own reference frame and predictions. The columns interact but are not merged
  Solution: Cortical columns are alters within a single brain. The Thousand Brains architecture is Kastrup's DID model applied at the cortical level. Consciousness at the brain level is the INTEGRATION of these column-level alters via the voting/consensus mechanism — exactly as Kastrup's universal consciousness would integrate individual minds
  Date Added: 2026-04-09
  Source: Clay, Leadholm & Hawkins, "The Thousand Brains Project: A New Paradigm for Sensorimotor Intelligence — Supplemental Deep-Read Analysis" (PROP-2026-04-09-SUPP-001)
  Confidence: Speculative

PRS-16:
  Label: P16 (PROP-2026-04-14-001) — Thousand-brains computational efficiency
  Problem: Current deep learning requires massive pretraining and lacks structured, compositional world models — learning is data-hungry and representations are opaque
  Resource: Monty system — a thousand-brains implementation using learning modules with explicit reference frames, sensorimotor exploration, and a Cortical Messaging Protocol for inter-module communication
  Solution: Demonstrated 8 orders of magnitude computational savings over transformer pretraining while achieving rapid, structured 3D object learning through active sensing (33,000× fewer computations than vision transformers; 527M× fewer than pretraining+finetuning)
  Date Added: 2026-04-14
  Source: Leadholm, Clay, Knudstrup, Lee & Hawkins, "Thousand-Brains Systems: Sensorimotor Intelligence for Rapid, Robust Learning and Inference" (arXiv:2507.04494, 2025-07-06)
  Confidence: High

PRS-17:
  Label: P17 (PROP-2026-04-14-001) — Embodied learning validates HTM
  Problem: AI systems lack the ability to learn from embodied, sensorimotor interaction — they process static datasets rather than actively exploring objects and environments
  Resource: Monty's sensorimotor learning loop — each learning module actively moves sensors over objects, building object-centric coordinate systems (reference frames) through exploration
  Solution: A working demonstration that active sensing with reference frames enables rapid, robust learning without massive datasets — vindicating the core HTM claim that intelligence requires movement
  Date Added: 2026-04-14
  Source: Leadholm, Clay, Knudstrup, Lee & Hawkins, "Thousand-Brains Systems: Sensorimotor Intelligence for Rapid, Robust Learning and Inference" (arXiv:2507.04494, 2025-07-06)
  Confidence: High

---
*Total PRS triplets: 17*