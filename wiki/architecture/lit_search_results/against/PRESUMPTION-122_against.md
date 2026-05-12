SEARCH-AGAINST-PRESUMPTION-122:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-122
  Original statement: "Documentation-for-Tom presumed to count as 'fix' for recurring scheduled-task pre-condition without programmatic enforcement"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-122
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD documentation-as-fix observation
      15b: Searched for counter-evidence on documentation-only remediation success rates
    Current status: CHALLENGED

  Sources:
    1. SRE / DevOps literature (Beyer 2016; Kim 2016) — documentation-only remediation has documented low success rates for recurring preconditions; toil reduction (programmatic enforcement) is canonical.
    2. Human-factors literature (Reason 1990 "Human Error") — relying on human-recall for documented preconditions is canonical recipe for recurrence.
    3. Adler & Borys (1996) "Two Types of Bureaucracy" — documentation without enforcement defaults to non-adoption under workload pressure.
    4. PRESUMPTION-108 / PRESUMPTION-111 cluster — recurring same-mode failures; documentation-only response has been the failure mode.
    5. C2A2-internal: cowork-to-chat sync, chat-scrape, Chrome MCP environment recurrences — documentation-only response has been observed as insufficient.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged by SRE, human-factors, and organizational-formalization literatures. The challenge is uniform: documentation-only remediation is documented failure mode for recurring preconditions; programmatic enforcement is canonical. The empirical recurrence pattern within C2A2 is the predicted failure mode.

  Specific risks: (a) Documentation-as-fix defaults to non-enforcement under workload; (b) recurrence pattern continues; (c) "fix" framing inflates the perceived progress.

  Mitigations available: (a) Programmatic enforcement (toil reduction); (b) automated guard for recurring preconditions; (c) reframe documentation as "interim measure" rather than "fix".

  Recommendation: CHALLENGED (literature consensus strong; empirical recurrence pattern within C2A2 confirms predicted failure mode)

  STEELMAN:
    Item: PRESUMPTION-122
    Strongest counterargument: SRE / DevOps practice is uniform: documentation-only remediation defaults to non-adoption under workload pressure for recurring issues. Human-factors literature is equally uniform: relying on human-recall for documented preconditions is canonical recipe for recurrence. The C2A2 cowork-to-chat sync cluster is now at 4 recurrences with documentation-only response — the empirical pattern matches the literature's prediction. Calling documentation a "fix" inflates the perceived progress and forecloses the programmatic-enforcement investigation.
    What would need to be true for C2A2 to be safe: (a) Programmatic enforcement for recurring preconditions; (b) automated guard; (c) reframe documentation as interim measure.
    How to test: Track the recurrence rate of preconditions that have only documentation-as-response vs. preconditions with programmatic enforcement; the recurrence rate gap is the empirical test.
