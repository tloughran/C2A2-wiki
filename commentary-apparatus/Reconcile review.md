---
title: Reconcile Review — Summa Commentary Apparatus (foundation §7 step 3)
updated: 2026-07-17
status: DERIVED from reconciliation.json + works_cited_staged.json — do not hand-edit; re-run reconcile_reference_master.py
relates_to: "[[Referencing and linking foundation]]", "reconciliation.json", "works_cited_staged.json"
---

# Reconcile Review — human-confirm queue

Step 3 (reconcile) ran non-destructively over the confirmed 46-work bibliography and the 307-day harvest. Nothing in `works_cited.json` or `reference_master.json` was changed. This page is the queue of judgment calls for your confirmation; the machine overlay is `reconciliation.json`; proposed new works are `works_cited_staged.json`.

## At a glance

- **634** body occurrences reconciled — **150** kept as harvested specifics, **484** generic → thinker-canonical default (flagged, never pinned; foundation §4).
- **0** auto-promotions (bounded policy: the only title-candidate present is the denylisted concept-label *active inference*).
- Ids resolved to a wiki node + endnote target: **48** scoped PRS, **10** unscoped PRS, **33** CROSS, **2** FLAG.
- **6** proposed new works (all `verified:false`) — your confirmation gates each.

Every PRS endnote cites **two** things (foundation §4): Loughran's PRS-form re-description (`loughran-2026-prs-synergistic-coil-form`) **+** the underlying thinker work below. CROSS/FLAG ids are internal (foundation §5, stripped at export) and never become a body citation.

## 1. Proposed new works — confirm & set `verified:true` (highest priority)

These underlying works are cited by PRS ids but were not among your confirmed 46. Each is staged `verified:false` in `works_cited_staged.json`. Confirm the detail, flip `verified`, then merge.

| cite_key | work | type | year | note / decision needed |
| --- | --- | --- | --- | --- |
| `friston-2026-active-inference-review` | Karl J. Friston, et al., "Active Inference and the Free Energy Principle: A Review" | article | 2026 | Underlying work for friston PRS-07/08 and the CROSS-006/007 substrate-independence confirmation. Venue/DOI/full author list UNVERIFIED - confirm before print. |
| `levin-2026-ferriss-interview` | Michael Levin, "Michael Levin - interview" — *The Tim Ferriss Show, episode 849* | talk | 2026 | Podcast interview. DECISION: is a podcast episode admissible to the bibliography, or should PRS-07/08 cite a published Levin paper instead (e.g. bioelectric-reprogramming work)? |
| `fredrickson-2025-conducive-conditions-positivity-resonance` | Barbara L. Fredrickson, "Conducive Conditions for Positivity Resonance at Multiple Levels of Analysis" — *UBC Psychology Colloquium* | talk | 2025 | Colloquium talk. Confirm whether a published paper version exists to cite instead. |
| `stump-2025-biblical-narratives-flourishing` | Eleonore Stump, Judith Wolfe, "Biblical Narratives and Human Flourishing: Knowledge Through Narrative" | book | 2025 | Confirm authorship (Stump & Wolfe?), subtitle, and year vs source. |
| `stump-2024-grains-of-wheat` | Eleonore Stump, "Grains of Wheat: Suffering and Biblical Narratives" | book | 2024 | PRS-08 gives '2024/25', PRS-11 gives 2024-10-01 - confirm publication year. |
| `carroll-2026-mindscape-349-harlow` | Daniel Harlow, Sean Carroll (host), "What Quantum Gravity Teaches Us About Quantum Mechanics" — *Mindscape podcast, episode 349* | talk | 2026 | AMBIGUOUS ATTRIBUTION: content is guest Daniel Harlow's, filed under Carroll's program only because it aired on his podcast. Do NOT attribute to Carroll as author. Decide whether it belongs in the bibliography at all. |

## 2. Scoped PRS-id resolutions (48)

### Deterministic (from works_cited source field) — no action  (12)

