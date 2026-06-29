SEARCH-AGAINST-PRESUMPTION-412:
  Date searched: 2026-06-27
  Original item: PRESUMPTION-412
  Original statement: "That deferred pushes converge rather than accumulate - three sessions closed staged-not-pushed over an already-mixed working tree"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-412
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: repeated push deferral presumed to converge, not compound
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Continuous-integration evidence (Accelerate / DORA; trunk-based development). - Frequent integration reduces risk; deferring integration grows the divergence between local and shared state, raising merge-conflict and regression risk - integration debt ACCUMULATES, it does not converge.
    2. WIP-limits / batch-size theory (Lean/Kanban). - Large unmerged batches increase cycle time and defect risk superlinearly; three sessions stacked over an already-mixed tree is exactly a growing batch.
    3. "Merge hell" / long-lived-branch failure literature. - Long-lived divergent working state is a documented anti-pattern that compounds with each deferred integration.

  Strength of challenge: Moderate-Strong

  Summary: The presumption runs directly against the CI/DORA evidence base: deferring pushes does not converge, it accumulates integration debt, and stacking three staged-not-pushed sessions over an already-mixed tree maximizes the divergence the evidence warns about. This is the cross-session form of PRESUMPTION-402 (manual-staging vigilance, REVISE-148): the same correct-by-attention posture, now compounding across sessions.

  Specific risks: Merge conflicts/regressions on eventual push; loss or entanglement of WIP across three sessions; an already-mixed tree pushed with unintended files; growing, unreviewed divergence.

  Mitigations available: Enforce a push cadence / WIP limit (integrate per session); use worktree/branch isolation (already flagged in REVISE-148) so each session's changes are independently pushable; fail loud when unpushed sessions exceed a threshold.

  STEELMAN:
    Item: PRESUMPTION-412
    Strongest counterargument: Every deferred push widens the gap between local and shared history; the CI evidence is unambiguous that this gap compounds, so "it'll converge later" is the precise belief that produces merge hell - three stacked sessions over a mixed tree is integration debt accruing interest.
    What would need to be true for C2A2 to be safe: Deferrals are rare and short, each session is independently isolated/pushable, and an alarm fires when unpushed work accumulates.
    How to test: Track count/age of staged-not-pushed sessions and measure conflict/regression rate at eventual integration vs per-session pushes.

  Search scope: CI/DORA; WIP limits; batch size; long-lived branches. Comprehensive.

  Recommendation: CHALLENGED
