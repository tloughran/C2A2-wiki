SEARCH-FOR-ASSUMPTION-319:
  Date searched: 2026-06-16
  Original item: ASSUMPTION-319
  Original statement: "git history of traditions/*/prs_triplets.md yields valid 'triplet-completed' dates (PRS-NN per commit-day)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-319
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-15 session (Metabolism event-dating from VCS history)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Mining Software Repositories (MSR) foundational practice (Palomba & Verdecchia, "Teaching Mining Software Repositories," Springer 2025). — Using commit history to date code/artifact events is a standard, validated MSR technique; the field is built on extracting event timelines from VCS metadata. This directly supports the general method of reading "when did PRS-NN appear" from git history.
    2. Claes et al., 2018, "Do Programmers Work at Night or During the Weekend?" (arXiv:1802.05084). — Finds commit timestamps reliable enough to recover daily/weekly working-rhythm structure (e.g., lunch-hour dips), evidence that commit timestamps are faithful at DAILY resolution — the exact resolution this assumption needs ("per commit-day").
    3. Empirical commit-frequency work (Kolassa et al., 2014, "The Empirical Commit Frequency Distribution of Open Source Projects," arXiv:1408.4978). — Establishes that commit events are a usable unit for temporal activity series at day granularity, supporting per-commit-day binning of triplet-completion events.

  Strength of support: Moderate

  Summary: Reading triplet-completion dates from the git history of prs_triplets.md is a standard MSR technique and is supported at the daily resolution the Metabolism view uses. Commit timestamps are demonstrably reliable enough to recover day-level structure. The support holds for the COARSE-RESOLUTION dating the assumption requires (PRS-NN per commit-day), which is well within the regime where MSR treats commit timestamps as trustworthy.

  Caveats: MSR's own validity literature flags that the mapping from "commit appears" to "work completed" is imperfect (batch commits, backfilled history, quick-remedy commits, committer-vs-author date divergence). The support is for coarse daily dating of when the line was committed, not for the stronger claim that the commit instant equals the completion instant. Validity depends on prs_triplets.md being committed roughly when triplets are completed rather than in periodic backfill batches — a checkable property.

  Search scope: MSR event-dating methodology, commit-timestamp reliability at daily resolution, commit-frequency distributions. Comprehensive.

  Recommendation: PARTIALLY-SUPPORTED
