SEARCH-AGAINST-PRESUMPTION-727:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-727
  Original statement: That the defect register describes a static corpus; a correctly-unanchored claim became anchorable because PRS-52 was added 2026-07-21, and 128 days now predate a tradition file they cite — no register entry carries the corpus state it was judged against, so verdicts cannot be replayed and clean passes have no expiry.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-727
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Paired a QC finding with the nightly verification's independent measurement of the same effect
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Carruthers, Diaz-Pace & Irrazábal, 2024. "A longitudinal study on the temporal validity of software samples." Information and Software Technology (ScienceDirect). Finds that after five years, project samples had below 25% probability of remaining representative for the metrics studied — demonstrating that corpora drift enough to invalidate earlier findings, and that maintenance/re-verification strategies (not just initial sampling) are required to detect this.
    2. Semmelrock et al., 2025. "Reproducibility in machine-learning-based research: Overview, barriers, and drivers." AI Magazine (Wiley). Documents that lack of provenance/versioning of the exact data/artifact state a result was computed against is a leading driver of irreproducibility.
    3. [unverified — from search snippet] "AI-Assisted Engineering Should Track the Epistemic Status and Temporal Validity of Architectural Decisions" (arXiv 2601.21116, 2026). Snippet claims current LLM-assisted engineering workflows lack explicit temporal-validity tracking and durable audit trails, and reports that "of 14 decisions with stale evidence, 12 were discovered only when they caused problems during incident investigation or refactoring" — directly analogous to a register that can't detect its own staleness until failure.
    4. Industry practice: DVC and general MLOps provenance tooling treat "record the exact snapshot/commit an evaluation ran against" as a baseline requirement precisely because unpinned evaluations become silently unreplayable as the underlying corpus changes.

  Strength of challenge: Strong

  Summary: The literature on temporal validity of software corpora and ML reproducibility converges on the same failure mode PRESUMPTION-727 identifies: verdicts recorded without a corpus-state anchor (commit hash, snapshot ID, or file inventory) decay silently, and the decay is discovered only retrospectively, when something downstream breaks. The "static corpus" assumption is explicitly contradicted by empirical measurement — representativeness/validity erodes measurably over time and use, not just hypothetically. No literature was found asserting audit corpora are stable by default; the field's consensus is the opposite.

  Specific risks: If register verdicts carry no corpus-state anchor, "clean pass" entries become false-negative sources indefinitely — new tradition files or PRS additions can retroactively make an old "unanchored, therefore fine" verdict wrong, but nothing re-triggers review. This compounds over cycles: the 128-day-old predates-cited-file gap found here is evidence the failure is already active, not hypothetical.

  Mitigations available: Yes — well-established: (1) pin each verdict to a corpus hash/snapshot ID at judgment time (content-addressable versioning, e.g. DVC-style); (2) give every "clean pass" an explicit expiry or re-validation trigger keyed to corpus diffs touching cited files; (3) periodic re-sampling/re-verification passes, as recommended in the temporal-validity literature, rather than one-shot verdicts.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-727
  Strongest counterargument: A defect/audit register that treats every past verdict as permanently valid is making an untested and empirically falsified assumption. Software-engineering research on temporal validity shows corpora become unrepresentative within a measurable, often short, timeframe, and MLOps reproducibility research shows that provenance-less evaluations are a primary cause of irreproducible, unreplayable conclusions. The register's own data — a claim that became anchorable after a later addition, and a 128-day gap against a cited file — is itself a documented instance of the exact failure the general literature predicts, not a hypothetical.
  What would need to be true for C2A2 to be safe: Every verdict would need to be either (a) re-validated whenever the corpus subset it depends on changes, or (b) explicitly time-boxed with an expiry that forces re-review, or (c) provably insensitive to corpus additions (e.g., verdicts about content that cannot be affected by new files). None of these appear to hold given the described register design.
  How to test: Sample N historical "clean pass" verdicts, diff the corpus state today against the corpus state at judgment time (if recoverable), and check whether any newly-added files would flip the verdict if replayed. A non-zero flip rate under a plausible-sized sample confirms the challenge empirically for this specific register.

Search scope: preliminary search — broader search into audit-trail/compliance-record versioning standards (e.g., ISO recordkeeping, blockchain-based provenance) recommended for deeper grounding.
