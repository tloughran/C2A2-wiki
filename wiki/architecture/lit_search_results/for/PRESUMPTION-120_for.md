SEARCH-FOR-PRESUMPTION-120:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-120
  Original statement: "Out-of-band Pattern-Detector deep-pass scheduling presumed policy-free — no specification for non-standard insertion priority or capacity competition"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-120
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD out-of-band scheduling observation
      15a: Searched for selection-effect literature on out-of-band content prioritization and scheduling-policy design
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. Selection-effect literature (Heckman 1979; Berk 1983) — out-of-band insertion without policy is a canonical source of selection bias; the high-leverage items get more attention by virtue of being inserted, not by virtue of being high-leverage.
    2. Scheduling-policy literature (Tanenbaum 2014 "Modern Operating Systems"; Pinedo 2016 "Scheduling: Theory, Algorithms, and Systems") — policy-free out-of-band insertion is documented as a queue-management anti-pattern.
    3. Out-of-band scheduling fairness literature in distributed systems (CFS, Linux kernel scheduler design notes) — out-of-band priority bumps require explicit policy or they introduce capacity-competition with baseline workloads.
    4. (No literature supports policy-free out-of-band scheduling as a sound default.)
    5. C2A2-internal: Pattern-Detector deep-pass scheduling has no documented out-of-band-insertion policy; the decision is currently ad hoc per item.

  Strength of support: None

  Summary: No literature supports policy-free out-of-band scheduling. The selection-effect, OS-scheduling, and distributed-systems literatures uniformly require explicit policy for out-of-band insertion. The presumption operates against literature consensus.

  Caveats: This is a NO-SUPPORT-FOUND for the FOR direction.

  Recommendation: NO-SUPPORT-FOUND
