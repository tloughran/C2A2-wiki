SEARCH-FOR-ASSUMPTION-272:
  Date searched: 2026-06-05
  Original item: ASSUMPTION-272
  Original statement: Draining the 36-file ingest backlog should proceed as small, attended-authorized batches (~5-8 files/run), not a single bulk ingest, to protect PRS-triplet quality and avoid sweeping unrelated working-tree changes into the commit.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-272
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the stated batch-ingest policy preferring small attended batches over a single bulk run.
      15a: Searched lean/agile WIP-limit and batch-size literature on small-batch quality and defect isolation.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Reinertsen, D. (via SAFe Principle #6: "Visualize and limit WIP, reduce batch sizes, manage queue lengths"). InformIT / Scaled Agile. — Foundational product-flow result: small batches reduce variability, accelerate feedback, and lower the cost and risk of each transaction. Direct support for capping ingest at ~5-8 files/run to keep defect cost bounded.
    2. dev2ops, "DevOps Lessons from Lean: Small Batches Improve Flow," 2012. — Smaller batches reduce the complexity handled at any one moment and enable rapid defect detection before defects multiply downstream — precisely the PRS-triplet quality-protection rationale.
    3. Lean Six Sigma Hub, "Batch Size Reduction: Why Smaller Batches Lead to Better Performance." — Smaller batches isolate and address quality issues promptly with minimal impact on the overall process, and simplify review/validation. Supports both clauses: better per-item curation quality and easier scoping of what enters each commit.

  Strength of support: Strong

  Summary: The lean/agile flow literature strongly supports small attended batches for a quality-sensitive curation task. Reducing batch size lowers per-transaction risk and variability, speeds defect detection, and simplifies review — all of which map directly onto protecting PRS-triplet quality and keeping each ingest commit scoped. The "avoid sweeping unrelated working-tree changes into the commit" clause is independently supported by commit-hygiene practice (small, coherent changesets are easier to review and revert). The recommended ~5-8 files/run sits well inside the regime the literature endorses.

  Caveats: The literature also warns that batch size can be made too small: per-batch transaction (overhead) cost sets a lower bound, and if attended authorization is expensive, very small batches can starve throughput (this is 15b's tension). The optimum is a U-curve, not "smaller is always better" — so 5-8 is defensible but should be tuned against actual per-run authorization overhead, not treated as a floor.

  Recommendation: SUPPORTED
