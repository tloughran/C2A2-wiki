SEARCH-AGAINST-PRESUMPTION-1118:
  Date searched: 2026-10-10
  Original item: PRESUMPTION-1118
  Original statement: [inferred] A one-word aggregate health verdict is presumed to cover everything
    though the instrument inspected a disjoint scope. Question: should health verdicts carry explicit
    scope and an UNKNOWN state for uninspected components?
  Under test: the implied correction "add explicit scope plus an UNKNOWN state". I searched for
    evidence that UNKNOWN/uncertainty states and richer verdicts get ignored, cause alert fatigue, or
    worsen decisions compared with simple summaries.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1118
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-09): Inferred that a one-word health verdict is being read as whole-system
        coverage despite a disjoint inspected scope; queued with scope/UNKNOWN-state question.
      15b (2026-10-10): Searched for challenging literature. 3 searches (alert fatigue / SRE
        symptom-based alerting; Nagios UNKNOWN-state practice; uncertainty visualisation and
        decision-making); 2 fetches (Kale, Kay & Hullman 2020 via ar5iv, full text; Nagios-devel
        thread p=72533, PARTIAL: only the original post rendered, replies truncated).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One full-text paper; one partial fetch; rest search-result, much of it
    vendor/practitioner material.

  Search scope: preliminary (3 searches, 2 fetches, 1 partial).

  Challenging evidence found: Partial
  Strength of challenge: Weak-Moderate

  Sources:
    1. Kale A, Kay M, Hullman J. 2020. "Visual Reasoning Strategies for Effect Size Judgments and
       Decisions." IEEE VIS / arXiv:2007.14516. [fetched, full text (abstract and intro read)] "when
       design choices emphasize means, users may overlook uncertainty information"; "visualization
       designs that support the least biased effect size estimation do not support the best
       decision-making"; users "satisfice with heuristics", so displays "optimally designed in theory
       may not be the most effective in practice." Bearing: adding uncertainty or scope information
       to a verdict does not ensure readers use it. They anchor on the headline token, so "HEALTHY
       (scope: X; UNKNOWN: Y)" may still be read as HEALTHY. HONEST COUNTER IN THE SAME SOURCE: the
       paper also says omitting uncertainty yields "incredible certitude", which supports the item.
    2. Alert-fatigue practitioner literature (resolve.ai, Rootly, leaddev.com, Traversal glossaries
       and blogs; Google SRE book as cited by vendors). [search-result, low-authority] When most
       signals are noise, engineers stop responding, which raises MTTR. One vendor-cited 2026 survey
       reports that 44% of organisations had incidents tied to suppressed or ignored alerts. SRE
       advice is to page on user-facing symptoms and keep cause-level detail on dashboards. Bearing:
       a persistent UNKNOWN for every uninspected component is a standing non-actionable signal of
       exactly the kind that trains readers to ignore the status channel. Survey figures are
       unverified and vendor-reported.
    3. Nagios-devel mailing list, "Services check and unreachable host status" (2007-era thread),
       support.nagios.com p=72533. [fetched, original post only; developer reply known from search
       snippet only = search-result] The operator wanted UNKNOWN instead of CRITICAL for services on
       unreachable hosts to reduce noise. Per the search snippet, a developer replied that this
       "would be misleading" since the services really are not working. Bearing: even mature
       monitoring practice disputes when UNKNOWN is the honest state. UNKNOWN can be used to soften
       real failures, and operators push to suppress it.
    4. Simplified.guide, "How to troubleshoot a Nagios plugin UNKNOWN result." [search-result] In
       Nagios, UNKNOWN (exit 3) mostly signals instrument failure (bad arguments, missing binaries),
       not "not inspected". Bearing: in the best-known three-plus-state monitoring system, UNKNOWN
       already means something different from the item's proposed use (uninspected scope). Reusing
       the label risks confusion.

  Summary: No source argues that verdicts should overclaim scope. The diagnosis (a one-word verdict
    hiding disjoint scope) is not contested. The challenge is to the remedy's effectiveness.
    Uncertainty-display research shows readers anchor on headline values and satisfice, so appended
    scope and UNKNOWN annotations are often ignored. Alert-fatigue practice shows that persistent
    non-actionable states erode attention to the whole channel. Monitoring practice uses UNKNOWN for
    instrument failure and treats it as contested even there. An UNKNOWN for every uninspected
    component would be permanent in a system where most components are uninspected on most runs.
    That is noise by construction.

  Specific risks: (a) Permanent UNKNOWNs habituate readers, so a real UNKNOWN (instrument broke) is
    missed. (b) The headline word still dominates, giving the appearance of a fix without changing
    interpretation. (c) Semantic collision between "not inspected" and "check failed".

  Mitigations available: Put scope IN the headline token (e.g. "HEALTHY[3/10]"), not as a footnote.
    Distinguish NOT-INSPECTED (expected, not alerting) from UNKNOWN (instrument failed, alerting).
    Alert only on changes.

  STEELMAN:
    Item: PRESUMPTION-1118
    Strongest counterargument: Telling readers about uncertainty does not make them use it. People
      anchor on the point estimate and satisfice, and on-call practice shows that a channel full of
      non-actionable states gets ignored wholesale. In a pipeline where any given instrument inspects
      only a fraction of components, an UNKNOWN for everything uninspected produces a standing wall of
      UNKNOWNs. It teaches every downstream reader, human or agent, to skip the field, including the
      rare UNKNOWN that means "the check itself broke". The fix may therefore cost more attention than
      the overclaim it corrects.
    What would need to be true for C2A2 to be safe: Uninspected scope is shown compactly (a ratio or
      a scope tag in the verdict token). It is distinct from instrument failure, and it does not
      generate alerts.
    How to test: After introducing scoped verdicts, check whether downstream agents' summaries still
      repeat the bare verdict word without its scope. If they do, the annotation is being ignored.

  Boundary conditions identified:
    - Alert fatigue applies to paging or interrupting channels. A passive, scope-tagged status line
      carries less fatigue risk.
    - Uncertainty-display findings are from human Mechanical Turk subjects. Transfer to LLM agent
      readers is untested, and agents may parse structured scope fields more reliably than humans.
    - Mature monitoring tools use UNKNOWN for check failure, so a separate state for "not inspected"
      avoids the collision.

  Recommendation: PARTIALLY-CHALLENGED (challenge is to the remedy's form and uptake, not the
    diagnosis)

  SYSTEMIC-RISK-FLAG: shared with ASSUMPTION-1757, PRESUMPTION-1115, PRESUMPTION-1117,
    PRESUMPTION-1119. Common vulnerability: binary corrections plus added meta-process that
    literature predicts will be ignored or accumulate as clutter in an unattended pipeline. Risk
    level: High. Full flag text in PRESUMPTION-1117_against.md.
