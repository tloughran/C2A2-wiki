SEARCH-AGAINST-PRESUMPTION-1198:
  Date searched: 2026-10-30
  Original item: PRESUMPTION-1198
  Original statement: "[inferred] REVISE-534's remedy (run both copies side by side and compare outputs) presumes the two copies can run concurrently without contaminating each other. The scheduler's own verdict for all 27 double-registered tasks is that 'two concurrent passes overwrite each other's output', and that parallel state is what exists now. A shadow run is only a comparison if the shadow's writes are isolated (separate output paths or a dry-run mode). For 14a/14b the isolation is accidental: the cloud copy dates its changelog by UTC, the local by EDT, but both would append to the same shared registers."

  Claim tested (literature): Shadow/parallel-run and dark-launch practice: requirement to isolate side effects (writes) of the shadow system; failure modes when shadow writes to shared state.

  Reading used for the AGAINST direction: The presumption is that two copies of a scheduled agent task can run side by side for comparison without explicit write isolation, and the comparison stays valid. AGAINST = evidence that un-isolated shadow writes corrupt shared state or invalidate the comparison. For balance, also looked for conditions under which isolation is not needed (read-only shadow, serialized runs, append-only/idempotent stores).

  Search scope: PRELIMINARY. 2 web searches (standard), 0 fetches. Searched: (1) GitHub Scientist guidance on candidate side effects / database writes; (2) shadow traffic and dark-launch practice on isolating writes to shared databases. Not reached: lost-update / write-write conflict literature for concurrent file appends; dual-write problem (e.g. outbox pattern) literature; append-only / CRDT / idempotent-store literature that might weaken the worry; lock-based mutual exclusion for cron/scheduled jobs; any peer-reviewed source.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1198
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-29 local pass (final assistant message per session via session_info; no interactive session today). REVISE-534's side-by-side remedy names no write isolation; scheduler health says concurrent passes overwrite each other's output.
      15b: Searched for challenging literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15b — CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. scientist (JavaScript port of GitHub Scientist), README on npmjs.com, https://npmjs.com/package/scientist [snippet only]. Author/year not in snippet. States the candidate must never permanently change external state, with a database update as the example. Directly contradicts running a candidate copy that writes to shared state.
    2. InfoWorld, "GitHub's Scientist puts Ruby rewrites to the test" (byline shown as Paul Krill; year not in snippet), https://www.infoworld.com/article/2243579/githubs-scientist-puts-ruby-rewrites-to-the-test.html [snippet only]. Quotes the Scientist author (Toth) saying the tool is not meant for code with side effects. The quote on database writes is cut off in the snippet.
    3. laboratory (Python port), PyPI, https://pypi.org/project/laboratory/0.1.0/ [snippet only]. Always returns the control's result. This limits user-facing risk only; it does nothing about the candidate's side effects. Shows the side-by-side pattern assumes the candidate is side-effect free.
    4. DesignGurus, "How do you run shadow traffic and dark launches?", https://www.designgurus.io/answers/detail/how-do-you-run-shadow-traffic-and-dark-launches [snippet only]. Author/year not in snippet. Warns mirrored requests can duplicate database writes and trigger external effects unless the shadow is carefully isolated. Recommends read-only routing, sandbox topics, and mutation-blocking DB roles.
    5. techinterview.org, "Low Level Design: Shadow Mode Testing", https://www.techinterview.org/post/3233473181/lld-shadow-mode-testing/ ; DZone, "How To Use Shadow Testing To Reduce the Risk of Production Issues", https://dzone.com/articles/how-to-use-shadow-testing-to-reduce-the-risk-of-pr ; oneuptime.com dark-launch patterns (2026-01-30 per URL) [all snippet only]. Authors not in snippet. Together suggest shadow database, read replicas, or no-op'd writes; compare logged outputs offline keyed by a shared request ID. Isolation is treated as a precondition, not an option.
    Balance (weakens the worry): Source 4/5 snippets note isolation can be achieved by making the shadow read-only, and comparison done offline from logs. Source 5's dark-launch example writes to both stores but reads only from the old one, so a dual write is tolerated when the copy under test is never the source of truth. No source found (not searched) on append-only or serialized runs making isolation unnecessary.

  Strength of challenge: Moderate

  Summary: Practitioner guidance on side-by-side experiments is consistent: the candidate or shadow must not change shared state. GitHub Scientist and its ports say this outright, with a database write as the example. Shadow-traffic guidance treats write isolation (read-only routing, shadow DB, no-op writes) as a precondition of a valid comparison. This challenges the presumption that REVISE-534's side-by-side run is safe without explicit isolation. Strength is Moderate, not Strong, because all sources are snippets from READMEs, blogs and interview-prep pages, and none addresses file-based registers or scheduled agents directly.

  Specific risks: If the 14a and 14b copies both append to the same shared registers, each copy's output is mixed into the other's input. The comparison then measures a contaminated pair, not two independent runs. Duplicate entries can enter the registers (the analogue of duplicated DB writes). Overlapping appends or read-modify-write cycles can lose entries (lost update). The UTC vs EDT changelog dating separates only the changelog naming; it does not isolate register writes, so the isolation is partial and accidental.

  Mitigations available: Run the shadow copy in a dry-run / read-only mode. Point the shadow at separate output paths or a sandbox copy of the registers. Serialize the two copies with a run lock (as lit_pipeline_lock.sh does for the lit pipeline), noting that serialization prevents clobbering but not cross-contamination of inputs. Compare outputs offline from logs keyed by run ID. Tag every register entry with the writing copy so mixed entries can be separated after the fact.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-1198
    Strongest counterargument: The shadow-traffic literature is about live request mirroring under real concurrency, where writes collide within milliseconds. Scheduled agent passes are coarse, run minutes or hours apart, and may in practice never overlap. If the registers are append-only and each entry is tagged with its source copy (UTC vs EDT stamps may already act as that tag), then both copies' outputs can be recovered and compared after the fact. Dual-write during migration, reading only from the old system, is an accepted pattern. On this reading the comparison is still valid, if messier.
    What would need to be true for C2A2 to be safe: The two copies never run at the same time, or a lock enforces this. Every register write is a pure append, never a read-modify-write or overwrite. Each entry carries an unambiguous source tag. Neither copy reads the other's entries as input during the comparison window.
    How to test: Check the scheduler logs for overlapping start/end times of 14a and 14b. Inspect the shared registers for duplicate or missing entries after a day when both ran. Diff the registers before and after each pass to confirm writes are append-only. Check whether 14b's input on a given day includes entries written by 14a that same day.

  SYSTEMIC-RISK note: Yes. This shares the "concurrent double-registered tasks overwriting output" vulnerability: the remedy (side-by-side comparison) relies on the same unisolated shared state that caused the problem. It also echoes "a named check treated as a check performed", since a "comparison" that reads contaminated outputs would look like a check without being one.
