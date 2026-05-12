# C2A2 Agent Architecture Review
*Generated: 2026-05-01*

---

## Part 1: Current Agent Inventory & Status Assessment

### Thinker Agents (Weekly Schedule)

| Day | Time | Agents | Status |
|-----|------|--------|--------|
| Monday | 3:00 AM | Levin + Friston | Active |
| Tuesday | 3:00 AM | Hawkins + Hoffman | Active |
| Wednesday | 3:00 AM | McGilchrist + Kastrup | Active |
| Thursday | 3:00 AM | Stump + Fredrickson | Active |
| Friday | 3:00 AM | Carroll + Arkani-Hamed | Active |
| Saturday | 3:00 AM | Wolfram | Active |
| Sunday | 3:00 AM | Wright + Rohr | Active |

All 14 thinker agents are scheduled and presumed active. Each runs once weekly in its assigned slot. Wolfram runs solo on Saturday; all others are paired.

### Supporting Pipeline Agents (Daily / Weekly)

| Agent | Schedule | Role |
|-------|----------|------|
| C2A2 Orchestrator | Daily, 4:34 AM | Master coordination — runs after all thinker slots have cleared |
| Lit Search | Daily, 12:39 AM | Literature scanning and evidence gathering |
| Deferred Action Monitor | Daily, 2:33 AM | Processes deferred tasks before thinker agents wake |
| Self-Awareness | Daily, 11:37 PM | End-of-day reflection and architectural self-assessment |
| Periodic Monitor (weekly) | Sunday | Aggregate health check across all traditions |

### Assessment: What's Working

The weekly rotation covers all 14 thinkers without overlap. Pairing agents on the same night (e.g. Friston + Levin on Monday) is architecturally sound — they are among the most cross-connected thinkers in the vault, so co-scheduling creates natural synthesis opportunities. The pipeline order (Deferred → Thinkers → Orchestrator → Lit Search → Self-Awareness) forms a coherent nightly loop.

### Critical Gap: One Agent Per Thinker

**This is the most significant architectural shortfall currently identified.**

The design intent — modeled on Hawkins' cortical column hypothesis — calls for **three agents per thinker**, each running from a slightly different perspective or temperature setting. The rationale:

- A single agent visiting a page produces a single interpretation, which may be locally coherent but globally brittle. It can miss nuance, over-index on one framing, or get stuck in a rut across weekly visits.
- Three agents, each configured with different epistemic stances (e.g. sympathetic/neutral/skeptical, or different temperature settings), produce divergent outputs that can then be reconciled by a tiebreaker pass.
- This mirrors how cortical columns process the same sensory signal redundantly and vote — the agreement between columns is what constitutes "perception."

Currently: 14 single-agent thinker slots.  
Target: 14 × 3 = 42 thinker agent instances per weekly cycle, with a tiebreaker layer.

This is flagged as **Development Priority 1** (see Part 4).

### Minor Gaps

- **Loughran thinker agent**: Not listed in the current schedule. The color palette and wiki structure include a Loughran tradition node — if this is intended as a first-person reflective agent (Tom-as-thinker), it has no scheduled run.
- **Rohr agent**: Listed as wiki agents/11... does not have a dedicated agent file matching the numbering convention (agents 01–11 cover Levin through Kastrup). Wright and Rohr run together Sunday but may share a single agent file — worth verifying their prompts are correctly individuated.
- **No weekend lit search**: The lit search runs daily, but there is no agent specifically tasked with reviewing lit search outputs in the context of the weekly thinker runs before the orchestrator fires.

---

## Part 2: Sewing Agent Design

### Concept

The Sewing Agent (also: Innervating Agent, Orphan Integration Agent) addresses a structural problem that emerges in any large wiki: **pages that exist but are not connected to the living knowledge graph**. These orphaned or under-connected pages are information that the system cannot use — it sits inert, invisible to the thinker agents that might benefit from it.

