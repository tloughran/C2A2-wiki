SEARCH-FOR-ASSUMPTION-1175 (REFRESH — 15d re-trigger, 2026-09-27, cycle 1):
  Date searched: 2026-09-28
  Original item: ASSUMPTION-1175
  Original statement: Context isolation between adversarial searchers (15a/15b) is a remedy for correlated
    error. Open sub-question at this monitor cycle: does isolating context between adversarial LLM agents
    reduce correlated error when the base model is shared, and by how much?

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a (2026-08-25) -> 15c -> MONITOR-547 -> 15d RE-TRIGGER (2026-09-27) -> 15a (2026-09-28)]
    Original item: ASSUMPTION-1175
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session discussion of the 15a/15b independence design
      15a (2026-08-25): PARTIALLY-SUPPORTED, Moderate, partial NOVELTY-FLAG
      15a (2026-09-28): Primary-source verification of two specific triggers named at intake
    Current status: SEARCHED (this cycle was verification, not a fresh keyword search)

  Supporting evidence found: No new supporting evidence this cycle (verification-only cycle).

  Sources verified this cycle:
    1. Denisov-Blanch, Y., Kazdan, J., Chudnovsky, J., Schaeffer, R., Guan, S., Adeshina, S., Koyejo, S.
       (2026). "Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness."
       arXiv:2603.06612. — Fetched and confirmed authorship and content. Directly relevant: reports that
       "language model errors are strongly correlated" across models, and that this correlation persists
       "even when conditioned on out of distribution random strings and asked to produce pseudo-random
       outputs." This is the exact condition the item's own decision rule named as the REVISE trigger.
    2. Begin, J., Gho, B., Muppavarapu, S., Tsay, T., Mohan, A., Shaik, A., Li, R., Sharma, V.,
       Vaidheeswaran, A. (2026). "Preference Optimization Drives Monoculture in LLM Prediction Markets."
       arXiv:2606.26583. — Authorship was UNVERIFIED at intake (2026-08-25); now CONFIRMED. Reports
       pairwise error correlation of 0.679+/-0.023 for same-model pairs vs. 0.396+/-0.011 for cross-model
       pairs, and that ten same-model agents provide only ~1.38 [1.36, 1.40] effective independent
       forecasters vs. ~2.2 for mixed-model teams. Isolates preference optimization (DPO) as the
       mechanism: DPO alignment increases correlation by +0.24 to +0.46 over SFT baselines depending on
       conditions. Matches the item's cited figures exactly.

  Strength of support: N/A for this cycle — this was a verification pass on pre-registered CHALLENGE
    triggers, not a fresh supportive search. See against/ASSUMPTION-1175_against.md for the disposition-
    relevant reading of these same two sources.

  Summary: Both sources named at the 2026-08-25 disposition as REVISE triggers are real, accurately
    cited, and confirm the conditions the item's own decision rule specified. No countervailing new
    supportive literature was found this cycle.

  Caveats: This was a targeted verification of two named citations, not a comprehensive fresh search of
    the field. A broader search was not repeated since the 2026-08-25 cycle already flagged this as a
    NOVELTY area (no study isolates context as the independent variable at fixed base model under opposed
    roles specifically for adversarial agent pairs).

  Recommendation: NO-SUPPORT-FOUND (this cycle) — the verification cycle's findings support the CHALLENGE
    side, not the FOR side. See 15c disposition (DISPOSITION-999): REVISE-488.