| PRS id | → underlying work | days | note |
| --- | --- | --- | --- |
| `arkanihamed-PRS-01` | `arkanihamed-1998-hierarchy-problem-new-dimensions` | 2 | deterministic from works_cited source field |
| `fredrickson-PRS-01` | `fredrickson-1998-what-good-positive-emotions` | 4 | deterministic from works_cited source field |
| `fredrickson-PRS-02` | `fredrickson-2013-love-2-0` | 5 | deterministic from works_cited source field |
| `friston-PRS-02` | `friston-2010-free-energy-principle` | 5 | deterministic from works_cited source field |
| `hawkins-PRS-01` | `hawkins-2004-on-intelligence` | 5 | deterministic from works_cited source field |
| `hawkins-PRS-02` | `hawkins-2021-thousand-brains` | 11 | deterministic from works_cited source field |
| `hoffman-PRS-02` | `hoffman-2019-case-against-reality` | 5 | deterministic from works_cited source field |
| `kastrup-PRS-01` | `kastrup-2014-why-materialism-is-baloney` | 22 | deterministic from works_cited source field |
| `kastrup-PRS-02` | `kastrup-2019-idea-of-the-world` | 22 | deterministic from works_cited source field |
| `levin-PRS-03` | `levin-2022-cognitive-light-cones` | 15 | deterministic from works_cited source field |
| `mcgilchrist-PRS-01` | `mcgilchrist-2009-master-and-his-emissary` | 1 | deterministic from works_cited source field |
| `wolfram-PRS-01` | `wolfram-2002-new-kind-of-science` | 3 | deterministic from works_cited source field |

### Maps to an already-seeded non-canonical work — **confirm**  (2)

| PRS id | → underlying work | days | note |
| --- | --- | --- | --- |
| `hoffman-PRS-07` | `hoffman-2026-multiscale-logic-collective-intelligence` | 1 | Thoughtforms Life talk = the seeded 2026 multiscale-logic entry; confirm talk-vs-article container |
| `wolfram-PRS-06` | `wolfram-2026-metaphysics-and-the-ruliad` | 18 | = the seeded 2026 Ruliad metaphysics entry |

### → a proposed NEW staged work (see §1) — **confirm**  (9)

| PRS id | → underlying work | days | note |
| --- | --- | --- | --- |
| `carroll-PRS-07` | `carroll-2026-mindscape-349-harlow` | 4 | Mindscape #349 GUEST (Harlow) - attribution decision needed |
| `fredrickson-PRS-08` | `fredrickson-2025-conducive-conditions-positivity-resonance` | 1 | UBC colloquium talk |
| `friston-PRS-07` | `friston-2026-active-inference-review` | 10 | 2026 review paper (also confirms CROSS-006/007) |
| `friston-PRS-08` | `friston-2026-active-inference-review` | 19 | same 2026 review, Section 4.1 |
| `levin-PRS-07` | `levin-2026-ferriss-interview` | 3 | Tim Ferriss Show #849 |
| `levin-PRS-08` | `levin-2026-ferriss-interview` | 8 | Tim Ferriss Show #849 |
| `stump-PRS-07` | `stump-2025-biblical-narratives-flourishing` | 1 | Stump & Wolfe, Routledge |
| `stump-PRS-08` | `stump-2024-grains-of-wheat` | 1 | Grains of Wheat, OUP |
| `stump-PRS-11` | `stump-2024-grains-of-wheat` | 16 | Grains of Wheat, OUP |

### RC-Tome re-description → thinker canonical work — **confirm**  (25)

