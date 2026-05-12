SEARCH-AGAINST-PRESUMPTION-103:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-103
  Original statement: "Specialist outputs labeled by weekday-of-assignment; convention unstated"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-103
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as labeling-convention presumption
      15b: Searched for challenging literature on label-mismatch errors in downstream consumers
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Workflow-orchestration literature (Airflow docs) — logical-date vs. execution-date confusion is the most-frequently-cited Airflow gotcha; documented user-error source.
    2. Distributed-systems literature (Kleppmann 2017) — implicit conventions drift; explicit-naming is canonical recommendation.
    3. C2A2-internal: 2026-05-05 catch-up labeled outputs by weekday-of-assignment; downstream consumers reading these as weekday-of-execution would error.
    4. Documentation literature (Procida 2017 "Diátaxis") — implicit conventions are routinely cited as documentation gaps.

  Strength of challenge: Moderate

  Summary: The convention itself is canonical (Airflow logical-date), but unstated conventions drift and produce label-mismatch errors. Literature consistently recommends explicit naming. PRESUMPTION-103 surfaces a real but low-architectural-consequence gap; the convention is supported but the unstatedness is not.

  Specific risks: (a) Downstream consumers misread weekday-of-assignment as weekday-of-execution; (b) implicit-convention drift accumulates; (c) low-cost gap that is easy to remediate.

  Mitigations available: (a) Document the convention explicitly; (b) annotate output files with execution-time alongside assignment-time; (c) low-cost ticket.

  Recommendation: PARTIALLY-CHALLENGED (Moderate) — convention canonical; unstatedness is the real gap; low-cost remediation

  STEELMAN:
    Item: PRESUMPTION-103
    Strongest counterargument: Airflow's most-cited gotcha is exactly this: logical-date vs. execution-date confusion. The convention itself is standard, but unstated conventions are documentation debt — every new downstream consumer pays the cost of figuring it out. The remediation is a single line of documentation; the cost of leaving the convention unstated grows monotonically with downstream consumer count.
    What would need to be true for C2A2 to be safe: (a) Convention documented in a single visible location; (b) annotation on output files distinguishing assignment-time from execution-time.
    How to test: Ask a downstream agent (or future Tom) to interpret a weekday label; if they assume execution-time when assignment-time is intended, the gap is confirmed.
