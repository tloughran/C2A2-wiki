# Provenance Protocol Specification

## Purpose

Every inter-agent message in C2A2's self-awareness system carries a **provenance header** that establishes a chain-of-custody for architectural claims. This header answers three critical questions:

1. **Where did this item originate?** Which agent or human author first identified it?
2. **What transformations has it undergone?** What work has been applied to it as it moved through the system?
3. **Was the original designer aware of this premise?** (This distinction determines downstream epistemic weight.)

The provenance protocol ensures that any downstream consumer — agent or human reviewer — can trace an architectural claim to its source, understand its epistemic status, and know whether the original designers were consciously committed to it (ASSUMPTION) or whether it was surfaced after the fact through inference (PRESUMPTION).

## Header Format

Every item routed between agents carries a PROVENANCE block with the following fields:

```
PROVENANCE:
  Origin: [14a | 14b]
  Chain: [full path, e.g., 14a → 15a → 14a]
  Original item: [ASSUMPTION-NNN or PRESUMPTION-NNN]
  Item type: [ASSUMPTION (stated) | PRESUMPTION (unstated — surfaced by inference)]
  Transform at each step:
    [14a or 14b]: [what you did — e.g., "extracted from session transcript"]
    [15a]: [if applicable — "searched for supporting literature"]
    [15b]: [if applicable — "searched for challenging literature"]
  Current status: [UNTESTED | SENT-TO-15a | SENT-TO-15b | SEARCHED | SUPPORTED | CHALLENGED | PARTIALLY-SUPPORTED | PARTIALLY-CHALLENGED | CONTESTED | NOVEL | GROUNDED]
```

### Field Descriptions

**Origin:** The agent that first created this item.
- `14a` — Item was extracted by Agent 14a (Assumption Extractor) from a stated claim
- `14b` — Item was surfaced by Agent 14b (Presumption Detector) through inference from unstated premises

**Chain:** The complete path the item has traveled through agents. Examples:
- `[14a]` — Item originates from 14a, not yet routed to literature agents
- `[14a → 15a]` — Item sent to Agent 15a for supportive literature search
- `[14a → 15b]` — Item sent to Agent 15b for challenging literature search
- `[14a → 15a → 14a]` — Item returned to 14a after 15a search completes
- `[14a → 15a, 15b → 14a]` — Item searched by both 15a and 15b, results returned to 14a

**Original item:** The unique identifier of this item in its registry file.
- Format: `ASSUMPTION-NNN` (for assumptions) or `PRESUMPTION-NNN` (for presumptions)
- This ID is permanent and does not change as the item moves through the chain

**Item type:** Distinguishes assumptions (stated, designer-aware) from presumptions (unstated, inferred).
- `ASSUMPTION (stated)` — Original designers were explicitly aware of this premise
- `PRESUMPTION (unstated — surfaced by inference)` — Original designers did not explicitly articulate this premise; it was reconstructed from conversation patterns by Agent 14b

This distinction is the **epistemic honesty marker**. Any downstream reader seeing `PRESUMPTION` knows to weight it differently than an `ASSUMPTION`.

**Transform at each step:** A record of what each agent did when this item passed through.
- Agent 14a: `"Extracted from session transcript: [context]"`
- Agent 14b: `"Surfaced as unstated presumption via inference: [evidence in conversation]"`
- Agent 15a: `"Searched for supporting literature; found [summary]"`
- Agent 15b: `"Searched for challenging literature; found [summary]"`

**Current status:** The item's epistemic state in the workflow (see Status Lifecycle section below).

## Item Type Taxonomy

### ASSUMPTION (stated)

An ASSUMPTION is a premise that the original designers articulated explicitly. It appears in design discussions, decision rationale, or hypothesis statements. Agent 14a extracts these.

Examples:
- "We're assuming that the 11 traditions adequately represent the research space."
- "The design relies on the hypothesis that cross-tradition connections reveal structural homologies."
- "We expect that agents can meaningfully instantiate research traditions."

**Marker:** `Item type: ASSUMPTION (stated)`

**Implication:** Original designers were aware of this premise and made a deliberate commitment to it (or at least acknowledged it as a working hypothesis). Downstream consumers can assume this represents a considered design choice.

### PRESUMPTION (unstated)

A PRESUMPTION is a premise that the designers relied upon but never explicitly stated. It lives in the gaps of conversation — the unquestioned framings, absent alternatives, transferred assumptions, and unexamined success criteria. Agent 14b surfaces these.

Examples:
- "The conversation assumed that more traditions would be better without questioning the cost-benefit tradeoff."
- "The design presumed that principles from Thousand Brains Theory transfer intact to multi-agent AI systems without checking transfer conditions."
- "Participants presumed that the PRS triplet structure captures the important aspects of research progress without exploring what it misses."

**Marker:** `Item type: PRESUMPTION (unstated — surfaced by inference)`

**Implication:** Original designers were NOT aware of this premise — it was embedded in their thinking without conscious acknowledgment. Downstream consumers should recognize this as a vulnerability worth examining.

