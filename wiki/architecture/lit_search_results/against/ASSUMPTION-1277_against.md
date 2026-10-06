SEARCH-AGAINST-ASSUMPTION-1277:
  Date searched: 2026-09-08
  Original item: ASSUMPTION-1277
  Original statement: A guard rule is not adopted until it passes a fixture AND a control in which the rule
    is neutralised fails — the paired falsifier is the adoption gate.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1277
    Item type: ASSUMPTION (stated — quoted from a commit message written with the designer present)
    Transform at each step:
      14a: Extracted verbatim from the attended session of 2026-09-07 ~10:50–11:00 and the
        `commit_daily_run.sh` fix message in `inbox/rc_sandbox/COMMIT_ME_2026-09-07.sh`; routed as a
        general methodological claim, not as a judgement on the specific guard.
      15b: Searched for challenging literature (2026-09-08), AGAINST direction only. Did not read the
        `for/` directory, `lit_search_returns.md`, or any 15a output.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Papadakis, M., Shin, D., Yoo, S. & Bae, D.-H., 2018. "Are Mutation Scores Correlated with Real
       Fault Detection? A Large Scale Empirical Study on the Relationship Between Mutants and Real
       Faults." ICSE '18, 40th International Conference on Software Engineering.
       [VERIFIED: PDF retrieved from coinse.github.io; abstract and Introduction read this run] — Using
       CoreBench and Defects4J, "all correlations between mutation scores and real fault detection are
       weak when controlling for test suite size." The reported strength of mutant-killing as a proxy
       for fault detection is largely a confound of how many tests you have. A single killed mutant —
       which is exactly what a neutralised-rule control is — carries close to no information about
       fault-detection capability under this result.
    2. Gay, G. & Salahirad, A., 2023. "How Closely are Common Mutation Operators Coupled to Real
       Faults?" (ICST/Mutation). [VERIFIED: PDF retrieved from greg4cr.github.io; abstract read this
       run] — Across 32,002 mutants from 31 operators against 144 real faults: "9.92% of the mutants
       are strongly coupled to real faults, and 51.03% of the faults have at least one strongly coupled
       mutant." Restated for this item: roughly half of real faults have *no* strongly coupled mutant
       anywhere in a 31-operator sweep. A gate consisting of one hand-chosen neutralisation is a
       vanishingly small sample of that sweep.
    3. Just, R., Jalali, D., Inozemtseva, L., Ernst, M.D., Holmes, R. & Fraser, G., 2014. "Are Mutants
       a Valid Substitute for Real Faults in Software Testing?" FSE 2014.
       [NOT-verified — cited from search-result summary; PDF not retrieved this run] — The commonly
       quoted figure is that 73% of real faults are coupled to at least one mutant, with the remaining
       27% requiring stronger or new operators. Even the most favourable headline number leaves about
       a quarter of real faults outside the reach of the whole mutant set.
    4. Wool, A., 2009/2010. "Firewall Configuration Errors Revisited." arXiv:0911.1240; and Wool, A.,
       2004. "A Quantitative Study of Firewall Configuration Errors." IEEE Computer 37(6).
       [VERIFIED: arXiv abstract page for 0911.1240 fetched and read; the 2004 Computer paper and its
       "over 80% of firewalls misconfigured" figure NOT retrieved — that number is from a search
       snippet] — Corporate rule-sets are "(still) poorly configured," and error count is positively
       correlated with rule-set complexity. The characteristic defect class in filter rules is
       over-permissiveness / over-broad match — a class that the paired falsifier is structurally
       blind to (see Summary).
    5. Michael, L.G. IV, Donohue, J., Davis, J.C., Lee, D. & Servant, F., 2019. "Regexes are Hard:
       Decision-making, Difficulties, and Risks in Programming Regular Expressions." ASE 2019;
       arXiv:2303.02555. [ABSTRACT-ONLY — title, venue, arXiv id and author list confirmed via search
       listings; findings taken from search-result summary, full text not retrieved. The claim resting
       on it is only: developers report regexes as hard to validate and are largely unaware of their
       risk classes] — If the author cannot validate the rule by reading it, the fixture pair is doing
       all the epistemic work, and the fixture pair is chosen by the same author with the same
       misconception.
    6. Lipsitch, M., Tchetgen Tchetgen, E. & Cohen, T., 2010. "Negative Controls: A Tool for Detecting
       Confounding and Bias in Observational Studies." Epidemiology 21(3):383–388; and the 2026
       guidance paper "Negative controls and how to use them" (International Journal of Epidemiology
       55(5)). [NOT-verified — both cited from search-result summaries; abstracts not opened this run]
       — The methodological point is the one that transfers: negative-control designs rest on an
       unverifiable assumption that the control shares the bias structure of the target, they "often
       lack specificity in the type of bias that they detect," and a passing negative control is
       evidence to be weighed, not a validity certificate.
    7. Petrović, G. & Ivanković, M. (with Fraser, G. & Just, R.), 2021. "Practical Mutation Testing at
       Scale: A View from Google." IEEE TSE. [NOT-verified — cited from search-result summaries;
       arXiv:2102.11378 not retrieved this run] — Google's own conclusion from ~15M mutants is that
       "achieving mutation adequacy is neither practical nor desirable"; value comes from surfacing a
       filtered set of *productive* mutants during review, not from the kill/no-kill gate itself.

  Strength of challenge: Moderate (strong against the *sufficiency* of the paired falsifier as an
    adoption gate; no evidence found that the practice is harmful, or worse than a positive fixture
    alone)

  Summary: The literature does not contain the comparison the item asks for — I found no study of
  "positive fixture plus neutralised control" versus "positive fixture alone" for configuration guards
  or filter rules. What exists is the mutation-testing literature, which is the nearest formal analogue
  and which has moved consistently *against* the inference the assumption makes. Papadakis et al. (2018)
  show the mutant-kill signal correlates only weakly with real fault detection once test-suite size is
  controlled; Gay & Salahirad (2023) show that about half of real faults have no strongly coupled mutant
  even across 31 operators; Google's own scaled deployment concludes mutation adequacy is not a sensible
  target. The deeper objection is structural rather than statistical. A neutralised-rule control is a
  *sensitivity* test: it proves the rule is reachable, wired in, and load-bearing on the chosen fixture.
  It is not a *specificity* test, and it cannot become one — an over-broad guard (one that matches or
  blocks more than intended) passes the positive fixture and also fails correctly when neutralised. The
  gate therefore returns "adopt" on precisely the defect class that the firewall/filter-rule literature
  identifies as dominant (Wool). Because the fixture and the neutralisation are authored by the same
  agent from the same mental model of the rule, and the regex literature says that mental model is
  frequently wrong and hard to check by reading, the pair is two draws from one distribution rather than
  two independent tests. The negative-control literature in epidemiology reaches the same conclusion from
  the other direction: a passing negative control does not license the inference, because the control's
  bias structure is assumed, not verified.

  Specific risks: (a) The gate certifies over-broad guards. A rule that blocks or matches too much
  passes the fixture and fails the neutralisation, is adopted, and then silently suppresses legitimate
  items — a failure mode with no fixture and no alarm, and one this project has an existing exposure to
  wherever guards filter registers, commits, or agent inputs. (b) The gate creates adoption confidence
  proportionate to its ceremony rather than its coverage: two tests feel like corroboration, but they
  are one hypothesis tested twice from the same side. (c) Scale failure: at one guard the method is
  cheap and probably net-positive; as the guard set grows, "passed the paired falsifier" becomes an
  adoption *entitlement*, and the population of adopted-but-unmeasured guards grows monotonically with
  no escape-rate measurement anywhere. (d) Because the pair is authored together, a guard whose fixture
  encodes the author's misreading of the requirement will pass both limbs and be recorded as
  falsification-tested.

  Mitigations available: Add a third, independent limb that tests specificity — a *negative fixture*: an
  input that the guard must NOT act on, authored (ideally) from the requirement rather than from the
  rule text, and required to pass with the rule live. That converts a sensitivity pair into a 2x2 and
  closes the over-broad blind spot at roughly the same cost. Where the guard is a filter or regex,
  prefer a small corpus over a single fixture (the regex literature's own recommendation). Record, per
  guard, whether the fixture was derived from the rule or from the requirement — same-source fixtures
  should not count as independent. Finally, measure the thing the assumption asserts: log guard
  false-positive and false-negative incidents after adoption, so that "reduces defect escape" becomes a
  number in this repo rather than a methodological belief.

  Search scope: Preliminary — 6 queries plus 3 document retrievals. Covered: mutant/real-fault coupling
  (three papers), mutation score validity under size control, industrial mutation practice, firewall and
  regex rule defect studies, and negative-control methodology in epidemiology. Not covered: the assertion-
  adequacy / "checked coverage" line (Schuler & Zeller), metamorphic testing, the configuration-testing
  literature (Yin et al. on misconfiguration), and any study of paired-falsifier designs in laboratory
  protocol validation. Broader search recommended before the item is dispositioned as settled: the
  central comparison is genuinely absent from what was searched, and that absence — not a refutation —
  is the main finding.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1277
  Strongest counterargument: The paired falsifier is not a falsifier. It asks one question — "does this
  rule do anything on this input?" — and answers it twice, once from each side. It cannot detect the
  defect that filter rules and guards actually have, which is not inertness but over-reach: an over-broad
  rule passes the positive fixture and fails the neutralised control exactly as a correct one does, so
  the gate returns "adopt" on the dominant misconfiguration class. Worse, both limbs are authored from
  the same reading of the requirement by the same agent, so a misunderstanding of what the guard should
  match is preserved intact through both tests and comes out the other side stamped as
  falsification-tested. The formal analogue, mutation testing, has spent a decade discovering that the
  kill signal is weak evidence of fault detection once confounds are controlled, and that about half of
  real faults are not strongly coupled to any mutant at all — and a paired falsifier is a single mutant
  at a single site, the weakest possible instance of that already-weak signal. The method's real value
  is that it catches wiring errors, which is worth having and costs almost nothing; the claim that it is
  "the adoption gate" is what the literature does not support.
  What would need to be true for C2A2 to be safe: Guard defects in this repo would have to be
  predominantly inertness defects (rule not wired in, rule shadowed, rule never reached) rather than
  scope defects (rule matches too much or too little). Additionally, fixtures would have to be derived
  from the stated requirement independently of the rule text, so that the two limbs are not two views of
  one belief. If both hold, the pair is close to sufficient; if the second fails, the gate's
  falsification claim is decorative.
  How to test: Take every guard adopted under this gate. For each, write one negative fixture — an input
  that the guard must leave alone — derived from the guard's stated purpose without looking at its
  implementation. Run all of them against the live guards. The fraction that fail is the escape rate the
  paired falsifier missed. If that fraction is above roughly 10%, the gate is not an adoption gate; it is
  a wiring check. A second, cheaper check: for each adopted guard, ask whether its fixture was written
  before or after the rule text — after-the-fact fixtures are the same-source case and should be counted
  separately.