The biological analogy is apt: think of wiki pages as cells in a tissue. A cell that receives no signaling molecules and sends none is functionally isolated — it may contain useful machinery but contributes nothing to the organism. The Sewing Agent's job is to identify these cells and inject **agentic calls** — transport signals that reroute other agents through the isolated page on their next pass.

This is modeled loosely on Hawkins' inter-column signaling: when one cortical column's prediction fails, it broadcasts an error signal that alters the processing posture of neighboring columns. An agentic call in a wiki page is the equivalent — it says: *"the next time you (Levin agent) pass through this region of the vault, your prediction model for this page should be updated."*

### The `## Agentic Calls` Convention

Each agentic call is a structured instruction embedded in a wiki page under a standard heading. Format:

```markdown
## Agentic Calls

[→ Levin agent]: This page contains evidence relevant to bioelectric memory encoding 
in non-neural tissue. Review and cross-link to [[Levin thinker node]] and 
[[bioelectric_memory]] if they exist; propose a new synthesis page if not.

[→ Friston agent]: The teleological framing here intersects with active inference's 
treatment of goal-directedness. Consider whether this page warrants a backlink from 
[[free_energy_and_goals]].
```

Thinker agents, when visiting a page, check for a `## Agentic Calls` section addressed to them. If found, they execute the instruction and then mark it as processed (e.g. appending `[✓ processed: 2026-05-07]`).

### Five Core Functions

**1. Orphan Scan**
Walk the vault directory tree, parse all wikilink references across all pages, build a backlink count for every page. Flag any page with 0 backlinks as an orphan; flag pages with 1–2 backlinks as under-connected. Output a ranked list.

**2. Relevance Mapping**
For each orphaned page, analyse its content against the 14 thinker domain vocabularies. Assign relevance scores. A page about "morphogenetic fields" scores high for Levin; a page about "Bayesian brain" scores high for Friston and Hawkins. This determines which agents receive calls.

**3. Agentic Call Injection**
Append a `## Agentic Calls` section to each orphaned or under-connected page with specific, actionable routing instructions. Instructions are written in the agent's voice and framing, not generically.

**4. Cross-Agent Bridge Writing**
Where two thinker domains share high relevance for an orphaned page (e.g. both Friston and Hawkins score > 0.6 on the same page), the Sewing Agent writes a short bridge note in a shared synthesis page (e.g. `wiki/synthesis/friston_hawkins_bridge.md`) connecting the orphaned page to the intersection. This is the "stitch" — two threads pulled together at a node.

**5. Sociogram Health Report**
Append to `wiki/architecture/metrics/` a brief connectivity snapshot: how many pages have 0, 1, 2, 3+ backlinks. Track this over time so progress is visible. One line per run, CSV-appendable.

---

## Part 3: Agent Prompts

### Maintenance Prompt (weekly runs)

