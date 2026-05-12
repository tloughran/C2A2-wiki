---
proposal_id: PROP-2026-04-20-003
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "BraiNCA: brain-inspired neural cellular automata and applications to morphogenesis and motor control"
source_url: https://arxiv.org/abs/2604.01932
source_date: 2026-04
searched_on: 2026-04-20
status: pending
---

## Summary
Preprint co-authored by Léo Pio-Lopez, Johannes Hartl, and Michael Levin introducing BraiNCA — a brain-inspired extension of Neural Cellular Automata (NCA). Standard NCAs model collective behavior via purely local cell-to-cell updates; BraiNCA augments this with (a) an attention mechanism that lets cells route information selectively, (b) long-range "hub" connections that break the strict locality of classical NCAs, and (c) cortical-style modularity with differentiated specialist regions. The authors demonstrate BraiNCA on morphogenetic target-pattern problems and on motor control tasks, arguing that biologically realistic cognition at the cell-collective scale requires exactly these brain-like architectural features: selective attention, non-local communication pathways, and functional modularity.

## Why This Matters for This Tradition
This is a formal architectural claim about *what kind of computational substrate* Levin's collective intelligence requires. Prior Levin NCA / xenobot work has emphasized that purely local rules suffice to generate rich morphogenetic behavior; BraiNCA is a self-correction/extension arguing that richer cognition — goal-direction, control, decision-making in cell collectives — requires non-local structure analogous to cortical architecture. This directly sharpens the Levin program's claim that "bioelectricity does exactly what it does in the brain" (PROP-2026-04-20-001) by providing a *computational model* of why brain-like features (attention, hubs, modularity) are necessary for the cognitive glue, not just helpful.

Also relevant to open research questions about the computational substrate of basal cognition and whether the same architectural principles scale from single cells to tissues to brains.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Classical Neural Cellular Automata model morphogenesis with purely local update rules, but cannot account for the goal-directed, coordinated behavior observed in real cell collectives — especially behavior requiring selective information routing across tissue
  Resource: BraiNCA — Neural Cellular Automata augmented with attention mechanisms, long-range hub connections, and cortical-style modular regions, inspired by brain architecture
  Solution: A computational substrate demonstrating that biologically realistic collective cognition requires brain-like features (attention, non-locality, modularity); successfully applied to morphogenetic target-pattern problems and motor control, providing a formal model of why the same architectural principles operate at cellular and neural scales
  Confidence: Medium-High
  Evidence: Preprint arXiv:2604.01932 (Pio-Lopez, Hartl, Levin, April 2026) — demonstrates BraiNCA on both morphogenesis and motor control benchmarks

## Cross-Tradition Signals
- **Levin × Hawkins:** Cortical modularity and columnar organization inside BraiNCA directly echoes Hawkins' hierarchical temporal memory / thousand brains theory — potential for a formal bridge: Hawkins' cortical algorithm as the same pattern operating in neural tissue that BraiNCA shows operating in generic cell collectives. Strong candidate for Pattern Detector review.
- **Levin × Friston:** BraiNCA's attention + long-range hubs give concrete computational realization for where active inference can run in tissue — deepens FINDING-007 (Friston × Levin bridge, morphogenetic active inference, Friston PRS-08). The flat/local FEP substrate is replaced by a richer architecture that looks more like a variational message-passing graph.
- **Levin × Wolfram:** BraiNCA continues Wolfram-style computational-substrate-for-cognition thinking, but argues against minimal-local-rule purism — cognitively adequate computations require architectural structure beyond local update rules. Potential tension worth Pattern Detector evaluation.
- **Levin × Hoffman:** Attention + hubs + modularity align with trace-logic agent-of-agents composition (FINDING-011, FINDING-012) — BraiNCA architecture could be read as a trace-logic agent whose sub-agents communicate through attention-gated hubs.
