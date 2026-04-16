SEARCH-AGAINST-PRESUMPTION-022:
  Date searched: 2026-04-14
  Original item: PRESUMPTION-022
  Original statement: "REVISE backlog is bounded and manageable; review rate can match generation rate"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-022
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from growing REVISE backlog 2026-04-14
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Technical debt literature — Once deprioritization begins, items accumulate; backlogs grow exponentially without deliberate management.
    2. Operations research — When generation rate exceeds review rate, queue grows without bound. Recommended: 15% capacity dedicated to backlog.
    3. QA scalability research — Pure human review cannot match accelerating generation; automation or throttling required.
    4. Software engineering debt studies — Old backlogs become "zombie debt" eventually discarded; items lose credibility over time.

  Strength of challenge: Strong

  Summary: The presumption contradicts operations research findings. Technical debt backlogs are notoriously unbounded once deprioritized. If generation > review rate, backlog grows without bound. Literature recommends dedicating 15% of capacity to backlog management. Moreover, correlated findings sharing common assumptions (e.g., all resting on FINDING-011) create batch processing risk.

  Specific risks: Generation may accelerate backlog faster than review capacity. REVISE items lose credibility over time. If FINDING-011 is flawed and multiple items depend on it, batch invalidation occurs.

  Mitigations available: Set hard cap on backlog size. Automatic halt to generation if backlog exceeds cap. Dedicate 15% of capacity to backlog.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Backlogs CAN be bounded if deliberately designed to be bounded. Set hard limits on generation rate based on observed review capacity. Some high-performing teams maintain discipline by treating backlog size as a constraint, not a symptom.
    What would need to be true for C2A2 to be safe: Explicit cap on REVISE backlog (e.g., max 25 items). Automatic halt if exceeded. Generation rate matched to review capacity.
    How to test: Track queue growth rate vs. review rate over 2-3 cycles; if monotonically growing, redesign needed.
