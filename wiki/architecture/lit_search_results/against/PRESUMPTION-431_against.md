SEARCH-AGAINST-PRESUMPTION-431:
  Date searched: 2026-07-01
  Original item: PRESUMPTION-431
  Original statement: "[inferred] That the recurring stale git index.lock is benign routine noise rather than a concurrency symptom (heartbeat cron vs attended commits)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-431
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from repeated stale-lock observations
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Git lock documentation / dev.to "Fixing Common Git Lock Errors" — .git/index.lock exists specifically to prevent corruption when two git writes run together; RECURRING stale locks mean two git processes are actually racing (scripts/CI/cron vs interactive), i.e., a concurrency symptom, not noise.
    2. Claude Code issue tracker (anthropics/claude-code #11005, #57102, #47721) — background/cron git operations create stale index.lock that block user git; the documented remedy is GIT_OPTIONAL_LOCKS=0 / --no-optional-locks for background reads and serializing writers. This is a recognized concurrency defect, not routine.
    3. Corruption escalation — "repeated lock errors plus other failures (ref missing, index corruption) suggest" real trouble; run git fsck. Recurrence is the warning sign, not the all-clear.

  Strength of challenge: Strong

  Summary: The git literature reads recurring stale index.lock as a concurrency symptom: a heartbeat cron running git writes/status concurrently with attended commits is exactly the race the lock guards against. Treating recurrence as benign noise ignores the documented escalation path to index/ref corruption. There is a concrete, recognized cause and fix.

  Specific risks: Concurrent git writers eventually interleave into index/ref corruption; attended commits fail or are silently blocked; a cron-vs-interactive race corrupts the repo state the whole C2A2 pipeline reads from.

  Mitigations available: Serialize git access (a repo-level lock/queue around commits), and set GIT_OPTIONAL_LOCKS=0 / --no-optional-locks for the heartbeat cron's read-only git; run git fsck to check for existing damage.

  STEELMAN:
    Item: PRESUMPTION-431
    Strongest counterargument: If the stale locks only ever appear from read-only git status races (never from concurrent writes), they are genuinely low-consequence and the fix is trivial (--no-optional-locks) — so the "benign" read is defensible for the read-only subset, just not for the write-vs-write case.
    What would need to be true for C2A2 to be safe: Establish that no two git WRITERS ever run concurrently (only read races remain), and apply --no-optional-locks to background reads.
    How to test: Log git invocations with timestamps; check for overlapping write operations (commit/add/pull) between cron and interactive sessions.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-07-01
    Affected items: ASSUMPTION-394, PRESUMPTION-426, PRESUMPTION-430 (measurement-validity / structural-proxy-as-ground-truth); ASSUMPTION-393, PRESUMPTION-425, PRESUMPTION-427 (one-shot-fix-as-durable-solution); PRESUMPTION-429, PRESUMPTION-431 (verification/observability independence)
    Common vulnerability: Two recurring root patterns in this cohort. (1) MEASUREMENT VALIDITY: substituting an easily-measured structural/aggregate proxy (count-match, connectome size, structural green) for the actual quality property it stands in for — a continuation of the 2026-06-29 connectivity-as-proxy / signals-per-day cluster (P-414, A-388/P-419). (2) ONE-SHOT-AS-DURABLE: treating a single action (attended clear, one bug fix) as a class/durable solution without process change — a continuation of the push-debt cluster (REVISE-150/159).
    Literature basis: Goodhart's law (proxy gaming); defect clustering / pesticide paradox; ETL count/checksum insufficiency; Lean backlog re-accumulation; N-version common-mode-failure.
    Risk level: High
    Recommendation: Institute (a) identity/semantic verification alongside every structural/count check; (b) a process/cadence decision paired with every one-shot remediation; and (c) preserve independent cross-checks (do not collapse complementary views). These are three concrete, cheap disciplines that neutralize the whole cluster.

  Recommendation: CHALLENGED (Strong — recurring stale locks are a documented concurrency symptom with a concrete fix, not benign noise)
