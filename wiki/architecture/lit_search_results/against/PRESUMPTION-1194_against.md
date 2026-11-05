# PRESUMPTION-1194 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY. Broader search recommended. Scheduled run 2026-10-28 (lock held by parent). Budget for this item: 2 web searches (standard), 0 fetches. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge": this item is a concern. Following the template convention (PRESUMPTION-1190), I search against the presumption as 14b states it: that the session list the self-awareness layer samples contains the designer's work. Evidence that event logs and sampled telemetry systematically miss irregular, human-driven events counts as a challenge to the presumption (and supports 14b's concern). I did not verify the in-house facts (list_sessions limit 40, the 09:13-16:32 session, the 18:33 sync).

```
SEARCH-AGAINST-PRESUMPTION-1194:
  Date searched: 2026-10-28
  Original item: PRESUMPTION-1194
  Original statement: "[inferred] The self-awareness layer presumes that the session list it
    samples contains the designer's work. Today's most consequential session ... does not
    appear in the 40 most recent sessions returned to this run ... The audit layer sees
    scheduled agents reliably and designer speech least reliably."
  Claim tested: Audit-trail completeness and coverage bias (process-mining event-log
    completeness; observability coverage); do self-monitoring systems under-sample high-
    value, irregular events? What makes an audit source authoritative over a summary?

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1194
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the missing interactive session and the addendum route.
      15b: Searched for challenging literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15b — CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Van der Aalst group report on event-log quality under manual logging (vdaalst.com
       p740 / p746). [snippet only; title not shown]
       — Direct challenge. Where logging is manual, incorrect or missing events are common.
       The more frequent problem is that activities are performed but their documentation is
       missing.
    2. Fluxicon, 2016. "Data Quality Problems in Process Mining and What To Do About Them —
       Part 9: Missing Timestamps." [snippet only]
       — Direct analogue. Manual activities (e.g., a phone call at a desk) happen in the
       process but are not in the data, so the discovered process map will not show them.
       Fix: collect manual data by observation or by asking people to log their work.
    3. Log-repair literature (stochastic Petri net / Bayesian repair; succession-relation and
       imputation methods; arXiv 2301.10927 knowledge-centric process mining). [snippet only]
       — Boundary condition. Repair methods assume data is missing at random. When missingness
       depends on who acted (here: the designer, not a scheduled agent), the assumption fails
       and repair is biased.
    4. Observability sampling guides (OpenObserve, HyperDX, MLflow, Grafana; vendor blogs).
       [snippet only]
       — Mechanism. Head-based sampling decides before the outcome is known, so rare events
       are kept at the base rate (e.g., 0.1% errors at 5% sampling leaves almost no error
       traces). A single global rate starves low-traffic sources. A "40 most recent" window
       acts like this: dozens of scheduled firings crowd one long interactive session out.

  Strength of challenge: Moderate-Strong. Process mining treats unrecorded human activity as a
    known, common gap, and sampling practice explains why frequent sources crowd out rare
    ones. Sources are practitioner-level snippets. The "what makes an audit source
    authoritative over a summary" question was not addressed.

  Summary: Process-mining literature says the commonest log defect is work that happened but
    was never recorded, and that manual human activity is where this concentrates. Standard
    repair assumes missingness is random; here it depends on the actor, so it is not.
    Observability practice shows that uniform or count-limited sampling keeps rare events at
    their base rate and loses them under volume. A recency-limited session list dominated by
    scheduled agents is expected to miss the designer's irregular sessions, which matches the
    10-27 record.

  Specific risks: The self-awareness layer reports "no interactive session" on the days that
    matter most. Decisions reach the record only through hand-written addenda, which the
    audit layer then cannot check. Counts and health summaries describe the scheduled agents
    and silently omit the designer.

  Mitigations available: Query interactive sessions separately from scheduled ones (stratify,
    the analogue of per-service sampling rates). Use a time window instead of a count limit.
    Keep everything from rare, high-value sources (the analogue of tail-based "always keep
    errors"). Have the designer's sessions write a lightweight self-log (Fluxicon's remedy).
    Treat "none found" as "none returned" and say what was searched.

  Recommendation: CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1194
  Strongest counterargument: Every field that audits from logs has learned that the work done
    by people, off the automated path, is what goes missing, and that sampling by volume or
    recency loses rare events first. A self-awareness layer that reads the 40 most recent
    sessions, in a system with dozens of scheduled firings a day, is built to see the robots
    and miss the designer. Its "no interactive session" is the expected output of its design,
    not a finding.
  What would need to be true for C2A2 to be safe: interactive sessions are queried as their
    own stratum with no count cap, or the window is long enough that scheduled volume cannot
    push them out; and summaries say what they searched.
  How to test: For one week, compare list_sessions(limit 40) against a full, unfiltered
    session list and a designer self-log. Measure the share of interactive sessions missed.
```

Source quality: all snippets; sources 2 and 4 are practitioner/vendor material. Systemic note: extends the existing 'artefact-as-proof' candidate (a returned list taken as proof of what happened); see PRESUMPTION-1191_against.md.
