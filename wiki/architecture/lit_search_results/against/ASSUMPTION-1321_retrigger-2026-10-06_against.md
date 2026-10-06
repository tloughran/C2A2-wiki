SEARCH-AGAINST-ASSUMPTION-1321 (RE-TRIGGER cycle 1, REMEDY limb — push vs pull — only):
  Date searched: 2026-10-06
  Original item: ASSUMPTION-1321
  Original statement: "in all 20 cases the *originating* run acted as if the covering premise did not exist —
    premise propagation, not routing." Held at MONITOR-606: whether the remedy is PUSH (deliver the covering
    premise to the point of work) or PULL (register consulted).

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. Note: my fetch of bmj.com/content/330/7494/765 was refused
    by the session tool as "already fetched in this session" by another caller; I did not see that content.
    Self-reference disclosure carried forward: the item restates 15b's own 2026-09-11 flag.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: ASSUMPTION-1321
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 15b's 2026-09-11 Critical systemic-risk flag.
      15b (2026-09-12): Searched against; override bands, tacit-knowledge objection.
      15c: DISPOSITION-948; remedy limb held as MONITOR-606.
      15d (2026-09-20): Re-triggered; owed = Kawamoto 2005 full text.
      15b (re-trigger cycle 1): Attempted Kawamoto full text (FAILED — see below); retrieved the PRIMARY
        abstract (upgrade from the CRD/DARE critical abstract) and the abstracts of the two later syntheses.
        One of the two later syntheses cuts against push; the other SUPPORTS it on adherence. Both reported.
    Current status: PARTIALLY-CHALLENGED

  Retrieval record for the owed item: Kawamoto full text NOT retrieved. bmj.com fetch suppressed (above);
    Europe PMC full-text XML for PMC555881 returned HTTP 500; PMC blocked by reCAPTCHA (not bypassed). The
    PubMed/Europe PMC primary ABSTRACT was retrieved [fetched]: 70 RCTs to 2003; CDSS improved practice in
    68%; four independent predictors — automatic provision as part of clinician workflow (P < 0.00001),
    recommendations not just assessments, support at time and location of decision, computer-based; 30 of 32
    (94%) four-feature systems improved practice. No odds ratios are quoted here (per instruction: the 112.1
    workflow figure is excluded; I also do not re-quote 15.4, which I have not read at source).

  Challenging evidence found: Partial

  Sources:
    1. Roshanov, P.S., Fernandes, N., Wilczynski, J.M., et al., Haynes, R.B. 2013. "Features of effective
       computerised clinical decision support systems: meta-regression of 162 randomised trials." BMJ
       346:f657. [fetched — abstract via Europe PMC API] Systems presenting advice INSIDE electronic charting
       or order-entry interfaces were LESS likely to be effective (OR 0.37, 95% CI 0.17–0.80); developer-
       evaluated systems more likely to show benefit (OR 4.35, 1.66–11.44); requiring a reason to override
       advice associated with success (OR 11.23, 1.98–63.72). [background-knowledge, NOT verified at source:
       Roshanov et al. also tested Kawamoto's automatic-provision feature and did not find it significant —
       the abstract does not state this; treat as unverified.]
    2. Van de Velde, S., Heselmans, A., Delvaux, N., ... Roshanov, P., ... Flottorp, S. 2018. "A systematic
       review of trials evaluating success factors of interventions with computerised clinical decision
       support." Implementation Science 13:114. [fetched — abstract via Europe PMC API] 66 head-to-head
       trials. **Automatic vs on-demand CDS "led to large improvements in adherence" — this SUPPORTS push and
       is reported against my own brief's hypothesis.** BUT: "The CDS intervention factors made little or no
       difference to patient outcomes"; requiring users to respond made little or no difference; certainty
       low to moderate for all factors.
    3. Kawamoto, K., Houlihan, C.A., Balas, E.A. & Lobach, D.F. 2005. BMJ 330:765. [fetched — primary
       abstract only] As above. Trials to 2003; evaluator independence not reported in the abstract.

  Strength of challenge: Moderate

  Summary: The literature did not "fail to replicate" push cleanly. The head-to-head evidence (Van de Velde)
    favours automatic over on-demand delivery for ADHERENCE — the best evidence FOR push found this cycle.
    The challenge is in three boundary conditions: (i) the larger meta-regression (Roshanov, 162 RCTs) found
    advice embedded in the working interface associated with FAILURE (OR 0.37), i.e. the most literal form of
    "deliver to the point of work" did worse than other delivery routes; (ii) the head-to-head review found
    delivery factors moved process adherence but not outcomes, so push may raise premise-citation without
    raising correct application; (iii) developer-evaluated trials overstate benefit ~4-fold in odds, and the
    2003-era evidence base behind Kawamoto is dominated by developer evaluations [background-knowledge]. The
    one consistent success factor across both later syntheses is a forcing step (reason-for-override), which
    is a different remedy from push. Note conflict: Van de Velde finds "requiring a response" made little or
    no difference, Roshanov finds reason-for-override strongly associated — unresolved.

  Specific risks: A push channel embedded in the agent's working prompt is the C2A2 analogue of in-EHR
    advice — the delivery mode Roshanov associates with failure; it may raise compliance tokens (premise
    cited) without improving the decision, and in-house evaluation by the builder will overstate it.

  Mitigations available: MONITOR-606 (b) precision measurement first; evaluate any push channel by an agent
    other than its builder; measure correct-application outcome, not citation adherence; trial a
    reason-for-override step as the competing remedy.

  Recommendation: PARTIALLY-CHALLENGED. Kawamoto full text still owed (third route: institutional access).

STEELMAN:
  Item: ASSUMPTION-1321 (remedy limb)
  Strongest counterargument: Twenty years after Kawamoto, the largest meta-regression found that putting
    advice directly into the interface where work happens is associated with lower odds of success, that
    builders' own evaluations inflate effects, and the head-to-head review found that delivery tweaks change
    what clinicians click, not what happens to patients. A push channel for premises is the same design;
    the likely result is agents that cite the covering premise more and apply it no better — a compliance
    artefact that reads as a fix.
  What would need to be true for C2A2 to be safe: push is high-precision (few irrelevant premises per point
    of work) and success is measured as correct application, judged by a non-builder.
  How to test: A/B the 20-case scenario with push vs. reason-for-override vs. control; score correct
    application blind to arm.
