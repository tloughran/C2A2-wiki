SEARCH-FOR-PRESUMPTION-1208:
  Date searched: 2026-11-03
  Original item: PRESUMPTION-1208
  Original statement: Each copy of a duplicated task presumes its own outcome is the task's outcome. The local lit pipeline reported 'didn't run today' and 'anything queued is still waiting' without reading the lock log.
  Claim tested (literature lane): primary sources on replica-local versus global status reporting in redundant schedulers (split-brain observability; health checks reporting only the local node). The in-house limb (10-26..11-02 pair-by-pair report comparison) is NOT 15a/15b scope and was not run.
  Reading used for the FOR direction: the presumption is a real, documented failure pattern: an observer with a partial view reports its own view as the system's state, and no recovery or correction is triggered.
  Search scope: PRELIMINARY. 3 web searches, 1 fetch. One source (Huang et al. 2017) was read in part via fetch summary; all others are title/URL hits only, content NOT read. Not reached: Chandra & Toueg 1996 text, Kleppmann on leader election/fencing, Google SRE text on distributed cron, any LLM-agent scheduler source.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15a
    Original item: PRESUMPTION-1208
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: inferred from the local pipeline's 'did not run' report contradicted by the other copy's lock-log record
      15a: Searched for supporting literature (preliminary; 3 searches, 1 fetch)
    Current status: PARTIALLY-SUPPORTED
  Supporting evidence found: Partial
  Sources:
    1. Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M., Yao, R., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS XVI. https://www.microsoft.com/en-us/research/publication/gray-failure-achilles-heel-cloud-scale-systems/ [read via fetch summary of the PDF, not full text] - defines differential observability: the system's own observer reports healthy while an app experiences failure; many such failures are "only detectable in a distributed fashion", each component seeing a partial view. Closest primary match to a replica reporting its local state as the system state.
    2. Chandra, T.D., Toueg, S., 1996, "Unreliable Failure Detectors for Reliable Distributed Systems," JACM [from memory, not retrieved here] - failure detectors give each node only a local, possibly wrong, suspicion; global agreement needs extra protocol. Not read.
    3. techinterview.org, "Cron Service Low-Level Design: Distributed Scheduling, Exactly-Once Execution, and Missed Job Recovery" https://www.techinterview.org/post/3233469930/lld-cron-service/ [title only; secondary, non-primary] - indicates that duplicate/missed execution under replicated schedulers is a standard design concern.
    4. Railway forum, "Best practice for running cron jobs with multiple replicas" https://station.railway.com/questions/best-practice-for-running-cron-jobs-with-cf8aa83b [title only; practitioner thread] - practitioner evidence that multi-replica cron runs are a common source of ambiguity about which copy ran.
    5. HPE Morpheus community thread "Health in UI does not show overall status of 3 HA node cluster" https://community.hpe.com/t5/hpe-morpheus-enterprise/health-in-ui-does-not-show-overall-status-of-3-ha-node-cluster/m-p/7247472/highlight/true [title only; vendor forum] - a product whose health view reflects one node rather than the cluster.
  Strength of support: Moderate for the general pattern (one read source, directly on point); Weak for the scheduler-specific and LLM-agent claim
  Summary: The gray-failure paper establishes that an observer with a partial view can report healthy while the system is not, and that a single local observer cannot detect failures visible only across components. That is the structure of the presumption: each copy of the task reports its own outcome as the task's outcome. Practitioner threads suggest the same confusion occurs with replicated cron jobs and HA health views, but these were not read. Nothing found concerns LLM-agent schedulers or reporting 'did not run' from an absent local log.
  Caveats: Only one source read, and only as a summary; the others are title-only. The presumption's specific defect (not reading a shared lock log that was available) is a procedural lapse, not a distributed-systems observability limit, so the analogy is partial: the global view existed and was simply not consulted.
  Recommendation: PARTIALLY-SUPPORTED
