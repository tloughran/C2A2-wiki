SYSTEMIC-RISK-FLAG:
  Date: 2026-08-19
  Filed by: 15b (Literature Search AGAINST)
  Affected items: PRESUMPTION-842, PRESUMPTION-838, PRESUMPTION-845, ASSUMPTION-1153, and (cross-cohort) PRESUMPTION-833
  Common vulnerability: **Every path that departs from the primary route is ungated, and the lifecycle has no terminal state for any of them.**

  Statement: Corrections, workarounds, retractions and withdrawn flags are all *departures* — actions taken when the normal route is judged wrong or unavailable. The system gates the normal route and gates nothing else. A correction needs no separate approval (842). A workaround substitutes for an absent capability with no declaration (838). A run that invalidates its own method can file a remedy but cannot stop (845). Instruments retract confident findings with no record of the retraction's own status (1153, 833). In each case the departure is treated as inheriting the legitimacy of the thing it departs from, and in each case there is no terminal state to record that it happened, was wrong, or was itself reversed.

  Literature basis:
    - Fix-induced regression rates: 29% of Stack Overflow-derived fixes introduce at least one new bug; 12.2% of PRs introduce bugs under full CI and review (stated as conservative); ~50% of Linux kernel bugs and 51.09% of Chromium bugs are regressions. [**All figures reach this flag through one secondary review, IJSRET 2026 "Why Bug Fixes Introduce New Bugs"; primary sources NOT independently retrieved. Verify before quoting.**] Supporting primary work located: arXiv:2411.02091, arXiv:2506.13182.
    - Workaround safety: Koppel and colleagues, "Workarounds to Barcode Medication Administration Systems", JAMIA 2008 — 15 workaround types, 31 causes, classified as omitted steps, out-of-sequence steps, unauthorised steps. [co-authors not verified]
    - Erroneous and non-propagating corrections: Research Evaluation, doi 10.1093/reseval/rvae016 (retractions flawed procedurally and on merit, with no reliable reversal route); PMC8550405 (retraction propagation inconsistent and incomplete). [authors not verified]
    - Normalisation of deviance: Vaughan, *The Challenger Launch Decision* [established-work]; CAIB Ch.8 "History as Cause", Vaughan [established-work].
    - Stop-work authority [established industrial-safety practice]: the control that permits halting without the approval of the party being halted. C2A2 has escalation and no brake.
    - Static-analysis false-positive base rates 76%–>90% (arXiv:2601.18844, Tencent industrial dataset), which is what a departure gate would be filtering.

  Risk level: **Critical**

  Why it is systemic: The item-level evidence already contains a worked example of the compound failure. ASSUMPTION-1153 records a retraction that would have licensed reversing correct Day 268/269 repairs — an ungated correction, acting on unvalidated instrument output, stopped by an ad hoc grep rather than by any gate. PRESUMPTION-845 records the same structure one level up: a run that discovered its own method was invalid, could not stop, and minted three premises anyway. The corrective direction is where the highest-consequence errors live, because a wrong detection costs an investigation whereas a wrong correction destroys work that was right — and it is the direction with no gate at all.

  Recommendation:
    1. Gate the corrective direction at least as strictly as the detective direction. Require independent confirmation before any action that reverses prior work. This single rule covers 842, 1153 and part of 845.
    2. Add terminal, machine-readable lifecycle states for: withdrawn flag, reversed correction, failed-to-propagate correction, declared substitution, and suspended-pending-resolution. Five states; none currently exist.
    3. Make corrections non-destructive so a wrong one is undoable.
    4. Measure C2A2's own correction-error rate — corrections issued versus corrections later reversed — rather than importing the software base rates. This is computable from existing records and it settles the magnitude question locally.
    5. Fail closed on absent capability. The one run that declined the substitution completed; the design should make declining the default, while separately supplying the missing capability (per Safety-II, a prohibition without provision converts a recorded workaround into an unrecorded one).