| PRS id | → underlying work | days | note |
| --- | --- | --- | --- |
| `carroll-PRS-01` | `carroll-2016-big-picture` | 4 | RC-Tome re-description; ontological-closure/emergence -> Big Picture |
| `carroll-PRS-04` | `carroll-2016-big-picture` | 6 | RC-Tome; agency-without-dualism -> Big Picture |
| `carroll-PRS-05` | `carroll-2016-big-picture` | 1 | RC-Tome; science-religion dialogue -> Big Picture |
| `fredrickson-PRS-04` | `fredrickson-2013-love-2-0` | 1 | RC-Tome; relational coherence -> Love 2.0 |
| `fredrickson-PRS-06` | `fredrickson-2013-love-2-0` | 5 | RC-Tome; democratizing participation -> Love 2.0 |
| `friston-PRS-01` | `friston-2010-free-energy-principle` | 3 | RC-Tome; biological agency without vitalism -> FEP |
| `friston-PRS-04` | `friston-2010-free-energy-principle` | 24 | RC-Tome; organism as active modeler -> FEP |
| `friston-PRS-05` | `friston-2010-free-energy-principle` | 3 | RC-Tome; distributed cognition across scales -> FEP |
| `friston-PRS-06` | `friston-2010-free-energy-principle` | 2 | RC-Tome; multi-agent coherence -> FEP |
| `hawkins-PRS-03` | `hawkins-2021-thousand-brains` | 1 | RC-Tome; knowledge-preserving AGI -> Thousand Brains |
| `hawkins-PRS-04` | `hawkins-2021-thousand-brains` | 2 | RC-Tome; reference frames -> Thousand Brains |
| `hoffman-PRS-01` | `hoffman-2019-case-against-reality` | 9 | RC-Tome; hard-problem transformation -> Case Against Reality |
| `hoffman-PRS-03` | `hoffman-2019-case-against-reality` | 18 | RC-Tome; perception fitness-tracking -> Case Against Reality |
| `hoffman-PRS-04` | `hoffman-2019-case-against-reality` | 3 | RC-Tome; observer-dependent spacetime -> Case Against Reality |
| `kastrup-PRS-04` | `kastrup-2019-idea-of-the-world` | 3 | RC-Tome; philosophy<->mathematics bridge -> Idea of the World |
| `levin-PRS-01` | `levin-2022-cognitive-light-cones` | 14 | RC-Tome; morphogenetic control -> Cognitive Light Cones (consider levin-2018-bioelectric-code) |
| `levin-PRS-04` | `levin-2022-cognitive-light-cones` | 10 | RC-Tome; cognition substrate/xenobots -> Cognitive Light Cones (consider levin-2020-xenobots) |
| `loughran-PRS-08` | `loughran-2026-prs-synergistic-coil-form` | 2 | RC-Tome tradition-crossing inquiry, re-homed from stump PRS-01 per ASSUMPTION-076; consider a distinct 'RC Tome' work |
| `mcgilchrist-PRS-03` | `mcgilchrist-2009-master-and-his-emissary` | 2 | RC-Tome; hemispheric modes -> Master & Emissary |
| `mcgilchrist-PRS-04` | `mcgilchrist-2009-master-and-his-emissary` | 2 | RC-Tome; multi-agent integration -> Master & Emissary |
| `mcgilchrist-PRS-05` | `mcgilchrist-2009-master-and-his-emissary` | 1 | RC-Tome; attention as ontological act -> Master & Emissary (consider 2021 Matter with Things) |
| `stump-PRS-04` | `stump-2010-wandering-in-darkness` | 13 | RC-Tome; final causality & biology -> Wandering (consider stump-2003-aquinas) |
| `stump-PRS-05` | `stump-2010-wandering-in-darkness` | 17 | RC-Tome; suffering & divine permission -> Wandering in Darkness |
| `stump-PRS-06` | `stump-2010-wandering-in-darkness` | 1 | RC-Tome; tradition vitality & MacIntyre -> Wandering (cross to macintyre) |
| `wolfram-PRS-04` | `wolfram-2020-project-fundamental-theory` | 3 | RC-Tome; computational irreducibility & agency -> Fundamental Theory (consider wolfram-2002-nks) |

## 3. Unscoped PRS-ids (10) — provisional, confirm scope

Appear in bodies with no adjacent surname; provisionally the C2A2/RC master framework (→ Loughran PRS-form). Could be a thinker's PRS the harvester failed to scope — confirm per occurrence.

| id | occurrences | provisional target | node |
| --- | --- | --- | --- |
| `PRS-01` | 31 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-02` | 18 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-03` | 23 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-04` | 23 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-05` | 5 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-06` | 11 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-07` | 7 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-08` | 20 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-09` | 2 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |
| `PRS-11` | 6 | `loughran-2026-prs-synergistic-coil-form` | wiki/master/C2A2_prs_triplets.md (or wiki/traditions/loughran/prs_triplets.md) |

## 4. CROSS / FLAG ids — internal bridges (34) — stripped at export

Not citable body works. Listed so the build step maps them to the involved programs' canonical works and so QC can verify none leak into print (foundation §5).

