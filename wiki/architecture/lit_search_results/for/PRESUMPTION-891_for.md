SEARCH-FOR-PRESUMPTION-891:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-891
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium-High)
  Original statement: [inferred] That an agent's intake channels define its world — that bulk state changes
    occurring outside those channels need not be detected.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-891
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an idle report and a day of maximal activity coinciding, with the run's own stale
        WATCH-003 reading as corroboration.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Search scope: WebSearch, 2026-08-28, one dedicated query on observability blind spots in event-driven
    monitoring and detection of state changes outside instrumented channels. Literature reached: SQLI's
    observability blind-spots brief; Datadog's architecture note on observability in event-driven
    architectures; arXiv 2510.24142 on monitoring and observability of ML systems (current practices and
    gaps); arXiv 2603.09002 on security considerations for multi-agent systems. NOT COVERED and material:
    the control-theory framing (observability proper) and the audit literature on completeness of population
    coverage. All sources SNIPPET-ONLY. Search confidence: MODERATE.

  Supporting evidence found: No

  Sources:
    1. SQLI, "Blind Spots: Invisible Risks in Complex System Landscapes" [SNIPPET-ONLY]
       https://www.sqli.com/int-en/observability-blind-spots — Defines the object: in distributed dynamic
       architectures, monitoring gaps form, and blind spots are regions lacking visibility where disruptions
       go unnoticed. The prescribed countermeasure is end-to-end coverage, not acceptance of the gap.
    2. Anon. (2025), "Monitoring and Observability of Machine Learning Systems: Current Practices and Gaps"
       (arXiv:2510.24142) [SNIPPET-ONLY; authors unverified] — Reports practitioners stating that signals
       must comprehensively cover subsystems to be actionable, and that coverage gaps prevent effective
       triage; also the failure pattern where deployment-success metrics read green while the deployed
       artifact performs poorly.
    3. Anon. (2026), "Security Considerations for Multi-agent Systems" (arXiv:2603.09002) [SNIPPET-ONLY;
       authors unverified] — Notes that not all operations are instrumented and that unmonitored paths are
       exploitable; cited for the general point that channel coverage is partial by default.

  Strength of support: None

  Summary: No source endorses treating an agent's intake channels as coextensive with its world. The
    literature reached treats exactly that condition as a defect with a name — an observability blind spot —
    and reports the specific failure mode the estate exhibited: a green report from a channel that is
    covering only part of the system while a large change happens elsewhere. What this direction did *not*
    find is a method; the sources prescribe "comprehensive coverage" without saying how a coverage gap is
    discovered from inside. That gap should be taken seriously, because a remedy that consists of
    instrumenting more channels is the same design one level out.

  Caveats: Two of three sources are unreviewed preprints with unverified authorship; the third is vendor
    consultancy material. Nothing measured.

  Recommendation: NO-SUPPORT-FOUND
