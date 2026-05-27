SEARCH-FOR-ASSUMPTION-214:
  Date searched: 2026-05-23
  Original item: ASSUMPTION-214
  Original statement: "A single self-contained handoff document can carry an experiment's full context into a cold-start chat, making the experiment portable across sessions."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-214
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the two-summa scoping work: the experiment was packaged as one cold-start brief, assuming the brief carries full context.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Knuth (1984) "Literate Programming"; Gentleman & Temple Lang (2007) "Statistical analyses and reproducible research" (research compendium). — A sufficiently complete written artifact can bundle code+context so others reproduce the work.
    2. Donoho et al. (2009) "Reproducible Research in Computational Harmonic Analysis." — Self-contained, documented bundles are an established route to portability of computational experiments.
    3. Design-doc / RFC practice (Amazon 6-page narrative memo; Google design docs). — Industry precedent that a single narrative document can transfer a project's intent to readers without live context.

  Strength of support: Moderate

  Summary: There is a real lineage for "one complete document carries the work": literate programming, the research-compendium model, and reproducible-research practice all show that a well-constructed self-contained artifact can transfer enough to reproduce an experiment. Design-doc/RFC culture extends this to intent transfer across people who were not in the room. Support is partial because every one of these traditions pairs the claim with explicit completeness requirements and known failure modes.

  Caveats: Support holds only to the degree the brief is genuinely complete; the literature consistently notes that "complete enough" is the hard part (see PRESUMPTION-232 / tacit knowledge). The precedents also assume a competent reader who shares background — a cold-start LLM chat may not.

  Recommendation: PARTIALLY-SUPPORTED