| CROSS id | programs | → canonical works if cited | occ |
| --- | --- | --- | --- |
| `CROSS-001` | Levin Agent, Friston Agent, Hawkins Agent, Kastrup Agent, Hoffman Agent | `levin-2022-cognitive-light-cones`, `friston-2010-free-energy-principle`, `hawkins-2021-thousand-brains`, `kastrup-2019-idea-of-the-world`, `hoffman-2019-case-against-reality` | 23 |
| `CROSS-002` | Wolfram Agent, Arkani-Hamed Agent, Carroll Agent, Hoffman Agent | `wolfram-2020-project-fundamental-theory`, `arkanihamed-2014-amplituhedron`, `carroll-2016-big-picture`, `hoffman-2019-case-against-reality` | 7 |
| `CROSS-003` | McGilchrist Agent, Friston Agent, Hoffman Agent, Fredrickson Agent | `mcgilchrist-2009-master-and-his-emissary`, `friston-2010-free-energy-principle`, `hoffman-2019-case-against-reality`, `fredrickson-2013-love-2-0` | 2 |
| `CROSS-005` | Fredrickson Agent, Stump Agent, Kastrup Agent | `fredrickson-2013-love-2-0`, `stump-2010-wandering-in-darkness`, `kastrup-2019-idea-of-the-world` | 19 |
| `CROSS-006` | Levin Agent, Friston Agent | `levin-2022-cognitive-light-cones`, `friston-2010-free-energy-principle` | 21 |
| `CROSS-007` | Levin Agent, Friston Agent | `levin-2022-cognitive-light-cones`, `friston-2010-free-energy-principle` | 1 |
| `CROSS-008` | Levin Agent, Stump Agent | `levin-2022-cognitive-light-cones`, `stump-2010-wandering-in-darkness` | 7 |
| `CROSS-009` | Friston Agent, McGilchrist Agent | `friston-2010-free-energy-principle`, `mcgilchrist-2009-master-and-his-emissary` | 1 |
| `CROSS-010` | Friston Agent, Fredrickson Agent | `friston-2010-free-energy-principle`, `fredrickson-2013-love-2-0` | 4 |
| `CROSS-011` | Friston Agent, Hawkins Agent | `friston-2010-free-energy-principle`, `hawkins-2021-thousand-brains` | 5 |
| `CROSS-013` | Hoffman Agent, McGilchrist Agent | `hoffman-2019-case-against-reality`, `mcgilchrist-2009-master-and-his-emissary` | 5 |
| `CROSS-014` | Hoffman Agent, Kastrup Agent | `hoffman-2019-case-against-reality`, `kastrup-2019-idea-of-the-world` | 10 |
| `CROSS-016` | Carroll Agent, Wolfram Agent | `carroll-2016-big-picture`, `wolfram-2020-project-fundamental-theory` | 2 |
| `CROSS-018` | Fredrickson Agent, Stump Agent | `fredrickson-2013-love-2-0`, `stump-2010-wandering-in-darkness` | 6 |
| `CROSS-019` | Stump Agent, Levin Agent | `stump-2010-wandering-in-darkness`, `levin-2022-cognitive-light-cones` | 1 |
| `CROSS-020` | McGilchrist Agent, Stump Agent | `mcgilchrist-2009-master-and-his-emissary`, `stump-2010-wandering-in-darkness` | 1 |
| `CROSS-021` | Wolfram Agent, Hoffman Agent | `wolfram-2020-project-fundamental-theory`, `hoffman-2019-case-against-reality` | 2 |
| `CROSS-022` | Kastrup Agent, Stump Agent | `kastrup-2019-idea-of-the-world`, `stump-2010-wandering-in-darkness` | 2 |
| `CROSS-024` | Wolfram Agent, Arkani-Hamed Agent | `wolfram-2020-project-fundamental-theory`, `arkanihamed-2014-amplituhedron` | 5 |
| `CROSS-025` | Friston Agent, Levin Agent | `friston-2010-free-energy-principle`, `levin-2022-cognitive-light-cones` | 1 |
| `CROSS-027` | Kastrup Agent, Friston Agent | `kastrup-2019-idea-of-the-world`, `friston-2010-free-energy-principle` | 7 |
| `CROSS-028` | Levin Agent, Kastrup Agent | `levin-2022-cognitive-light-cones`, `kastrup-2019-idea-of-the-world` | 1 |
| `CROSS-029` | McGilchrist Agent, Levin Agent | `mcgilchrist-2009-master-and-his-emissary`, `levin-2022-cognitive-light-cones` | 2 |
| `CROSS-032` | Hoffman Agent, Friston Agent | `hoffman-2019-case-against-reality`, `friston-2010-free-energy-principle` | 2 |
| `CROSS-037` | Friston Agent, Levin Agent, Kastrup Agent | `friston-2010-free-energy-principle`, `levin-2022-cognitive-light-cones`, `kastrup-2019-idea-of-the-world` | 1 |
| `CROSS-038` | Hoffman Agent, Kastrup Agent | `hoffman-2019-case-against-reality`, `kastrup-2019-idea-of-the-world` | 1 |
| `CROSS-039` | Friston Agent, Hoffman Agent | `friston-2010-free-energy-principle`, `hoffman-2019-case-against-reality` | 1 |
| `CROSS-040` | Friston Agent, Hawkins Agent | `friston-2010-free-energy-principle`, `hawkins-2021-thousand-brains` | 2 |
| `CROSS-041` | McGilchrist Agent, Fredrickson Agent | `mcgilchrist-2009-master-and-his-emissary`, `fredrickson-2013-love-2-0` | 1 |
| `CROSS-049` | Wolfram Agent, Friston Agent | `wolfram-2020-project-fundamental-theory`, `friston-2010-free-energy-principle` | 1 |
| `CROSS-050` | Carroll Agent, Levin Agent, Friston Agent, Kastrup Agent | `carroll-2016-big-picture`, `levin-2022-cognitive-light-cones`, `friston-2010-free-energy-principle`, `kastrup-2019-idea-of-the-world` | 1 |
| `CROSS-051` | Stump Agent, Fredrickson Agent | `stump-2010-wandering-in-darkness`, `fredrickson-2013-love-2-0` | 4 |
| `CROSS-053` | Stump Agent, MacIntyre Agent, C2A2 (meta) | `stump-2010-wandering-in-darkness`, `macintyre-1981-after-virtue` | 1 |

