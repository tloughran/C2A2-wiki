SEARCH-AGAINST-PRESUMPTION-707:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-707
  Original statement: That naming the queue non-determinism explains it; "the --max starvation
    artifact again" presents as diagnosed a phenomenon that does not obviously cover three
    identical calls returning 31/24/31 with disjoint membership.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-707
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Tested the proposed mechanism against a prior observation it does not cover — three
        identical calls returning 31/24/31 results with disjoint membership.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. PostgreSQL project documentation and mailing-list record on LIMIT without ORDER BY.
       Located this session: a pgsql commit message dated 2007-06-08, "Add note that LIMIT
       without ORDER BY can produce outright [wrong results]" (postgresql.org message-id
       20070608202618.2B12E9FBDBE), plus related -hackers and -general threads on UNION with
       LIMIT and on non-deterministic behaviour from parallelised sub-queries (BUG #15324
       thread, message-id 22819.1534183487). [Thread contents read only in search-summary form.]
       This is the most directly relevant mechanism in the literature: a bounded query without a
       total order over the result set is *specified* to be free to return any subset of the
       qualifying rows, and the returned subset varies across executions. Crucially, the
       documented cause is plan and parallelism variation — when a scan is split across workers
       and the bound is applied to whichever rows arrive first, successive executions return
       different rows, not merely the same rows in a different order.
    2. Snowflake knowledge-base article, "SELECT query with LIMIT clause returns
       non-deterministic result if ORDER BY clause exists in different level"
       (community.snowflake.com, located this session; author and date [UNVERIFIED]). Vendor
       documentation, cited for the operational statement: the bound picks rows arbitrarily
       unless the ordering is applied in the *same* statement scope as the bound. Directly
       relevant because a bounded audit query assembled from a subquery plus an outer cap is
       exactly this shape.
    3. Percona, "Non-Deterministic Order for SELECT with LIMIT" (percona.com blog, located this
       session; author and date [UNVERIFIED]) and Ben Nadel, "Always Use A Deterministic ORDER
       BY When Using LIMIT And OFFSET In MySQL" (bennadel.com, blog post 3197). Practitioner
       sources, non-peer-reviewed, cited for the consensus framing that this is a known,
       named, well-understood defect class with a standard remedy, and for the specific
       observation that the same query returns different rows on successive executions.
    4. Flaky-test and root-cause-attribution literature. Located this session: the Wikipedia
       "Flaky test" entry, Datadog's knowledge-center article on flaky tests, "Test Flakiness'
       Causes, Detection, Impact and Responses: A Multivocal Review" (ResearchGate record;
       authors, year and venue [UNVERIFIED]), and "Flaky Test Sanitisation via On-the-Fly
       Assumption Inference for Tests with Network Dependencies," arXiv 2208.01106 (identifier
       and title confirmed; authors [UNVERIFIED]). The directly transferable findings are: that
       many practitioners label a failure "flaky" *without* investigating the root cause, and
       that the inability to identify a clear reason for intermittent behaviour does not imply
       there is not one; that hidden non-determinism leaves root causes unaddressed and
       persisting; and that it is typically unclear to decision makers whether the flakiness
       originates in the system under test, in the test, or in the environment. This is the
       generic form of the presumption: a label that terminates investigation.
    5. Reproducibility requirements for audit and forensic evidence. Located this session: NIST's
       distinction between repeatability (same method, identical items, same laboratory,
       operator and equipment, short interval) and reproducibility (same method, identical items,
       different laboratories, operators and equipment), relayed via forensic-validation
       material (trustarray.com; ResearchGate record for "Reproducibility of Digital Evidence in
       Forensic Investigations"). [NIST definitions relayed from secondary sources; the NIST
       document itself was not retrieved.] The standard is that forensic results must yield the
       same outcome under identical conditions. Three identical calls returning different
       cardinalities with disjoint membership fails repeatability in the strict sense, which
       means any audit conclusion drawn from a single such call is unreproducible by
       construction.

  Strength of challenge: Strong

  Summary: The label does not fit the observation, and the literature makes the mismatch precise.
    "Starvation" is a scheduling term with a specific meaning — a subset of items is persistently
    denied service while others are repeatedly served. That predicts a *stable* excluded set and
    says nothing about cardinality varying between calls. What was actually observed — 31, 24 and
    31 results across three identical calls, with disjoint membership — is the documented
    signature of a different mechanism entirely: a bound applied to an unordered or partially
    ordered result set, where plan choice and parallel scan determine which qualifying rows reach
    the bound first. The database literature has named, documented and supplied a standard remedy
    for that mechanism for nearly twenty years, and the remedy (impose a total order in the same
    scope as the bound) is completely different from anything "starvation" would suggest. The
    flaky-test literature supplies the meta-point: labelling an intermittent phenomenon closes
    the investigation, and premature labels leave root causes in place. And the audit-
    reproducibility standard supplies the consequence: if identical calls return disjoint sets,
    every finding derived from a single call is unreproducible, so the non-determinism is not a
    cosmetic artifact but a defect in the evidentiary standing of the audit itself.

  STEELMAN:
    Item: PRESUMPTION-707
    Strongest counterargument: "Starvation artifact" may be shorthand rather than a causal claim
      — a local name for a known-and-tolerated class of query instability, used the way engineers
      say "the usual flake." Read that way, the summary is not asserting a mechanism at all, and
      14b has convicted a nickname of being a bad explanation. There is also a reading on which
      starvation genuinely is part of the story: if the underlying retrieval interleaves sources
      or shards and the bound truncates whichever sources respond first, then some sources *are*
      persistently under-served relative to others, and that is a starvation-shaped phenomenon
      even though the observable is membership variation rather than a stable excluded set.
      Cardinality variation (31/24/31) is also compatible with a timeout or partial-result path
      that starves a slow source on some runs and not others, which would make "starvation" the
      correct family and the disjointness a second-order effect. Finally, there is a real cost
      question: fully determinising an exploratory query — imposing a total order, removing the
      bound, paginating exhaustively — may be expensive on a large vault, and if the query is
      used for sampling rather than for enumeration, non-determinism is a feature. The presumption
      only bites if the query's output is being treated as an enumeration.
    What would need to be true for C2A2 to be safe: (a) the queries whose results feed the
      register are enumerations, not samples — and if they are samples, they are labelled as
      such and no completeness claim is drawn from them; (b) a total order is imposed in the same
      scope as any bound, which is the standard remedy and would eliminate membership variation
      whatever the underlying cause; (c) the mechanism has been distinguished empirically rather
      than named — specifically, whether the excluded set is stable (starvation) or varies
      (ordering instability), which a handful of repeated calls settles; (d) any finding already
      recorded from a bounded call is re-derived from an unbounded or ordered one before it is
      relied on, since the current findings are unreproducible; (e) the union across repeated
      calls is checked against an unbounded count, so the system knows whether the bound is
      truncating at all. Condition (c) is decisive and takes minutes: it is the difference
      between a diagnosis and a nickname.
    How to test: Immediately runnable. Issue the same call ten times and record the full result
      sets. Compute (i) the cardinality distribution, (ii) the size of the intersection across
      all ten, and (iii) the size of the union. If the intersection is small and the union
      substantially exceeds the per-call cardinality, the mechanism is ordering instability under
      a bound, not starvation, and the label is refuted. If instead a stable subset never appears
      in any of the ten, starvation is supported and the label is vindicated. Second test: issue
      the same query with an explicit total order and with the bound removed; if the result
      becomes stable and its cardinality equals the union from the first test, the diagnosis and
      the remedy are both settled. Third: check whether any conclusion currently in the register
      was drawn from a single bounded call; each such conclusion is unreproducible until
      re-derived, and the count of them is the size of the exposure.

  Specific risks: If the named mechanism is wrong, then (i) the remedy will be wrong — effort
    goes to fairness or scheduling when the fix is a total order in the right scope, and the
    instability persists after the fix is declared complete; (ii) the naming closes
    investigation, which the flaky-test literature identifies as the principal cost of premature
    labelling, so the real cause accrues further consequences unobserved; (iii) every audit
    finding derived from a bounded call is unreproducible, which means the register may contain
    counts, absences and completeness claims that a later run cannot confirm and cannot refute —
    the worst state for an audit record; (iv) *absence* findings are the most dangerous class
    here, because a call that returns 24 instead of 31 will report items as missing that exist,
    and disjoint membership means the missing set differs each time; (v) the word "again" in the
    summary indicates the phenomenon has recurred and been re-labelled rather than investigated,
    so the label has already survived at least one opportunity to be tested against evidence.

  Mitigations available: (1) Impose a total order in the same statement scope as any bound — the
    standard, documented remedy, and effective regardless of which mechanism is operating. (2)
    Remove the bound for any query whose output is treated as an enumeration; use bounds only
    where sampling is intended and label the output accordingly. (3) Run the repeated-call
    protocol above before assigning a mechanism, and record the intersection/union figures next
    to the diagnosis. (4) Mark every register finding derived from a bounded call as provisional
    until re-derived. (5) Adopt an explicit rule that intermittent phenomena are not assigned a
    named cause in the register unless the name has been tested against the observations it
    must cover — the generalisable form of what 14b did here by hand. (6) Log the query text and
    result cardinality with each finding so later reproduction is possible at all.

  Search scope: Comprehensive for the database mechanism (PostgreSQL project record, Snowflake
    knowledge base, MySQL practitioner sources), which is the literature that speaks most
    directly to the observation's actual signature. Adequate for the meta-level point about
    premature labelling of non-determinism, drawn from the flaky-test literature; those sources
    are a mix of peer-reviewed and practitioner material and the peer-reviewed items were
    reached via records rather than full texts. Preliminary on audit-query reproducibility — the
    NIST repeatability/reproducibility definitions were relayed from secondary forensic-
    validation sources and not confirmed against the NIST document. Not searched, and both
    directly relevant: the scheduling literature's formal definition of starvation and
    fairness (which would let the mismatch be argued from the definition rather than from the
    observation), and the information-retrieval literature on unstable result sets in bounded
    top-k queries. Broader search recommended on the former in particular — a formal statement of
    what starvation predicts would make this challenge decisive rather than strong.

  Recommendation: CHALLENGED
