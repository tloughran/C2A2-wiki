---
title: Unsaid-Edges Map
pathway_id: unsaid_edges
status: drafted
created: 2026-05-13
depends_on: [perspective_lattice, generative_canvas]
enables: []
isme_critical: no
---

# Pathway 07: Unsaid-Edges Map

## Purpose

The perspective lattice (Pathway 04) is large — 12 perspectives × thousands of vault nodes, plus 55 pairwise T-T relationships, plus the PRS cross-products, plus the Summa entries. Most cells in this lattice are populated. Some are not. The unpopulated cells — the *empty edges* in the network of inquiries — are research-program-generating facts in their own right.

This pathway exists to surface those empty edges deliberately. The pairwise T-T relationships that have never been interrogated, the PRS triplets that have never been tested across traditions, the Summa questions that no commentator in any of the eleven thinkers' communities has engaged — each is a candidate for the next conversation, the next podcast, the next graduate student's research direction. In MacIntyrean terms, the traditions that haven't yet spoken to one another are exactly where the next progress lives.

## Function set

The unsaid-edges map has three moving parts:

1. **Emptiness query.** A lookup against the perspective lattice that returns cells with no vault attestation above a confidence threshold. "Give me all pairwise T-T relationships with no shared discussion." "Show me PRS triplets where no other tradition has proposed a resource." "List Summa II-II questions with no commentary in the contemporary version."

2. **Two-filter significance scoring.** Each empty edge gets two independent scores, combined into a priority class:

   - **How often** (demand signal): count of probe events (Pathway 03) and voice mentions (Pathway 01) on adjacent cells, count of lattice queries that landed near this cell, count of dialogue turns that hovered around it. Captures *attention* — is anyone currently trying to engage this?
   - **How important** (structural signal): how many proximate cells are populated, how much PRS overlap the adjacent thinker-pages share, how many cross-references exist in nearby empty-edge contexts. Captures *conceptual ripeness* — is the neighborhood rich enough that engagement would land?

   The combination produces a 2×2 priority matrix:

   |                  | Low importance       | High importance                              |
   |------------------|----------------------|----------------------------------------------|
   | **High demand**  | Foundational gap     | Established research direction (in-flight)   |
   | **Low demand**   | Quiet backwater      | **Strong research-program candidate**        |

   - *Low demand × High importance* (the strongest category): the system's distinctive contribution. The conceptual ground is fertile but no one has yet noticed the question. MacIntyrean territory — work that opens new questions rather than ratifying existing ones.
   - *High demand × High importance:* an established research direction. The system confirms it; it's not what the system uniquely surfaces.
   - *High demand × Low importance:* demand without scaffolding — interest exists but the conceptual ground isn't yet ready; flag as a foundational gap.
   - *Low demand × Low importance:* quiet backwater; surface only when filters are widened.

3. **Visualization.** The map renders as a perspective-lattice viewer (built on the generative canvas, Pathway 06) where empty cells are foregrounded — not absent, but visibly empty, colored by priority class. The **Low demand × High importance** quadrant gets the strongest visual emphasis (boldest color, largest annotation), reflecting that this is the category the system distinctively contributes. Hovering over an empty cell shows the two scores plus a one-line description of what an investigation might address.

## Architecture sketch

```
perspective_lattice (Pathway 04)
        ↓
   emptiness query
   ├─ what cells have no attestation?
   └─ what attestations are weak (low provenance)?
        ↓
   two-filter significance scoring
   ├─ how often (demand): probes, mentions, lattice queries, dialogue hovering
   └─ how important (structural): proximate populated cells, PRS overlap, cross-references
        ↓
   priority class (2×2 matrix; Low×High emphasized as strongest candidate)
        ↓
   render via generative canvas (Pathway 06)
   ├─ foreground empty cells
   ├─ color by priority class (Low×High brightest)
   └─ click reveals candidate research question + scores
```

## Decisions taken

- **Empty cells are first-class data.** Not absences to be filled, but findings to be displayed. The map is a research-program-generating instrument.

- **Two-filter scoring: how often × how important; Low × High is the strongest candidate** (decided 2026-05-13, refined in same session). A single "latent affinity" score conflated demand and structural ripeness. Splitting them and combining into a 2×2 matrix surfaces four meaningfully different situations, with the **Low demand × High importance** quadrant identified as the system's most distinctive contribution: territory where the conceptual ground is fertile but no one has yet seen the question. That is research-program candidacy in the strong sense — work that opens new questions rather than ratifying existing ones. The Low×High quadrant gets visual emphasis in the map.

- **Foregrounding rather than filtering.** The map doesn't hide populated cells; it visually emphasizes the empty ones. Audience sees both the activity and the gaps simultaneously.

- **Provenance applies in reverse.** Where the rest of the system uses provenance footers to attest "this is what the vault says," this map attests "this is what the vault does *not* yet say." The negative attestation is its own kind of fidelity.

## Open questions

- **Threshold for "empty."** Sometimes a cell has trace vault attestation that's too thin to count as engaged. Where's the line between "lightly touched, still effectively empty" and "engaged"? Probably tunable, with a slider in the map UI.

- **Time dimension.** Empty cells get filled over time. Should the map remember which cells used to be empty? A "what got addressed in the last six months" track would itself be a progress indicator.

- **Action surface.** When a user finds an interesting empty edge, what's the natural next step? "Generate a candidate research question," "draft an outreach DM to the relevant lab," "open a GitHub Issue tagged 'research-program-candidate'" — each is plausible. The map should make at least one obvious.

- **MacIntyrean framing.** Worth working out the language carefully for the ISME audience. Empty edges are not *gaps to be patched* (which would carry an Enlightenment-rationalist subtext). They are loci where traditions have not yet found grounds to speak — and MacIntyre's framework treats that as a positive feature of intellectual life, not a deficiency. The map should embody that frame in its copy and labels.

## Edges

- **perspective_lattice (04):** primary data source. The map is the dual of the lattice.
- **generative_canvas (06):** the map is rendered on the generative canvas — a custom perspective-lattice viewer with empty-cell foregrounding.
- **voice_dialogue (01):** "what hasn't been said about X" becomes a queryable question. The agent can read off candidate research directions from the map.
- **outreach_automation (12):** high-score empty edges become candidate outreach moments — invitations to the lab whose tradition could plausibly engage that empty cell.
- **apprentice_mode (15):** apprentices ramping into a tradition see the empty edges from their tradition as the frontier; the curriculum can guide them toward live questions.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- This pathway was the most distinctive in the agent's dream-along contribution: "Every pairwise T-T edge that has never been interrogated, every PRS triplet that has never been tested against another tradition's framework, is a research-program-generating fact." Tom affirmed the alignment ("you've nailed it"). The MacIntyrean framing is the core motivation.

## Status

Drafted in prose. Implementation depends on the perspective lattice (Pathway 04) being in place — the emptiness query needs cells to query. Significance scoring is light: a few graph traversals over the lattice and the vault. Visualization rides on the generative canvas (Pathway 06).
