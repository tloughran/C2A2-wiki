SEARCH-FOR-ASSUMPTION-451:
  Date searched: 2026-07-13
  Original item: ASSUMPTION-451
  Original statement: "qc_sweep.py's report path keys on the newest pair timestamp and therefore returns 0 across the board — the scripted staleness instrument is fully blind and manual scanning is the sole work source."

  PROVENANCE:
    Origin: 14a
    Chain: 14a -> 15a
    Original item: ASSUMPTION-451
    Item type: ASSUMPTION (stated; QUEUED-EMPIRICAL)
    Transform at each step:
      14a: Extracted from the 2026-07-12 EOD run (Summa QC work-sourcing)
      15a: Searched for supporting literature
    Current status: SUPPORTED (polarity: hazard confirmed — the failure CLASS is real and common)

  Supporting evidence found: Yes
  Sources:
    1. [Vacuity-detection literature in formal verification (Beer, Ben-David, Eisner & Rodeh lineage; "Robust Vacuity for Branching Temporal Logic," arXiv:1002.4616; SystemVerilog assertion "vacuous success" doctrine). — A property passes VACUOUSLY when a subformula is irrelevant to its satisfaction; empirically ~20% of specifications pass vacuously on the first formal-verification runs of a new hardware design, and a vacuous pass ALWAYS indicates a real problem in the design, the specification, or the environment. An instrument that keys on a predicate that is never false is the software analogue.]
    2. [Silent-failure / observability doctrine (Ministry of Testing software-testing glossary, "Silent failure"; industry observability literature on detecting silent failures in microservices). — A silent failure is one where the system fails but surfaces no error: "tests may pass, dashboards may look healthy," and infrastructure metrics remain green while the underlying behaviour is broken. A staleness scanner returning 0 unconditionally is exactly this pattern: a green dashboard that cannot go red.]
    3. [Kudrjavets, G., Nagappan, N. & Ball, T. (2006). "Assessing the Relationship Between Software Assertions and Faults." ISSRE / MSR-TR-2006-54. — Establishes that in-code checks only reduce fault density when they can actually FIRE; a check whose antecedent is never satisfied contributes nothing, which is the mechanism the claim alleges.]
  Strength of support: Strong (for the hazard class), None (for the specific code fact)
  Summary: The failure mode ASSUMPTION-451 alleges is a well-characterised and common class, not an exotic hypothesis. Formal verification has an entire sub-discipline (vacuity detection) devoted to it, with the striking empirical finding that roughly a fifth of specifications pass vacuously on first run and that a vacuous pass never means "all is well" — it always points at a real defect somewhere. Observability doctrine names the same pattern at the system level: the green dashboard that cannot go red. If qc_sweep.py's report path really does key on the newest pair timestamp, then it is a verifier that cannot fail, and the literature says such verifiers are actively harmful because they consume the trust budget that a working instrument would earn.
  Caveats: The literature confirms the hazard class; it cannot confirm the specific code fact. Whether THIS script has THIS defect is decidable only by reading the report code path and running the queued fixture (one fresh pair + one deliberately stale pair). The claim's second clause — "manual scanning is the sole work source" — is a universal generalisation from a single observation and is not addressed by any literature.
  Recommendation: SUPPORTED (hazard class) / NO-SUPPORT-FOUND (specific instance — in-house test required)
