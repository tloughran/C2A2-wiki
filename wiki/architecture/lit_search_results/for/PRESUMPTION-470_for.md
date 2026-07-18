SEARCH-FOR-PRESUMPTION-470:
  Date searched: 2026-07-11
  Original item: PRESUMPTION-470
  Original statement: "Registry counts are interchangeable across agents and clocks — no census protocol (timestamp + rule) governs shared figures."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-470
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced by inference from 2026-07-10 EOD daily run
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. [AccountingTools (Bragg, S.), "How to ensure a proper inventory cutoff" (with SuperfastCPA, "How to Ensure a Proper Inventory Cutoff?"). — Accounting practice has required for over a century exactly what 14b infers is missing: a cut-off convention (a specific time and date at which counting occurs, with inventory movement frozen and boundary transactions assigned to a period by explicit rule). Counts taken without a cut-off are treated as non-comparable and error-generating by definition.]
    2. [Chandy, K.M. & Lamport, L., 1985. "Distributed Snapshots: Determining Global States of Distributed Systems." ACM TOCS 3(1):63-75. — The distributed-systems formalization of the same point: figures read by different processes at different times form a meaningful global state only along a consistent cut; states assembled without a snapshot protocol can describe a global state that never existed. Direct theoretical grounding for "counts are not interchangeable across agents and clocks without a protocol."]
    3. [Aurora Financials, "How to Perfect Your Audit Cut-Off Testing" (representative of audit cut-off testing literature). — Documents that cut-off errors (recording transactions against the wrong period boundary) are a standard, named audit finding with known remediation: define the boundary rule, then test boundary transactions against it. Empirical precedent that shared figures require a timestamp + rule to reconcile.]
  Strength of support: Strong
  Summary: Two independent literatures — one from accounting/inventory control, one from distributed computing — converge on 14b's inference. Accounting cut-off doctrine holds that a count is only meaningful relative to a declared instant and an assignment rule for boundary items, and inventory reconciliation presupposes both. Chandy-Lamport makes the computational version precise: without a snapshot protocol, per-node observations taken at different times can compose into a global figure that corresponds to no actual state of the system, which is a parsimonious explanation for C2A2's registry count discrepancies. The embedded belief that raw counts are interchangeable across agents and clocks has no support in either literature; the surfaced need for a census protocol (timestamp + rule) is directly precedented in both.
  Caveats: Polarity note: literature supports the surfaced deficiency claim and contradicts the embedded interchangeability belief. Chandy-Lamport is stronger machinery than a wiki registry needs — the accounting analogue (declare an as-of timestamp plus a counting rule, reconcile discrepancies against boundary events) is the proportionate precedent. Search scope confidence is high; both literatures are foundational and stable.
  Recommendation: SUPPORTED
