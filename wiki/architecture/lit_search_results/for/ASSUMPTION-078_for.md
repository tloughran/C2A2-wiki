SEARCH-FOR-ASSUMPTION-078:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-078
  Original statement: "Two parallel sandbox-infrastructure failure modes (auth gap, mount topology) are treated as user-fixable"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-078
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 — concurrent failure modes both routed to user-fix
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. ITIL Service Operation framework — failure-mode classification distinguishes "user-fixable", "tier-1 support", "engineering escalation"; user-fixable is a recognized category but the framework warns that mis-classifying tier-1+ failures as user-fixable is a documented failure mode.
    2. Norman (1988) "The Design of Everyday Things" — user-fix patterns work when the affordance is clear; "blame the user" classification is a known design anti-pattern.
    3. Cognitive Walkthrough literature (Lewis et al. 1990) — supports the proposition that simple, well-affordant failure modes can be user-fixed; complex ones cannot.
    4. SRE error-budget literature (Beyer et al. 2016, Ch. 4) — endorses graceful-degradation-with-user-action for narrow failure classes (e.g., refresh-the-page); rejects it for systemic infrastructure failures.
    5. C2A2 operational record: PRESUMPTION-061 (sandbox mount topology) was already REVISE-flagged 2026-04-21; PRESUMPTION-068 (Chrome auth resolved-vs-transient) was MONITOR-flagged 2026-04-21. Both predate today's evidence.

  Strength of support: Weak-to-Moderate

  Summary: User-fixable as a failure-mode classification is supported in service-operation frameworks (ITIL) and SRE for narrow, well-affordant cases. However, the literature uniformly warns that classifying systemic infrastructure failures as user-fixable is a documented failure mode — and the C2A2 record already shows both modes (mount topology, auth) being flagged for higher-tier remediation in prior cycles. ASSUMPTION-078's framing aligns with the literature's narrow case but conflicts with C2A2's own prior flags.

  Caveats: (a) The literature distinguishes "single-incident user-fixable" from "recurring user-fixable"; the latter is a known anti-pattern. (b) Both failure modes referenced in ASSUMPTION-078 have already been flagged in prior cycles as warranting escalation, suggesting the user-fixable framing has already been weakened by C2A2's own evidence.

  Recommendation: PARTIALLY-SUPPORTED (user-fixable is a valid classification for narrow cases; the two specific failure modes referenced are documented as recurring and have prior-cycle escalation flags, weakening the literal claim)
