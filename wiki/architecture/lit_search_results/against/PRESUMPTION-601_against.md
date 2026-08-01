SEARCH-AGAINST-PRESUMPTION-601:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-601
  Original statement: [as queued] The HOLD_LIST.md remedy presumes durable state must live where the ingesting phase looks, rather than that a HOLD is a decision and decisions.md is the existing designated register; the fix adds a third state store beside an unused second one.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-601
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from the ingest-regression diagnosis and its remedy
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Microsoft Azure Architecture Center, "CQRS Pattern"; Bogard, J., "Busting some CQRS myths"; event-driven.io, "CQRS facts and myths explained." — The command model is the single source of truth for writes; one or more READ MODELS are legitimate, deliberately duplicated projections shaped for the reader's access pattern. A second store optimised for the reading phase is a named pattern, not an anti-pattern. This directly challenges the item's inference from "a third store" to "a design error."
    2. Evans, E., Domain-Driven Design (bounded contexts); Software Architecture Guild, "Bounded Contexts." — Duplication of the same fact across bounded contexts is expected and correct where the contexts model it differently; SSOT is scoped WITHIN a context, not globally across a system. The item applies SSOT globally without establishing that ingest and decision-recording share a context.
    3. Wikipedia, "Single source of truth." — The doctrine's own statement is that data is edited in one place, while derived/read copies are permitted; it does not prohibit additional stores, it prohibits additional AUTHORITIES. The item's argument needs the stronger prohibition and does not have it.
    4. Nygard, ADR corpus (adr.github.io); Microsoft Well-Architected ADR guidance. — ADRs are specified as records of ARCHITECTURAL decisions, deliberately scoped to be "short and durable" and few in number. Routing a per-item operational HOLD to the architectural decision register is a category expansion the ADR literature does not endorse and which its own guidance (keep ADRs consequential) argues against.
    5. Internal, but decisive and reported per PREMISE-120: decisions.md has been unwritten for 26 consecutive days. Reliability engineering's standard reading of a component with a 26-day observed write failure is that routing new traffic to it increases, not decreases, the probability of loss.

  Strength of challenge: Strong

  Summary: The item's structural diagnosis is defensible but its inferential step is not. "The remedy adds a third state store" is treated as self-evidently faulty, and the mainstream architecture literature does not agree: CQRS read models and bounded-context duplication are explicit, well-established patterns in which a reader-shaped store beside the authoritative one is correct design. SSOT prohibits multiple authorities, not multiple copies — and HOLD_LIST.md as a Phase-1-readable projection of a decision recorded elsewhere would violate nothing. Separately, the item's proposed alternative destination is challenged on its own terms: the ADR literature scopes decision registers to architectural decisions and explicitly counsels against inflating them, and decisions.md's 26-day write failure makes it the less reliable of the two options by direct observation. The item is strongest where it says a HOLD is a decision whose authority should be named; it is weakest where it converts that into an objection to the file.

  Specific risks: If C2A2 acts on the item as stated and routes HOLDs to decisions.md instead of building the Phase-1-readable store, it will have moved a fact from a store that would have been read into one that has not been written for 26 days — converting a propagation failure into a silent-loss failure with no read path at all. The item's framing makes this outcome look like the disciplined choice.

  Mitigations available: Yes, and they are standard: name decisions.md (or a successor) as the AUTHORITY for HOLD facts and generate HOLD_LIST.md as a derived projection with a stated refresh rule — the CQRS answer, which satisfies both the item's classification claim and the remedy it objects to. The failure the item should be pointing at is the absence of a stated authority, not the count of files.

  STEELMAN:
    Item: PRESUMPTION-601
    Strongest counterargument: The number of state stores is not a quality metric, and the literature the item implicitly relies on says the opposite of what the item needs. Modern architecture deliberately multiplies stores — read models, projections, caches, per-context copies — and treats a single physical store as an availability and coupling liability. What matters is whether exactly one store is AUTHORITATIVE and whether the derivation rules from it are stated. The 07-31 remedy is faulted for adding a file; it should be faulted, if at all, for not naming which file wins on conflict. Moreover, the item's preferred destination is empirically the worse one: a register with a 26-day observed write failure. A recommendation that moves data toward a demonstrably non-functioning component, justified by an appeal to conceptual tidiness, is the more dangerous of the two errors on the table.
    What would need to be true for C2A2 to be safe: (a) an authority is named for HOLD facts and the derivation from it to any read-shaped store is written down; (b) decisions.md's write path is repaired and demonstrated before anything is routed to it; (c) the count of stores is dropped as a criterion in favour of the count of unreconciled authorities.
    How to test: Enumerate every fact class in the wiki and, for each, count the stores that can be WRITTEN independently (authorities) versus stores that are derived. The item's thesis predicts the authority count is inflated; the counter-thesis predicts the authority count is fine and only the derivation rules are missing. Both are computable from the existing file set — denominator is the fact-class list, not a per-run count, so this escapes the PRESUMPTION-604 problem.

  Recommendation: PARTIALLY-CHALLENGED
