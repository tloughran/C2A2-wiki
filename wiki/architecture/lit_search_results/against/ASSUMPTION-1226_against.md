SEARCH-AGAINST-ASSUMPTION-1226:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1226
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High)
  Original statement: A gate set built on ids, glosses, grades and length signals cannot detect
    argument-layer inversions in doctrinal or technical prose; detection methods for such reversal exist.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1226
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the Summa QC sweep; n=1 generalisation flagged in status.
      15b: Searched for challenging literature
    Current status: CHALLENGED (second limb) / NO-CHALLENGE-FOUND (first limb)

  Search scope: WebSearch, 2026-08-28, one dedicated query on LLM-judge and NLI reliability for
    contradiction and negation. Reached: the Collective Intelligence Project's "LLM Judges Are Unreliable";
    arXiv 2509.25868 (ReFACT confabulation benchmark), 2510.03418 (LegalWiz contradiction detection),
    2512.16041 (assessing LLM-as-a-judge), 2409.11239 (what judges and reward models can and cannot do).
    NOT COVERED: the negation-specific NLI literature (Hossain et al. and successors), which is the exact
    citation for the failure mode and which I reached only through secondary description. All SNIPPET-ONLY.
    Confidence: MODERATE-HIGH.

  Challenging evidence found: Yes — on the remedy, not on the diagnosis

  Sources:
    1. Collective Intelligence Project, "LLM Judges Are Unreliable" [SNIPPET-ONLY]
       https://www.cip.org/blog/llm-judges-are-unreliable — Direct challenge to the assumption's implied
       remedy: LLM judges are widely deployed on the assumption of reliable error detection, and the
       assumption does not hold.
    2. Anon. (2025), "ReFACT: A Benchmark for Scientific Confabulation Detection with Positional Error
       Annotations" (arXiv:2509.25868) [SNIPPET-ONLY; authors unverified] — Reports GPT-4-class accuracy of
       about 0.60 on comparative judgment, and that detection degrades as errors become subtler. An
       argument-layer inversion in doctrinal prose is a subtle error by construction.
    3. Anon. (2025), "LegalWiz: A Multi-Agent Generation Framework for Contradiction Detection in Legal
       Documents" (arXiv:2510.03418) [SNIPPET-ONLY; authors unverified] — States the two-sided failure:
       NLI models lack contextual depth; LLM judges suffer prompt sensitivity, limited evidence
       verification, hallucination and overconfidence. Hybrid confidence-weighted schemes are proposed
       because neither is sufficient alone.
    4. Springer NPL multilingual NLI survey (2024), doi:10.1007/s11063-024-11673-2 [SNIPPET-ONLY] —
       Models generalise poorly off-domain, especially where world knowledge, multi-hop reasoning or
       non-literal meaning are involved, and are sensitive to superficial lexical change. Doctrinal prose is
       all four at once.

  Strength of challenge: Strong on limb 2; None on limb 1

  Summary: The against direction found nothing contesting the assumption's first and load-bearing limb —
    that a structural gate over ids, glosses, grades and length cannot see an argument-layer inversion. No
    source defends structural checking as semantically adequate, and the theorem-proving literature concedes
    it in a domain where the static checker is far stronger. The challenge is entirely to the second limb.
    The detection methods the assumption says exist do exist, and they perform at levels that would not have
    caught the case that prompted the item: roughly 0.60 accuracy on comparative judgment, degrading as the
    error gets subtler, brittle to lexical variation, and worst on exactly the constructions — negation,
    scope reversal, non-literal meaning — that constitute an argument-layer inversion.

  Specific risks: Installing a semantic checker on the strength of "detection methods exist" would replace
    a gate that visibly cannot see the defect with one that invisibly cannot see it, at higher cost and with
    a green light attached. The industrial-verification source names this outcome directly: automated
    checking that does not separate what it can decide from what it cannot "can create false confidence."

  Mitigations available: Scope the semantic check to a screen rather than a gate — route flagged items to
    human adjudication and treat unflagged items as unchecked rather than as passed. Calibrate on a seeded
    set of known inversions before trusting any rate. Keep the structural gate for what it does decide.

  STEELMAN:
    Item: ASSUMPTION-1226
    Strongest counterargument: 0.60 accuracy is being compared against a perfect standard when the operative
      comparison is against the current gate's accuracy on this defect class, which is zero. A screen that
      catches three in five argument inversions is a large improvement over one that catches none, and the
      failure-to-generalise findings concern benchmark transfer, not a checker calibrated on the estate's
      own corpus with its own known-traps record.
    What would need to be true for C2A2 to be safe: the screen's output would have to be treated as a
      partial signal, never as certification, and the false-negative rate would have to be measured on
      seeded inversions rather than assumed.
    How to test: seed twenty known argument-layer inversions into a review batch and measure catch rate for
      the structural gate and for a semantic screen. This also settles the n=1 problem in the original
      observation.

  Recommendation: CHALLENGED (limb 2) / NO-CHALLENGE-FOUND (limb 1)
