---
proposal_id: PROP-2026-08-10-003
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Homeostatic feedback model of energy metabolism with adaptive enzyme levels exhibits problem solving behavior"
source_url: https://www.biorxiv.org/content/10.64898/2026.05.07.721661v1
source_date: 2026-05-07
searched_on: 2026-08-10
status: pending
---

> SOURCE-READ NOTE (fail-loud): **abstract-level content only**, retrieved via search; the bioRxiv page itself was not fetched and the **full text, figures, and parameter values were not read**. Authorship and date confirmed against Levin's preprints page (de Baat, A., Levin, M., 2026, bioRxiv doi 10.64898/2026.05.07.721661). No quantitative claim is made below. Retry URL from the Mac: `https://www.biorxiv.org/content/10.64898/2026.05.07.721661v1`.
>
> COVERAGE NOTE: see PROP-2026-08-10-001 for the in-window sweep — nothing new found in the 30-day window. Filed under "significant work not yet captured." This is the **thinnest** of today's three Levin proposals and is filed because it extends basal cognition into a substrate the wiki has not yet covered (metabolic networks), not because the source is rich.

## Summary
De Baat and Levin build a coarse-grained dynamical model of mammalian energy metabolism and ask whether **prior perturbation can improve future metabolic response** — that is, whether the feedback architecture that keeps metabolism robust can also produce learning-like, experience-dependent adaptation.

The model represents core glucose, glutamine, fatty-acid, and oxidative-phosphorylation pathways with Michaelis–Menten-type fluxes, product-inhibition feedback, adaptive enzyme-capacity regulation, and — importantly — **explicit ATP costs for enzyme adjustment**, so that adaptation is not free. The reported result is that the system exhibits problem-solving behavior.

## Why This Matters for This Tradition
Levin's basal-cognition claim has been demonstrated principally in **bioelectric** networks: membrane voltage, gap junctions, ion flux. The metabolic network is a different information-processing substrate in the same cells, and the tradition has said comparatively little about it. If a coarse-grained metabolic model with nothing but homeostatic feedback and adaptive enzyme levels shows experience-dependent improvement, then the tradition's central claim — that goal-directedness is a property of feedback architectures rather than of neurons — gains a second, independent biological substrate.

The costed-adaptation detail matters more than it looks. Because enzyme adjustment carries an explicit ATP price, any learning the model shows is learning the system *paid for*, which is the kind of trade-off that distinguishes an adaptive policy from a passive relaxation to equilibrium.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Homeostatic feedback is standardly read as a *stability* mechanism — it returns a system to setpoint and nothing more. Whether the same architecture can also produce experience-dependent improvement (learning-like behavior) has not been tested in metabolism.
  Resource: A coarse-grained dynamical model of mammalian energy metabolism — glucose, glutamine, fatty-acid, and oxidative-phosphorylation pathways with Michaelis–Menten fluxes, product-inhibition feedback, adaptive enzyme-capacity regulation, and explicit ATP costs for enzyme adjustment.
  Solution: The model "exhibits problem solving behavior" — prior perturbation improves later response, so the same feedback architecture that yields robustness also yields something that looks like learning.
  Confidence: Medium
  Evidence: Retrieved abstract summary. Medium, not High: what counts as "problem solving" here, and how strong the improvement is, are in the unread results.

PRS-CANDIDATE-02:
  Problem: Basal cognition in Levin's program has been argued almost entirely from bioelectric evidence. A framework claiming substrate-independence is weaker if it keeps returning to one substrate.
  Resource: Metabolism as a second, non-bioelectric candidate substrate for basal problem-solving within the same cell.
  Solution: The diverse-intelligence framework extends to metabolic networks, which suggests the operative variable is the **feedback-plus-costed-plasticity architecture** rather than any particular physical medium.
  Confidence: Speculative
  Evidence: Inference from the abstract, not a claim the authors are shown to make in the retrieved text. Flagged Speculative for that reason — the generalization is the wiki's reading, not a quoted position.

## Cross-Tradition Signals

**Friston — a costed free-energy story, ready-made (strong, direct).** This is the cleanest Levin↔Friston bridge in today's batch. The model's structure maps almost term-for-term onto active inference: product-inhibition feedback is prediction-error correction; adaptive enzyme capacity is slow parameter updating; and the **explicit ATP cost of enzyme adjustment** is precisely the complexity term of variational free energy — accuracy *as cheaply as possible*, which the Friston wiki already carries verbatim from PROP-2026-07-20-004. The Friston tradition also carries an open question, "What are the thermodynamic limits of free energy minimisation — can it address the energetic cost of cognition?" (active question 5). **This model is a concrete system in which that question has an answer, because the energetic cost of adaptation is an explicit parameter.** Recommend the Friston agent be asked to attempt the derivation directly.

**Levin-internal — connects to the metabolism/aging thread (medium).** Ties to the already-captured Sediqi & Levin keratinocyte-senescence work (morphostatic information loss) and to the multi-scale longevity preprint. If metabolic feedback can learn, then metabolic *dysregulation* is a candidate for unlearning — which is the shape of Levin's existing account of cancer and aging in bioelectric terms.

**Hawkins — learning without a learning rule (weak, note only).** No synaptic plasticity, no explicit learning algorithm, and yet experience-dependent improvement. Noted for the "what is the minimal architecture that learns?" thread.

## Sources
- [Homeostatic feedback model of energy metabolism with adaptive enzyme levels exhibits problem solving behavior — bioRxiv](https://www.biorxiv.org/content/10.64898/2026.05.07.721661v1) (abstract-level summary retrieved via search; **full text NOT read**)
- [Dr. Michael Levin — Preprints](https://drmichaellevin.org/publications/preprints.html) (read in full; authorship and date confirmation)
