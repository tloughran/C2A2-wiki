---
proposal_id: PROP-2026-10-12-002
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "The phantastic organ: predictive processing in the brain"
source_url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1901293/full
source_date: 2026-09-25
searched_on: 2026-10-12
status: pending
---

## Summary
Friston and Thomas Parr's review in *Frontiers in Psychology* (vol. 17, Perception Science; doi 10.3389/fpsyg.2026.1901293) traces predictive coding from Helmholtz's "unconscious inference" to present-day active inference. It covers precision (and neuromodulation as the way the brain encodes it), reward learning, machine learning, planning, and structure learning. It also offers a "reverse history": it starts from the free energy principle and derives predictive coding from it. The "ph" in *phantastic* marks two links the authors intend: to Newton's term for imagery not caused by light, and to psychoanalytic "phantasy," an unconscious inner reality fitted to an outer one.

## Why This Matters for This Tradition
This is the program's own up-to-date account of how its parts connect, written by its founder and a principal co-author. It closes on structure learning, the question of how a system finds the right model in the first place, and frames that as Bayesian model selection, which the authors call "the mathematical image of natural selection." Neither the title nor this framing is yet in `traditions/friston/`.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Predictive coding, active inference, reward learning and generative AI are usually told as separate histories, which hides whether they are one idea or several.
  Resource: A "reverse history" that begins from the free energy principle: any multidimensional random dynamical system, "from a postsynaptic process ... to a person," can be described as minimizing variational free energy. Predictive coding then follows as a general description of self-organizing open systems.
  Solution: The developments become special cases of one scheme. Generative models unify the line "from Helmholtz's unconscious inference, through 20th century developments in variational calculus, to the mechanics of predictive coding," and the same models underwrite generative AI.
  Confidence: High. The section text and conclusion were read directly.
  Evidence: Section 8 ("A reverse history of predictive coding: neurobiology from first principles") and Section 11 (Conclusion).

PRS-CANDIDATE-02:
  Problem: Standard predictive-processing models assume a fixed set of variables. They do not explain how a brain discovers which variables exist, or how those variables relate.
  Resource: A mean-field partition of the unknowns in a generative model: fast-changing states, precision (which sets how far each signal is trusted), and slowly changing parameters. To these the paper adds a fourth attribute, structure, meaning the model's architecture and functional form. This yields a three-way distinction between inference, learning, and selection.
  Solution: Structure learning becomes Bayesian model selection: choose the model with the greatest evidence, which is the same as the smallest variational free energy. The authors call this the "mathematical image of natural selection at an evolutionary timescale," which places causal discovery in the brain inside the same free-energy scheme.
  Confidence: Medium. The section's opening argument was read; the later, more technical part of Section 10 was not.
  Evidence: Section 10 ("Structured predictions: causal discovery in the brain"): "The distinction between model states, parameters and structure leads to a distinction between inference, learning and selection ... one simply selects the model with the greatest evidence (or smallest variational free energy)."

PRS-CANDIDATE-03:
  Problem: How do the pieces of the program connect to brain anatomy and physiology closely enough to be tested?
  Resource: The review's stated aim is to "furnish a framework that brings theory and empirical study in close contact, through generating mechanistic (anatomical and physiological) hypotheses about sense-making in the brain." It treats precision as neuromodulatory gain, which the paper calls "representational sharpening."
  Solution: It consolidates the program's empirical agenda (precision as gain, applied to clinical disorders including hallucinations and apathy) as a single source of hypotheses. This continues the precision-psychiatry line (PRS from PROP-2026-05-18-003).
  Confidence: Medium. It is a review; its new content is mostly in how it synthesizes the field.
  Evidence: Abstract; Section 3 ("The importance of being precise: neuromodulation and representational sharpening").

## Cross-Tradition Signals
- **Levin (flag explicitly):** The opening claim that free-energy minimization applies to any random dynamical system, "from a postsynaptic process to a person," is the substrate-independence premise behind Levin's bioelectric agency. Structure learning framed as natural selection also connects to Levin's reading of evolution as a search over problem-solving competencies.
- **Wolfram:** Structure learning as selection over a space of model architectures parallels search across the ruliad, a selection among possible computational rules.
- **McGilchrist / Kastrup:** "Phantasy" as an unconscious inner reality fitted to the outer world maps onto McGilchrist's account of the hemispheres' different ways of attending to the world and onto Kastrup's dissociated inner/outer states.
- **Hawkins:** The paper's planning and structured-prediction sections overlap with reference-frame learning in cortical columns.
- **C2A2 relevance:** Model selection by evidence is a formal analogue for how traditions are compared. On that analogy, a community "selects" among rival generative models by their accumulated evidence, in line with MacIntyre's account of how traditions rise or fall in rational standing.
