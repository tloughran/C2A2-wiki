SEARCH-FOR-PRESUMPTION-707:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-707
  Original statement: That naming the queue non-determinism explains it; "the
    --max starvation artifact again" presents as diagnosed a phenomenon that
    does not obviously cover three identical calls returning 31/24/31 with
    disjoint membership. Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-707
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Tested the proposed mechanism against a prior observation it does
        not cover.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. MySQL Reference Manual, section "LIMIT Query Optimization" (dev.mysql.com,
       versions 5.7 / 8.0 / 8.4 / 9.7 all located this session). — Direct
       vendor-documented support for the *membership* half of the observation.
       The manual states that where multiple rows have identical values in the
       ORDER BY columns the server may return them in any order and may do so
       differently depending on the execution plan, and that the sort order is
       nondeterministic with respect to non-ordered columns. A bounded query
       without a total order is documented as free to return a different subset
       on each execution. Disjoint membership across three identical calls is
       exactly what this predicts.
    2. Percona, "Non-Deterministic Order for SELECT with LIMIT"
       (percona.com blog); Snowflake Community article "SELECT query with LIMIT
       clause returns non-deterministic result if ORDER BY clause exists in
       different level"; PostgreSQL commit message noting that LIMIT without
       ORDER BY can produce inconsistent results (postgresql.org message
       20070608202618). [All located this session; none opened beyond the
       returned summaries.] — Cross-vendor confirmation that this is a
       recognised, named, well-documented class of behaviour rather than a
       local mystery. Percona's stated mechanism is the useful one for this
       item: with parallelism, the table is split and multiple threads each work
       on their own piece, and results otherwise follow physical file order,
       which shifts with updates and deletes. That is a mechanism that produces
       genuinely arbitrary membership, and it supports the run's instinct that
       what it was seeing had a known name.
    3. Starvation (computer science) / Resource starvation — Wikipedia and
       standard OS-course treatments (GeeksforGeeks, Scaler, LibreTexts
       "6.3: Starvation"), all located this session. — Located as support for
       the term used and it does not support it. Starvation is defined as a
       process being *perpetually* denied a resource because it is continuously
       given to others, typically under priority-based scheduling; the located
       material draws the distinction this item needs explicitly, noting that a
       mutual-exclusion algorithm choosing arbitrarily between two processes is
       deadlock-free but not starvation-free, and that arbitrary or
       nondeterministic selection is *not* the same thing as starvation, which
       requires a systematic and persistent denial rather than unpredictable
       allocation. The observation described — 31/24/31 with disjoint membership
       — is unpredictable allocation, and if anything the disjointness is
       evidence *against* starvation, since a starved item would be
       persistently excluded rather than appearing in one call and not another.
       The label appears to be misapplied even though the underlying phenomenon
       is real.
    4. Digital-forensics reliability material — "Reliability validation enabling
       framework (RVEF) for digital forensics in criminal investigations,"
       Forensic Science International: Digital Investigation / ScienceDirect
       (S266628172300063X, authors and year not captured in the snippet and NOT
       verified). — Supplies the standard this item is implicitly holding the
       query to, and it is a demanding one. The located material states that
       only deterministic algorithms can be used in forensic work because
       reproducibility requires that identical input give identical output, and
       that where repeatability cannot be achieved the evidential value of the
       result drops considerably. Applied here, it is support for the *practical
       stakes* of the item rather than for the presumption: an audit query whose
       result set changes between identical invocations has, by this standard,
       reduced evidential value regardless of whether the cause has a name.
    5. Preprint material on deterministic orchestration for audit and governance
       — titles located this session include "Auditable Climate Risk
       Intelligence from Fragmented ESG Data: Deterministic Orchestration..."
       (arXiv 2606.02604) and "Protocol-Driven Development: Governing Generated
       Software Through Invariants and Continuous Evidence" (arXiv 2605.12981).
       [Titles/IDs only; not opened; no claims taken from them beyond the
       existence of the design pattern.] — Weak, listed for completeness. The
       recurring pattern is deterministic seed control, immutable logging and
       replayability as prerequisites for auditability. This supports the
       existence of a remedy, not the adequacy of the diagnosis.

  Strength of support: Moderate (that the phenomenon is real and documented);
    Weak (that the label given explains this observation)

  Summary: The run was pointing at something real. Non-determinism in bounded
    query result sets is one of the best-documented behaviours in database
    practice, is stated explicitly in the MySQL manual and echoed by Percona,
    Snowflake and PostgreSQL, and its documented mechanisms — plan variation,
    parallel splitting, physical file order shifting with updates — produce
    exactly the disjoint membership across identical calls that was observed.
    To that extent, invoking a known artefact was reasonable. What the search
    does not support is the naming. "Starvation" has a specific technical
    definition — perpetual, systematic denial of a resource to a particular
    process under a scheduling policy — and the located sources draw the exact
    distinction 14b is pressing, stating that arbitrary or nondeterministic
    selection is not starvation. Disjoint membership is if anything evidence
    against starvation, since a starved item would be persistently absent
    rather than present in one call and absent in the next. The count variation
    (31/24/31) is also not covered: ordering instability under a cap explains
    *which* items come back but not *how many*, and no located source explains
    a bounded query returning fewer than its bound on some invocations without
    a further mechanism such as partial results, timeout truncation or a
    changing underlying set. The presumption 14b surfaced — that naming it
    finished the diagnosis — is therefore not sustained: a real phenomenon has
    been given the wrong name, and the wrong name conceals the residue the name
    does not cover.

  Caveats: I do not know C2A2's query substrate. If the "--max" queries are not
    SQL at all — a filesystem walk, a grep over a vault, an agent-mediated
    search — then sources 1 and 2 transfer only by analogy, though the analogy
    is decent since the underlying cause (no total order plus a cap) is
    substrate-independent. The count variation could be explained by a mechanism
    the item does not name and the search did not look for; I searched for
    starvation-versus-ordering and for query non-determinism, not for partial
    result or truncation semantics, so absence of an explanation here is partly
    an artefact of scope. Source 4's author list and year are unverified.
    Sources 2 and 5 are vendor blogs and unopened preprints respectively. One
    argument in the run's favour that no source refutes: an operator who has
    seen a phenomenon repeatedly may legitimately use a local shorthand that is
    not the textbook term, and the mislabelling would then be a communication
    defect rather than a diagnostic one — the item cannot distinguish these
    from the outside and neither can the literature.

  NOVELTY-FLAG: Not raised. Query result non-determinism and the definition of
    starvation are both settled. The uncovered residue — a bounded query
    returning varying counts below its bound across identical invocations — is
    a well-formed question that the located sources simply do not address, and
    is better characterised as an unsearched seam than as a literature gap.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: non-determinism in bounded query
    result sets, LIMIT-without-ORDER-BY semantics across MySQL, PostgreSQL and
    Snowflake; the formal definition of resource starvation and its distinction
    from nondeterministic ordering; reproducibility and determinism requirements
    for audit and forensic evidence. Not searched, and recommended: partial
    result and truncation semantics in paginated or timeout-bounded APIs, which
    is the most likely home of an explanation for the count variation; and
    snapshot isolation / read consistency, which would cover the case where the
    underlying set is itself changing between calls.
