SEARCH-FOR-ASSUMPTION-1595:
  Date searched: 2026-09-22
  Original item: ASSUMPTION-1595
  Original statement: A guideline breached by every instance of a task class, always for the same
    stated reason, no longer distinguishes necessary cost from thrash.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-1595
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Read five same-day declared budget breaches as a population rather than singly.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Cvach, M. (2012). "Monitor Alarm Fatigue: An Integrative Review." Biomedical Instrumentation
       & Technology, 46(4), 268-277. PubMed 22839984. — Clinical-monitoring literature establishing
       that a threshold triggered on a high proportion of instances (poor positive predictive value,
       high false-alarm rate) is a recognized technology hazard, not a signal of genuine danger each
       time; the field's response is to recalibrate the threshold rather than trust every alarm.
       Directly analogous to "a guideline breached every time no longer distinguishes."
    2. Goodhart, C. (1975, unpublished Reserve Bank of Australia address); popularized as Goodhart's
       Law — "When a measure becomes a target, it ceases to be a good measure." Summarized well in
       Wikipedia's "Goodhart's law" entry and Splunk/FourWeekMBA explainers. — Theoretical grounding
       for the claim: a fixed limit that is uniformly and predictably breached for a stated reason has
       stopped functioning as a discriminating measure and instead describes normal operation.
    3. [unverified — from background knowledge, not confirmed by this search] Industrial condition-
       monitoring practitioner literature (e.g. Reliamag, "Stop Setting Condition Monitoring Alarm
       Thresholds and Forgetting Them") — static thresholds set once and never revisited against
       actual operating baselines are a known cause of chronic, uninformative breaches; treat as
       practitioner-grade corroboration, not peer-reviewed.

  Strength of support: Moderate

  Summary: The claim has a single limb and it maps cleanly onto two well-established literatures:
    alarm fatigue in safety-critical monitoring (a threshold breached constantly, for a stable reason,
    is evidence of miscalibration rather than of repeated genuine emergencies) and Goodhart's Law
    (a measure that is always exceeded in the same way has stopped discriminating signal from routine
    operation). Both give strong theoretical and empirical grounding for treating a uniformly-breached
    guideline as a calibration problem rather than as N independent instances of necessary overage.

  Caveats: The alarm-fatigue literature is domain-specific to clinical/industrial monitoring, and the
    Goodhart's Law literature is domain-general almost to the point of being a truism — neither
    directly studies "declared budget breaches in an agentic task pipeline." The inferential leap from
    "alarms" or "targets" to "declared, stated-reason budget breaches in software agents" is analogical,
    not a direct empirical match. No source was found addressing this exact scenario (LLM/agent task
    budgets).

  Search scope: Preliminary — three targeted searches across alarm-fatigue/threshold-calibration and
    Goodhart's-law/quota literatures. Broader search into software-engineering-specific "budget
    guideline" or SLO/error-budget literature (e.g. SRE error-budget practice) recommended for a fuller
    picture.

  Recommendation: SUPPORTED
