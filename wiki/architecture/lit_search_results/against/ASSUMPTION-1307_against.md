SEARCH-AGAINST-ASSUMPTION-1307:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1307
  Original statement: "**Four of the 36 cards approved a pointer, not a reading** (FINDING-089) — each
    said so itself and asked to be caught... **A batch APPROVE can't distinguish 'read and agreed' from
    'not read separately.'**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1307
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed. Six of thirty-six cards in the network's largest ingest are of
        uncertain warrant on the run's own account, and all thirty-six were ingested anyway, flagging
        rather than holding.
      15b: Searched for challenging literature; found that class-level approval IS a valid warrant form
        in the best-developed regulatory analogue, and that heavyweight item-level approval is measurably
        NOT the control it is assumed to be — but neither rescues the specific act taken here.
    Current status: PARTIALLY-CHALLENGED

  Register pre-check:
    - PREMISE-172 (ACTIVE) — "A PASS MARK IS A VERDICT ABOUT A (READER, FRAME, SCOPE) READING — NOT A
      PROPERTY OF THE FILE... a mark carries no information about what was NOT examined." This is an
      almost exact pre-answer to the assumption's stated limb, already ACTIVE.
    - PREMISE-176 (ACTIVE) — "FOR AN IRREVERSIBLE OPERATION, REVIEW IS NOT A CONTROL; REVERSIBILITY IS."
      **This is the hinge.** It relocates the whole question from approval granularity to whether the
      ingest was reversible.
    - PREMISE-117 (ACTIVE) — continuing to publish under an unresolved definitional dispute is codified
      practice: publish-then-revise with a revision flag. Supports flag-and-ingest.
    - PREMISE-090 (ACTIVE) — for a one-time quality-sensitive backlog whose extraction errors propagate
      into a validated-premise register, an attended (HITL) pass is justified. Cuts the other way.
    - PREMISE-050 (ACTIVE) — drain in small scoped batches, not one bulk run. A 36-card single APPROVE is
      the configuration this premise advises against.
    - PREMISE-103 (ACTIVE) — absence of primary text is a KIND-difference in evidence: no confidence
      label over metadata-only material is well-founded, and downgrading confidence is not a valid
      substitute for an explicit "unfounded pending retrieval" state. **Directly governs the four
      pointer-cards** and denies the flag-and-ingest disposition for them specifically.
    - PREMISE-121 (ACTIVE) — review-queue acceptance is a function of workload, not item merit; override
      rates 49-96%. Predicts exactly what a 36-item batch produces.
    - PREMISE-201 (ACTIVE) — amending a gate threshold is not the intervention; the intervention is
      amendment paired with a retained measurement of what is still caught.

  Challenging evidence found: Partial

  LIMB STRUCTURE — three limbs, and the recommendation splits across them:
    LIMB A — "a batch APPROVE cannot, as an artefact, distinguish read-and-agreed from not-read."
      (An information-theoretic claim about the record.)
    LIMB B — "therefore a batch approval cannot carry item-level warrant." (A normative claim.)
    LIMB C — "flagging rather than holding was nonetheless the right disposition for the six."
      (The action actually taken; not stated as an assumption but entailed by the run.)

  Sources:
    1. 45 CFR § 46.110 — Expedited review procedures (eCFR / Cornell LII). — SECONDARY (regulation text
       summarised from two independent hosts; I read the summaries, not the full section) — **Class-level
       approval is a valid, codified warrant form.** The Secretary publishes CATEGORIES of research; an
       IRB may approve anything in a listed category via a single designated reviewer exercising all the
       authorities of the full board. Item-level full-board deliberation is explicitly not required. This
       falsifies the strongest reading of LIMB B: aggregated authorisation *can* carry item-level warrant,
       provided the class is pre-specified and a bounded exception rule exists (here: the reviewer may
       not DISAPPROVE under expedited procedure, which is the structural safeguard).
    2. 45 CFR § 46.116(d) — Broad consent, with limited IRB review under § 46.104(d)(7). — SECONDARY —
       Broad consent to a *described class* of future uses is a recognised pathway; what it is NOT is
       blanket approval. The distinction found in the literature is precise and unhelpful to the run:
       broad consent keeps a review gate in the loop for each downstream use, and "blanket consent" has
       no definition in the Common Rule, FDA regulations or ICH E6 at all. So the valid form of
       class-approval is *class + per-use gate*, which the 36-card single APPROVE did not have.
    3. DORA / *Accelerate* State of DevOps research on change approval (dora.dev capability page;
       2019 Accelerate State of DevOps Report). — SECONDARY (capability pages and report landing page
       retrieved via search; I did not read the report's statistical appendix, so the "2.6x" figure is
       SECONDARY and the "negatively correlated with lead time, deployment frequency and restore time,
       no correlation with change fail rate" finding is SECONDARY) — **This is the substantive
       challenge.** External item-level approval boards are negatively associated with delivery
       performance and show NO association with lower change-failure rates; organisations with formal
       external approval are reported ~2.6x more likely to be low performers. The recommended substitute
       is lightweight peer review plus automated detection — i.e. the field's best-measured answer is
       that approval granularity is the wrong lever and detection/reversibility is the right one.
    4. PREMISE-176 (in-register, ACTIVE) — VERIFIED (read in `premises_index.md`) — reframes the item: if
       ingest is reversible (tombstone / quarantine / staged removal), flag-and-ingest is defensible and
       the granularity of the APPROVE is second-order. If it is not, no approval granularity saves it.

  Strength of challenge: Moderate (LIMB A: None — it is analytically true and PREMISE-172 already carries
    it. **LIMB B: Moderate-to-Strong** — expedited review is a working counterexample. LIMB C: None —
    nothing found supports flag-and-ingest for the four pointer-cards, and PREMISE-103 denies it.)

  Summary: The assumption is stated too strongly and the regulatory analogue it invites is the one that
    refutes it. Class-level approval demonstrably can carry item-level warrant: expedited IRB review
    approves by pre-published category through a single designated reviewer with full board authority.
    What makes that valid is not the reviewer's per-item reading but three structural features the C2A2
    batch lacked — a pre-specified class, a bounded scope (minimal risk), and an asymmetric authority
    (the expedited reviewer may approve but may not disapprove). The DevOps evidence pushes the same way
    from a different domain: heavyweight item-level approval is not measurably protective, and the
    protective factors are peer review, automated detection and reversibility. So LIMB B is challenged.
    But none of this rescues LIMB C. The four pointer-cards are metadata-only material, and PREMISE-103
    (ACTIVE) holds that no confidence label over metadata-only material is well-founded and that
    downgrading is not a substitute for an explicit "unfounded pending retrieval" state. Flagging them
    and ingesting them anyway is precisely the substitution PREMISE-103 denies.

  Specific risks: If LIMB B is false in the direction found here, the estate's remedy instinct — split
    the batch, approve item by item — costs throughput and buys nothing measurable, while the actual
    exposure (six cards of uncertain warrant now inside the largest ingest in the network's history,
    feeding 85 PRS triplets and CROSS-132..135) goes untreated. The compounding risk is ASSUMPTION-1295's:
    if ingest is licensed by ID alignment rather than by approval, then the APPROVE was never the control
    at all and its granularity is irrelevant — in which case the estate believes it has a gate it does
    not have. That is the PREMISE-187 failure: a gate that appears to check what it cannot decide is
    worse than no gate.

  Mitigations available:
    - Answer the reversibility question first (PREMISE-176). Can the 36 cards, the 85 triplets and
      CROSS-132..135 be reverted? If yes, flag-and-ingest is defensible and the batch size is a
      throughput question. If no, this is the finding, not the approval granularity.
    - Adopt the expedited-review structure rather than rejecting class approval: pre-declare the CLASS a
      batch APPROVE may cover (e.g. "cards with retrieved primary text and no self-declared caveat"), and
      make any card outside the class fall out of the batch automatically. The four self-identified — the
      machinery to route them already exists in the cards themselves.
    - Give the four pointer-cards the PREMISE-103 state they require: `UNFOUNDED-PENDING-RETRIEVAL`, not
      `INGESTED (flagged)`. The "queue retrieval after 2026-09-24" card supplies its own review date.
    - Per PREMISE-201, if the batch gate is kept, retain a measurement of what it still catches —
      otherwise its precision is unknown and the gate is decorative.

  STEELMAN:
    Item: ASSUMPTION-1307
    Strongest counterargument: The claim is about what the *artefact* records, not about what is
      procedurally permissible, and on that reading it is simply true: one APPROVE over 36 heterogeneous
      cards is a single bit, and no later reader can recover from it which cards were read. The expedited-
      review counterexample does not touch this, because expedited review carries a per-item determination
      recorded against a pre-published category — the record retains item-level structure even though the
      deliberation was lightweight. The C2A2 batch retained none. Moreover PREMISE-121 predicts that at
      36 items acceptance tracks workload rather than merit, and the run's own account confirms it: six
      cards flagged themselves and were ingested regardless. The assumption is the correct diagnosis of a
      record-keeping defect, and the fact that heavyweight boards do not help is beside the point, since
      nobody is proposing a board.
    What would need to be true for C2A2 to be safe: (1) the ingest is reversible at item granularity;
      (2) the APPROVE is not in fact the licensing step (ASSUMPTION-1295 must be settled either way, and
      if ID alignment is the real license, the estate must stop describing APPROVE as a control);
      (3) the four pointer-cards are held in an explicit unfounded state rather than ingested-with-flag;
      and (4) there exists a downstream detector that would catch a bad card that slipped through, so the
      system does not depend on the approval being the only gate.
    How to test: Seed the next batch. Insert 3 synthetic cards with known defects of the pointer-card
      type into a 30-card batch and observe whether the batch APPROVE path surfaces them, whether they
      are ingested, and whether any downstream check catches them. This is the seeded-defect design
      PREMISE-162 already names as the only way to get a denominator for a self-audited detector, and it
      converts "a batch APPROVE can't distinguish" from an assertion into a measured escape rate.

  Search scope: comprehensive on the regulatory-analogue and change-approval angles; preliminary on
    consent granularity in data protection. Searched: broad consent and the 2018 Common Rule; expedited
    IRB review categories and single-reviewer authority; "blanket approval" as a regulatory term; IRB
    rubber-stamping; DORA/Accelerate change approval and CABs; batch size in change management. NOT
    searched: GDPR purpose-limitation and granular-consent case law (which likely runs FOR the
    assumption), and the auditing literature on block sampling vs item-level testing, which is the
    closest quantitative analogue and would be the best next search.

  Recommendation: PARTIALLY-CHALLENGED — resting on LIMB B only. LIMB A stands (and is already
    PREMISE-172). LIMB C is NOT challenged and is arguably strengthened: nothing found here licenses
    ingesting the four metadata-only cards, and PREMISE-103 forbids it.
