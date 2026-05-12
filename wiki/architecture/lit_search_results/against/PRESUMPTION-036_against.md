SEARCH-AGAINST-PRESUMPTION-036:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-036
  Original statement: "Aggregating Chrome + git + ACL + Anthropic failures as one 'OPERATIONAL-DRIFT' cluster is legible despite four disjoint root causes"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-036
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — composite cluster labeling with disjoint root causes
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Root-cause-analysis literature (Rooney & Vanden Heuvel 2004; Carroll 1995 on 5-whys): aggregating distinct root causes under a single label is a documented anti-pattern that obscures action; separate root causes require separate remediation tracks.
    2. Allspaw (2012) "Blameless Postmortems": single-cluster remediation chronically under-fixes composite-cluster events — the most attention-worthy root cause dominates, others drift.
    3. Failure-mode-classification literature (Leveson 2011 "Engineering a Safer World"): taxonomic accuracy is essential for remediation prioritization; coarse labels lose information.
    4. Common-cause vs. coincident failure literature: mislabeling independent incidents as a single cluster both over-attributes and under-attributes responsibility.

  Strength of challenge: Strong

  Summary: The literature's position is clear: aggregating four disjoint root causes under one label is a remediation anti-pattern. Each failure channel — browser extension, git auth, ACL, vendor billing — has distinct causes, owners, and fixes; a single cluster label invites single-track remediation that will chronically under-fix the quieter three. The legibility gain (one alert instead of four) is outweighed by the remediation loss (three channels get quietly ignored).

  Specific risks: Most-visible failure dominates attention and gets fixed; quieter three persist and recur; chronic under-fixing; future aggregation reinforces the same pattern; reviewing "OPERATIONAL-DRIFT" as a single event loses the per-channel lesson.

  Mitigations available:
    - Composite-for-visibility, atomic-for-remediation: dashboard view aggregates; incident records are per-channel
    - Track each channel's fix independently; aggregate flag is closed only when all component incidents are closed
    - Tag each failure with its root-cause category; report both aggregate and per-cause counts

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-036
    Strongest counterargument: Composite labels for disjoint root causes erase the information needed for remediation. Four channels went down today; each has a different owner and fix. Cluster labels drive single-track response; independent channels need independent response. The legibility benefit (one alarm) is precisely the cost (one fix for four problems).
    What would need to be true for C2A2 to be safe: Per-channel incident tracking is preserved; cluster label is observational (a display choice), not operational (a remediation unit); a remediation record exists for each root cause independently.
    How to test: Next similar event — does each channel get a separate fix, or does one fix "close" the cluster while others persist? Track recurrence rate per channel.
