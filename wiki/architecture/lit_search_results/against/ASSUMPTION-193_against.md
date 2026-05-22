SEARCH-AGAINST-ASSUMPTION-193:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-193
  Original statement: "PRS network grown to 231/90/35 + 32-coil layer (from 133/54/20); 231-vs-225 divergence."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-193
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: PRS network counts grown to 231/90/35 + 32-coil layer; a 231-vs-225 divergence noted across sources.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Bailis, P. & Ghodsi, A. (2013). "Eventual Consistency Today." — A persistent (non-converging) divergence between sources signals a real reconciliation bug, not benign lag; 231-vs-225 must be shown to converge.
    2. Redman, T. (2001). "Data Quality." — Cross-source count mismatch is a data-quality defect until reconciled to a single source of truth; assuming it is expected is itself a risk.

  Strength of challenge: Moderate

  Summary: The counter: 'divergence is expected' is only true for transient, converging differences. A 231-vs-225 gap that persists across reads is a reconciliation defect, and treating it as benign (PRESUMPTION-212's failure mode) hides a real inconsistency feeding the Pattern Detector. The challenge is moderate: the gap needs to be reconciled to determine whether it is lag or a bug.

  Specific risks: Pattern Detector ingests inconsistent counts; downstream Pathway-13 analysis built on the wrong figure.

  Mitigations available: Reconcile 231 vs 225 to a single source of truth; identify which source/derivation produces each; assert a single count invariant.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-193
    Strongest counterargument: Cross-source count divergence is only benign if it converges; a fixed 231-vs-225 gap is a reconciliation defect masquerading as eventual-consistency lag. Assuming it is expected is exactly PRESUMPTION-212.
    What would need to be true for C2A2 to be safe: Safe once the two counts are traced to their derivations and reconciled, or one is declared authoritative.
    How to test: Recompute both counts from the same snapshot; if they still differ, it is a derivation bug, not lag.
