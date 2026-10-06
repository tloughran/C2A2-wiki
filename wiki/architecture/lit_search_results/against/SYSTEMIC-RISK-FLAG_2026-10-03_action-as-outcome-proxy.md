SYSTEMIC-RISK-FLAG:
  Date: 2026-10-03
  Raised by: 15b (Literature Search AGAINST)
  Affected items: PRESUMPTION-1107, ASSUMPTION-1733, PRESUMPTION-1109, ASSUMPTION-1739, PRESUMPTION-1106 (and PRESUMPTION-890, which 1107 generalises)

  Common vulnerability: Unvalidated proxies standing in for outcomes, with the proxy's validity depending on an unpublished, externally controlled mechanism.
    - ASSUMPTION-1733: "SELECT 1 succeeded" stands in for "project credited as active"; the crediting rule (Supabase "sufficient user database activity") is undefined and vendor-controlled.
    - ASSUMPTION-1739 / PRESUMPTION-1109: "web search returned 0 items" stands in for "thinker produced nothing new"; recall depends on undisclosed, variable indexing latency and coverage.
    - PRESUMPTION-1106: "a lock file exists" stands in for "writers are coordinated"; the link holds only if every writer's spec checks it.
    - PRESUMPTION-1107: the general form — a task's own successful action or prior PASS treated as evidence that the outcome holds.
    In each case the monitor checks its own action, not the state of the world, and failures are silent: the proxy reads green while the outcome fails.

  Literature basis:
    - Fleming & DeMets 1996, Annals of Internal Medicine, "Surrogate End Points in Clinical Trials: Are We Being Misled?"
    - Manheim & Garrabrant 2018, "Categorizing Variants of Goodhart's Law", arXiv:1803.04585
    - flock(2) man pages (advisory locks bind only cooperating processes); Kleppmann 2016/2017 on fencing tokens
    - Martín-Martín et al. 2018, arXiv:1806.04435 (unpredictable GS indexing lag); Gusenbauer 2022, Scientometrics (coverage gaps)
    - Supabase "Project Pausing" docs, fetched 2026-10-02 revision
    - Beyer et al. 2016, Site Reliability Engineering, ch. 6 (symptom vs cause monitoring) [background-knowledge]

  Risk level: Moderate (agent spec allows High|Critical; Moderate used per the 2026-10-03 run instructions' Low/Moderate/High scale). The per-item harms are recoverable (paused projects restorable, missed papers findable later). The shared pattern makes failures correlated and silent across several monitoring tasks at once, which could justify High if more monitors turn out to share it.

  Recommendation (what the system should consider, not a design directive): For each monitoring/maintenance task, record (a) the outcome it exists to secure and (b) whether its PASS condition observes that outcome directly; treat null results and prior PASSes as "unverified" unless recall/validity has been tested; schedule periodic fault-injection or recall back-tests.
