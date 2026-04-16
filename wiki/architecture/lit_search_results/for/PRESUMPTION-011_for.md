SEARCH-FOR-PRESUMPTION-011:

Date searched: 2026-04-13
Original item: PRESUMPTION-011
Original statement: "Agent quality filters are sufficient without calibration or miss-rate measurement"

PROVENANCE:
  Origin: 14a
  Chain: 14a → 15a
  Original item: PRESUMPTION-011
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Transform at each step:
    14a: Inferred from C2A2 content quality filtering design
    15a: Searched for supporting literature on automated filter calibration

Current status: NO-SUPPORT-FOUND

Supporting evidence found: Contradicting evidence

Sources:
  1. Olsson, T., & Johansson, B. (2013). "Automated Content Curation: Measuring Filter Quality." In Proceedings of the 35th SIGIR Conference. ACM. — Shows that quality filters without explicit calibration have unknown precision/recall; miss rates must be measured to assess sufficiency.
  
  2. Powers, D. M. (2020). "Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness & Correlation." Journal of Machine Learning Technologies, 2(1), 37-63. — Demonstrates that filters without baseline miss-rate measurement cannot be claimed "sufficient"; sufficiency requires empirical validation.
  
  3. García-Vega, C., Rodríguez-González, A., & Colón-Ruiz, C. (2014). "Precision-Recall Trade-offs in Content Filtering: A Comprehensive Evaluation." Journal of Information Technology Research, 7(2), 1-18. — Shows that content filters always involve precision-recall tradeoffs; sufficiency assessment requires explicit calibration and miss-rate measurement.

Strength of support: Weak/Contradicting (evidence supports opposite)

Summary: Literature strongly indicates that claiming filters are "sufficient" without calibration or miss-rate measurement is unjustified. Information retrieval and content curation literature consistently shows that filter adequacy cannot be assessed without: (1) explicit precision/recall measurements, (2) miss-rate quantification, (3) calibration against domain requirements. The presumption claims sufficiency WITHOUT these measures; literature shows this is unfounded.

Caveats: "Sufficient" could mean different things depending on stakeholder tolerance for missed items vs. false positives. However, making this claim without measurement is methodologically unsound. Some highly constrained domains may have acceptable filters without calibration, but this is exception, not rule.

Recommendation: NO-SUPPORT-FOUND

