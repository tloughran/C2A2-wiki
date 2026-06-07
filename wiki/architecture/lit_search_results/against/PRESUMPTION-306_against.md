SEARCH-AGAINST-PRESUMPTION-306:
  Date searched: 2026-06-06
  Original item: PRESUMPTION-306
  Original statement: [inferred] "Two verbs over one dataset" presumes the curated graph (156, CC-001...) and the cards directory (855, C0001...) are unifiable, despite measured near-total disjointness (0 id / 3 name / 5 host matches). P3 rests on a join that may be very sparse.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-306
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the presumption that two near-disjoint sets are unifiable.
      15b: Searched for when key disjointness signals distinct populations and for limits of fuzzy joins at low overlap.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Record-linkage theory (Fellegi-Sunter; Christen, "Data Matching"). — Probabilistic linkage requires discriminative, overlapping attributes to separate matches from non-matches; with near-zero observed overlap there is little signal, and the method's match probabilities collapse toward the non-match prior. Challenges the feasibility of recovering a dense join.
    2. Data Ladder / entity-resolution guidance. — "If used in isolation, fuzzy matching can be misleading; similar-looking values do not always represent the same entity, and aggressive thresholds significantly increase false-match rates." Direct warning against forcing a join from low overlap.
    3. Entity-resolution practice on distinct populations. — When two record sets share almost no keys, the parsimonious inference is often that they describe largely DIFFERENT populations, not that the join is hidden; forcing linkage manufactures false positives.

  Strength of challenge: Strong

  Summary: The measured 0 id / 3 name / 5 host overlap across 156x855 is, by record-linkage theory, near the floor of recoverable signal: probabilistic matching needs discriminative overlapping attributes, and with essentially none, fuzzy methods produce false matches rather than recovered truth. The honest reading is that the two sets may describe largely distinct populations — i.e., "two verbs over ONE dataset" may be false; it may be two datasets. Because P3's whole architecture rests on this join, a sparse-or-absent join is not a detail but a foundational risk. This is the strongest single challenge in the batch.

  Specific risks: P3 is built on a join that does not exist or is too sparse to be useful; aggressive fuzzy matching creates spurious community<->record links that corrupt the graph; the "one dataset" framing (ASSUMPTION-275/276) inherits a false premise.

  Mitigations available: Before building P3, run the actual record-linkage experiment and report precision/recall and estimated true-match count; pre-register a minimum join density that P3 requires; if density is below threshold, treat the two as distinct populations that ASSOCIATE rather than unify (couples PRESUMPTION-311).

  STEELMAN:
    Item: PRESUMPTION-306
    Strongest counterargument: Near-total key disjointness is itself the finding. Entity resolution is not magic; it recovers links where discriminative shared attributes exist, and 0/3/5 says they largely do not. Presuming unifiability anyway inverts the evidence: it treats the absence of a join as a problem to be engineered away rather than as data about the world. If you force the join with loose thresholds you will get links, but they will be artifacts of the threshold, not the territory — and an entire architecture (P3) would then rest on a manufactured join.
    What would need to be true for C2A2 to be safe: A real record-linkage pass recovers a join of usable density (well above chance) at acceptable precision — i.e., the curated communities and directory records genuinely overlap as populations.
    How to test: Run probabilistic linkage (e.g., Splink/Fellegi-Sunter) over name+host+fuzzy fields; report estimated true matches with precision/recall; compare against a null/shuffled baseline to confirm the matches exceed chance.

  Recommendation: CHALLENGED
