SEARCH-FOR-PRESUMPTION-467:
  Date searched: 2026-07-11
  Original item: PRESUMPTION-467
  Original statement: "Firing-health aggregates to system health — a scheduler watchdog may say 'all clear' while multi-day outcome-level outages stand."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-467
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced by inference from 2026-07-10 EOD daily run
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. [Computer Weekly (Rae, B.), "Watermelon SLAs — making sense of green and red alerts" (with HappySignals, "The Watermelon Effect in IT"). — The ITSM literature has a named, widely documented failure mode — "watermelon" reporting, green outside, red inside — in which operational metrics all pass while the user-experienced outcome fails. Direct precedent for a watchdog reporting all-clear across a multi-day outcome-level outage.]
    2. [Beyer, B. et al. (Google), 2016. "Site Reliability Engineering," Ch. 4 "Service Level Objectives" and Ch. 6 "Monitoring Distributed Systems" (sre.google). — Canonical prescription that SLIs must measure user-visible outcomes (symptoms), not internal mechanics (causes): "start by thinking about what your users care about, not what you can measure." Firing counts are an internal-cause metric; the SRE literature exists in large part because such metrics do not aggregate to system health.]
    3. [ALVAO, 2025-2026. "The Watermelon Effect in IT: Why SLAs Fail & How XLAs Fix It" (representative of the XLA/experience-level-agreement literature). — Documents empirically that organizations meeting 100% of component-level SLA targets still deliver failed outcomes, and that the remedy is outcome-level measurement added as a distinct tier — supporting 14b's inference that the presumption is a real, recognized hazard rather than a hypothetical.]
  Strength of support: Strong
  Summary: The inference 14b surfaced is one of the best-documented propositions in service management and reliability engineering. The gap between output metrics (tasks fired, SLAs met, probes green) and outcome metrics (users got the thing) has a name in two separate literatures: the watermelon effect in ITSM and symptom-vs-cause SLI design in SRE. Both bodies of work assert precisely that firing-health does NOT aggregate to system health, and both document real cases of green dashboards over standing outages. C2A2's own incident — scheduler watchdog green while OpenStory outcomes were down for days — is a textbook instance. The presumption, as an unexamined belief embedded in the watchdog design, is refuted by this literature; as a surfaced risk claim it is strongly supported.
  Caveats: Support runs to the surfaced inference (the hazard is real and general), not to any specific fix. Note the polarity carefully in downstream processing: literature SUPPORTS the claim "a watchdog may say all-clear during outcome outages" and therefore CONTRADICTS the embedded design belief "firing-health suffices." Search scope confidence is high; this literature is abundant and convergent.
  Recommendation: SUPPORTED
