SEARCH-AGAINST-ASSUMPTION-208:
  Date searched: 2026-05-21
  Original item: ASSUMPTION-208
  Original statement: "Progress = better compression; a forming master science shows as total description length falling while coverage rises."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-208
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: proposed headline progress metric — progress as compression (total description length down, coverage up).
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Grunwald (2007) "The Minimum Description Length Principle"; Kolmogorov uncomputability. — MDL requires a fixed model class & coding scheme; "total description length" over an open corpus is not well-defined (gates on PRESUMPTION-222).
    2. Kuhn (1962) incommensurability. — Across paradigm shifts there is no common code/length to compare; description length is not paradigm-invariant.
    3. Counterexamples: the Standard Model, general relativity. — Major progress often ADDS descriptive machinery while increasing coverage; "shorter" is not necessary for progress.
    4. Overfitting/Goodhart. — Minimizing description length can be gamed by lossy compression that drops important distinctions; length vs coverage is not a single scalar.

  Strength of challenge: Strong

  Summary: The challenge is strong on two levels. Formally, there is no canonical, computable 'total description length' over a heterogeneous, paradigm-spanning corpus (Grunwald; Kolmogorov; Kuhn) — so the headline metric is ill-defined as stated. Substantively, progress is not always compression (major theories add machinery while extending reach) and a length target is gameable. The metric rests on PRESUMPTION-222, which is itself unvalidated.

  Specific risks: Adopting description-length as THE progress metric could drive over-compression, misreport progress, and penalize genuinely progressive complexity.

  Mitigations available: Demote to one indicator among several; or adopt an explicitly-labeled computable proxy (LM cross-entropy codelength; MDL graph summarization) and validate it; pair with a coverage/fidelity guard.

  Recommendation: CHALLENGED (strong)

  STEELMAN:
    Item: ASSUMPTION-208
    Strongest counterargument: 'Total description length falling while coverage rises' presupposes a paradigm-invariant code that Kolmogorov uncomputability and Kuhnian incommensurability both deny; worse, real master theories (the Standard Model) grew longer while covering more, so the metric can mislabel progress as regress.
    What would need to be true for C2A2 to be safe: Description-length is a labeled proxy (e.g., LM codelength) used as one indicator with a fidelity guard, not the definition of progress.
    How to test: Compute a proxy codelength over a versioned corpus and check whether it tracks independently-judged progress; expect divergence at paradigm shifts.
