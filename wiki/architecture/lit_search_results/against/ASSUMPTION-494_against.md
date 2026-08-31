SEARCH-AGAINST-ASSUMPTION-494:
  Date searched: 2026-08-30
  Original item: ASSUMPTION-494
  Queue ref: for_lit_search.md — 2026-07-21 EOD batch (Priority Medium)
  Original statement:
    The inbox-diff slug normalizer produces a systematic false positive by retaining the date prefix
      (reported 126 unprocessed; true 33); same error class as 07-19 and 07-20.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-494
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-21 daily run, exact quote
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: WebSearch, 2026-08-30, clustered query — "wontfix / deferred-defect triage as rational prioritisation; technical-debt prioritisation". Snippet-level only; zero
    full-text and zero abstract-level reads. Search confidence: MODERATE. This item was searched on its
    GENERALIZABLE limb only; the internal-empirical limb (a claim about this repository's own file state)
    is not adjudicable by literature and is marked NOT-SEARCHED, per the 2026-08-29 run's split-limb
    finding.

  Challenging evidence found: Partial

  Sources:
    1. Atlassian. "Bug Triage: Definition, Examples, and Best Practices." — the defect list always exceeds
       available time; deferral is a normal triage outcome, not a failure.
    2. Crosscheck. "Bug Triage Process." — deferral is legitimate WHEN severity, priority, owner and
       rationale are documented and linked; that record is the discriminator.
    3. Besker et al. / Lenarduzzi et al. "A systematic literature review on Technical Debt prioritization."
       J. Systems & Software (2020). — organizations largely lack systematic TD prioritization; ad
       hoc deferral is the norm, not evidence of a decision.

  Strength of challenge: Moderate

  Summary:
    The challenge is not to the diagnosis but to the 'same error class three days running' framing carrying
      an implied obligation to fix. Triage literature treats deferral as a normal outcome: the defect list
      always exceeds capacity, and a known defect may legitimately be promoted with written acceptance. What
      the literature does require is a deferral record -- severity, priority, owner, rationale -- and
      repeat-finding visibility.

  STEELMAN:
    a normalizer false positive that inflates a count nobody acts on may be correctly ranked below
      every other open item. Recurrence across days is then evidence of consistent prioritisation, not of
      neglect. The failure would only be real if no deferral rationale exists.

  Recommendation: PARTIALLY-CHALLENGED
