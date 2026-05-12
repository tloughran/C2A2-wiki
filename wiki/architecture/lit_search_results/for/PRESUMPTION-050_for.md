SEARCH-FOR-PRESUMPTION-050:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-050
  Original statement: "4-day stale .git/index.lock classified as single incident, not escalation (asymmetric with ASSUMPTION-042 Chrome threshold)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-050
    Item type: PRESUMPTION (unstated — surfaced by inference) — INTERNAL-CONSISTENCY flag with ASSUMPTION-042
    Transform at each step:
      14b: Surfaced as asymmetric incident-classification across channel pairs
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (minor/partial)

  Sources:
    1. Incident-management literature (ITIL Incident vs. Problem classification; Google SRE book ch. 14): a persistent unresolved issue is classified as a *problem*, not merely a repeated incident. A 4-day static blocker satisfies the problem-classification criterion.
    2. Circuit-breaker / staleness-threshold literature (Nygard 2007 "Release It!"; Hystrix; Netflix chaos-engineering practice): repeated occurrences of an unresolved issue cross a threshold and are escalated as standing conditions, not logged as transient incidents.
    3. DECISION-018 history in the wiki itself: the git-index.lock issue already has an open standing remediation — it is *already classified* as a known persistent condition, so treating it as a single transient incident contradicts the wiki's own decision record.
    4. C2A2 prior INTERNAL-CONSISTENCY cluster (PRESUMPTION-044 + ASSUMPTION-042): the system has a prior disposition recognizing that threshold-logic asymmetry across channels is a named consistency gap. PRESUMPTION-050 extends the same pattern.

  Strength of support: None

  Summary: No literature supports the asymmetric classification. Every relevant body — ITIL, SRE, circuit-breaker, and C2A2's own decision record — supports classifying a 4-day standing blocker as a problem (or escalated incident), not as a single transient incident. The INTERNAL-CONSISTENCY flag with ASSUMPTION-042 is structurally sound: the same system applies divergent thresholds to different channels.

  Caveats: (a) The asymmetry could be *intentional* if there is a documented reason why git-index.lock has a longer tolerance than Chrome failures — but no such reason is documented; (b) one could argue the lock issue is lower-impact per-day than Chrome, but that would call for *documented* differential thresholds, not *silent* asymmetry.

  Recommendation: NO-SUPPORT-FOUND (supports the AGAINST position — the asymmetry is a named consistency gap, not a defensible design choice)
