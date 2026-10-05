SYSTEMIC-RISK-FLAG:
  Date: 2026-09-30
  Raised by: 15b (Literature Search AGAINST), scheduled run 2026-09-30
  Affected items: PRESUMPTION-1096, ASSUMPTION-1702, PRESUMPTION-1097, PRESUMPTION-1098, PRESUMPTION-1095
  Common vulnerability: Self-referential verification with no independent observer. In each item,
    the component that would detect a failure is the component that failed, or shares its failure
    mode:
      - 1096: the health monitor runs in the sandbox whose disk exhaustion it should detect.
      - 1702: the artifact's freshness is judged from the artifact (or a rebuild of it) rather than
        from an independent upstream probe.
      - 1097: the prompts' validity is judged by runs that execute those prompts and may not
        change them. Staleness is observed but never fixed.
      - 1098: the disposition agent's own default category (MONITOR) absorbs the cases where its
        evidence is too thin to decide.
      - 1095: the archive's coverage policy is the writing model's own safety defaults, and no
        outside review exists.
    Each case produces the same symptom: quiet, fluent, plausible output ("nothing to report",
    "fresh", "watched", "done") on exactly the days when something is wrong.
  Literature basis:
    - Wilkinson (2016), SRE book ch. 10 "Practical Alerting": white-box monitoring can "only alert
      on the failures that you expected". Prober, replicated monitors and meta-monitoring are the
      remedy. [fetched]
    - U.S. NRC CCF guidance (ML23205A190) and ORNL/TM-2013/563: independence and diversity as the
      standard defense against common-cause failure. [search-result level]
    - Patsakis, Argyropoulos & Alepis (2026), arXiv:2609.31575: prompts rot silently. [fetched]
    - Tversky & Shafir (1992), Psychological Science 3(6): conflict drives deferral and default
      choice. [fetched]
    - Schwartz & Cook (2002), Archival Science 2: selection must be visible and accountable.
      [search-result level]
  Risk level: High
  Recommendation: Consider one independent-observer layer that sits outside the sandbox and outside
    the agents it checks. It would (a) expect a daily health artifact and alert on absence or
    partial content, (b) probe upstream sources directly for their newest item, (c) lint task
    prompts for perishable references, and (d) audit a sample of MONITOR dispositions and in-run
    omissions. The literature consistently treats the absence of an independent check as a
    structural blind spot, not an operational detail. (Report only; design decisions belong to
    14a/14b reconciliation and Tom.)
