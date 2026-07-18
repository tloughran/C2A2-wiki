SEARCH-FOR-PRESUMPTION-472:
  Date searched: 2026-07-12
  Original item: PRESUMPTION-472
  Original statement: "Systematic citation mislabels are textually regular enough for batch grep — the error class is presumed string-shaped, though one observed instance is a gloss."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-472
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced by inference from 2026-07-11 EOD daily run
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. [US Patent 12,222,911, "String data error detection and repair." — String-shaped error classes are a recognized, tractable category: when errors are textually regular, pattern-based detection and repair at scale is established practice with dedicated tooling.]
    2. [Apex CoVantage, "Automating Citation Validation: A Game-Changer for Publishers and Authors." — Production citation-QC systems do catch a large share of citation defects mechanically (formatting errors, outdated details, metadata mismatches) by pattern- and database-cross-checking — evidence that a substantial subclass of citation errors is indeed surface-detectable.]
    3. [Nightfall AI, "What's the difference between Regex and AI-based Detection?" — Regex detection performs well precisely when the target class is well-defined and textually regular; the boundary of its adequacy is the boundary of the class's regularity.]
  Strength of support: Weak
  Summary: If the mislabel cluster is string-shaped, batch grep is well-precedented — pattern-based repair of textually regular error classes is standard, and commercial citation QC demonstrates that much of citation error is mechanical. But the support is conditional on the very property the presumption assumes rather than establishes: regularity of the class. Publisher-grade tools that rely on surface checking are documented to catch the formatting subclass while requiring semantic (full-text or NLP) analysis for the rest. The single observed instance being a gloss — a semantic error — is a within-case signal that the class extends beyond the string-shaped subclass.
  Caveats: Support degrades to the extent the cluster contains semantic mislabels; grep yield vs. sampled semantic read (the queued empirical test) is the direct measure of that boundary. Preliminary search — the citation-integrity NLP literature is moving quickly.
  Recommendation: PARTIALLY-SUPPORTED
