SEARCH-FOR-PRESUMPTION-1194:
  Date searched: 2026-10-28
  Original item: PRESUMPTION-1194
  Original statement: "[inferred] The self-awareness layer presumes that the session list it samples contains the designer's work. Today's most consequential session (binding rulings, new branch, print build; 09:13-16:32) does not appear in the 40 most recent sessions returned to this run, and the 18:33 evening sync declared no interactive session. The decisions reached 14a only through a hand-written addendum. The audit layer sees scheduled agents reliably and designer speech least reliably: the inverse of what it exists to watch."

  Claim tested (literature): Audit-trail completeness and coverage bias (process mining event-log completeness; observability coverage); evidence that self-monitoring systems under-sample high-value, irregular events. What makes an audit source authoritative over a summary?

  Reading used for the FOR direction: the item is a concern, so support means literature showing that (a) event logs systematically miss certain kinds of activity, especially activity recorded by hand or outside the automated system, and (b) monitoring pipelines under-sample rare, irregular, high-value events. 15a does not judge whether the session listing in fact missed the 09:13-16:32 session.

  Search scope: PRELIMINARY. 2 web searches (standard), 0 fetches. Searched: process-mining event-log quality and missing events (Bose, Mans, van der Aalst; Rogge-Solti et al.); observability sampling bias and rare-event coverage. Not reached: Suriadi et al. 2017 "Event log imperfection patterns" primary; audit-log standards (NIST SP 800-92, ISO 27001 logging controls); archival-science literature on the authority of record versus summary.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1194
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the day's most consequential interactive session being absent from list_sessions(limit 40), and from the 18:33 sync declaring no interactive session. Decisions reached 14a only through a hand-written addendum.
      15a: Searched for supporting literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15a — PARTIALLY-SUPPORTED

  Supporting evidence found: Partial. Event-log incompleteness (a) is a recognised research problem. Rare-event under-sampling (b) is widely noted, but mostly in practitioner and vendor sources. Nothing found answers what makes an audit source authoritative over a summary.

  Sources:
    1. Bose, R.P.J.C., Mans, R.S., van der Aalst, W.M.P. 2013. "Wanna improve process mining results? It's high time we consider data quality issues seriously." (research.tue.nl; vdaalst.com). [snippet only]. Identifies 27 classes of event-log quality issues, including missing events, imprecise activity names and timestamp problems. Later work (with Suriadi et al. 2017) treats missing data as one of the major data-quality issues in process mining. Relevance: direct grounding for (a). Missing events are a known, catalogued failure mode of the logs that process-aware audits rely on.
    2. Rogge-Solti, A., Mans, R.S., van der Aalst, W.M.P., Weske, M., on repairing event logs with missing events (vdaalst.com p740/p746 PDFs); Leemans, Fahland, van der Aalst on discovery from incomplete logs (academia.edu). [snippet only]. In hospital settings staff enter treatment events by hand, so events or timestamps may be missing. The authors focus on the more frequent case where activities were performed but not documented. Their repair method assumes events are missing at random. Leemans et al. note that incompleteness forces discovery either to exclude the missing behaviour or to guess. Relevance: analogous support for (a). Performed-but-unrecorded activity tends to be the human-entered part of the process. The standard repair assumption (missing at random) is exactly what the item says fails, where the missing events are the high-value ones.
    3. Observability sampling sources: Tsuga, "Log sampling" blog; Tian Pan blog (tianpan.co, observability tag); Gravitee, "Observability Bias in AI Systems"; arXiv 2607.02528 (Kubernetes operational memory, evidence horizon taxonomy); arXiv 2603.16694 (observability limits in supply-chain attacks). [snippet only; mostly vendor/practitioner, two arXiv preprints]. Sampled telemetry under-represents rare but important events and short-lived spikes. Head-based sampling keeps routine traffic at the same rate as unusual cases. Sampled debugging corpora skew away from failures. A short-lived pod inside one scrape interval leaves no data. "Observability bias" means monitoring that over-represents some behaviours and under-represents others. Recommended fixes include protected rare-event lanes. Relevance: analogous support for (b). Monitoring designed around regular, high-volume events is known to under-see irregular ones.

  Strength of support: Moderate

  Summary: Process-mining research treats missing events as a catalogued, major data-quality problem. It specifically notes that activities performed but documented by hand are the ones most often missing. The standard repair assumes events are missing at random, an assumption the item's scenario (the most consequential session missing) would violate. Observability practice widely recognises that sampled monitoring under-represents rare, irregular, high-value events relative to routine traffic. Together these support the item's concern that a self-monitoring layer built on a recency-limited session list can systematically miss irregular designer sessions while capturing scheduled agents reliably. The question of what makes an audit source authoritative over a summary was not addressed by any source found.

  Caveats:
    - Process-mining sources concern business and hospital event logs. Transfer to an AI agent system's session listing is by analogy.
    - Observability evidence is mostly vendor and practitioner material, with two preprints. It is not peer-reviewed empirical work.
    - Nothing found shows coverage that is specifically inverse to importance. The item's mechanism here is more specific: a recency cap of 40 crowded out by many scheduled runs.
    - The "authoritative source" sub-question is untouched. Audit-standards and archival literature were not reached.

  Recommendation: PARTIALLY-SUPPORTED

  NOVELTY-FLAG (weak, provisional):
    Item: PRESUMPTION-1194
    Searched: event-log incompleteness; observability sampling bias (2 searches)
    Finding: No literature found on self-monitoring in agent systems where high-volume scheduled activity crowds the principal's irregular sessions out of a recency-capped audit window.
    Implication: possibly an under-described failure mode for AI agent self-audit. The general mechanism (sampling bias against rare events) is known.
    Recommended status: retain as PARTIALLY-SUPPORTED; NOVEL only for the specific agent-self-audit framing, pending a broader search.
