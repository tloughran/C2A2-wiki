SEARCH-AGAINST-PRESUMPTION-724:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-724
  Original statement: That when a watchdog and a task disagree, one is wrong; today both were right and the joint reading lived in a clause no watchdog can read.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-724
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred by constructing the joint reading the system could not, from three same-day summaries
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. SQLI, "Blind Spots: Invisible Risks in Complex System Landscapes" (2025) — siloed monitoring tools covering only part of a system, plus poor cross-tool integration, produce blind spots that are structural, not incidental; disagreement between tools does not imply one tool is defective.
    2. Baeldung, "Observability in Distributed Systems" — draws the standard distinction that monitoring watches a predefined set of metrics (a known failure taxonomy) while observability answers arbitrary questions about internal state; a watchdog is monitoring, so by construction it cannot represent states outside its predefined metric set — including a state that is jointly true across watchdog and task but expressible in neither alone.
    3. bluepes.com, "Distributed system monitoring: detect and prevent failures" — notes that transactions failing at intermediate stages "leave their fingerprints on limited data paths," so two instruments sampling different data paths of the same event can each be locally accurate yet jointly incomplete.

  Strength of challenge: Moderate

  Summary: General SRE/observability literature supports the more general claim underlying this presumption: contradictory signals from independent monitors frequently indicate the monitors are sampling different measurands of the same event, not that one is in error. This is the standard "monitoring sees only its predefined slice; observability requires synthesis across slices" argument, and it directly undercuts a design that treats watchdog/task disagreement as a binary correctness question. No C2A2-specific literature exists (expected, since this is a bespoke system), so the challenge is by analogy from distributed-systems monitoring theory.

  Specific risks: If the system's escalation/triage logic assumes disagreement implies an error to isolate, it will systematically misdiagnose true joint states (both signals correct, describing different aspects) as false alarms or false confidence, discarding the very information needed to reconstruct the joint reading — exactly the failure the item describes.

  Mitigations available: Add a reconciliation layer that treats watchdog and task output as complementary partial observations rather than competing verdicts; explicitly model "differing measurand" as a third outcome alongside "watchdog wrong" / "task wrong."

  STEELMAN:
    Item: PRESUMPTION-724
    Strongest counterargument: Monitoring instruments are, by design, narrow — a watchdog is built to answer a fixed, small set of questions, and a task's self-report answers a different fixed set. Standard observability theory predicts that when two narrow instruments disagree, the disagreement itself is data about a state that spans both instruments' blind spots, not evidence that one instrument malfunctioned. Treating disagreement as "someone is wrong" discards this information by construction, because no single instrument — including a hypothetical smarter watchdog — can express a joint state that only exists in the gap between two measurands.
    What would need to be true for C2A2 to be safe: Either watchdog and task would need to share a common, sufficiently expressive state model (so disagreement genuinely does imply error), or the system would need an explicit reconciliation step that constructs joint readings rather than adjudicating a winner.
    How to test: Retrospectively audit past watchdog/task disagreements to see what fraction resolve to "one was simply wrong" vs. "both correct, different measurand" — the ratio determines how costly this presumption is in practice.
