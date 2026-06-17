SEARCH-AGAINST-ASSUMPTION-326:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-326
  Original statement: "Build the metric before iterating the view layer that depends on it ('cart-before-horse' sequencing)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-326
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the sequencing decision (metric before view)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Iterative/agile & data-visualization practice — strict "define the metric fully first" can be a waterfall anti-pattern; cheap exploratory views frequently SURFACE defects in a metric's definition (edge cases, ambiguous semantics) that pure up-front specification misses. The dependency can run both ways.
    2. Co-evolution of measure and display (exploratory data analysis, Tukey) — visualization is itself a validation instrument for the metric; sequencing the view strictly after a "finished" metric forgoes that diagnostic feedback.

  Strength of challenge: Weak-Moderate

  Summary: The sequencing is sound as dependency-ordering (15a), but the challenge is to a STRICT reading: building the metric fully before any view can forgo the diagnostic value of cheap prototype views, which often expose metric-definition flaws (EDA/Tukey; the view validates the measure). "Metric strictly before view" risks a mini-waterfall; the better practice is metric-first but with throwaway views used to pressure-test the definition. Weak-moderate because the core ordering is still correct.

  Specific risks: A metric finalized without any visual pressure-testing ships with undetected definitional edge-cases; the "finished" metric then anchors the view design (and PRESUMPTION-360's over-trust) before its flaws surface.

  Mitigations available: Keep metric-first but build a deliberately rough, disposable view early to stress the metric definition; treat the view as a validation instrument; don't harden the production view until the metric survives that probe.

  STEELMAN:
    Strongest counterargument: Designing a polished view against an undefined metric guarantees rework and is the very "cart-before-horse" error being avoided; insisting on a metric definition first is simply respecting the dependency, and nothing in metric-first forbids a quick exploratory sketch.
    What would need to be true for C2A2 to be safe: "Metric first" is interpreted as "define + cheaply pressure-test the metric," not "fully finalize the metric in isolation," so the view's diagnostic feedback is not lost.
    How to test: Did any view-building surface a metric-definition problem after the metric was declared "built"? If yes, the strict ordering left value on the table.

  Search scope: iterative vs waterfall sequencing; EDA/visualization as metric validation; measure-display co-evolution. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
