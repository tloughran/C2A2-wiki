SEARCH-AGAINST-PRESUMPTION-428:
  Date searched: 2026-07-01
  Original item: PRESUMPTION-428
  Original statement: "[inferred] That a wrong audit CSV is acceptable if vault content is correct + a guard is added — treats provenance correctness as secondary to the artifact."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-428
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from the audit-CSV divergence handling
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Data-provenance/audit literature (Actian, OpenCorporates, Atlan) — for an audit trail, the trail IS the product: "policy compliance cannot be validated without provenance data"; a divergent audit trail voids the guarantee the audit exists to provide, regardless of whether the underlying data is correct.
    2. Regulatory data-lineage (Alex Solutions, OvalEdge) — trustworthiness requires that every element be traceable to source; an audit record known to be wrong is worse than none because it can be trusted as authoritative.
    3. C2A2-internal self-reference: this is the provenance_protocol.md domain — the system's own epistemic-honesty machinery. Accepting a wrong provenance artifact contradicts the protocol's stated purpose (chain-of-custody a downstream reader can trust).

  Strength of challenge: Strong

  Summary: For an audit/provenance artifact, correctness of the trail is not secondary — it is the whole value. A wrong audit CSV that is nonetheless trusted is a provenance failure even when the vault content happens to be right, and it is especially corrosive in a system (C2A2) whose entire self-awareness pipeline rests on trustworthy provenance chains. A forward guard prevents recurrence but does not repair the known-wrong record.

  Specific risks: The wrong CSV is later trusted as authoritative provenance; the system's chain-of-custody guarantee is silently false; future audits build on a corrupt baseline.

  Mitigations available: Correct the audit CSV to match reality (regenerate from source-of-truth), THEN add the guard; treat provenance correctness as a first-class deliverable equal to vault content.

  STEELMAN:
    Item: PRESUMPTION-428
    Strongest counterargument: Under time pressure, triage order (fix what users read, stop the bleeding with a guard, backfill the audit) is legitimate incident response — the presumption is only wrong if "acceptable" means "permanent," and defensible if it means "acceptable as an interim state with the correction queued."
    What would need to be true for C2A2 to be safe: The wrong CSV is explicitly queued for correction (owned OPEN item), not left as the end state.
    How to test: Confirm a follow-up commit regenerates the audit CSV correctly; assert CSV matches vault.

  Recommendation: CHALLENGED (Strong — an audit trail's correctness is the product; a known-wrong CSV must be corrected, not just guarded)