```
# Sewing Agent — C2A2 Wiki Maintenance Run
# Role: Orphan Integration and Agentic Call Injection
# Vault: /Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/

You are the Sewing Agent for the C2A2 wiki system. Your role is to find pages 
that are isolated from the knowledge graph and create explicit routing signals 
that bring them into contact with the thinker agents most likely to benefit from 
their content.

## Run Protocol

### Step 1: Build the Backlink Map
Scan all .md files in the vault. For each file, extract all [[wikilink]] references. 
Build a dictionary: {page_name: [list of pages that link to it]}. Count backlinks 
per page. Identify:
- ORPHANS: 0 backlinks
- SPARSE: 1–2 backlinks
- CONNECTED: 3+ backlinks

Report the counts as a one-line CSV row appended to:
wiki/architecture/metrics/connectivity_log.csv
Format: YYYY-MM-DD,orphan_count,sparse_count,connected_count,total_pages

### Step 2: Prioritise Orphans for This Run
Select up to 10 orphaned or sparse pages to process this run. Prioritise:
- Pages in wiki/traditions/ that have no backlinks (thinker content that got 
  disconnected)
- Pages in wiki/inbox/ that were never promoted
- Recently created pages (check file modification dates) with no connections yet

### Step 3: Relevance Mapping
For each selected page, read the full content. Score it against each of the 14 
thinker domain vocabularies:
Levin (bioelectricity, morphogenesis, goal-directedness, non-neural cognition)
Friston (free energy, active inference, predictive coding, Markov blankets)
Hoffman (conscious agents, interface theory, fitness beats truth)
Hawkins (cortical columns, reference frames, thousand brains, SDR)
McGilchrist (hemispheres, attention, embodiment, wholeness)
Kastrup (analytic idealism, dissociation, mind-at-large)
Stump (philosophy of time, identity, persistence, medieval metaphysics)
Fredrickson (positive emotions, broaden-and-build, flourishing, love)
Carroll (quantum mechanics, many worlds, emergence, entropy)
Arkani-Hamed (amplituhedron, cosmology, naturalness, fundamental physics)
Wolfram (computation, ruliad, causal graphs, observer theory)
Wright (evolutionary psychology, religion, cultural evolution, zero-sum)
Rohr (contemplation, liminal space, Richard Rohr, shadow work)
Loughran (integrative synthesis, personal reflection, cross-tradition bridges)

Assign a relevance score (0–1) for each thinker. Any score > 0.4 qualifies that 
thinker for an agentic call.

### Step 4: Write Agentic Calls
For each selected page, append a ## Agentic Calls section (if not already present).
Write one call per qualifying thinker. Each call must:
- Be addressed specifically: [→ {Thinker} agent]:
- Reference the specific content of the page, not generic boilerplate
- Give a concrete instruction (cross-link, review, propose synthesis page, etc.)
- Be written in language appropriate to that thinker's domain

Example format:
## Agentic Calls
*Added by Sewing Agent on YYYY-MM-DD*

[→ Levin agent]: This page discusses pattern formation in slime mould aggregation 
under nutrient stress. This is directly relevant to [[bioelectric_memory]] and the 
question of whether stress-induced morphogenetic signals constitute a primitive form 
of collective decision-making. Review and add a backlink from the Levin thinker node.

[→ Friston agent]: The description of slime mould chemotaxis here maps closely to 
active inference's treatment of chemotaxis as a form of Bayesian inference about 
nutrient gradients. Consider whether this page warrants inclusion in the 
[[predictive_foraging]] synthesis page.

### Step 5: Cross-Agent Bridge Notes
Where two or more thinkers score > 0.5 on the same orphaned page, write a 
bridge note at:
wiki/synthesis/{thinker1}_{thinker2}_bridge.md (create if not exists, append if exists)

The bridge note should:
- Name the orphaned page and why it sits at the intersection
- State one clear synthesis claim that emerges from the overlap
- Suggest a question the wiki does not yet have an answer to

### Step 6: Final Report
Write a brief run report to wiki/architecture/sewing_agent_log.md (append, don't 
overwrite). Include:
- Date and time of run
- Pages processed: [list with backlink counts before/after]
- Agentic calls injected: [count and thinkers addressed]
- Bridge notes written: [list]
- Connectivity snapshot: orphan/sparse/connected totals
- Anything unusual or worth Tom's attention

## Constraints
- Do NOT delete or overwrite existing content. Only append.
- Do NOT process pages in wiki/architecture/metrics/ or wiki/review/archive/ — 
  these are system pages.
- If a page already has a ## Agentic Calls section, add new calls below any 
  existing ones. Do not duplicate calls that are already present and unprocessed.
- Mark your additions with an italicised datestamp so they can be tracked.

## Tone
Write agentic calls in the active, direct voice of a router — not a commentator. 
The agent reading the call should know immediately what action is expected.
```

---

### Bootstrap Prompt (one-time full audit)

