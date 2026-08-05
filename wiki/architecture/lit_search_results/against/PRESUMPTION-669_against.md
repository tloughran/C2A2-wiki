SEARCH-AGAINST-PRESUMPTION-669:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-669
  Original statement: That a hold is a state with terms someone re-reads — whereas a
    length-only hold was read by two independent runs as "unreviewable," excluding a 15-pair
    band whose semantic content had never been reviewed, and the correction came only from a
    run that read the hold's terms rather than its label.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-669
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from one documented over-broad hold plus one condition known to be
        permanently unsatisfiable
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "An Empirical Study of Suppressed Static Analysis Warnings." FSE 2025 / Proceedings of
       the ACM on Software Engineering, DOI 10.1145/3715729. [AUTHORS UNVERIFIED — paper,
       venue, DOI and findings confirmed via ACM DL and the software-lab.org author copy;
       author list not retrieved.] — The first in-depth empirical study of warning
       suppressions, across Python, Java and JavaScript with Pylint, Checkstyle, PMD and
       ESLint. Three findings hit this presumption directly: (i) the number of suppressions in
       a project *continuously increases over time* — suppressions are effectively
       monotonically accumulating, i.e. nothing takes them out; (ii) 50.8% of suppressions do
       not affect any warning and are practically useless, which is only possible if nobody
       ever re-reads them against current state; (iii) suppressions, including the useless
       ones, *may unintentionally hide future warnings* — the over-broad-scope failure mode,
       which is the specific defect observed in the 15-pair band.
    2. ANSI/ISA-18.2-2016, Management of Alarm Systems for the Process Industries; and EEMUA
       Publication 191, Alarm Systems: A Guide to Design, Management and Procurement. — The
       normative standards for holds in a safety-critical setting require that shelving be
       time-bounded: a maximum time an alarm may remain shelved without being actively
       re-shelved, enforced by system default. The standards exist in this form precisely
       because unbounded suppressions were found not to be re-read. C2A2's hold has no
       expiry and no re-affirmation requirement, which the governing standard in the one
       industry that has formalised this treats as a defect by construction.
    3. Memon, A., Gao, Z., Nguyen, B., Dhanda, S., Nickell, E., Siemborski, R. & Micco, J.,
       2017. "Taming Google-Scale Continuous Testing." ICSE-SEIP 2017. — Google's account of
       operating continuous testing at scale, including the management of flaky and disabled
       tests as a first-class, continuously-growing population requiring dedicated machinery
       rather than case-by-case judgement.
    4. Luo, Q., Hariri, F., Eloussi, L. & Marinov, D., 2014. "An Empirical Analysis of Flaky
       Tests." FSE 2014, DOI 10.1145/2635868.2635920. — The foundational empirical
       characterisation of the population that gets quarantined; establishes that flakiness is
       a persistent, categorisable property rather than a transient one, so quarantine
       populations do not self-clear.
    5. "A Qualitative Study on the Sources, Impacts, and Mitigation Strategies of Flaky Tests,"
       arXiv:2112.04919 (ICST 2022). [AUTHORS UNVERIFIED — title, identifier and findings
       confirmed via search index.] — Reports that quarantining is among the most common
       practitioner measures, and explicitly lists as *open research questions*: how to deal
       with quarantined tests, how long tests should stay in quarantine, and how many may be
       quarantined at once. That these remain open is itself the evidence: the exit path from
       quarantine is unspecified in practice.
    6. Guo, P.J., Zimmermann, T., Nagappan, N. & Murphy, B., 2010. "Characterizing and
       Predicting Which Bugs Get Fixed: An Empirical Study of Microsoft Windows." ICSE 2010. —
       Whether a deferred defect is ever fixed is predicted by *social* variables — reporter
       reputation, same-team handling, geographic proximity — rather than by the defect's own
       terms. Deferral outcomes are therefore not governed by the recorded conditions, which is
       the presumption's load-bearing claim.
    7. Practitioner literature on test quarantine (Slack Engineering, "Handling Flaky Tests at
       Scale: Auto Detection & Suppression"; multiple independent CI-tooling sources).
       [GREY LITERATURE.] — Convergent on the same observation in near-identical language:
       quarantine without ownership is a graveyard; teams add quarantine as a fix but "later"
       never comes; the skip marker is in practice permanent because nobody schedules time to
       revisit it. The convergence across unaffiliated sources is what gives this weight.
    8. Vaughan, D., 1996. The Challenger Launch Decision. University of Chicago Press.
       [PRIMARY TEXT NOT DIRECTLY RETRIEVED; mechanism confirmed via multiple secondary
       safety-science sources.] — Normalization of deviance supplies the mechanism by which a
       hold's *scope* grows: each time the label is read rather than the terms, the broader
       reading survives without consequence and becomes the operative definition.
    9. Dekker, S., 2011. Drift into Failure. Ashgate. — The exclusion widened by two
       independent runs in the same direction is a two-step drift, and Dekker's point is that
       each step was locally reasonable: reading a label is cheaper than reading terms, and
       nothing punished it.

  Strength of challenge: Strong

  Summary: The presumption has two components and the literature challenges both. On
    persistence, the FSE 2025 suppression study is close to dispositive: suppression counts
    increase monotonically over project lifetimes and more than half of all suppressions no
    longer correspond to any live warning, a state that can only arise if the terms are never
    re-read against current conditions. The alarm-management standards corroborate normatively
    — ANSI/ISA-18.2 and EEMUA 191 mandate a maximum shelve time with active re-shelving, a
    control that exists only because the unbounded case was found to fail, and C2A2's hold has
    no such bound. On scope, the same study documents the precise mechanism observed: a
    suppression whose extent exceeds its justification silently hides material that was never
    within its rationale — here a 15-pair band whose semantic content had never been reviewed,
    excluded by a hold whose stated terms were about length only. Guo et al. add that the fate
    of a deferred item is predicted by social factors rather than by its recorded conditions,
    which directly denies that the terms are what govern. The item's own evidence is the
    strongest single datum: two independent runs read the label and got it wrong in the same
    direction, and only the run that read the terms got it right — a 2-to-1 empirical estimate
    of the base rate of label-reading, generated inside C2A2 without instrumentation.

  Specific risks: The immediate exposure is the 15-pair band: content whose semantics have
    never been reviewed is currently excluded from review by a hold that does not cover it, and
    unless the hold's terms are re-read by every future consumer, it will stay excluded
    indefinitely. Because the erroneous reading was independently reproduced by two runs, this
    is not an outlier — it is the expected behaviour, and the correct reading was the exception.
    Per the suppression study, the hold population will grow monotonically and a growing share
    of it will be stale, so the cost of the eventual audit grows superlinearly while the
    probability of anyone performing it falls. The permanently-unsatisfiable condition noted in
    the item is the acute case: a hold whose exit condition can never be met is not a hold at
    all but a silent permanent deletion of scope, presented in the data model as a temporary
    state, which means the system's own accounting of what is under review is wrong and will
    never self-correct. Per Vaughan/Dekker, each further label-reading widens the operative
    scope, so the excluded set drifts outward without any decision being taken to widen it —
    there will be no artifact recording the expansion. And the failure is compounding with
    PRESUMPTION-668 and PRESUMPTION-662: this system has several mechanisms that convert an
    open item into a quiescent record, and no mechanism that inventories quiescent records.

  Mitigations available: (1) Give every hold a mandatory expiry and require active
    re-affirmation to extend, per ANSI/ISA-18.2 shelving. This is the single highest-value
    change and it is purely mechanical: a date field plus a sweep. (2) Require holds to be
    machine-checkable: the hold's *terms* should be a predicate that a consumer evaluates,
    not prose that a consumer paraphrases. If the hold is "length > N," then the exclusion is
    computed, and no run can widen it by reading its label. This removes the observed failure
    class entirely rather than mitigating it. (3) Forbid unsatisfiable exit conditions at
    filing time: a hold whose release condition cannot be met must be recorded as a permanent
    exclusion with a named owner, which makes the scope loss visible in the accounting. (4)
    Report the held population as a first-class metric — count, age distribution, and count of
    holds whose terms have not been evaluated since filing. Per the suppression study, the
    useless fraction will be large and the number is the argument for acting. (5) Audit the
    15-pair band now and, separately, sweep every existing hold for scope-vs-terms mismatch;
    the observed defect is that the label is broader than the terms, which is detectable by
    comparing the excluded set against the predicate. (6) Record who read what: when a run
    applies a hold, log whether it evaluated the terms or the label. Two runs got this wrong
    and it was only caught by chance; the logging converts chance into measurement.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-669
    Strongest counterargument: The system detected and corrected this itself, within the same
      cycle, without external prompting — which is evidence that holds *are* re-read, just not
      by every reader. A population of runs in which two read the label and a third read the
      terms is a redundant reading architecture that produced the right answer; demanding that
      every run parse every hold's terms would be enormously more expensive and would slow
      every consumer to the speed of the most careful one. The suppression and quarantine
      literature concerns artifacts created by *different* people from those who later read
      them, over years, in codebases with turnover; C2A2's holds are days old, few in number,
      and read by agents that can be instructed to read terms. ANSI/ISA-18.2's shelve timers
      exist for operator alarm floods with thousands of shelved points and hard real-time
      consequences, a regime with no resemblance to a handful of review holds in a wiki. And
      an over-broad reading of a hold is a *conservative* error in the direction of reviewing
      less rather than asserting more — nothing false entered the vault; some true things were
      merely not yet examined.
    What would need to be true for C2A2 to be safe: (a) The careful reader is reliably present
      — i.e. the correction was structural rather than lucky. If the third run's terms-reading
      was incidental to its task, the redundancy is not a designed property and cannot be
      counted on. (b) The hold population stays small enough that occasional term-reading
      suffices; the suppression study's monotonic-growth finding predicts it will not. (c) No
      hold's exit condition is unsatisfiable — the item states that at least one is, which
      falsifies this outright and is the strongest single point against the steelman. (d)
      Deferred review is genuinely deferred rather than abandoned, which requires that some
      process eventually consumes the held set; PRESUMPTION-652 (27 items advanced unconsumed)
      is evidence that it does not.
    How to test: Direct. (i) Enumerate every open hold; for each, mechanically evaluate its
      stated terms against current content and compare the resulting set to the set actually
      being excluded. Any divergence is a scope error of the observed kind, and the count
      across all holds gives the base rate. (ii) For each hold, check whether its release
      condition is satisfiable at all; the unsatisfiable ones are permanent exclusions
      misfiled as temporary. (iii) Plot hold count and hold age over the vault's history — if
      the count is monotonically increasing and the median age is growing, the FSE 2025 result
      has reproduced here and the argument is settled empirically rather than by citation.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-05
    Affected items: PRESUMPTION-664, PRESUMPTION-666, PRESUMPTION-668, PRESUMPTION-669
      (continuous with PRESUMPTION-660, PRESUMPTION-661)
    Common vulnerability: All four substitute a *declaration* for a *measurement*. The system
      reads an artifact produced by, or adjacent to, the very process whose state is in
      question — an empty report channel (664), a status assertion (666), a retraction (668),
      a hold's label (669) — and treats that artifact as the state. 669 is the purest case: a
      label was read in place of the predicate it summarises, by two of three readers.
    Literature basis: FSE 2025 suppression study (monotonic accumulation; 50.8% useless;
      unintended hiding of future warnings); ANSI/ISA-18.2 and EEMUA 191 (mandatory maximum
      shelve time); Guo et al. 2010 (deferral outcomes governed by social not recorded
      factors); Vaughan 1996 / Dekker 2011 (scope drift without a deciding artifact); Huang et
      al. 2017 (differential observability).
    Risk level: Critical
    Recommendation: Adopt a single invariant across the monitoring and deferral layers — no
      claim about state may be derived from a summary artifact produced by, or standing in for,
      the subject of the claim. Operationally: holds carry machine-evaluable predicates and
      expiry dates; health claims carry evidence pointers; defect records outlive the run that
      filed them. Each of these is a small mechanical change; together they close the class.

  Search scope: Adequate. Concepts searched: quarantined tests and exit from quarantine;
    suppression accumulation and staleness in static analysis; over-broad suppression scope;
    alarm shelving and suppression management standards (ANSI/ISA-18.2, EEMUA 191); deferred
    and won't-fix defect outcomes; normalization of deviance and scope drift. Not searched:
    the legal/regulatory literature on sunset clauses and expiring waivers, and the medical
    literature on diagnostic label anchoring, both of which would likely add independent
    support for the label-vs-terms mechanism.
