SEARCH-AGAINST-ASSUMPTION-062:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-062
  Original statement: "A weak circuit breaker beats none; pick an approximation threshold now and tune later."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-062
    Item type: ASSUMPTION (stated; methodological)
    Transform at each step:
      14a: Extracted from morning chat scrape
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND (weak caveats only)

  Challenging evidence found: Weak

  Sources:
    1. Premature optimization literature (Knuth 1974 "Structured Programming with go to Statements"; applied to thresholds): premature tuning of thresholds can embed incorrect assumptions that are difficult to remove later. A poorly-chosen weak threshold can become load-bearing.
    2. Anchoring-bias literature (Tversky & Kahneman 1974): initial approximations can anchor subsequent tuning, even when better data arrives. "Tune later" assumes tuning actually happens — anchoring often prevents it.
    3. Threshold-proliferation literature (SRE on "alert fatigue"; Beyer 2016): shipping multiple weak thresholds creates a jungle that collectively degrades signal quality. The "weak beats none" principle, applied broadly, can produce a threshold-jungle that is worse than either none or well-tuned.
    4. Safety-critical exceptions (aerospace software engineering; medical-device software; financial-control systems): for safety/financial/regulatory-critical thresholds, ship-and-iterate is not acceptable; the initial threshold must be defensible before shipping. Generalizing ASSUMPTION-062 to all threshold decisions is wrong.

  Strength of challenge: Weak

  Summary: The challenges are real but narrow. Anchoring bias is a genuine concern — "tune later" is often "never tune" without instrumentation and a tuning cadence. Threshold-proliferation is a genuine concern — applied indiscriminately, the principle can produce a jungle. Safety/financial-critical exceptions are real. But for the specific application (DECISION-024 specialist-task turn-cap = 20) and the C2A2 domain generally, none of these rise to strong challenge. The principle is correct with three operational conditions: (a) conservative initial threshold, (b) instrumentation + tuning cadence established at ship time, (c) exclude safety/financial-critical categories.

  Specific risks: (a) Anchoring — turn-cap = 20 may stick even if data says 30 or 10; (b) threshold-jungle — generalizing the principle broadly may produce alert fatigue; (c) over-application — using the principle for all threshold decisions, including those that warrant rigor.

  Mitigations available: (a) Pair weak-threshold-ship with an instrumentation + tuning-cadence commitment; (b) limit the principle to non-safety-critical thresholds; (c) track all thresholds shipped under this principle in a "tune-me" register so they do not accumulate as load-bearing defaults.

  Recommendation: NO-CHALLENGE-FOUND on the core principle for the C2A2 domain; weak cautions on tuning cadence, threshold proliferation, and safety-critical exclusions.

  STEELMAN:
    Item: ASSUMPTION-062
    Strongest counterargument: "Weak beats none, tune later" only works if tuning actually happens. Anchoring bias (Tversky & Kahneman) predicts that initial approximations stick; the "tune later" commitment is not self-enforcing. Applied broadly without an instrumentation + cadence commitment, the principle produces a threshold-jungle that degrades signal quality (alert-fatigue literature). And for safety/financial/regulatory-critical categories, ship-and-iterate is flatly wrong — those categories require defensible initial thresholds. The principle is correct for the right categories with the right operational pairing; without the pairing, it becomes an excuse for shipping sticky defaults that never get tuned.
    What would need to be true for C2A2 to be safe: Instrumentation + tuning cadence committed at ship time for each threshold under this principle; explicit scope boundary excluding safety/financial/regulatory thresholds; tune-me register for tracking.
    How to test: Audit thresholds shipped under this principle at 30-day, 90-day marks; measure fraction that got tuned vs. fraction that remained at initial approximation; compare false-positive/true-positive rates against target bands.
