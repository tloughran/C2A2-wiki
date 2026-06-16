SEARCH-FOR-PRESUMPTION-332:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-332
  Original statement: Current build capacity (attended cadence + agentic throughput + infrastructure) persists through the ~4-week ISME schedule, despite a same-day record of 7-day sync outage and a growing single-human review gate.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-332
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from ISME plan (2026-06-09 EOD run)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (literature supports the embedded risks, not the persistence assumption)
  Sources:
    1. Kahneman & Tversky, 1979 (planning fallacy); Buehler, Griffin & Ross, 1994. "Exploring the planning fallacy." JPSP. — Forecasts that assume current conditions persist and ignore one's own recorded disruption history are the canonical planning-fallacy pattern.
    2. Flyvbjerg, 2006. "From Nobel Prize to project management: Getting risks right." Project Management Journal (reference class forecasting). — The corrective the literature endorses: base the 4-week forecast on the observed reference class (which here includes a 7-day outage), not on the inside view.
    3. Bus-factor / key-person-dependency literature (e.g. Avelino et al., 2016. "A novel approach for estimating truck factors." IEEE ICPC). — A single-human review gate is a recognized throughput ceiling and single point of failure; identified as a schedule risk, never as a neutral persistence condition.
  Strength of support: None
  Summary: No literature was found supporting the presumption that current build capacity persists through a hard ~4-week schedule when the same record contains a recent week-long infrastructure outage and a growing single-reviewer bottleneck. The relevant literatures run uniformly counter: planning-fallacy research shows people systematically discount their own documented disruption history; reference-class forecasting requires incorporating the observed outage rate into the schedule (a 7-day outage inside the recent window implies material expected downtime within any 4-week horizon); and the bus-factor literature treats a single human gate as a first-order schedule risk requiring buffering or de-bottlenecking. The only mitigating note: short horizons (~4 weeks) and recently-measured throughput give better-than-average forecast conditions, and buffering practice (20–30% schedule reserve, MVD fallbacks) shows how the schedule could be made sound — but those are remedies the presumption omits, not support for it.
  Caveats: A buffered version of the plan (outage-adjusted throughput, explicit minimum-viable-deliverable, reviewer-gate triage) would be well supported; the unbuffered persistence assumption is not. Searched practitioner and academic planning literature; no source found defending capacity-persistence assumptions against contrary same-record evidence.
  Search scope: 1 query ("planning fallacy project schedule overrun buffer key person dependency single point of failure bus factor risk"); productive for the counter-case, unproductive for support.
  Recommendation: NO-SUPPORT-FOUND
