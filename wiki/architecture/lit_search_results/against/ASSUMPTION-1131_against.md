SEARCH-AGAINST-ASSUMPTION-1131:
  Date searched: 2026-08-18
  Original item: ASSUMPTION-1131
  Original statement: Four ids were cited for claims their own bodies argue against, and every one passed an existence check and a label check — "every such anchor would have looked correct at the Label." (Escalation: the read-the-body rule.)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1131
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Collected four same-day polarity failures from four independent runs and extracted the stated escalation of the read-the-body rule.
      15b: Searched for challenging literature; found that automated and human polarity/stance judgement of a citation is itself unreliable and ill-posed, so "read the body" is not the clean remedy the escalation implies, and that a four-case same-day cluster is weak evidence for a systemic Label-layer defect given the very low base rate of contradicting citations.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Bakker, C., Theis-Mahon, N., Brown, S., 2023. "Evaluating the Accuracy of scite, a Smart Citation Index." Hypothesis: Research Journal for Health Information Professionals. — Independent evaluation of the leading production polarity classifier: of 98 classified citations scite labelled 2 supporting and 96 mentioning, where the human raters found 42 supporting, 39 mentioning and 17 contrasting; F-measures ranged 0.0–0.58. Contradicting citations were essentially never recovered. This challenges the implicit premise that a body-reading stage (automated or tool-assisted) reliably recovers polarity where the Label did not.
    2. Nicholson, J.M. et al., 2021. "scite: A smart citation index that displays the context of citations and classifies their intent using deep learning." Quantitative Science Studies 2(3):882–898. — Reports vendor-side precision of 0.80/0.85/0.97 for supporting/contradicting/mentioning over 800M+ classified citation statements; disputing citations are ~0.3–0.8% of the corpus. Even the optimistic figures leave a large residual error rate, and the extreme class imbalance means a handful of missed contradictions is the expected operating point, not a signal of a new defect.
    3. Catalini, C., Lacetera, N., Oettl, A., 2015. "The incidence and role of negative citations in science." PNAS 112(45):13823–13826. — Negative citations were 2.40% of citations in a 15,000-citation immunology training set that required PhD immunologists to annotate. The base rate is low and the judgement is expert-dependent; four same-day instances is consistent with the ambient rate rather than with a step-change in system behaviour.
    4. Lauscher, A. et al., 2022. "MultiCite: Modeling realistic citations requires moving beyond the single-sentence single-label setting." NAACL. — Establishes that a single citation frequently has multiple functions spread across multiple sentences. This undercuts the framing in which an anchor has one polarity that the body would have revealed: for many citations there is no single correct answer for a checker to have found.
    5. Greenberg, S.A., 2009. "How citation distortions create unfounded authority: analysis of a citation network." BMJ 339:b2680. — In a 242-paper, 675-citation network, unfounded authority arose through citation bias against refuting papers, amplification by papers presenting no data, and conversion of hypothesis into fact by citation alone — all produced by humans with full access to the bodies. Reading the body is not sufficient protection against exactly the failure mode described.
    6. Reported inter-annotator agreement for stance polarity and stance intensity of ~62% and ~54% weighted kappa, with multiple argument-mining papers noting that relation identification is hard for humans outside full-debate context. [Specific paper attribution not confirmed in this session — figure surfaced in a survey summary; treat as indicative, not citable.] — If humans agree at kappa ≈ 0.6 on stance, "the body argues against it" is not a crisp ground truth against which anchors can be adjudicated.

  Strength of challenge: Moderate

  Summary: The literature does not contradict the core observation — label-level metadata genuinely does not encode polarity, and the four anchors would indeed have looked correct at the Label. What it challenges is the inference structure around it. First, the escalation ("read the body") is presented as the fix, but the best-performing production system for exactly this task recovers 0 of 17 contrasting citations in independent evaluation, and human annotators agree on stance only moderately. Second, MultiCite shows that citation polarity is often not single-valued, so some anchors will have no determinate polarity for any checker to find. Third, the base rate of contradicting citations (2.4% in PNAS, 0.3–0.8% in scite's corpus) means a four-case same-day cluster is within the expected ambient rate; the claim that this is a Label-layer defect is under-identified relative to the alternative that it is the normal error rate becoming visible because someone looked.

  Specific risks:
    - Over-confidence in the remedy: adopting "read the body" as the escalation may create the impression that polarity failures are now closed, when the measured recall of contradiction detection is near zero in the one published independent evaluation.
    - Ill-posedness: for multi-function citations there is no single correct polarity; a rule demanding one will generate confident-but-arbitrary verdicts.
    - Cost blindness: full-body polarity adjudication requires domain-expert reading (Catalini et al. used PhD immunologists); an automated proxy will not have that fidelity.
    - Sampling inference: four cases from four runs does not distinguish "new failure mode" from "ambient 2% rate finally sampled."

  Mitigations available:
    - Record a confidence/abstain state for polarity rather than a binary verdict; treat "indeterminate" as a first-class outcome (this also addresses PRESUMPTION-831).
    - Adjudicate polarity per anchored sentence, not per identifier, following the MultiCite multi-sentence/multi-label finding.
    - Establish a denominator: measure how many anchors were checked, so a four-case cluster can be compared against a rate rather than treated as an event.
    - Prefer targeted verification of high-load anchors (those doing argumentative work) over uniform body-reading, since Greenberg shows the damage concentrates in amplified, load-bearing claims.

  Search scope: Citation function/intent classification (SciCite, ACL-ARC, MultiCite), citation polarity and sentiment in scientific text, production smart-citation indices and their independent evaluations, scientometrics of negative citations, citation distortion and citation bias, stance detection and argumentation-mining annotation reliability. Searched 2026-08-18. Not covered: proprietary/unpublished classifier benchmarks; non-English citation corpora.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-1131
    Strongest counterargument: The observation that the Label carries no polarity information is not in dispute anywhere in the literature — CiTO's existence, scite's whole business model, and the Catalini et al. annotation effort all presuppose it. The four failures are therefore correctly diagnosed at the layer where they occurred. Where the item overreaches is in the implied sufficiency of the escalation and in treating four instances as evidence of a change in kind. The literature says the failure is structural and permanent, not episodic: contradicting citations are rare, hard to detect, hard to agree on, and often not single-valued, which means the honest posture is a known residual error rate with abstention, not a new rule that closes the gap.
    What would need to be true for C2A2 to be safe: (a) body-reading must be performed by a reader with enough domain competence to recognise hedged disagreement, since that is what Catalini et al. required; (b) the system must tolerate an "indeterminate polarity" outcome rather than forcing support/undercut; (c) the escalation must be applied to load-bearing anchors specifically, because uniform application at scale will regress toward the ~0.0–0.58 F-measure regime; (d) the residual error rate must be published alongside outputs rather than treated as eliminated.
    How to test: Construct a held-out set of anchors with known polarity (e.g. sample from scite's disputing set plus a matched mentioning/supporting set), run the read-the-body rule blind, and report recall on the contradicting class specifically — not overall accuracy, which the class imbalance will flatter. Independently, have two readers adjudicate the same 50 anchors and compute kappa; if agreement lands near the ~0.5–0.6 stance-detection band, the rule cannot support a binary verdict and must emit abstentions.
