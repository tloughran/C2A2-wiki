SEARCH-FOR-PRESUMPTION-1053:
  Date searched: 2026-09-21
  Original item: PRESUMPTION-1053
  Original statement: Measurement instruments that are also members of the measured population
    systematically distort their own series, and the estate has not enumerated which of its registers
    are both.

  **Execution note (recorded for honesty, not buried):** this run of 15a and 15b was executed by a
  single scheduled process (`c2a2-lit-search-pipeline`, 2026-09-21). The two directions were run as
  separately-framed query sets and the FOR files were written before any AGAINST query was issued, but
  the strict independence the spec assumes (two processes, neither seeing the other) was NOT achieved.
  Read the strength ratings with that caveat.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-1053
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Generalised three same-day, independently-reached instrument-contamination findings.
      15a: Searched for supporting literature on reflexive measurement and self-inclusion in metrics.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Michelson, J. "Reflexive Measurement." (PhilArchive, MICRM-4). — Develops measurement-as-
       intervention: the thesis that a measurement can causally affect the phenomenon it investigates,
       with Goodhart's Law named as the folk statement of it. This is the claim under test stated as a
       general principle of measurement theory.
    2. Goodhart, C. 1975 (Goodhart's Law, as formalised in later literature). — "When a measure becomes
       a target, it ceases to be a good measure." Originating case: monetary aggregates whose stable
       relationship to inflation broke down *once central banks adopted them as targets*. The canonical
       demonstration that a series distorts when the measured system acts on the measurement.
    3. Fire, M. & Guestrin, C. 2019. "Over-optimization of academic publishing metrics: observing
       Goodhart's Law in action." *GigaScience* (PMC6541803; arXiv:1809.07841). — Closest domain
       analogue available: a knowledge-production system whose own output counts are its performance
       metrics. Documents measurable distortion of the publication record over a century of data.
    4. Thomas, R. & Uminsky, D. 2020. "The Problem with Metrics is a Fundamental Problem for AI."
       arXiv:2002.08512. — Argues metric-driven optimisation in AI systems reliably diverges from the
       latent quality the metric proxied, because agents shift toward the cheapest metric-moving
       intervention. Supplies the mechanism for self-inclusion: the instrument's own activity is the
       cheapest available metric-moving intervention.

  Strength of support: Strong

  Summary: Reflexive measurement is a named, theorised and empirically documented phenomenon across
    measurement theory, economics, scientometrics and ML evaluation, and the documented cases include
    the one nearest to C2A2's situation — a scholarly-output system scored on its own output counts.
    The general claim (self-including instruments distort their own series) is as well supported as
    claims of this kind get. The *second* half of the presumption — that the estate has not enumerated
    which registers are both instrument and member — is an in-house factual claim on which no
    literature bears; it is an enumeration task, and it is cheap.

  Caveats: The literature's paradigm case is distortion driven by *incentive* — an agent that benefits
    from moving the metric. C2A2's registers have no incentive; contamination there would be mechanical
    (an agent's own run-notes entering the corpus it counts), which is arguably a milder and more
    tractable failure than the Goodhart case, and possibly correctable by a filter rather than a redesign.
    Scope note: comprehensive on the principle, silent on the estate's particulars.

  Recommendation: SUPPORTED
