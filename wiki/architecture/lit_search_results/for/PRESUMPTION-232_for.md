SEARCH-FOR-PRESUMPTION-232:
  Date searched: 2026-05-23
  Original item: PRESUMPTION-232
  Original statement: "Experiment portability presumes a cold-start chat shares enough tacit context that nothing load-bearing is lost when the only carrier is a single brief."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-232
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred as the unstated twin of ASSUMPTION-214 — that a single brief loses nothing load-bearing on a cold start.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Requirements/specification practice (IEEE 830 SRS). — Well-formed specifications are intended to be a sufficient, standalone carrier of intent; the discipline exists precisely to externalize context.
    2. Reproducible-research compendia (Donoho 2009; Gentleman & Temple Lang 2007). — Documented self-contained bundles routinely transfer enough to reproduce results.
    3. Prompt/context engineering: a thorough system/context prompt can reconstitute task framing for an LLM with no prior turns.

  Strength of support: Weak-Moderate

  Summary: There is precedent that a sufficiently complete written carrier transfers task intent without prior shared state — that is the entire point of specifications and research compendia. For LLM cold starts specifically, a rich context prompt can reconstitute framing. Support is weak-moderate because all these traditions concede that completeness is the binding constraint and that tacit/background knowledge routinely leaks out of written carriers (the core of the 15b challenge).

  Caveats: "Enough" is empirical and brief-specific; the supportive case cannot certify a particular brief without testing it on a real cold start.

  Recommendation: PARTIALLY-SUPPORTED
