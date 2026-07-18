SEARCH-AGAINST-PRESUMPTION-460:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-460
  Original statement: "Capture is binary and final — a source already in prs_triplets.md needs no re-examination even after new context (e.g., a paradigm-boundary lens) changes what in it matters."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-460
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference (unstated presumption, MEDIUM, from 2026-07-08 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. AHRQ Evidence-based Practice Center Program. "Living Systematic Reviews: Practical Considerations." NCBI Bookshelf NBK579073. — Directly poses and answers the governing methodological question: when review criteria change, teams must decide whether to apply new criteria retrospectively and reconsider previously excluded/processed studies; treating prior screening decisions as final under changed criteria is flagged as a transparency and validity problem, with modified PRISMA flows recommended to track re-screening.
    2. "Methodological challenges for living systematic reviews conducted during the COVID-19 pandemic: A concept paper." 2021. PMC8435072. — Documents that as review questions and criteria evolve, previously screened corpora require re-examination; criteria drift without re-screening produces a corpus whose early and late members were selected by different rules — an inconsistency, not an archive.
    3. Saldaña, J. "The Coding Manual for Qualitative Researchers." SAGE. — Qualitative-methods canon: coding is iterative; when the coding frame (lens) changes, earlier data must be re-coded under the revised frame. First-pass extraction under an old frame is explicitly NOT treated as final.
    4. Glaser, B., Strauss, A., 1967. "The Discovery of Grounded Theory." (constant comparative method). — Foundational method built on re-comparing previously analyzed data against newly emerged categories; "what in a source matters" is defined relative to the current category system, and the method exists because that system changes.

  Strength of challenge: Strong

  Summary: Both research traditions that professionally manage "captured" corpora — evidence synthesis and qualitative analysis — reject capture-finality when the analytical lens changes. Their shared reasoning maps exactly onto prs_triplets.md: extraction is not a property of the source alone but of (source × lens), so a new lens (the paradigm-boundary lens) redefines what counts as signal in every already-captured source. A source processed under lens v1 and marked done is done only with respect to v1; treating the DONE flag as lens-independent quietly converts the corpus into a mixture of extraction regimes, with the oldest sources contributing the least under the current framework — an invisible recency bias in what the triplet store knows. Living-review methodology's specific finding is that this must be an explicit decision (retrospective re-screen vs prospective-only, documented), never a silent default.

  Specific risks: The paradigm-boundary lens sees only sources captured after its introduction — precisely the older, foundational sources most likely to contain paradigm-boundary material are the ones never re-read; conclusions drawn from prs_triplets.md inherit an undocumented lens-era stratification; the error compounds with each future lens change, and nothing in a binary DONE flag even records which lens version processed each source.

  Mitigations available: Version the lens and stamp each capture with its lens version (capture becomes (source, lens-version) → done, restoring re-examination triggers for free); on lens change, enqueue a retrospective re-extraction sweep — prioritized, not necessarily total (living-review practice allows prospective-only application IF explicitly decided and documented); cheap triage variant: re-scan only sources whose original extraction flagged near-boundary content.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Full retrospective re-processing on every lens change is O(corpus × lens-changes) — the living-review literature itself acknowledges this is often unaffordable and sanctions prospective-only application as a legitimate, documented choice. If the paradigm-boundary lens mostly reweights rather than redefines relevance, the marginal yield of re-reading old sources may be low, and the raw sources remain on disk: capture-finality in prs_triplets.md loses an index entry, not the underlying data, so any specific source can still be re-examined on demand.
    What would need to be true for C2A2 to be safe: The decision to apply new lenses prospectively-only must be explicit and recorded (not an unexamined default — which is exactly what 14b flagged); raw sources must remain retrievable for on-demand re-extraction; lens changes must be rare or mostly reweighting; the lens version in force at each capture must be reconstructible.
    How to test: Sample 10-15 pre-lens-change sources from prs_triplets.md and re-extract them under the paradigm-boundary lens; the yield of new, material triplets directly measures what capture-finality is costing. Near-zero yield vindicates the presumption; substantial yield mandates the re-sweep.
