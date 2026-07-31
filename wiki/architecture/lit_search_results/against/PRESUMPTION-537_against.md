SEARCH-AGAINST-PRESUMPTION-537:
  Date searched: 2026-07-24
  Original item: PRESUMPTION-537
  Original statement: [inferred] A clean, self-evident separability between literature-testable and internal-empirical claims is presumed, though all 34 sat in one queue until hand-sorted — no intake gate encodes the distinction.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-537
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from a lit-vs-internal split applied retrospectively
      15b: Searched for evidence that a workable empirical/internal demarcation exists
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Popper, K. (1959). Falsifiability. — Provides an operational, decidable-enough test (is there a possible observation that would bear on this claim?) that in practice separates empirically-testable from internal/analytic claims well enough to route work.
    2. Practical claim-triage in evidence-based practice (PICO framing, systematic-review inclusion criteria). — Working demarcation criteria are routinely and reliably applied by trained reviewers; the hand-sort's success is evidence that an operational line exists.
    3. Machine-learnability of text-type classification. — Claim-type classification is a standard, high-accuracy supervised task; the absence of a philosophically sharp boundary does not prevent a high-precision operational classifier.

  Strength of challenge: Moderate

  Summary: The presumption over-reads the difficulty. Although no PRINCIPLED analytic/empirical boundary exists (Quine), a workable OPERATIONAL criterion does — Popperian falsifiability plus the demonstrated success of the hand-sort and of routine claim-triage in evidence-based practice. The gap the presumption names is real (no intake gate encodes it) but the fix is cheap and the distinction is operationally learnable, so the "clean separability" worry is more a missing-feature note than a deep vulnerability.

  Specific risks: Over-weighting the philosophical difficulty could stall building a simple, useful intake classifier.

  Mitigations available: Build the classifier with a "route-to-human when uncertain" fallback; measure precision against the hand sort (the item's in-house test).

  STEELMAN:
    Item: PRESUMPTION-537
    Strongest counterargument: The 26-item misrouting already happened — that is direct evidence the distinction is NOT self-evident in practice, and an unencoded criterion will keep misrouting at some rate. A criterion that lives only in a hand-sorter's head is not a system property.
    What would need to be true for C2A2 to be safe: the distinction must be encoded in an intake gate with measured precision/recall; relying on retrospective hand-sorting guarantees recurring misroutes.
    How to test: build the intake classifier; measure lit-vs-internal precision against the hand sort.

  Recommendation: PARTIALLY-CHALLENGED (operational demarcation is achievable; the missing-gate concern stands)
