SEARCH-FOR-PRESUMPTION-1218:
  Date searched: 2026-11-06
  Original item: PRESUMPTION-1218
  Original statement: Health ledger presumed to allow a writer to withhold a true observation to keep the last-line-wins aggregate correct.
  Claim tested (literature lane): append-only audit logs vs. derived status views; alarm-fatigue suppression and its effect on monitoring validity (SRE / safety-critical alarm management, e.g. ISA-18.2 alarm rationalization). The in-house limb (count of days on which routine_health.md's last line came from a different copy than an earlier same-day line) is NOT 15a/15b scope and was not run.
  Reading used for the FOR direction: the presumption is a real hazard if the literature treats the log as the record of truth and the status as a derived view, and treats unlogged suppression of true signals as degrading monitoring validity.
  Search scope: PRELIMINARY. 3 web searches for the FOR direction, 0 fetches. All hits are title-only; no page was opened.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15a
    Original item: PRESUMPTION-1218
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: inferred from the design of a last-line-wins health ledger
      15a: Searched for supporting literature (preliminary; 3 searches, 0 fetches, title-only)
    Current status: PARTIALLY-SUPPORTED
  Supporting evidence found: Partial
  Sources (all title-only, unread):
    1. Event-sourcing pattern pages (learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing; gravitee.io "Event Sourcing Patterns for Auditability and Replay"; val.town ADR "Single append-only events log as source of truth for history") - titles indicate the standard pattern is an append-only log as source of truth with state derived from it, which is the opposite of letting a writer decide what enters the log.
    2. ISA-18.2 alarm management lifecycle / rationalization (exida.com Alarm Rationalization; e2g.com "Reduction of Nuisance Alarms ... Focus on Rationalization"; open-exam-prep ISA-18.2 lifecycle) - titles indicate alarms are rationalized by documented criteria rather than ad hoc by the operator, i.e. the field treats who may drop a signal as a controlled decision.
    3. ISA/InTech "Alarm suppression" and AIChE 2022 "Alarm Management, Rationalization and Suppression ... Situational Awareness" - titles indicate suppression is a recognised mechanism that affects situational awareness and needs control.
    4. Selective-reporting literature ("Reporting bias in medical research - a narrative review," PMC2867979; Cochrane abstract on selective reporting of analyses) - titles indicate withholding observations that disagree with the summary biases the aggregate.
  Strength of support: Weak. Titles show the log-of-truth/derived-view split and controlled suppression are standard ideas; no page was read, and nothing addresses a single-writer health ledger with duplicate copies.
  Summary: The neighbourhood agrees that a derived status should not be allowed to filter what enters the record, and that suppression is a controlled act. Nothing read confirms the specific hazard in a last-line-wins file.
  Caveats: Title-only; Scribd and vendor pages are low-authority. NOVELTY: not flagged for the general pattern; the duplicate-copy last-line case is unaddressed.
  Recommendation: PARTIALLY-SUPPORTED
