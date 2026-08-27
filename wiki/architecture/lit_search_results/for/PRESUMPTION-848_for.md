SEARCH-FOR-PRESUMPTION-848:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-848
  Original statement: [inferred] That a count read at the start of a run is a fact about the system
    rather than a fact about that run's moment.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-848
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by generalising one agent's own race observation from the id counter
        to the queue depth in the same report.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, August 2026, no date restriction. Queries covered: lost-update and
    read-modify-write anomalies and isolation-level definitions (Berenson et al. critique of ANSI
    SQL); time-of-check-to-time-of-use race conditions (CWE-367); instantaneous vs. time-weighted
    queue-depth measurement and point-in-time telemetry semantics; Prometheus gauge semantics and
    observation-time vs. event-time. Classification: comprehensive for the database-isolation and
    security-race literature and for metric-type semantics; preliminary for measurement-theoretic
    treatments of observing a system that changes during observation, where results were thin and
    largely patent literature. Gaps: full text not obtained for the Berenson et al. paper; no
    source located that directly frames the specific question "when is a start-of-run count a
    system fact."

  Supporting evidence found: Partial

  Sources:
    1. Prometheus, "Metric types." https://prometheus.io/docs/concepts/metric_types/ ; and
       supporting commentary, ClickHouse, "Gauge vs counter: Prometheus metric types explained,"
       https://clickhouse.com/resources/engineering/gauge-vs-counter
       — [read as search snippets + landing page] The most direct support available. Gauge metrics
       are a first-class, standard, legitimate telemetry primitive defined exactly as the claim
       assumes: "a gauge is a metric that represents a single numerical value that can arbitrarily
       go up and down"; it "represents a snapshot of a current value at a specific point in time";
       gauges "reflect the system's current state at the time of each scrape." Queue depth is named
       explicitly as a canonical gauge use case. Supports the claim insofar as a point-in-time
       count is a well-defined, valid, accepted measurement of the system — but note the definition
       itself carries the timestamp qualification ("at the time of each scrape") in every phrasing.
    2. Berenson, H., Bernstein, P., Gray, J., Melton, J., O'Neil, E., O'Neil, P., 1995. "A Critique
       of ANSI SQL Isolation Levels." *Proceedings of ACM SIGMOD 1995*.
       https://www.cs.umb.edu/cs734/CritiqueANSI_Iso.pdf ; also https://arxiv.org/pdf/cs/0701157
       [volume/page details unverified from snippets]
       — [read as search snippet + PDF landing page] Supports the claim in one specific and
       important respect: the paper's whole apparatus exists because the conditions under which a
       read *is* a durable fact about the system are formally characterisable, and achievable. It
       documents that "Cursor Stability is designed to avoid the lost update phenomenon (P4, P4C)"
       and sits between READ COMMITTED and REPEATABLE READ, holding read locks until the cursor
       advances. Under a sufficiently strong isolation level — or under snapshot isolation, which
       provides a consistent view as of a single point — a start-of-run read is a coherent fact
       about a well-defined system state, not merely a momentary artefact. That is genuine support,
       conditional on the isolation level actually in force.
    3. Snapshot isolation as characterised in the TOCTOU mitigation literature, e.g. Emergent Mind,
       "TOCTOU Races: Timing Vulnerabilities," https://www.emergentmind.com/topics/time-of-check-to-time-of-use-toctou-races
       — [read as search snippet] Notes snapshot isolation as a mitigation: "read stable snapshot —
       avoids some anomalies — may delay visibility of new writes." Supports the claim under the
       stated condition: a stable snapshot read makes the start-of-run value internally consistent
       and durable for the run's purposes. The trade-off recorded in the same breath — delayed
       visibility of new writes — is the precise price: the value stays a fact about the snapshot
       moment, not about the present.
    4. Wikipedia, "Time-of-check to time-of-use," https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use ;
       MITRE, "CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition,"
       https://cwe.mitre.org/data/definitions/367.html
       — [read as search snippets + landing pages] The definitional statement of the failure mode:
       "TOCTOU races arise whenever a system validates mutable external state and later acts as
       though that validation were still current." Recorded here because it names the exact
       condition under which the claim's support lapses, and because CWE-367's existence as a
       catalogued weakness class establishes that the claim's *negation* is the industry-default
       assumption for mutable state. Does not support the claim.
    5. Brian Candler, "Interpreting Prometheus metrics for Linux disk I/O utilization."
       https://brian-candler.medium.com/interpreting-prometheus-metrics-for-linux-disk-i-o-utilization-4db53dfedcfc
       — [read as search snippet] On the specific measurand at issue (queue depth): polling gives
       "the number of items in the queue at the sampling instant only, and this value can vary
       massively from millisecond to millisecond, making the sampled value very noisy"; the
       recommended alternative is time-weighted aggregation, multiplying depth by the duration at
       that depth. Directly bears on generalising a start-of-run queue-depth read into a system
       fact, and does not support doing so.

  Strength of support: Weak

  Summary: There is a defensible supported reading of this claim and it should not be dismissed:
    point-in-time reads are a standard, well-defined, legitimate class of measurement. Prometheus
    gauge semantics establish that "a single numerical value that can arbitrarily go up and down,"
    sampled at an instant, is a first-class telemetry primitive with queue depth named as its
    canonical example — this is not a degenerate way to measure a system, it is the normal one. The
    isolation-level literature establishes further that the conditions under which such a read
    constitutes a coherent fact about a well-defined system state are formally characterisable and
    routinely achieved: under snapshot isolation, or cursor stability, or in a single-writer
    quiescent system, a start-of-run count is a real fact about a real state. What the literature
    will not support is the claim's operative contrast — "a fact about the system *rather than* a
    fact about that run's moment." Every supporting definition located carries the timestamp inside
    it ("at a specific point in time," "at the time of each scrape," "as of the snapshot"), and the
    entire TOCTOU weakness class (CWE-367) exists to catalogue the consequences of dropping that
    qualification. On the specific measurand, queue depth, the practitioner guidance is that
    instantaneous samples are so noisy that time-weighted aggregation is the appropriate substitute
    when a durable statement about the system is wanted.

  Caveats: (a) The support is strictly conditional on either an explicit isolation guarantee
    (snapshot / cursor stability / serializable) or on the system being quiescent for the read's
    validity window. Neither condition is established for the case in the provenance, and the
    provenance itself records a race observed on a sibling measurand (the id counter), which is
    evidence that the quiescence condition does not hold. (b) Snapshot isolation buys internal
    consistency at the cost of currency — the value becomes a firm fact about a past moment, which
    is not what the claim asks for. (c) Domain transfer: the isolation-level literature governs
    transactional databases; whether the counter and queue read in question are served under any
    transactional guarantee at all was not something I could establish from literature and is a
    property of the specific system. (d) Berenson et al. bibliographic details beyond authors,
    title and year are unverified. (e) The queue-depth noise guidance is from a practitioner blog
    post, not peer-reviewed work.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: PRESUMPTION-848
    Searched: lost-update and read-modify-write anomalies; ANSI SQL isolation levels and their
      critique; TOCTOU race conditions; instantaneous vs. time-weighted queue-depth measurement;
      Prometheus gauge and point-in-time metric semantics; observation-time vs. event-time in
      telemetry.
    Finding: The general question is exhaustively addressed — the conditions under which a read
      remains valid after the moment of reading are among the most thoroughly formalised topics in
      computing. What I found unaddressed is the inferential step in the provenance: whether a race
      demonstrated on one counter in a system licenses treating a *different* count read by the
      same process at the same moment as similarly unstable. The literature characterises staleness
      per-datum, under per-datum isolation guarantees; I located nothing on propagating an observed
      concurrency anomaly from one measurand to a co-read measurand as evidence about the latter.
    Implication: The claim's supported region is reads taken under an explicit isolation guarantee
      or in a demonstrably quiescent system. The generalisation move that produced this item —
      from id-counter race to queue-depth read — is an inference the located literature neither
      licenses nor forbids, and should be treated as an untested step rather than as an application
      of established results.
    Recommended status: PARTIAL NOVELTY — unaddressed sub-claim: that a concurrency anomaly
      observed on one counter generalises to other counts read by the same process at the same
      moment.
