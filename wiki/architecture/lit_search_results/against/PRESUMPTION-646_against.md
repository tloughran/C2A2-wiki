SEARCH-AGAINST-PRESUMPTION-646:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-646
  Original statement: That the day's work is fully visible in the session-transcript
    channel, such that the absence of a session in `list_sessions` licenses the
    conclusion "no attended work occurred."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-646
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation that a "no attended work"
        conclusion was drawn from an empty `list_sessions` result
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Cook, R.I., Allspaw, J. et al., 2017. "STELLA: Report from the SNAFUcatchers
       Workshop on Coping with Complexity." SNAFUcatchers Consortium, Ohio State
       University. — Introduces "dark debt": failure modes that exist only in
       interactions between components and are, by construction, invisible to any
       instrument that examines components. A channel that records sessions cannot
       record work whose existence is constituted outside that channel.
    2. (2011). "Underreporting of patient safety incidents reduces health care's
       ability to quantify and accurately measure harm reduction." PubMed PMID
       21500613. — Direct evidence that a reporting channel's null result is a
       measure of the channel, not of the world; underreporting rates in voluntary
       systems are large and systematically biased toward certain event classes.
    3. (2015). "How effective are incident-reporting systems for improving patient
       safety? A systematic literature review." Milbank Quarterly; indexed at AHRQ
       PSNet. — Concludes that incident reports show only how many incidents were
       reported, never how many occurred, and that relying on a single reporting
       system to assess safety is unsound; multiple independent methods are required.
    4. Freedman, D.H., 2010. "The Streetlight Effect." Discover Magazine. — Names the
       bias directly: search is conducted where instrumentation exists, and "we
       looked and did not find it" is silently converted into "it does not exist."
    5. (2026). "Missing-Aware Multimodal Fusion for Unified Microservice Incident
       Management." arXiv:2603.25538. — Finds empirically that observability data
       absence is driven predominantly by failures of the observability
       infrastructure itself (agent failures, network policy), not by absence of
       activity — and that gaps coincide with exactly the periods engineers most
       need to diagnose.
    6. (2026). "Auditing Inferential Blind Spots: A Framework for Evaluating Forensic
       Coverage in Network Telemetry Architectures." Network (MDPI), 6(1), 9.
       doi:10.3390/network6010009. — Formalises the notion that a telemetry
       architecture defines an inferential universe, and that conclusions outside
       that universe are unsupported regardless of how clean the data inside it is.

  Strength of challenge: Strong

  Summary: The literature is close to unanimous and spans four independent fields
    — resilience engineering, patient safety, epidemiology of measurement, and
    cloud observability. Every one of them treats "the channel returned nothing"
    as a statement about the channel. The observability work is the most directly
    damaging: data absence correlates positively with incident periods, because the
    same conditions that break the system break the recording of the system. The
    patient-safety literature adds the sharper point that a reporting channel
    cannot even estimate its own sensitivity without an independent second method,
    so the coverage of `list_sessions` is not merely unknown — it is unknowable from
    inside `list_sessions`. The streetlight framing supplies the cognitive
    mechanism by which the inference feels safe to the agent making it.

  Specific risks: If PRESUMPTION-646 is false, C2A2 will periodically declare days
    with real attended work to be empty days. Those declarations are not inert: they
    enter persistent memory, they suppress follow-up, they bias staleness ordering
    (work that "did not happen" never becomes overdue), and they corrupt any
    downstream rate or trend computed over days. The failure is silent and
    self-reinforcing — a day recorded as empty generates no artifact whose later
    discovery would contradict the record. Worst case: the sessions least likely to
    appear in the transcript channel are precisely the anomalous ones (crashed,
    interrupted, run under a different harness), so the blind spot is biased toward
    the events most worth seeing.

  Mitigations available: (1) Never let a null channel result produce a positive
    claim — emit "no sessions visible in channel X" and forbid the string "no work
    occurred" downstream of a single-channel query. (2) Establish a second,
    structurally independent witness for the same day: filesystem mtimes across the
    vault, git log, artifact-directory listings, scheduled-task run records. Agreement
    of two independent channels is the minimum for an absence claim. (3) Measure
    channel sensitivity directly and cheaply: on days where an artifact provably
    exists, check whether `list_sessions` shows a corresponding session; the miss
    rate is the channel's false-negative rate and should be recorded. (4) Instrument
    the instrument — log query failures, empty responses, and errors distinctly, since
    an empty list and a failed call are different events that today look identical.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-646
    Strongest counterargument: In a closed single-user system, the session harness
      may in fact be the sole mechanism by which attended work is possible — if
      every attended interaction necessarily instantiates a session object, then
      the channel is not a sample of the work but is constitutive of it, and the
      inference is sound by definition rather than by induction. The observability
      literature is written about systems where work can occur through paths the
      instrument does not own; that is a contingent property, not a universal one.
      Where the instrument is the only door, absence of a record is genuinely
      absence of an event, and demanding a second witness is pure overhead.
    What would need to be true for C2A2 to be safe: (a) Every mode of attended work
      creates a session record with no exceptions — including crashed, killed, and
      alternately-launched sessions. (b) The recording is durable and not subject to
      retention windows, pagination limits, or filtering defaults. (c) The query
      path itself cannot fail silently — a broken call must be distinguishable from
      an empty result. (d) No second harness, CLI, or API path can produce work
      without registering.
    How to test: Cheap in-house check. Take the last 30 days. For each day, compute
      (i) whether `list_sessions` reports any session, and (ii) whether any file under
      the vault or outputs directory has an mtime on that day. Cross-tabulate. Any
      cell where files changed but no session was listed is a direct falsification.
      Also: deliberately kill a session mid-run and check whether it still appears —
      this tests the exact failure mode most likely to be biased against.

  Search scope: Adequate. Concepts searched: absence of evidence in monitoring;
    observability coverage gaps and unknown unknowns; telemetry data-absence causes;
    incident-reporting underreporting and sensitivity; dark debt and resilience
    engineering; streetlight/ascertainment bias; instrument-defined event universes.
