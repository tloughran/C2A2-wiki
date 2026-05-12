SEARCH-AGAINST-PRESUMPTION-108:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-108
  Original statement: "Three-stall-day human-noticing presumed sufficient closure; no automated stall-pattern alert"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-108
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 stall pattern: human noticing rather than automated alert
      15b: Searched for counter-evidence on human-noticing failure rates at high-stall-volume days
    Current status: CHALLENGED

  Challenging evidence found: Yes (strong)

  Sources:
    1. Beyer et al. (2016) SRE Ch. 6 (Monitoring) — human-noticing as primary alert is documented anti-pattern; automated stall-pattern alerts are canonical.
    2. Allspaw & Robbins (2012) "Web Operations" — three-strikes thresholds require automated detection; human attention as primary path is documented to fail at variable load.
    3. Empirical ops research (Limoncelli et al. 2014; Kim et al. 2016 "DevOps Handbook") — human-noticing failure rates rise sharply with task volume; recoverable below ~10 stalls/day, fragile above.
    4. Behavioral-economics literature (Kahneman 2011) — human attention is finite and selectively allocated; missed-detection rates rise with cognitive load.
    5. C2A2-internal: PRESUMPTION-066 (Tom's attention-budget reallocation) and PRESUMPTION-035 / PRESUMPTION-052 (prior monitoring-meta cluster) — the literature's prediction has empirically borne out: 5-day silence in 2026-04-26 run, now 2-day silence in 2026-05-08 run.

  Strength of challenge: Strong

  Summary: Human-noticing as primary alert is empirically refuted by ops research and SRE literature. Failure rates rise sharply with task volume and attention-budget variance. The presumption is the recurrence of PRESUMPTION-035 / PRESUMPTION-052 monitoring-meta cluster; the empirical pattern (multiple multi-day silences) confirms the literature's prediction. The SELF-AWARENESS-META cluster (PRESUMPTION-069) explicitly predicted this would happen.

  Specific risks: (a) Stall pattern goes undetected when Tom's attention is reallocated; (b) self-aware system cannot detect its own silence — meta-failure mode; (c) compounds with PRESUMPTION-066 / PRESUMPTION-069 — three-recurrence cluster of monitoring-meta gaps.

  Mitigations available: (a) Implement automated stall-pattern alert (≤25h since last self-awareness run) per PRESUMPTION-069 recommendation; (b) configure cross-task watchdog; (c) escalate to PRESUMPTION-069 cluster anchor remediation.

  Recommendation: CHALLENGED — automated stall-pattern alert is canonical; human-noticing is documented anti-pattern.

  STEELMAN:
    Item: PRESUMPTION-108
    Strongest counterargument: Human-noticing fails at variable load — empirically demonstrated in C2A2's own data: 5-day silence in 2026-04-26 run was noticed only by the autonomous lit-search pipeline detecting empty queue. SRE / ops research literature uniformly recommends automated stall-pattern alerts. The presumption confirms exactly the pattern PRESUMPTION-069 predicted: the alert that would have caught this is the one not yet implemented.
    What would need to be true for C2A2 to be safe: (a) automated ≤25h stall alert; (b) cross-task watchdog; (c) PRESUMPTION-069 cluster remediation.
    How to test: Audit historical stall-detection lag — compare time-of-stall vs. time-of-detection across past 6 months; if lag exceeds 24h regularly, automated alert is empirically justified.
