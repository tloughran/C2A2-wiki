SEARCH-FOR-ASSUMPTION-094:
  Date searched: 2026-05-09
  Original item: ASSUMPTION-094
  Original statement: "Cross-project sandbox-infrastructure constraints accumulate to single-escalation threshold around N≥5"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-094
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-08 cross-project escalation decision: N≥5 sandbox issues bundled for single escalation to Anthropic
      15a: Searched for supporting literature on incident-aggregation policy in vendor escalation; bug-bundling vs. atomic reporting
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes (with conditions)

  Sources:
    1. ITIL v4 (2019) Service Management — incident bundling is endorsed when issues share a common service / infrastructure layer; bundling reduces context-switching cost for the receiving organization.
    2. ITSM literature (Limoncelli, Hogan, Chalup 2014 "The Practice of System and Network Administration") — N-threshold escalation policies are canonical; specific N values vary by org maturity.
    3. SRE postmortem-clustering practice (Allspaw 2012 "Blameless Postmortems") — bundling of related incidents into a single escalation surfaces structural patterns better than atomic reporting.
    4. Vendor-management literature (Snell & Bohlander 2009) — relationship-preserving escalation favors bundling when issues are non-urgent and share-common-cause.
    5. C2A2-internal: 2026-04-26 / 2026-04-27 escalation-discipline material — bundling is consistent with C2A2's prior MEDIUM/MEDIUM-HIGH escalation discipline.

  Strength of support: Moderate

  Summary: Bundled cross-project escalation at an N-threshold is canonical ITSM / SRE practice when issues share a common architectural layer. The N≥5 specific threshold is not literature-prescribed but is a reasonable operational choice consistent with documented patterns. Supportive literature treats bundling as preferable to atomic reporting for non-urgent issues with shared root cause.

  Caveats: (a) Bundling requires that the bundled issues share a common architectural layer — if they don't, bundling dilutes signal (this is exactly PRESUMPTION-110 territory); (b) literature does not endorse a universal N value — N=5 is a heuristic that may understate or overstate appropriate batch size depending on issue severity; (c) high-urgency issues (SYSTEMIC ESCALATION class — see ASSUMPTION-095) should not be bundled with low-urgency issues; bundling is canonical only within urgency tier.

  Recommendation: PARTIALLY-SUPPORTED (bundling is canonical; same-architectural-layer precondition and urgency-tier discipline are the standard guards)
