SEARCH-AGAINST-PRESUMPTION-345:
  Date searched: 2026-06-12
  Original item: PRESUMPTION-345
  Original statement: "Proposed artifacts get created or their absence gets noticed (plan-inventory durability; an individuation_vs_reunion.md gap went 18 days unnoticed)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-345
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from 2026-06-11 EOD session
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. APS / ScienceDaily (2012). "When we forget to remember: Failures in prospective memory range from annoying to lethal." Association for Psychological Science. — Establishes that prospective memory failures (forgetting to perform deferred intentions) are among the most common and consequential everyday cognitive failures; deferred tasks with no external cue systematically decay without execution.
    2. McDaniel, M.A. & Einstein, G.O. (2007). Prospective Memory: An Overview and Synthesis of an Emerging Field. Sage. — Comprehensive review establishing that the key risk factors for prospective memory failure are: (a) increasing delay between intention formation and execution, (b) absence of a strong environmental cue at the intended moment, and (c) competition from intervening tasks. All three apply to a multi-day artifact backlog.
    3. Dismukes, R.K. (2010). "Prospective Memory in Aviation and Everyday Settings." NASA Human Systems Integration. — Documents prospective memory failures in high-stakes operational contexts; shows that experienced professionals in safety-critical roles fail to execute deferred intentions reliably when the intention-to-action gap exceeds a session boundary, even with checklists and reminders. The 18-day gap in the C2A2 case substantially exceeds the intervals studied.
    4. Tandfonline (2024). "Effects of delay and reminders on time-based prospective memory in a naturalistic task." Memory. — Directly relevant: shows that delay is the strongest predictor of prospective memory failure; even short delays (hours to days) produce significant intention-to-action failures in naturalistic settings; the effect compounds with delay length.
    5. Springer (Koriat et al., 1990). "Prospective memory: When reminders fail." Memory & Cognition. — Shows that even when reminders exist, they can fail to trigger the associated intention if the reminder and the original context are not well linked; an entry in a plan log is only as effective as the system for monitoring it.
    6. Swanson, H.L. & Siegel, L. (2001). "Learning Disabilities as a Working Memory Deficit." Issues in Education. — In the broader context: limited working memory capacity means that prospective intentions not supported by external cues compete poorly against immediate task demands; this is not a pathological condition but a feature of ordinary cognition, making external cue systems necessary rather than supplementary.
    7. Empirical software engineering studies on orphaned TODOs (e.g., Storey et al., 2008, "TODO or to Bug: Exploring How Task Annotations Play a Role in the Work Practices of Software Developers." ICSE). — Shows that TODO annotations in codebases have high orphan rates (never acted on); the proportion of TODOs that are never resolved increases with project age and team size. The parallel to plan-inventory items in a shared knowledge base is direct.

  Strength of challenge: Strong

  Summary: The presumption that proposed artifacts get created or their absence gets noticed is directly falsified by the 18-day gap cited in the original item itself — the C2A2 system already contains an empirical instance of the failure. This is not a theoretical risk but a documented occurrence. The prospective memory literature provides the mechanism: deferred intentions without strong environmental cues at the execution moment fail at high rates, and the failure rate compounds with delay length. Software engineering research on orphaned TODOs shows the same pattern in a structurally analogous setting: plan-inventory items without active monitoring systems have high decay rates. The "absence blindness" aspect is equally well-supported: humans are not reliable detectors of missing expected items; absence of a stimulus generates no salient cue, so the detection of plan-inventory gaps requires active monitoring rather than passive observation.

  Specific risks: The plan-inventory will accumulate ghost entries — proposed artifacts that were never created and whose absence is never noticed. Over time, the vault's apparent comprehensiveness will diverge from its actual coverage; topics that were intended for development but never received an artifact will have no representation, systematically biasing the vault toward areas where execution followed intention. The maturity model may credit planning activity as equivalent to artifact production, further inflating apparent progress.

  Mitigations available: Maintain a separate, actively monitored plan-inventory log with explicit status fields (PROPOSED / IN-PROGRESS / CREATED / ABANDONED); implement periodic (weekly) sweeps of the plan-inventory to identify items with no status update; set time-bounded completion expectations at the moment of proposal rather than open-ended deferred intentions; use environmental cues (calendar reminders, session-opening checklist items) to trigger review of outstanding proposals.

  STEELMAN:
    Strongest counterargument: The 18-day gap was noticed — that is why it appears in the EOD session that generated this presumption. The detection mechanism, however slow, did function. A system that eventually detects and surfaces gaps is better than one that never does; the question is whether the detection latency (18 days) is acceptable given the cost of the gap. If artifact gaps have low impact on downstream reasoning quality, the detection latency may be tolerable. The gap is a calibration data point, not a systemic failure.
    What would need to be true for C2A2 to be safe: The plan-inventory would need an active monitoring mechanism with a defined maximum acceptable gap between proposal and either creation or explicit abandonment; gaps should trigger automated alerts rather than relying on passive detection. The acceptable latency should be defined based on how quickly a missing artifact can distort downstream reasoning.
    How to test: Audit the full plan-inventory log for all proposed artifacts against the vault's actual contents; count the current orphan rate and median age of unresolved proposals. If the orphan rate exceeds 20% or median age exceeds 7 days, the presumption is empirically falsified.

  Search scope: Searched prospective memory failure literature (McDaniel & Einstein, Dismukes NASA, Koriat et al.), delay effects on intention execution, orphaned TODO software engineering studies, and absence blindness / change blindness literature. Comprehensive for primary challenge directions.

  Recommendation: CHALLENGED
