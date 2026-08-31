SEARCH-FOR-PRESUMPTION-900:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-900
  Original statement: [inferred] Convergence among independently generated proposals indicates redundancy rather than corroboration.
  Generalizable limb searched: Is there literature under which agreement among nominally independent generators is correctly read as redundancy (correlated error / shared cause) rather than as corroboration?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. Several
    supporting sources are recent arXiv preprints seen only as search snippets — weighted accordingly.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-900
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from the intake layer's handling of co-arising proposals — the layer
        deduplicates rather than pools, which only makes sense if convergence is being read as
        redundancy. Flagged NOVELTY candidate; paired with ASSUMPTION-1242.
      15a: Searched for supporting literature (2026-08-31)
    Current status: SUPPORTED (conditionally — the condition is the load-bearing part)

  Supporting evidence found: Yes

  Sources:
    1. Bommasani, R., Creel, K. A., Kumar, A., Jurafsky, D., Liang, P. (2022), "Picking on the Same Person:
       Does Algorithmic Monoculture lead to Outcome Homogenization?" NeurIPS 2022 (arXiv:2211.13972).
       — The strongest and best-established source here (peer-reviewed, NeurIPS main track). Proposes and
       tests the "component sharing hypothesis": systems built on the same data or models increasingly
       homogenize outcomes. Increased data-sharing reliably exacerbates homogenization. Directly supports
       reading agreement among same-substrate generators as a property of the substrate, not of the world.
    2. "Correlated Errors in Large Language Models" (arXiv:2506.07962). — Snippet-level. Reports that
       frontier models exhibit correlated errors, with higher correlation for individually more accurate
       models and for models from the same developer or base architecture — i.e. models converge in the
       errors they make as they improve.
    3. "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels"
       (arXiv:2605.29800). — Snippet-level. The title states the finding: nominally independent judges
       collapse to a far smaller effective sample. Describes judges as correlated through shared family,
       training data, and prompt artifacts, producing an "illusion of redundancy."
    4. Hurlbert, S. H. (pseudoreplication / the pooling fallacy), via "Pseudoreplication Is (Still) a Problem"
       (ResearchGate 40022598), Lazic et al. "Population sampling affects pseudoreplication" (PLOS Biology,
       2018, PMC6188620), and a Bayesian treatment in Scientific Reports (2020), s41598-020-59384-7.
       — The classical statistical form of the same error: treating non-independent observations as
       independent replicates falsely inflates N and statistical power, raising Type I error. Reported as
       affecting more than half of published experiments in some fields.
    5. Condorcet Jury Theorem independence condition, as applied in the LLM-ensemble literature above and
       in orq.ai's practitioner writeup "Weak judges, strong panel." — Snippet-level. Majority voting
       improves accuracy only when individual errors are uncorrelated; when they are correlated the
       ensemble behaves as an echo chamber and large N does not rescue it.

  Strength of support: Strong (for the conditional form); Weak (for the unconditional form)

  Summary: There is a substantial and current literature supporting the presumption, but it supports a
    sharpened version of it: convergence indicates redundancy WHEN the generators share a common cause.
    The AI-specific work is unusually on-point for this project, because the shared cause it identifies —
    same base model, overlapping training data, shared prompt scaffold, shared upstream context — is
    exactly the configuration of a multi-agent pipeline whose agents are instances of one model. The
    NeurIPS monoculture result and the correlated-errors preprints together say that "independently
    generated" in the sense of "run in separate contexts" is NOT independence in the sense the evidential
    argument requires. Pseudoreplication supplies the older statistical form of the same point and shows
    the error is both common and consequential. So the intake layer's implicit deduplication instinct is
    defensible, and defensible for a better reason than it probably knows.

  Caveats: The support is entirely conditional on non-independence, and the presumption as stated is
    unconditional — it reads convergence as redundancy full stop. That unconditional form is not supported
    and is contradicted by the consilience/corroboration literature found under ASSUMPTION-1242. The
    two items are contraries only if both are read unconditionally; read conditionally they are two
    branches of one rule. Second caveat: three of the five sources are recent arXiv preprints seen only as
    snippets; the peer-reviewed weight rests mainly on Bommasani et al. and on the pseudoreplication
    literature. Third: the AI monoculture work concerns errors and outcomes, not proposal generation, so
    the transfer to "co-arising conceptual proposals" is an extrapolation I did not find directly tested.

  Recommendation: SUPPORTED

  NOVELTY-FLAG:
    Item: PRESUMPTION-900
    Searched scope: algorithmic monoculture, LLM correlated errors and judge panels, Condorcet
      independence, pseudoreplication / pooling fallacy.
    Finding: NOT novel. The 14b novelty flag should be withdrawn — this is an active research area with
      a NeurIPS-published core result and a 2025-2026 preprint literature addressing the LLM case
      specifically. The intake note describes this as "the accelerator's own measurement problem appearing
      in its intake layer"; the literature would call it correlated-error/monoculture, and it already has
      an effective-sample-size framing ("nine judges, two effective votes") ready to import.
    Implication: The intake layer needs an independence test, not a dedup rule. Concretely: were the
      co-arising proposals generated from the same base model, the same context window, or the same
      upstream document? If yes, discount toward one effective observation. If no, pool and upgrade per
      ASSUMPTION-1242. The pipeline currently cannot answer that question, which is the actual gap.
    Recommended status: NOT NOVEL — supersede with the effective-sample-size / component-sharing framing.
