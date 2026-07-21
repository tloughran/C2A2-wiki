# Canonical Agent Map — OpenStory ↔ C2A2 Agent Explorer

**Purpose.** The contract between three sources of identity:
1. **Scheduler** — the authoritative `taskId` (from `list_scheduled_tasks`), which is the exact string OpenStory stores in `sessions.label` as `<scheduled-task name="{taskId}">`.
2. **OpenStory** — captured session telemetry, keyed by that slug.
3. **C2A2 roster** — the "constitutional markdown" shown in the Agent Explorer tab (`wiki/agents/NN_*.md`), or, for operational agents, the scheduled task's own `SKILL.md`.

**Join key:** `taskId` == name parsed from `sessions.label`. No re-instrumentation needed.

**Capture status legend:** sessions currently in the OpenStory store (`./data/open-story.db`) for that slug, with the last date seen. Most are sparse/zero because OpenStory has been watching `~/.claude/projects/` (13 files) instead of the Cowork store `~/Library/Application Support/Claude/local-agent-mode-sessions/` (2,763 files) — see the diagnosis. These counts will change once the watch path is fixed.

---

## Thinker-pair agents (category: c2a2-thinker)

| taskId | Day | Constitution(s) | OpenStory capture |
|---|---|---|---|
| `c2a2-agent-levin-friston` | Mon 03:00 | 01_levin, 02_friston | 3 sessions (→06-08) |
| `c2a2-agent-hawkins-hoffman` | Tue 03:00 | 04_hawkins, 03_hoffman | 2 (→05-05) |
| `c2a2-agent-mcgilchrist-kastrup` | Wed 03:00 | 05_mcgilchrist, 11_kastrup | **0** |
| `c2a2-agent-stump-fredrickson` | Thu 03:00 | 07_stump, 06_fredrickson | **0** |
| `c2a2-agent-carroll-arkanihamed` | Fri 03:00 | 08_carroll, 09_arkanihamed | **0** |
| `c2a2-agent-wolfram` | Sat 03:00 | 10_wolfram | 2 (→05-05) |
| `c2a2-agent-wright-rohr` | Sun 03:04 | 18_wright, 19_rohr | **0** |

> 4 of 7 thinker pairs have zero captured sessions — the most important gap to close, since the thinker network is central to the thesis.

## Pipeline agents (category: c2a2-pipeline)

| taskId | Schedule | Constitution(s) | OpenStory capture |
|---|---|---|---|
| `c2a2-self-awareness-daily` | daily 23:30 | 14a_assumption_extractor, 14b_presumption_detector | 5 |
| `c2a2-lit-search-pipeline` | daily 00:30 | 15a_lit_search_for, 15b_lit_search_against, 15c_net_evaluator | 5 |
| `c2a2-periodic-monitor-weekly` | Sun 03:30 | 15d_periodic_monitor | **0** |
| `c2a2-deferred-action-monitor` | daily 02:30 | 16_deferred_action_monitor | **0** |
| `c282-wiki-agent-daily-run` ⚠️ | daily 04:34 | 12_master_C2A2 (orchestrator) | 8 |
| `c2a2-wiki-janitor-weekly` | Sun 05:45 | — (SKILL.md only) | **0** |
| `c2a2-sewing-agent-weekly` | Sun 04:30 | — (SKILL.md only) | **0** |
| `c2a2-prs-connectome-weekly` | Sun 07:30 | — (SKILL.md only) | 1 |

> ⚠️ `c282-wiki-agent-daily-run` — note the `c282`/`c2a2` typo baked into the taskId; the join still works because both sides share the string. Worth renaming someday, but don't rename casually (it would orphan historical sessions keyed to the old slug).

## Summa project agents (category: project)

| taskId | Schedule | Constitution | OpenStory capture |
|---|---|---|---|
| `summa-qc-sweep` | every 4h | SKILL.md | 8 (35k events, 9.5k eval/apply) |
| `summa-commentary-reviewer` | every 4h | SKILL.md | 6 |
| `summa-2026-daily-batch` | daily 05:00 | SKILL.md | 1 |
| `summa-2026-nightly-verification` | daily 23:00 | SKILL.md | **0** |

## Bridge agents (category: bridge)

| taskId | Schedule | OpenStory capture |
|---|---|---|
| `morning-walk-cowork-handoff` | M–F 09:00 | 4 |
| `c2a2-morning-chat-scrape` | daily 08:45 | 4 |
| `c2a2-evening-cowork-to-chat` | daily 18:30 | 4 |

## Infrastructure agents (category: infrastructure)

| taskId | Schedule | OpenStory capture |
|---|---|---|
| `morning-system-health` | daily 06:00 | 9 |
| `morning-project-status` | daily 08:00 | 9 |
| `agentic-cost-tracker` | Mon 05:30 | 4 |
| `openstory-version-check` | Mon 05:35 | 3 |
| `reviewer-review-weekly` | Mon 06:30 | 1 |
| `scheduler-health-check` | daily 07:00 | 1 |
| `supabase-c2a2-keep-warm` | daily 06:30 | 1 |
| `weekly-agent-ecosystem-report` | Sun 22:30 | **0** |
| `connector-health-weekly` | Sun 06:15 | **0** |
| `weekly-claude-projects-backup` | Sun 23:00 | **0** |
| `execution-assistant` | manual | **0** |

---

## Unmapped constitutions (no scheduled task)

`12_master_C2A2` (linked above to the orchestrator), `17_macintyre`, `20_loughran`. These appear to be framework/meta roles invoked within other runs rather than independently scheduled. Confirm intent before showing them as standalone rows.

## Notes / open items for the strong build

- **Identity is solved**; the only blocker is capture (watch-path fix + backfill).
- **Constitution source differs by category**: thinker/pipeline agents → `wiki/agents/NN_*.md`; operational agents → their scheduled `SKILL.md`. The generator should resolve both.
- **Pairs vs. individuals**: thinker tasks are pairs but constitutions are individual files — the tab's "click → constitution" needs to show both members (or a merged view).
- This table should become a small machine-readable `agent_map.json` that the future extractor/generator reads (single source of truth). Easy to emit from this once approved.
