SEARCH-FOR-PRESUMPTION-122:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-122
  Original statement: "Documentation-for-Tom presumed to count as 'fix' for recurring scheduled-task pre-condition without programmatic enforcement"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-122
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD documentation-as-fix observation
      15a: Searched for documentation-vs-enforcement literature in operational reliability
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. SRE / DevOps literature (Beyer 2016; Kim 2016 DevOps Handbook) — documentation-only remediation is documented as recurrence-prone; programmatic enforcement (toil reduction; automated guard) is canonical for recurring-precondition issues.
    2. Human-factors literature (Reason 1990 "Human Error") — relying on human-recall for documented preconditions is canonical recipe for recurrence; system-fix is preferred to social-contract for recurring issues.
    3. Adler & Borys (1996) "Two Types of Bureaucracy" — enabling vs. coercive formalization research shows that documentation without enforcement defaults to non-adoption under workload pressure.
    4. (No literature supports documentation-only as adequate remediation for recurring preconditions.)
    5. C2A2-internal: Recurring scheduled-task preconditions (cowork-to-chat sync, chat-scrape, Chrome MCP environment) have been documented multiple times; recurrence pattern is the empirical refutation of documentation-as-fix.

  Strength of support: None

  Summary: No literature supports documentation-only remediation for recurring preconditions. The SRE, human-factors, and organizational-formalization literatures uniformly endorse programmatic enforcement for recurring issues. The presumption operates against literature consensus and the empirical recurrence pattern within C2A2.

  Caveats: This is a NO-SUPPORT-FOUND for the FOR direction.

  Recommendation: NO-SUPPORT-FOUND
