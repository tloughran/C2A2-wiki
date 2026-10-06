*** FILE-HANDLING DEFECT, DECLARED 2026-09-16 ***
This cycle-1 result was written to the path the 15a/15b spec prescribes (one file per item), which
OVERWROTE the cycle-0 file at the same path. The cycle-0 search text is LOST. Its findings survive only
in lit_search_returns.md and in DISPOSITION-359 / -361 / -397. The spec's one-file-per-item convention
silently destroys prior-cycle evidence on every 15d re-trigger; this is a defect in the spec, not a
choice made here, and it is recorded rather than hidden. Recommended fix: path should carry the cycle.

SEARCH-AGAINST-PRESUMPTION-439:
  Date searched: 2026-09-16
  Original item: PRESUMPTION-439
  Original statement: [inferred] That k=5, though acknowledged underpowered, still supports a stable
    robust/directional/null sort of the results.
  Cycle: 15d re-trigger 2026-07-12, cycle 1. Prior 15b (2026-07-03): CHALLENGED (Moderate-Strong).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15b]
    Original item: PRESUMPTION-439
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the acknowledged-underpowered k=5 co-occurring with a categorical verdict treated
        as stable (2026-07-02).
      15b: Re-searched for challenging literature; executed 2026-09-16.
    Current status: CHALLENGED
    INDEPENDENCE CAVEAT (declared): 15a and 15b ran in a SINGLE process this cycle.

  Challenging evidence found: Yes — the strongest of the three items searched this run.

  Sources:
    1. MacKinnon, Nielsen & Webb, 2023. "Cluster-robust inference: A guide to empirical practice."
       Journal of Econometrics 232(2). — The authoritative treatment. With few clusters, t- and Wald tests
       OVER-REJECT, and the over-rejection is severe when one or a few clusters are unusually large or
       when only a few are treated. Directly on point: the C2A2 design treats the conversation as the
       cluster and has five of them.
    2. Same, leverage result. — A single high-leverage cluster can change estimates SUBSTANTIALLY when
       omitted. This is the mechanism by which a robust/directional/null sort flips: one conversation
       carries a bucket.
    3. Liu et al., 2022. "Stability estimation for unsupervised clustering: A review." WIREs
       Computational Statistics. — Establishes leave-one-out resampling as the STANDARD instrument for
       asking whether a classification survives non-essential perturbation of the data, and states the
       governing norm: a meaningful classification should remain intact when the data set is changed in a
       non-essential way.
    4. Ben-David, von Luxburg & Pal, "A Sober Look at Clustering Stability." — Cautions that stability
       results are themselves sensitive to how many groups are posited; a three-way sort imposed on five
       units is in the regime the paper warns about.
    5. "Underpowered != Inconclusive != Negative != Neutral," arXiv:2604.09108. — Read against the item:
       the "null" label applied to P-civility is not licensed at this power. Absence of a detected effect
       in an acknowledged-underpowered design is INCONCLUSIVE. This is a live mislabelling in a delivered
       artefact, not a hypothetical.

  Strength of challenge: STRONG (upgraded from Moderate-Strong at intake).

  STEELMAN:
    Item: PRESUMPTION-439
    Strongest counterargument: The presumption is not merely unsupported; the standard reference says the
      opposite in the exact design C2A2 used. Cluster-robust inference at k=5 over-rejects, and a single
      leveraged cluster can move an estimate enough to reassign it. A three-way categorical sort is
      strictly more fragile than the underlying interval it summarises, because it discretises: a small
      shift that would be invisible in a wide interval becomes a CATEGORY CHANGE at the boundary. So
      conceding "intervals are wide by design" while presenting the sort as a deliverable is not a
      balanced pair of statements — the concession, taken seriously, IMPLIES the sort is unstable. And the
      "null" bucket is affirmatively wrong under a taxonomy 15a itself retrieved: at k=5, no detected
      effect means inconclusive. Two of the three labels are therefore doing work the data cannot bear.
    What would need to be true for C2A2 to be safe: (a) the sort is labelled provisional/triage, never
      "stable" or "settled" — which is what DISPOSITION-397 already ruled on 2026-07-03; AND (b) the
      "null" bucket is relabelled "inconclusive"; AND (c) leave-one-conversation-out recomputation shows
      low churn.
    How to test: Exactly the instrument MONITOR-415 named at intake and that has not been run in 75 days —
      recompute the sort five times, omitting one conversation each time, and count reassignments. Five
      recomputations over data already in hand. High churn -> REVISE and bank nothing; low churn -> the
      provisional sort may stand as provisional.

  Specific risks: A fragile sort reassigns "robust" results on a strengthening run, undercutting claims
    already presented as settled. The concrete exposure is P3'b (directional) and P-civility (null); the
    latter is mislabelled independent of any churn result.

  Mitigations available: Yes, and two of the three are free. Relabelling "null" -> "inconclusive" is a text
    edit. Labelling the sort provisional is already 15c policy. Only the leave-one-out recomputation costs
    anything, and it costs five recomputations.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-09-16
    Affected items: PRESUMPTION-414, PRESUMPTION-439
    Common vulnerability: MEASURE ADOPTED / VALIDATION INSTRUMENT NAMED / INSTRUMENT NEVER RUN. In both
      items a summary measure was taken as ground truth (connectivity as vault health; a three-way sort as
      a result classification); in both, the literature names one cheap, standard validation instrument
      (proxy-reliability correlation against a non-link outcome; leave-one-conversation-out recomputation);
      and in both, the instrument was specified in the MONITOR entry at intake — 2026-06-29 and
      2026-07-03 respectively — and has not been run in the 75-79 days since. PRESUMPTION-414 is already
      recorded as a member of the STRUCTURAL-PROXY-AS-GROUND-TRUTH cluster (MONITOR-403).
    Relation to existing flags: This is NOT a new pattern. It is a second cohort of the pattern recorded
      on 2026-09-12 as "owed measurements never executed" (items 1321, 959, 960, 968). Filed as an
      extension of that flag rather than as a new one, because minting a fresh flag for a known pattern is
      itself an instance of the pattern. What these two add is that the owed measurements are OLDER than
      any in the 09-12 cohort and sit in the re-trigger lane, which the 15d run measured at 280 standing
      unconsumed blocks draining at 7 per fortnight. At that rate the lane does not clear.
    Severity: High, on the same grounds as the 09-12 flag.

  Recommendation: CHALLENGED