**Note on tone:** Presumptions are not criticisms or accusations. They are the normal substrate of all thinking. No system operates with complete epistemic transparency. The value of surfacing them is visibility, not blame.

## Status Lifecycle

Items move through a state machine as they flow through the agents:

### Starting State

**UNTESTED**
- Initial state for all newly extracted assumptions and surfaced presumptions
- Item is valid and identified but has not yet entered the literature search pipeline
- Next step: Agent 14a or 14b routes to 15a and 15b

### In-flight States

**SENT-TO-15a**
- Item has been queued for Agent 15a (supportive literature search)
- Awaiting 15a's response
- Next step: 15a completes search and returns results

**SENT-TO-15b**
- Item has been queued for Agent 15b (challenging literature search)
- Awaiting 15b's response
- Next step: 15b completes search and returns results

**SEARCHED**
- Item has been searched by at least one of 15a or 15b
- Awaiting completion by the other agent (if both were initiated)
- Next step: Second search completes, then 14a/14b reconciles results

### Terminal States (after reconciliation)

**SUPPORTED** (high confidence)
- Both 15a and 15b found support, or 15a found strong support and 15b found no challenge
- Literature consensus: the assumption/presumption is well-grounded
- Next step: Document as trusted premise in architecture; incorporate into design decisions

**PARTIALLY-SUPPORTED**
- 15a found support but with important caveats or scope limitations
- 15b found no challenge or weak challenge
- Literature consensus: the assumption/presumption is valid under specific conditions
- Next step: Document conditions explicitly; incorporate with noted constraints

**CHALLENGED** (from 15b only)
- Only 15b found evidence; 15a found no support
- Literature consensus: the assumption/presumption is contradicted or unsupported
- Next step: Revisit design decision; consider alternatives; flag as risk

**PARTIALLY-CHALLENGED**
- 15a found support but 15b found credible challenges
- Literature consensus: the assumption/presumption is contested; evidence goes both ways
- Next step: Document both positions; make explicit the tradeoff; add to risk register

**CONTESTED**
- 15a found strong support but 15b found strong challenges
- Literature consensus: the assumption/presumption is actively disputed
- Next step: Treat as high-risk assumption; design mitigations; plan for testing

**NOVEL**
- Neither 15a nor 15b found any existing literature addressing this claim
- Literature consensus: no data yet — this may be an original contribution
- Next step: Flag as potential original research; track for publication; continue monitoring

**GROUNDED**
- Status reserved for assumptions/presumptions that have been validated through C2A2's own empirical work (post-implementation testing)
- Literature may not exist yet, but C2A2 has direct evidence
- Next step: Document case and contribute back to literature

## Chain Notation

The chain is written as a sequence of agent labels showing the path an item has traveled:

**Simple chains (single direction):**
- `[14a]` — Just extracted, not yet routed
- `[14a → 15a]` — Routed to 15a, currently in their queue
- `[14a → 15a → 14a]` — Returned to 14a after 15a search

**Branching chains (both literature agents):**
- `[14a → 15a, 15b]` — Routed to both 15a and 15b simultaneously
- `[14a → 15a, 15b → 14a]` — Searched by both; results returned to 14a

**Extended chains (if reconciliation agents are added):**
- `[14a → 15a, 15b → 16_reconcile → 14a]` — Future extension for automated reconciliation

Each arrow `→` represents a handoff. The chain is read left-to-right as a temporal sequence.

### Recording Transforms

When an item moves between agents, both the sending and receiving agents update the PROVENANCE block:

**At send time (Agent 14a sending to 15a):**
```
Transform at each step:
  14a: Extracted from session: "We assume traditions are adequate units of analysis"
  15a: [pending]
```

**At return time (Agent 15a returning to 14a):**
```
Transform at each step:
  14a: Extracted from session: "We assume traditions are adequate units of analysis"
  15a: Searched for supporting literature; found 8 sources supporting cross-domain unity; strength: Strong
```

This creates an audit trail visible to any downstream reader.

## Reconciliation Rules

Agent 14a (for assumptions) or 14b (for presumptions) reconciles the results from 15a and 15b. The reconciliation rules are:

| 15a Result | 15b Result | Final Status | Confidence | Interpretation |
|------------|------------|--------------|------------|---|
| **SUPPORTED** | **NO-SUPPORT-FOUND** | **SUPPORTED** | High | Strong consensus in literature |
| **SUPPORTED** | **WEAK-CHALLENGE** | **SUPPORTED** | Moderate | Mostly supported; minor objections |
| **SUPPORTED** | **STRONG-CHALLENGE** | **CONTESTED** | Low | Active dispute in literature |
| **PARTIALLY-SUPPORTED** | **NO-SUPPORT-FOUND** | **PARTIALLY-SUPPORTED** | Moderate | Supported with scope limits |
| **PARTIALLY-SUPPORTED** | **WEAK-CHALLENGE** | **PARTIALLY-SUPPORTED** | Low | Limited support; some objections |
| **PARTIALLY-SUPPORTED** | **STRONG-CHALLENGE** | **PARTIALLY-CHALLENGED** | Low | More challenged than supported |
| **NO-SUPPORT-FOUND** | **NO-CHALLENGE-FOUND** | **UNTESTED** | N/A | Literature gap; no data either way |
| **NO-SUPPORT-FOUND** | **CHALLENGED** | **CHALLENGED** | Moderate | Only evidence is against |
| **NO-SUPPORT-FOUND** | **STRONG-CHALLENGE** | **CHALLENGED** | High | Clear evidence of invalidity |

