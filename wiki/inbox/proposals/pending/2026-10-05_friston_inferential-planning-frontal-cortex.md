---
proposal_id: PROP-2026-10-05-001
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Inferential planning in the frontal cortex"
source_url: https://www.biorxiv.org/content/10.1101/2025.11.26.690672.full.pdf
source_date: 2026-08 (Cell Reports publication, reported 2026-08-31; bioRxiv preprint posted 2025-11-26)
searched_on: 2026-10-05
status: pending
---

## Summary
Donnarumma, Parr, Friston, Whittington & Pezzulo build a two-level active-inference model in which a plan is not sampled one step at a time but *inferred* all at once: the upper level holds a separate copy of state and action beliefs for every future time step, and those copies exchange messages with each other and with the goal. Simulated on three primate frontal-cortex tasks (maze cursor planning, a remembered saccade sequence, and forward/backward sequences of variable length), the model reproduces what recordings show — all plan elements active at once, nearly orthogonal "rank" memory subspaces, and the same memory subspaces reused for forward and backward recall. The authors conclude that planning and sequence working memory are one inference process seen from two sides.

## Why This Matters for This Tradition
It is a neural-data test of active inference's planning-as-inference claim, and it gives a mechanistic reason (parallel message passing needs past, present and future held at once) for a representational format that serial and competitive-queuing models must simply assume. Note on attribution: Friston is a middle co-author; Pezzulo is corresponding author. It is squarely inside the Friston program but is not a Friston-led paper.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Frontal cortex represents every element of a planned sequence simultaneously, in separable neural subspaces ("activity slots"), which contradicts classical serial and competitive-queuing accounts of planning. Why would the brain use this format?
  Resource: A hierarchical active-inference generative model whose upper level contains one copy of state/action beliefs per time step, updated by variational message passing (belief-propagation style).
  Solution: Simultaneous slot coding falls out of inferring a plan: for past, present and anticipated states to pass messages to each other in parallel, each must be represented at the same time. The format is a precondition of inference, not an added queuing mechanism.
  Confidence: High
  Evidence: Abstract (bioRxiv, read directly) states the model reproduces "the simultaneous activation of multiple plan elements, the emergence of (almost) orthogonal 'memory' subspaces, and their reuse across forward and backward sequence tasks." The Cell Reports discussion section, as summarised by a secondary news source (ebiotrade.com, Chinese-language), states the "necessary precondition" argument explicitly.

PRS-CANDIDATE-02:
  Problem: Planning, sequence working memory and motor preparation are usually modelled by separate mechanisms.
  Resource: The same inferential-planning model applied across three task families, with subspace analysis (PCA, principal angles, participation ratio) matched to published primate recordings.
  Solution: One inference process accounts for all three; planning and working memory are "two sides of the same coin."
  Confidence: Medium
  Evidence: Abstract claims the framework "unifies previously disparate findings on planning, working memory, and motor preparation." Medium because the fit is to previously published data, not new recordings, and execution of the plan was not simulated (a limitation the authors state, per the secondary summary).

PRS-CANDIDATE-03:
  Problem: Under uncertainty about sequence length or direction, how should plan representations evolve before the ambiguity resolves?
  Resource: Simulations of variable-length forward vs. backward recall and a late direction cue.
  Solution: The model predicts fast commitment to the first element in forward recall, held-off commitment in backward recall until all targets are seen, and balanced forward/backward hypotheses until the cue arrives. These are testable predictions about active-inference dynamics.
  Confidence: Speculative
  Evidence: Prediction-level only; drawn from the secondary summary of the results section. Primary full text not read in this pass.

## Cross-Tradition Signals
- **Hawkins** — strongest signal. Hawkins's Thousand Brains theory treats cortex as a sequence-and-prediction machine. This paper offers a competing mechanism for sequence representation in cortex (parallel inferred slots vs. Hawkins's sequence memory). Worth a bridge note asking whether the two make different predictions about the orthogonal rank subspaces.
- **Levin** — Pezzulo is Levin's frequent co-author (*Bootstrapping Life-Inspired Machine Intelligence*, already approved). Inferring a whole trajectory toward a goal state, rather than stepping through it, has the same shape as Levin's morphogenetic "target morphology" framing. Speculative; flag only.
- **C2A2 relevance** — weak. Nothing here about social systems or physics.

## Provenance Note
Abstract and author list read directly from the bioRxiv page. The Cell Reports version was not fetched; the publication venue and the ~2026-08-31 date come from a Chinese-language science-news page (ebiotrade.com) that translates the Cell Reports abstract and summarises the paper. The two abstracts match. Before ingesting, swap in the Cell Reports DOI and check whether the published text differs from the preprint.
