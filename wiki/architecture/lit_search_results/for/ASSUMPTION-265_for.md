SEARCH-FOR-ASSUMPTION-265:
  Date searched: 2026-06-02
  Original item: ASSUMPTION-265
  Original statement: The daily-run git phase must verify version-control health each run rather than infer it from no-error — a stale `.git/index.lock` from a crashed process can silently block all staging with no surfaced error (here: 2026-05-29 → 2026-06-02).

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-265
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from a realized 4-day silent git-staging outage (stale index.lock).
      15a: Searched silent-failure / fail-loud design, pre-flight integrity checks, read-after-write verification, and lock-file hazards.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Safety vs liveness properties (Hillel Wayne, "Safety and Liveness Properties"; Lamport). — "No error" is at best a weak safety signal; that the intended effect EVENTUALLY occurred (staging happened) is a liveness property that absence-of-error does not establish. Directly supports verifying the effect, not inferring it from no-error.
    2. Read-after-write / verify-the-side-effect (read-your-writes consistency; same family as PREMISE-045). — Confirm the write took effect by reading committed state; a `git status`/index check after staging is exactly this pattern.
    3. Fail-loud-on-violation + pre-flight integrity checks (OpenAI Sandbox Agents fail-loud, cited validated_premises ~line 1020; lock-file hazard practice). — A stale lock from a crashed process is a known automation hazard; surfacing it via an explicit health check is canonical fail-loud.

  Strength of support: Strong

  Summary: The assumption is strongly supported and empirically realized: a stale `.git/index.lock` silently blocked all staging for ~4 days with no surfaced error. "No error" is a weak safety signal that does not establish the desired liveness property (changes actually staged/tracked); the established remedy is to verify the side effect (read-after-write / pre-flight integrity check) and fail loud on a detected lock or dirty/unexpected state. Same fail-loud/verify-the-effect family as PREMISE-045 (ASSUMPTION-264).

  Caveats: 15b notes pre-flight checks can be over-engineering for low-frequency pipelines — but that objection is undercut here because the silent failure actually occurred and persisted 4 days.

  Recommendation: SUPPORTED
