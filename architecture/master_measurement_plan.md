# C2A2 Master Measurement Plan — Measuring Progress Across the Accelerator/Detector System

_Drafted 2026-06-09. Synthesizes the 2026-06-09 [[measurement_framework]] (three measurement levels under the constitutional aim) with the 40-step start-up algorithm and detector instruments set out in the 2022 ISME paper "Four Models of Cultural Exchange." Purpose: a single measurement plan for the whole accelerator/detector system — using OpenStory data where it fits, and naming every other data type we must gather. OS-inclusive, not OS-centered._

---

## 1. The core reconciliation

Three things that have been described separately are three views of one object:

- **The three measurement levels** (Agent Activity / Community Interaction / Deep Interaction) are a *nesting of units of analysis* — the individual agent, the community, the pair of traditions in contact.
- **The 40-step algorithm** is the *operational protocol* that drives a pair of traditions from "assembled" to "evidentially interacted," and it ships with its own measurement instruments.
- **The accelerator/detector metaphor** is the *instrument theory*: traditions are prepared (accelerated) and then passed through detectors (concept inventories, application tests, mature-member agreement) that register what happened when they met.

The plan below treats the 40-step algorithm as the **detector design for the deepest level**, the GPRS frame as the **detector for the community level**, and OpenStory as the **detector for the activity level** — plus a cross-cutting role OS plays at every level because it observes the *agents* that increasingly do the work at all three.

A one-line statement of what "progress" means here: **the system is making progress to the exact extent that it can register departures from chance in how fully-informed agents behave at the interface of rival traditions, and can do so with increasing precision, breadth of person-types, and stability under repeated interaction.** Everything below is an attempt to instrument that sentence.

---

## 2. Measurement architecture (the three nested detectors)

```
CONSTITUTIONAL AIM  (loving, peaceful, integrative, liberating network; all agents as ends)
        │
        ▼  measured at three nested units of analysis
┌─────────────────────────────────────────────────────────────────────┐
│ L1  AGENT ACTIVITY      unit = the agent (AI or human)               │
│     detector: OpenStoryArc telemetry                                 │
│     "who did what, how often, with whom, and is it agentic"          │
├─────────────────────────────────────────────────────────────────────┤
│ L2  COMMUNITY INTERACTION   unit = the community / tradition          │
│     detector: GPRS spine (Goal-Problem-Resource-Solution)            │
│     "does the community succeed on its own terms; who helps whom"     │
├─────────────────────────────────────────────────────────────────────┤
│ L3  DEEP INTERACTION    unit = the PAIR of traditions in contact      │
│     detector: the 40-step algorithm's instruments —                  │
│       MMA (mature-member agreement), CCI (concept inventory),         │
│       AT (application test), second-first-language certification,     │
│       outcome-typing (intractable/conversion/complementary/           │
│       transformative/incomplete)                                      │
└─────────────────────────────────────────────────────────────────────┘
        │
        ▼  cross-cutting ledger
   PRS CONNECTOME  —  the accumulating record of problems solved /
   resources introduced across all traditions; the running "progress
   tape" against which any of the three levels can be scored over time.
```

---

## 3. Level 1 — Agent Activity (OpenStory is the instrument)

**Unit:** the individual agent run (currently 34-agent C2A2 roster; OS holds 572 sessions / 98,765 events as of 2026-06-08).

**What we can measure now, directly from `agent_telemetry.json`:** sessions, events, eval/apply counts and ratio, scope open/close, errors, **delegations** (sub-agent calls — the native "in contact with whom" and agent-to-agent signal), tool_use (named), thinking, prompts, run duration, day-of-week distribution, tools used, models used, tool-coverage. The agentic-vs-human distinction the framework asks for is structural in OS (sessions carry a scheduled-task label vs. interactive).

