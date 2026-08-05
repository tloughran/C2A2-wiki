SEARCH-AGAINST-PRESUMPTION-657:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-657
  Original statement: That a check runs where its subject runs — whereas two of four
    sections of a daily health report read the sandbox container's process table and
    report it as the host Mac's state.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-657
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 finding that two of four health-report sections
        read container-scoped state and labelled it host state
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kung, F., 2014. "Memory inside Linux containers." fabiokung.com. — The reference
       treatment of the problem: `/proc/meminfo` and its neighbours are not namespaced,
       so `free` and `top` inside a container report host-wide figures. The tools predate
       cgroups and are not cgroup-aware, which makes their output "useless for modern
       Linux containers" — while looking entirely normal.
    2. "Why top and free inside containers don't show the correct container memory."
       ops.tips. — Confirms and demonstrates the same failure with worked examples, and
       shows that the reported numbers are plausible rather than obviously wrong, which is
       why the error survives review.
    3. Virtuozzo Engineering, "Java and Memory Limits in Containers: LXC, Docker and
       OpenVZ." — Documents the consequential form: the JVM sizes its heap from host RAM
       because it cannot see the container's allocation, producing OutOfMemoryError under
       a limit it never knew about. Demonstrates that this class of error propagates into
       decisions, not just displays.
    4. lxcfs issue #334, "Miscalculated used memory inside the container (cgroup v2)."
       github.com/lxc/lxcfs. — Shows that even the dedicated corrective (lxcfs) misreports
       under cgroup v2 by parsing memory.stat whose semantics differ between versions:
       the mitigation itself has version-dependent validity.
    5. Linux PID-namespace documentation and container-introspection guidance (namespace
       semantics; `readlink /proc/self/ns/pid`; `--pid=host`). — Establishes that the
       process table a container sees is namespace-scoped by construction, starting at
       PID 1, and that whether it shows host processes depends entirely on a launch flag
       the reading code cannot infer from its own output.
    6. Huang, P. et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems."
       HotOS '17. — General framing: the observer's vantage point determines what the
       failure detector can see, and the resulting observation gap is the mechanism by
       which systems report healthy while being unhealthy.

  Strength of challenge: Strong

  Summary: This is not a contested claim — it is a documented, decade-old, and still
    unsolved property of Linux containers, and the item's observation is a textbook
    instance of it. The critical detail from the literature is that the failure is
    plausible-looking rather than obviously broken: the container returns a well-formed
    process table and well-formed memory figures, so nothing downstream can tell that the
    subject is wrong. The JVM case shows the failure escalating from a display error to a
    decision error. The lxcfs bug shows that even the standard mitigation has
    version-dependent correctness, so "we installed the fix" is not sufficient assurance.
    The namespace documentation supplies the general result: what a process sees is
    determined by flags set at launch and is not discoverable from the observation itself,
    which means a check cannot verify its own subject without explicitly comparing
    namespace identifiers.

  Specific risks: Two of four sections of the daily health report are currently
    describing a different machine than the one they claim to describe, and doing so in
    the same format and with the same authority as the two correct sections. A reader
    cannot tell them apart. The immediate consequences: real host-side problems (a hung
    process, resource pressure, a stalled scheduled task on the Mac) are invisible and
    will report healthy; conversely, sandbox-side artefacts will be raised as host alarms
    and waste attention. Because the sandbox is ephemeral and largely idle, the likely
    error direction is false reassurance — the report will read healthy essentially
    always, which makes the health report an active source of unjustified confidence
    rather than a neutral null. This compounds with PRESUMPTION-661: a stalled host
    process is exactly the class of thing these sections purport to detect.

  Mitigations available: (1) Make the vantage point explicit in the artifact: every
    section of the health report should record where it executed (container vs host) and
    what namespace it read. A section that cannot state this should not emit a verdict.
    (2) Add a self-check: compare `readlink /proc/self/ns/pid` against the expected host
    namespace, or simply test for the presence of a known host-only process. A single
    boolean "am I where I think I am" gate is cheap and catches the whole class.
    (3) Route host-state questions through a mechanism that genuinely runs on the host
    (a host-side agent, scheduled task output written to a shared path, or a
    filesystem-mediated report) rather than through in-container process inspection.
    (4) Prefer cgroup-aware sources over `/proc` for any resource figure, and record the
    cgroup version, given the lxcfs v2 discrepancy. (5) Until fixed, relabel the two
    affected sections rather than deleting them — "sandbox process table" is a true and
    occasionally useful statement; "host Mac state" is a false one.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-657
    Strongest counterargument: If the container is configured with `--pid=host` or an
      equivalent, its process table genuinely is the host's, and the check is correct as
      written; the failure mode depends on a configuration detail that may not apply here.
      More broadly, a health report that is right in two of four sections is still net
      useful, and the two container-scoped sections may be answering a question that is
      actually about the sandbox — which is where most of the system's work runs anyway,
      making the sandbox arguably the more relevant subject. Demanding host-side execution
      introduces a whole new component (a host agent) whose own failures would be
      unmonitored, potentially trading a known labelling error for an unknown availability
      one.
    What would need to be true for C2A2 to be safe: (a) The container shares the host PID
      namespace, verifiable directly. (b) The resource figures come from cgroup-aware
      sources with a known cgroup version. (c) The questions those two sections answer are
      genuinely about the sandbox, and the artifact says so. (d) Nothing downstream treats
      a healthy verdict from those sections as evidence about host-side scheduled work.
    How to test: One command settles it. Inside the sandbox, list processes and look for a
      known host-only process (e.g. the Claude desktop app, Finder, or a launchd agent). If
      absent, the namespace is not shared and the two sections are provably misreporting.
      Equally cheap: compare `readlink /proc/self/ns/pid` inside the sandbox with the value
      obtained on the host. Both are seconds of work and give a definitive answer.

  Search scope: Adequate. Concepts searched: PID and mount namespace scoping of `/proc`;
    `top`/`free` reporting host values inside containers; cgroup-awareness and lxcfs
    limitations; JVM container-awareness failures; observability in split-execution
    environments; differential observability.
