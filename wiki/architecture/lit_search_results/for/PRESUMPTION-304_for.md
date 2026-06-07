SEARCH-FOR-PRESUMPTION-304:
  Date searched: 2026-06-05
  Original item: PRESUMPTION-304
  Original statement: [inferred] The 36-vs-152 PROCESSED_LOG conflict is presumed a cosmetic format artifact resolvable by a later tidy — presuming 36 is correct and 152 carries no lost data, i.e., a narrative log can double as a machine-diffable system-of-record once cleaned.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-304
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated presumption that the count conflict is cosmetic and that a narrative log can serve as a machine-diffable system-of-record after a later cleanup.
      15a: Searched data-completeness audit patterns and narrative-vs-structured operational-log reconciliation.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Lemaire, A. "Event Sourcing, Audit Logs, and Event Logs." Sunday/Medium, 2026. — Narrative/audit records and structured state-change records are legitimately different projections of one history; a heterogeneous log routinely yields divergent counts under different reads without data loss. Supports that 36-vs-152 CAN be a projection artifact rather than missing files.
    2. Fowler, M. "Event Sourcing." martinfowler.com. — A log can serve as system-of-record with derived projections; supports the presumption that, in principle, a cleaned log can be made machine-diffable so the canonical count is recoverable deterministically.
    3. Microsoft Learn, "Event Sourcing Pattern." Azure Architecture Center. — Establishes that mixed-content logs are made authoritative by imposing explicit record schema and fold rules — i.e., "tidy later" is a recognized, achievable end-state, not wishful thinking.

  Strength of support: Weak-Moderate

  Summary: The literature supports the POSSIBILITY embedded in the presumption — a heterogeneous narrative log can, after structuring, double as a machine-diffable system-of-record, and a count divergence can be a pure projection artifact with no lost data. What it supports much more weakly is the presumption's confident DIRECTION — that 36 is correct and 152 carries nothing real — which is asserted in advance of the tidy rather than demonstrated by it. The supportive case is essentially "this is a solvable, well-understood class of problem," not "the optimistic reading is the right one." Note this item is the inferred (PRESUMPTION) twin of ASSUMPTION-271 and inherits the same FOR/AGAINST structure; as a presumption it carries less designer-scrutiny weight.

  Caveats: Support is for feasibility, not for the presumed answer. The same event-sourcing guidance insists the canonical count be PROVEN by applying the fold, and the data-reconciliation literature (see 15b) treats "assume the smaller count is correct and the larger carries no loss" as the precise failure mode that hides silent data loss. So the FOR case explicitly does not license acting on 36 before the reconciliation runs.

  Recommendation: PARTIALLY-SUPPORTED
