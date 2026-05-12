SEARCH-AGAINST-PRESUMPTION-120:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-120
  Original statement: "Out-of-band Pattern-Detector deep-pass scheduling presumed policy-free — no specification for non-standard insertion priority or capacity competition"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-120
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD out-of-band scheduling observation
      15b: Searched for counter-evidence on out-of-band scheduling fairness vs. baseline-discoverable content
    Current status: CHALLENGED

  Sources:
    1. Selection-effect literature (Heckman 1979; Berk 1983) — out-of-band insertion without policy is canonical source of selection bias.
    2. Scheduling-policy literature (Tanenbaum 2014; Pinedo 2016) — policy-free out-of-band insertion is documented anti-pattern in queue management.
    3. CFS / Linux kernel scheduler design notes — out-of-band priority bumps require explicit policy or they introduce capacity-competition with baseline workloads.
    4. PRESUMPTION-029 cluster (multi-subagent batch inflation) — same failure mode at adjacent layer; this is recurrence pattern.
    5. C2A2-internal: Pattern-Detector deep-pass scheduling has no documented out-of-band-insertion policy; current decisions are ad hoc per item.

  Strength of challenge: Moderate-Strong

  Summary: The presumption that policy-free out-of-band scheduling is acceptable is challenged by selection-effect, OS-scheduling, and distributed-systems literatures. Without policy, out-of-band insertion enjoys selection bias — items prioritized via the deep-pass channel get more attention because of insertion, not because of outcome. PRESUMPTION-029 cluster recurrence at adjacent layer (multi-subagent batch inflation) confirms the pattern.

  Specific risks: (a) Selection bias toward items detected by Pattern-Detector deep-pass; (b) capacity-competition with baseline-discoverable content; (c) recurrence of PRESUMPTION-029 multi-subagent batch inflation pattern.

  Mitigations available: (a) Explicit out-of-band-insertion policy; (b) capacity-competition guard (per-cycle out-of-band budget); (c) outcome-based ranking for prioritization rather than selection-based ranking.

  Recommendation: CHALLENGED (literature consensus strong against policy-free out-of-band scheduling; recurrence of PRESUMPTION-029 cluster pattern)

  STEELMAN:
    Item: PRESUMPTION-120
    Strongest counterargument: Policy-free out-of-band scheduling enjoys selection bias by construction. The items prioritized through the deep-pass channel get more attention because they were inserted, not because they have higher outcome value. This is the recurring failure mode that PRESUMPTION-029 (multi-subagent batch inflation) was REVISE'd for at the adjacent layer. The OS-scheduling literature is uniform: explicit policy is required for out-of-band insertion or capacity-competition with baseline workload is canonical.
    What would need to be true for C2A2 to be safe: (a) Explicit out-of-band-insertion policy; (b) per-cycle out-of-band budget; (c) outcome-based ranking rather than selection-based ranking.
    How to test: Track the outcome (downstream uptake, INCORPORATE rate) of items inserted via deep-pass vs. baseline-discoverable items; if deep-pass items don't outperform on outcome, the prioritization is selection-bias.
