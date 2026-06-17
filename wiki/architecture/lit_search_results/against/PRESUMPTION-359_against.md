SEARCH-AGAINST-PRESUMPTION-359:
  Date searched: 2026-06-17
  Original item: PRESUMPTION-359
  Original statement: "[inferred] Git history is a complete census of PRS-triplet production ('264 produced', not '264 git can see')."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-359
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated census claim (git record = full production population)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes (Strong)

  Sources:
    1. Kalliamvakou et al. 2014, "The Promises and Perils of Mining GitHub" (MSR) — a foundational warning that the repository is NOT a complete record of work: much activity happens off the tracked history; commits are not a census of what was done. Directly refutes "git history = complete census."
    2. Repository-mining coverage threats — rebases/squashes/force-pushes rewrite or delete history; pre-VCS and out-of-band artifacts never enter it; the log enumerates the COMMITTED, not the PRODUCED. Map-vs-territory: the tool's record is mistaken for the population.
    3. Survivorship/coverage bias — counting only what the instrument captured and calling it the population is a textbook coverage error; "264 git can see" != "264 produced."

  Strength of challenge: Strong

  Summary: The census claim is strongly challenged by the canonical MSR caution (Kalliamvakou et al. 2014) and basic coverage reasoning: git records what was committed under a tracked workflow, not the full population of what was produced. Rewritten history, pre-VCS drafts, and out-of-band authoring all sit outside the log, so "264 produced" overstates what is really "264 the git record contains." This is the map-vs-territory / survivorship error: the instrument's record is being read as the territory.

  Specific risks: Production is systematically undercounted (invisible pre-VCS/out-of-band work) or miscounted (rewritten history), while the system reports the git number as the true production; couples ASSUMPTION-322 (creation-dating) and PRESUMPTION-355 (birth-rate) — all inherit the coverage gap.

  Mitigations available: Phrase as "264 in the tracked history" not "264 produced"; audit for rebases/squashes and pre-VCS artifacts; state the coverage boundary explicitly; if a complete census is needed, reconcile git against an independent inventory.

  STEELMAN:
    Strongest counterargument: If PRS triplets are born-in-repo by workflow — created only by committing to traditions/*/prs_triplets.md, never drafted elsewhere — then the git log IS by construction the complete population, and the MSR cautions (aimed at multi-tool OSS workflows) do not bite for this closed, single-author, single-store pipeline.
    What would need to be true for C2A2 to be safe: Verified no out-of-band creation path and no history rewriting that drops/moves triplets — then git is a true census of the tracked store (still labeled as such).
    How to test: Audit for pre-commit drafts, squashed/rebased history, and any triplets that exist outside the tracked file; if none, the born-in-repo census claim holds for the store.

  Search scope: MSR completeness/coverage (Kalliamvakou 2014); history-rewriting threats; survivorship/map-vs-territory. Comprehensive. (Couples ASSUMPTION-322, PRESUMPTION-355.)

  Recommendation: CHALLENGED
