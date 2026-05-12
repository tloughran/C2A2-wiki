SEARCH-FOR-ASSUMPTION-062:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-062
  Original statement: "A weak circuit breaker beats none; pick an approximation threshold now and tune later."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-062
    Item type: ASSUMPTION (stated; methodological)
    Transform at each step:
      14a: Extracted from morning chat scrape — Chat-side Claude's methodological principle for DECISION-024
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Circuit-breaker design literature (Nygard 2007 "Release It!"; Netflix Hystrix 2012-2017 documentation): any circuit breaker is valuable; the threshold is a tunable parameter. Nygard explicitly endorses "ship a conservative default, instrument, tune" over "block on finding the optimal threshold."
    2. Worse-is-better literature (Gabriel 1991 "The Rise of Worse-is-Better"): simplicity and shippability beat theoretical optimality. Shipping a weak circuit breaker and iterating is preferred to blocking on optimal design.
    3. Satisficing literature (Simon 1956, 1979 bounded-rationality; "good enough" decision-making): under bounded information, satisficing (pick a workable solution, iterate) outperforms optimizing (find the best solution, block until found). Threshold selection under uncertainty falls directly in this space.
    4. Ship-and-iterate literature (Ries 2011 "The Lean Startup"; Agile practice): approximation-first + instrumentation beats optimization-first + paralysis. The principle is one of the most well-established in modern software engineering.
    5. SRE empirical-tuning practice (Beyer 2016 SRE on "what is a reasonable SLO" — "pick one and measure"): concrete thresholds matter less than the discipline of having a threshold at all. The empirical tuning happens after instrumentation, which requires a threshold to measure against.
    6. C2A2-internal applicability (OPEN-033 specialist task turn-cap; OPEN-032 transience-threshold generalization): the principle generalizes beyond DECISION-024 to threshold decisions across OPERATIONAL-DRIFT channels, staleness criteria, alert policies.

  Strength of support: Strong

  Summary: The methodological principle — "weak circuit breaker > none; approximate now, tune later" — is one of the best-established in SRE, agile software engineering, and bounded-rationality literature. Nygard's "Release It!" is the canonical text; Gabriel's "Worse-is-Better," Simon's satisficing, and Ries's Lean Startup all converge on the same conclusion. Concrete thresholds matter less than having a threshold at all; instrumentation + iteration is the correct path. The principle applies directly to DECISION-024 (turn-cap = 20) and generalizes to OPEN-032/033 and staleness/alert thresholds across C2A2.

  Caveats: (a) "Weak" must still be "conservative" — a threshold set too aggressively can produce false-positive interrupts that degrade the system (classic circuit-breaker tuning literature warns of this); (b) the principle assumes instrumentation is available for tuning — without measurement, "tune later" becomes "never tune"; (c) generalizing to all threshold decisions is appropriate but requires recognizing that some thresholds (financial, safety-critical) warrant more rigor before shipping.

  Recommendation: SUPPORTED (strong support across SRE, satisficing, ship-and-iterate, and worse-is-better literature; conditional on conservative initial threshold + instrumentation)
