SEARCH-FOR-PRESUMPTION-083:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-083
  Original statement: "Browser-authentication is user-fixable indefinitely (no escalation tier required)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-083
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced — repeat user-fix occurrences without escalation imply indefinite-fixability
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED (Weak)

  Sources:
    1. ITIL Service Operation — supports user-fix patterns as a tier-0 intervention; explicitly warns against indefinite reliance on tier-0.
    2. Norman (1988) "The Design of Everyday Things" — well-affordant fixes can be user-managed; the literature supports the pattern only when the affordance does not degrade.
    3. SRE error-budget literature (Beyer et al. 2016) — endorses graceful-degradation-with-user-action for narrow, single-incident cases; not endorsed for recurring patterns.
    4. C2A2 prior cycle: PRESUMPTION-068 (Chrome auth resolved-vs-transient) was MONITOR-flagged 2026-04-21; the indefinite-fixability framing was already weakened at that point.

  Strength of support: Weak

  Summary: User-fixability is endorsed for narrow cases but never as an indefinite policy. The literature consistently pairs user-fix with an escalation tier; the absence of an escalation tier (which the presumption implies) is the documented anti-pattern.

  Caveats: (a) The single-incident form is supported; the indefinite form is not. (b) The case is structurally similar to PRESUMPTION-068, already MONITOR-flagged.

  Recommendation: PARTIALLY-SUPPORTED (Weak — single-incident user-fix has support; indefinite-fixability does not)
