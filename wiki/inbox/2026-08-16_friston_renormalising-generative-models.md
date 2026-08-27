---
proposal_id: PROP-2026-08-16-007
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Renormalising Generative Models for Active Inference: Foundations, Derivations, and Verification"
source_url: https://arxiv.org/abs/2608.09512
source_date: 2026-08-10
searched_on: 2026-08-16
status: pending
---

## Summary
Zaghw, Pashea, Pritsch, Nuijten, Friston and Da Costa give a self-contained derivation of Renormalising Generative Models (RGMs) — the machinery that lets discrete active-inference models stack across spatial and temporal scales, coarse-graining low-level states and paths into higher-level causes for objects, events and actions — together with an open, verified implementation. The paper's stated purpose is reproducibility: the published mathematics is compact and the existing reference code is welded into specialised software, so many algorithmic details were implicit. Where the published equations and the working implementation emphasise different things, the authors say so explicitly and explain what each choice costs.

## Why This Matters for This Tradition
Free-energy work has a recurring criticism attached to it: the formalism is general enough that a reader cannot always tell what an implementation actually does. This paper is Friston's group answering that criticism structurally rather than rhetorically — separating theory from its original implementation context so the framework can be audited and benchmarked by people outside the lab.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Discrete active-inference models do not scale to rich spatial and temporal domains.
  Resource: Renormalising generative models — a hierarchy that composes discrete generative models across scales, coarse-graining lower-level states and paths into higher-level causes.
  Solution: An explicit account of how the hierarchy is built, how beliefs and actions update within it, and how information passes between levels.
  Confidence: High
  Evidence: The abstract names all three as the paper's expository contributions; "renormalising" is used in its physics sense of coarse-graining across scales.

PRS-CANDIDATE-02:
  Problem: The framework was effectively unreproducible — compact published mathematics plus reference implementations embedded in specialised software environments left algorithmic details implicit.
  Resource: An open, verified implementation released alongside a derivation-oriented exposition.
  Solution: Lowered barrier to entry; the framework becomes transparent, auditable and reproducible, and can be quantitatively evaluated on machine-learning benchmarks by third parties.
  Confidence: High
  Evidence: Stated as the explicit motivation and contribution of the paper.

PRS-CANDIDATE-03:
  Problem: Where the published equations and the working code disagree, which is authoritative?
  Resource: Explicit documentation of each divergence between published equations and implementation, with its modelling consequences.
  Solution: The discrepancies become a documented modelling choice rather than a hidden one.
  Confidence: Medium
  Evidence: "Where the published equations and implementation differ in emphasis, we make those choices explicit and explain their modelling consequences." How many such divergences there are, and how substantive, needs the full text.

## Cross-Tradition Signals
- **Wolfram**: renormalisation-by-coarse-graining as the operation that produces higher-level causes is structurally the same move as Wolfram's computationally-bounded observer coarse-graining the ruliad into perceived law. Same operation, opposite starting ontology.
- **Levin**: multi-scale competency architectures — Levin's claim that goals exist at every level of organisation, each level coarse-graining the one below — has an obvious formal counterpart in an RGM hierarchy. This is a candidate site for an actual shared formalism rather than an analogy.
- **Carroll**: coarse-graining as the source of emergent macro-level causes is Carroll's own account of emergence; whether "higher-level causes" here are ontologically real or bookkeeping is the live disagreement.
- **Loughran / C2A2 architecture**: a methodological signal as much as a scientific one — a research programme deliberately making itself auditable is the reproducibility norm the wiki's own build guards enforce.
