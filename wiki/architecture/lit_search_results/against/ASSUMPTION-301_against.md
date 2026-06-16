SEARCH-AGAINST-ASSUMPTION-301:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-301
  Original statement: Substrate-layer reveal behavior is correct because it shares the admission code path already verified for the projected/flow layers (verification claimed from code-path identity after direct observation stalled the renderer).

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-301
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption from architecture record (code-path-identity verification claim)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Leveson & Turner, 1993. "An Investigation of the Therac-25 Accidents." IEEE Computer. — Canonical case of reused, "already proven" software failing catastrophically when the same code ran in a new operating context; code identity did not transfer safety.
    2. Lions et al., 1996. "Ariane 5 Flight 501 Failure: Report by the Inquiry Board." ESA. — Reused Ariane 4 alignment code, verified for its original flight profile, failed under Ariane 5's data conditions: identical code path, different inputs, total loss.
    3. Heicon (engineering practice survey), "Static analysis and dynamic testing: strengths and weaknesses" (heicon-ulm.de) — a system that has only been structurally argued/statically analysed "has no proof of functional correctness"; runtime behavior must be observed.
    4. Real-world shared-path bug reports (e.g., Docker moby#48731; Jest #15358) — same code path produces divergent behavior under different invocation contexts and data shapes.
  Strength of challenge: Strong
  Summary: The literature consistently treats code-path identity as necessary but not sufficient for behavioral correctness. The substrate layer pushes different data (node sets, counts, attribute states, timing) through the "same" admission path, and the most famous failures in software engineering (Therac-25, Ariane 5) are precisely reused-and-trusted code meeting new input regimes. Notably, the verification stall itself (renderer stalling under substrate load) is evidence the substrate context is NOT equivalent — the very condition that blocked observation is a context difference. Equivalence claims require an argument that the input/state envelope is identical, which is not established here.
  Specific risks: Substrate reveal could silently mis-admit or drop nodes/edges under load or ordering conditions unique to that layer; the bug class most likely (load-dependent, state-dependent) is exactly the class code-identity arguments cannot exclude; downstream narration and filter counts would be wrong without any validator alarm.
  Mitigations available: Verify behaviorally on a reduced dataset (small substrate slice) where the renderer does not stall; add an admission-count invariant check (expected vs admitted nodes) that runs even when visual confirmation is impossible; log admission decisions per layer and diff against projected/flow runs.
  STEELMAN:
    Strongest counterargument: If the admission function is pure, takes the same parameter types, and the substrate inputs fall strictly within the input envelope already exercised by projected/flow layers, then code identity plus envelope containment is a legitimate verification argument — this is how regression arguments work in practice, and re-verifying every caller of every shared function is neither feasible nor standard.
    What would need to be true for C2A2 to be safe: Admission path is pure/stateless; substrate input distribution (sizes, attribute values, call ordering) is contained within the already-verified envelope; no load-dependent branches (timeouts, budgets, batching) exist in the path.
    How to test: Run substrate reveal on a 10% subsample where rendering completes; assert admitted-set equality against an offline recomputation of expected admissions.
  Search scope: 1 WebSearch ("shared code path bug manifests different context untested configuration..."); plus established reliability literature (Therac-25, Ariane 5).
  Recommendation: CHALLENGED
