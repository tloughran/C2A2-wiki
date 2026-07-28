SEARCH-AGAINST-PRESUMPTION-557:
  Date searched: 2026-07-28
  Original item: PRESUMPTION-557
  Original statement: [inferred] The review-page defect is treated as local (wrong pid array) when the same generator has failed in three different signatures on three dates; a submission mapping constructed independently of the render pass is a structural defect class, not a bug.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-557
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a three-incident defect history treated as three bugs rather than one class
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Fenton, N. E. & Ohlsson, N. 2000. "Quantitative Analysis of Faults and Failures in a Complex Software System." IEEE Transactions on Software Engineering 26(8): 797-814. — Found strong evidence that a small number of modules contain most pre-release faults and a very small number contain most operational faults, while the large majority of modules contain none. Repeated failures concentrated in one generator module is therefore the statistically EXPECTED distribution, not per se evidence of a distinct structural defect class. Three incidents in one hotspot is the base rate, so it carries much less inferential weight than the presumption assigns it.
    2. Cook, R. I. 1998/2000. "How Complex Systems Fail." (Cognitive Technologies Laboratory, Univ. of Chicago; reprinted in Allspaw & Robbins, eds., Web Operations, O'Reilly 2010.) — Argues post-hoc attribution to a single root cause is "nearly always wrong" because overt failure requires multiple jointly-sufficient faults. This cuts BOTH ways: it undercuts the local "wrong pid array" reading, but equally undercuts the presumption's own move of naming one structural cause ("mapping built independently of render") as THE defect class. Promoting a symptom to a class is the same attributional error at a higher level of abstraction.
    3. Metz, S. 2016. "The Wrong Abstraction." sandimetz.com (widely cited in practitioner literature). — "Duplication is far cheaper than the wrong abstraction." A poorly conceived unification imposes higher maintenance cost than the duplication it removed, and the recovery path is to re-inline. The presumption's implied remedy (unify submit and render onto a single source of truth) is not risk-free; if the abstraction is drawn before the requirement is understood, the generator gets worse, and it is precisely the module already under three-incident stress.
    4. AIHA. 2024. "Hierarchy of Controls" white paper v1 (May 2024) — on classification schemes generally: real cases show "overlaps that blur the separate layers," so bug/class is not a clean dichotomy. Also relevant: standard RCA guidance (e.g., Informa TechTarget, "How to handle root cause analysis of software defects") treats defect classification as a judgement made under cost constraints, not a fact discovered.

  Strength of challenge: Moderate

  Summary: The literature does not defend the "it's just a wrong pid array" reading, but it substantially weakens the inference the presumption draws from three incidents. Fenton & Ohlsson's defect-clustering result means repeated faults in the same module is the expected empirical pattern rather than a signal of a distinct structural class, so the three-incident count is weak evidence. Cook's argument against single-root-cause attribution applies symmetrically: the presumption itself names one structural cause for a multi-incident history, which is the same attributional shortcut relocated upward. Metz's "wrong abstraction" result adds a concrete cost to the implied remedy - collapsing render and submit onto one source of truth before the requirement is settled can be more expensive than the duplication. The honest residue is that "structural defect class" is a plausible hypothesis, not an established classification, and its remedy has a real downside.

  Specific risks: If the presumption is over-read, C2A2 blocks the cheap local fix pending an architectural rework of the generator, extending an outage that is already blocking the review pass; and if the unification is drawn wrongly it creates a harder-to-diagnose coupled defect in the same hotspot module. If the presumption is under-read, the fourth signature appears on the fourth date.

  Mitigations available: Ship the local fix AND record the class hypothesis separately with a falsifiable prediction (a fourth divergent-signature failure in generate_review_page.py). Add a cheap invariant instead of an abstraction: assert at generation time that the submit pid set equals the rendered card id set, which detects the whole class without committing to a refactor. Fenton & Ohlsson's own recommendation - use early fault data to target testing at hotspots - is available without any redesign.

  STEELMAN:
    Item: PRESUMPTION-557
    Strongest counterargument: Defect clustering is one of the best-replicated findings in empirical software engineering, so three faults in one generator is what the base rate predicts and cannot by itself distinguish "one structural class" from "a hotspot with three ordinary bugs." Meanwhile the complex-systems literature says single-cause attribution is nearly always wrong - which indicts the presumption's own single structural cause as much as the local reading it criticises. And the remedy it points at (one source of truth spanning render and submit) is the exact move Metz identifies as more costly than the duplication when made before the requirement is understood. The disciplined response is an invariant check, not a reclassification.
    What would need to be true for C2A2 to be safe: the three incidents share a demonstrated common mechanism (not merely a common file), and the unification is drawn only after the render/submit contract is written down; the local fix is not delayed on the classification question.
    How to test: read the three incident records and check whether all three trace to submit-side state constructed without reference to the rendered set. If yes, class confirmed; if the three mechanisms differ, this is a hotspot, and the prediction is that a fourth failure will again have a new signature.

  Recommendation: PARTIALLY-CHALLENGED
