SEARCH-FOR-PRESUMPTION-657:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-657
  Original statement: That a check runs where its subject runs — two of four
    sections of a daily health report reading the sandbox container's process
    table and reporting it as the host Mac's state.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-657
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation that two of four sections
        of the daily health report read the sandbox container's process table
        and presented it as host state
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Kung, F., 2014. "Memory inside Linux containers." — The canonical
       write-up of the misattribution class: the host's procfs remains visible
       inside the container, so tools reading /proc report values belonging to
       a different execution context than the one the reader believes they are
       inspecting.
    2. Alibaba Cloud, "Kubernetes Demystified: Using LXCFS to Improve Container
       Resource Visibility"; LXCFS project documentation. — States the problem
       and the remedy explicitly: because /proc is not namespaced, monitoring
       tools such as free and top read host resource status from inside the
       container, "which leads to errors"; LXCFS exists as a FUSE shim to make
       /proc/cpuinfo, /proc/meminfo, /proc/stat, /proc/uptime and others
       container-aware. That a dedicated piece of infrastructure exists solely
       to fix this is itself the strongest evidence that the presumption does
       not hold by default.
    3. Docker, "Runtime metrics" (engine documentation) and Docker Engineering,
       "Gathering LXC and Docker containers metrics." — Documents that
       container-scoped metrics must be read from cgroup interfaces rather than
       from the conventional process-table view, i.e. that the naive read
       returns the wrong scope.
    4. Agent-based vs agentless monitoring literature (ManageEngine, Nagios,
       Palo Alto Networks, 2025-2026). — The nearest thing to support: agent-
       based architectures are designed on the premise that the collector runs
       on the monitored host, and all collection and health checking is handled
       by the agent installed on the device. This is a design convention that
       makes the presumption true when honoured — and it is exactly the
       convention violated by a check executing in a sandbox and reporting on
       the host.

  Strength of support: None

  Summary: No evidence was found that a check can be assumed to run where its
    subject runs; the located literature treats the opposite as a well-known
    and specifically-named failure. The container ecosystem documents the
    misattribution in the mirror-image direction — a process inside a container
    reading /proc and getting host figures — and has built dedicated
    infrastructure (LXCFS, cgroup-based metric collection) whose whole purpose
    is to close the gap between where a check runs and what it describes. The
    underlying principle is scope-symmetric: namespace-scoped introspection
    reported as the state of the other side of the boundary is wrong in either
    direction. The agent-based monitoring literature supports the presumption
    only as a design contract that must be deliberately honoured, and the
    observation reported is a case where it was not. Two of four sections
    reporting the wrong subject is, on this literature, the expected outcome of
    an unexamined co-location assumption rather than an anomaly.

  Caveats: The container literature is Linux-specific and concerns resource
    metrics rather than process tables per se, and the direction of the error
    is inverted relative to C2A2's case; the transfer is by principle, not by
    direct precedent. No source was found addressing this failure specifically
    in agent sandboxes reporting on a developer workstation, which is the exact
    configuration at issue — that narrower configuration is thinly covered and
    could reward a more targeted search.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Adequate. Concepts searched: observability in containerised and
    split-execution environments; namespace-scoped introspection reported as
    host state; /proc namespacing and LXCFS; container vs host resource
    visibility; agent-based vs agentless monitoring and collector placement;
    health-check target misattribution.
