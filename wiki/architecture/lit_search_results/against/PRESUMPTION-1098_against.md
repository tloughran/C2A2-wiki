SEARCH-AGAINST-PRESUMPTION-1098:
  Date searched: 2026-09-30
  Original item: PRESUMPTION-1098
  Original statement: A 'monitor' disposition class is informative rather than a default sink.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1098
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 61461c72 dispositions.
      15b: Searched for challenging literature (scheduled run 2026-09-30; depth: web search + selective fetch)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Tversky, A., & Shafir, E. (1992). "Choice under Conflict: The Dynamics of Deferred Decision."
       Psychological Science 3(6):358-361. [Fetched: full text.] When the options involve conflict
       (trade-offs, no dominant option), people defer the choice or keep the default more often,
       even when the choice set is at least as good. Adding a second attractive option raised
       deferral from 34% to 46% (CD players). In the pens study, choosing the default rose from 25%
       to 53%. Deferral tracks how hard the decision is, not the value of the options. A
       "watch/defer" category will therefore fill up in proportion to decision difficulty and
       mixed evidence, not in proportion to real uncertainty about the premise.
    2. Villas Boas, P. J. F., et al. (2013). "Systematic reviews showed insufficient evidence for
       clinical practice in 2004: what about in 2011? The next appeal for the evidence-based
       medicine age." Journal of Evaluation in Clinical Practice 19(4). [Search-result level;
       first-author name from background recall.] In 2004, 47.83% of Cochrane reviews concluded
       insufficient evidence. In 2011, 45.30% of 1,128 reviews concluded likely benefit, and only
       2.04% of those said no further research was needed. The "insufficient / more research
       needed" category absorbs a large share of outputs, and the evidence-medicine literature
       criticizes it as unhelpful to decision-makers.
    3. Background knowledge, not fetched this run. Johnson, E. J., & Goldstein, D. (2003). "Do
       Defaults Save Lives?" Science 302:1338-1339. The default option captures a large share of
       choices regardless of preference. Status-quo bias: Samuelson & Zeckhauser (1988), Journal of
       Risk and Uncertainty 1:7-59.

  Strength of challenge: Moderate

  Summary: Decision research shows that a defer/hold option attracts choices in proportion to
    decision conflict and effort, not to real evidential ambiguity (Tversky & Shafir). Defaults
    capture choices whatever the underlying preference (Johnson & Goldstein; status-quo bias).
    Evidence synthesis shows an "insufficient evidence" bucket can absorb nearly half of all
    outputs, which reviewers criticize as uninformative. A MONITOR category that took 7 of 7 items
    on 09-29 (running 628 vs 220 PREMISE and 488 REVISE), while a deeper pass leaned REVISE on
    three of them, fits the sink pattern. The boundary condition (steelman below) is that
    "insufficient" can be informative when it states what evidence would resolve it and has an
    exit rule.

  Specific risks: Premises with moderate challenges are parked as "watched" and never revisited.
    MONITOR grows without bound. The disposition log looks balanced while it hides a backlog of
    unresolved challenges. This interacts with shallow searches (the 09-29 systemic flag):
    thinner evidence produces more MONITOR outcomes, which lowers the pressure to search deeper.

  Mitigations available: Require each MONITOR disposition to state a trigger (what evidence would move
    it to PREMISE or REVISE) and a revisit date. Cap MONITOR's share per run, or require an extra
    justification after N consecutive MONITOR outcomes. Audit MONITOR items against later deeper
    passes to measure how often they should have been REVISE. Borrow GRADE's practice of stating the
    certainty level together with the reason for downgrading.

  Search scope: Preliminary: 2 searches, 1 fetch.
  Excluded results: arXiv 2608.07298 "Revealed Default Under Choice Overload" (surfaced; not read;
    not cited); Management Science 2022 reexamination of choice deferral (surfaced; not read). The
    reexamination may qualify the Tversky & Shafir effect size, and a broader search should check
    it.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1098
  Strongest counterargument: A hold category is where decisions go when they are hard, not when
    they are uncertain. Tversky and Shafir showed that adding conflict, even with better options,
    pushes people toward deferral and the default. A disposition agent facing mixed 15a/15b
    evidence is in exactly that situation. When a category absorbs 100% of a run's outcomes, and a
    deeper look at the same items moves several toward REVISE, the category is recording the
    agent's reluctance to decide, not the state of the evidence.
  What would need to be true for C2A2 to be safe: Each MONITOR item carries an explicit resolution
    trigger and revisit date. The rate at which MONITOR items later resolve to REVISE is tracked and
    low.
  How to test: Take the 628 MONITOR items (or a random sample of 30), re-run them through a
    deep-search disposition blind to their prior label, and measure the share that come out REVISE
    or PREMISE. Compare MONITOR rates between shallow and deep search runs.
