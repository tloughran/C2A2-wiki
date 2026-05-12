SEARCH-FOR-PRESUMPTION-036:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-036
  Original statement: "Aggregating Chrome + git + ACL + Anthropic failures as one 'OPERATIONAL-DRIFT' cluster is legible despite four disjoint root causes"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-036
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — aggregate cluster naming with disjoint root causes
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Composite incident management literature (Allspaw 2012 "Blameless Postmortems"): composite views of concurrent failures can be operationally useful for triage and human situational awareness.
    2. Systems thinking literature (Sterman 2000 "Business Dynamics"): cross-system pattern recognition (even across disjoint root causes) can reveal systemic pressures that individual-incident analysis misses.
    3. "Saturation" / "overload" framings in distributed systems postmortem literature: aggregate labels sometimes surface capacity/attention problems that per-incident analysis cannot.

  Strength of support: Weak

  Summary: Composite / aggregate labeling of concurrent incidents has some support as a human-attention tool (triage overview, systemic-pressure detection). However, the literature treats this as a coarse-grained lens that is distinct from — and not a substitute for — per-incident root-cause analysis. The specific claim that the aggregation is "legible" as an operational unit is only weakly supported; legibility is defensible for situational awareness, less so for remediation planning.

  Caveats: Support applies to the observer-attention use case (e.g., situational dashboards), not to the remediation use case. If the cluster label drives single-track remediation, per-root-cause fixes will be under-served (which is the risk PRESUMPTION-036 itself calls out).

  Recommendation: PARTIALLY-SUPPORTED (weak)
