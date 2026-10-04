# Sociogram

**family** graph · **tier** T3 (the only T3) · **manifest entry** yes, `sociogram`

## identity
`wiki/wiki_narration.html`, 63,245,369 B. Explorer tab "Sociogram", the default
active tab (`explorer.html:452`, `data-src="wiki_narration.html"`; iframe at
`:479`). **Generated** by `wiki/c2a2-wiki-narration/scripts/generate_visualization.py`
— the whole HTML is one Python template (`generate_html`, `:410`) with data
injected and written by `main()` (`:4246`). Extractor:
`extract_vault_data.py`. Regen: `wiki/c2a2-wiki-narration/regen_sociogram.sh`
(Mac) or `scripts/regen_summa_sociogram.sh` (`--summa`, generate to temp,
`validate_html.py`, then `mv`, `:48-89`). 5,287 nodes / 161,221 links per
`scripts/build_meta.json`.

**The same file is also loaded twice more**, as the Agent Map's sociogram
sub-view (`agents_tab.html:383, 1626-1631`, `#agents` preset, ~25 MB) and as
Curriculum Tools' (`summa_explorer.html:451, 1274`, ~29 MB). Three routes, one
document. See `21_nested_subsurfaces.md`.

## purpose
A force-directed map of every vault markdown file, the Summa nodes and the
agent-activity actors, with edges for wikilinks, mentions, shared references and
asserted cross-tradition signals, so a reader can see how the thinkers and
structures interconnect and open any file.

## data sources
Everything is inlined at generation time; no runtime data fetch.
- `extract_vault_data.py`: `rglob("*.md")` (`:500`), `parse_changelogs` (`:210`),
  `parse_findings` (`:251`), `parse_decisions` (`:311`),
  `parse_cross_connections` (`:358`), `parse_summa_vault` (`:1076`, `--summa`).
- `wiki/agents/openstory/agent_node_edges.json` as the generator's third arg
  (`regen_summa_sociogram.sh:54`; `generate_visualization.py:4253`).
- `wiki/lib/c2a2-search.js` read at generation (`:418`) and inlined as
  `window.C2A2Search`; used only by the metered "Ask AI" path.

## entities and fields
- **Node** (`:179-186`): `id` (vault path), `label`, `directory`, `date`,
  `color`, `group` (e.g. `traditions/levin`, `summa`, `architecture`,
  `agent-activity`), `size`, `content` (full markdown), `has_tags[]`,
  `references[]`. Agent nodes add `kind`, `category` (`:307-318`).
- **Link** (`:238-246`): `source`, `target`, `type` (signal | wikilink | mention
  | reference), `bridge` (cross | same), `score_deg`, `score_type`,
  `score_bridge`, optional `reference`. Agent edges: substrate | projected | flow.
- **Side tables**: `FINDINGS` (`id, finding, programs, type`),
  `CROSS_CONNECTIONS` (`id, question, programs, notes, nature`) — both searched
  by `runSearchLocal` (`:3601-3606`).

## cut
Fully expressible, and the manifest already did it from a live runtime sweep of
84 controls (`manifests.json` sociogram `_coverage_note`).

| dim | kind | binding |
|---|---|---|
| group filters | set | 32 `input[data-group]` → `groupVisibility` (`:1353,1359`); `#chk-all`, `#chk-none`, `#chk-all-traditions`, `#chk-all-structure` |
| edges | set | `showEdgeType`: `#chk-edge-signal|-wikilink|-mention|-reference`, `#chk-all-edges` (`:830-833`) |
| bridges | set | `showEdgeBridge`: `#chk-edge-cross|-same` (`:836,841`) |
| layers | set | `showLayer`: `#chk-layer-substrate|-projected|-flow`, `#chk-substrate-context` (`:846-849`) |
| tags | set | `showTagKind`: `#chk-tag-finding|-decision|-cross|-open`, `#chk-all-tags` |
| highlight | value | `#search-input` → `SEARCH_CUT {query, ids[]}` (`:1025`) |
| selection | value | `currentRightNode` (+ `currentLeftNode` for an edge) |
| camera | value | d3 `zoomBehavior` transform; action `#btn-fit-all` |
| mode | value | `#layout-mode` (free \| discipline-year), `#score-mode` (balanced \| connected \| cross-tradition \| editorial) |
| toggles | value | `#chk-hold-forces`, `#chk-hover-names` |
| continuous | value | `#brightness-slider`, `#date-slider` (`DATE_START`→`DATE_END`) |

