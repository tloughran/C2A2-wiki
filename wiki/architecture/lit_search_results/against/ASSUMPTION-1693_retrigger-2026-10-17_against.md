SEARCH-AGAINST-ASSUMPTION-1693 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-17
  Original item: ASSUMPTION-1693
  Original statement: A small, non-preregistered study warrants a "Speculative" confidence grade.
  Under test this cycle (MONITOR-621, Low): whether the two-variable grading rule (sample size +
    preregistration status) is defensible as the trigger for "Speculative". Cycle 0 found the
    direction of the grade is right but the rule is coarse. This cycle I searched for how the
    established grading system (GRADE) actually uses sample size, and for predictors of replication
    beyond N and preregistration.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read lit_search_results/for/, any *_for file, or 15a
    sections of lit_search_returns.md. I read only my own cycle-0 file for this item
    (ASSUMPTION-1693_against.md).

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-1693
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Stump/Fredrickson 2598543c.
      15a (cycle 0): independent; not read by this agent
      15b (cycle 0, 2026-09-29): PARTIALLY-CHALLENGED (Weak-to-Moderate; recorded upstream as Weak) —
        grading rule coarse; preregistration label unreliable (Protzko et al. retraction).
      15c: disposition → MONITOR-621 (Low).
      15d: re-trigger, cycle 0 → 1.
      15b (cycle 1, 2026-10-17): 2 searches (GRADE imprecision/sample size; replication predictors);
        1 fetch (Cochrane Colloquium 2020 abstract, read in full).
    Current status: PARTIALLY-CHALLENGED
    Sources this cycle: Llanos et al. 2020 [read in full — abstract page]; GRADE 2011/2022
      imprecision guidance [snippet]; Camerer et al. 2018 SSRP [snippet]; replicationindex.com
      2021 [snippet — blog, low authority].
    Date: 2026-10-17

  EVIDENCE GRADE: PRELIMINARY. One fully read conference abstract; remainder search-result summaries.

  Challenging evidence found: Partial (against the rule's form; not against the direction)

  Sources:
    1. Llanos P, Arcos C, Carvajal-Juliá N, Urrea G, Franco JVA, Meza N, Madrid E,
       Pérez-Bracchiglione J. (2020). "How precise are we when assessing imprecision?: an analysis
       of Cochrane systematic reviews published during 2019." Cochrane Colloquium Abstracts 2020
       (oral). https://abstracts.cochrane.org/2020-abstracts/how-precise-are-we-when-assessing-imprecision-analysis-cochrane-systematic-reviews
       [read in full — abstract] Of 499 Cochrane reviews, 438 downgraded for imprecision; the
       commonest rationale was "few events/patients or small sample size" (66.4%), yet only 10.9%
       used the optimal information size concept, and "some reviews provided reasons that might not
       be adequate." Bearing: even the most institutionalised grading system shows that "small
       sample → downgrade" as a stand-alone shortcut is the practice auditors flag as inadequately
       justified. ASSUMPTION-1693 encodes exactly that shortcut.
    2. GRADE Working Group imprecision guidance (2011; 2022 update). [snippet — not fetched]
       Per search summaries: the primary criterion is whether the confidence interval crosses a
       decision threshold; sample size enters as a secondary check against an optimal information
       size, and a sub-400 sample "should prompt consideration" of rating down — a consideration,
       not an automatic grade. Bearing: GRADE does not map "small" to a grade; it maps precision
       relative to a decision to a downgrade step. (Exact handbook wording not verified.)
    3. Camerer, C. F. et al. (2018). "Evaluating the replicability of social science experiments
       in Nature and Science between 2010 and 2015." Nature Human Behaviour. [snippet via news
       coverage; title from background knowledge — UNVERIFIED] Replications ~5x larger than
       originals still found effects ~50% smaller; prediction markets called 18/21 outcomes.
       Bearing: larger N alone did not rescue findings, and peer judgement of evidence quality
       predicted outcomes — information the two-bit rule discards.
    4. Schimmack, U. (2021). "Predicting Replication Outcomes: Prediction Markets vs. R-Index."
       replicationindex.com. [snippet — blog, low authority] Claims an original-p < .005 rule
       matched markets (~72% across 103 studies). Treated as corroborative only.

  Strength of challenge: Weak (unchanged from cycle 0 as recorded upstream)

  Summary: Nothing found argues small non-preregistered studies deserve HIGH confidence; the
    direction stands. The new evidence sharpens cycle 0's point about form: GRADE itself treats
    sample size as one input to a precision judgement, not a grade trigger, and an audit of 499
    Cochrane reviews shows the "small sample" shortcut is the commonest and least well-justified
    downgrade rationale. Replication meta-research shows that N alone neither predicts nor repairs
    replicability; strength of the original evidence does better.

  Specific risks: C2A2 adopts a rule that experienced evidence graders are criticised for using
    loosely; grades become uninformative across traditions because all small studies collapse to
    one tier regardless of precision, effect plausibility or replication.

  Mitigations available: treat "Speculative" as a CEILING; require a stated precision rationale
    (CI vs a decision threshold, or explicit "no decision threshold defined"); add downgrade path
    for withdrawn/contested findings and upgrade path for independent replication.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1693
  Strongest counterargument: The field that invented certainty grading explicitly declines to let
    sample size set a grade; it asks whether the estimate is precise enough for the decision at
    hand. An audit of Cochrane practice shows the "few patients" shortcut is used most and
    justified least. A wiki rule that hard-codes the shortcut inherits the very weakness auditors
    criticise, and replication data show N is not what separates findings that hold from those
    that don't.
  What would need to be true for C2A2 to be safe: "Speculative" is applied as an upper bound with a
    one-line precision rationale, and grades can move down (withdrawn) or up (replicated)
    independently of N and preregistration status.
  How to test: sample 10 "Speculative" grades in the wiki; for each, ask whether a stated precision
    or replication reason exists beyond "small, not preregistered". If most have none, the rule is
    operating as the shortcut.

  Search scope: preliminary — 2 searches, 1 fetch. Cycle-0 limb on Fredrickson-lineage withdrawn
    findings not re-searched.
