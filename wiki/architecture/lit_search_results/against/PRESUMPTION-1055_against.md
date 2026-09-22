SEARCH-AGAINST-PRESUMPTION-1055:
  Date searched: 2026-09-21
  Original item: PRESUMPTION-1055
  Original statement: Mandated disclosure without a resolution path converts into ritual -- repeat-
    disclosure counts rise while fix rates do not.

  **Execution note:** 15a and 15b were executed by a single scheduled process on 2026-09-21. Query sets
  were framed separately and the FOR files were written before any AGAINST query was issued, but the
  two-process independence the spec assumes was NOT achieved. Weight the strength ratings accordingly.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-1055
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Counted repeat-disclosure streaks across today's runs.
      15b: Searched for evidence that disclosure without immediate action still improves outcomes.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. NASA/FAA Aviation Safety Reporting System (ASRS), est. 1976 (ASRS programme documentation;
       Wikipedia, *Aviation Safety Reporting System*; FAA Aviation Voluntary Reporting Programs). —
       The counterexample the item most needs to face. ASRS is a confidential, non-punitive reporting
       system in which the overwhelming majority of individual reports produce *no* fix traceable to
       that report. Its documented value is the identification of *thousands of latent safety issues*
       in aggregate and its effect on industry-wide safety culture. Fifty years of disclosure with no
       per-report resolution path, and it is the most-cited success in safety reporting.
    2. "The dynamics between voluntary safety reporting and commercial aviation accidents," *Safety
       Science* (ScienceDirect S0925753521001958). — Studies the relationship at system level rather
       than per-report, which is the methodological point: a per-report fix-rate metric would have
       scored ASRS as ritual.
    3. Just-culture reporting literature (as summarised in ASRS/FAA programme materials). —
       Organisations with strong reporting cultures gather more data on small precursor events; the
       returns are in aggregation and trend detection, not in per-report remediation.

  Strength of challenge: Strong

  Summary: The presumption's causal story (no resolution path -> ritualisation) is well attested for
    *alerts addressed to an operator expected to act now*. It is contradicted for *reports addressed to
    a register expected to be analysed later*. ASRS is the canonical case of the second kind, and the
    metric 14b proposes — repeat-disclosure count against fix rate — is precisely the metric that
    mis-scores it. C2A2's disclosures are much closer to ASRS reports than to ICU alarms: low-volume,
    human-authored, addressed to a durable register, and read by one person on a delay.

  Specific risks: If repeat disclosure is judged ritual and suppressed, the estate loses the aggregate
    signal that makes repeat disclosure worth anything. The repetition *is* the data: a defect declared
    on twenty-one consecutive days is a stronger finding than the same defect declared once, and a rule
    that penalises the streak would delete that finding. Note that the streak in question here is the
    one that surfaced ASSUMPTION-1568 and the pipeline stall itself.

  Mitigations available: Score disclosure at the aggregate level, not per report: count *distinct*
    unresolved defects and their age, not disclosure events. Keep the disclosure obligation; add a
    promotion rule (a defect disclosed N times without action is escalated to the human queue rather
    than suppressed). That preserves the ASRS property while answering 14b's real worry.

  STEELMAN:
    Item: PRESUMPTION-1055
    Strongest counterargument: The item names a real risk with the wrong remedy implied. Ritualisation
      is a hazard of disclosure, but the fix is never fewer disclosures — ASRS demonstrates that fifty
      years of mostly-unactioned reports can be the single most valuable safety instrument in an
      industry, provided something *aggregates* them. C2A2's defect is not that it discloses without
      fixing; it is that nothing aggregates. The repeat-disclosure streak 14b counted is the aggregation
      working by hand, once, and it produced the most important finding in the 2026-09-20 intake.
    What would need to be true for C2A2 to be safe: that some process reads disclosure streaks and
      escalates on length. Today that process is a human noticing.
    How to test: count distinct defects disclosed 3+ times without a disposition, and their median age.
      If that list is short, disclosure is working; if it is long and old, the failure is aggregation,
      not ritual.

  Recommendation: CHALLENGED
