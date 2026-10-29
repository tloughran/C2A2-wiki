SEARCH-FOR-PRESUMPTION-1196:
  Date searched: 2026-10-29
  Original item: PRESUMPTION-1196
  Original statement: "[inferred] The double-registration fix ('confirm the cloud trigger fires before disabling the local entry') presumes the cloud and local copies of a task are equivalent once both fire. They are not: the cloud 14a/14b copy fires nightly but lacks session_info and has NO-OP'd since 10-24, while the local scheduler-health copy lacks the Routines connector that the cloud side has. 'Fires' is the only parity test named; tool parity is not. Following the rule as written would disable the only 14a/14b path that reads transcripts."

  Claim tested (literature): Verifying a migration cutover beyond liveness. This covers capability and feature-parity checks, and shadow-run comparison of outputs (dark launching, parallel run). Does "trigger fired" suffice as a cutover criterion?

  Reading used for the FOR direction: the item is a concern, so support means literature showing that (a) liveness alone (the new path runs or fires) is not an accepted cutover criterion, and (b) standard practice is to check capability or feature parity and compare outputs between the old and new paths before retiring the old one. 15a does not judge whether the cloud copy in fact lacks session_info, whether it has NO-OP'd since 10-24, or whether the local copy lacks the Routines connector.

  Search scope: PRELIMINARY. 2 web searches (standard), 0 fetches. Searched: migration cutover with parallel run and shadow traffic, output comparison and feature parity before decommissioning; GitHub Scientist and dark-launch refactoring. Not reached: Fowler's ParallelChange and StranglerFig bliki entries; Google SRE book chapters on launch and canarying; Kubernetes readiness versus liveness probe documentation; academic work on back-to-back testing, N-version comparison and differential testing; peer-reviewed migration case studies. The second search's health-check/liveness terms returned nothing on liveness probes. Every hit was about Scientist.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1196
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-10-28 local pass (final assistant message per session via session_info; no interactive session that day). The double-registration fix names only "fires" as its parity test. The cloud and local copies differ in available tools (session_info, Routines connector).
      15a: Searched for supporting literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15a — SUPPORTED

  Supporting evidence found: Yes, for (a) and (b) as practice. The sources are mainly practitioner and vendor material plus one widely used open-source tool. No peer-reviewed source was reached.

  Sources:
    1. GitHub Engineering blog, "Scientist: Measure Twice, Cut Once" (github.blog, dated 2015-02-17 in URL; author not shown in snippet), and the github/scientist repository; InfoWorld coverage by Paul Krill, "GitHub's Scientist puts Ruby rewrites to the test" (year not in snippet). [snippet only]. Scientist sends production calls to both the old and new code paths, compares the results and records mismatches, and returns only the old path's result. The new path is activated only once comparison shows it behaves correctly. InfoWorld reports it was used for a multi-year rewrite of permission code and a switch to a new code-search cluster. Ports exist for Python (Laboratory), JavaScript and .NET. Relevance: direct support for (b). The established pattern gates cutover on output equivalence, not on whether the new path executes. The .NET port's docs add a caveat that comparison has a cost: the calling method can slow down.
    2. Gravitee, "Parallel Run Migrations: Cut Over Without Downtime", "Migration basics: how to plan a safe cutover" and "API Migration Validation: A Practical Guide" (gravitee.io; authors and dates not in snippet). [snippet only; vendor]. Lists blue/green, canary and shadowing as cutover patterns. Shadow traffic lets teams compare the two implementations before switching. Says parity checks should go beyond payloads to response codes, headers, timeouts, pagination, idempotency and error semantics. Relevance: support for (b). Parity is defined over behaviour and capability, not over reachability.
    3. Digiqt, "Parallel run core migration validation" (digiqt.com; author and date not in snippet), and a DEV Community post on running two ACH payment stacks in parallel during a shadow-traffic migration (dev.to; author shown only as a handle, date not in snippet). [snippet only; practitioner]. Recommends measurable exit gates set in advance, e.g. zero functional discrepancies for five consecutive business days, and states that "it looks fine" is not an exit criterion. Keeps the legacy system as the reference until owners sign off. The payments team compared outputs on every transaction for about two weeks and made the comparison gate a hard block on cutover. Relevance: direct support for (a). Practitioners explicitly reject impressionistic or liveness-only criteria, and the old path is kept until output parity is shown.
    4. Supplementary, same search (InfoQ, "Shadow table strategy for data migration"; TestDevLab, legacy-modernization QA migration checklist; techinterview.org, "Shadow Mode Testing"; authors and dates not in snippets). [snippet only]. Further practitioner descriptions of shadow and parallel validation before decommissioning. Relevance: corroborates that the pattern is common practice. Not individually assessed.

  Strength of support: Moderate. The practice is consistent across sources and well established (Scientist is a long-standing tool used at scale). The evidence base reached is practitioner and vendor material, not peer-reviewed.

  Summary: Every source found treats retiring a legacy path as conditional on demonstrated parity of outputs and behaviour, not on the replacement merely running. GitHub's Scientist is the clearest example: both paths run, results are compared, and the old path stays authoritative until mismatches are resolved. Migration guides list capability dimensions beyond the payload that must match, and they demand measurable, pre-set exit gates while rejecting "it looks fine" as a criterion. On this reading, "the trigger fires" is a liveness check, and the literature does not treat it as a sufficient cutover criterion. That supports the item's concern that a fires-only rule could retire the more capable path.

  Caveats:
    - The literature reached mostly concerns request/response services and data pipelines, where outputs can be diffed directly. Scheduled LLM agent tasks whose outputs are non-deterministic prose are harder to compare. Parity there may have to be judged at the level of tools or capabilities, not outputs. No source addresses that case directly.
    - The item's specific gap is tool or connector availability that differs between two execution environments of the same task. The sources discuss behavioural parity in general. They do not discuss environment capability inventories as a distinct check.
    - One source warns that a successful parallel run can reproduce a legacy bug, so parity shows equivalence, not correctness. This is a limit on the remedy, not on the concern.
    - All sources are [snippet only]. Most are vendor or practitioner blogs, and publication bias toward success stories is likely.
    - Liveness-versus-readiness probe literature (e.g., Kubernetes) was not reached. It would bear on (a) directly.

  Recommendation: SUPPORTED

  NOVELTY-FLAG (weak, provisional):
    Item: PRESUMPTION-1196
    Searched: migration cutover and parallel-run parity; Scientist and dark-launch output comparison (2 searches)
    Finding: No literature found on cutover verification for scheduled AI agent tasks where the two copies differ in the tools or connectors available to them, so that each "fires" but neither can do the other's job.
    Implication: possibly an under-described failure mode for agent-task migration. Capability parity is a precondition separate from output parity, and it matters where outputs are non-deterministic. The general principle (liveness is not parity) is well known.
    Recommended status: retain as SUPPORTED; NOVEL only for the agent tool-parity framing, pending a broader search.
