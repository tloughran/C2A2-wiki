SEARCH-FOR-PRESUMPTION-609:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-609
  Original statement: The verifier's self-caught splitter defect is reported as self-checking working, but the stated detection mechanism is "I caught it because my numbers contradicted last night's." Detection required a prior run to differ from. On a first-ever run, on a newly added check, or after any legitimate change in the figures, the identical bug passes silently. The run presumes cross-run comparison is a general correctness check when it is only a change detector — and reports in the same message that the corpus is no longer static, which is the condition that makes a change detector produce legitimate differences and lose its power to flag illegitimate ones.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-609
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the stated detection route in the 2026-07-31 nightly verification report and the absence of any first-run-capable check in the applied remedy
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Barr, Harman, McMinn, Shahbaz & Yoo, 2015. "The Oracle Problem in Software Testing: A Survey." IEEE TSE. — Defines the test oracle problem as distinguishing correct from incorrect behaviour, and classifies "pseudo-oracles" — including comparison against a previous version — as DERIVED oracles whose verdict is relative to the reference, not absolute. This is precisely the item's distinction between a change detector and a correctness check.
    2. Chen, T.Y. et al. "Metamorphic Testing: A Review of Challenges and Opportunities." (HKU TR-2017-04) and Segura et al. — Metamorphic testing exists specifically because a correct reference output is unavailable; a metamorphic relation is checkable on a single execution or a constructed pair, with no prior run required. Supplies exactly the class of check the item says is missing.
    3. Liu, Kuo, Towey & Chen. "How effectively does metamorphic testing alleviate the oracle problem?" IEEE TSE. — Empirical comparison showing MT detects faults that reference-comparison approaches miss, and that MR-based checks are effective where no baseline exists.
    4. Regression-testing definition literature (standard): regression testing establishes that behaviour has not CHANGED relative to a baseline; a fault present in the baseline is, by construction, not a regression. — Supports the item's specific case: the splitter bug would have been invisible had it existed on the first run.
    5. The item's own proposed invariant (frontmatter + body word counts sum to file total) is a textbook conservation-style metamorphic relation; the literature endorses this class as first-run-capable.

  Strength of support: Strong

  Summary: The support here is close to definitional rather than merely analogical. The oracle-problem survey classifies comparison against a prior version as a derived pseudo-oracle whose verdict is relative to a reference, which is exactly the item's claim: it detects difference, and only inherits correctness-detecting power from the assumption that the reference was correct. The metamorphic-testing literature exists because of that limitation and supplies the complement — relations checkable without any prior run. The item's second, sharper claim also has support: as the reference itself becomes legitimately variable (a no-longer-static corpus), the signal-to-noise of a difference-based check degrades, because differences stop being diagnostic. The remedy the item gestures at — a conservation invariant on word counts — is a canonical metamorphic relation, so the fix is not novel and is well-precedented.

  Caveats: (1) The MT literature is largely about deliberately constructed input transformations; the item's invariant is a simpler intra-output consistency check, which is a weaker but still recognised oracle class. (2) None of the sources measures the specific quantity the item asks for — the fraction of a check suite that is first-run-capable — so the literature grounds the classification but cannot supply the count. (3) The item's claim is about a check suite of order-10; the literature's effectiveness comparisons are at much larger scale, so effect sizes do not transfer. (4) Search scope: oracle problem, metamorphic testing, regression semantics. NOT searched: differential/N-version testing, property-based testing (QuickCheck lineage), both of which bear.

  Recommendation: SUPPORTED
