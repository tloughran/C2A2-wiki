SEARCH-AGAINST-ASSUMPTION-482:
  Date searched: 2026-07-21
  Original item: ASSUMPTION-482
  Original statement: The pipeline's binding constraint is not evidence but measurement nobody has taken; 11 of 14 dispositions turn on discriminating tests reducing to ~6 measurements, 5 under an hour each.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-482
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-20 15c disposition run, exact quote
      15b: Searched for challenging literature (constraint misidentification, diagnosis-vs-remediation share of MTTR, estimation optimism)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  Search scope: Moderate — three clusters (Theory of Constraints on policy vs physical constraints; MTTR phase decomposition; planning fallacy). Searched deliberately for evidence that the constraint is something other than missing measurement.

  Sources:
    1. Theory of Constraints, standard exposition (Wikipedia; Six Sigma Study Guide; Smartsheet; retrieved 2026-07-21). The framework the item invokes states that most constraints are NOT physical but arise from company policy and practice, and that policy constraints are harder to identify and more often mismanaged than physical ones. In knowledge work the constraint is typically a policy — approval process, batch size, meeting load — not a missing input. TOC therefore does not license "the missing thing is a measurement" as the default reading; it warns against exactly that inference.
    2. MTTR phase decomposition (Dynatrace, "What is MTTR?"; Selector, "Complete Guide to MTTR"; retrieved 2026-07-21). MTTR decomposes into detection, diagnosis and remediation, and detection — not diagnosis — is described as the largest controllable factor. Tracking MTTD and MTTR separately is the recommended way to establish whether the bottleneck is visibility or operational delay. The item asserts the visibility answer without having run the separation.
    3. Kahneman and Tversky's planning fallacy, as summarised in Wikipedia "Planning fallacy" and The Decision Lab (retrieved 2026-07-21); the 1994 finding that ~70% of participants overran their own predicted deadlines, sometimes by a factor of two. The "5 under an hour each" figure is an inside-view estimate produced by the party proposing the work, which is the exact configuration the literature identifies as most biased.

  Strength of challenge: Moderate
  Summary: The observation that eleven of fourteen dispositions turn on unmade measurements is not contradicted and is probably true as stated. What is challenged is the leap from that observation to "measurement is the binding constraint." Theory of Constraints — the framework the item's own search targets invoke — holds that in knowledge work the constraint is usually a policy rather than a missing input, and that policy constraints are the ones organisations habitually fail to identify. The incident-management literature makes the same structural point in a different vocabulary: you establish whether the bottleneck is detection or response by measuring both, not by asserting one. And the sub-hour cost estimates are inside-view self-estimates of the kind that overrun by roughly a factor of two. PRESUMPTION-513 offers the competing diagnosis and the TOC literature is, on balance, friendlier to 513 than to 482 — but see the note below: the two are not exhaustive.
  Specific risks: If measurement is not the binding constraint, taking the six measurements produces six more findings into a channel that already does not consume findings, and the pipeline records the effort as progress. Second risk: the sub-hour estimates set an expectation that, if overrun twofold, converts a "cheap" recommendation into a half-day of unbudgeted work and discredits the next cheap recommendation.
  Mitigations available: Do not treat 482 and 513 as exhaustive alternatives — the implementation-science sources retrieved for 513 state that solution-specific information and resource capacity are jointly necessary, so both constraints can bind at once. Timebox and record actuals for the first measurement taken and compare against the sub-hour estimate before committing to the remaining four; this is the outside-view correction and it costs nothing extra. Before declaring measurement the constraint, apply the MTTD/MTTR separation: count, over the last 30 days, how many findings were made versus how many produced an attributable change.
  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-482
    Strongest counterargument: The item invokes Theory of Constraints and then reaches the conclusion TOC most often warns against. TOC's central practical teaching is that in knowledge work the constraint is rarely a missing physical input and is usually a policy — an approval step, a batch size, an authority boundary — and that policy constraints are the ones most frequently misidentified because they are invisible to the people inside them. "Nobody has taken the measurement" is a description of a symptom that is equally consistent with the measurement being unavailable and with the measurement being available, cheap, known, and not taken because nothing in the system requires anyone to take it. Fifteen days of identified, cheap, unexecuted actions is direct evidence for the second reading. Separately, the "five under an hour each" figure is an inside-view estimate produced by the agent proposing the work, and the estimation literature is unambiguous that such estimates cluster near best-case and overrun by roughly a factor of two, which matters because the entire persuasive force of the recommendation rests on its cheapness.
    What would need to be true for C2A2 to be safe: That the measurements, once available, would actually be consumed — i.e. that there exists a step which takes a measurement result and changes an agent's behaviour. Nothing retrieved establishes such a step exists, and PRESUMPTION-506 asserts it does not.
    How to test: Execute exactly one of the five measurements and record two numbers: elapsed wall-clock time against the sub-hour estimate, and whether any disposition changed within seven days as a result. If elapsed time is within estimate and a disposition changed, 482 is vindicated. If the measurement is taken and no disposition changes, the constraint was never enumeration.
