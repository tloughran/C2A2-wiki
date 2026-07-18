SEARCH-AGAINST-PRESUMPTION-470:
  Date searched: 2026-07-11
  Original item: PRESUMPTION-470
  Original statement: "Registry counts are interchangeable across agents and clocks — no census protocol (timestamp + rule) governs shared figures."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-470
    Item type: PRESUMPTION (unstated — surfaced by inference, QUEUED-EMPIRICAL)
    Transform at each step:
      14b: surfaced by inference from 2026-07-10 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Chandy, K.M., & Lamport, L., 1985. "Distributed Snapshots: Determining Global States of Distributed Systems." ACM TOCS 3(1):63-75. — Foundational result: in an asynchronous system with no shared clock, independently-taken local observations do not compose into a consistent global state; uncoordinated counts can reflect a state the system never passed through. A coordination protocol (marker/consistent cut) is *required*, not optional, for comparable global figures.]
    2. [Auditing literature on cut-off testing (e.g., Hyperbots, "What is Cutoff Testing?"; AuditingAccounting.com, "Cut-Off Procedures for Bank Balances in Auditing"). — Centuries of accounting practice converged on mandatory cut-off conventions: figures are only comparable relative to a declared close date and recognition rule; timing differences around the cut-off are the classic source of spurious discrepancies, which is why auditors test the days around the boundary specifically.]
    3. [Payment-reconciliation practice literature (e.g., Rexi, "Timing Differences in Payment Reconciliation: When to Investigate"). — Documents "phantom" discrepancies: two correct systems disagree purely because they snapshot at different times or apply different recognition rules; without a shared cut-off, investigation effort is spent on differences that are artifacts of measurement, not errors.]
    4. [Statistical-census practice (dual-system estimation, census.gov methodology; Bird & King 2018). — Every serious enumeration fixes a reference moment ("census night") and inclusion rules before counting, precisely because counts without a reference instant are not comparable across enumerators.]
  Strength of challenge: Strong
  Summary: Three independent disciplines — distributed-systems theory, financial auditing, and official statistics — each independently invented the same requirement: a shared figure needs a declared instant and a declared inclusion rule, or it is not a shared figure. Chandy-Lamport proves the strong version: uncoordinated local snapshots can compose into a global "count" corresponding to no state that ever existed. Accounting cut-off practice shows the operational consequence: reconciliation without a close convention produces phantom discrepancies that consume investigation effort and erode trust in all figures. C2A2's observed count discrepancies between agent registries are the textbook symptom, and — worse — the presumption makes real discrepancies (a lost item, per ASSUMPTION-437) indistinguishable from timing artifacts, so the census problem and the completeness problem mask each other.
  Specific risks: Agents "correct" each other's accurate-but-differently-timed counts, introducing real errors while chasing phantom ones; genuine losses hide inside the noise band of expected timing skew; EOD reports embed incomparable figures that later agents cite as contradictions, generating spurious ASSUMPTION items and audit churn; no discrepancy is ever closable because there is no agreed ground truth to close against.
  Mitigations available: A lightweight census protocol: every shared count carries (a) snapshot timestamp, (b) counting rule (which states/tags included), (c) source registry — three metadata fields, near-zero cost; a designated close ("counts as of 00:00 UTC daily, post-EOD-write, pre-morning-run") that all agents cite; single-writer canonical count with others reconciling against it rather than publishing rivals; discrepancy triage that first tests the timing-artifact hypothesis before treating a difference as real.
  STEELMAN:
    Strongest counterargument: The full rigor of consistent snapshots and accounting close is calibrated to high-frequency, high-stakes environments; a wiki pipeline whose registries change a handful of times daily has long quiescent windows in which any snapshot is trivially consistent, so counts taken hours apart are usually genuinely interchangeable. Imposing close discipline on a small autonomous system adds protocol weight, and small persistent discrepancies may be cheaper to tolerate than to govern — the observed discrepancies may have caused zero actual harm.
    What would need to be true for C2A2 to be safe: Registry mutation frequency is low enough that concurrent counting during a mutation is rare; observed discrepancies are small, transient, and self-resolving by the next quiescent period; and no downstream decision (queue processing, incident detection, completeness claims) keys off exact counts. Note this last condition is already violated if count comparisons are used to detect lost items.
    How to test: For the next observed discrepancy, re-count all registries inside a known quiescent window (no scheduled runs active). If the discrepancy vanishes, it was a timing artifact and a cheap timestamp convention suffices; if it persists, it is a real integrity problem and the census protocol becomes urgent for diagnosis.
  Recommendation: CHALLENGED
