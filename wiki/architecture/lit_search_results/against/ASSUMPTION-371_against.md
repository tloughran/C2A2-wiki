SEARCH-AGAINST-ASSUMPTION-371:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-371
  Original statement: "That launchd supervision makes the OpenStory backend durable and reboot-safe (the right durability posture)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-371
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: launchd supervision assumed to deliver durable, reboot-safe backend
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Reliability terminology (process liveness vs data durability). - A supervisor restarts a PROCESS; it does not guarantee that in-flight WRITES survived the crash. Conflating "restarts after crash" with "durable" overstates the guarantee.
    2. Distributed-systems availability literature (single point of failure). - A single supervised node is still a single point of failure: hardware failure, disk loss, or a crash-looping config defeats launchd entirely; "reboot-safe" != "available."
    3. Crash-consistency literature (see PRESUMPTION-405; SQLite atomic-commit docs). - Durability of state depends on the storage layer's crash-consistency, which supervision does not provide.

  Strength of challenge: Moderate

  Summary: launchd is the right tool for process liveness (15a), but the word "durable" smuggles in two guarantees it does not deliver. (1) Data durability: supervision does nothing for in-flight writes; if the storage layer is not crash-consistent, a supervised restart can come back to a corrupted/partial state. (2) Availability: a single supervised node remains a single point of failure - launchd cannot help against disk loss or a crash-loop. The posture is correct but should be stated narrowly as "single-node process liveness + reboot restart," not "durable."

  Specific risks: False confidence that "supervised" implies data safe; data loss/corruption on crash if storage is not crash-consistent; total outage on node/disk failure with no failover.

  Mitigations available: Pair supervision with crash-consistent writes (WAL/fsync; PRESUMPTION-405); periodic backups; for availability, plan replication/failover at the distributed step (PRESUMPTION-404).

  STEELMAN:
    Item: ASSUMPTION-371
    Strongest counterargument: Supervision answers "is the process running?" not "did my data survive and can I tolerate node loss?" Labeling it "durable and reboot-safe" conflates liveness with durability and availability, so the posture is right for what it covers and misleading for what it implies.
    What would need to be true for C2A2 to be safe: Storage is crash-consistent and backed up, and the single-node scope is explicit (no HA implied).
    How to test: SIGKILL mid-write, let launchd restart, run integrity_check + reconcile data; pull power/disk to confirm the (accepted) single-node failure boundary.

  Search scope: Liveness vs durability vs availability; supervision. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
