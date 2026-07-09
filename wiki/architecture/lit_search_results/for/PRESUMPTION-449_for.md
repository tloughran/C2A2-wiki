SEARCH-FOR-PRESUMPTION-449:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-449
  Original statement: "[inferred] The set of possible repo writers is fully enumerable from the local process table."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-449
    Item type: PRESUMPTION (unstated — surfaced by inference; severity MEDIUM)
    Transform at each step:
      14b: Inferred that "no git process is running" (from a process listing) was treated as proof that no other writer existed before acting on a lock
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Practitioner lock-diagnosis canon (Sinjakli, 2021, "Waiting for apt locks without the hacky bash scripts"; OneUptime 2026 dpkg-lock guide; Siebenmann, "Lslocks notes," utcc.utoronto.ca). — Documents the standard, widely endorsed procedure: before touching a lock file, enumerate holders via fuser/lsof/lslocks/ps against the local process table, and only remove the lock once no live holder is found. This is direct support that local process-table enumeration is the accepted first-line method for identifying current writers on a single host.
    2. lslocks / /proc/locks kernel facility (util-linux documentation). — On a single host, the kernel's lock table is authoritative for kernel-level advisory locks; supports enumerability in the restricted case where all writers are local, live processes using kernel locks.
    3. Cron/scheduled-job monitoring literature (Cronitor troubleshooting guide; UptimeRobot crontab guides; "Kubernetes CronJobs silently fail more than you think," DEV 2025). — Establishes that scheduled writers are knowable in principle from local configuration (crontab, launchd, task scheduler manifests) even when not currently running; supports a broadened version of the claim: the writer set is locally enumerable if process table AND scheduler configuration are both consulted.

  Strength of support: Weak

  Summary: There is genuine practice-level support for the operational core of this presumption: on a single machine, checking the process table (ps/lsof/fuser/lslocks) before acting on a lock is the documented, recommended procedure, and for live local processes it is authoritative. The presumption's word "fully," however, outruns the support. A process table enumerates current writers only: scheduled agents that have not yet fired are absent from it by construction (they exist in scheduler configuration, not the process table), and the same practitioner sources that recommend the lsof check frame it as reducing—not eliminating—uncertainty. Git's index.lock is not a kernel lock, so /proc/locks-style authority does not even apply; the lock's existence is the only evidence, and its holder may be a process that already died (stale) or one about to spawn (imminent). The strongest defensible version supported by the literature is: current local writers are enumerable; possible writers require consulting scheduler state as well.

  Caveats: Support weakens or vanishes when (a) writers can arrive from outside the process table's time slice — cron/launchd/scheduled agents firing between check and action (TOCTOU gap); (b) the repository is reachable via network mounts or remote sessions (writers on other hosts are invisible locally); (c) the lock mechanism is file-existence-based (git) rather than kernel-advisory, so no tool maps lock to holder reliably; (d) agent processes run under names not obviously associated with git (wrapper processes make grep-based enumeration under-inclusive).

  Recommendation: PARTIALLY-SUPPORTED
