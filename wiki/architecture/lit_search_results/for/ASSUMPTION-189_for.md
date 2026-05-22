SEARCH-FOR-ASSUMPTION-189:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-189
  Original statement: "Recurring index.lock + 716/356 morass caused by colliding/silently-failing scheduled commit agents."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-189
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: recurring index.lock and 716/356 staging morass diagnosed as concurrent scheduled commit agents colliding.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Chacon, S. & Straub, B. "Pro Git." — Git takes index.lock to serialize index modification; two processes touching the index concurrently is the textbook cause of index.lock contention.
    2. Lamport, L. (1978). "Time, Clocks, and the Ordering of Events." — Concurrent uncoordinated writers to shared state produce race conditions; serialization (mutual exclusion) is the remedy.
    3. cron + flock best practice (util-linux flock(1)). — The standard fix for overlapping scheduled jobs touching shared state is an exclusive lock; its absence is a known anti-pattern.

  Strength of support: Strong

  Summary: The mechanism — concurrent scheduled commit agents colliding on the git index — is strongly supported as a plausible and common root cause of recurring index.lock and a confused staging state. Git's locking model and decades of cron-serialization practice make uncoordinated concurrent writers the leading hypothesis. The premise correctly identifies a real failure mode.

  Caveats: Strong support that this is A cause; not proof it is THE cause (15b lists credible alternatives that produce the same symptom).

  Recommendation: SUPPORTED (mechanism plausible and common)
