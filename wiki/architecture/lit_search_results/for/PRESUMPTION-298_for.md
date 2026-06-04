SEARCH-FOR-PRESUMPTION-298:
  Date searched: 2026-06-03
  Original item: PRESUMPTION-298
  Original statement: [inferred] A single live spot-check generalizes to full correctness — the fade fix was verified on one isolate (`levin`) and one focus pair (`levin ~ summa`) and signed off as "works" for all isolates/foci.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-298
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an induction risk — one isolate + one focus pair signed off as correct for all.
      15a: Searched induction/sampling risk, coverage vs single-case verification, equivalence-class/boundary testing.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Equivalence-class partitioning theory (TestBench; Myers, Art of Software Testing ch.4; Katalon BVA guide). — One representative per class is sufficient ONLY if the class is genuinely equivalent; the method's validity rests on a correct partition, which a single ad-hoc isolate does not establish.
    2. Boundary value analysis (Ficode BVA/EP; testbench). — Defects cluster at boundaries (e.g., isolates with zero cross-links, maximally-connected foci); testing a single mid-class case misses exactly the cases most likely to break.
    3. Believed-equivalence refinement for autonomous systems (arXiv:2103.04578). — Formalizes that "believed equivalence" between cases must be refined/verified, not assumed; a spot-check presumes an equivalence that has not been checked.

  Strength of support: Moderate-Strong

  Summary: The presumed weakness is supported by standard test-design theory: a single spot-check generalizes to a class only when the class is truly equivalent, and that partition must be justified rather than assumed. Fade behavior plausibly varies by isolate degree and focus connectivity, with boundaries (zero-link isolates, dense foci) being the highest-risk and least-represented by one mid-class sample. So "verified on `levin` + `levin~summa`, therefore correct for all" is exactly the induction the literature cautions against. Support is for the existence of the generalization risk.

  Caveats: If the fade logic is provably uniform across isolates/foci (one code path, no per-node branching), one representative case can be legitimately sufficient and exhaustive UI checking would be wasteful (see 15b). The risk is conditional on the partition being non-trivial.

  Recommendation: SUPPORTED
