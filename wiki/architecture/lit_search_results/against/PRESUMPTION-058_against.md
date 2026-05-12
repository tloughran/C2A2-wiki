SEARCH-AGAINST-PRESUMPTION-058:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-058
  Original statement: "Splitting the Levin+Friston joint entry without reviewing its original rationale is correct"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-058
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from Levin Agent Template deliverable committing to the split without recording the joint-entry rationale
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Architecture Decision Record (ADR) literature (Nygard 2011 "Documenting Architecture Decisions"; ThoughtWorks Technology Radar 2014-2024): when reversing a prior decision, the ADR best-practice is to record the original decision's rationale, the triggering condition for revisit, and the reasoning for the new direction. Skipping this record creates decision-archaeology loss.
    2. Reversibility / one-way-vs-two-way-doors (Bezos 2016 shareholder letter; Amazon design principles): irreversible decisions deserve deliberate consideration; the Levin-Friston split is reversible but is coupled to the 2026-04-27 caching rollout, which makes coordinated rollback complex.
    3. Coupled-change risk (Fowler 2018 "Refactoring" 2nd ed.; Humble & Farley 2010): shipping two structural changes at once (caching architecture + tradition-entry split) makes attribution of problems impossible. If quality regresses, was it caching or the split?
    4. Cross-tradition signal capture (C2A2 internal: ASSUMPTION-005 PREMISE-001; cross-tradition literature): the Levin+Friston joint entry may have been motivated by their cross-tradition corridor (developmental bioelectricity ↔ free-energy principle). Splitting without auditing that corridor's strength risks losing the signal that motivated the pairing.
    5. Path of least resistance bias (design-process literature; Nygard 2011): architectural reversals that are adjacent to another change frequently happen "because the other change forces it." That bias is worth flagging — the caching architecture makes joint entries awkward, which creates pressure to split without independent justification.

  Strength of challenge: Moderate

  Summary: The split itself is defensible and reversible, but two features of how it is being done are literature-challenged: (a) absence of original-rationale review is an ADR anti-pattern, and (b) coupling the split to the caching rollout makes attribution of post-rollout quality changes impossible. Literature treats both as standard pitfalls. The fix is low-cost: record a brief rationale note before rollout; and either decouple the split from the caching rollout or explicitly acknowledge the coupled-change risk and pre-define what would trigger a rollback.

  Specific risks: (a) Decision-archaeology loss (future revisit has no starting point); (b) coupled-change attribution failure (quality regression could be caching OR split); (c) cross-tradition signal corridor degradation invisible to a same-cycle measurement; (d) the split becomes harder to reverse as downstream tooling and monitoring are built around the separated agents.

  Mitigations available: (a) Record a brief note (even retrospective) of why the joint entry existed and why the split is now preferred; (b) stage the rollout — caching on 2026-04-27, split on (say) 2026-05-11, or vice versa, so attribution is cleaner; (c) instrument cross-tradition-signal generation pre- and post-split to detect any corridor degradation; (d) set a 4-week trigger for reviewing the split's effects independently.

  Recommendation: PARTIALLY-CHALLENGED (split is reasonable but the coupling to caching rollout and the absence of rationale-review are both literature-challenged; fixes are cheap)

  STEELMAN:
    Item: PRESUMPTION-058
    Strongest counterargument: Reversing a prior decision without recording its original rationale is an ADR anti-pattern: it eliminates decision-archaeology, making any future revisit start from zero. Coupling the split to the caching rollout compounds the problem — if post-rollout quality regresses, attribution becomes impossible (was it caching or the split?). The split itself may be correct; the PROCESS around the split is literature-challenged on two axes: skipped rationale-review and coupled-change risk. Fixes are low-cost: a brief rationale note and either staged rollout or pre-defined rollback triggers.
    What would need to be true for C2A2 to be safe: Brief rationale note recorded; rollout staged OR explicit pre-defined rollback triggers; cross-tradition-signal corridor monitored for the first 4 weeks.
    How to test: Track cross-tradition-signal generation rate from Levin and Friston separately over 4 weeks post-split; compare against the prior joint-entry weeks; any corridor atrophy signals the split was net-negative.
