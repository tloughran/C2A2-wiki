SEARCH-AGAINST-ASSUMPTION-102:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-102
  Original statement: "20-item EOD lit-search batch draining 100% in single morning 15a/15b/15c cycle constitutes operational baseline for lit-search throughput at present queue scale"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-102
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD throughput observation
      15b: Searched for counter-evidence on throughput-only baselines missing quality drift
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Goodhart's Law (Goodhart 1975; Strathern 1997) — throughput-as-target ceases to be a good metric; baseline established by single-cycle observation is canonically Goodhartable.
    2. DORA / Accelerate literature (Forsgren 2018) — throughput-only metrics predict downstream-quality regression when not paired with quality and stability metrics.
    3. SRE baselining literature (Beyer 2016) — operational baselines require multi-period observation; single-period is upper-bound point estimate, not baseline.
    4. Hopp & Spearman (2008) — single-cycle observation is canonical for upper-bound estimation under stationary assumption; "operational baseline" implies sustained measurement.
    5. C2A2-internal: 0% INCORPORATE rate while throughput is celebrated (PRESUMPTION-123) is the predicted Goodhartable failure mode.

  Strength of challenge: Moderate

  Summary: Single-cycle drain rate is a positive data point but not an operational baseline by SRE / DORA / queueing-theory standards. Operational baselines require sustained observation (≥3 cycles) and multi-metric design (throughput + quality + stability). The 2026-05-09 single-cycle observation is positive evidence but not yet a baseline. Throughput-only baselines without quality complement (INCORPORATE rate, REVISE-backlog growth) are documented as Goodhartable failure modes (PRESUMPTION-123 captures this).

  Specific risks: (a) Single-cycle observation treated as baseline can lock in unsustainable throughput target; (b) throughput-without-quality is Goodhartable; (c) "present queue scale" is not specified — when queue grows, throughput may not scale.

  Mitigations available: (a) Multi-cycle observation before baselining; (b) pair throughput with INCORPORATE-rate / REVISE-backlog / quality-drift metrics; (c) queue-scale envelope specification.

  Recommendation: PARTIALLY-CHALLENGED (single-cycle is positive evidence but is not a baseline by literature standards; throughput-only is Goodhartable per PRESUMPTION-123)

  STEELMAN:
    Item: ASSUMPTION-102
    Strongest counterargument: An "operational baseline" by SRE / DORA / queueing-theory standards requires sustained multi-period observation and multi-metric design. Single-cycle drain at 20/cycle is a positive data point but is one observation; treating it as baseline is canonical Goodhartable failure mode. The C2A2 cycle simultaneously emits 0% INCORPORATE rate and growing REVISE backlog — exactly the quality regression that Goodhart's Law predicts when throughput becomes the target. The "present queue scale" framing is also under-specified — the 2026-05-05 cycle handled 77 items (20 + 57 retriggered); the 2026-05-09 cycle handled 20; throughput per item differs.
    What would need to be true for C2A2 to be safe: (a) ≥3 consecutive cycles of stable drain rate; (b) throughput paired with INCORPORATE-rate / REVISE-backlog / quality-drift metrics; (c) queue-scale envelope specified.
    How to test: Observe drain rate across the next 3 cycles; track INCORPORATE rate and REVISE-backlog growth alongside throughput; document the queue-scale envelope explicitly.
