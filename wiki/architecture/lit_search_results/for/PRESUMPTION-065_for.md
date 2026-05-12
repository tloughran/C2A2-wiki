SEARCH-FOR-PRESUMPTION-065:
  Date searched: 2026-04-21
  Original item: PRESUMPTION-065
  Original statement: "The two simultaneously-running 'Morning' scheduled tasks are treated as independent data points for candidate DECISION-024's turn-cap empirical case."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-065
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from CHANGE-2026-04-21-006 counting three data points in four days
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Independent-events literature (statistics textbooks; Rice 2007 "Mathematical Statistics"): treating co-occurring observations as independent is defensible only if shared-environment confounds are absent. Provides conditional support — if independence holds, the count-as-N argument is valid.
    2. Engineering practice (CI/CD parallel-test runs): parallel runs of independent tasks ARE counted as independent observations in common engineering contexts.

  Strength of support: Weak

  Summary: No literature supports the specific presumption under C2A2 conditions. The two Morning sessions share a sandbox environment, invocation pattern, calendar day, and possibly the same MCP server state. Statistical independence requires absence of shared confounds — a condition the sessions do not meet. Supportive literature for "count-as-N" explicitly conditions on environmental independence; C2A2's setup does not provide it. Close-adjacent precedent PRESUMPTION-029 (multi-subagent batch correlation) applies the same concern at the subagent layer and has been STRONGLY-CHALLENGED in prior cycles.

  Caveats: (a) Engineering practice supports count-as-N only when environmental independence is verified; (b) the presumption as stated does not verify independence, so supportive literature cannot ground it.

  Recommendation: NO-SUPPORT-FOUND (independence unverified under conditions that literature explicitly conditions on; precedent PRESUMPTION-029 already STRONGLY-CHALLENGED for parallel concern at subagent layer)