**The cut is split across two stores and no single call returns it.** Filters are
reachable only through `groupVisibility` / `activeFilters()`; the highlight only
through `c2a2ReadCut()`. The one function that returns the *view state* is
`buildDescriptor()` (`:4151-4177`), answered over `postMessage describe_view`:
`{selected, filters, counts:{passingNodes, inViewNodes, totalNodes, passingEdges,
inViewEdges, totalEdges}, legend, dominant}`. A third, lossy reader —
`getCurrentViewState()` (`:3678`) — scrapes node opacities. See the main
document §4.2: this page is the primary evidence against the
`c2a2ReadCut`-as-pivot hypothesis.

The **date slider is excluded by design** (manifest §14.4), so a date window is
not part of the semantic cut. Whether it ought to be is a live design question,
and the same question Metabolism raises (`04_metabolism.md`).

## change signal
Not defined anywhere. Natural grain is **per regen**, diffing node `id` + a
content hash against the prior extract (inferred). `generate_visualization.py:4296-4312`
already writes `build_meta.json` (node/link counts, `nodes_by_group`,
`substrate_skipped`), which `regen_sociogram.sh:23-32,85-94` uses as a delta
guard — aggregate counts only, not per node. Per-node is derivable: nodes carry
`date` (git or frontmatter) and `has_tags`, and "new FINDING / DECISION / CROSS
ids" is readable off `references[]`.

## export shape
Nothing exists. The only output is `popoutPage()` (`:2079`), which opens a node's
markdown in a new window (the manifest excludes it as chrome).
- CSV, node grain: `id, label, group, directory, date, has_tags, references, degree`
  (`content` optional — it is the bulk of the 63 MB).
- CSV, edge grain: `source, target, type, bridge`.
- JSON: the node object plus its neighbour ids.

## narration
Rich and generated. A semantic narration engine (`:3040`) builds text from
`FINDINGS_BY_GROUP`, `CROSSES_BY_GROUP`, `GROUP_TO_PROGRAMS` into
`#narration-text` (`:3171-3173`); a timeline narration (History / Recent /
Latest) at `:3176`; `IDLE_NARRATION` captured at init (`:4040`). Per-tab help via
`scripts/derive_tab_help.py`. It is the only surface with **three** knowledge
files (`sociogram.graph.default.md`, `.node_selected.md`, `.edge_selected.md`),
i.e. the only one whose narration is state-dependent.

## current capability
- Contract: **full** — `c2a2Find` (`:3656`), `c2a2Clear` (`:3664`),
  `c2a2ReadCut` (`:3669`). Only surface in the project.
- `window.c2a2Ask` (`:3799`) wrapping the metered `askSociogram`.
- `inShell()` routes the page's own box to the shell's `find` by postMessage
  (`:3542-3553`) — the alias road, verified by `test_voice_shell.cjs` row X b.
- State bus: **yes** — `describe_view` (`:4151`) and a `view_changed` emitter
  (`:4196`). Only surface with one.
- Export: none. "?" : three in-page popovers (`#btn-edge-help`, `#btn-edges-help`,
  `#btn-tags-help` with `#edges-help-popover`, `#tags-help-popover`, `:759-911`),
  hand-written, manifest-excluded as "chrome, no view state"; plus a shell
  `descriptions` entry.
- Manifest: 32 caps, `knobs: []` (`_knobs_note`: no `set` verb in v1), 10
  `dim_coverage` rows, 4 families, 4 `controls_deferred`
  (`#layout-mode`/`#score-mode`; `#chk-hold-forces`/`#chk-hover-names`;
  `dismissLeftPage`; `#search-external`), 6 `controls_excluded`.

## what resisted description
Nothing genuinely amorphous; all of it undocumented or deliberately deferred.
1. No single "read the whole cut" call (above). This is the finding that changes
   the plan.
2. `c2a2Find`'s `ids` reports `SEARCH_CUT` only. `focus:` and isolate call
   `noteCut`, but **AI-picked ids (`applyAIResult`, `:3731`) do not**, so the
   contract is blind to Ask-AI results (inferred from reading; not tested).
3. Edge identity is not addressable (`edge_click` deferred in the manifest).
4. `activeFilters()` and `selectedState()` bodies, and the `view_changed` emitter
   body, were not opened — read only at their call sites.
