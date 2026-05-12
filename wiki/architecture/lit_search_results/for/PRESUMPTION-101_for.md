SEARCH-FOR-PRESUMPTION-101:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-101
  Original statement: "Filter-semantics popover ≡ implementation without automated test"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-101
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the doc-implementation equivalence claim embedded in ASSUMPTION-083 without automated test
      15a: Searched for supporting literature on doc-code synchronization patterns
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Software-engineering literature (Parnas 1972; Knuth 1984 "Literate Programming") — doc-code synchronization is the canonical concern; equivalence-by-default is explicitly warned against.
    2. Documentation literature (Procida 2017 "Diátaxis"; Spencer 2014) — popover/tooltip text is the most-prone-to-drift documentation surface; literature recommends test-coverage, not equivalence-by-default.
    3. Test-driven-development literature (Beck 2002; Martin 2008) — equivalence claims without tests are documented anti-patterns; the "trust the docs" default is consistently warned against.
    4. C2A2-internal: validate_html.py exists for HTML structural validation but does not currently cover filter-semantics popover content.

  Strength of support: None

  Summary: Literature does not support equivalence-by-default between documentation and implementation. Popover/tooltip text is identified as the highest-drift documentation surface; automated tests are the canonical mitigation. PRESUMPTION-101 is operating without the canonical mitigation; the equivalence claim is empirically unverified.

  Caveats: (a) The claim may be empirically true at the moment, but the absence of test means future drift is invisible; (b) PRESUMPTION-status + NO-SUPPORT is a strong signal; (c) the gap is small and remediable — adding a popover-content snapshot test is low-cost.

  Recommendation: NO-SUPPORT-FOUND (literature is unambiguous; doc-implementation equivalence-by-default is documented anti-pattern)
