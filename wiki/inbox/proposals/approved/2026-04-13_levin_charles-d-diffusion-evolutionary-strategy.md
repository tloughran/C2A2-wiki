---
proposal_id: PROP-2026-04-13-002
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Heuristically Adaptive Diffusion-Model Evolutionary Strategy"
source_url: https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202511537
source_date: 2026-02-01
searched_on: 2026-04-13
status: pending
---

## Summary
Hartl, Zhang, Hazan, and Levin introduce CHARLES-D (Conditional, Heuristically-Adaptive Regularized Evolutionary Strategy through Diffusion), a framework that integrates deep learning diffusion models with evolutionary algorithms. The key insight: diffusion models and evolutionary algorithms share a core generative principle — iterative refinement of random initial distributions to produce high-quality solutions. By using diffusion models to generate offspring parameters in an evolutionary process, the method achieves efficient convergence toward high-fitness solutions while preserving explorative diversity. Crucially, diffusion models introduce "deep memory" into evolution — retaining historical information across generations and leveraging subtle data correlations, elevating evolutionary algorithms from shallow heuristics to frameworks with deep memory.

## Why This Matters for This Tradition
This paper extends Levin's research program into computational evolution and AI, connecting his biological work on morphogenesis to artificial optimization. The central theme — that evolution can be enhanced by giving it memory and generative modeling capacity — directly parallels Levin's biological thesis that cells are not blind Darwinian actors but goal-directed agents with memory (bioelectric memory encoding anatomical targets). CHARLES-D is, in effect, the computational analogue of Levin's biological claim: evolution works better when it can remember and predict, not just mutate and select.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Evolutionary algorithms are powerful optimizers but lack memory — each generation starts fresh, losing subtle correlations and historical information that could accelerate convergence
  Resource: CHARLES-D — a framework integrating diffusion models (which retain learned data distributions) with evolutionary algorithms, giving evolution "deep memory" across generations
  Solution: Evolutionary optimization with memory and conditional generation achieves faster convergence to high-fitness solutions while maintaining diversity, demonstrated across diverse optimization domains
  Confidence: High
  Evidence: Published in Advanced Science (2026); benchmark results across multiple domains

## Cross-Tradition Signals
**Friston (moderate):** CHARLES-D's use of generative models to guide evolutionary search is structurally analogous to active inference — both use generative models to reduce surprise/prediction error and guide action/selection. The connection between evolutionary optimization and FEP-style inference is worth flagging for the Friston agent.

**Wolfram (moderate):** The claim that diffusion and evolution share a core generative principle resonates with Wolfram's computational equivalence thesis — both processes may be instances of the same underlying computational substrate performing iterative refinement.

**C2A2 (direct):** If AI agents in the tradition-accelerator network need to evolve their knowledge structures over time, CHARLES-D-style memory-augmented evolution could provide a mechanism for tradition-level learning — agents that remember what worked across generations of inquiry.
