SEARCH-AGAINST-PRESUMPTION-299:
  Date searched: 2026-06-03
  Original item: PRESUMPTION-299
  Original statement: [inferred] The 10x cap raise (2000->20000) presumes graceful performance across the whole new range; it was validated only against the present 2529-node case, with no characterization between ~2.5k and 20k nodes.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-299
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as scale-blindness across the permitted range.
      15b: Searched when a generous cap needs no characterization for a slowly-growing dataset; YAGNI on perf testing.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. YAGNI on perf characterization for slow-growing data (KISS/YAGNI; prior PRESUMPTION-288 FOR lineage). — The dataset grew to 2529 nodes over ~190 days of project life; characterizing 2.5k–20k now tests a range the data will not reach for a long time, if ever. Perf-testing unused ranges is speculative work.
    2. The cap is a guard, not a performance promise. — MAX_NODES exists to prevent a hard crash, not to certify smooth interaction at every count; "graceful across the whole range" may be a stronger claim than the cap was ever meant to make. Mild slowdown between 2.5k and 20k is acceptable degradation, not a failure.
    3. Cheaper alternative to full characterization: a runtime warning. — Existing crash-proofing already warns at 80% of cap; a soft warning as the graph grows gives early notice without a perf-sweep up front (event-driven rather than pre-emptive testing).

  Strength of challenge: Moderate

  Summary: The challenge concedes the uncharacterized range (15a is correct that 20000 is untested) but disputes that characterizing it now is warranted. For a dataset that took ~190 days to reach 2529 nodes, the 2.5k–20k range is a speculative future; YAGNI argues against perf-sweeping it pre-emptively. The cap's job is crash-prevention, not a smoothness guarantee, so some mid-range slowdown is tolerable degradation rather than the failure the presumption implies. A cheap soft-warning as the graph approaches problematic sizes substitutes for an up-front characterization. The real disagreement with 15a is timing: test-when-approaching vs test-now.

  Specific risks: Deferring characterization risks a slowdown/crash IF growth unexpectedly accelerates and no warning fires first; pre-empting it spends effort on a range that may never be used. A growth-triggered warning bounds the downside cheaply.

  Mitigations available: Keep the existing 80%-of-cap warning but re-anchor it to a measured cliff once known; add a one-time lightweight check at the next significant growth step rather than a full sweep now; treat 20000 as a provisional guard, explicitly labeled untested, not a verified safe ceiling.

  STEELMAN:
    Item: PRESUMPTION-299
    Strongest counterargument: For a dataset that grows slowly, perf-characterizing 2.5k–20k now is speculative YAGNI; the cap is a crash guard, not a smoothness certificate, and a cheap growth-triggered warning gives early notice without an up-front sweep. The uncharacterized range is a real but low-probability, well-telegraphed risk, not a present defect.
    What would need to be true for C2A2 to be safe: Growth stays slow AND a warning fires before the graph reaches problematic sizes, so characterization can happen just-in-time rather than pre-emptively.
    How to test: Confirm a growth-triggered warning exists and fires below the (eventually measured) cliff; if so, defer the full sweep; if growth accelerates, run the sweep then.

  Recommendation: PARTIALLY-CHALLENGED
