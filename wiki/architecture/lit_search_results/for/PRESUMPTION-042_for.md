SEARCH-FOR-PRESUMPTION-042:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-042
  Original statement: "The morning autonomous 14a/14b run's zero-output is a correct reflection of zero architectural activity, rather than a pipeline-coverage miss"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-042
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — zero-output attributed to zero activity (not to pipeline miss)
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Information extraction evaluation literature (Chinchor 1995 MUC evaluation methodology; Manning et al. 2008): zero-output runs in IE pipelines are known to conflate true-negative coverage with pipeline miss; null-output validation requires a gold-standard or external signal.
    2. Self-monitoring / self-evaluation literature (Nisbett & Wilson 1977 "Telling More Than We Can Know"; Flanagan 1984): self-referential evaluation of coverage has systematic blind spots.
    3. The self-awareness pipeline's own 14b instructions explicitly note false-negative invisibility ("false negatives are invisible by definition" — per 14b's own operating instructions).

  Strength of support: None

  Summary: No literature supports treating a zero-output run as self-validating. On the contrary, the IE-evaluation literature and self-monitoring literature are unanimous that null-output validation requires external calibration. The presumption is directly contradicted by the self-awareness pipeline's own acknowledged blind-spot description. The reasonable interpretation of a zero-output day is "possibly correct, possibly pipeline miss, cannot discriminate without external signal."

  Caveats: The presumption could become supportable if paired with an external coverage audit (e.g., Tom reviewing the same session transcript and confirming no extractable items were missed).

  Recommendation: NO-SUPPORT-FOUND
