SEARCH-FOR-ASSUMPTION-463:
  Date searched: 2026-07-17
  Original item: ASSUMPTION-463
  Original statement: The git-persistence step cannot self-complete from the autonomous sandbox (mount denies .git object writes; no push credentials); per No-Blind-Push, outputs are left "staged for the Mac" — a persistence-layer sibling to the login/quota/connection transmission causes.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-463
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-16 EOD run (durable-write blocked; No-Blind-Push safety rule)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. arc42 Quality Model, "Safety Interlocks." — An interlock defaults to its safe state; if a precondition (here: human review / credentials) cannot be satisfied, the gated operation never proceeds. Confirms No-Blind-Push behaves as a precondition gate on persistence.
    2. Temporal, "Adding Durable Human-in-the-Loop." — Establishes the standard pattern of a durable pending_approval state that survives restarts until human confirmation — the exact capability C2A2's "staged for the Mac" lacks a durable channel for.
    3. MachineLearningMastery, 2026. "Building a Human-in-the-Loop Approval Gate for Autonomous Agents." — Documents queue-then-execute: decoupling checkpoint state from approval state so a blocked write is preserved, not lost.

  Strength of support: Moderate-Strong

  Summary: The literature confirms both halves of the assumption: (a) a safety gate that cannot evaluate its precondition legitimately blocks the operation, and (b) the accepted remedy is a durable, credentialed write/commit queue that holds output until the human step completes. This validates the framing that "staged for the Mac" is a persistence-layer failure of the same family as the transmission outages, and that established durable-execution patterns exist to address it.

  Caveats: Support is for the mechanism and the remedy space; it does not confirm C2A2 has implemented any durable channel. The cited patterns assume a bounded human latency, which the 11-day unattended stretch violates.

  Recommendation: SUPPORTED
