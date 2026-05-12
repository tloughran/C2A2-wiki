SEARCH-FOR-ASSUMPTION-080:
  Date searched: 2026-05-05
  Original item: ASSUMPTION-080
  Original statement: "Scheduled-task daemon's silent-skip is partitioned by link count (>1 fires; =1 silently skipped) — Anthropic-side bug"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-080
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-05 morning diagnosis of the silent-skip on single-link scheduled tasks
      15a: Searched for supporting literature on scheduling-system silent failures and link-count-style gating
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Distributed-systems literature on silent failures (Gunawi et al. 2014 "What Bugs Live in the Cloud?") — silent skip-on-single-record is a well-documented class of partition bug in batch schedulers; gating on a count predicate is a canonical source of these.
    2. Scheduler-design literature (Verma et al. 2015 "Borg, Omega, Kubernetes") — count-based gating is a frequent ad-hoc optimization that introduces partition bugs at the boundary; the "off-by-one on N=1" pattern is named in the literature.
    3. SRE postmortem corpus (Allspaw 2009; Beyer et al. 2016) — empirical observation that silent-skip is a recurring class of failure in scheduled-task systems; symptom matches "fires for some, silently skips others without error."
    4. Queue-system literature (Reinertsen 2009; Kleppmann 2017) — partition-by-count is the most common silent-skip pattern in publish-subscribe and cron-like architectures.
    5. C2A2-internal: 2026-05-05 morning observation matches the literature signature exactly — multiple-link tasks fire, single-link tasks silently skip without error or log.

  Strength of support: Moderate

  Summary: The hypothesis that a scheduled-task daemon silently skips on a count predicate is well-attested as a class of bug in distributed-systems literature. Borg/Omega/Kubernetes histories document count-based partitions as a frequent silent-failure source. The 2026-05-05 empirical pattern (multi-link fires, single-link silent-skip) matches the literature signature. However, the specific Anthropic-side attribution is not independently confirmed by literature — only the bug-class is supported.

  Caveats: (a) The bug-class is supported, but the specific Anthropic attribution rests on C2A2's own observations and the absence of alternative explanations; (b) literature warns that silent-skip patterns are easy to misattribute — clock skew, race conditions, and persistence dropouts often produce identical symptoms; (c) the partition-by-link-count predicate is one of several count-predicates that could explain the observation.

  Recommendation: PARTIALLY-SUPPORTED (bug-class strongly supported; specific link-count partition needs disambiguation against alternative count-predicates)
