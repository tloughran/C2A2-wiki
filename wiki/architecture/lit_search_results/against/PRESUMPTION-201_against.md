SEARCH-AGAINST-PRESUMPTION-201:
  Date searched: 2026-05-19
  Original item: PRESUMPTION-201
  Original statement: "morning-briefing-write-as-success vs Tom-action-as-success presumption; briefing-write counter is measured, action-rate is not, gap is invisible. (SELF-MEASUREMENT Goodhart cluster.)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-201
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — implicit success-equals-write
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Goodhart, C. (1975). "Problems of Monetary Management: The U.K. Experience." — Foundational: "When a measure becomes a target, it ceases to be a good measure." Briefing-write becoming the success measure is the textbook setup for Goodhart-style metric collapse.
    2. Strathern, M. (1997). "'Improving ratings': audit in the British University system." European Review. — Reformulation of Goodhart: any institutionalized measure shapes the behavior of the measured, often perversely.
    3. Manheim, D. & Garrabrant, S. (2019). "Categorizing Variants of Goodhart's Law." — Modern taxonomy: SELF-MEASUREMENT cluster (agent measures its own output and optimizes for the measure) is among the most pernicious variants; precisely what is named in the presumption.
    4. Muller, J. Z. (2018). "The Tyranny of Metrics." Princeton. — Documents systematic harm from output-volume metrics decoupled from outcome metrics; "writing briefings = success" is exactly the pattern critiqued.
    5. Hollnagel (2014). "Safety-II in Practice." — Resilience-engineering: process metrics decoupled from outcome metrics produce systems that appear to work while drifting away from purpose.
    6. ITIL v4 Continual Improvement — explicit guidance: output-volume metrics must be paired with outcome metrics; bare output measurement is an antipattern.

  Strength of challenge: Strong

  Summary: The literature on Goodhart's law and metric design is uniformly against the presumption. The agent's own framing ("SELF-MEASUREMENT Goodhart cluster") correctly identifies the failure mode: a metric the measured agent controls (briefing-write) becomes the success criterion, and the actual outcome (Tom-action) is invisible. Manheim/Garrabrant's taxonomy puts this exact variant in the most pernicious category. Muller's "Tyranny of Metrics" is a book-length development of the critique. The presumption is essentially indefensible as a success criterion.

  Specific risks: (a) Briefing-write counter grows; Tom-action-rate may be flat or declining; gap invisible by design. (b) Agents optimize for the measured quantity (write more briefings) rather than the unmeasured outcome (briefings that produce action). (c) Briefing quality may degrade as volume rises; no signal of degradation reaches the agent. (d) Compounds with ASSUMPTION-175 / PRESUMPTION-202: queue depth + briefing volume both rising = "agents are productive" by output measure, "Tom is overwhelmed and acting on less" by outcome measure. (e) Genuine SELF-MEASUREMENT trap: agents grading their own outputs.

  Mitigations available: Track Tom-action-rate explicitly (briefing-to-action conversion); make outcome metric primary, output metric secondary; require briefing-quality audit on a sample; if conversion rate drops, briefing-write is no longer success. The agent should not be the sole judge of its own success.

  Recommendation: CHALLENGED (MEDIUM-HIGH urgency — REVISE)

  STEELMAN:
    Item: PRESUMPTION-201
    Strongest counterargument: This is a textbook Goodhart failure, named as such by the queue item itself. The literature is uniformly against this metric design. Output-volume without outcome-paired metric is the most-critiqued metric pattern in management, Lean, SRE, and resilience-engineering literature. The agent measuring its own outputs without external outcome signal is the failure-mode-by-design.
    What would need to be true for C2A2 to be safe: Tom-action-rate tracked as primary outcome metric; briefing-write demoted to secondary; briefing-to-action conversion ratio reported; if ratio drops, briefing-write counter no longer counted as success; agent does not grade itself.
    How to test: Sample briefings from past 30 days; check what fraction resulted in a Tom action. If <30%, briefing-write is a poor success proxy. Trend over time to detect drift.
