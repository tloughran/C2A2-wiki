SEARCH-AGAINST-PRESUMPTION-127:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-127
  Original statement: "Today's McGilchrist off-cadence filing presumed routinely absorbable without raising 2-day off-cadence pattern flag"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-127
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD off-cadence pattern observation
      15b: Searched for counter-evidence on multi-day off-cadence pattern indicator-rate
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Statistical-process-control literature (Wheeler 2000) — multi-event runs in a short window can be above-significance even when single events are below; clustering matters.
    2. Agile / Scrum literature (Cohn 2010) — pattern emergence (multi-day off-cadence cluster) warrants observability flag even when individual events are absorbable.
    3. Research-output cadence literature (Chubb & Reed 2018) — pattern-detection requires multi-event window; absorbing without observing is documented failure mode for trend detection.
    4. ASSUMPTION-091 / PRESUMPTION-113 cluster — uniform-treatment cluster recurrence; this is the third item in the cluster.
    5. C2A2-internal: 3 off-cadence events in 4 days is borderline by SPC; absorbing without flagging means trend invisible to downstream agents.

  Strength of challenge: Moderate

  Summary: The presumption is moderately challenged. Single off-cadence absorbability is canonical practice; the gap is at the cluster level — 3 events in 4 days warrants observability flag even when individual events are absorbable. PRESUMPTION operates at the cluster-recognition level; literature supports observability without escalation.

  Specific risks: (a) Cluster invisible to downstream agents; (b) trend detection foreclosed by absorption-without-observability; (c) extends ASSUMPTION-091 / PRESUMPTION-113 uniform-treatment cluster.

  Mitigations available: (a) Cadence-tag on filings; (b) cluster-flag at N-th off-cadence event in window; (c) cadence-sliced metric.

  Recommendation: PARTIALLY-CHALLENGED (single-event absorbability is supported; cluster-level observability is the gap)

  STEELMAN:
    Item: PRESUMPTION-127
    Strongest counterargument: Single off-cadence events are routinely absorbable; the literature supports this. But the C2A2 cluster has now reached 3 off-cadence events in a 4-day window (ASSUMPTION-091, PRESUMPTION-113, PRESUMPTION-127) — this is borderline by SPC discipline. Absorbing without raising the cluster flag means the trend is invisible to downstream agents and to cadence-sliced metrics. Observability ≠ escalation; observability is the canonical first step.
    What would need to be true for C2A2 to be safe: (a) Cadence-tag on filings; (b) cluster-flag at N-th off-cadence event in window; (c) cadence-sliced metric.
    How to test: Add cadence-tag; observe whether cluster-flag fires at N-th event; check cadence-sliced approval-rate against pooled.
