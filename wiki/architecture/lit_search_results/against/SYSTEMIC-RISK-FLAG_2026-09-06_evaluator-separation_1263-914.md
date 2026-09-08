SYSTEMIC-RISK-FLAG:
  Date: 2026-09-06
  Affected items: ASSUMPTION-1263, PRESUMPTION-914 (and, by the same mechanism, the 8 orchestrator-written
    files of 2026-09-05 and the 3 orchestrator-written AGAINST files of this run)
  Common vulnerability: Both items define 15a/15b independence by what was READ (file order) rather than by
    what the two evaluators SHARE (model, alignment, and — in the fallback case — a single context window).
    The pipeline's own independence metric is therefore measured on the weakest channel (PREMISE-111) and
    reports nominal when the fallback removes the evaluators entirely.
  Literature basis: Kohli 2026 arXiv:2605.29800 (nine blinded judges ≈ two votes; 8–22pp shortfall);
    Temkit 2026 arXiv:2605.22714 AMEL (cross-item polarity carry-over inside one context, d = −0.28 on
    ambiguous items); arXiv:2506.00069 (prior-context degradation up to 32–73%); van Rooyen et al. 1998 JAMA
    (blinding editorially insignificant); Nemeth et al. 2001 (role-played dissent bolsters the prior view).
  Risk level: High
  Recommendation: (1) Never count a same-context FOR/AGAINST pair as two readings (DISPOSITION-900
    precedent, now general). (2) Report read-channel and execution-channel independence as two separate
    numbers in every run note. (3) When 15b delegation fails, prefer a loud FAIL (no AGAINST file, item left
    [SEARCHED-15a] only, dispositioned next run) over orchestrator fallback — the fallback produces files
    whose names imply an independence they lack. This run did NOT follow (3); it fell back and declared.
    Tom's ruling requested on whether (3) becomes the rule.
  PROVENANCE: Origin 15b · Chain [14a/14b → 15b] · Items ASSUMPTION-1263, PRESUMPTION-914 · Written by the
    15c orchestrating context acting as 15b (delegation failure, declared in each result file).
