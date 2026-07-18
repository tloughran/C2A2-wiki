SEARCH-FOR-PRESUMPTION-491:
  Date searched: 2026-07-18
  Original item: PRESUMPTION-491
  Original statement: [inferred] An agent presumes a scheduled job firing implies its intended effect occurred ("ran on schedule" ≡ "succeeded"); the morning status called OpenStory "refreshed on schedule" while the db has been unwritten since 07-05.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-491
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption (scheduler-fired equated with succeeded)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Kubernetes docs, "Configure Liveness, Readiness and Startup Probes." — Formalizes that "process is alive / started" (liveness) is a distinct signal from "did the intended work / is usable" (readiness); a fired job that is merely alive is not certified to have succeeded.
    2. oneuptime, 2026. "Health Checks That Distinguish Between Liveness and Readiness." — Argues explicitly that liveness ≠ correctness; end-to-end/artifact-level verification is needed to claim success. Maps directly to "scheduler fired" vs "db actually written."
    3. Red Hat Developer, "You (probably) need liveness and readiness probes." — Reinforces the two-signal model and the danger of treating one as the other.

  Strength of support: Strong

  Summary: The presumption identifies a well-known category error, and the literature strongly supports its being an error: "the job fired / process is up" (liveness) must not be read as "the intended effect occurred" (readiness/correctness). The correct practice is to bind a success claim to an artifact-level check — here, the OpenStory db's mtime / last-write / row-delta — not to the scheduler having fired. The morning "refreshed on schedule" claim over a db unwritten since 07-05 is exactly the failure the liveness/readiness distinction guards against.

  Caveats: The Kubernetes framing is for long-running services; for one-shot scheduled jobs the analogue is exit-code + artifact verification rather than a readiness endpoint, but the underlying "fired ≠ succeeded" principle transfers cleanly.

  Recommendation: SUPPORTED
