SEARCH-FOR-PRESUMPTION-689:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-689
  Original statement: That a task specification is satisfiable; ten days of
    budget-breach disclosures treated the breach as the run's fault until one
    run measured that the mandatory preamble alone exceeds the ceiling. Risk:
    High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-689
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from one run inverting a claim ten prior runs made in the
        opposite direction.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. van Lamsweerde, A., Darimont, R. & Letier, E., 1998. "Managing conflicts
       in goal-driven requirements engineering." IEEE Transactions on Software
       Engineering 24(11). [Journal and year confirmed via multiple secondary
       records this session; volume/issue from established knowledge] — Denies
       the presumption at its foundation. The framework's premise is that a
       wide range of inconsistencies arise as goals and requirements are
       elicited, that resolving them is a *necessary condition* for successful
       development, and that conflict and divergence must therefore be
       discovered by formal and heuristic technique rather than assumed absent.
       Satisfiability is treated as a property to be established, never as a
       default. The introduction of "divergence" — a weaker conflict form where
       requirements are jointly unsatisfiable only under some boundary
       condition — is directly the shape of this item: a preamble and a ceiling
       that conflict only once the preamble's actual size is measured.
    2. Degiovanni, R., Alrajeh, D. et al., 2016. "Goal-Conflict Detection based
       on Temporal Satisfiability Checking." ASE 2016 (paper confirmed at
       doc.ic.ac.uk/~da04/publications/2016_goalconflict.pdf; full author list
       not verified). — The mechanised form of the same denial, and the closest
       analogue to what the eleventh run did by hand. Boundary conditions under
       which a goal set becomes unsatisfiable are computed automatically by
       satisfiability checking over the specification. The existence of a
       research programme devoted to finding these conditions is itself the
       evidence: if specifications could be presumed satisfiable, the field
       would not exist.
    3. Vaughan, D., 1996. The Challenger Launch Decision: Risky Technology,
       Culture, and Deviance at NASA. University of Chicago Press. And:
       Sedlar, U. et al. [author list uncertain], 2022. "A qualitative
       systematic review on the application of the normalization of deviance
       phenomenon within high-risk industries." Journal of Safety Research
       (ScienceDirect S0022437522001827). — Supplies the consequence the item
       is worried about. Normalization of deviance is the process by which
       departure from a stated rule becomes culturally defined as normal and
       acceptable because it conforms to workgroup practice; frequent
       engagement in the deviant practice standardises it and resets what
       counts as tolerable, from which further deviation proceeds. Ten
       consecutive disclosures of the same breach, each attributed to the run
       rather than the rule, is the documented onset pattern.
    4. Hale, A. & Borys, D., 2013. "Working to rule or working safely? Part 1:
       A state of the art review" and "Part 2: The management of safety rules
       and procedures." Safety Science 55. — The most directly transferable
       source, and it inverts the item's ten-day attribution. Hale and Borys
       contrast a top-down rational paradigm, in which rules are static
       comprehensive limits and violations are negative behaviour to be
       suppressed, with a constructivist paradigm in which rules are dynamic
       situated constructions and violation is often evidence that the rule
       does not fit the work. Their proposed framework places *monitoring and
       adapting the rules* at the centre, with the rule set treated as the
       object of revision. On this account, universal violation is a diagnostic
       reading on the rule, not an aggregate reading on the actors.
    5. Work-as-imagined versus work-as-done (Hollnagel and the resilience
       engineering literature; practitioner and review sources confirmed this
       session, primary Hollnagel texts not fetched — treat the framing as
       [UNVERIFIED] as to specific citation). And: Understanding procedural
       violations using Safety-I and Safety-II: the case of community
       pharmacies, PMC5862557. — Names the gap the item found and locates it as
       the main barrier faced by safety management. The pharmacy study is the
       useful empirical case: most violations were routine, judged by
       participants as unlikely to cause harm, and functioned to maintain the
       way work was actually done. Routine universal violation degrades the
       compliance signal precisely because it stops distinguishing anything.
    6. Desuetude and selective enforcement (legal doctrine). [UNVERIFIED —
       cited from established knowledge, not confirmed this session] — Noted as
       the adjacent legal principle rather than as evidence: a rule violated
       universally and enforced never loses normative force, and enforcement
       against any individual instance becomes arbitrary. Flagged for a later
       run to source properly; not relied on here.

  Strength of support: None

  Summary: No literature was found supporting a default presumption of
    specification satisfiability, and the two fields with most at stake —
    requirements engineering and safety-rule management — are both organised
    around denying it. Requirements engineering treats consistency and
    satisfiability as properties to be checked by formal technique, with an
    entire subfield devoted to computing the boundary conditions under which a
    goal set becomes unsatisfiable; that is the mechanised version of what the
    eleventh run did by measuring the preamble. Vaughan's normalization of
    deviance and Hale and Borys's rule-management review supply the second
    half: when violation of a stated rule is universal, the established reading
    is that the rule is wrong, and the culturally normal response — attributing
    each instance to the actor — is itself the documented pathology, because it
    resets the tolerance baseline without touching the cause. The ten-to-one
    ratio in this item (ten runs attributing the breach to themselves, one
    measuring the rule) is a textbook instance of the top-down rational
    paradigm Hale and Borys argue against. The compliance-signal degradation
    the item names is well attested: routine violations become the way work is
    done and stop carrying information.

  Caveats: There is one genuine boundary condition under which the presumption
    is defensible. For sufficiently expressive specification languages,
    satisfiability checking is undecidable or intractable, and the requirements
    literature acknowledges that current techniques either fail to consider the
    requirement set as a whole or cannot handle heterogeneous specifications in
    different languages. A working presumption of satisfiability is therefore
    sometimes forced by cost. That defence does not reach this case: the
    conflict here is arithmetic — a fixed preamble length against a fixed
    ceiling — and is decidable by one measurement, which is why one run could
    settle it. Further scope limits: the safety literature concerns human
    operators with tacit local knowledge, and the transfer to agent runs
    executing a written specification is by analogy; and the
    normalization-of-deviance material describes escalation toward catastrophic
    outcomes, which is not obviously the risk profile here. Source 3's second
    author list and source 2's full author list are uncertain.

  NOVELTY-FLAG: Not raised. Well covered, and the literature runs against the
    presumption.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Comprehensive. Concepts searched: normalization of deviance
    (Vaughan and the high-risk-industry systematic review); work-as-imagined
    versus work-as-done; routine and situational violation; Hale and Borys on
    safety rule management; requirements-engineering inconsistency management
    and conflict detection; goal-conflict detection by temporal satisfiability
    checking; procedures that cannot be executed as written. Not searched:
    contract law on impossibility of performance, and the resource-budget
    literature on infeasible constraint sets in scheduling — either could
    sharpen the "mandatory preamble exceeds the ceiling" case specifically.
