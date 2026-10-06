SYSTEMIC-RISK-FLAG:
  Date: 2026-09-21
  Affected items: ASSUMPTION-1560, ASSUMPTION-1561, ASSUMPTION-1571, PRESUMPTION-1053,
    PRESUMPTION-1054, PRESUMPTION-1057 (6 of the 7 literature-bearing items in the 2026-09-20 intake)
  Also: ASSUMPTION-1575, PRESUMPTION-1058, PRESUMPTION-1059, PRESUMPTION-1060 (the intake's four
    empirical-only items, every one of which names an instrument and none of which has been run)

  Common vulnerability: **Every item in this intake resolves to an in-house measurement that is
  specified, cheap, and unrun.** Not one of the ten needs an instrument that does not exist:
    - 1560: classify CROSS-008's three sources by whose voice the attribution is in (~30 min)
    - 1561 + 1057: the pre-registered back-test over 24 elapsed months (hours)
    - 1571: the REVISE base rate for non-downgraded searched items (one grep)
    - 1053: per-register self-inclusion share, plotted over 90 days
    - 1054: assert on the newest date-stamped section in `lit_search_returns.md` (one line)
    - 1575, 1058, 1059, 1060: enumerations 14a/14b already specified
  The literature searches this run performed were, in every case, the *less* decisive of the two
  available evidence sources — and they are the ones that got done, because they are the ones the
  pipeline is built to do.

  Literature basis: this is a recurrence, not a discovery. SYSTEMIC-RISK-FLAG 2026-09-16
  (`named-instrument-never-run`, items 414-439) recorded the same pattern five days ago. The estate has
  now flagged the same systemic vulnerability twice in one week, and between the two flags the
  instruments named in the first were not run either. The 2026-09-20 intake's own routing note records
  a third instance of the type: 15d routed 23 re-triggers into a lane it had not checked was moving.

  Risk level: **Critical** — upgraded from the 2026-09-16 flag's level on the strength of recurrence.
  The failure is no longer "an instrument was not run." It is that the system's cheap, decisive,
  in-house measurements are structurally out-competed by its expensive, indecisive, automatable ones,
  and that the imbalance is self-reinforcing: the automatable lane produces artefacts each run, so it
  looks productive, while the decisive lane produces nothing and looks idle.

  Recommendation: The estate has a literature pipeline and no measurement pipeline. Until one exists,
  the honest reading of any "SUPPORTED" disposition in this run is *supported by the weaker of the two
  available sources*. Concretely, and in order: (1) run the 1054 assertion, because it is one line and
  it would have caught the current stall four days ago; (2) run the 1571 base rate, because it is a grep
  and it decides an item this run is otherwise about to leave open; (3) run the 1560 source
  classification, because it is the only one with a correction waiting on it in three places.