- `FLAG-003` (7 occ) — Paradigm-shift flag (internal, stripped at export). NOTE: current paradigm_flags.md lists only FLAG-001/002; this id's definition was not found in the staged file - verify its home (wiki/flags/).
- `FLAG-005` (3 occ) — Paradigm-shift flag (internal, stripped at export). NOTE: current paradigm_flags.md lists only FLAG-001/002; this id's definition was not found in the staged file - verify its home (wiki/flags/).

## 5. Generic→specific promotion candidates (bounded)

No occurrence was auto-promoted. The only title-candidate in the harvest is the denylisted concept-label *active inference* (→ `friston-2017-active-inference-process-theory`). These Friston days matched it; confirm which genuinely cite the 2017 process-theory paper versus staying generic → FEP:

- **friston**, 44 days: d4, d7, d8, d9, d10, d11, d12, d13, d18, d19, d20, d22, d23, d24, d27, d30, d31, d32, d33, d34, d37, d40, d41, d42, d43, d44, d45, d48, d49, d50, d51, d52, d53, d54, d55, d81, d82, d83, d84, d85, d86, d88, d89, d90

## 6. Generic surname-only mentions → canonical default (flagged, foundation §4)

Kept resolved to each thinker's canonical work, flagged for confirmation — never silently pinned. Per-thinker counts (specific kept / generic-default flagged):

| thinker | canonical | specific kept | generic→canonical (flagged) |
| --- | --- | --- | --- |
| aquinas | `aquinas-summa-theologiae` | 0 | 65 |
| friston | `friston-2010-free-energy-principle` | 2 | 59 |
| kastrup | `kastrup-2019-idea-of-the-world` | 4 | 53 |
| levin | `levin-2022-cognitive-light-cones` | 0 | 50 |
| hoffman | `hoffman-2019-case-against-reality` | 3 | 46 |
| stump | `stump-2010-wandering-in-darkness` | 19 | 35 |
| fredrickson | `fredrickson-2013-love-2-0` | 0 | 31 |
| mcgilchrist | `mcgilchrist-2009-master-and-his-emissary` | 7 | 29 |
| wolfram | `wolfram-2020-project-fundamental-theory` | 6 | 29 |
| hawkins | `hawkins-2021-thousand-brains` | 5 | 23 |
| wright | `wright-1992-new-testament-people-of-god` | 42 | 23 |
| carroll | `carroll-2016-big-picture` | 3 | 17 |
| arkanihamed | `arkanihamed-2014-amplituhedron` | 2 | 11 |
| rohr | `rohr-2019-universal-christ` | 57 | 4 |
| loughran | `loughran-2026-prs-synergistic-coil-form` | 0 | 3 |
| macintyre | `macintyre-1981-after-virtue` | 0 | 3 |
| kuhn | `kuhn-1962-structure-scientific-revolutions` | 0 | 3 |

---
*Self-check: PASS — 634 occurrences accounted for; 93 distinct ids resolved to a node.*