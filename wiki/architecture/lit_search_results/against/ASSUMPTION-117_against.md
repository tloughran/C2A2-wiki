SEARCH-AGAINST-ASSUMPTION-117:
  Date searched: 2026-05-13
  Original item: ASSUMPTION-117
  Original statement: "14a/14b skipped-EOD-slot pattern (5 consecutive misses) satisfies ASSUMPTION-098 three-recurrence threshold for DECISION-NNN canonization — second activation of stated canonization protocol after ASSUMPTION-108"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-117
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-12 EOD 5-consecutive-skip pattern triggering ASSUMPTION-098 governance threshold (second activation)
      15b: Searched for counter-evidence on three-recurrence-rule activation under skipped-rather-than-failed pattern; substrate-decomposition concerns
    Current status: CHALLENGED

  Sources:
    1. Vesely et al. (1981) "Fault Tree Handbook" NUREG-0492 — common-cause failures inflate apparent recurrence counts; 5 consecutive misses with the same underlying scheduler may be a single failure event, not five.
    2. Allspaw & Cook (2000-) — distinguishing absence-of-output (skip) from failure-with-output is canonical in operational reporting; ASSUMPTION-098's recurrence rule is generally framed for failures-with-output, not for skips. Misapplication risk.
    3. Hollnagel (2012) — "drift into failure" — repeated skipped-output without per-task verification is the textbook description of historic-extrapolation pattern, which the same registry has REVISE'd at PRESUMPTION-138 (REVISE 2026-05-11). Authorizing canonization on the recurrence-count of an unverified pattern is structurally inconsistent.
    4. PRESUMPTION-134 (REVISE 2026-05-11, HIGH urgency, unresolved) — substrate-decomposition gate; same caveat that gated ASSUMPTION-108 first activation applies to second activation. The recurrence-counter authorizing canonization is itself unreliable.
    5. C2A2-internal: ASSUMPTION-098 is MONITOR-101, not INCORPORATE; first activation (ASSUMPTION-108) is MONITOR-110 with substrate-decomposition gate; using the same circular-dependency pattern to authorize a second canonization compounds the unvalidated governance risk.

  Strength of challenge: Strong

  Summary: The challenge is strong. The three-recurrence threshold (ASSUMPTION-098) is itself unvalidated (MONITOR-101); using it to authorize canonization is circular. The 5-consecutive-skip pattern may be a single common-cause failure misclassified as five (Vesely fault-tree concern). The skip-vs-failure distinction (Allspaw, Hollnagel) is operationally important and not addressed. Joint with PRESUMPTION-138 (REVISE 2026-05-11) — per-task verification was REVISE'd for the historic-extrapolation pattern; the same pattern operates here. Joint with PRESUMPTION-134 (REVISE 2026-05-11, HIGH) — substrate-decomposition is the load-bearing prerequisite, same as ASSUMPTION-108 first activation.

  Specific risks: (a) Circular dependency on unvalidated ASSUMPTION-098 compounded at second activation; (b) Common-cause failure inflation — 5 skips may be 1 substrate failure; (c) Skip vs. failure distinction unaddressed — the rule may not apply; (d) Joint substrate-decomposition gap (PRESUMPTION-134) underwriting both first and second activations.

  Mitigations available: (a) Block second activation until ASSUMPTION-098 is INCORPORATE (resolves circularity); (b) substrate-decomposition first (resolves common-cause inflation); (c) explicit skip-vs-failure rule clarification; (d) reframe "second activation" as "second pending-activation pending governance-rule validation."

  Recommendation: CHALLENGED (Strong) — circular-dependency on unvalidated rule, unresolved substrate-decomposition gate, and skip-vs-failure ambiguity together challenge the activation

  STEELMAN:
    Item: ASSUMPTION-117
    Strongest counterargument: Using a governance rule that is itself only MONITORed (not INCORPORATEd) to authorize a second canonization compounds the circular dependency that gated the first activation. The 5 consecutive misses may be a common-cause failure misclassified as five independent events (the substrate-decomposition concern PRESUMPTION-134 raised about chat-scrape failures applies just as plausibly to scheduled-task failures — both share the scheduler / login-state substrate). The skip-vs-failure distinction is operationally meaningful: "skipped runs" without per-task verification is the same anti-pattern PRESUMPTION-138 REVISE'd two days ago. The conservative move is to block both first and second activations until ASSUMPTION-098 is itself INCORPORATEd and substrate-decomposition is performed.
    What would need to be true for C2A2 to be safe: (a) ASSUMPTION-098 INCORPORATE; (b) substrate-decomposition completed; (c) skip-vs-failure rule clarified.
    How to test: Audit scheduler logs for whether the 5 skips share a substrate cause; check whether per-task verification was attempted for each skip.