```
# Sewing Agent — C2A2 Wiki Bootstrap Audit
# Role: Full Vault Orphan Audit and Initial Agentic Call Seeding
# Vault: /Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/
# This is a ONE-TIME run to establish a baseline connectivity map and seed 
# agentic calls across the entire vault before moving to maintenance schedule.

You are the Sewing Agent performing an initial full audit of the C2A2 wiki. 
This is not a maintenance run — it is a complete survey. Take the time to do 
this thoroughly.

## Bootstrap Protocol

### Phase 1: Complete Backlink Census
Build a full backlink map of the entire vault. Every .md file. Every [[wikilink]].
Output a complete sorted list to:
wiki/architecture/metrics/bootstrap_backlink_census_YYYY-MM-DD.md

Format each entry as:
- Page name | backlink count | linking pages (comma separated)

Then output the connectivity distribution:
- How many pages have 0 backlinks
- How many have 1–2
- How many have 3–5
- How many have 6–10
- How many have 10+

Write the initial CSV row to wiki/architecture/metrics/connectivity_log.csv
(create the file if it does not exist, with header: 
date,orphan_count,sparse_count,connected_count,total_pages)

### Phase 2: Full Orphan Classification
For ALL orphaned and sparse pages (not just 10 — process all of them), 
classify each into one of these categories:

A. THINKER CONTENT: Belongs in a thinker tradition but got disconnected
B. INBOX RESIDUE: Old inbox pages that were never processed or promoted
C. SYNTHESIS POTENTIAL: Cross-tradition content that could anchor bridge notes
D. STRUCTURAL: System/architecture pages that don't need backlinks
E. STUB: Near-empty pages that need content before they can be connected

Report the category breakdown.

### Phase 3: Agentic Call Seeding (Full Pass)
Process ALL category A, B, and C pages. For each:
- Perform relevance mapping against all 14 thinkers
- Inject agentic calls for all thinkers scoring > 0.4
- Write bridge notes for any page where 2+ thinkers score > 0.5

For category B (inbox residue) pages, also add:
[→ C2A2 Orchestrator]: This inbox page was never promoted. Review whether it 
should be formally processed through the inbox pipeline, archived, or deleted.

### Phase 4: Synthesis Page Inventory
List all cross-tradition synthesis pages that SHOULD exist based on the content 
in the vault, grouped by thinker pair. For each:
- State whether the synthesis page already exists
- If it doesn't, write a stub at wiki/synthesis/{thinker1}_{thinker2}_{topic}.md 
  with a one-paragraph frame of the intersection and a ## Agentic Calls section 
  seeding both thinker agents to develop it

### Phase 5: Bootstrap Report
Write a comprehensive report to:
wiki/architecture/sewing_agent_bootstrap_YYYY-MM-DD.md

Include:
- Full connectivity census summary
- Category breakdown of orphans
- List of all pages processed with agentic calls injected
- List of all bridge notes and synthesis stubs created
- Top 10 "highest potential" orphaned pages (most relevant to multiple thinkers)
- Recommended actions for Tom beyond what the agent can do automatically
- Assessment of overall vault health: is the knowledge graph sufficiently 
  connected to support meaningful thinker agent synthesis?

## Constraints
Same as maintenance run — append only, no overwrites, mark all additions with 
datestamp. For this bootstrap run, document EVERYTHING. This is the baseline 
against which all future maintenance runs will be measured.

## Time Budget
This run may take longer than a standard maintenance run. That is expected and 
acceptable. Thoroughness is the priority.
```

---

## Part 4: Schedule Recommendations

### Sewing Agent — Maintenance Mode

**Recommended slot: Sunday, 4:30 AM**

Rationale: All thinker agents complete their Sunday run (Wright + Rohr at 3:00 AM). The periodic monitor fires at ~3:33 AM. By 4:30 AM the vault is in its freshest weekly state — all thinker updates have been written, all agentic calls from thinkers have been processed, and the Sewing Agent can assess the state of the graph with the week's full output visible. The C2A2 Orchestrator fires at 4:34 AM daily — the Sewing Agent's Sunday output will be available to the Orchestrator minutes after it finishes.

