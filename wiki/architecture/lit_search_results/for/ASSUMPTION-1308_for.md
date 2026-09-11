SEARCH-FOR-ASSUMPTION-1308:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1308
  Original statement: "**FLAG-023 is time-limited.** Two Kastrup sources six days apart bracket a live
    Levin exchange — a timestamped displacement measurement the inter-tradition study almost never
    gets... Method note in CROSS-135: **code it independently in both wikis before comparison, or the
    number is worthless.**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1308
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed. A rare case of a method fixed *before* the data can be obtained
        — the opposite of the pattern REVISE-436 tracks. No owner and no date attached to the
        member-access step.
      15a: Searched for supporting literature; found a large, well-quantified literature supporting the
        control (blinding/independent coding) with specific effect sizes, but NOT supporting the word
        "worthless."
    Current status: PARTIALLY-SUPPORTED

  Register pre-check: Several ACTIVE premises bear, and the independence family is the relevant one.
    - PREMISE-156: "CHECKS THAT SHARE AN INPUT DATUM ARE ONE CHECK, AND METHOD-DIVERSITY REMEDIES DO
      NOTHING AGAINST THEM." Directly governs the mechanism the method note is protecting against.
    - PREMISE-096: no self-produced artifact may certify itself; a corroborating layer must draw on a
      genuinely disjoint evidence source.
    - PREMISE-080: a pre-specified battery of operationally independent indicators is more robust —
      conditional on demonstrated independence, since shared method variance yields pseudo-convergence.
    - PREMISE-078: self-testing is rendered substantially non-vicious by specifying the falsifier
      independently of outcomes (register, then look) — necessary, but sufficient only when the
      specification is exhaustive (thresholds, exclusions, analysis path pre-committed). This directly
      bears on the pre-registration aspect of CROSS-135 and states its limit.
    Also PREMISE-197, PREMISE-180 (correlated errors among model-generated judgements). Searched anyway
    per OPEN-192.

  Supporting evidence found: Yes (for the control); No (for "worthless")

  Sources:
    1. Hróbjartsson A. et al. 2012. "Observer bias in randomised clinical trials with binary outcomes:
       systematic review of trials with both blinded and non-blinded outcome assessors." BMJ 344:e1119.
       — SECONDARY (BMJ full text not retrieved; figure read directly from the CEBM Oxford Catalogue of
       Bias entry, which I fetched in full) — Non-blinded outcome assessors generated odds ratios
       exaggerated by 36% on average. This is the best-quantified effect size available for the exact
       control CROSS-135 pre-registers, and it comes from a design (trials with BOTH blinded and
       non-blinded assessors on the same data) that isolates the assessor effect cleanly.
    2. Hróbjartsson A. et al. 2013. CMAJ 185:E201-11 (measurement-scale outcomes). — SECONDARY (same
       source) — Non-blinded assessment exaggerated effect size by 68%.
    3. Hróbjartsson A. et al. 2014. Int J Epidemiol 43:937-48 (time-to-event outcomes). — SECONDARY (same
       source) — Non-blinded assessment overstated the hazard ratio by approximately 27%.
    4. Mahtani K., Spencer E.A., Brassey J. "Observer bias." Catalogue of Bias, CEBM, University of
       Oxford, 2017. — VERIFIED (fetched in full) — The source from which 1-3 above are taken; also
       supplies the preventive-steps framing (separating access to exposure data from outcome data) and
       the finding that observer bias is reducible but not eliminable, and that training reduced
       between-nurse variation without removing it.
    5. Cochrane Handbook for Systematic Reviews of Interventions, ch. 1 (Starting a review) — on protocol
       pre-registration. — SECONDARY (chapter retrieved via search results) — Publishing a protocol
       "written without knowledge of the available studies reduces the impact of review authors' biases,
       promotes transparency of methods and processes, reduces the potential for duplication, [and]
       allows peer review of the planned methods before they have been completed." Direct support for the
       pre-registration limb of CROSS-135 specifically — a method fixed before the data exist is the
       recommended form, not an anomaly.
    6. Inter-rater reliability practice (Landis & Koch 1977 kappa benchmarks; the Jergas & Baethge
       meta-analysis reports mean kappa 0.76 across studies reporting it, and kappa 0.26 for minor errors
       in the one study reporting them separately). — VERIFIED for the kappa figures (Jergas & Baethge
       PeerJ 2015 full text fetched) — Illustrates that independent coding does not automatically produce
       agreement, and that reliability collapses for the finer-grained judgements. Relevant because a
       "displacement" code is closer to a minor-error judgement than to a binary death outcome.

  Strength of support: Strong (for limb a: independent coding before comparison is a warranted control);
                       None (for limb b: that a non-blind measurement here is "worthless").

  Summary: Limb (a) is strongly supported and quantified. Hróbjartsson's three systematic reviews are the
    canonical measurement of exactly this control, use the strongest available design, and give
    consistent directional exaggeration of 27-68% depending on outcome type. The pre-registration
    element of CROSS-135 is separately endorsed by Cochrane's guidance on protocols written before the
    studies are known. Limb (b), the word "worthless," is not supported by anything retrieved and is
    contradicted by the shape of the evidence: the literature's finding is that non-blind assessment
    produces a *biased but informative* estimate with a characterised direction and magnitude, which is
    why meta-epidemiology can correct for it. A 36% exaggeration is a large bias, not an absence of
    signal. The honest form of the method note is "code it independently, or the number carries an
    exaggeration bias of the order of tens of percent in a known direction and cannot be reported
    uncorrected" — which is a strong enough claim to do the work the run wants it to do.

  Caveats:
    - Domain transfer is the main concern. All three Hróbjartsson reviews are RCTs in clinical medicine
      with a treatment allocation to be blinded to. The FLAG-023 setup has no allocation; the analogue is
      "coder knows what the other wiki said," which is closer to non-independent content analysis than to
      unblinded outcome assessment. The direction transfers; the 36% does not, and must not be imported
      as a number into any C2A2 artifact.
    - The kappa evidence cuts both ways. Independent coding is necessary but does not deliver reliability
      on its own: the one retrieved study that separated major from minor judgements found kappa 0.26 for
      the finer-grained call. An independently coded displacement number with unmeasured inter-rater
      reliability is not obviously better than a non-blind one with a declared bias — PREMISE-080's
      "conditional on demonstrated independence" caveat applies, and the method note does not currently
      specify a reliability statistic.
    - n = 2 sources, six days apart, with one exchange. The measurement is a single event; PREMISE-136's
      accrual-design point applies and no blinding protocol recovers power that the design does not have.
      The methodological care here is disproportionate to the achievable denominator.
    - PREMISE-078 applies with force: pre-registering "code independently" is not an exhaustive
      specification. Thresholds, exclusions, and the analysis path are not pre-committed in CROSS-135 as
      quoted, so the register-then-look protection is only partial.
    - The gating step (member access to a paywalled dialogue) has no owner and no date. The window is
      stated to be time-limited; nothing in this search addresses that, and it is the binding risk.

  Search scope: comprehensive search — blinding of outcome assessors and observer bias effect sizes
    (Hróbjartsson trio via CEBM Catalogue of Bias), blinded outcome assessment in open trials,
    inter-rater reliability and kappa benchmarks, pre-registration and protocol publication (Cochrane
    Handbook ch. 1), independent double coding in content analysis.

  Recommendation: PARTIALLY-SUPPORTED — the recommendation rests on limb (a), which is strongly and
    quantitatively supported. Limb (b) ("worthless") is NO-SUPPORT-FOUND and should be restated as a
    magnitude-and-direction claim. Recommend the method note be amended to (i) drop "worthless,"
    (ii) add a pre-committed reliability statistic, and (iii) name an owner and date for the member-access
    step, which is the actual load-bearing dependency.
