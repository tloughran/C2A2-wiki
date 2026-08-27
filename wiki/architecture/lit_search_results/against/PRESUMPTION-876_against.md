SEARCH-AGAINST-PRESUMPTION-876:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-876
  Queue ref: LIT-QUEUE-2026-08-24-010
  Original statement: A dated health verdict in an append-only register can be read as current state
    without a staleness or retraction mechanism.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-876
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b surfaced it during 14a's resolution of a three-way contradiction that dissolved once
           observation times were applied
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: HONEST LIMITATION — no WebSearch query was executed specifically for this item. The
    session WebSearch budget (200/200) was exhausted before I reached it; my planned query (stale
    monitoring data / timestamp staleness / alarm auto-clear and re-arm / phantom faults in
    append-only status logs) returned a budget-exhausted error. The evidence below comes from a paper
    surfaced by the PRESUMPTION-871 search and then fetched and read directly, which happens to
    formalise the exact failure mode under the name "stale-generation." Venues reached: arXiv (cs.SE,
    cs.LO, cs.MA). Date range: 2026. The coverage is NARROW but the single source is unusually
    precise — it is a machine-checked formalisation with an empirical pilot, not an opinion piece.
    NOT COVERED: the operations/SRE literature on alarm lifecycle semantics (auto-clear, re-arm,
    flapping, heartbeat/liveness timeouts), which is the most obviously relevant body of practice and
    would very likely raise this from Moderate to Strong; and the temporal-database / bitemporal
    literature (valid time vs transaction time), which addresses the append-only-register question
    head-on. This item should be re-queued for a budgeted search of those two literatures.

  Challenging evidence found: Yes

  Sources:
    1. [Authors not captured.] 2026. "Verified Detection and Prevention of Concurrency Anomalies in
       Multi-Agent Large Language Model Systems." arXiv:2606.17182.
       https://arxiv.org/abs/2606.17182 — Names and formalises the failure mode. The paper models
       agent state sharing as "long-running read–generate–write operations" and formalises four
       anomalies in TLA+, the first of which is *stale-generation* — an agent generating on the basis
       of a value that is no longer current — presented as a structural analogue of a classical
       database isolation anomaly, with a TLC counter-example. Key empirical result: the real-LLM
       pilot (700 synthetic traces, 300 gpt-4o sessions, then a 900-session three-strategy baseline
       replicated on Claude Sonnet 4.5; 1,800 token-instrumented sessions across two model families)
       "reports stale-generation at 1%, 35%, 100% across plan-execute/triage/edit-review." The 100%
       figure is for the edit-review workload — the workload most similar to reading a health verdict
       out of a register. The authors flag both endpoints as workload-engineered, "a sensitivity check
       rather than a prevalence finding," so the numbers bound the phenomenon rather than estimate
       its base rate. FULL-TEXT (abstract, §1 contributions, §5 pilot summary read via fetch).
    2. Same source — the fix is an explicit mechanism, not a convention. Three deployed Rust runtimes
       realise consistency levels L0–L1 (pessimistic locking, serializable snapshot isolation,
       default-SI), "each verified against stale-generation." Crucially the paper reports that the
       weakest level "admits A1 [stale-generation] by design through the read-only no-write bypass" —
       i.e. a reader that does not write is *exactly* the case that goes unprotected, which is
       precisely the C2A2 situation of an agent reading a dated verdict and acting on it without
       writing back. Prevention costs are "bounded, not zero": ~8% tokens for snapshot isolation,
       1.6–2.3x for pessimistic locking, "not the order-of-magnitude penalty commonly assumed."
       FULL-TEXT.
    3. Same source — silence is the operative property. They "reproduce a silent lost update in
       ByteDance's deer-flow" (from an open issue in a shipped application) and "exhibit tool-effect
       reordering in LangGraph's ToolNode on unmodified output." Section 6.5 is titled "In the wild:
       the silent variant, reproduced from a live bug." A staleness failure does not announce itself;
       it produces a confident, well-formed, wrong assertion. FULL-TEXT (section titles and abstract).
    4. [Authors not captured.] 2026. "Delayed Verification Destabilizes Multi-Agent LLM Belief:
       Instability Thresholds and Optimal Corrector Placement." arXiv:2606.27409.
       https://arxiv.org/html/2606.27409v1 — Bears on why an append-only register without retraction
       is worse than a stale value in isolation: "claims are exchanged, revised, and reused as
       context, so an unsupported claim from one agent can be amplified by others," and correction
       arrives "only after several interaction steps; meanwhile the unverified claim has already
       propagated." An append-only register with no retraction mechanism maximises the propagation
       window, because the correction never arrives at all — it is merely appended alongside.
       FULL-TEXT (§1 read via fetch).
    5. The item's own provenance is corroborating evidence and should be counted as such: per the
       brief, 14a resolved a three-way contradiction that "dissolved once observation times were
       applied." That is a within-system replication of the challenge — the contradiction was an
       artefact of reading dated verdicts as current state, and applying temporal validity resolved
       it. FIRST-PARTY (from LIT-QUEUE-2026-08-24-010).

  Strength of challenge: Moderate

  Summary: The claim is contradicted both by formal work and by the pipeline's own experience. A 2026
  machine-checked formalisation names this failure mode "stale-generation," proves detectors for it
  sound and complete, and measures it at up to 100% in an edit-review workload — the workload closest
  to reading a status verdict out of a register. Two details make the challenge sharper than a generic
  "staleness is bad" result. First, the unprotected case in their weakest consistency level is
  specifically the read-only no-write bypass, which is exactly the C2A2 pattern of an agent consulting
  a health register without updating it. Second, the failure is *silent*: they reproduce a silent lost
  update in shipped production software, so the absence of an error signal is not evidence that
  staleness did not occur. The append-only aspect compounds it — without retraction, a superseded
  verdict is never removed, only buried, so a stale reading remains permanently available to any later
  reader, and the delayed-verification result suggests corrections that merely coexist with the
  original propagate too slowly to prevent amplification. Rated Moderate rather than Strong only
  because I could not reach the operations literature on alarm lifecycle semantics or the bitemporal
  database literature, either of which would almost certainly settle this; the evidence I did reach
  points one way with no dissent.

  Specific risks: If a dated verdict cannot be read as current state, then every agent that has ever
  consulted the health register may have acted on a superseded fact, and none of them would have
  known. Concretely: (a) phantom faults — an agent reads a resolved-but-never-retracted "unhealthy"
  verdict and treats a working component as broken, generating remediation work for a non-problem;
  (b) the inverse and worse case, phantom health — a stale "healthy" verdict masks a live fault, and
  because the register is append-only and nothing expires, the masking persists indefinitely; (c)
  spurious inter-agent contradiction, which is the observed symptom in the brief: three agents read
  the register at different moments, report incompatible states, and appear to be disagreeing about
  facts when they are agreeing about different times — this consumes reconciliation effort and, worse,
  erodes trust in agents that were individually correct; (d) the register's append-only property
  converts a transient error into a permanent one, since there is no operation that makes a wrong
  entry stop being readable; (e) it compounds with PRESUMPTION-871 — if contradictions are not
  surfaced by a dedicated mechanism, and staleness manufactures contradictions, then the pipeline is
  generating undetectable disagreement at an unknown rate; (f) it compounds with PRESUMPTION-875 — a
  health verdict sitting unreviewed in an unbounded queue is guaranteed to be read stale if it is ever
  read at all.

  Mitigations available:
    - Attach an observation timestamp to every verdict and require readers to apply it. This is the
      fix 14a already performed ad hoc, and it is nearly free; the change is to make it mandatory at
      write time rather than reconstructive at read time.
    - Attach an explicit validity horizon (TTL) so a verdict expires into "unknown" rather than
      persisting as "healthy" or "unhealthy." Absence of a TTL is what makes append-only dangerous
      rather than merely verbose.
    - Add a retraction/supersession operation so the register is append-only in storage but
      last-write-wins in interpretation — i.e. separate the physical log from the current-state view.
      (The bitemporal valid-time/transaction-time distinction is the standard framing here; I did not
      reach that literature in this search and flag it as unverified.)
    - Adopt an explicit consistency level over shared state, verified against stale-generation, and
      close the read-only no-write bypass specifically; measured cost is bounded at ~8% tokens for
      snapshot isolation (arXiv:2606.17182).
    - Note that alarm auto-clear and re-arm semantics are the standard operational answer to exactly
      this problem. I was unable to search for that literature and so cannot cite it; this is a known
      gap, not an absence.

  STEELMAN:
    Item: PRESUMPTION-876
    Strongest counterargument: The stale-generation results concern *concurrent* agents mutating
    shared state under a runtime that permits interleaving, where a value can change between read and
    write within a single operation. A health register may be a much tamer object: if verdicts change
    slowly relative to the read interval, if writes are infrequent and serialised, and if every entry
    carries its date on its face, then a dated verdict genuinely is readable as current state to a
    good approximation, and the date is itself the staleness mechanism — a reader who sees a
    three-week-old entry can discount it. The three-way contradiction cited in the brief supports this
    rather than undermining it: 14a resolved it correctly using nothing but the timestamps already
    present, which means the register already contained the information needed. Adding TTLs and
    retraction machinery would then be solving a problem that timestamps plus reader discipline
    already solve, at real cost in complexity.
    What would need to be true for C2A2 to be safe: (i) every entry must actually carry an
    unambiguous observation time, not merely a write time — and these differ whenever an agent
    reports something it observed earlier; (ii) the rate of state change must be slow relative to the
    read interval, so that a recent entry is reliably current; (iii) readers must consistently apply
    the timestamp rather than reading the verdict alone — 14a did, but the three agents that generated
    the contradiction did not, which is direct evidence that reader discipline is not reliable; (iv)
    there must be no read-only consumers acting on the register without any write-back that could
    reveal a conflict; (v) no downstream artefact may quote a verdict without its date, since
    quotation strips the only staleness signal present.
    How to test: Directly testable against the existing register. For each entry, compute the interval
    until the next entry about the same artefact, and compute the fraction of that interval during
    which the entry was superseded-but-still-readable — this is the register's stale-exposure rate.
    Then audit downstream artefacts for verdicts quoted without their observation time; each such
    quotation is a realised instance of the failure. Finally, replicate 14a's resolution
    systematically: search the corpus for sets of incompatible state assertions about one artefact and
    check what fraction dissolve once observation times are applied. If most do, staleness — not
    disagreement — is the dominant source of apparent inter-agent contradiction in this pipeline, and
    the presumption is confirmed as the root cause rather than merely challenged.

  Recommendation: CHALLENGED
