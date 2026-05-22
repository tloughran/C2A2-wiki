SEARCH-FOR-PRESUMPTION-166:
  Date searched: 2026-05-14
  Original item: PRESUMPTION-166
  Original statement: "Pathway-doc decisions treated as equal-commitment-weight to formal DECISION-NNN canonizations; 'made' framing despite not-in-decisions.md; extends PRESUMPTION-041 implicit-decision-drift at pathway-doc layer"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-166
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from pathway-doc 'made' framing without formal canonization
      15a: Searched for implicit-decision-drift in software ADR practice
    Current status: SUPPORTED

  Sources:
    1. Nygard (2011) "Documenting Architecture Decisions" — ADRs exist to canonize decisions; informal pathway-doc commitments without ADR have well-documented drift risk.
    2. Fowler (2017) "Sliding scale of architectural decision rigor" — decisions made at different rigor levels acquire different commitment weight; conflating them is a recognized pattern.
    3. C2A2-internal: PRESUMPTION-041 implicit-decision-drift cluster; the pathway-doc layer is the next level out.
    4. Brooks (1995) "The Mythical Man-Month" 20th anniversary — undocumented design decisions accumulate as system entropy.

  Strength of support: Strong

  Summary: Implicit-decision-drift in pathway-docs / informal-design-passes is a recognized risk pattern. The presumption correctly identifies that ASSUMPTION-126/127/128/129 etc. all read as 'made' but are not in decisions.md. Extending PRESUMPTION-041 to the pathway-doc layer is the right structural move. Strong support for the inference.

  Caveats: (a) Pathway-docs may legitimately have lower commitment weight than ADRs (sliding-scale rigor); (b) The remediation is canonization, not pathway-doc removal; (c) Canonization cost is non-trivial — selective canonization may be appropriate.

  Recommendation: SUPPORTED — implicit-decision-drift at pathway-doc layer is a real recurring pattern