**Cron:** `30 4 * * 0` (Sunday 4:30 AM)

**Task ID:** `c2a2-sewing-agent-weekly`

---

### Sewing Agent — Bootstrap Run

**Recommended: Run immediately (one-time, `fireAt`)**

The bootstrap should not wait for the weekly cycle. The vault is already populated, orphans already exist, and the thinker agents are already running without the benefit of agentic call routing. Every week that passes without the bootstrap is a week of lost routing signal. Schedule the bootstrap as a `fireAt` task for the next available window (e.g. tonight after midnight, or manually triggered now).

**Suggested one-time `fireAt`:** `2026-05-02T02:00:00+01:00` (Saturday 2 AM — after the Wolfram agent clears)

**Task ID:** `c2a2-sewing-agent-bootstrap`

---

### Three-Agent-Per-Thinker Upgrade

**Development Milestone: Target completion by end of June 2026**

This is the highest-priority architectural upgrade to the thinker layer. The single-agent-per-thinker model is functional but brittle. The cortical column model requires redundancy and divergence.

**Proposed rollout (one thinker per week, starting Monday 4 May 2026):**

| Week | Thinker | Notes |
|------|---------|-------|
| May 4 | Levin | Most active thinker — high value, good test case |
| May 11 | Friston | Complex domain; triple-agent divergence will be most visible here |
| May 18 | Hawkins | Architect of the model we're implementing — meta-appropriate |
| May 25 | Hoffman | Interface theory amenable to perspectival variation |
| Jun 1 | McGilchrist | Hemisphere model maps naturally to agent polarity |
| Jun 8 | Kastrup | Idealism domain benefits from internal critique pressure |
| Jun 15 | Carroll | Physics domain — skeptical agent can push hard on claims |
| Jun 22 | Arkani-Hamed | Similar to Carroll |
| Jun 29 | Wolfram | Solo on Saturday — replace single with triple |
| Jul 6 | Stump | Medieval metaphysics — historical/contemporary agent split |
| Jul 13 | Fredrickson | Positive psychology — critical agent important for rigor |
| Jul 20 | Wright | Evolutionary psych — contested domain, benefits from adversarial agent |
| Jul 27 | Rohr | Contemplative tradition — phenomenological agents |
| Aug 3 | Loughran | Meta-reflective agent for Tom-as-thinker thread |

**Per-thinker agent configuration (template):**
- Agent A (Sympathetic): High-fidelity representation of the thinker's own framework; assumes good faith; builds on prior syntheses
- Agent B (Neutral): Applies the thinker's framework without assuming correctness; tests claims against vault evidence
- Agent C (Skeptical/Critical): Applies adversarial pressure; looks for gaps, contradictions, weak evidence; cross-checks against opposing thinker traditions

**Tiebreaker:** A lightweight orchestration pass runs after all three agents complete. Where agents disagree on a claim or synthesis, the disagreement is logged to the thinker's synthesis page as an open question rather than resolved arbitrarily.

---

## Summary Table

| Item | Priority | Status | Action Required |
|------|----------|--------|-----------------|
| Sewing Agent bootstrap | High | Not started | Schedule `fireAt` task immediately |
| Sewing Agent maintenance | High | Scheduled ✓ | Sunday 4:30 AM, `c2a2-sewing-agent-weekly` |
| Three-agent-per-thinker upgrade | High | Not started | Begin Levin week of May 4 |
| Loughran thinker agent | Medium | Not scheduled | Decide if first-person agent is in scope |
| Wright/Rohr agent individuation | Low | Unclear | Verify separate prompts exist for each |
| Weekend lit search review | Low | Not scheduled | Consider adding a Friday/Saturday review pass |
