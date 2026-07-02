# OpenStory Substrate - Legibility Map

_Generated 2026-06-30 01:16 from a read-only snapshot._

_Snapshot: `open-story-snapshot.db`_

## 1. The model: one immutable log, many regenerable folds

Everything here is either the **`events`** log (the immutable substrate) or a **fold** over it (`turns`, `patterns`). The recrystallize replay proved any fold can be deterministically rebuilt from the log - so every analysis below, and every future one, is a re-runnable projection, never a baked-in artifact.

## 2. Inventory and the event alphabet

- **events**: 330,290
- **turns**: 4,910
- **patterns**: 225,684
- **sessions**: 1,564
- **plans**: 0
- **span**: 2026-03-30T19:09:19.612Z -> 2026-06-30T00:53:02.743Z
- **distinct hosts / users**: 1 / 1 (this corpus is one human across many agent sessions/projects)


Event subtypes (the alphabet the substrate is written in):

| subtype | count |
|---|---:|
| `system.thinking_tokens` | 78,828 |
| `message.assistant.tool_use` | 54,268 |
| `message.user.tool_result` | 54,100 |
| `queue.enqueue` | 29,865 |
| `system.status` | 27,580 |
| `queue.dequeue` | 26,828 |
| `message.assistant.thinking` | 21,999 |
| `message.assistant.text` | 18,306 |
| `system.permission_auto_approved` | 4,222 |
| `message.user.prompt` | 4,006 |
| `system.permission_request` | 3,035 |
| `queue.remove` | 3,022 |
| `system.init` | 2,830 |
| `system.turn.complete` | 642 |
| `system.api_retry` | 401 |
| `system.permission_response` | 136 |
| `system.compact` | 108 |
| `system.task_progress` | 89 |
| `system.model_refusal_fallback` | 11 |
| `system.permission_denied` | 3 |
| `system.task_notification` | 3 |
| `system.task_started` | 3 |
| `system.task_updated` | 3 |
| `system.commands_changed` | 1 |
| `system.hook` | 1 |

## 3. What a 'turn' actually is

A `turn` is one boundary-delimited beat of the working loop, and the row carries **content, not just counts**. Fields present in `turns.data`:

`agent`, `applies`, `duration_ms`, `env_delta`, `env_size`, `eval`, `event_ids`, `human`, `is_terminal`, `scope_depth`, `session_id`, `stop_reason`, `thinking`, `timestamp`, `turn_number`

The load-bearing point: `human` (the prompt), `thinking`, and `eval` (the response) are all in the same row as `applies`, `stop_reason`, `scope_depth`, `duration_ms`. So the substrate is a **content-bearing dialogue record**, not mere activity telemetry.

**Example** (session `agent-a53b56`, turn 0, 2 applies, stop_reason=`end_turn`):

> **human:** Search for a file called "distributed-logos.md" under /sessions/funny-youthful-mendel/mnt/Projects/. Use Glob and then Read the file. Report the full path and complete contents. Research only, no edits....

> **eval:** ## Results

**Full Path:**
`/sessions/funny-youthful-mendel/mnt/Projects/RC_Wiki_Karpathy2upgrades/RC_Wiki/concepts/distributed-logos.md`

**Complete Contents:**

```markdown
---
name: Distributed Logos
type: philosophical
tradition: [thomism, cognitive-science, theology]
related_thinkers: [aquinas,...

## 4. Data health - what is alive, thin, or frozen

| signal | count | last seen | status |
|---|---:|---|---|
| events (substrate) | 330,290 | 2026-06-30T00:53:02.743Z | ALIVE |
| eval_apply.eval | 117,564 | 2026-06-30T00:36:54.548Z | ALIVE - core deliberation signal |
| eval_apply.apply | 96,565 | 2026-06-30T00:36:54.548Z | ALIVE - core action signal |
| turns table | 4,910 | 2026-06-30T00:36:15.177Z | ALIVE - content-rich, full history |
| turn.sentence | 882 | 2026-06-30T00:36:15.177Z | thin - explicit boundaries only |
| eval_apply.turn_end | 881 | 2026-06-30T00:36:15.177Z | thin - explicit boundaries only |
| eval_apply.scope_open | 7,499 | 2026-04-08T21:10:47.874Z | FROZEN - Apr drift, not recovered |
| eval_apply.scope_close | 1,086 | 2026-04-08T21:10:47.874Z | FROZEN - Apr drift, not recovered |
| turn.phase | 517 | 2026-04-08T16:45:09.403Z | FROZEN - Apr drift, not recovered |
| error.recovery | 155 | 2026-04-08T21:08:25.650Z | FROZEN - Apr drift, not recovered |
| agent.delegation | 28 | 2026-04-06T14:23:49.485Z | FROZEN - Apr drift, not recovered |

**eval:apply ratio = 1.22** (slightly more deliberation than action, full history).

## 5. Turn coverage and skew

- sessions total: **1,564**; with >=1 turn: **223**; with >=1 human prompt: **911**
- sessions that have prompts but **no** crystallized turns: **807** (a coverage gap, not empty noise)
- turns/session: median **1**, max **2,524** (one session dominates) - heavily skewed


Turns by month (the freeze and its recovery, in numbers):

| month | turns |
|---|---:|
| 2026-03 | 117 |
| 2026-04 | 895 |
| 2026-05 | 993 |
| 2026-06 | 2,905 |

## 6. Human/AI structure

- `message.user.prompt`: 4,006
- `message.assistant.text`: 18,306
- `message.assistant.thinking`: 21,999
- `message.assistant.tool_use`: 54,268
- `message.user.tool_result`: 54,100
- `system.turn.complete`: 642

- **AI-to-AI is capturable now via lineage**: 191 `agent-*` sessions, `origin_agent` set on 1564/1564. The per-turn `is_agent` flag, by contrast, is **0/4910** - dead. So agent-to-agent structure lives at the session level, not the flag.

- of 4,910 turns: **3,655** carry the human prompt, **3,669** carry AI thinking, **3,954** carry the AI response - the relational raw material is already present.

## 7. Reading the map

**What we have, robustly:** the event substrate (full alphabet), the eval/apply cognitive rhythm (full history), and a content-bearing `turns` table spanning Mar-Jun with the human prompt + AI thinking + AI response in ~75-80% of rows. Listening/relationship folds can be built directly on `turns.data` - no dependency on new OpenStory instrumentation.

**What is thin or dark:** the turn-boundary patterns (`turn.sentence`/`turn_end`) fire only on explicit boundaries (~880), and four detectors (`scope_*`, `turn.phase`, `error.recovery`, `agent.delegation`) went dark at the same Apr-7/8 format drift and the replay did **not** revive them - a separate, still-open signal gap.

**Two questions for OpenStory:** (a) which dropped Claude Code signals fed those four dark detectors, and can they be re-derived? (b) why do 807 prompt-bearing sessions crystallize no turns - a fold-coverage gap worth closing before we measure on top of it.