**What L1 cannot yet see, and how to close it:**
- **Capture completeness.** 4 of 7 thinker-pair agents read ZERO sessions because OS watched `~/.claude/projects/` not the Cowork store. Fix = the symlink bridge (`~/openstory-watch/`) + full backfill; must run on the Mac. *Until this runs, every L1 number is a biased sample — flag on every chart.*
- **"Upgrades, skill additions, changes" over time.** Not a native OS field. Derive it by diffing the agent roster / constitution files / installed skills across snapshots (a small scheduled job writing a changelog), then join to OS activity to ask "did capability change move output?"
- **Dynamic vs. static scheduling.** Today schedules are fixed cron. The measurable opportunity: feed OS output metrics (events, eval/apply yield, error rate per agent) back as the *signal* for reallocating run frequency — i.e., turn L1 from a dashboard into a controller. That is a genuine experiment (does output-driven scheduling beat fixed cron?), not just a metric.

**L1 progress metrics:** capture-completeness %, weekly active agents (human/agentic split), delegation graph density, eval/apply yield per session, error rate trend, and capability-change events correlated with output.

---

## 4. Level 2 — Community Interaction (GPRS is the instrument)

**Unit:** the community/tradition describing its own work through the Goal-Problem-Resource-Solution spine (self-first articulation: goals; problems; resources have/tap/need; solutions effected/proposed). The Community Explorer already holds **156 curated GPRS nodes (640 edges)** and the PRS connectome holds **269 triplets** across 14 traditions.

