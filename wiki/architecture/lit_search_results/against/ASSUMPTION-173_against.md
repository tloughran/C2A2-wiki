SEARCH-AGAINST-ASSUMPTION-173:
  Date searched: 2026-05-19
  Original item: ASSUMPTION-173
  Original statement: "Future-dated lecture announcements warrant follow-up monitoring-task scheduling rather than past-tense treatment."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-173
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced from morning curation — forward-looking scheduling decision
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Rasmussen, J. (1997). "Risk management in a dynamic society: a modelling problem." Safety Science. — Documents how proliferation of low-value monitoring tasks degrades attention to high-value ones; "vigilance dilution."
    2. Reason, J. (1990). "Human Error." Cambridge University Press. — Notes that follow-up-task-creation systems accumulate cruft if not actively pruned; the cure (monitor everything future-dated) becomes worse than the disease (occasionally missing a follow-up).
    3. ITIL v4 Continual Improvement literature — explicitly cautions against unbounded "follow-up task" creation; recommends a triage filter.
    4. Lean / Kaizen literature (Ohno, Shingo) — concept of "muda" (waste); monitoring tasks that produce no action are waste.

  Strength of challenge: Weak-to-moderate

  Summary: The challenge is not that follow-up-on-future-events is wrong, but that blanket application is wasteful and creates monitoring debt. Vigilance dilution (Rasmussen, Reason) and Lean muda critique converge: monitoring tasks that don't generate decisions are pure overhead. The assumption needs a significance filter to be operationally sound.

  Specific risks: Monitor-task accumulation creates a second pending queue; agents spend time updating tickler files rather than producing primary work; low-value future-dated mentions crowd out attention to high-value ones.

  Mitigations available: Tier follow-up tasks by significance; auto-expire monitor tasks if not acted on within N cycles; require explicit "expected value of follow-up" annotation.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-173
    Strongest counterargument: Unbounded follow-up scheduling produces monitoring debt that competes with primary work. The principle of "schedule, don't past-tense" is correct in spirit but needs a significance triage filter, or it generates muda.
    What would need to be true for C2A2 to be safe: Follow-up tasks must be triaged by expected information value; auto-expiry policy in place; monitor-queue depth bounded.
    How to test: Track conversion rate from monitor-tasks to actual updates; if <X%, the scheduling rule is too liberal.
