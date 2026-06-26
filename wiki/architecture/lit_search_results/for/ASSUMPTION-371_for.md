SEARCH-FOR-ASSUMPTION-371:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-371
  Original statement: "That launchd supervision makes the OpenStory backend durable and reboot-safe (the right durability posture)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-371
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: launchd supervision assumed to deliver durable, reboot-safe backend
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Apple launchd / launchd.plist documentation (KeepAlive, RunAtLoad). - launchd is the supported macOS supervisor: it restarts a crashed daemon and starts it at boot, which is exactly the process-liveness/reboot-restart posture claimed.
    2. systemd service supervision (Restart=, WantedBy boot targets) as the cross-platform analogue. - Process supervisors are the established, recommended pattern for restart-on-crash and start-on-boot of single-node services.
    3. Candea & Fox 2003, "Crash-Only Software." - Designing services to be safely killed and restarted by a supervisor is a validated reliability pattern; supervision + crash-only recovery is sound for liveness.

  Strength of support: Moderate

  Summary: Using launchd to supervise the backend is the correct, standard posture for single-node process liveness: it provides restart-on-crash and start-at-boot, the core of "reboot-safe" in the process sense, and aligns with the crash-only-software reliability pattern. Support is strong for the LIVENESS claim. It does not, by itself, establish DATA durability (in-flight writes surviving a crash) or high availability - those are separate guarantees addressed in the caveats and by 15b.

  Caveats: "Durable" must be split: supervision delivers process durability, not data durability (which requires crash-consistent writes - see PRESUMPTION-405) and not HA (single node remains a single point of failure - see PRESUMPTION-404).

  Search scope: launchd/systemd supervision; crash-only software. Adequate.

  Recommendation: SUPPORTED
