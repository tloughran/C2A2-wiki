SEARCH-FOR-ASSUMPTION-1153 (OWED LIMB ONLY: formal statistical decision theory — Neyman-Pearson, inspection games, audit sampling; asymmetric loss between detection-direction and correction-direction error):
  Date searched: 2026-10-09
  Original item: ASSUMPTION-1153
  Original statement: Three (four) instruments retracted their own confident, specific findings within one day, and
    one retraction prevented the reversal of correct repairs. The item treats this as an anomaly requiring
    architectural explanation.
  Limbs searched: the formal decision-theory body that both directions reported UNREACHED for two consecutive runs,
    specifically whether it separates the cost of a false detection from the cost of acting on one (the
    correction-direction error). The second MONITOR-542 limb, stating C2A2's own loss function, is not a search and
    was not attempted.
  Cycle: 1 (RE-TRIGGER by 15d 2026-08-30, MONITOR-542; processed 2026-10-09)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: ASSUMPTION-1153
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-08-18 run logs recording four same-day retractions (parser artifact, proximity
        binding, recount bug, clause-short reading) and a fifth near-miss
      15a (cycle 0): reported base-rate material; decision-theory body UNREACHED
      15b (cycle 0): reframed as at/below field FP base rate; decision-theory body UNREACHED and named highest-value
      15c: → MONITOR-542 (High); detection-vs-correction distinction carried into REVISE-363
      15d: re-triggered cycle 1 2026-08-30; did not evaluate evidence
      15a (cycle 1, 2026-10-09): 3 searches, 1 fetch (full text); see below
    Current status: PARTIALLY-SUPPORTED (Moderate-to-Strong for the asymmetric-error structure; None for the
      "anomaly" framing).

  Search scope: 3 web searches: (a) asymmetric loss / Neyman-Pearson / Bayes threshold under unequal error costs;
    (b) inspection games (Avenhaus, von Stengel, Canty) and false-alarm probability; (c) audit sampling, risk of
    incorrect rejection vs incorrect acceptance. Fetch: PCAOB AS 2315 (pcaobus.org), FULL TEXT, read for ¶.12–.13.
    The Avenhaus/von Stengel/Zamir Handbook chapter and Avenhaus & Canty "Compliance Quantified" (1996) were NOT read.
    The Neyman-Pearson primary text was NOT read; the NP characterisation below is textbook background, marked as such.

  Supporting evidence found: Yes (for the existence of a formal asymmetric treatment); Partial overall

  Sources:
    1. PCAOB, AS 2315 "Audit Sampling". [fetched, full text] Verbatim: "The risk of incorrect acceptance and the risk
       of assessing control risk too low relate to the EFFECTIVENESS of an audit in detecting an existing material
       misstatement." And ¶.13: "The risk of incorrect rejection and the risk of assessing control risk too high
       relate to the EFFICIENCY of the audit. For example, if the auditor's evaluation of an audit sample leads him to
       the initial erroneous conclusion that a balance is materially misstated when it is not, the application of
       additional audit procedures ... would ordinarily lead the auditor to the correct conclusion." This is a
       codified asymmetric loss with a stated mechanism. A false detection is cheap ONLY BECAUSE it is routed
       through further verification before any corrective action. It maps directly onto MONITOR-542's distinction.
       The 08-18 retractions were false detections that stayed cheap because "one grep" re-verification happened.
       The near-miss was the case where a false detection would have gone to CORRECTION without that step.
    2. Inspection games: Avenhaus, von Stengel & Zamir (Handbook of Game Theory vol. 3, 2002); Avenhaus & Canty
       (1996); Avenhaus & Krieger; Avenhaus & Okada. [search-result, secondary descriptions] The inspector fixes a
       false-alarm probability α and minimises worst-case non-detection β (Neyman-Pearson structure inside a game).
       The literature explicitly asks whether ignoring false alarms is justified (Avenhaus & Krieger, nuclear interim
       inspections, attribute sampling counted only non-detection). It treats the false-alarm cost as a separate,
       design-relevant term. Supports: the two error directions must be priced separately and chosen, not inherited.
    3. Bayes-threshold derivations under unequal costs: arXiv 2606.01340 (Thm C.1: predict positive when posterior ≥
       C_FP/(C_FP+C_FN)); arXiv 2602.04146 (threshold "encodes the cost asymmetry"); Shewchuk, Berkeley CS189 lecture
       6 notes (asymmetric loss; screening example). [search-result] The textbook point: without stated costs, the
       threshold is arbitrary, so whether a retraction rate is "too high" cannot be judged.
    4. Neyman-Pearson lemma (background knowledge, NOT fetched or verified this run): fix Type I error at α, maximise
       power. The threshold is set by an α budget, not by costs. This is a different route to the same asymmetry.

  Strength of support: Moderate-to-Strong that formal decision theory separates the two error directions and requires
    an explicit loss function. Source 1 (codified, fetched) is the strongest. It adds a mechanism: a false detection
    is cheap when, and only when, a verification step sits between detection and correction.

  Summary: The body unreached for two runs is reached at preliminary depth and is supportive. Audit-sampling standards
    codify the asymmetry: wrongly accepting is an effectiveness failure, while wrongly rejecting is an efficiency cost,
    because further procedures ordinarily catch it before action. Inspection games and Bayes decision theory treat
    false-alarm and miss costs as separate parameters that must be fixed by design. Read with ASSUMPTION-1153, the
    literature supports the part MONITOR-542 says to preserve: the danger lies in the correction direction. It also
    reframes it: four retractions are a normal efficiency cost of a sensitive detector, not an anomaly, PROVIDED a
    verification gate precedes corrective action. The architectural question is therefore whether that gate exists,
    not why the detectors erred.

  Caveats: (i) Inspection-game and Bayes sources are at search-result level. (ii) AS 2315 concerns financial
    statements; its "ordinarily lead to the correct conclusion" assumes a human auditor with further procedures,
    and the transfer to agent pipelines is by analogy. (iii) No support was found for the item's "anomaly" framing;
    the literature points the other way (a base-rate cost). (iv) No source supplies C2A2's actual cost ratio; that
    remains MONITOR-542 limb (a), an in-house obligation.

  Recommendation: PARTIALLY-SUPPORTED. SUPPORTED (Moderate-to-Strong) for the asymmetric-loss structure and the
    detection/correction separation carried into REVISE-363. NO-SUPPORT-FOUND for "anomaly requiring architectural
    explanation" as framed. Suggested hand-off to 15c: the AS 2315 mechanism (verification gate between detection
    and correction) is a concrete shape for REVISE-363.

  NOVELTY-FLAG: No. Item ASSUMPTION-1153. The detection/correction asymmetry is long-established and codified.

  Independence attestation: Read: 15a definition; batch_context.md (queue block, MONITOR-542); for/PRESUMPTION-888_
    retrigger-2026-10-08_for.md (format); assumptions.md statement via grep. NOT read: any against/ file; any 15b
    output dated 2026-10-09.
