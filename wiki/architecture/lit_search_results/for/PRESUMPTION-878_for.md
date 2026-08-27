SEARCH-FOR-PRESUMPTION-878:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-878
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake)
  Original statement: "[inferred] That the right response to a defect class found by hand is to build a
    downstream check — rather than to repair the process that generates the defect, or to accept that
    hand-reading is the instrument."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-878
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from absent alternatives — a one-member remedy space held across five runs,
        sharpened by the appearance of a generator-level hypothesis (ASSUMPTION-1211) that no run
        picked up. Medium-high confidence; the absence is clear, the alternatives are 14b's construction.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-26, five queries. Limbs covered: (a) cost-of-quality / PAF model
    (prevention–appraisal–failure) and the relative economics of prevention vs. appraisal spend;
    (b) defect containment vs. defect removal in software engineering, phase containment
    effectiveness, PSP review data; (c) Deming's Point 3 ("cease dependence on inspection") as the
    canonical statement of the *opposing* position, searched deliberately so the supportive case is
    stated against its strongest rival; (d) empirical effectiveness of automated static analysis and
    CI-integrated checking — the closest technical analogue to "build a deterministic check";
    (e) Wagner's quality-economics-of-defect-detection programme.
    Assessment: **moderate coverage — one limb not run.** I did not reach the human-factors literature
    on *manual inspection as a standing instrument* (the presumption's third, dismissed alternative:
    "accept that hand-reading is the instrument"), nor the specific literature on automated reference/
    citation checking tools, which would be the nearest domain-matched empirical precedent. Both are
    named as gaps. I also found no source addressing the item's live sub-issue — a *named but unbuilt*
    check, i.e. the delivery risk of the detection remedy rather than its effectiveness once built.

  Supporting evidence found: Yes

  Sources:
    1. Wagner, S. "A Literature Survey of the Quality Economics of Defect-Detection Techniques."
       arXiv preprint. https://arxiv.org/pdf/1612.04590 ; and Wagner, S. "A model and sensitivity
       analysis of the quality economics of defect-detection techniques." arXiv:1612.03785 /
       Proc. ISSTA 2006, https://dl.acm.org/doi/abs/10.1145/1146238.1146247 ; and Wagner, S.
       "Cost-Optimisation of Analytical Software Quality Assurance." TUM,
       https://mediatum.ub.tum.de/doc/619080/619080.pdf
       — The most directly relevant body of work: it treats defect-*detection* techniques as an
       object of economic optimisation in their own right, models their costs and benefits against
       failure costs, and derives a practical model for allocating QA effort. Its existence as a
       research programme is itself the support: building a detection technique is a rationally
       optimisable remedy, not a category error. SNIPPET-ONLY (abstracts and summary pages read;
       full PDFs not retrieved).
    2. "Preprint: An Empirical Study on the Effectiveness of Static C Code Analyzers."
       Technical University of Munich, https://mediatum.ub.tum.de/doc/1659728/1659728.pdf
       [authors unverified]
       — Empirical measurement of what automated downstream checkers actually catch. Supports the
       claim that a deterministic check reliably removes a defect class, while also reporting that
       agreement between tools is low (pairwise warning alignment typically under 10%), which bears
       on the caveats. SNIPPET-ONLY.
    3. "The Cost and Benefits of Static Analysis During Development." arXiv:2003.03001
       [authors unverified]
       — Reports that across 35 projects, applying static analysis reduced both escaped defect
       density *and* total development effort, whether applied shortly after coding or at build time.
       This is the strongest located empirical statement that a downstream automated check is net
       cost-reducing, not merely defect-reducing. SNIPPET-ONLY.
    4. "On the Benefit of Automated Static Analysis for Small and Medium-Sized Software Enterprises."
       arXiv:1611.07549 [authors unverified]
       — Finds that static analysis tools improve QA efficiency *conditional on* continuous use and
       good integration into the existing toolchain. Directly relevant: the benefit is contingent on
       the check actually being built and wired in — which is exactly the unmet condition in the
       C2A2 case (four named checks, none built). SNIPPET-ONLY.
    5. Cost-of-quality / PAF model, as presented in: "6.3 Cost of Quality," *Fundamentals of
       Operations Management* (eCampusOntario Pressbooks),
       https://ecampusontario.pressbooks.pub/fundamentalsopsmgmt/chapter/6-3-cost-of-quality/ ;
       Quality-One, "COQ | Cost of Quality," https://quality-one.com/coq/ ;
       Accounting For Management, "Costs of quality,"
       https://www.accountingformanagement.org/costs-of-quality-or-quality-costs/
       — Standard framework: appraisal (inspection/test/review) is a *legitimate and costed* category
       of quality investment alongside prevention, and both are justified by the failure costs they
       avert. Supports the weaker reading of the presumption — that a downstream check is a
       recognised remedy — but not the stronger reading that it is the *preferred* one; these sources
       consistently state that prevention spend yields larger reductions in total quality cost.
       SNIPPET-ONLY (textbook and practitioner pages).
    6. "SE 350 Software Process & Product Quality — Defect Removal Metrics" and "Defect Prevention and
       Removal." Rochester Institute of Technology course materials,
       https://www.se.rit.edu/~swen-350/slides/DefectRemovalMetrics.pdf ,
       https://www.se.rit.edu/~swen-350/slides/DefectRemoval.pdf [author unverified]
       — Defines Phase Containment Effectiveness and reports defect removal effectiveness for peer
       review techniques ranging from 30% to over 90%, with trained-team inspections starting near
       60% and improving with experience. Establishes that detection remedies have measurable,
       often high, yield. SNIPPET-ONLY.
    7. Kemerer, C. F., and Paulk, M. (attribution from URL/title; year unverified). "The Impact of
       Design and Code Reviews on Software Quality: An Empirical Study Based on PSP Data."
       University of Pittsburgh, https://sites.pitt.edu/~ckemerer/PSP_Data.pdf
       — PSP data showing defect density reduced from a median of 67 to 48 defects/KLOC (factor ~1.4)
       through design and code reviews, i.e. through *reading*, applied systematically. Note this
       supports the presumption's *third*, dismissed alternative as much as its first: structured
       hand-reading is itself a validated instrument. ABSTRACT-ONLY / SNIPPET-ONLY.
    8. Deming, W. E. *Out of the Crisis* (1982), Point 3, as documented by The W. Edwards Deming
       Institute, https://deming.org/explore/fourteen-points/ and
       https://deming.org/quotes/cease-dependence-on-inspection-to-achieve-quality-eliminate-the-need-for-inspection-on-a-mass-basis-by-building-quality-into-the-product-in-the-first-place-3/
       — Included for completeness and honesty: this is the canonical statement *against* the
       presumption ("cease dependence on inspection… build quality into the product in the first
       place"; "you burn the toast, I'll scrape"). No supportive source located rebuts it directly.
       SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: There is a substantial literature establishing that downstream detection is an effective,
    measurable and economically rational remedy for a known defect class. Wagner's quality-economics
    programme treats defect-detection techniques as objects of formal cost optimisation; the empirical
    static-analysis literature reports that automated checking reduces escaped defect density and, in
    at least one 35-project study, total development effort as well; and the defect-removal-metrics
    literature reports removal effectiveness for review and inspection techniques ranging from 30% to
    over 90%. The cost-of-quality PAF model gives appraisal a standing place alongside prevention as a
    justified quality investment. So the presumption's first limb — that building a check is a
    legitimate and probably effective response — is supported. What the literature does *not* support
    is the exclusivity that 14b identified: the same body of work consistently reports that prevention
    spend produces the larger reduction in total quality cost, phase containment (catching defects in
    the phase that introduced them) is the preferred metric, and higher levels of process improvement
    reduce high-severity defect likelihood. Deming's Point 3 is the canonical statement of the rival
    position and no located source rebuts it. On the third alternative — hand-reading as the standing
    instrument — the PSP review data arguably support it rather than the detection remedy.

  Caveats: (1) The strong static-analysis results are conditional on the tool being *built,
    continuously used, and integrated into the toolchain* — precisely the condition that fails in the
    generating case, where four checks have been named across five runs and none built. No located
    source measures the value of an unbuilt check, which is zero. (2) Tool-agreement is low (under
    10% pairwise warning alignment), so a single check covers a narrower slice of a defect class than
    its designers expect; the literature recommends suites, not single checks. (3) Domain transfer is
    real but not verified: every empirical source is about *code*, where defect classes are
    syntactically characterisable. The C2A2 defect class is semantic citation error, where the
    "check" is a resolution or coverage test whose relation to the actual defect is itself in question
    (see PRESUMPTION-877). (4) The support here is for detection as *a* remedy; the literature's
    weight, read plainly, is against detection as *the* remedy, and the presumption as 14b states it
    is the exclusive version. (5) All sources read at snippet or abstract level; no full text
    retrieved.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Supported sub-claims: (i) that automated downstream checks measurably remove defect classes and
    can reduce total effort; (ii) that appraisal is a standing, costed and rational category of
    quality investment; (iii) that defect-detection technique selection is formally optimisable.
    Unsupported sub-claim: that detection is *preferable to* upstream process repair. The located
    literature runs the other way on this, from Deming forward.
    Unaddressed sub-claim: **the delivery risk of a detection remedy — the case where the check is
    correctly identified, repeatedly named, and never built.** I found no literature on the base rate
    or consequences of *named-but-unimplemented* quality checks, i.e. on detection-as-remedy failing
    at the implementation step rather than at the effectiveness step. Given that this is the actual
    observed pattern in the generating case (four checks, five runs, zero built), this looks like a
    genuine gap worth flagging as a possible original contribution.
