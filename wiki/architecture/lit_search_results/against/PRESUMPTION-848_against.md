SEARCH-AGAINST-PRESUMPTION-848:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-848
  Original statement: [inferred] That a count read at the start of a run is a fact about the system
    rather than a fact about that run's moment.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-848
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by generalising one agent's own race observation from the id counter
        to the queue depth in the same report.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: Comprehensive on the database/concurrency side, moderate on the queueing-theory
    side. Queries: "TOCTOU time-of-check time-of-use stale read snapshot isolation lost update
    read-modify-write anomaly monitoring counter"; "queue depth instantaneous sample misleading
    metric time-averaged backlog Little's law point-in-time gauge"; "dual write problem".
    Venues: Wikipedia (TOCTOU, Little's Law), the ANSI SQL isolation-levels critique,
    performance-engineering blogs (Sookocheff, Gunther/perfdynamics), storage-vendor patents on
    queue-depth metrics. Date range 1995–2026.
    Gaps: no source found that addresses this specific epistemic framing directly; the
    challenge below is assembled from three adjacent literatures (concurrency anomalies,
    security race conditions, queueing measurement) rather than drawn from one authority. The
    strength rating reflects that.

  Challenging evidence found: Partial

  Sources:
    1. "Time-of-check to time-of-use." https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use
       — The canonical name for the exact error: "a program makes a decision based on a
       property it checked earlier, but later performs an operation assuming that property
       still holds." Also notes TOCTOU arises from improper use of database transactions, not
       only filesystems. FULL-TEXT.
    2. Berenson, Bernstein, Gray, Melton, O'Neil, O'Neil, "A Critique of ANSI SQL Isolation
       Levels." https://arxiv.org/pdf/cs/0701157 [SIGMOD 1995; volume/pages unverified]
       — Formalises the anomalies that arise when a read is treated as durable knowledge:
       fuzzy reads, lost updates, phantoms. The relevant point for this item is that under
       snapshot isolation a transaction reads a snapshot as of its *start timestamp* — the
       read is explicitly indexed to a moment by construction, and treating it otherwise is
       what produces the anomaly. FULL-TEXT (PDF).
    3. Lost-update / read-modify-write characterisation, recovered from the isolation-levels
       result set (e.g. https://blog.calvinsd.in/isolation-levels-in-databases,
       https://www.systemdesignacademy.com/blog/isolation-in-databases)
       — Two readers of the same value both act on it and one effect is silently lost. The
       fix is a compare-and-set on the originally read value, i.e. explicitly re-asserting the
       moment at write time. SNIPPET-ONLY.
    4. "Little's law." https://en.wikipedia.org/wiki/Little's_law and Sookocheff, "Using
       Little's Law to Measure System Performance." https://sookocheff.com/post/modeling/littles-law/
       — Little's Law relates the *average* queue occupancy to arrival rate and residence time.
       The quantity the theory treats as meaningful about the system is the time-average; a
       single instantaneous reading is a sample from a fluctuating process, not the parameter.
       FULL-TEXT.
    5. Gunther, "How Long Should My Queue Be?" The Pith of Performance.
       http://perfdynamics.blogspot.com/2007/04/how-long-should-queue-be.html
       — "Looking at the system for a few minutes while it is running is really an
       instantaneous snapshot of the system, rather than a steady-state view." Directly against
       reading a single depth measurement as a system property. SNIPPET-ONLY.
    6. Storage-industry framing of queue-depth metrics as fluctuating occupancy requiring
       averaging over a period (US patents on backlog-based capacity management and queue-depth
       performance-impact detection, e.g. US 9,686,204; US 11,023,169) — cited only as evidence
       that the instantaneous-vs-averaged distinction is standard practice in the field, not as
       a scientific authority. SNIPPET-ONLY.

  Strength of challenge: Moderate

  Summary: No source directly addresses the presumption in these words, but three adjacent
  literatures agree on its substance. TOCTOU names the general error precisely — acting later
  on a property checked earlier, assuming it still holds — and notes that it arises with
  database reads, not only files. The isolation-levels literature shows that a read is
  formally indexed to a timestamp (snapshot isolation defines the read *as of* the
  transaction's start), and that treating it as timeless is what generates lost updates and
  phantoms; the standard remedy, compare-and-set against the originally read value, works by
  re-asserting the moment at write time. Queueing theory adds that the quantity meaningful
  about a system is the time-averaged occupancy, not a single sample — Gunther's point that a
  short look is a snapshot rather than a steady-state view. The challenge is Moderate rather
  than Strong because it is conditional: where the queue is quiescent for the run's duration,
  or where the count is used only for a report labelled with its timestamp, the presumption is
  harmless. It becomes false exactly where the count is used for a decision that outlives the
  moment it described, and the item's own evidence — a race already observed on the id counter
  in the same report — indicates the system is not quiescent.

  Specific risks: The risk is graded by use. If the count only feeds a display or a log line,
  a stale reading is cosmetic. If it feeds a decision — batch sizing, a "queue is empty, exit
  early" branch, an alert threshold, a completion assertion, or a capacity check — then a count
  read at start and acted on at end is a lost-update or TOCTOU bug: items that arrived during
  the run are invisible to the run that was supposed to handle them, and get carried to the
  next cycle or silently skipped. Compounded across days this produces monotonic queue growth
  that no single run reports as anomalous, because each run truthfully reports the depth it
  saw at its own start. Note this interacts badly with ASSUMPTION-1161: a run that dies
  mid-phase leaves a start-of-run count that describes a state no longer reachable, so the
  count becomes actively misleading on recovery. It also interacts with PRESUMPTION-847: a
  start-of-run count is not evidence about how far a truncated run got.

  Mitigations available:
    - Timestamp every count at the point of measurement and carry the timestamp with the value,
      so downstream consumers cannot silently treat it as current (standard telemetry practice;
      follows from the snapshot-isolation framing in Berenson et al.).
    - Compare-and-set / optimistic concurrency: condition the write on the value originally
      read, and re-read on conflict (lost-update remedy, isolation-levels literature).
    - Re-read at the point of use rather than the point of planning; where the gap cannot be
      closed, take the transaction boundary around check-and-act (TOCTOU remedy).
    - Report both start-of-run and end-of-run counts plus items processed, so arrivals during
      the run are visible as a residual rather than absorbed silently.
    - Where the question is about the system rather than the run, use a time-averaged or
      windowed measure rather than a point sample (Little's Law; Gunther).

  STEELMAN:
    Item: PRESUMPTION-848
    Strongest counterargument: A count is a measurement of a moving quantity, and the act of
    reading it does not freeze it. TOCTOU is the name for building on a property that has since
    changed, and the database literature makes the indexing explicit — under snapshot isolation
    a read is defined *as of* a timestamp, so a read stripped of its timestamp has lost the
    only thing that made it well-formed. Queueing theory pushes further: even a correctly
    timestamped instantaneous depth is a sample from a fluctuating process, so it is not the
    system-level quantity anyone actually wants; that is the time-average. The presumption
    therefore commits two errors at once — treating a moment as a duration, and treating a
    sample as a parameter — and the item's own evidence that a race was already observed on the
    id counter in the same report shows the preconditions for both errors are present.
    What would need to be true for C2A2 to be safe: (a) the queue does not change during a run
    — no concurrent producer, and the run is the only consumer; or (b) the count is used only
    for reporting and is displayed with its measurement timestamp; or (c) every decision that
    depends on the count re-reads it at the point of decision, or is guarded by a
    compare-and-set that fails loudly on change; or (d) the run's correctness is defined over
    the set of items it actually processed rather than over a count captured at start.
    How to test: Instrument both endpoints — record depth at start and at end of each run,
    together with items processed — and check whether `start - processed == end` holds. Any
    persistent residual is direct evidence of arrivals during the run, and therefore that the
    start-of-run count was a fact about a moment. Second test: enqueue items deliberately while
    a run is in flight and observe whether that run, or only the next one, handles them; and
    whether any log line asserts a depth that was already wrong when written.

  Recommendation: PARTIALLY-CHALLENGED
