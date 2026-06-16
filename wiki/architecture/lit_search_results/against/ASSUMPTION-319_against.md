SEARCH-AGAINST-ASSUMPTION-319:
  Date searched: 2026-06-16
  Original item: ASSUMPTION-319
  Original statement: "git history of traditions/*/prs_triplets.md yields valid 'triplet-completed' dates (PRS-NN per commit-day)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-319
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-15 session (event-dating from VCS)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Committer-vs-author date divergence ("Teaching Mining Software Repositories," Palomba/Verdecchia 2025; "Does the Tool Matter?" arXiv:2501.15114). — Git records TWO dates and rewriting history (rebase, squash, amend) changes the commit date; tools that bin by committer date vs author date produce SHIFTED time-series peaks at interval boundaries. So "the commit-day" is not a single well-defined fact, and the choice of which date silently moves events across day boundaries.
    2. Batch/backfill and quick-remedy commits ("Quick remedy commits and their impact on MSR," PMC8553712; commit-frequency studies). — When prs_triplets.md is edited in periodic batches (several triplets committed together, or backfilled after the fact), the commit-day reflects the WRITING-DOWN day, not the completion day, collapsing many real completion events onto one date and emptying the days they actually occurred. This is highly likely for a curated markdown ledger maintained alongside other work.
    3. Conclusion (in-)stability in empirical SE (arXiv:2510.06844). — Quantitative findings mined from repositories are sensitive to such methodological choices; small changes in timestamp handling can change the resulting series materially, so a single naive extraction is fragile.

  Strength of challenge: Moderate

  Summary: The method is valid in principle but the specific claim — that prs_triplets.md commit history yields VALID per-day completion dates — is challenged by well-documented MSR temporal-validity threats. The committer/author date ambiguity can shift events across day boundaries; batch commits and backfill of a curated ledger systematically map completion events onto the day they were transcribed rather than achieved; and history rewriting can move dates. For a hand-maintained markdown file these threats are not edge cases — they are the expected pattern, since people rarely commit each triplet at its moment of completion.

  Specific risks: The Metabolism timeline shows spikes on ledger-update days and false zeros on real-work days; if the user reads cadence/rhythm off this, they read their COMMITTING habit, not their completing habit. Backfilled history (a batch of triplets entered in one sitting) appears as a single burst of "productivity," distorting any trend or correlation built on the series.

  Mitigations available: Audit prs_triplets.md history for batch/backfill signatures (many PRS-NN added in one commit; long quiet stretches then bursts); prefer author-date over committer-date and state the choice; where completion dates matter, record an explicit completion-date field IN the triplet rather than inferring from commit metadata; flag/annotate commits that add many triplets at once as low-temporal-confidence.

  STEELMAN:
    Strongest counterargument: At the coarse daily/weekly resolution of a personal metabolism view, and if the user's actual habit is to commit prs_triplets.md soon after completing each triplet, commit-day is a good-enough proxy — MSR uses commit timestamps for exactly this kind of daily-rhythm reconstruction, and outlier/invalid timestamps are rare. The threat is real only to the extent batching/backfill actually occurs, which is an empirical question about this one file's history.
    What would need to be true for C2A2 to be safe: The commit pattern for prs_triplets.md would need to be predominantly single-triplet, near-real-time commits (not batches/backfill), and a consistent date choice (author vs committer) would need to be fixed.
    How to test: Run the batch/backfill audit above on the actual file history; if >~20% of triplets arrive in multi-triplet batch commits, the completion-date inference is materially distorted and an explicit completion-date field is needed.

  Search scope: MSR temporal-validity threats, committer/author date semantics, batch/backfill and quick-remedy commits, conclusion instability. Comprehensive. (Couples PRESUMPTION-350.)

  Recommendation: PARTIALLY-CHALLENGED
