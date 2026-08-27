---
proposal_id: PROP-2026-08-16-009
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Limbomorphs"
source_url: https://arxiv.org/abs/2607.23842
source_date: 2026-07-26
searched_on: 2026-08-16
status: pending
---

## Summary
Alvarez and Levin work with Gifbreeder, an animated version of the interactive-evolution art platform Picbreeder, where a genome encodes not an agent and not an environment but a spatiotemporal field, evolved purely by a human user picking what looks appealing. Some of the evolved animations look like moving creatures; the authors call these Limbomorphs, because each exists in a deterministic three-second loop — a "limbo". They probe them by perturbing the input space and find that different Limbomorph types react in type-specific ways, then ask whether those reactions are goal-directed behaviour such as navigation or only the appearance of it.

## Why This Matters for This Tradition
Every other Levin substrate — cells, tissues, xenobots, sorting algorithms — at least has a body and an environment. Here there is neither: no agent, no environment, no interaction rules are defined anywhere in the system, yet agent-like dynamics show up and respond differentially to perturbation. It is the cleanest available test of whether Levin's agency-detection methods are finding something real or manufacturing it.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Artificial-life systems normally presuppose the very things whose emergence they claim to study — an agent, an environment, or dynamical rules over both.
  Resource: Gifbreeder, whose genomes encode a spatiotemporal field and evolve by human aesthetic selection alone, with no agent, environment, or interaction rules specified.
  Solution: A substrate in which agent-like dynamics, if they appear, cannot have been built in by the designer.
  Confidence: High
  Evidence: The abstract states the system has "no explicitly defined agent, environment, or interaction rules," contrasted against the standard artificial-life setup.

PRS-CANDIDATE-02:
  Problem: How to test for behaviour in an entity that has no sensors, no actuators, and no defined environment to act in.
  Resource: Input-space perturbation as the assay — disturb the field's inputs and characterise the response.
  Solution: Species-specific reactions to different kinds of perturbation, giving a behavioural signature that distinguishes Limbomorph types.
  Confidence: Medium
  Evidence: "We assess their behavior via input-space perturbations and find species-specific reactions to different kinds of perturbations." How many types, and how the species boundaries were drawn, needs the full text.

PRS-CANDIDATE-03:
  Problem: Whether such reactions constitute goal-directed behaviour (e.g. navigation) or only its appearance — the perennial charge against ascribing cognition to unconventional substrates.
  Resource: The three-second deterministic loop itself as a constraint: nothing here can learn, remember across loops, or be selected for competence, since selection was aesthetic.
  Solution: The authors pose the question rather than settle it, and use it to ask more broadly how agent-like dynamics arise where nothing agent-like was specified.
  Confidence: Speculative
  Evidence: The abstract explicitly frames this as a discussion — "We discuss whether these reactions may reflect goal-directed behavior like navigation, or merely the appearance of it." Treating it as a settled finding would misread the source.

## Cross-Tradition Signals
- **Hoffman**: an artefact selected purely on how it looks to a human observer, then found to have observer-independent-seeming structure, is a live case for interface theory — is the agency in the field or in the perceiver's headset? This is one of the few places the two programmes could be put in genuine tension rather than analogy.
- **Friston**: a system with no defined environment cannot have a Markov blanket in the standard sense, so it is a boundary case for the free-energy account of what makes something a thing.
- **McGilchrist**: aesthetic selection as the sole fitness function — the right-hemisphere mode of attention as the thing doing the selecting — is unusually literal here.
- **Wolfram**: lifelike behaviour emerging from a spatiotemporal field with no agent specified is close to the cellular-automaton lineage; Gifbreeder's genomes are a different encoding of the same question.
