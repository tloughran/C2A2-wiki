SEARCH-FOR-ASSUMPTION-1321 (REMEDY limb only — push vs pull):
  Date searched: 2026-10-06
  Original item: ASSUMPTION-1321
  Original statement: "15b's Critical flag puts the defect further upstream: in all 20 cases the
    *originating* run acted as if the covering premise did not exist — premise propagation, not routing."
  Limb searched: B (REMEDY) — whether normative knowledge should be PUSHED to the point of work rather
    than left to be PULLED from the register (MONITOR-606 (c)). Limbs A and C are at REVISE-459.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-20; processed 2026-10-06)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: ASSUMPTION-1321
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from run report — originating runs acted as if covering premises did not exist
      15a (cycle 0): Kawamoto et al. 2005 verified via CRD/DARE critical abstract (NBK71623) only
      15c: DISPOSITION-948 — remedy limb held at MONITOR-606
      15d: re-triggered cycle 1; owed = one full-text fetch of Kawamoto 2005
      15a (cycle 1, 2026-10-06): full text of Kawamoto 2005 FETCHED from bmj.com and read in the
        Results (univariate + meta-regression), Discussion and Implications sections
    Current status: SUPPORTED

  Search scope: 1 web search (locate full text), 1 fetch (bmj.com/content/330/7494/765 — full text
    retrieved; tables 5–7 are pop-ups and their cell values were NOT in the fetched text).

  Supporting evidence found: Yes

  Sources:
    1. Kawamoto, K., Houlihan, C. A., Balas, E. A., Lobach, D. F., 2005. "Improving clinical practice
       using clinical decision support systems: a systematic review of trials to identify features
       critical to success." BMJ 330:765. [fetched — full text] — Statements confirmed at source:
       - Univariate: "75% of interventions succeeded when the decision support was provided to
         clinicians automatically, whereas none succeeded when clinicians were required to seek out the
         advice of the decision support system (rate difference 75% (37% to 84%))." This is the most
         direct push-vs-pull datum in the paper.
       - Univariate: delivery at the time and location of decision making "fell just short of being
         significant at the 0.05 level (rate difference 48% (−0.46% to 70.01%))."
       - Meta-regression (71 comparisons): four independent predictors — automatic provision as part of
         clinician workflow (P < 0.00001), time and location of decision making (P = 0.0263),
         recommendation rather than assessment (P = 0.0187), computer-generated (P = 0.0294).
       - "Among the 32 clinical decision support systems incorporating all four features ... 30 (94%
         (80% to 99%)) significantly improved clinical practice"; systems lacking any of the four:
         18/39 (46% (30% to 62%)).
       - Implications: "If a clinical decision support system must depend on clinician initiative for
         use, we recommend that system use be carefully monitored"; unifying principle: an effective
         system "must minimise the effort required by clinicians to receive and act on system
         recommendations."
       Odds ratios: the table cell values were not visible in the fetched text; no odds ratio is quoted
       here. Per MONITOR-606, the 112.1 workflow-feature figure is NOT quoted.

  Strength of support: Moderate

  Summary: The primary text confirms the four-feature finding as stated through the critical abstract
    and adds the sharper push/pull contrast: 0% success where clinicians had to seek the advice out
    themselves, against 75% where it arrived automatically. The authors' own design inference — minimise
    the effort to receive and act on advice; monitor use if it depends on user initiative — is the PUSH
    remedy in clinical terms. MONITOR-606 item (c) is satisfied: the finding and its conditions are now
    confirmed at source.

  Caveats (several stated by the authors themselves): binary success outcome, not effect size;
    "suboptimal" cases-to-variables ratio and possible over-fitting acknowledged; publication bias
    acknowledged; RCTs to 2003, human clinicians. The time/location feature is NOT significant
    univariately (CI crosses zero) and only reaches P = 0.0263 in the multivariate model. Nothing here
    addresses alert precision — PREMISE-121/173's ordering (measure precision before building a push
    channel) is untouched by this source. Transfer to LLM agents reading premises is assumed.

  Recommendation: SUPPORTED (moderate) for the remedy direction in principle; precision-first constraint
    stands.
