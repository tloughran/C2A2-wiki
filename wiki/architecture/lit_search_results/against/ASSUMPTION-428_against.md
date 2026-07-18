SEARCH-AGAINST-ASSUMPTION-428:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-428
  Original statement: "Deferring the 117-item 15d refresh backlog is acceptable so long as the deferral is surfaced and a remedy recommended ('deferred and surfaced, not silent')."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-428
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extraction (stated assumption, MEDIUM, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Vaughan, D., 1996. "The Challenger Launch Decision." University of Chicago Press. — Foundational account of normalization of deviance: the O-ring anomaly was repeatedly surfaced, documented, and waived; surfacing without action became the mechanism of the disaster, not a defense against it.
    2. 2022. "A qualitative systematic review on the application of the normalization of deviance phenomenon within high-risk industries." Journal of Safety Research (ScienceDirect S0022437522001827). — Systematic review across high-risk industries finding a recurring pattern: deviations that are visible and acknowledged but repeatedly tolerated become the accepted baseline, with a long incubation period of "misinterpreted, ignored or missed" warnings before failure.
    3. NTSB investigation of the 2009 Washington DC Metro (Fort Totten) collision (summarized in Wikipedia, "Alarm fatigue"). — ~8,000 surfaced track-circuit alerts per week desensitized dispatchers; the warning channel existed and fired continuously, and its very persistence neutralized it.
    4. IBM / Atlassian incident-management literature on alert fatigue (ibm.com/think/topics/alert-fatigue; atlassian.com/incident-management/on-call/alert-fatigue). — Surfaced-but-unactioned alerts degrade response to ALL alerts; repeated exposure to a standing warning normalizes it as routine.

  Strength of challenge: Strong

  Summary: The safety-science literature directly challenges the premise that surfacing a deferral discharges the risk. Normalization-of-deviance research shows that repeatedly surfaced, repeatedly waived anomalies are the classic precursor pattern to failure: each uneventful deferral becomes evidence that deferral is safe. Alert-fatigue research adds a second mechanism: a standing warning that appears every cycle ("117-item backlog, remedy recommended") rapidly loses signal value and trains readers to skim past it — and past neighboring warnings. "Deferred and surfaced, not silent" is better than silent, but the literature says surfacing decays to functional silence within a few repetitions unless it is coupled to an escalation or forcing function.

  Specific risks: The 15d refresh backlog quietly becomes permanent infrastructure debt; stale items are consumed downstream as if fresh; the recurring backlog banner desensitizes the human reviewer to other surfaced warnings in the same reports (cross-contaminating alert channels); when a stale item finally causes a visible error, the incubation-period pattern means it will look "sudden" despite months of surfaced warnings.

  Mitigations available: Attach an escalation ladder to the deferral (N consecutive deferrals → forced agenda item / blocking status); put a hard age or size cap on the backlog beyond which the pipeline refuses to defer further; make the surfaced warning state-changing rather than static (show growth rate and age of oldest item, not just existence); schedule a one-time burn-down rather than treating deferral as steady-state.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Deferral with surfacing is standard, rational triage under constrained capacity — every mature engineering organization runs a known-issues backlog, and the alternative (blocking on 117 refreshes) has its own failure modes. The 15d refresh items are staleness risks, not safety-critical anomalies; the cost of a stale wiki entry is low and reversible, unlike O-rings. Surfacing plus a recommended remedy preserves the option to act and keeps the decision with the human, which is the correct division of authority.
    What would need to be true for C2A2 to be safe: The cost of item staleness must genuinely be low and reversible; the surfaced warning must demonstrably still be read (evidence: occasional action taken on it); backlog growth must be bounded rather than monotone; deferral must be a decision renewed on evidence, not a default.
    How to test: Track whether any surfaced deferral in the last N reports produced action; measure backlog age/size trend. If the warning has fired repeatedly with zero resulting action and the backlog is growing, the normalization mechanism is already operating.
