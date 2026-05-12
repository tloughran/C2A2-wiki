SEARCH-AGAINST-PRESUMPTION-101:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-101
  Original statement: "Filter-semantics popover ≡ implementation without automated test"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-101
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as doc-implementation equivalence claim without test
      15b: Searched for challenging literature on doc drift after refactoring
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Software-engineering literature (Parnas 1972; Knuth 1984) — doc-code equivalence-by-default is documented anti-pattern.
    2. Documentation literature (Procida 2017 "Diátaxis") — popover/tooltip text is highest-drift documentation surface; tests are the canonical mitigation.
    3. Refactoring literature (Fowler 1999) — refactoring without doc-update is canonical drift source; popovers especially.
    4. C2A2-internal: validate_html.py covers HTML structural validation but not popover-content; the test gap is concrete.
    5. Test-driven-development literature (Beck 2002) — equivalence claims without tests are documented anti-pattern.

  Strength of challenge: Strong

  Summary: Literature is unambiguous: doc-implementation equivalence-by-default is anti-pattern, popover text is highest-drift surface, automated tests are the canonical mitigation. PRESUMPTION-101 operates without the canonical mitigation. Challenge is strong because the literature direction is unanimous and the remediation is low-cost.

  Specific risks: (a) Popover content drifts from implementation silently; (b) users misinterpret filter semantics based on stale popover; (c) compounds ASSUMPTION-083's user-error risk.

  Mitigations available: (a) Snapshot test on popover content; (b) integration test on filter semantics; (c) low-cost remediation given existing validate_html.py infrastructure.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE (low-cost; likely small ticket)

  STEELMAN:
    Item: PRESUMPTION-101
    Strongest counterargument: Popover text is the highest-drift documentation surface in any UI system. Refactoring filter logic without updating the popover is the most common drift source in HCI engineering, and the canonical mitigation — a snapshot or integration test — is low-cost given that validate_html.py already exists. The presumption is "doc equals implementation"; without a test, that equivalence is unverified at any moment.
    What would need to be true for C2A2 to be safe: (a) Snapshot test on popover content; (b) integration test on filter semantics; (c) inclusion in the validate_html.py pipeline.
    How to test: Add a snapshot test now; compare against implementation; if any divergence, drift is already present.
