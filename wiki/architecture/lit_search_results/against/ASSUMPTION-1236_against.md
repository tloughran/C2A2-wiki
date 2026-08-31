SEARCH-AGAINST-ASSUMPTION-1236:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1236
  Original statement: "A structurally identical ~300 KB file is clutter, not measurement."
  Generalizable limb searched: Does a repeated measurement under an unchanged method carry
    information, or is byte-identical output by definition uninformative?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Moderate. 2 queries (Priority Medium — no Pass 2, per budget). The first query
    returned repeated-measures statistics that were only obliquely relevant; the second returned
    the replication literature, which is directly on point. UNDER-SEARCHED on the software /
    regression-testing limb, where I expect the strongest counter-evidence lives (golden-file and
    characterisation testing) and where I ran no dedicated query. Snippet-level reading only.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1236
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Stated as a judgement about a redundant artefact produced during the run.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Replication crisis." Wikipedia, accessed 2026-08-31. — Encyclopedic summary of the direct-
       replication argument: direct replications add data that increase the precision of effect-size
       estimates, and without direct replication there is no reliable way to identify false
       positives; direct replications producing negative results identify boundary conditions. The
       explicit counter to "same method, same result, therefore no information." Tertiary source.
    2. Stanford Encyclopedia of Philosophy, "Reproducibility of Scientific Results."
       plato.stanford.edu. — Distinguishes reproducibility (same data, same code, same conditions →
       same result) from replicability. Under this distinction, a byte-identical re-run is the
       definition of a successful reproducibility check, i.e. it is a measurement of the pipeline,
       not of the vault. Snippet/entry-level only.
    3. Cockburn, Dhillon & Samila (as carried in) "Threats of a Replication Crisis in Empirical
       Computer Science." Communications of the ACM. — Argues the replication problem is live in
       empirical CS specifically. I saw the title and venue via search listing and did not read the
       article; author attribution here is from the venue listing and should be verified before
       citing onward.
    4. "When Negative Turns Positive and Vice Versa: The Case of Repeated Measurements."
       ScienceDirect (Journal of Clinical Epidemiology / related), 2017. — Repeated measurement
       changes the sign and magnitude of inferred relationships relative to single measurement;
       repeated measures are how measurement error is separated from real change. Snippet only.
    5. INTERNAL CONTRADICTION (not a literature source, recorded as evidence): ASSUMPTION-1237 in
       the same cohort licenses week-over-week deltas *because* five top-hub counts reproduced
       exactly. The same run therefore treats exact reproduction as informative when it is a control
       and as clutter when it is a file. Both cannot be right.

  Strength of challenge: Moderate

  Summary: The claim conflates two different things — the file being redundant on disk, and the act
  of re-measuring being uninformative. The first may well be true; the second is not, and the run's
  own reasoning proves it. Under the standard reproducibility/replicability distinction, a
  structurally identical output under an unchanged method is a *passed reproducibility check*: it
  establishes that the extraction pipeline is deterministic, which is the precondition for reading
  any subsequent difference as a signal about the vault rather than about the tooling. Delete the
  re-runs and the next non-identical output becomes ambiguous between "the vault changed" and "the
  pipeline drifted." The replication literature adds the sharper point that negative and null
  results are the mechanism by which false positives get caught, and that they are systematically
  under-produced precisely because they feel like clutter — which is the exact judgement 1236 makes.

  Specific risks: Discarding identical re-runs removes the only baseline against which silent
  pipeline drift could be detected — a changed dependency, a changed default, a changed parser. In
  a pipeline whose main product is week-over-week deltas, losing the ability to distinguish tool
  drift from corpus change is a direct threat to every delta claim, including the ones 1237 licenses.
  The second risk is that "clutter" is applied asymmetrically: outputs that differ get kept and
  outputs that match get deleted, which biases the retained record toward change and manufactures
  an appearance of movement.

  Mitigations available: Keep the measurement, drop the bytes — store a hash or a small manifest
  (row counts, top-N values, schema fingerprint) per run instead of the full 300 KB. That preserves
  the reproducibility check and the drift detector at ~0.1% of the storage. If the artefact really
  is byte-identical, deduplicate by content address rather than deleting. Either way the correct
  target is storage cost, not the measurement.

  STEELMAN:
    Strongest counterargument: The replication literature is about independent re-execution under
    conditions that could have differed — different lab, different sample, different analyst. A
    deterministic script re-run on an unchanged input is not a replication in that sense; it is a
    tautology, and it cannot fail in any way that carries information about the world. Retaining
    such artefacts is genuinely the collector's fallacy applied to outputs. The internal-contradiction
    point is weaker than it looks: 1237's controls reproduce across a *changed* input, which is
    informative, whereas 1236's file reproduces across an *unchanged* one, which is not — the two
    cases are not symmetric.
    What would need to be true for C2A2 to be safe: The input would have to be genuinely unchanged
    and verifiably so, and the pipeline genuinely deterministic and verifiably so. If either is only
    assumed, the identical output is the evidence for the assumption and cannot be discarded on the
    strength of it.
    How to test: Deliberately perturb the pipeline — bump a dependency, change a locale, reorder an
    input — and check whether the ~300 KB artefact changes. If it does, it is a live drift detector
    and 1236 is false. If nothing perturbs it, it is inert and 1236 is right.

  Recommendation: CHALLENGED
