# Schedule Update — Sunday Tradition Synthesis Day
*Architectural decision recorded: 2026-06-02*
*Decision type: Agent roster expansion + schedule revision*

---

## Change Summary

Four new specialist tradition agents (Agents 17-20) have been added to the agent roster and assigned to a new weekly slot: **Sunday Tradition Synthesis Day**. Sunday previously ran only the orchestrator's fallback hunt with no specialist agents. It now runs four specialist agents before the orchestrator fallback.

---

## Revised Weekly Schedule

| Day | Agents | Character | External search load |
|-----|--------|-----------|----------------------|
| Monday | Agent 01 (Levin) + Agent 02 (Friston) | Consciousness + Biology | High |
| Tuesday | Agent 04 (Hawkins) + Agent 03 (Hoffman) | Neural Architecture + Conscious Realism | Medium-High |
| Wednesday | Agent 05 (McGilchrist) + Agent 11 (Kastrup) | Divided Brain + Analytic Idealism | Medium-High |
| Thursday | Agent 07 (Stump) + Agent 06 (Fredrickson) | Thomism + Flourishing | Medium |
| Friday | Agent 08 (Carroll) + Agent 09 (Arkani-Hamed) | Physics/Naturalism + Post-Spacetime | Medium |
| Saturday | Agent 10 (Wolfram) | Computational Physics | Medium |
| **Sunday** | **Agent 17 (MacIntyre) + Agent 18 (Wright) + Agent 19 (Rohr) + Agent 20 (Loughran)** | **Tradition-Rationality + Narrative Theology + Contemplation + Architecture** | **Low** |
| Sunday cont. | Orchestrator fallback hunt | Remaining thinker coverage | Variable |

---

## Rationale for Sunday Grouping

The four new agents are grouped on Sunday because they share a single unifying question that none of the existing daily pairings address: *how do traditions know, develop, and encounter each other?* MacIntyre provides the theory (tradition-constituted rationality), Wright provides the narrative model (five-act hermeneutic, faithful improvisation), Rohr provides the contemplative practice (non-dual knowing, order-disorder-reorder), and Loughran provides the architectural implementation (Synergistic Coil, C2A2). Together they constitute the tradition-epistemology axis.

Sunday is the right day because:

1. **These four produce the lightest external search load of any multi-agent combination.** MacIntyre publishes infrequently; Loughran has no external sources at all (Agent 20 reads the week's accumulated C2A2 output, not the web); Wright and Rohr are active but their primary sources are less dense than the scientific programs. Combined, Sunday's four agents run 5-7 total web searches — comparable to a single science tradition agent on a heavy day.

2. **Sunday's position at the end of the Mon-Sat cycle is architecturally appropriate.** The Loughran agent specifically reads the week's accumulated Pattern Detector findings and cross-program output and generates synthesis questions and Synergistic Coil assessments. This requires the week to be nearly complete before it runs. Sunday is the only day this is true.

3. **Sunday's outputs feed the Monday restart.** MacIntyre's self-critique dispatches, Wright's faithful-improvisation assessments, Rohr's contemplative probes, and Loughran's Synergistic Coil candidates are all available to Monday's Levin and Friston agents as they begin the new cycle.

4. **The grouping does not disrupt any existing pairing.** All eleven existing specialist agents retain their current day assignments unchanged.

---

## Token Budget Assessment

Estimated Sunday session cost vs. a typical two-science-tradition day:

| Component | Typical Monday (Levin + Friston) | Sunday Tradition Synthesis Day |
|-----------|----------------------------------|-------------------------------|
| Web searches | 6-10 searches | 5-7 searches (MacIntyre ~1-2, Wright ~2-3, Rohr ~2-3, Loughran ~0) |
| PRS extraction | 4-8 new triplets across 2 traditions | 2-5 new triplets across 4 traditions |
| Cross-program flags | 2-4 | 3-6 (Loughran's synthesis function generates more flags per triplet) |
| Dispatch volume | 2-4 dispatches | 4-6 dispatches |
| Net token estimate | ~25,000-40,000 tokens | ~20,000-35,000 tokens |

Sunday is estimated to be **cheaper than Monday** in typical operation, with Loughran's zero-search profile significantly reducing the search overhead that drives most of the token cost in science-tradition days.

---

## Architectural Notes

**Agent 20 (Loughran) has no external search responsibility.** This is by design and is architecturally coherent: the C2A2 program's primary sources are C2A2's own outputs. The Loughran agent is explicitly the system's reflective capacity, not its intake function.

**Agent 17 (MacIntyre) has a dual role** that no other tradition agent has: it maintains MacIntyre's wiki like any other tradition agent, but it also applies MacIntyre's tradition-vitality criteria back to C2A2 itself. The C2A2 self-critique dispatch type (available only to Agent 17) is a structural safeguard — the system's immune response to its own potential corruption.

**Agent 19 (Rohr) explicitly permits Speculative confidence** as the epistemologically honest rating for many contemplative-epistemological claims. This is a departure from the implicit preference for High confidence across the network and should be treated as information (about the character of non-dual knowing) rather than as a failure of the agent.

**The orchestrator fallback hunt continues after the four Sunday specialists run.** The orchestrator fallback should check whichever thinkers among the 15 have not been covered by their specialist on a given week. With MacIntyre, Wright, Rohr, and Loughran now having Sunday specialists, the orchestrator fallback scope on Sundays narrows to thinkers whose designated specialist slots fell on a day where the specialist didn't run.

---

## Files Affected

- `wiki/agents/17_macintyre_agent.md` — new
- `wiki/agents/18_wright_agent.md` — new
- `wiki/agents/19_rohr_agent.md` — new
- `wiki/agents/20_loughran_agent.md` — new
- `wiki/architecture/schedule_update_sunday_tradition_day.md` — this file
- `wiki/PETER/AGENTS.md` — updated to reflect new agents in the ecology

---

## Update Required: Master Agent Schedule Configuration

The Master Agent (`wiki/agents/12_master_C2A2_agent.md`) contains the operative weekly schedule that drives actual autonomous runs. **That file must be updated** to include Sunday's four new specialist agents before the Sunday schedule will execute. This requires an attended session: read the Master Agent file, locate the schedule section, and add the Sunday Tradition Synthesis Day block.

Until that update is made, Agents 17-20 exist as governance documents only and will not run autonomously. They can be invoked manually in attended Cowork sessions immediately.

---
*Recorded by: Tom Loughran / Cowork session 2026-06-02*
*Reversibility: Moderate — agents can be removed from rotation without other architectural changes*
*Downstream effects: Master Agent schedule config requires update; PETER/AGENTS.md updated in this session*
