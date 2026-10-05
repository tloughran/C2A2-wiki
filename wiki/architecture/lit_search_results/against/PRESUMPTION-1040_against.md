SEARCH-AGAINST-PRESUMPTION-1040:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1040
  Original statement: Registry liveness does not track process liveness. A status flag set at launch cannot distinguish a slow process from a dead one; only a progress heartbeat with a timeout can, and that distinction is provably not free.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1040
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (third observed instance; downstream drain currently zero)
      15b: Searched for challenging literature; found no source refuting the core claim; found boundary conditions on "only a progress heartbeat can" and on cost/false-positive behavior; strength: Weak
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Search scope: preliminary search — broader search recommended (4 web searches, 4 page fetches; no access to full-text of paywalled papers; Kubernetes page fetch returned no cautions text, so K8s pitfalls are NOT cited as evidence).

  Sources:
    1. Huang, Guo, Zhou, Lorch, Dang, Chintalapati, Yao, 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS 2017. https://www.microsoft.com/en-us/research/publication/gray-failure-achilles-heel-cloud-scale-systems/ — Shows heartbeat/health-check detectors can report "alive" while the application is degraded ("differential observability"). Challenges "only a progress heartbeat can distinguish": a heartbeat is itself a liveness proxy and can be decoupled from real progress (boundary condition: heartbeat must be emitted from the work path, not a side thread).
    2. Ma and Wang, 2018. "Accurate Timeout Detection Despite Arbitrary Processing Delays." USENIX ATC 2018. https://www.usenix.org/conference/atc18/presentation/ma-sixiang — Timeouts yield false failure reports when OS/application delays are unpredictable; states a mechanism to prevent false reports despite arbitrary delays. Supports the "not free" half but also challenges the claim that the slow/dead distinction is inherently unavoidable-cost: the cost can be reduced in some settings (requires mechanism support, e.g., lease/OS-level cooperation, unlikely in a registry-based agent pipeline).
    3. Temporal documentation, "Detecting Activity Failures." https://docs.temporal.io/encyclopedia/detecting-activity-failures — Production workflow engine states heartbeating is unnecessary for short operations and not required for local activities, and caps heartbeat timeout by the start-to-close timeout; indicates that a simple overall timeout (a status/deadline mechanism, not a progress heartbeat) is considered sufficient for bounded-duration work. Boundary condition: heartbeats matter only for long-running work.
    4. Beyer, Jones, Petoff, Murphy (eds.), 2016. "Monitoring Distributed Systems," in Site Reliability Engineering (Google). https://sre.google/sre-book/monitoring-distributed-systems/ — Advises paging on symptoms rather than causes, asks "will I ever be able to ignore this alert, knowing it's benign?", and recommends removing rarely-exercised alerting rules as fragile. Indirect support for the false-positive/fragility concern about absence alarms; it does not quantify false positives for analytical jobs.

  Strength of challenge: Weak

  Summary: No located source contradicts the core claim; the impossibility of perfectly distinguishing slow from dead in asynchronous systems is standard (that is the content 15a will cover). The challenges are boundary conditions. (a) Gray failure work shows heartbeats are themselves imperfect proxies, so "only a progress heartbeat can" holds only if the heartbeat is tied to genuine work progress. (b) Production systems (Temporal) treat a plain overall deadline as adequate for bounded jobs, so a launch-time flag plus a hard deadline may suffice where durations are predictable. (c) The specific sub-claim in the queue brief, that absence alarms on long-running analytical jobs produce more false positives than the silent deaths they catch, was NOT found stated or measured in any source I could verify; only general alert-fatigue guidance (SRE book) points the same direction. This is a literature gap, not evidence of absence.

  Specific risks: If the heartbeat is emitted by a wrapper/side thread rather than from the work loop, C2A2 would get a false "alive" signal (gray failure) and silent deaths of the useful kind would persist while the system believes it has closed the gap. Conversely, a tight timeout on bursty analytical jobs may mark slow-but-healthy runs dead, causing duplicate work or discarded results.

  Mitigations available: Emit heartbeats from within the work loop with a progress counter (not just a timestamp); use adaptive/phi-accrual style timeouts or generous multiples of observed p99 inter-progress interval; two-tier states (SUSPECT before DEAD) with a verification probe before reaping; make reaping idempotent so false positives are cheap; keep a hard deadline for bounded jobs.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1040
  Strongest counterargument: The claim treats "heartbeat with timeout" as the discriminating mechanism, but the gray-failure literature shows that heartbeat signals are exactly the kind of shallow proxy that diverges from real health, so adding one can create false confidence rather than closing the gap. Meanwhile, for jobs with bounded, roughly predictable duration, a launch-time flag plus a single hard deadline gives most of the benefit at near-zero ongoing cost and none of the false-positive tuning burden, which is why mature workflow engines make heartbeating optional and only recommend it for long activities. For bursty analytical workloads, any fixed heartbeat timeout sits between two failure modes (false kills versus delayed detection), and under alert-fatigue dynamics a noisy absence alarm can be worse than silence because humans learn to ignore it. The presumption therefore overstates both the necessity and the net benefit of the heartbeat.
  What would need to be true for C2A2 to be safe: Heartbeats reflect real forward progress; job durations are long and unpredictable enough that a hard deadline is inadequate; reaping a falsely-suspected process is cheap and reversible; a human or agent reviews absence alarms at a rate that does not cause habituation.
  How to test: Replay C2A2's observed runs (including the three observed instances) against candidate detectors: (1) launch flag + hard deadline, (2) fixed heartbeat timeout, (3) adaptive timeout; measure false-kill rate and detection delay versus actual silent deaths.

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1040
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak
  Key source: Huang et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS 2017.
  Specific risk: A heartbeat not tied to real progress yields false "alive" signals (gray failure), and tight timeouts on bursty jobs can kill healthy runs. The queue's specific claim that absence alarms cost more than the deaths they catch was not found in verifiable literature (literature gap).
  Summary: Core claim not contradicted; challenges are boundary conditions (heartbeat quality, hard deadline sufficiency for bounded jobs). Preliminary search; broader search recommended.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-1040_against.md

SYSTEMIC-RISK-FLAG: none (single item; no shared vulnerability established)

QUEUE SUMMARY: [SEARCHED-15b: 2026-10-05] PRESUMPTION-1040 — PARTIALLY-CHALLENGED, Weak; gray failure/heartbeat-as-proxy and hard-deadline sufficiency; false-positive sub-claim unsourced.
