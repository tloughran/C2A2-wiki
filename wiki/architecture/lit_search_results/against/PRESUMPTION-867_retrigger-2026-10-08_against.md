SEARCH-AGAINST-PRESUMPTION-867 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-08
  Original item: PRESUMPTION-867
  Original statement (per MONITOR-551): A "fail loud" norm improves system health; its second-order effect
    on success accounting is benign.
  Owed this cycle: CONJUNCT 2 ONLY — whether a run that terminates by faithfully reporting total failure
    can be booked as a completed/successful run without corrupting the aggregate health metric. Named
    venues: Manheim & Garrabrant (Goodhart formalisations); Vaughan (normalization of deviance);
    measurement gaming; Inozemtseva & Holmes 2014 (proxy-metric case). Conjunct 1 is settled
    (PREMISE-102, PREMISE-173) and was not re-searched.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. The cycle-0 15a verdict is known to me only as the
    one-line summary inside MONITOR-551.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-867
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three same-day runs that completed by reporting total failure.
      15b (2026-08-25): PARTIALLY-CHALLENGED (Moderate) on conjunct 1 only; conjunct 2 NOT searched
        (budget exhausted); declined to cite Goodhart/Vaughan from memory.
      15c: DISPOSITION-808 → MONITOR-551 (HIGH; Critical SYSTEMIC-RISK-FLAG 1 member).
      15d (2026-09-13): Re-triggered; owed = metric-corruption literature for conjunct 2.
      15b (re-trigger cycle 1, 2026-10-08): 2 searches dedicated to this item (Goodhart; Vaughan) plus 1
        (Inozemtseva & Holmes); 1 full-text fetch (Manheim & Garrabrant). Cycle-0's gap on conjunct 2 is
        closed.
    Current status: CHALLENGED

  EVIDENCE GRADE: one full-text fetch (Manheim & Garrabrant); two search-result-level sources (Vaughan
    via secondary summaries; Inozemtseva & Holmes via abstract/award/secondary summaries). Preliminary-to-
    moderate scope. No source studies the specific accounting rule in question; the bearing is by
    formal mapping, stated explicitly below.

  Challenging evidence found: Yes

  Sources:
    1. Manheim, D. & Garrabrant, S. 2018 (rev. 2019). "Categorizing Variants of Goodhart's Law."
       arXiv:1803.04585. [fetched — full text via ar5iv] Two of the paper's named cases map directly
       onto booking a faithful-failure run as "completed/successful":
       (a) "Ignored Additional Cause — The metric is caused by multiple factors, of which the goal relates
           to only some." If "success" counts both runs that achieved the task and runs that terminated
           cleanly by reporting failure, the metric now has a cause (clean termination) unrelated to the
           goal (task achieved), which the paper says produces "worsened regressional Goodhart effects."
       (b) "Metric Manipulation — The regulator intervenes to set the Metric, without affecting other
           nodes ... it simply changes M so that it is useless (or, if only some scores are changed,
           less useful) in measuring G." Re-labelling a subset of failures as successes is a
           regulator-side setting of M for some cases — the paper's teacher-changes-grades example —
           and requires no adversarial agent and no optimisation pressure to degrade the metric.
       BOUNDARY CONDITION (honest): the paper also states "The importance of Goodhart effects depends on
       the amount of power directed towards optimizing the proxy." The regressional/extremal/adversarial
       cases need selection pressure; if nobody selects or steers on the success rate, those cases are
       weak. Case (b) does NOT need selection pressure — it degrades the metric definitionally — so the
       boundary condition does not rescue conjunct 2.
    2. Vaughan, D. 1996. The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA.
       University of Chicago Press. [search-result — secondary summaries only (Columbia Magazine;
       psychsafety field guide; Flight Safety Australia); primary text NOT read] The mechanism reported
       across the summaries: anomalies were "normalised" because each flight that returned safely
       reinforced the belief that the anomaly was an acceptable risk; the success record itself became
       the reassurance; no rules were broken. Bearing: a success tally that absorbs runs carrying a
       failure signal is the accounting form of exactly this — the aggregate reports the system as
       healthy precisely because failures that "completed" are counted as completions. Bearing is by
       analogy (an engineering-safety organisation, not a run ledger).
    3. Inozemtseva, L. & Holmes, R. 2014. "Coverage is not strongly correlated with test suite
       effectiveness." ICSE 2014, pp. 435–445. [search-result — abstract and secondary summaries (Colyer
       2014; Wilson 2021; ICSE 2024 Most Influential Paper citation); full PDF located but not fetched]
       31,000 suites, five systems up to 724 KLOC: low-to-moderate correlation between coverage and
       fault-detection once suite SIZE is controlled; "coverage ... should not serve as a quality
       target." Bearing: the canonical software-engineering case of a widely-used health proxy that
       tracks VOLUME of activity rather than the outcome. A completed-run count that includes
       faithful-failure runs is, by construction, a volume measure (runs that terminated) presented as
       an outcome measure (runs that succeeded).

  Strength of challenge: Moderate (formally direct via a fetched source; empirically indirect — no
    source measures this specific accounting rule)

  Summary: The cycle-0 gap is closed and the literature runs against conjunct 2. Manheim & Garrabrant's
    taxonomy contains a case — metric manipulation by the regulator — that corrupts a metric without any
    gaming agent and without optimisation pressure: setting the metric's value for a subset of cases
    makes it "less useful" in proportion to the subset. Booking a faithful-failure run as successful is
    that case. Their "ignored additional cause" case says the same thing from the measurement side.
    Vaughan supplies the organisational mechanism by which a success record that absorbs failure signals
    becomes the reason those signals stop being read, and Inozemtseva & Holmes supply the
    software-engineering precedent of a health proxy that tracks volume rather than outcome. The
    conjunct can only be "benign" if the failure-reporting runs are a negligible fraction of runs or the
    success metric is never consulted — neither is established.

  Specific risks: (i) the aggregate success rate overstates health by exactly the share of
    faithful-failure runs, and the overstatement GROWS as the fail-loud norm succeeds (more honest
    failures → more mis-booked successes); (ii) the metric becomes least reliable at the moment it
    matters most (a cluster of total-failure runs reads as a healthy streak); (iii) normalisation —
    a run-ledger that reads "completed" for a total failure trains downstream readers to treat that
    pattern as acceptable.

  Mitigations available: a three-valued outcome (succeeded / failed-and-reported / failed-silently)
    instead of a binary completed flag; report the success rate with and without failure-reporting
    runs (MONITOR-551's own in-house test — compute it over the 49-day window); treat "completed by
    reporting total failure" as its own counted state, not a sub-case of success.

  Recommendation: CHALLENGED — conjunct 2 contradicted in kind by a fetched formal source; magnitude for
    C2A2 is an arithmetic question the estate can answer directly and should, because it decides
    REVISE without further literature.

STEELMAN:
  Item: PRESUMPTION-867 (conjunct 2)
  Strongest counterargument: Goodhart effects are usually discussed as the consequence of optimising a
    proxy, which invites the reply "we don't optimise our success rate, so no harm." Manheim & Garrabrant
    close that exit: their metric-manipulation case needs no optimiser — when the regulator itself
    re-labels some cases, the metric stops measuring the goal for those cases, full stop. A ledger that
    books "I tried, everything failed, here is the faithful report" as success has not merely added
    noise; it has defined a failure state into the success column. And the better the fail-loud norm
    works, the larger that column becomes, so the corruption is positively coupled to the very virtue
    the norm was introduced to produce. Vaughan shows what the organisation then does with an unbroken
    success record: it stops treating the embedded anomalies as signals.
  What would need to be true for C2A2 to be safe: faithful-failure runs are a negligible share (e.g.
    <2%) of runs in every reporting window; OR no human or agent reads the aggregate success rate as a
    health signal; OR the ledger already distinguishes failed-and-reported from succeeded and only the
    prose summary conflates them.
  How to test: recompute the success rate over the 49-day window with faithful-failure runs moved to a
    separate state; any divergence above a pre-stated tolerance (say 5 points) converts this to REVISE.
