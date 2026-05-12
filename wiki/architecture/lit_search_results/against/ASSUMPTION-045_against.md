SEARCH-AGAINST-ASSUMPTION-045:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-045
  Original statement: "'Other thinkers well-covered / no primary-source material inside 60-day window' is a valid per-thinker coverage claim"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-045
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from briefing-layer coverage-freshness claim
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Per-author publication-rate variance (Lotka 1926 productivity-distribution; Sinatra et al. 2016 "Quantifying the evolution of individual scientific impact"): author-level publication rates are highly skewed; a uniform 60-day window under-fits prolific authors and over-fits infrequent ones. Fixed-window heuristics are a named anti-pattern in bibliometrics.
    2. Coverage-claim validation literature (Salo 2018 research-support audits; Newman 2014 "Data-driven documentation"): "well-covered" is a compound claim that includes depth as well as recency; a no-recent-material check does not establish coverage, only freshness.
    3. Selection-on-observable literature (Hernán & Robins 2020): if the 60-day window is applied on a single data source, coverage-well-covered-elsewhere is confounded with data-source-blindspot. Cross-source validation is required to license the claim.
    4. Null-as-coverage anti-pattern: the form of the claim ("no material inside window → well-covered") mirrors PRESUMPTION-042 and PRESUMPTION-048 (null interpreted as success). This is the same structural gap surfaced at the coverage-audit layer.
    5. Gamability of freshness-based gating (search-engine SEO literature; recommender-systems gaming research): authors can drift in and out of the 60-day window without changing their substantive coverage status, making the heuristic noise-sensitive.

  Strength of challenge: Moderate

  Summary: The claim's *shape* is conventional, but two specific weaknesses surface in literature: (a) the single-window assumption under-fits per-author variance; (b) "well-covered" is conflated with "no-new-material-inside-window," which is a null-as-success pattern matching the SELF-AWARENESS-META cluster's known gap. Neither makes the heuristic *wrong*; both warrant explicit calibration and explicit qualification of what "well-covered" means.

  Specific risks: (a) Friston-class risk — a prolific author can emit material *inside* the window that the system misses due to source-coverage blindspots; (b) the inverse: a thinker can go quiet for coverage-neutral reasons (sabbatical, slow year) and be *dropped* from active coverage tracking incorrectly; (c) extends the null-as-success cluster to the coverage-audit layer.

  Mitigations available:
    - Replace fixed 60-day window with per-thinker adaptive window based on observed publication rate.
    - Separate "coverage claim" from "freshness claim" — the briefing can say "no new material in 60 days" without asserting "well-covered."
    - Add cross-source validation (multiple data sources) before declaring coverage adequate.
    - Cross-check with PRS triplet state (if PRS recently changed for a thinker, coverage deserves a fresh look regardless of primary-source window).

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-045
    Strongest counterargument: The 60-day window is an unaudited hyperparameter masquerading as a policy. The literature on per-author variance strongly predicts that a single window under-fits prolific authors (Friston-class) and over-fits infrequent ones. Treating "no new material" as equivalent to "well-covered" imports the same null-as-success blind spot the system has already flagged as a cluster. The briefing-layer claim collapses two distinct claims (freshness and coverage-adequacy) into one unaudited shorthand.
    What would need to be true for C2A2 to be safe: Either (a) disaggregate the two claims and report them separately; (b) derive per-thinker windows from observed publication rates; (c) require cross-source coverage validation before the "well-covered" label is emitted.
    How to test: Run per-thinker coverage audit against a primary-source corpus for 4+ thinkers; measure false-positive rate of "well-covered" label on thinkers that actually had recent primary-source material outside the checked sources.
