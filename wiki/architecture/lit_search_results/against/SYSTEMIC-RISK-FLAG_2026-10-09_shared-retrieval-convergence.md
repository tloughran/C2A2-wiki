SYSTEMIC-RISK-FLAG:
  Date: 2026-10-09
  Filed by: 15b (re-trigger cycle 1 batch)
  Affected items: ASSUMPTION-1164, PRESUMPTION-844, ASSUMPTION-1153 (directly observed);
    by extension every item searched by 15a and 15b in the same session; MONITOR-547 / ASSUMPTION-1175
    and REVISE-350 (the decorrelation premise itself).

  Common vulnerability: 15a/15b independence is enforced at the READ channel (neither reads the
    other's files) but not at the RETRIEVAL channel. In today's batch, 3 of my 10 fetch attempts were
    refused by the fetch tool as "Already fetched … 14–27s ago in this session," for URLs I had never
    fetched:
      - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8508177/  (ASSUMPTION-1164; 24 s)
      - https://peerj.com/articles/cs-193/                      (PRESUMPTION-844; 27 s)
      - https://pcaobus.org/Standards/Auditing/Pages/AS2315.aspx (ASSUMPTION-1153; 14 s)
    The most plausible explanation is that today's 15a, running concurrently on the same items and
    sharing the fetch layer, selected the same sources seconds earlier. I could not verify which agent
    fetched them and I received no content, so no read-channel breach occurred. But the observation
    shows (a) the two directions, given the same queue text and the same search engine, converge on
    the SAME sources for 3 of 5 items, and (b) the fetch layer couples the agents — the first to fetch
    a URL denies the second its content, so source access is order-dependent.

  Why this matters: the 15a/15b design treats agreement or disagreement between directions as
    evidence (both-support → SUPPORTED; 15a-support + 15b-challenge → CONTESTED). If both directions
    draw on one retrieval pipeline that returns the same top results, their agreement is partly an
    artefact of shared retrieval, and their apparent opposition is partly the same source read with
    two framings. This is the same-model-family correlation REVISE-350 records, operating one layer
    lower (retrieval rather than reasoning). Also: in all three cases the source in question was the
    single most decision-relevant document for the item (the only controlled decomposition
    experiment; the audit standard that states the asymmetric loss; the only operationalisation of
    question-generation), so 15b's evidence grade on exactly those sources fell to search-result level.

  Literature basis: none searched for this flag (it is an in-pipeline observation, not a literature
    finding). Conceptually adjacent: correlated-error/ensemble-diversity arguments already cited for
    REVISE-350 and MONITOR-547; Song 2026 arXiv:2603.16244 (parallel independent runs vs. shared
    context) as recorded in the cycle-0 PRESUMPTION-863 file. No new citation is offered.

  Risk level: High

  Recommendation (what the system should consider, not a design decision):
    1. Record, per searched item, the set of URLs each direction fetched; 15c should compute source
       overlap before treating 15a/15b agreement as independent corroboration.
    2. Give 15a and 15b separate fetch caches (or run them in separate sessions), so neither is
       denied content by the other's prior fetch.
    3. Consider deliberately diversifying retrieval (different query seeds, required venue lists per
       direction) for items where the queue block names a single owed body of literature — that is
       when convergence is most likely.
    4. Treat today's three dedup refusals as fetch FAILURES in 15b's counts (done), not as evidence
       about the sources.

PROVENANCE:
  Origin: 15b (re-trigger cycle 1 batch, 2026-10-09)
  Chain: [14a/14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1) → SYSTEMIC-RISK flag]
  Items: ASSUMPTION-1164, PRESUMPTION-844, ASSUMPTION-1153 (direct); 15a/15b pairing generally
  Transform at this step: cross-item vulnerability flag raised by 15b
  Current status: FLAGGED — for 15c and Tom
  Note: PROVENANCE block appended by the orchestrator (15b omitted it); content above is 15b's unchanged.
