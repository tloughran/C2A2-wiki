SEARCH-FOR-PRESUMPTION-601:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-601
  Original statement: The ingest regression is diagnosed as a memory failure of Phase 1 ("PROCESSED_LOG is the only durable state, and a HOLD leaves no mark in it") and the fix proposed is a new file, inbox/HOLD_LIST.md, that Phase 1 reads. This presumes durable state must live wherever the ingesting phase happens to look, rather than that a HOLD is a *decision* and the system already has a register for decisions (decisions.md, designated authority, unwritten for 26 days). The remedy adds a third state store beside a second one that is not being used.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-601
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from the 2026-07-31 chat summary's ingest-regression diagnosis and its proposed remedy
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Wikipedia / Mad Devs / MuleSoft SSOT summaries, accessed 2026-08-01. — Single source of truth is stated as a data-architecture principle in which each datum is edited in exactly one authoritative place; duplication across stores is named as the failure mode the principle exists to prevent. Tertiary sources; treated as evidence of a settled engineering convention, not as primary research.
    2. IBM, "System of Record vs. Source of Truth." — Distinguishes the system of record (authoritative for a class of facts) from downstream copies; supports the item's core move, that the question "where does a HOLD live?" is answered by asking which register is authoritative for that class of fact, not by asking which phase reads which file.
    3. Nygard, M., 2011. "Documenting Architecture Decisions"; adr.github.io ADR corpus; Microsoft Azure Well-Architected Framework, "Maintain an architecture decision record." — A decision is a first-class, durably recorded artifact with its own register; the collection of ADRs constitutes the decision log. Directly supports the item's classification of a HOLD as a decision rather than as phase-local state.
    4. Microsoft Learn (Well-Architected), 2025. — States the operational consequence: decisions not recorded in the decision log are re-litigated or lost when the recording context changes. This is the mechanism by which the 07-27 HOLD failed to reach the 07-31 ingest.

  Strength of support: Moderate

  Summary: The literature supports the item's structural claim on two independent legs. First, SSOT/system-of-record doctrine holds that state should be persisted where it is authoritative, not where it is convenient to read; adding a third store for a fact class that an existing register already owns is the canonical anti-pattern that doctrine names. Second, the ADR literature treats a decision as an artifact requiring its own durable record with rationale, which is exactly the category a HOLD falls into — a human judgment to defer, which a later, differently-scoped phase must be able to read. Both legs converge on the item's diagnosis: the fix considered was scoped to Phase 1's read path because that is the path that failed, not because that is where the fact belongs. The support is for the *classification* (a HOLD is a decision) and for the *anti-pattern* (proliferating stores), not for any specific remedy.

  Caveats: (1) The sources are engineering convention and tertiary summaries, not primary empirical research; no measured comparison of one-register versus many-register designs was found. (2) SSOT doctrine is about data, and a HOLD is arguably a workflow state rather than a datum; the transfer is analogical. (3) The strongest fact against the item's own remedy direction is internal, not literature-based: decisions.md has been unwritten for 26 days, so routing to it is routing to a register with a demonstrated write failure — the literature says nothing about which of two non-functioning options is better. (4) Search scope: SSOT, system-of-record, ADR/decision-log. NOT searched: workflow-engine state-management literature (BPMN/durable execution), which may bear.

  Recommendation: SUPPORTED
