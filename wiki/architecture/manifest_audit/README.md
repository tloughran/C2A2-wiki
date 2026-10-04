# Per-surface manifest entries — first pass, 2026-10-04

Companion to `../explorer_manifest_audit_2026-10-04.md`. One file per live
surface (or per group, where the surfaces are small and alike). Each entry
attempts the ten fields asked for in the audit brief:

identity · purpose · data sources · entities and fields · **cut** ·
change signal · export shape · narration · current capability ·
what resisted description

Conventions used throughout:

- Line citations are `file:line` against the state of the repo on 2026-10-04.
  Generated pages are cited against their **generator**, not the built output,
  except where only the output could answer the question.
- `(inferred)` marks a claim reasoned to rather than read.
- "the contract" = `window.c2a2Find` / `c2a2Clear` / `c2a2ReadCut`, the trio the
  shell's `tabFindApi` looks for (`explorer.html:3496`).
- "the manifest" = the existing `wiki/voice_guide/manifests.json` (v1, 9 entries).
- `family` is the §5 discriminator: graph · chart · reader · prose · table.

| file | surface | family |
|---|---|---|
| `01_sociogram.md` | Sociogram | graph |
| `02_narrative_connectome.md` | Narrative Connectome | graph |
| `03_agent_map.md` | Agent Map | chart + table |
| `04_metabolism.md` | Metabolism | chart |
| `05_curriculum_tools.md` | Curriculum Tools | reader |
| `06_inter_tradition_study.md` | Inter-Tradition Study | reader |
| `07_rc_document_explorer.md` | RC Document Explorer | reader |
| `08_rc_sandbox.md` | RC Sandbox | reader |
| `09_physics_explorer.md` | Physics Explorer | reader |
| `10_trv_commentary.md` | TRV Commentary | graph + reader |
| `11_ai_heartbeat.md` | AI Heartbeat | table |
| `12_community_explorer.md` | Community Explorer (graph + Cards) | graph + table |
| `13_community_interactions.md` | Community Interactions | prose |
| `14_prose_and_doors.md` | Start here, What's it doing?, What's it saying?, Who's Who, Summa Commentary, Review Log | prose / reader |
| `21_nested_subsurfaces.md` | Level-2 Signal Stream, IT Readout, IT Matrix, Community Cards, Sociogram presets | mixed |
| `22_shell.md` | `explorer.html` | — |
| `23_non_surfaces.md` | build inputs, orphans, stale, dead | — |
