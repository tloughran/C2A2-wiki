PROVENANCE:
  Origin: 15b | Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1) → SYSTEMIC-RISK flag]
  Item type: SYSTEMIC-RISK (cross-item) | Items: PRESUMPTION-867, PRESUMPTION-865, PRESUMPTION-876, PRESUMPTION-888
  Transform at this step: pattern flag across per-item AGAINST results of the 2026-10-08 re-trigger cohort
  Current status: FLAGGED — awaiting orchestrator / 15c

SYSTEMIC-RISK-FLAG:
  Date: 2026-10-08
  Raised by: 15b (re-trigger cycle 1 cohort)
  Affected items: PRESUMPTION-867 (MONITOR-551), PRESUMPTION-865 (MONITOR-552), PRESUMPTION-876
    (MONITOR-553), PRESUMPTION-888 (MONITOR-565). ASSUMPTION-1211 is NOT a member.
  Related prior flags: SYSTEMIC-RISK-FLAG_2026-09-09_absence-read-as-all-clear;
    SYSTEMIC-RISK-FLAG_2026-10-01_silence-read-as-health; SYSTEMIC-RISK-FLAG_2026-10-04_surface-signal-
    as-verdict. Distinct from those: they concern a MISSING record read as good news. This flag concerns
    a PRESENT record (or a present collection decision) forced into a positive state because the status
    vocabulary has no slot for the negative or qualified state.

  Common vulnerability: In each item the estate's status vocabulary lacks a state the literature treats
    as mandatory, so the case that needs that state is filed under the nearest positive one:
      - 867: no "failed-and-reported" outcome distinct from "completed/successful." Manheim & Garrabrant
        (2018, fetched): setting the metric for a subset of cases makes it "less useful" in proportion —
        no optimiser required.
      - 876: no "superseded/retracted" state (and no separate observed-at vs written-at). Torp, Jensen &
        Snodgrass (fetched): "current" is DEFINED by an open transaction-time interval that a retraction
        closes; without that act the register has no current state.
      - 865: no "never-sampled / deliberately dropped" stratum record. Zhu/Mitra et al. 2021 (fetched):
        zero-probability strata are a structural positivity violation; reweighting cannot recover them
        and more data does not help.
      - 888: no "UNASSESSED" state for material no consumer reads (MONITOR-565's own discriminating
        test). Duranti 1994 and Beaven 1999 (fetched): value inferred from use, even external use,
        inherits the consumers' availability bias; unread is not evidence of low value.
    In every case the missing state is the one that would make the system's own blind spot legible:
    the failure that completed, the verdict that expired, the stratum no longer looked at, the
    material no one read.

  Literature basis: Manheim & Garrabrant 2018 arXiv:1803.04585 [fetched, full text]; Torp, Jensen &
    Snodgrass "Effective Timestamping in Databases" [fetched, full text]; Zhu, Hubbard, Chubak, Roy &
    Mitra 2021, PMC8492528 [fetched, full text]; Duranti 1994, American Archivist 57(2) [fetched, full
    text]; Beaven 1999, Archivaria 48 [fetched, full text]; supporting at search-result level: Vaughan
    1996; Inozemtseva & Holmes 2014; Konno & Pullin 2020; Maddi et al. 2023 arXiv:2311.04909.

  Risk level: High
    (Not Critical: each member has a cheap, local fix and none is shown to have caused harm yet; the
    risk is that the same omission recurs in every new register because it is a vocabulary design habit,
    not a per-item defect.)

  Recommendation (what to consider, not a directive): an estate-wide check that every status field
    includes, at minimum, a negative-outcome state, a superseded state, and an unassessed/unknown state,
    and that defaults resolve to UNKNOWN rather than to the last positive value. Each member's in-house
    test (867: success rate with/without failure-reporting runs; 876: stale-exposure rate; 865: back-fill
    of one dropped stratum; 888: count of unread material recorded nowhere) measures the size of the
    collapsed category directly, and these measurements, not further literature, now decide the cohort.
