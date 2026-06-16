SEARCH-FOR-PRESUMPTION-344:
  Date searched: 2026-06-12
  Original item: PRESUMPTION-344
  Original statement: "Queue emptiness is pipeline health (the health indicator did not migrate with the constraint to the 57-item review stage)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-344
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from 2026-06-11 EOD session
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Businessmap / Lean Kanban literature. "How to Track Kanban Queue Length." businessmap.io. — In Lean/Kanban systems, queue length is an established flow health metric: shorter queues correlate with shorter cycle time and lower WIP accumulation. Aging WIP and queue length make visible the economic cost of items waiting, and tracking queue length enables early detection of forming bottlenecks before they manifest in late delivery.

    2. Goldratt & Cox, 1984. "The Goal." North River Press. / Theory of Constraints Institute, tocinstitute.org. — Goldratt's Theory of Constraints (TOC) establishes that optimising local metrics (clearing one queue) without tracking the system-level constraint migrates the bottleneck rather than eliminating it. Once a constraint is elevated, a new constraint emerges elsewhere. This directly predicts the pattern described: queue emptiness at one stage is not global health if the constraint has shifted downstream (to the 57-item review stage).

    3. Planview, "Lean Metrics to Improve Flow." planview.com. — Flow metrics literature identifies that cumulative flow diagrams (CFDs) and cycle time scatterplots are superior pipeline health indicators to simple queue counts at a single stage, precisely because they capture system-wide flow rather than local queue state. A health dashboard anchored to a single stage's queue count is structurally liable to mask constraint migration.

  Strength of support: Moderate

  Summary: The Lean and TOC literature provides strong support for the first part of the claim — that queue length is a legitimate health indicator — and simultaneously provides a principled explanation of why the specific failure described occurred. TOC explicitly predicts that local queue clearance without system-level monitoring will migrate the constraint invisibly. The claim as stated conflates two distinct propositions: (a) queue emptiness is a valid health signal (supported), and (b) the health indicator did not migrate with the constraint (this is the failure being diagnosed, not a presumption that was valid). The literature supports treating this as a design flaw in the health-monitoring approach rather than a presumption to validate.

  Caveats: The C2A2 pipeline is not a manufacturing or software delivery system; the direct application of Lean/TOC metrics requires domain-transfer. However, the structural logic (local queue ≠ system health when constraints shift) applies to any multi-stage processing system. The claim is better read as a diagnostic finding than a generalised presumption: the system presumed queue emptiness = health, and the literature explains why that presumption is structurally flawed.

  Search scope: Searched for: (1) queue length as health indicator in Lean/Kanban, (2) flow metrics and pipeline health, (3) Theory of Constraints and constraint migration/bottleneck shift, (4) cumulative flow diagrams as system health indicators. Preliminary — literature on multi-stage AI pipeline monitoring would be more directly applicable.

  Recommendation: PARTIALLY-SUPPORTED