Special case:
- If search yields no results in either direction (neither 15a nor 15b finds relevant literature), status remains **UNTESTED** and tagged as a **literature gap**.
- If a claim is genuinely novel (no prior literature), 15a flags it as **NOVEL** and recommends treatment as original contribution.

## Downstream Visibility

### For Items Tagged ASSUMPTION

Any downstream reader seeing `Item type: ASSUMPTION (stated)` knows:
- The original designers explicitly acknowledged this premise
- It appeared in design discussions or decision rationale
- The system is operating with informed consent on this assumption
- If challenged, the response is "we knew this and accepted the risk"

### For Items Tagged PRESUMPTION

Any downstream reader seeing `Item type: PRESUMPTION (unstated — surfaced by inference)` knows:
- The original designers did NOT explicitly articulate this premise
- It was embedded in their thinking unconsciously
- It represents a potential vulnerability or blind spot
- If challenged, the response is "we didn't see this; let's examine it"

This distinction is critical for epistemic honesty. A system that surfaces its blind spots is more trustworthy than one that doesn't.

### Usage in Downstream Decisions

When an agent or human reviewer encounters an item with provenance:

1. **Check the Item Type** — Is this an assumption or presumption? If presumption, apply extra scrutiny.
2. **Check the Status** — Is it SUPPORTED, CONTESTED, or NOVEL? Route accordingly.
3. **Check the Chain** — Where has this item been? What transforms has it undergone? Are there gaps?
4. **Check the Transform Record** — What did each agent do? Can you reproduce their work if needed?

## Integration with Dispatch Format

The provenance header is designed to integrate with C2A2's enhanced dispatch format used by tradition agents. The dispatch includes two new fields:

```
reference_frame_location: [which assumption/presumption registry this item relates to]
conceptual_bearing: [the chain notation and current status]
```

Example dispatch entry:
```yaml
item_id: "ASSUMPTION-047"
summary: "The 11 traditions adequately represent the research space"
reference_frame_location: "wiki/architecture/assumptions.md#ASSUMPTION-047"
conceptual_bearing: "[14a → 15a, 15b → 14a]; status=SUPPORTED"
provenance_chain: "[14a → 15a, 15b → 14a]"
current_status: "SUPPORTED"
item_type: "ASSUMPTION (stated)"
confidence: "High"
```

This allows tradition agents to:
- Quickly assess whether they're working with a tested assumption or a novel one
- Trace any architectural claim back to its source
- Adjust their behavior based on the epistemic status of the assumptions they depend on
- Flag violations of presumptions they encounter in practice

## Implementation Notes

### File Locations

- **Source records:** Items appear first in `wiki/architecture/assumptions.md` (14a) or `wiki/architecture/presumptions.md` (14b)
- **Queue for literature search:** `wiki/architecture/for_lit_search.md` (shared by 14a and 14b)
- **Search results:** `wiki/architecture/lit_search_results/for/` (15a) and `wiki/architecture/lit_search_results/against/` (15b)
- **Returns:** `wiki/architecture/lit_search_returns.md` (joint return point from 15a and 15b)

### Versioning

The PROVENANCE block is a living document. It is updated at each step of the chain:
- When 14a extracts an item, the block is initialized
- When 15a or 15b searches it, the block is updated with their results
- When 14a/14b reconciles, the block receives the final status
- If an item's status changes due to later evidence, the block is appended (never overwritten)

### Immutability

Once an item enters the provenance system, its `Original item` ID never changes. The item may be re-searched, re-evaluated, or superseded by a newer item, but the original ID remains stable for traceability.

### Epistemic Weight

The combination of item type + status + chain + confidence creates a powerful epistemic signal:
- **Highest weight:** `ASSUMPTION` + `SUPPORTED` + high confidence (designer-aware, literature-backed)
- **High weight:** `ASSUMPTION` + `PARTIALLY-SUPPORTED` (designer-aware, conditionally backed)
- **Medium weight:** `PRESUMPTION` + `SUPPORTED` (designer-unaware but literature-backed)
- **Lower weight:** `PRESUMPTION` + `CONTESTED` (designer-unaware, disputed)
- **Lowest weight:** Any item + `NOVEL` (no literature baseline)

Downstream agents and human reviewers should apply proportional skepticism based on this signal.

---

**Version:** 1.0  
**Status:** Authoritative Specification  
**Last updated:** 2026-04-10  
**Maintained by:** Agent 12 (Master C2A2 Agent)  
**Related agents:** [[14a_assumption_extractor_agent]], [[14b_presumption_detector_agent]], [[15a_lit_search_for_agent]], [[15b_lit_search_against_agent]]
