# Lit pipeline run (2026-11-08, cloud, scheduled)

**Outcome:** 4 literature-lane items searched (15a, 15b) and dispositioned (15c), all MONITOR.
- ASSUMPTION-2061 -> DISPOSITION-1121 -> MONITOR-706 (Medium)
- PRESUMPTION-1222 -> DISPOSITION-1122 -> MONITOR-707 (Medium)
- PRESUMPTION-1224 -> DISPOSITION-1123 -> MONITOR-708 (High): Markov-blanket partition does not by itself license a group knower (Bruineberg et al. 2022; Raja et al. 2021)
- PRESUMPTION-1225 -> DISPOSITION-1124 -> MONITOR-709 (Medium)

**Limits (fail loud):** preliminary searches, 0 page fetches. Sources are titles seen or background recall, labelled as such. 15a/15b independence is procedural only (one orchestrator, shared searches). Not met: "all queued items searched" - the [IN-HOUSE] items and the older bare-literature backlog (line ~20061 note) were not touched.
**Lock:** scripts/lit_pipeline_lock.sh is outside the mounts, so LOCKED/RELEASED lines were appended to lit_pipeline.lock by hand. Backups: *.bak.20261108-pre-15pipeline in architecture/.
