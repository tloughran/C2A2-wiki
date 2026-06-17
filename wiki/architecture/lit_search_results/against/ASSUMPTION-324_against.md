SEARCH-AGAINST-ASSUMPTION-324:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-324
  Original statement: "Yield headline = gross cumulative production (264), reported alongside net on-disk-unique (262); retired/reused ids kept in cumulative."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-324
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the reporting convention (gross headline + net alongside)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Goodhart's law (Goodhart 1975; Jellyfish/EngThrive software-metric gaming literature) — foregrounding the GROSS count as the headline incentivizes id-churn/reuse inflation; a gross headline is the more gameable choice, and "yield" framing invites optimization.
    2. Reused-id ambiguity — keeping reused ids in the cumulative double-counts identity: a reused (tradition, PRS-NN) is one slot, two productions; counting both as "produced" conflates slot-occupancy with creation events and can overstate distinct output.
    3. Headline-choice/framing effects — which of two legitimate numbers is the HEADLINE is itself a value choice; choosing the larger (gross) as the headline is not neutral and can mislead casual readers about the system's "size."

  Strength of challenge: Moderate

  Summary: The dual-reporting itself is sound (15a), but the CHOICE to headline the gross cumulative is challenged: a gross "yield" headline is the most gameable framing (Goodhart), reused ids in the cumulative blur identity vs creation, and headlining the larger number is a non-neutral framing decision. The challenge is not to reporting both numbers but to which is foregrounded and to the unexamined "retired/reused kept in cumulative" rule.

  Specific risks: Gross headline becomes a target -> rewards splitting/churning/id-reuse; readers take the headline as the system's current size; reused-id double counts inflate apparent distinct production.

  Mitigations available: Headline the conservative net census, report gross alongside as a flow; never use gross as a target/optimizer input; show the reused-id count explicitly; label "artifacts produced (incl. retired)" vs "currently on disk." Consistent with prior REVISE-115 (don't let a raw count do silent valuation) and MONITOR-345.

  STEELMAN:
    Strongest counterargument: Gross cumulative production is the honest answer to "how much has this system ever generated," retirees are real work that happened, and reporting net alongside fully discloses the surviving footprint — so the convention hides nothing and the headline choice is a presentation detail, not a measurement error.
    What would need to be true for C2A2 to be safe: The gross headline is never used as a target/optimizer, both numbers are always shown with clear labels, and reused-id semantics are disclosed so "produced" is not silently inflated.
    How to test: Check whether anything optimizes against the headline; audit the reused/retired id set; user-test whether readers interpret the headline as current size.

  Search scope: Goodhart/gaming of gross counts; reused-id identity ambiguity; headline-framing effects; stock-vs-flow labeling. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
