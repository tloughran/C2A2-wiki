SEARCH-FOR-ASSUMPTION-102:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-102
  Original statement: "20-item EOD lit-search batch draining 100% in single morning 15a/15b/15c cycle constitutes operational baseline for lit-search throughput at present queue scale"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-102
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD throughput observation
      15a: Searched for queueing-theory throughput baselines for human-augmented review pipelines
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Kleinrock (1975) "Queueing Systems Vol 1" — single-cycle drain rate is a canonical service-rate baseline for bounded queueing systems; 20/cycle satisfies baseline definition under stationary-queue assumption.
    2. Hopp & Spearman (2008) "Factory Physics" — operational baseline is established by sustained drain rate over ≥3 consecutive cycles, not single-cycle observation; single-cycle is an upper-bound point estimate.
    3. Beyer (2016) "Site Reliability Engineering" on SLO baselining — service-rate baseline requires multi-period observation; single-period is insufficient for SLO calibration.
    4. C2A2-internal: 2026-04-27 (57 items processed across new + retriggered) and 2026-05-05 (20 + 57 retriggered) prior cycles establish that throughput can vary with retrigger load; single-cycle baseline at 20 items underspecifies the load envelope.
    5. PRESUMPTION-123 surfaces the parallel concern: throughput-as-success metric without quality / INCORPORATE-rate complement.

  Strength of support: Moderate (Partial)

  Summary: Single-cycle drain at queue-scale is a defensible point estimate for throughput baseline but is not, by queueing-theory or SRE-baselining standards, a sufficient baseline. Operational baselines in mature observability literature require ≥3 consecutive cycles of stable drain rate. The 2026-05-09 single-cycle observation is positive evidence but not yet a baseline. Throughput-only baselines also miss the quality dimension that PRESUMPTION-123 surfaces.

  Caveats: (a) "Operational baseline" in the literature implies sustained measurement, not single-cycle; (b) baseline at "present queue scale" requires queue-scale specification — when queue grows (e.g., 57+20 items), throughput may not scale; (c) throughput baselines without quality metrics (INCORPORATE rate, REVISE-backlog growth) are incomplete per PRESUMPTION-123.

  Recommendation: PARTIALLY-SUPPORTED (single-cycle is a positive data point; canonical baseline requires multi-cycle observation; quality complement per PRESUMPTION-123 is the standard adjacent guard)
