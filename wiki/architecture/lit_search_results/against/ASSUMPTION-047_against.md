SEARCH-AGAINST-ASSUMPTION-047:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-047
  Original statement: "Master-wiki narrative discrepancy should be flagged transparently rather than silently reconciled at the briefing layer"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-047
    Item type: ASSUMPTION (stated) — normative stance
    Transform at each step:
      14a: Extracted from briefing-policy statement
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND (weak)

  Challenging evidence found: No (minor / partial)

  Sources:
    1. Reconciliation-at-source literature (Kimball & Ross 2013 "Data Warehouse Toolkit"): some traditions prefer silent reconciliation at the *data source* so downstream consumers always see a consistent picture. However, this tradition still flags discrepancies upstream — not in the downstream briefing.
    2. Alert-fatigue counterargument (Ancker et al. 2017): *too much* transparency on minor discrepancies can itself be harmful; not every narrative gap warrants a flag. This challenges the *universal* form of the ASSUMPTION but supports its *calibrated* form.
    3. UX-minimalism critique (Krug 2014 "Don't Make Me Think"): user-facing surfaces can be harmed by exposing system state unnecessarily. A briefing is a UX surface, and over-flagging is a valid concern.
    4. "Silent reconciliation is sometimes right" literature (CRDTs; conflict-free replicated data types; Shapiro et al. 2011): some systems are designed to reconcile silently because the reconciliation logic is sound. This challenges the *categorical* form of the ASSUMPTION.

  Strength of challenge: Weak

  Summary: The ASSUMPTION is fundamentally well-grounded, and the literature against it is thin. The strongest challenges are calibration-level, not direction-level: "how much transparency" and "which discrepancies warrant flagging" are valid concerns, but they don't overturn the principle. The universal quantifier ("rather than silently reconciled") could be weakened to "when the discrepancy is consequential" without abandoning the core commitment.

  Specific risks: (a) Briefing noise if every minor narrative discrepancy is surfaced; (b) false sense of transparency if flagging is routine (Tom learns to skip them); (c) conflation of "flag" (notify) and "flag" (block) — the ASSUMPTION doesn't distinguish.

  Mitigations available:
    - Tier the flags: minor-discrepancy (annotation only), moderate (inline in briefing), severe (block briefing until resolved).
    - Require a flag-handling protocol: who acts on the flag, by when?
    - Pair with a "how stale is too stale" threshold — without that, every discrepancy is a flag.

  Recommendation: NO-CHALLENGE-FOUND (weak) — ASSUMPTION is essentially sound; calibration-level concerns only

  STEELMAN:
    Item: ASSUMPTION-047
    Strongest counterargument: The weakest part of the ASSUMPTION is the implicit universal — every discrepancy gets flagged, regardless of consequence or frequency. In practice, the briefing layer has a finite attention budget; if every minor staleness gap is flagged, the flags themselves become noise (alert fatigue). A calibrated commitment — "flag consequential discrepancies, reconcile cosmetic ones at source" — is more defensible than the unqualified universal.
    What would need to be true for C2A2 to be safe: Specify a tier structure (cosmetic / moderate / severe) and a reconciliation-vs-flag decision rule; specify a flag-handling protocol with owner and SLA.
    How to test: Track flag-to-action ratio over 4 weeks; if the ratio is <20%, consider raising the flag threshold.
