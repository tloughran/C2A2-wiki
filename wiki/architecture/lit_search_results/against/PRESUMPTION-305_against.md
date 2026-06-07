SEARCH-AGAINST-PRESUMPTION-305:
  Date searched: 2026-06-05
  Original item: PRESUMPTION-305
  Original statement: [inferred] Accumulating uncommitted working-tree state is cost-free — 587 changes (up from 476) on feature/sociogram-search-integration, each unattended run adding to the pile under the no-blind-push rule, presuming a future attended session cleanly separates and commits them.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-305
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated presumption that accumulating uncommitted working-tree state is cost-free and cleanly separable later.
      15b: Searched long-lived-branch divergence, merge cost, and working-tree/WIP accumulation risk.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Atlassian, "Trunk-Based Development." — Long-lived divergence from trunk raises a higher risk of conflicting updates and progressively harder merges; the longer state is held unmerged, the greater the divergence, technical debt, and bug/deployment risk. Directly contradicts "cost-free accumulation."
    2. StxNext, "Escape from Merge Hell"; trunkbaseddevelopment.com, "Short-Lived Feature Branches." — A branch held beyond ~2 days is flagged as the antithesis of healthy practice; merge difficulty grows super-linearly with divergence. 587 accumulated changes across many unattended runs is far past that threshold.
    3. WIP/inventory lean principle (SAFe Principle #6; cf. 15a's own batch sources). — Uncommitted changes are unreleased inventory: WIP that carries holding cost (risk of loss, conflict, and forgotten rationale) and hides defects until integration. "Each unattended run adding to the pile" is monotonically growing WIP, which lean treats as a cost to minimize, not a free buffer.

  Strength of challenge: Strong

  Summary: The presumption that accumulating uncommitted working-tree state is cost-free is strongly challenged and essentially unsupported (15a found no real FOR case). Version-control and lean literature converge: unmerged/uncommitted divergence carries holding cost that grows with size and time — harder merges, conflict risk, accumulating technical debt, and lost rationale ("clean separation later" gets harder, not easier, as the author forgets which change served which purpose). The "future attended session cleanly separates 587 changes" assumption is precisely the bet the merge-hell literature says fails: separability degrades as the pile grows and context decays. Each unattended run silently raises the eventual reconciliation cost while the no-blind-push rule (sound in itself) is mis-applied to justify not COMMITTING rather than merely not PUSHING.

  Specific risks: A future attended session faces 587+ intermingled changes spanning unrelated concerns, making clean separation error-prone or impractical; worst case the branch becomes effectively un-mergeable / gets force-reconciled, sweeping unrelated changes together — the exact harm ASSUMPTION-272 wanted to avoid, now realized at the repo level. Risk grows every run.

  Mitigations available: Decouple the two actions the presumption conflates: keep the no-blind-PUSH safety rule, but COMMIT frequently in small, scoped, local commits each run (committing is not pushing). This bounds working-tree growth, preserves per-change rationale, and makes the eventual attended push a review of coherent commits rather than a 587-change untangling.

  STEELMAN:
    Item: PRESUMPTION-305
    Strongest counterargument: "Cost-free" is the most dangerous word here. Uncommitted working-tree state is unreleased inventory whose cost is invisible right up until integration, when it lands all at once as merge conflicts, lost rationale, and un-separable changes. The no-blind-push rule is being stretched to excuse unbounded WIP growth, but it only ever justified deferring the network push — it never justified refusing to commit. Every unattended run that adds to the pile is borrowing against a future attended session whose untangling cost grows super-linearly; presuming that session will "cleanly separate" hundreds of intermingled changes is exactly the optimism merge-hell is made of.
    What would need to be true for C2A2 to be safe: Either the working tree is committed in small scoped increments each run (bounding accumulation), OR the eventual attended session is guaranteed near-term AND the changes are genuinely independent and few. The current trajectory (587 and rising, many runs) satisfies none of these.
    How to test: Measure merge/separation effort as a function of accumulated change count on a dry-run reconciliation; confirm whether 587 intermingled changes can be cleanly partitioned by concern, or whether rationale has already decayed past clean separation.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-06-05
    Affected items: PRESUMPTION-303, PRESUMPTION-304, PRESUMPTION-305 (and coupled ASSUMPTION-271)
    Common vulnerability: A shared "defer-and-tidy-later" optimism — admit-now/review-later (303), reconcile-later (304), commit-later (305) — each presuming a future attended session will cleanly resolve accumulated, unverified, or intermingled state at no extra cost. The literature on staging-queue rot, silent data loss, and merge-hell independently shows deferral cost grows with accumulation and the cleanup sometimes never happens.
    Literature basis: Agile backlog-refinement & maintenance-backlog cost-inflation studies (303/304); ETL reconciliation / silent-data-loss guidance (304); trunk-based-development merge-hell & lean WIP (305).
    Risk level: High
    Recommendation: Treat "later attended cleanup" as a cost-bearing liability that accrues every unattended run, not a free option. Adopt bounded-accumulation defaults system-wide: enforce provisional-item adjudication deadlines (303), reconcile counts at detection rather than deferral (304), and commit-in-increments while deferring only the push (305). Surface the growing backlog/working-tree/queue size as a tracked metric so the silent accrual becomes visible.

  Recommendation: CHALLENGED