**What we can measure now:**
- **Articulation depth** — count and richness of GPRS entries per community; how complete the have/tap/need resource picture is. This is a real "does the community succeed on its own terms" proxy: a tradition that can state its goals, name its problems, inventory its resources, and point to solutions is measurably further along than one that cannot.
- **Structural connectivity** — shared-reference and PRS-similarity edges between communities (already computed: 156-node similarity graph; sociogram's 70k cross-edges). Kindred-effort discovery is an edge-detection problem we can already run.
- **PRS chain growth** — the connectome grew 231→269 triplets in one regen; the *rate* of accumulation is itself a community-vitality signal.

**What L2 cannot yet see, and how to close it:**
- **Mutual-assistance flows (H→H, H→AI, AI→H, AI→AI).** The framework's headline L2 measure. Not captured anywhere today. Requires an **interaction-event log**: each assist tagged with giver-type, receiver-type, community, and what was exchanged (a resource? a solution?). OS captures the AI-side half (delegations, tool calls) but not the human side or the *semantic* "this helped." Proposed instrument: a lightweight assist-ledger that both the Community Explorer (human-entered) and the agents (auto-logged) write to, with a common schema.
- **Success-on-own-terms over time.** Needs each community's goals to carry a status field that can move (proposed → in progress → met), so we can plot goal-attainment curves rather than static snapshots.

**L2 progress metrics:** GPRS completeness per community, PRS-triplet accumulation rate, cross-community edge count/weight (kindred efforts found), and the four-way assist-flow volume once the assist-ledger exists.

---

## 5. Level 3 — Deep Interaction (the 40-step algorithm IS the detector)

This is where the 2022 paper does the heavy lifting the framework only gestured at. The 40 steps are not just a workflow; **each instrument the steps build is a measuring device with a defined pass/fail and a physics analogue.** The unit of analysis is the *pair of traditions in contact*.

### 5.1 The detector instruments (all are new data types — essentially none exist yet)

| Instrument | What it measures | Physics analogue (paper's framing) | Status |
|---|---|---|---|
| **MMA — Mature-Member Agreement** | Whether a defined set of mature members unanimously affirm a claim/test/outcome; this *constitutes* a tradition's assent | The calibration source — the known-status "particles" you send through the detector | Not gathered. The 14 thinker rosters are agent-built *proxies*, not certified mature-member cohorts. |
| **CCI — Community Concept Inventory** | Conceptual maturity in a tradition, plain-language, validated so all-and-only mature members pass | The Force Concept Inventory | None built for any tradition. |
| **AT — Application Tests** | Ability to *apply* the tradition's concepts in varied contexts | The Mechanics Baseline Test | None built. |
| **Detector validation** ("rediscover the standard model") | That MMA+CCI+AT reproduce a broad range of already-known in-tradition results | Test-beam / standard-model rediscovery | Not run. |
| **Second-first-language certification** | That a member of tradition A can play a mature member of tradition B | — | Not gathered; this is the central L3 output. |
| **Outcome-typing** | The settled type of a completed interaction: *intractable / conversion / complementary / transformative / incomplete* | The detected event category | No interactions run, so no outcomes typed. |

### 5.2 What this means for measurement honesty

Level 3 is **almost entirely uninstrumented today** — and that is the most important finding of this audit. What C2A2 has built (rosters, PRS connectome, sociogram, explorers) corresponds to the *earliest steps* of Pilot Stage 1 (assemble traditions; build PRS histories). The detector proper — CCI/AT/MMA and outcome-typing — has not been started for any tradition. This is not a criticism; it is the map of where the measurable frontier actually is.

### 5.3 The AI-agent shortcut (and its measurement caveat)

The framework's bet is that AI agents can stand in as mature members and second-first-language speakers, running interactions at machine speed. If so, L3 instruments become *generatable and runnable in software* far sooner than human cohorts allow — and **OpenStory becomes the L3 observer too**, because it can watch the agent-run interactions step-by-step. The caveat to measure explicitly: an agent "passing" a CCI it or its kin authored is circular. L3 validity therefore needs the paper's own safeguard imported into the agent setting — *human* mature-member agreement as the calibration source, at least for certifying the instruments before agents run them at scale.

**L3 progress metrics (once instruments exist):** number of traditions with validated CCI/AT, count of certified second-first-language pairs, count of completed interactions by outcome-type, and — the deepest one — the *outcome-type distribution and its movement over repeated runs* (e.g., are "intractable" verdicts converting to "complementary" as preparation improves?).

---

## 6. The unifying progress metric: departure-from-chance over the PRS ledger

The paper supplies the single quantity that ties all three levels together: **statistically significant departure from a random distribution of outcomes** at the tradition interface (its computational sketch models traditions by PRS-commitments `c`, interaction-history `h`, and individual factors across person-types `n`/`g`). Concretely, a master progress index for C2A2 should combine:

1. **Ledger growth** — PRS triplets accumulated and *chained* (problems solved drawing on prior resources). This borrows directly from the physics-history tool's demonstration that progress can be quantified by chaining PRS triplets, and it already has live data (269 and climbing).
2. **Detector coverage** — fraction of traditions with validated MMA/CCI/AT (currently 0).
3. **Interaction yield** — count of completed, outcome-typed interactions, weighted toward complementary/transformative outcomes (currently 0).
4. **Person-type breadth** — over how many discernible person-types an outcome holds (future; needs the computational modeling track).
5. **Stability** — does an outcome survive re-interaction and wider promulgation (future).

Items 1 is measurable now; 2–5 mark the build order. The honest headline: **today we can measure the ledger and the activity around it; we cannot yet measure the thing the system exists to measure (what fully-informed agents do at the interface), because the detector for that has not been built.**

---

## 7. Readiness scorecard — where C2A2 sits on the 40 steps today

| Phase (from the 2022 paper) | Step cluster | C2A2 status now |
|---|---|---|
| **Pilot S1 — prepare traditions** | 1. Identify mature-member pool | Partial — 14 thinker *proxies* assembled; no certified human MMA cohort |
| | 2. Build PRS-triplet history | **Strongest asset** — 269-triplet connectome, per-thinker PRS |
| | 3. Design CCI + Application Tests | Not started |
| | 4. Align tests to MMA | Not started |
| | 5. Validate ("rediscover the standard model") | Not started |
| | 6–7. Backward-design + test curriculum | Pedagogical proto-tools exist (physics/RC explorers); not tradition-certified |
| | 8–10. Certify traditions + the pair | Not reached |
| **Pilot S2 — interact the pair** | 1. Begin capturing everything | **OpenStory is exactly this capability** — instrumented, partially live |
| | 2–8. Train SFL speakers → exchange → verdicts → outcome-typing | Not started (no certified speakers, no interactions) |
| | 9–10. Promulgate + review | Dissemination surfaces exist (public repo, explorers); nothing to promulgate yet |
| **Run 1 (parallel cohort) + dissemination** | support team, 4–6 traditions, podcasting, ITS-for-traditions | Future; podcast/dissemination + community-curated platform are named but unbuilt |

Read at a glance: **we are at Pilot Stage 1, steps 1–2, with the Stage-2 capture layer (OS) already in hand ahead of schedule.** The next measurable milestone is the first CCI/AT for a single tradition — the step that turns the rosters from a *picture* of traditions into a *detector* of maturity in them.

---

## 8. Data inventory — have now vs. must gather

| Data type | Level | Have now? | Source / what's needed |
|---|---|---|---|
| Agent activity telemetry | L1 | **Yes (biased sample)** | OpenStory; needs the symlink-bridge backfill on the Mac |
| Capability-change log (skills/upgrades) | L1 | No | Scheduled diff of roster/constitutions/skills → changelog |
| GPRS community self-descriptions | L2 | **Partial (156 nodes)** | Community Explorer; extend coverage + add goal-status field |
| PRS-triplet connectome | L2/ledger | **Yes (269)** | Regen pipeline (Mac-only currently) |
| Cross-community kindred-effort edges | L2 | **Yes** | Sociogram + PRS-similarity graph |
| Four-way mutual-assistance flows | L2 | No | New assist-ledger schema written by both humans (Explorer) and agents |
| MMA cohorts + agreements | L3 | No | Recruit/certify mature members (human first, for calibration) |
| CCI + Application Tests per tradition | L3 | No | Author + validate per tradition (the next real build) |
| Second-first-language certifications | L3 | No | Produced by the 40-step prep; agents may accelerate |
| Outcome-typed interactions | L3 | No | Produced by running interactions |
| Person-type / departure-from-chance models | master | No | Computational track ("chang equation", GAN modeling) |
| Dissemination/reach metrics | Run 1 | No | Future community-curated platform + podcast analytics |

---

## 9. Recommended build order (what makes the next increment measurable)

1. **Make L1 honest** — run the OS symlink-bridge backfill on the Mac so capture is complete; only then publish L1 numbers. *(Mac-needed; sandbox cannot.)*
2. **Make the ledger a first-class progress tape** — expose PRS-triplet accumulation rate and chain-depth as a tracked time series (the one defensible "progress" number we have today).
3. **Stand up the assist-ledger schema** — the smallest new instrument that unlocks the framework's headline L2 measure (four-way assistance flows). Design now; it's software.
4. **Author the first CCI for one tradition** — the milestone that converts a roster into a detector and opens Level 3. Start with the tradition that has the richest PRS history. Requires human mature-member agreement for calibration; agents draft, humans certify.
5. **Specify the agent-run interaction harness + its OS observation** — so that when instruments exist, interactions can be run and outcome-typed at machine speed, watched by OS, with the circularity safeguard (human-certified instruments) built in.

---

## 10. Honest bottom line

OpenStory gives us a strong **Level 1** instrument and, conveniently, the **Pilot-Stage-2 capture layer** ahead of schedule. The **PRS connectome** is a genuine, already-live progress ledger and the best candidate for a single quantified-progress number today. But the system's *reason for being* — measuring what fully-informed agents do at the interface of rival traditions — lives at **Level 3**, whose detector (CCI/AT/MMA, outcome-typing) **has not yet been built for any tradition.** The master plan is therefore less "wire up the dashboards" and more "**build the detectors, calibrate them against human mature-member agreement, then let agents and OpenStory run and observe interactions at speed.**" The measurable frontier is the first concept inventory.
