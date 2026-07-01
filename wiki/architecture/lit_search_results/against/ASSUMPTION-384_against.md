SEARCH-AGAINST-ASSUMPTION-384:
  Date searched: 2026-06-29
  Original item: ASSUMPTION-384
  Original statement: "The 2,337 orphan count is an artifact of excluding shared-reference edges + counting structural/inbox pages that shouldn't carry backlinks - not a real knowledge-graph deficit."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-384
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: orphan metric framed as artifact rather than deficit
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Measurement-artifact reasoning cuts both ways. - The same edge-type sensitivity that inflates the count can be used to explain away a genuine deficit; absent a recomputation, "artifact" is an assertion, not a demonstration.
    2. Implicit-edge inflation of connectivity. - Admitting shared-reference edges can OVERSTATE connectedness (any two pages citing a common source become "connected"), so re-including them may hide real orphans rather than reveal false ones.
    3. Structural/inbox pages still need navigability. - Even if structural pages "shouldn't" carry backlinks by convention, dated inbox pages that never get triaged are a real findability deficit, not a pure counting artifact.

  Strength of challenge: Moderate

  Summary: The "artifact" framing is convenient but unverified: it predicts the count would shrink under a different edge set, yet shared-reference edges are so permissive that re-including them can manufacture connectivity and mask true orphans. Reclassifying structural/inbox pages as "expected to be orphans" risks defining away a genuine triage backlog. Without an actual recomputation, the deficit-vs-artifact question is undecided, and the optimistic reading is unproven.

  Specific risks: Explaining away orphans could suppress a real findability problem (untriaged inbox, genuinely disconnected content); over-counting shared-reference edges could create false confidence.

  Mitigations available: Actually recompute orphans under the proposed edge set and node filter; report the residual; treat untriaged inbox separately from structural pages.

  STEELMAN:
    Item: ASSUMPTION-384
    Strongest counterargument: "It's an artifact" is the kind of claim that should be demonstrated by recomputation, not asserted; and since shared-reference edges are extremely permissive, including them risks inflating connectivity and hiding orphans that are real - so the optimistic framing could be exactly backwards.
    What would need to be true for C2A2 to be safe: A recomputation with the corrected edge set + node population still leaves a small, explainable residual, AND the included shared-reference edges represent genuine, usable relations.
    How to test: Run the corrected orphan computation; inspect a sample of the "now-connected" pages to confirm the shared-reference links are meaningful.

  Search scope: Edge-type sensitivity; implicit-edge inflation; inbox/structural handling. Adequate.

  Recommendation: PARTIALLY-CHALLENGED
