---
title: Generative-Canvas Visualization
pathway_id: generative_canvas
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue, ambient_viz, probing_channel]
enables: [unsaid_edges]
isme_critical: no
---

# Pathway 06: Generative-Canvas Visualization

## Purpose

The visualization surface stops being a fixed palette of pre-built tools (Sociogram, 3D PRS, narration, on-demand plots) and becomes a *generative canvas*: any active intelligence can request a representation that doesn't yet exist as a built tool, and the system produces it. The agent shifts from operator-of-existing-instruments to instrument-maker.

Concrete example from Tom's session: "We had a relationship between three thinkers, which seemed linear at first, but then triangular, and then we added a fourth, a fifth, and other vertices. We had confidence levels associated with the various connections, which you could imagine representing by thickness of edge." That's not a Plotly chart type. It's a custom topological object that grows as the conversation extends it. The generative canvas is where requests like that land.

## Function set

The canvas has four moving parts:

1. **Request interpreter.** A code-writing agent receives a natural-language request, identifies the visualization idiom (force-directed graph, geometric solid, custom Plotly variant, three.js scene, WebGL shader), looks up vault data needed to populate it, and generates a self-contained code block.

2. **Sandboxed render surface.** A canvas region in the whiteboard tab where the agent's generated code runs. Sandboxed via iframe with a restrictive Content Security Policy — generated code can render, can read data the broker provides, cannot execute external network calls or access the host page directly.

3. **Continuity-of-object across edits.** A generated visualization persists with a session-scoped ID. "Now add Friston" doesn't replace the figure; it reshapes the existing object. The agent has a handle on the running visualization and can issue mutations against it ("add vertex," "thicken edge," "rotate view") rather than re-generating.

4. **Probe and bias integration.** Elements in the generated visualization subscribe to the probe stream (Pathway 03) and the mention signal stream (Pathway 02), just like Sociogram nodes do. A custom thinker-simplex behaves the same way the Sociogram does when a thinker is mentioned — its corresponding vertex highlights or shifts gravity.

## What's sandboxing? *(apprentice note)*

Sandboxing here means the generated code runs in an isolated browser environment (an `<iframe>` with strict permissions) that cannot reach into the host page, cannot make arbitrary network calls, and cannot persist anything outside its own region. The reason: a code-writing agent that runs unchecked code is a security hole — generated code might be wrong, might be deliberately adversarial in a public deployment, might leak data. The sandbox is the equivalent of running a script inside a container instead of on the host. The agent gets to be creative within the sandbox; the rest of the system stays safe.

## Architecture sketch

```
voice/text request:
"draw three thinkers as a triangle with edges weighted by confidence"
        ↓
   code-writing agent (broker-side)
   ├─ identify viz idiom (here: force-directed graph)
   ├─ look up vault data (thinker IDs, confidence weights on relationships)
   ├─ generate self-contained code (D3 or three.js)
   └─ ship to client
        ↓
   sandboxed iframe in whiteboard tab
   ├─ runs the generated code
   ├─ renders the geometry
   ├─ subscribes to probe stream
   └─ subscribes to mention signals
        ↓
   mutation requests ("now add Friston")
   ├─ agent receives mutation request
   ├─ generates a diff or patch against the running viz
   └─ sandbox applies the diff
```

## Decisions taken

- **In-browser code generation, sandboxed.** The agent writes D3 / three.js / Plotly / WebGL into a sandboxed iframe rather than pre-building viz types. Sandbox is the security boundary; generated code stays inside.

- **Continuity of object across edits.** A canvas instance has a session-scoped ID and persists across mutation requests. "Add Friston" reshapes; doesn't replace.

- **Provenance still attached.** Every generated visualization carries metadata: the request that produced it, the vault data it pulled, the timestamps. Visible in a small expandable footer.

- **Joins the ambient layer.** Custom viz subscribes to the same probe and mention streams the Sociogram does. The custom thinker-simplex doesn't have a separate command grammar; it participates in the system's shared-attention layer.

- **Vault schema requirement surfaces here.** The thinker-simplex example requires confidence weights on T-T relationships. Some of that may live implicitly in PRS structure; some likely needs explicit numbers in edge frontmatter. The "quick lookup" only feels quick if the schema already supports it — otherwise the agent improvises and provenance gets murky. Tracked as a vault-schema task.

- **Viz library set: D3, three.js, Plotly, bare canvas/WebGL** (decided 2026-05-13). D3 for graphs and custom 2D; three.js for 3D geometry like the thinker-simplex; Plotly for charts that overflow Pathway 05's grammar; bare canvas/WebGL for rare cases. Sandbox surface is validated for each library; new libraries require explicit broker-side approval before generated code can target them.

## Open questions

- **Code-generation provider.** A model that writes correct, runnable D3 / three.js on first try is a real ask. Sonnet-class models have been reliable; gpt-4o variants are competitive. Worth a small benchmark of "request → working render" on the thinker-simplex example.

- **Mutation grammar.** What vocabulary does the mutation handler understand? "Add Friston" is structured enough; "make it more like a sphere" is harder. Probably start with structured mutations (add/remove vertex, edit edge weight, change layout) and grow the natural-language coverage.

- **Failure modes.** Generated code can fail to render. What's the fallback? Probably: agent verbally announces the failure, offers an alternative ("I can do this in 2D instead of 3D"), keeps the original viz visible if any.

## Edges

- **broker (00):** code generation happens broker-side; the broker also stamps provenance metadata on the shipped code.
- **voice_dialogue (01):** requests for custom viz arrive via the dialogue layer; agent narrates the generated viz the same way it narrates Sociogram or Plotly views.
- **ambient_viz (02):** custom viz subscribes to mention signals; vertices for currently-discussed thinkers bias just like Sociogram nodes do.
- **probing_channel (03):** elements in the custom viz raise probe events with `element_type: "canvas_region"` or specific custom types.
- **whiteboard (05):** custom canvas renders inside the same whiteboard tab Plotly does, sharing tab real estate and the data layer.
- **unsaid_edges (07):** unsaid-edges visualizations can be built on the generative canvas — empty edges in a perspective lattice rendered with their own grammar.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- Emerged from Tom's expansion: "What I'd really like to do is ask for any visualization I'd like, and have it produced on the fly." The thinker-simplex example crystallized the requirement: not a Plotly chart type, not the Sociogram, a custom object that grows as the conversation extends it.

## Status

Drafted in prose. The browser-side generative-canvas pattern is reachable (sandboxed iframes, code-writing models, D3/three.js as the working substrate). The un-buildable starts past this — requests for data we don't have, modalities the browser can't render, cognitive states no instrument can observe. Implementation begins with the sandbox harness and a small benchmark of generation reliability on the thinker-simplex case.
