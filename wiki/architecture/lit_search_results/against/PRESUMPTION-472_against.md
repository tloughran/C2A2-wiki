SEARCH-AGAINST-PRESUMPTION-472:
  Date searched: 2026-07-12
  Original item: PRESUMPTION-472
  Original statement: "Systematic citation mislabels are textually regular enough for batch grep — the error class is presumed string-shaped, though one observed instance is a gloss."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-472
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced by inference from 2026-07-11 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [arXiv:2606.08589, "Detection and Interpretability Analysis of Quotation Errors by Large Language Models." — Quotation/citation errors are treated in the current literature as a semantic detection task requiring full-text analysis of the cited source; the field moved to LLM/NLP methods precisely because the error class is NOT surface-regular.]
    2. [Sarol, M.J. et al., 2024. "Assessing citation integrity in biomedical publications: corpus annotation and NLP models." Bioinformatics/PMC11231046. — Citation-integrity error taxonomies are dominated by semantic classes (claim not supported by the cited source, misrepresentation of findings — i.e., glosses); measured citation inaccuracy rates of 20–26% in biomedical literature are mostly NOT string-detectable.]
    3. [Nightfall AI, "Regex vs AI-based Detection"; arXiv:2603.00311 (regex engine testing). — Pattern methods miss anything outside predefined surface forms and cannot see semantic wrongness that triggers no textual irregularity; this is the defining boundary of the method, not a tuning problem.]
  Strength of challenge: Strong
  Summary: The citation-integrity literature classifies mislabels/misattributions as predominantly semantic errors, detectable only by comparing the citing text against the cited content — the class of check grep cannot perform by construction. The presumption's own evidence base contains the refutation: the ONE instance actually inspected is a gloss, i.e., a member of the semantic subclass, yet the repair plan is keyed to the string-shaped subclass. Presuming string-shape from a sample whose only inspected member is not string-shaped inverts the available evidence.
  Specific risks: Batch grep repairs the easy subclass, OPEN-118 closes, and the semantic mislabels — the class the literature says is both more common and more damaging — persist under a "resolved" flag.
  Mitigations available: The queued test is exactly right: grep yield vs sampled semantic read on the same range; define "cluster closed" by the semantic residue rate, not grep exhaustion.

  STEELMAN:
    Item: PRESUMPTION-472
    Strongest counterargument: The error class was defined by the tool available rather than by the errors observed — the single inspected error is semantic, the planned detector is syntactic, and the literature's base rates say semantic citation errors outnumber mechanical ones. If the presumption stands, the system will measurably "fix" a cluster whose observed exemplar its fix cannot see.
    What would need to be true for C2A2 to be safe: The gloss instance is an outlier — established only by the sampled semantic read showing the residue class is negligible.
    How to test: Same day-range, two passes: grep yield vs sampled semantic read; residue rate decides.
  Recommendation: CHALLENGED
