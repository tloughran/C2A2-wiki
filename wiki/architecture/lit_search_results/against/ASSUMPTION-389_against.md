SEARCH-AGAINST-ASSUMPTION-389:
  Date searched: 2026-06-30
  Original item: ASSUMPTION-389
  Original statement: "PRS-triplet / cross-program extraction is quality-sensitive and gated to attended sessions by standing policy — the unattended daily orchestrator deliberately defers backlog extraction."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-389
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-29 self-awareness cohort
      15b: Searched for challenging literature (first-time, genuine web search 2026-06-30)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. MindStudio / Beetroot HITL guides — best practice is confidence-threshold ROUTING: most low-risk items proceed automatically, only ambiguous/high-impact items are held for humans. Blanket deferral of the whole backlog is the cruder, costlier form.
    2. Braintrust (2026), "Human-in-the-loop LLM evaluation platforms" — sampling/prioritization rules are preferred over all-or-nothing human gates once volume is high.
    3. Operational evidence (this run's context): the gate has frozen approval axes ~12 days and queued ~68 cards — a concrete throughput/staleness cost of the blanket form.

  Strength of challenge: Moderate

  Summary: The challenge is not to gating per se but to its BLANKET form: literature favors confidence-based selective routing so that low-risk extraction is not held hostage to attendance, whereas C2A2 defers the entire backlog. The 12-day freeze / ~68-card queue is the visible cost.

  Specific risks: Blanket attended-gating converts a quality control into a liveness liability: axes freeze between attended sessions, and the backlog grows unboundedly if attended sessions are sparse.

  STEELMAN: If even a single mis-extracted PRS triplet corrupts the validated-premise lineage downstream, a conservative blanket gate may be rational until a calibrated confidence signal exists — you cannot selectively route on confidence you have not yet measured.

  Recommendation: PARTIALLY-CHALLENGED (Moderate — gating is sound; the blanket (vs selective/confidence-routed) form carries an unmeasured throughput/staleness cost)
