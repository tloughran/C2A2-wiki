---
proposal_id: PROP-2026-05-05-002
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Bootstrapping Life-Inspired Machine Intelligence: The Biological Route from Chemistry to Cognition and Creativity"
source_url: https://arxiv.org/abs/2602.08079
source_date: 2026-02-08
searched_on: 2026-05-05
status: pending
---

## Summary
Pezzulo & Levin (arXiv 2602.08079, February 2026) propose a "genuinely life-inspired" approach to machine intelligence, distilling five design principles drawn from biology that they argue underlie life's capacity for robust, autonomous, and open-ended problem-solving: (1) multiscale autonomy, (2) growth through self-assemblage of active components, (3) continuous reconstruction of capabilities, (4) exploitation of physical and embodied constraints, and (5) pervasive signaling enabling self-organization and top-down goal control. The paper is explicitly an alternative to scaling-and-tokens approaches to AGI, arguing that creativity and open-endedness require bootstrapping intelligence the way biology does — from chemistry upward, with goal-directedness preserved at each level.

## Why This Matters for This Tradition
This is the most synthetic statement to date of how Levin's program (joined with Pezzulo's active-inference robotics work) translates into a constructive AI design philosophy. It deserves capture as significant work not yet in the wiki — even though it predates the strict 30-day window — because it directly extends PRS-05 (AI alignment via biology) and PRS-15 (Neurobots) into a five-principle constructive program for machine intelligence. It is the explicit bridge document between the basal-cognition empirical literature and the AI-architecture community.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Current AI architectures (transformer-based foundation models, RL agents) achieve high performance on narrow tasks but lack the open-ended creativity, robustness, and multi-scale autonomy characteristic of biological intelligence. Scaling alone has not produced these properties; the field lacks a constructive design philosophy for them.
  Resource: A five-principle design framework distilled from biology — multiscale autonomy, self-assemblage growth, capability reconstruction, physical/embodied constraints, and pervasive signaling — formalized into a "bootstrapping" recipe from chemistry to cognition.
  Solution: A constructive program for life-inspired machine intelligence that does not depend on scaling token prediction. AI systems built bottom-up from these principles inherit biology's capacity for creative problem-solving, robustness, and goal-preservation across scales — providing concrete engineering targets for the alignment-friendly properties Levin's program identifies.
  Confidence: High
  Evidence: The paper explicitly distills the five principles, grounds each in Levin-program empirical results (xenobots, bioelectric reprogramming, multi-scale agency), and contrasts the resulting design philosophy with current dominant AI paradigms.

PRS-CANDIDATE-02:
  Problem: The relation between Levin's empirical biology and the AI architecture community has been suggestive but not constructive — biology has been used as analogy and inspiration but not as a design specification.
  Resource: The "bootstrapping" frame — explicit translation of Levin/Pezzulo biological principles into recipes a machine-intelligence engineer could implement, with concrete targets at each level of abstraction (chemistry → cells → tissues → organisms → cognition).
  Solution: A translation layer between Levin's empirical program and AI architecture, specifying what each principle delivers (e.g., multiscale autonomy as a guard against single-point-of-failure misalignment) and how to test for it in synthetic systems.
  Confidence: High
  Evidence: The paper functions as a design document — each principle is paired with biological exemplars and engineering implications, making it a direct output of the Levin program for the AI community.

## Cross-Tradition Signals
- **Friston (strong):** Pezzulo is co-author and brings active-inference framing; the five principles align with Friston-style generative-model architectures (multiscale autonomy ≈ hierarchical Markov blankets; pervasive signaling ≈ precision-weighted message passing). This paper functions as a concrete instance of the Friston × Levin alignment already flagged in FINDING-001/002. Strong CROSS candidate.
- **Hawkins (medium):** "Self-assemblage growth" and "multiscale autonomy" map directly to Hawkins' cortical-column architecture and the Thousand Brains theory. The five principles read as a biological-substrate-agnostic generalization of Hawkins' design rules.
- **Wolfram (medium):** "Pervasive signaling enabling self-organization" maps to Wolfram's substrate of pervasive computation. Joint formulation: the five principles characterize the regime of the ruliad where life-like computation occurs.
- **Kastrup (speculative):** A bootstrapping route from chemistry to cognition that preserves goal-directedness at each level is consistent with — though does not require — an idealist substrate. Worth flagging as a potential point of constructive disagreement: does goal-directedness emerge or is it primary?
- **Loughran/C2A2 (high relevance):** The five principles are candidate criteria for evaluating whether C2A2 Wiki Agents themselves are aligned with the program's goals — multiscale autonomy maps to the agent-and-master architecture; pervasive signaling maps to the dispatch system. Worth using as a self-evaluation framework for the network.
