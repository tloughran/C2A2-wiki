---
proposal_id: PROP-2026-04-13-005
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "A survey on neuro-mimetic deep learning via predictive coding"
source_url: https://www.sciencedirect.com/science/article/pii/S089360802501041X
source_date: 2026-03-01
searched_on: 2026-04-13
status: pending
---

## Summary
Salvatori, Mali, Buckley, Lukasiewicz, Rao, Friston, and Ororbia provide a comprehensive survey of predictive coding as a framework for neuro-mimetic deep learning. The paper reviews how predictive coding — originally a neuroscience theory — has been translated into practical deep learning architectures. Key findings: predictive coding networks can model information processing across different brain areas, function in control and robotics settings, have solid mathematical foundations in variational inference (Friston's FEP), and perform computations asynchronously — a property that conventional backpropagation-based deep learning lacks. Published in Neural Networks, March 2026.

## Why This Matters for This Tradition
This survey consolidates the state of predictive coding as a bridge between Friston's theoretical neuroscience and practical AI. It demonstrates that FEP-grounded predictive coding is not merely a theory of the brain but a viable alternative computational paradigm for artificial intelligence. The asynchronous computation property is particularly significant: biological neural networks compute asynchronously, and predictive coding networks replicate this, making them more biologically plausible than standard deep learning. This advances Friston's program by showing that FEP's mathematical framework produces practical engineering advantages, not just theoretical elegance.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Predictive coding has been proposed as a biologically plausible alternative to backpropagation for deep learning, but the field lacks a comprehensive assessment of its practical capabilities, limitations, and relationship to FEP
  Resource: Systematic survey of neuro-mimetic deep learning via predictive coding, covering brain modeling, robotics, variational inference foundations, and asynchronous computation — co-authored by Friston to ensure FEP-theoretical grounding
  Solution: Predictive coding is established as a viable, biologically plausible computational paradigm for AI with demonstrated capabilities across perception, control, and generation — with unique advantages (asynchronous computation, local learning rules) that backpropagation lacks
  Confidence: High
  Evidence: Published in Neural Networks (March 2026); comprehensive review with Friston as co-author ensuring theoretical consistency with FEP

## Cross-Tradition Signals
**Hawkins (strong):** Hawkins' Thousand Brains Theory relies on cortical columns performing predictive coding. This survey's demonstration that predictive coding networks work in practice — with asynchronous computation matching biological neural dynamics — provides engineering validation for Hawkins' architectural claims.

**Levin (moderate):** If predictive coding can be implemented in artificial neural networks asynchronously, the same computational principles may operate in Levin's bioelectric networks, which also process information asynchronously across cell populations. This survey strengthens the formal bridge between FEP-as-neuroscience and FEP-as-basal-cognition.

**C2A2 (moderate):** Predictive coding as a practical AI paradigm could inform the architecture of C2A2 tradition agents — agents that predict what a tradition would say about a given question and update based on prediction errors from actual tradition outputs.
