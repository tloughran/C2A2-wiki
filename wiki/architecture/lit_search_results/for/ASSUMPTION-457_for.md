SEARCH-FOR-ASSUMPTION-457:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-457
  Original statement: Sandbox-visible process data is not a valid substitute for host process data; the honest move is to disclose the scope gap rather than let a report imply coverage it lacks.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-457
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15a: Searched for supporting literature; result SUPPORTED (strength Strong)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Observability-scope literature (microservice trace-coverage work, arXiv:2604.13522): when instrumentation cannot see part of the system, reports built on the visible part overstate coverage; honest analysis must bound its own scope.
    2. Survivorship-bias literature (Wald; data-science survivorship-bias treatments): concentrating on the observable subset and implying it is the whole produces systematically wrong conclusions - disclosure of what is unseen is the corrective.

  Strength of support: Strong

  Summary: Strongly supported as a framework/honesty commitment. Both the observability-scope and survivorship-bias literatures endorse the assumption directly: a report drawn from a partial vantage (sandbox process table) must disclose the scope gap rather than imply host-wide coverage. The honest-coverage norm is well-established and low-controversy.

  Caveats: EMPIRICAL for the specific scope claim (whether the sandbox process table can enumerate host processes) - a one-command check.

  Recommendation: SUPPORTED
