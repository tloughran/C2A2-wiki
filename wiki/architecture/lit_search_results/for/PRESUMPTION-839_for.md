SEARCH-FOR-PRESUMPTION-839:
  Date searched: 2026-08-19
  Original item: PRESUMPTION-839
  Original statement: That a consecutive-failure streak counted within one task lineage is the fleet's
    streak. Six runs, one night, six correct and mutually inconsistent counters for one condition; no
    fleet-level denominator exists.

  Reading used for this search: the FOR direction is read as support for 14b's diagnosis — that inferring
  a population-level quantity from a within-partition count is a named, studied inferential error, and
  that partitioned observation systematically under-reports correlated failure.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-839
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by placing six same-night breach counters side by side and asking what would have to
        be true for all six to be correct and none to be actionable.
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Diez-Roux, A. "A Glossary for Multilevel Analysis," Pan American Health Organization /
       *Epidemiological Bulletin*. [consulted via www3.paho.org; author named on the page] — Defines the
       *atomistic fallacy*: "the conceptual model being tested corresponds to the higher level, but the
       data are collected for a lower level." This is a precise formal name for the error PRESUMPTION-839
       identifies — a fleet-level (higher-level) claim evidenced by lineage-level (lower-level) counts.
    2. "The (forgotten) atomistic fallacy in political science and its implications for how we interpret
       elections." *European Journal of Political Research* (Cambridge Core). (author list not verified) —
       States that the atomistic fallacy is "underpinned by the same logic as the ecological fallacy,
       namely the erroneous practice of making inferences about one level of analysis by using data from
       another," working in the opposite direction, and notes it "remains relatively underexplored."
       Supports both the diagnosis and 14b's implicit claim that this error is easy to miss.
    3. "[Roaming through methodology. XXVI. The ecological fallacy and its less well-known counterpart,
       the atomistic fallacy]." PubMed 11103669. (Dutch-language; author list not verified) — Confirms the
       ecological/atomistic pairing as established methodological vocabulary in the health sciences.
    4. Multilevel-modelling teaching materials (ReStore unit 5.4; SAGE, "What Is Multilevel Modeling and
       Why Should I Use It?"). [textbook/teaching sources] — State that analysing at the individual level
       while ignoring context misses group-level effects, and that the remedy is a model carrying both
       levels simultaneously. Supports 14b's structural point that no amount of correct per-lineage
       counting yields the fleet quantity; a fleet-level denominator has to be constructed.
    5. Kish, L. — design effect / effective sample size. [established-work] Standard apparatus for the
       related point that clustered observations do not aggregate as independent ones.

  Strength of support: Strong (for the inferential-error diagnosis); Weak (for the specific
  distributed-monitoring limb)

  Summary: 14b's diagnosis has an exact, long-established name in the multilevel-analysis literature: the
  atomistic (or individualistic) fallacy — drawing conclusions about a group-level outcome from
  lower-level data. The sources found define it, pair it explicitly with its better-known mirror the
  ecological fallacy, and note that the standard remedy is to model both levels rather than to count more
  carefully at one. This directly supports the item's core structural claim: six per-lineage counters can
  each be correct and none can be the fleet's streak, because the fleet quantity is not a function of any
  single partition's series. The literature also supports the "none actionable" consequence: without a
  fleet-level denominator the base rate is not estimable, so no threshold can be set. The
  distributed-monitoring limb of the search angle was only weakly served — the on-topic hits were patent
  filings rather than research, and I found no study quantifying under-reporting of correlated failure
  under partitioned observation.

  Caveats: The atomistic-fallacy literature is epidemiological, political-science and educational; it
  concerns statistical inference from survey and observational data, not operational counters in an agent
  fleet. The mapping is conceptually clean but formally untested in this domain. Nothing found addresses
  whether constructing a fleet-level denominator is feasible or cheap here. The claim that all six
  counters were "correct" is an assertion about this vault, not something literature can adjudicate.
  Search scope: moderate for the fallacy; preliminary and largely unsuccessful for distributed-monitoring
  under-reporting — a targeted search of the SRE/observability and reliability-engineering literature on
  correlated-failure detection is recommended and has NOT been done.

  Recommendation: SUPPORTED
