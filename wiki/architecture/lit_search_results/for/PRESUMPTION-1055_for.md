SEARCH-FOR-PRESUMPTION-1055:
  Date searched: 2026-09-21
  Original item: PRESUMPTION-1055
  Original statement: Mandated disclosure without a resolution path converts into ritual -- repeat-
    disclosure counts rise while fix rates do not.

  **Execution note (recorded for honesty, not buried):** this run of 15a and 15b was executed by a
  single scheduled process (`c2a2-lit-search-pipeline`, 2026-09-21). The two directions were run as
  separately-framed query sets and the FOR files were written before any AGAINST query was issued, but
  the strict independence the spec assumes (two processes, neither seeing the other) was NOT achieved.
  Read the strength ratings with that caveat.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-1055
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Counted repeat-disclosure streaks across today's runs.
      15a: Searched for supporting literature on alert fatigue and unactioned reporting regimes.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Alarm fatigue synthesis, AHRQ *Making Healthcare Safer III*, ch. on Alarm Fatigue
       (NCBI Bookshelf NBK555522); and the alarm-fatigue review literature generally. — The best-
       evidenced case of the mechanism: nonactionable alarms are alarms that fire correctly but signify
       an event "that is not clinically significant and/or requires no additional intervention," and
       their accumulation degrades response to the actionable ones. Disclosure volume up, action flat.
    2. Security-operations alert-fatigue literature (SOC overload surveys; industry figures of 25-30% of
       alerts going uninvestigated). — Documents the response side: analysts ignore or silence alerts to
       cope, producing blind spots. "Each repeated alert lowers perceived urgency, and alerts that once
       triggered immediate investigation begin to feel routine" — the ritualisation claim stated as an
       observed effect.
    3. Observability/monitoring practice literature on non-actionable alerting (LogicMonitor and
       equivalents). — Converges on the design rule that an alert without a defined response path
       should not be an alert; the rule exists because the failure it prevents is well attested.

  Strength of support: Strong

  Summary: Across clinical alarms, security operations and infrastructure monitoring, the same finding
    recurs: signals that carry no resolution path lose force with repetition, and the decay is
    behavioural rather than technical. Two of the three literatures report quantitative versions —
    proportion of alerts uninvestigated, correlation between alarm burden and response delay — which is
    the *shape* of measurement 14b proposed (repeat-disclosure count vs. fix rate). The presumption is
    an instance of a general, well-replicated pattern.

  Caveats: (1) The nearest literatures concern *high-volume machine-generated* alerts; C2A2's
    disclosures are low-volume and human-authored, and the fatigue mechanism is partly a function of
    volume. (2) The literature's disclosures are addressed to an operator with a fix at hand; C2A2's are
    addressed to a register and a single human reader, which may make them more like mandated regulatory
    disclosure than like an alarm — a literature (securities/consumer disclosure) this search did not
    reach. Preliminary search — the disclosure-regulation literature is the named gap.

  Recommendation: SUPPORTED
