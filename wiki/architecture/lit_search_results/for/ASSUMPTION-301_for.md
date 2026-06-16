SEARCH-FOR-ASSUMPTION-301:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-301
  Original statement: Substrate-layer reveal behavior is correct because it shares the admission code path already verified for the projected/flow layers (verification claimed from code-path identity after direct observation stalled the renderer).

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-301
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted stated assumption from architecture work log (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Rothermel, G. & Harrold, M.J., 1997. "A Safe, Efficient Regression Test Selection Technique." ACM TOSEM. — Formalizes conditions under which unchanged/shared code paths license skipping re-verification; the strongest principled grounding for inference-from-path-identity.
    2. Wang, M. et al., 2024. "TransferFuzz: Fuzzing with Historical Trace for Verifying Propagated Vulnerability Code." arXiv:2411.18347. — Vulnerability-propagation work assumes shared code implies shared behavior strongly enough to direct verification effort; indirect support for path-identity inference.
    3. Microsoft Learn (testing guidance). "Common Test Patterns and Reuse of Test Designs." — Practitioner precedent for transferring test designs/assurance across reused code, while noting calling-context preconditions can mask or expose bugs.
  Strength of support: Weak
  Summary: There is genuine precedent for drawing assurance from code-path identity: safe regression test selection proves that if the executed path is provably unchanged, prior verification carries over, and recurring-bug/vulnerability-propagation research treats shared code as predictive of shared behavior. However, the same literature conditions this on identical execution context (inputs, preconditions, load), and explicitly notes bugs that manifest only when context differs. The substrate layer's differing data volume/visibility state is exactly the kind of context shift the formal results exclude. Support is real but conditional, not categorical.
  Caveats: Transfer holds only if the substrate layer exercises the shared path with equivalent preconditions and scale; the renderer stall that blocked direct observation is itself evidence the contexts differ (load-dependent). Path identity supports plausibility, not verification.
  Search scope: 1 WebSearch ("shared code path bugs manifest different context untested conditions code reuse verification transfer testing"); plus known regression-test-selection literature.
  Recommendation: PARTIALLY-SUPPORTED
