SEARCH-FOR-ASSUMPTION-1684 (RE-TRIGGER — 15d 2026-10-11, MONITOR-618, cycle 1; Medium):
  Date searched: 2026-10-12
  Original item: ASSUMPTION-1684
  Original statement: After one full review, later structural (mechanical) checks are enough to keep a text's
    pass status. (Summa QC 8c58d8ca: "the review was lighter than a full read"; commentaries checked
    mechanically because each had had a full review on 09-19 or 09-20.)
  Owed (per 15d block): "Neither direction has primary evidence. This is an untested premise, not a refuted
    one. Would change with a primary source on checklist-vs-holistic re-review efficacy, or an in-house
    measure..."
  MONITOR-618 exit condition (2026-09-30): INCORPORATE the conditional form (carry-forward allowed with
    verified no-change plus periodic full review) if REVISE-493's sampled semantic spot-check is adopted.
  Cycle: 1 (RE-TRIGGER by 15d 2026-10-11; processed 2026-10-12)

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c -> 15d -> 15a (re-trigger cycle 1)]
    Original item: ASSUMPTION-1684
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Summa QC 8c58d8ca; quote confirmed in transcript.
      15a (cycle 0, 2026-09-29): NO-SUPPORT-FOUND (None). One shallow query that returned compliance blogs.
      15b (cycle 0): independent; not read by this agent.
      15c: DISPOSITION-1002 -> MONITOR-618; refreshed by DISPOSITION-1016 (bound to REVISE-493)
      15d: re-triggered 2026-10-11 without evaluating evidence
      15a (cycle 1, 2026-10-12): 2 web searches.
        - compact.nl (KPMG) article fetched in full.
        - PCAOB primary text fetch FAILED: the URL was not in the provenance set and the tool refused it.
    Current status: PARTIALLY-SUPPORTED (Moderate) for the conditional form; None for the unconditional form

  Search scope: Formalised practice in which one full test is carried forward on the strength of later
    lighter checks:
    (a) PCAOB AS 2201 (formerly AS5) Appendix B "benchmarking" of automated controls;
    (b) software regression-test selection (retest only what changed).
    Checklist-vs-holistic re-review of TEXTS was not found directly, and no primary study on that question
    was located.

  Supporting evidence found: Partial. Codified analogous practice was found for the conditional form. No
    primary efficacy study was found.

  Sources:
    1. PCAOB Auditing Standard AS 2201 (formerly AS No. 5), Appendix B, ¶B28–B33, "Benchmarking of automated
       controls". [primary text NOT read; pcaobus.org fetch refused] As reported in source 2 (read in full)
       and in Protiviti / SAPinsider summaries (snippets only):
       - Quoted in source 2: "Entirely automated application controls are generally not subject to
         breakdowns due to human failure. This feature allows the auditor to use a 'benchmarking' strategy."
       - Paraphrased: once a control has been tested to a baseline, the auditor may treat it as still
         effective in later years WITHOUT repeating the full test, provided that:
         - change-management general controls are effective;
         - there is evidence that the control "has not changed since" the baseline;
         - the benchmark is re-established periodically (B33; practice is about 3 years, sometimes 3–5).
       Relevance: this is a codified, long-standing regulatory precedent for "one full review, then lighter
       no-change verification suffices". It holds only under exactly the conditions MONITOR-618's exit
       condition names: verified no-change plus a periodic full re-review.
    2. op het Veld, M. & de Bruijn, R.J.C.H.M., 2008. "Benchmarking IT application controls: a practical
       guide for SAP." Compact 2008/3 (KPMG NL). [read: full text] The article lists five preconditions:
       - effective general controls;
       - a stable environment with few changes;
       - the control mapped to a specific program;
       - evidence the program has not changed;
       - periodic re-baselining.
       Its gloss: "if you are feeling well, you do not have to go the doctor every year or undergo a full-
       body scan". It also notes that the MANUAL part of IT-dependent manual controls "should be tested for
       operational effectiveness each year". Benchmarking covers only the deterministic part.
    3. Rothermel, G. & Harrold, M.J., 1997. "A Safe, Efficient Regression Test Selection Technique." ACM
       TOSEM 6(2):173–210. [search snippet; paper not read] The paper proves that, under stated conditions,
       retesting only tests that touch changed code is "safe": the tests selected include every original
       test that can expose a fault in the modified program.
       Relevance: theoretical grounding that, where the change set is known, re-verifying only what changed
       loses nothing relative to a full rerun. It also implies that safety depends on correctly identifying
       what changed.

  Strength of support:
    - Moderate for the CONDITIONAL form: carry forward a full review only with verified no-change, a reliable
      change record, and periodic full re-review. Source 1 is a binding audit standard, but it was read
      second-hand. Source 3 is formal grounding.
    - None for the UNCONDITIONAL form as stated, i.e. mechanical checks are enough without a no-change
      verification or a re-baseline cycle.
    - No primary efficacy study on checklist-vs-holistic re-review of prose was found.

  Summary: Cycle 0 found nothing. This cycle finds that auditing has codified something close to ASSUMPTION-
    1684 for two decades. A baseline test may be carried forward on lighter evidence, but only if the object
    is shown not to have changed, change control is effective, and the baseline is periodically re-
    established. Regression-test selection gives the same logic a formal safety proof. Both bodies attach
    conditions the assumption as stated lacks.
    - Mechanical checks of sections, phrasing and labels are not a no-change verification. A text can pass
      them after a semantic edit.
    - The audit precedent explicitly excludes human-judgement components from carry-forward.
    So the literature supports MONITOR-618's conditional form, which REVISE-493's sampled semantic
    spot-check would approximate, and does not support the bare form.

  Owed condition: PARTIALLY met. Codified practice and a formal analogue were found for the conditional
    form. The specifically owed "primary source on checklist-vs-holistic re-review efficacy" for texts was
    NOT found. The in-house measure was not examined.

  Caveats:
    - Automated controls are deterministic, while a commentary's quality judgement is not. The text itself
      is static unless edited, so the "no-change" leg transfers well, but the "baseline was correct" leg
      does not.
    - The PCAOB primary text was not read; paragraph numbers come from secondary sources, which disagree
      slightly (B29 vs B31).
    - Source 3 was read as a snippet.

  Recommendation: PARTIALLY-SUPPORTED (Moderate) for the conditional form only. The unconditional statement
    remains NO-SUPPORT-FOUND.
