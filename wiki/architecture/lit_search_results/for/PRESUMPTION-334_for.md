SEARCH-FOR-PRESUMPTION-334:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-334
  Original statement: When direct observation is blocked, structural code-path identity is an acceptable substitute for behavioral verification.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-334
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced unstated presumption by inference from work-log verification claim (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Rothermel, G. & Harrold, M.J., 1996-97. Safe regression test selection (ICSE/TOSEM line). — The one rigorous form of the presumption: when execution traverses only provably unchanged code under equivalent conditions, prior behavioral verification may be reused without re-observation. Establishes that path-identity arguments are admissible — under formal preconditions.
    2. Tricentis / BrowserStack verification-vs-validation guidance (industry assurance practice). — Static verification (reviews, structural analysis) is an accepted assurance contribution when dynamic validation is constrained, though always as a complement, not a substitute.
    3. GeeksforGeeks, "Overview of Latent Defects" (and the compatibility-defect literature it summarizes). — Documents the boundary: identical code exhibits latent defects under different configurations/loads, defining exactly when structural identity fails to carry behavioral guarantees.
  Strength of support: Weak
  Summary: The presumption has a defensible kernel: safe regression-test-selection theory and assurance-case practice both admit structural arguments (unchanged/shared code) as evidence, and industry standards (e.g., safety cases combining analysis with test) accept analytical verification when direct observation is infeasible. But the literature grants this only under strict side conditions — equivalent input domains, configuration, and load — and the latent-defect literature documents that those side conditions are exactly what differ in practice (stress, scale, environment). "Acceptable substitute" overstates what any source supports; "admissible interim evidence pending observation" is the supportable form. Notably, the blocking condition here (renderer stall under the substrate layer's load) is itself a behavioral difference between the contexts, weakening the equivalence premise.
  Caveats: Support is conditional and weakest precisely when observation is blocked by load/scale, since load-dependence is the canonical defeater of path-identity transfer. The presumption should carry an explicit re-verification obligation once observation is unblocked.
  Search scope: 1 WebSearch ("verification by analogy insufficient testing same code different configuration latent bugs evidential standard software assurance"); plus known regression-test-selection literature.
  Recommendation: PARTIALLY-SUPPORTED
