SEARCH-AGAINST-PRESUMPTION-332:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-332
  Original statement: Current build capacity (attended cadence + agentic throughput + infrastructure) persists through the ~4-week ISME schedule, despite a same-day record of 7-day sync outage and a growing single-human review gate.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-332
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from ISME plan (2026-06-09 EOD run): 4-week schedule presumes capacity continuity contradicted by same-day outage record; flagged MEDIUM
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Kahneman, D. & Tversky, A., 1979. "Intuitive Prediction: Biases and Corrective Procedures." TIMS Studies in Management Science. — Origin of the planning fallacy and the inside/outside view distinction: schedules built from current-capacity extrapolation ignore the distribution of disruptions, which is exactly what a capacity-persistence presumption does.
    2. Flyvbjerg, B., 2006. "From Nobel Prize to Project Management: Getting Risks Right." PMJ. — ~86% of projects overrun; reference-class forecasting requires anchoring on observed disruption rates. Here the reference class contains a documented 7-day outage recorded the same day the 4-week plan was made — base-rate evidence of roughly 25%-of-schedule-length outages being live.
    3. Buehler, R., Griffin, D., Ross, M., 1994. "Exploring the 'Planning Fallacy'." JPSP. — People persist in optimistic forecasts even with full knowledge of their own past delays, attributing them to non-recurring causes — the precise mechanism by which a same-day outage record fails to update a same-day schedule.
    4. Avižienis, A. et al., 2004. "Basic Concepts and Taxonomy of Dependable and Secure Computing." IEEE TDSC (with the bus-factor literature, e.g., Avelino et al. 2016, "A Novel Approach for Estimating Truck Factors," ICPC). — A pipeline with a single non-redundant component (one human review gate) has system availability bounded by that component's availability; growing queue load on a single gate predicts saturation, the canonical single-point-of-failure pattern.
  Strength of challenge: Strong
  Summary: This is a near-textbook planning-fallacy configuration, with the unusual feature that the disconfirming base-rate evidence (a 7-day sync outage) was recorded the same day the capacity-persistence presumption was made. Buehler et al. show exactly this pattern: past disruptions are mentally filed as one-offs and excluded from the forecast. Reference-class reasoning says a 4-week schedule in an environment that just produced a 1-week outage should carry an explicit ~25% capacity-loss contingency. Independently, dependability theory makes the single-human review gate the binding constraint: agentic throughput can rise without raising delivered output, because system availability and throughput are capped by the non-redundant component — and that component (one person's attention) is subject to illness, travel, and competing demands over any 4-week window.
  Specific risks: ISME deadline slips for reasons already in evidence; review-gate saturation silently converts "4 weeks of build" into "4 weeks of queue"; outage recurrence mid-schedule leaves no slack; failure arrives as a surprise despite being base-rate predictable, compounding ASSUMPTION-298's over-promising exposure.
  Mitigations available: Reference-class buffer (add observed outage rate to the schedule explicitly); define the minimum viable ISME deliverable now and sequence work so it completes first; reduce review-gate load via batching/triage tiers (not everything needs the human gate at the same depth); pre-plan degraded-mode operation for the next sync outage.
  STEELMAN:
    Strongest counterargument: Small-team short-horizon projects are not Flyvbjerg megaprojects; a 4-week window is short enough that current conditions plausibly persist, and the dyad has direct recent evidence of high realized throughput. The 7-day outage, having just occurred and presumably been diagnosed, may now be the LEAST likely disruption (fixed root cause), making its same-day recording an argument for confidence rather than alarm. Agentic capacity is also genuinely elastic: lost days can be partially recovered by parallelism in a way human-only teams cannot.
    What would need to be true for C2A2 to be safe: The outage's root cause is fixed and verified; the human gate has measured headroom (review queue is stable or shrinking, not growing); a minimum-viable fallback exists so a capacity dip degrades scope rather than killing the deliverable.
    How to test: Instrument the review gate for one week — items entering vs items cleared. A growing queue falsifies capacity persistence immediately. Also: write down the explicit contingency math (schedule x observed outage rate) and check the plan still closes.
  Search scope: "planning fallacy software project schedule overrun reference class forecasting single point of failure key person dependency bus factor" (1 search); plus Kahneman & Tversky 1979, Buehler et al. 1994, Avelino et al. 2016 from established literature.
  Recommendation: CHALLENGED
