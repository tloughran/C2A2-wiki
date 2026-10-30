SEARCH-FOR-PRESUMPTION-1198:
  Date searched: 2026-10-30
  Original item: PRESUMPTION-1198
  Original statement: "[inferred] REVISE-534's remedy (run both copies side by side and compare outputs) presumes the two copies can run concurrently without contaminating each other. The scheduler's own verdict for all 27 double-registered tasks is that 'two concurrent passes overwrite each other's output', and that parallel state is what exists now. A shadow run is only a comparison if the shadow's writes are isolated (separate output paths or a dry-run mode). For 14a/14b the isolation is accidental: the cloud copy dates its changelog by UTC, the local by EDT, but both would append to the same shared registers."

  Claim tested (literature): Shadow/parallel-run and dark-launch practice requires isolating the side effects (writes) of the shadow system. When a shadow writes to shared state, it corrupts that state or invalidates the comparison.

  Reading used for the FOR direction: The item is a concern. "Support" means literature showing that shadow or parallel runs require isolating the shadow's side effects (separate stores, dry-run, write suppression, idempotency), and that shadows without isolation corrupt shared state or invalidate the comparison. In-house facts (27 double-registered tasks, UTC/EDT changelog dating, shared registers) are not judged.

  Search scope: PRELIMINARY. 2 web searches (standard), 0 fetches. Searched: GitHub Scientist and its ports (side-effect warnings); shadow traffic / dark launch / traffic mirroring write isolation. Not reached: Fowler ParallelChange / Strangler Fig; differential testing literature (McKeeman); peer-reviewed work on shadow deployment (e.g. Facebook/Google dark-launch papers); idempotency and concurrent-append race literature; batch-job "parallel run" practice in mainframe migration.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1198
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-29 local pass (final assistant message per session via session_info; no interactive session today). REVISE-534's side-by-side remedy names no write isolation; scheduler health says concurrent passes overwrite each other's output.
      15a: Searched for supporting literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15a — SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. InfoWorld (Paul Krill), "GitHub's Scientist puts Ruby rewrites to the test" (also syndicated at cio.de), [snippet only]. Year not in snippet. Quotes Jesse Toth (GitHub, Scientist author): Scientist "is not meant to be used for any code that has side effects. A candidate code path that writes to the same database as the control, invalidates a cache, or otherwise modifies data that affects the original, production..." Direct support: the tool's own author rules out comparison runs where the candidate writes to the control's store. URL: https://www.infoworld.com/article/2243579/githubs-scientist-puts-ruby-rewrites-to-the-test.html
    2. Laboratory (Python port of Scientist), PyPI documentation, [snippet only]. Author/year not in snippet. States that "any code with side effects, such as disk or database writes, or other state changes, are unsuitable as they'll lead to duplicated writes." Direct support: names duplicated writes as the failure mode. URL: https://pypi.python.org/pypi/laboratory
    3. Codementor, "Smarter, safer refactoring with Scientist" (author rlue per URL; year not in snippet), [snippet only]. Says the biggest gotcha is that Scientist focuses on return values, not side effects; offers a transaction-rollback workaround for database writes. Supports that write isolation must be added explicitly; it is not provided by the comparison mechanism. URL: https://codementor.io/@rlue/smarter-safer-refactoring-with-scientist-wdwbilti5
    4. Paleontologist (Deno port of Scientist), project listing, [snippet only]. Author/year not in snippet. FAQ says run order is not randomized because the functions "should not have side effects." Analogous support. URL: https://awesome.ecosyste.ms/projects/github.com%2Ftruewill%2Fpaleontologist
    5. Design Gurus, "How do you run shadow traffic and dark launches?", [snippet only]. Author/year not in snippet. Recommends routing mirrored calls to read-only replicas, sandbox topics, or stubbed external actions, and tagging shadow requests so database roles block mutations. Direct support for write isolation as standard practice. URL: https://www.designgurus.io/answers/detail/how-do-you-run-shadow-traffic-and-dark-launches
    6. techinterview.org, "Low Level Design: Shadow Mode Testing", [snippet only]. Author/year not in snippet. Suggests nullifying shadow writes or sending them to a shadow database, and routing events to a shadow topic. Direct support (separate output paths / dry-run analogue). URL: https://www.techinterview.org/post/3233473181/lld-shadow-mode-testing/
    7. F22 Labs, "Shadow testing: a beginner's guide" (and similar practitioner posts), [snippet only]. Author/year not in snippet. Notes mirrored requests can duplicate database writes and trigger emails unless the shadow environment is isolated. Supports the failure mode. URL: https://www.f22labs.com/blogs/shadow-testing-a-beginners-guide/
    8. Oteemo, "Using shadow release strategy", [snippet only]. Author/year not in snippet. States new services under shadow should not be able to modify database backends; recommends separate read replicas. Direct support. URL: https://oteemo.com/using-shadow-release-strategy/
    9. OneUptime, "How to Build Shadow Routing" (2026-01-30 per URL), [snippet only]. Author not in snippet. Says stateful systems need fully isolated state or only explicitly safe shared state, since shared caches/state make mirrored behavior diverge. Supports the "comparison invalidated" half of the claim. URL: https://oneuptime.com/blog/post/2026-01-30-shadow-routing/markdown

  Strength of support: Moderate

  Summary: Practitioner literature agrees that a shadow or candidate run must not write to the control's state. The Scientist library's author and its ports state this directly and name duplicated writes as the failure mode. Shadow-traffic guides list the same isolation tactics the item names: separate stores, write suppression (dry-run), and blocked mutations. One source also notes that shared state makes the shadow's behavior diverge, which undermines the comparison itself. The sources are consistent but are practitioner posts and tool docs, not peer-reviewed work.

  Caveats:
    - All sources are snippet-only; quotes and attributions were not verified by fetch.
    - Sources are mostly vendor, tutorial, and practitioner posts; no formal standard or peer-reviewed study was reached.
    - The literature concerns request-level shadowing of services and code paths. Two scheduled agent passes appending to shared markdown registers is an analogy, not a direct match.
    - The specific sub-claim that differing timestamp conventions (UTC vs EDT) provide only "accidental" isolation was not searched; no source addresses it.
    - The search engine summary blended sources; individual attribution of tactics to specific sites may be imprecise.

  Recommendation: SUPPORTED
