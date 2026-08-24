SEARCH-FOR-PRESUMPTION-844:
  Date searched: 2026-08-19
  Original item: PRESUMPTION-844
  Original statement: That the review artifact is the right instrument and only its depth is the problem.
    Four runs escalated the queue; none named the 677 KB, 54-card single-page review as a variable.

  Reading used for this search: this item is unusual for the FOR direction. The presumption 14b names is
  that *only depth matters and the artifact is not a variable*. Supporting literature would therefore be
  evidence that volume/depth is the dominant driver of review throughput and abandonment, with interface
  form second-order. I searched for that. I also record where the literature runs the other way, since
  cherry-picking is prohibited.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-844
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by noting that four independent escalations shared one framing of the bottleneck and
        that the artifact itself was never treated as a design choice.
      15a: Searched for supporting literature (2026-08-19)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. "Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision
       support system." PMC5387195. (author list not verified) — Reports that reminder acceptance drops by
       about 30% for each additional reminder received per encounter, and that acceptance is associated
       with work complexity and repeated alerts. This is the strongest support for the presumption as
       stated: sheer volume per session is a measured, strong driver of acceptance, independent of any
       interface manipulation.
    2. "Alert fatigue measurement in clinical decision support: a systematic review." *JAMIA* (2026),
       doi:10.1093/jamia/ocag064. (author list not verified) — Systematic review; notes that override
       rates of 49%–96% are routine and that override is influenced by both alert frequency and alert
       quality. Supports volume as a first-order driver, but explicitly does NOT support volume as the
       *only* driver. Also reports that alert-fatigue measurement itself is not consistently defined —
       a caution against treating "depth" as a clean measured variable.
    3. Judicial and clinical sequential-decision findings (parole-ruling fluctuation by session position;
       increased late-in-day antibiotic and opioid prescribing), as summarised in the sources consulted.
       [reported secondhand in review sources; primary papers not verified] — Would support the general
       claim that quantity-in-sequence degrades judgement quality.
    4. COUNTER-WEIGHT, recorded for honesty: "No evidence for decision fatigue using large-scale field
       data from healthcare." *Communications Psychology* (2025), doi:10.1038/s44271-025-00207-8; also
       PubMed 40011733 / PMC11865449. (author list not verified) — Large-scale field data finding no
       decision-fatigue effect, and stating that most prior evidence comes from retrospective designs
       without preregistration or external validation. This directly weakens source 3 and weakens the
       general "batch size degrades judgement" argument.

  Strength of support: Weak-to-Moderate

  Summary: The presumption's *first* clause — that depth/volume is a real and important driver of review
  throughput — has genuine empirical support from the alert-fatigue literature, where per-encounter alert
  count predicts acceptance with a large measured effect (~30% acceptance drop per additional reminder)
  and override rates in the 49%–96% range are routine. The presumption's *second* clause — that the
  artifact is therefore not a variable — is NOT supported. The JAMIA systematic review is explicit that
  alert quality as well as frequency drives override, which is precisely the claim that instrument design
  matters. And the broader decision-fatigue foundation on which a pure-volume account would rest has been
  substantially challenged by a 2025 large-scale field study finding no effect. On the specific question
  14b raised — whether a 677 KB, 54-card single-page review is itself a design variable — I found NO
  literature on interface granularity in human-in-the-loop review queues at all. That gap is itself the
  finding.

  Caveats: All quantitative support comes from clinical decision support, where alerts are interruptive
  and time-pressured; a self-paced wiki review page is a different task with different abandonment
  dynamics. The decision-fatigue literature is actively contested and should not be cited as settled. I
  did not locate any HCI or CSCW study of review-artifact granularity, batch presentation, or
  single-page-versus-paginated review queues; this may reflect a real gap or an inadequate search.
  Search scope: preliminary — covered alert fatigue and decision fatigue; did NOT cover the HCI
  literature on progressive disclosure, chunking, or triage-interface design, nor the code-review
  literature on change-set size and review effectiveness (which is likely the closest analogue and is the
  single most valuable unsearched avenue here).

  Recommendation: PARTIALLY-SUPPORTED
