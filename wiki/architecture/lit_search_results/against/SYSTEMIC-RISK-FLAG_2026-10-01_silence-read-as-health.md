SYSTEMIC-RISK-FLAG:
  Date: 2026-10-01
  Raised by: 15b (Literature Search AGAINST), scheduled run
  Affected items: PRESUMPTION-1099, PRESUMPTION-1100, PRESUMPTION-1102 (core); PRESUMPTION-1101 (partial)
  Level: High

  Shared vulnerability: Silence and last-written records are read as positive evidence of health. No component asserts liveness or outcome positively and independently.
    - 1099: no alarm from a surface's own monitor is read as "the whole fleet is fine," though that monitor cannot see the other surface.
    - 1100: the last line written is read as current state; a missing line is read as "did not fire."
    - 1102: a clean exit that found nothing is read as success; a long streak of no-ops is not questioned.
    - 1101 (partial): the designer's silence is read as "keep deferring" rather than as a signal to change mode.

  Why it matters: These errors stack. A dead task writes nothing (1099), a stale status line still says PASS (1100), any surviving runs report clean no-op success (1102), and every open question is re-flagged to an absent designer (1101). The system can look healthy for days while doing nothing useful. This matches the 09-30 symptoms: ten weekly agents silent with no alarm, conflicting pending counts, 15 no-op batches, disks full.

  Supporting literature (see item files for fetch levels):
    - Huang et al. 2017, "Gray Failure" (differential observability).
    - Grafana Labs 2021, meta-monitoring with dead-man's switch.
    - Fowler 2005, "Event Sourcing" (log vs state).
    - mrveiss 2026, AutoBot-AI issue #17726 ("found nothing" vs "did not run" must stay separable).
    - Deng 2026, "Goal-Autopilot" (vacuous success on exit_code==0).
    - trackrat #1826 (disk full silenced the disk alert: no data, no alert).

  Common mitigation: One independent liveness and outcome ledger. Every run, on any surface, appends a line (task, run ID, surface, time, outcome, items processed). One external checker compares this ledger to the expected-task manifest and alerts on absence, staleness, long no-op streaks, and conflicting writers. The checker itself has a dead-man's switch.
