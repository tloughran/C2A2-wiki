# Manifest schema acceptance test — §8 of the audit, run

*Written 2026-10-04, same day as `explorer_manifest_audit_2026-10-04.md`, which
is its input. This document does not redo the audit. It tests one falsifiable
claim the audit makes in §8:*

> "Every one of them can be *generated* from this block: `TABS` from `route`,
> `destinations.json` from `identity` + `items`, `descriptions` from `explain`,
> `KNOWLEDGE` from `narration.knowledge_file`, `FIND_TABS` from
> `capability.find_contract`. That is the acceptance test for v2: **no
> hand-maintained page table survives it.**"

*Artefacts: `wiki/voice_guide/manifests.v2.json` (the manifest, all 24 live
surfaces) and `scripts/generate_page_tables.py` (the generator and the differ).
Nothing live was modified: not a page, not a table, not an existing generator.*

---

## 0. Verdict

**PASSES, with eight named schema revisions — and one of the audit's five stated
derivations is false as written.**

Unpacked, because the one-word answer hides the result:

1. **Membership passes outright.** On all six tables, the *set of rows* is
   derivable from one `identity` block per surface, by one rule applied
   uniformly to all 24 pages, with no per-page exception. Four of six match
   row-for-row. The two that do not (`destinations` short by one, `KNOWLEDGE`
   wrong on one value) differ because **the live table is stale or structurally
   incapable**, not because the schema cannot express the row. That is the
   central claim, and it holds.

2. **Field-level reproduction needs eight revisions**, listed in §2. Six are
   small and uncontroversial. One (**R7**, `family` must be a list) contradicts
   §5's own text. One (**R5/R6**, counted as two) means §8's claim that
   `FIND_TABS` derives from `capability.find_contract` **is false**:
   `find_contract` is declared *observed*, and `FIND_TABS` encodes a test
   *expectation* plus a probe needle. Nothing in §8 can hold either.

3. **"No hand-maintained page table survives it" is the wrong frame, in the
   audit's favour.** Two of the six are not hand-maintained at all —
   `destinations.json` is written whole by `build_destinations.py`, and
   `descriptions[].body` is rewritten by `derive_tab_help.py`. Both have drifted
   anyway: `destinations.json` was last written **2026-07-23** and is missing the
   `rc_sandbox` tab entirely, and the `derive_tab_help` gate is **silently blind
   to one tab** (§3.3). A derived table with no gate drifts exactly like a hand
   one. The consolidation argument is stronger than the audit stated it, not
   weaker.

4. **The test found three live defects the audit did not name.** §4. One of them
   — the `KNOWLEDGE` basename collision — is a structural impossibility, not a
   typo.

### The number that should temper all of this

337 of 1,494 leaf values in the filled manifest are the literal string
`"unknown"` — **23%**, concentrated on exactly the surfaces the audit triaged
rather than manifested (`review_log` 36%, `level2_signal_stream` 36%,
`inter_tradition_study` 33%). The manifest can carry **identity** for 24
surfaces today. It cannot yet carry **capability** or **cut** for more than about
nine. §6 says what that does to the five-layer plan.

---

## 1. The six diffs

Run `python3 scripts/generate_page_tables.py --diff`. Full output in Appendix A.
Derivation rules: `--list-rules`.

| table | rows gen / live | membership | fields | classification |
|---|:--:|:--:|:--:|---|
| `TABS` | 14 / 14 | **exact**, in order | `words` differs on 6 | live table **incomplete** |
| `manifests.json.tabs` | 9 / 9 | **exact** (2 keys renamed) | `aka` differs on 6 | live table **wrong** (keys + compensating aliases) |
| `descriptions` | 14 / 14 | **exact** | titles exact; 3 bodies not derivable | 1 **stale**, 1 **work item**, 1 **new defect** |
| `KNOWLEDGE` | 16 / 16 | **exact** | 1 value differs | live table **structurally wrong** |
| `destinations.json.tabs` | 14 / 13 | 1 missing | 4 labels, 6 `aka` | live table **stale** + **wrong** |
| `FIND_TABS` | 8 / 8 | **exact** | needles + expectations exact | **schema insufficient** (R5, R6) |

Row order differs on `descriptions`, `KNOWLEDGE` and `FIND_TABS`. That is
cosmetic in all three — `descriptions` and `KNOWLEDGE` are looked up by key, and
`FIND_TABS` order only sets test sequence. `TABS` order *does* matter (it is the
voice `switch_tab` enum order and `build_destinations.py` preserves it), and it
matches exactly.

### 1.1 `TABS` — the only difference is aliases, and generated ⊃ live

`key`, `kind`, `id` and `src` reproduce exactly for all 14 rows. `words` differs
on six rows, and in **every** case the generated set is a strict superset:

```
sociogram        gen: sociogram, knowledge graph, wiki graph, graph, map, wiki_narration
                live: sociogram, knowledge graph, wiki graph
agent_map        gen: agent map, agents, agent activity, the agents, agents_tab
                live: agent map, agents
```

`identity.aka` in the manifest is the **union** of each page's `TABS.words` and
its `manifests.json` `aka`. Those two live lists are both "what a user might call
this page", they have no derivation rule between them, and neither is a superset
of the other. **Classification: the live table is incomplete.** `TABS.words`
reaches the voice guide only through `build_destinations.py` →
`destinations.json.aka` → the shell's resolver, so each alias missing from
`TABS.words` is a phrase the guide cannot hear today even though the manifest
already knows it. No schema revision needed; this is drift, and it is the
cheapest win in the whole exercise.

### 1.2 `manifests.json.tabs` — the mixed namespace, measured

Count matches (9). Two of nine keys are **filenames, not page keys**:

```
only in GENERATED: narrative_connectome, agent_map
only in LIVE:      prs_3d,               agents_tab
```

That is audit finding 2 reproduced mechanically rather than by inspection.

The `aka` differences are more interesting. Six rows differ, and the live lists
contain entries that are **not spoken aliases at all** — `wiki_narration`,
`metabolism_view`, `prs_3d`, `agents_tab`, `summa_explorer`, `start_here`,
`what_is_c2a2`, `what_is_saying`, `community_explorer`. Nobody says
"metabolism_view" out loud. They are there because the manifest resolver matches
`aka` against the active frame's **filename** when the key lookup misses
(`explorer.html:3222-3227`, whose own comment documents the bug it once caused:
"`aka[i] === key` compared an entry's alias to its own key, so … matched every
tab"). **Classification: the live table is wrong — those nine entries are
workarounds for the un-unified key namespace.** Under v2 `route.data_src` carries
the filename as data, the resolver matches on it, and all nine become dead
weight. One revision is needed, and only for the migration: **R2**
`identity.v1_key`, so the old table can be regenerated during the cut-over.

### 1.3 `descriptions` — titles pass, three bodies do not

Membership is exact, 14 of 14, **including** the two rows that are defects:
`community/index.html` (whose entry `showHelp` can never reach) and
`__section:education` (which is not a page). The schema reproduces the defects
faithfully, which is the right behaviour for a test.

**Titles match on all 13 page rows.** That needed one revision — **R4**
`explain.title`, because three help titles are deliberately not the tab label
("Narrative (PRS) Connectome" vs "Narrative Connectome", "Agent Metabolism" vs
"Metabolism", "Community Explorer (Cards)"). Whether those three are deliberate
or drift cannot be settled by more reading; it is a decision. **R4 is named as a
revision rather than resolved**, and it lets the divergence be deliberate and
visible instead of accidental and invisible.

Bodies are derived the way `derive_tab_help.py` already derives them — the
`## Purpose` section of the page's knowledge file, collapsed. Three of 13 do not
reproduce. Each is a different kind of problem, and §3 takes them one at a time.
`__section:education`'s body does not reproduce either, for a fourth reason:
there is no knowledge file for a *chapter*, so §8 has nowhere to put it
(**R3**).

### 1.4 `KNOWLEDGE` — a key namespace that cannot work

Membership is exact (16/16) under a rule read off the consumer, not chosen to
flatter the diff: the shell looks up **the active frame's basename**, so every
page that can *be* the active frame must have a row — always for tabs and
chapters, `null` when no knowledge file exists; other route kinds only when a
file exists. The same rule predicts `rc_sandbox_notebook.html`'s literal `null`
*and* `community/index.html`'s presence, and omits `whos_who` /
`summa_commentary` / `review_log`, matching the live table on all five.

One value differs, and it is not drift:

```
index.html:  generated 'community_cards.default'   live 'ai_heartbeat.default'
KEY COLLISION: index.html: 'community_cards.default' (community_cards)
               collides with the existing 'ai_heartbeat.default'
```

`wiki/community/index.html` and `wiki/heartbeat/index.html` have the same
basename. **The `KNOWLEDGE` key space is not injective over the 24 surfaces**, so
one of the two surfaces can never have a knowledge file, whatever anyone writes.
`community_cards.default.md` exists, is 100% written, and is unreachable.
**Classification: the live table is structurally wrong.** The schema is fine —
`identity.path` is injective by construction — but the *table* must change key
space, and no amount of care in maintaining it by hand would have helped. This is
the single strongest piece of evidence the test produced.

### 1.5 `destinations.json.tabs` — not hand-maintained, and stale anyway

```
rows only in GENERATED (1): ['rc_sandbox']
rc_document_explorer.label: generated 'RC Document Explorer'  live 'Rc Document Explorer'
trv_commentary.label:       generated 'TRV Commentary'        live 'Trv Commentary'
ai_heartbeat.label:         generated 'AI Heartbeat'          live 'Ai Heartbeat'
start_here.label:           generated 'Start here'            live 'Start Here'
```

Two separate findings.

**The missing row is pure staleness.** `destinations.json` carries
`authored_by: build_destinations.py`, `authored_at: 2026-07-23T17:20:32` and
`counts.tabs: 13`. `build_destinations.py` parses `var TABS` from
`explorer.html`, so re-running it today would emit 14. `rc_sandbox` was added to
`TABS` after July 23 and nothing re-ran the generator. The voice guide's
`find_destination` therefore cannot navigate to RC Sandbox by name — a live
capability hole caused by a generator with no gate. **This corrects the audit:
`destinations.json` is not a hand-maintained table. It is worse — a derived table
nobody re-derives.**

**The four labels are wrong because of how they are computed.**
`build_destinations.py` does `label = aka[0].title()`, i.e. it title-cases the
first *spoken alias*. Title-casing an alias is not a label: it produces "Rc",
"Trv", "Ai". The generated column uses `identity.title`, the string actually
printed in the UI, and gets all four right. **Classification: live table wrong.**
Schema sufficient — this is a fix the consolidation delivers for free.

### 1.6 `FIND_TABS` — exact match, and the weakest result in the test

All 8 rows, all 8 needles, all 8 expectations reproduce exactly. **This proves
much less than it looks like.**

§8 says `FIND_TABS` derives from `capability.find_contract`. It does not, and
cannot. §8 defines `capability` as **observed** ("`capability` is observed,
`caps` is declared") — and the whole point of `FIND_TABS` is that 7 of its 8 rows
are *red on purpose*: it records which surfaces the contract is **expected** on,
and the project's own commit message calls that red "the only honest instrument
in the project for this layer". A table of expectations cannot come from a field
of observations. It also carries a per-surface **probe needle** ("levin",
"civic", "newton") which is a test fixture and has no home in §8 at all.

Generating it required two new fields, **R5** `capability.find_expected` and
**R6** `capability.find_probe` — and **their values exist nowhere in the project
except `FIND_TABS` itself**, so I read them off it. The diff therefore tests
*expressiveness* only: it shows the revised schema **can** hold this table. It is
**not** independent evidence that the information was already recorded elsewhere,
and it must not be counted as one of the five-sixths that passed. Stated plainly
so that nobody later reads a clean row as a clean result.

---

## 2. Schema revisions the test forced

Each is required to reproduce a live table, and each is named rather than
smuggled into the generator as a special case.

| id | revision | forced by | severity |
|---|---|---|---|
| **R1** | `identity.route.row` — `"row2"` / `"row2-edu"` / `null` | `TABS.kind` distinguishes `tools` from `edu`, which is a tab-row assignment. §8's `route` has `kind` and `selector` but nothing for the row. Derivable from the selector by string-matching; declared instead. | trivial |
| **R2** | `identity.v1_key` | Regenerating `manifests.json`'s current keys during migration (`agents_tab`, `prs_3d`). Delete after cut-over. | trivial, temporary |
| **R3** | a top-level `sections` block with its own `explain` | `descriptions` has a `__section:education` row that is a *chapter*, not a page, and no page can own it. §8 has no non-page scope. | small |
| **R4** | `explain.title`, distinct from `identity.title` | Three help titles are deliberately not the tab label. One `identity.title` cannot emit both. | small |
| **R5** | `capability.find_expected` | `FIND_TABS` records expectation; `find_contract` is observation. §8's stated derivation is false without this. | **significant** |
| **R6** | `capability.find_probe` | `FIND_TABS` carries a per-surface search needle. No home in §8. | small, but see §1.6 |
| **R7** | `identity.family` must be a **list** | §5 itself puts `agent_map` in F2 *and* F5, `whos_who` in F4 *and* F5, `trv_commentary` in F1 *and* F3. A single-valued discriminator cannot hold them, and §5's "required blocks per family" rule becomes ambiguous for exactly those three. | **significant** |
| **R8** | `narration.site_intro_file` | `00_project.md` sits in `knowledge/` but is the *site* introduction, read by `window.C2A2Intro` and absent from `KNOWLEDGE`. Filed as the shell's `knowledge_file` it produces a phantom 17th row — the mistake any glob over `knowledge/*.md` would make. | trivial |

**R7 is the one that costs design time.** It is not a field addition; it says the
§5 taxonomy is not a partition. Three of 24 surfaces are two families at once,
and they are the three the audit already flagged as awkward. Either `family` is a
list and "required blocks" becomes a union over the list, or the three surfaces
get split into sub-surfaces with their own entries — which is a bigger change
than it sounds, because splitting `agent_map` means the shell's one tab button
points at two manifest entries.

---

## 3. The three undrivable `descriptions` bodies, separately

### 3.1 `rc_sandbox_notebook.html` — the live table is the only copy

No knowledge file exists (`narration.knowledge_file: null`,
`needs_writing: true`; `KNOWLEDGE` records the same thing as a literal `null`).
So the ~180-word help body in `explorer.html` is the **only** prose describing
this surface anywhere in the project. **Not a schema gap, and not stale — a work
item**, and the one place where the live table is genuinely load-bearing. The
consolidation must not delete it before `rc_sandbox.default.md` is written.

### 3.2 `commentary_explorer.html` — stale, and the project already knows

Live body carries 235 characters of text beyond the knowledge file's `Purpose`
("Annotation covers every page from pp. 5-240, all ten chapters, with 3,400
marks…"). `python3 scripts/derive_tab_help.py --check` independently reports
this same tab and only this tab as out of sync. **Classification: live table
stale.** Independent confirmation from a tool nobody wrote for this test is the
best evidence in the document.

### 3.3 `rc_document_explorer.html` — a new defect, invisible to the gate

Generated body is empty. The cause is one character:
`voice_guide/knowledge/rc_document_explorer.default.md` writes its purpose
heading as **`# Purpose`** (H1), where every other knowledge file writes
`## Purpose`. `derive_tab_help.py` matches `##\s+Purpose`, finds nothing,
and — by its own documented "partial rollout is safe" behaviour — **silently
leaves the tab untouched**. So:

- the help body for this tab is hand-maintained without anyone intending it,
- `derive_tab_help.py --check` reports it as in sync, because it is excluded, and
- the janitor's `voice_knowledge_help_drift` check cannot see it either.

**A one-character typo in a markdown heading removed a tab from the drift gate,
and the gate reports success.** The generator here was deliberately kept at exact
parity with `derive_tab_help.py` (same regex) rather than loosened to
`#{1,2}\s+Purpose`, because loosening it would have hidden the finding behind a
clean diff. The fix is in the knowledge file, not in either script. Worth noting
because this is the same shape as every failure
`check_scheduler_health.py`'s docstring was written about: a check that reports
nothing and is believed.

---

## 4. Live defects this test found that the audit did not name

1. **`KNOWLEDGE` basename collision** (§1.4) — `community/index.html` vs
   `heartbeat/index.html`. Structural; `community_cards.default.md` is dead on
   arrival. Combined with the audit's own finding that this surface's
   `descriptions` entry is unreachable, Community Cards now has **two**
   independent dead pointers — on the one surface that holds the project's only
   working export.
2. **`destinations.json` is 73 days stale and missing a tab** (§1.5). The voice
   guide cannot navigate to RC Sandbox by name.
3. **`derive_tab_help.py`'s gate is blind to `rc_document_explorer`** (§3.3).
4. *(minor, read not inferred)* **`whos_who.html` is reached by a bare `href`**
   from `start_here.html:166`, with no `data-target` — so it navigates the
   iframe without telling the shell, which never re-lights the chapter or hides
   the tab rows. This is the exact defect the `saying` door shipped with and had
   fixed, as `explorer.html`'s own door-handler comment records. The audit lists
   `whos_who` as a door but does not state the mechanism.

---

## 5. Where I inferred rather than read

Marked here because the manifest's `_unknown` convention only covers values I
left out, not values I reasoned to.

- **Agent Map's data source** — `wiki/agents/openstory/agent_telemetry.json` is
  inferred from the audit's "hybrid (hand shell + injected `TELEMETRY` block)"
  plus the file's existence. Not traced through the injector.
- **IT Readout = the 18-step animation, IT Matrix = the 40-step matrix** —
  inferred from §3.1's list of "three unrelated instruments" in order. Not read
  from the pages.
- **`sociogram_curriculum`'s fragment** — recorded as `#agents`, the same as the
  Agent Map preset, because the audit gives the two loads and their weights but
  not distinct fragments. Flagged in the manifest.
- **Family assignments for `review_log`, `intertradition_readout` and
  `intertradition_matrix`** — left `"unknown"`. §5's five families do not
  classify them and I did not open the pages to decide.
- **`explain.title` for every row** — read from the live `descriptions` map,
  which is circular for that one diff in the same way R5/R6 are circular for
  `FIND_TABS`, though far less consequentially: the titles are visible UI strings
  with no other possible source.

---

## 6. What this says about the five-layer plan

The useful result is not the verdict. It is the asymmetry the test exposed.

**The `identity` half of the plan is proved and cheap.** §8's order-of-work step
1 — "unify the key namespace and generate the five derived tables" — survives the
test intact. Membership for all six tables is derivable today, from material the
audit had already gathered, with no per-page exceptions and only trivial
revisions (R1–R4, R8). It pays off immediately and independently: it fixes four
wrong labels, one missing navigation target, one unreachable knowledge file and
one unreachable help entry, and it does so whether or not a single one of the
five layers is ever built. That was §8's own argument for step 1 and the test
supports it.

**The `capability` half is not proved, and the plan treats the two as one task.**
Step 2 says "Fill `identity` + `purpose` + `capability` for all 24 surfaces. Most
of it is in `manifest_audit/` already." The first two, yes. The third, no — and
`FIND_TABS` is the proof, because it is the *only* layer-bearing table among the
six and it turned out to encode **test intent, not page identity**. Its eight
rows are a statement about what the project has decided to build next. That is
not an observation of a page and it cannot be derived from one. Generating it
needed two invented fields whose values existed nowhere but in the test file.

Generalised: a manifest can hold what a surface **is**. It can hold what a
surface **currently does**, if a sweep observes it. It cannot hold what a surface
**ought to do** without becoming a plan document, and the moment it does, the
coverage gate that makes `manifests.json` trustworthy stops being able to tell a
missing implementation from an unfilled field. Keeping `caps` (declared) and
`capability` (observed) separate — which §8 already insists on, rightly — is not
enough: **a third thing, intent, has to live somewhere too**, and `FIND_TABS`
shows it is already being recorded, in a test, by hand, for eight surfaces.

Three concrete consequences for the plan:

1. **Split step 2.** `identity` + `purpose` is a day's transcription from
   `manifest_audit/` and should be done now. `capability` should be **emitted by
   the runtime sweep**, never hand-filled, or the gate loses its meaning. Intent
   (`find_expected` and its siblings for the other four layers) belongs with the
   tests that assert it, not in the manifest — and if it does go in the manifest,
   it needs a block of its own, visibly not `capability`.
2. **Settle R7 before writing per-family profiles.** §5's "one schema, five
   profiles" assumes the families partition the surfaces. They do not, for three
   of 24. Writing required-block rules per family before deciding whether
   `family` is a list or `agent_map` splits in two will produce exactly the kind
   of contradiction the single manifest exists to prevent.
3. **Do not read 23% `"unknown"` as 77% done.** The unknowns are not spread
   evenly — they cluster on the four surfaces the audit triaged
   (`review_log` 36%, `level2_signal_stream` 36%, `inter_tradition_study` 33%,
   `intertradition_readout` 33%) and on `cut`, which is the block every one of
   the five layers actually consumes. Nine surfaces have a real `cut` (the nine
   with v1 entries). Fifteen do not. Any layer that claims 24 consumers is
   claiming fifteen it cannot describe.

Nothing here argues against the plan. It argues that step 1 is better supported
than the audit claimed, step 2 is two tasks wearing one name, and the fifth
layer's only existing instrument is a test, not a manifest.

---

## Appendix A — full diff output

Reproduce with `python3 scripts/generate_page_tables.py --diff` (exit code 1).

```
TABS           generated 14 rows, live 14 rows  -- 6 difference group(s)
  community_explorer.words: generated='community explorer, communities graph, communities, community'  live='community explorer, communities graph'
  sociogram.words: generated='sociogram, knowledge graph, wiki graph, graph, map, wiki_narration'  live='sociogram, knowledge graph, wiki graph'
  narrative_connectome.words: generated='narrative connectome, prs connectome, 3d, connectome, prs, prs_3d'  live='narrative connectome, prs connectome, 3d'
  agent_map.words: generated='agent map, agents, agent activity, the agents, agents_tab'  live='agent map, agents'
  metabolism.words: generated='metabolism, agent pulse, telemetry, pulse, activity, metabolism_view'  live='metabolism, agent pulse, telemetry'
  curriculum_tools.words: generated='curriculum tools, summa, curriculum dashboard, summa explorer, the summa, summa_explorer'  live='curriculum tools, summa, curriculum dashboard'
manifests      generated 9 rows, live 9 rows  -- 9 difference group(s)
  rows only in GENERATED (2): ['narrative_connectome', 'agent_map']
  rows only in LIVE      (2): ['agents_tab', 'prs_3d']
  start_here.aka: generated=['start here', 'home', 'intro']  live=['start here', 'start_here', 'home', 'intro']
  community_explorer.aka: generated=['community explorer', 'communities graph', 'communities', 'community']  live=['community explorer', 'community_explorer', 'communities', 'community']
  sociogram.aka: generated=['sociogram', 'knowledge graph', 'wiki graph', 'graph', 'map', 'wiki_narration']  live=['sociogram', 'graph', 'map', 'wiki_narration']
  metabolism.aka: generated=['metabolism', 'agent pulse', 'telemetry', 'pulse', 'activity', 'metabolism_view']  live=['metabolism', 'pulse', 'activity', 'metabolism_view']
  curriculum_tools.aka: generated=[... 'curriculum dashboard', 'summa explorer', ...]  live=[... 'summa explorer', ... 'curriculum dashboard', ...]
  what_is_c2a2.aka: generated=[...'the framings']  live=[...'the framings', 'what_is_c2a2']
  what_is_saying.aka: generated=[...'the medium is the message']  live=[...'the medium is the message', 'what_is_saying']
descriptions   generated 14 rows, live 14 rows  -- 2 difference group(s)
  same rows, DIFFERENT ORDER
  body differs on 4 shared rows: ['__section:education', 'rc_document_explorer.html', 'rc_sandbox_notebook.html', 'commentary-explorer/commentary_explorer.html']
KNOWLEDGE      generated 16 rows, live 16 rows  -- 3 difference group(s)
  same rows, DIFFERENT ORDER
  index.html: generated='community_cards.default'  live='ai_heartbeat.default'
  KEY COLLISION under the basename rule: index.html: 'community_cards.default' (from community_cards) collides with the existing 'ai_heartbeat.default'
destinations   generated 14 rows, live 13 rows  -- 11 difference group(s)
  rows only in GENERATED (1): ['rc_sandbox']
  start_here.label: generated='Start here'  live='Start Here'
  rc_document_explorer.label: generated='RC Document Explorer'  live='Rc Document Explorer'
  trv_commentary.label: generated='TRV Commentary'  live='Trv Commentary'
  ai_heartbeat.label: generated='AI Heartbeat'  live='Ai Heartbeat'
  (plus the six `aka` subset differences already shown under TABS)
FIND_TABS      generated 8 rows, live 8 rows  -- 1 difference group(s)
  same rows, DIFFERENT ORDER

6 of 6 tables differ from the generated form.
```

## Appendix B — one correction to the audit, for the record

Audit finding 2 and its table describe all six as "hand-maintained page tables".
Two are not:

- `destinations.json.tabs` is generated whole by `scripts/build_destinations.py`
  from `var TABS`. Its drift is a **stale generator**, not a stale hand.
- `descriptions[].body` is generated by `scripts/derive_tab_help.py` from
  `voice_guide/knowledge/*.md`, under a canonical-source rule already written
  down in `voice_guide_state_bus.md`. Only membership and `title` are hand-held
  there.

This does not weaken finding 2; the counts still disagree and the keys still do
not match. It sharpens it. **Deriving a table is not sufficient — it has to be
derived on a gate.** `destinations.json` has a generator and no gate, and is 73
days stale. `descriptions[].body` has a generator *and* a gate, and the gate is
blind to one tab because of a markdown heading level. The lesson the five-layer
plan should take is not "generate the tables" but "generate them, gate them, and
make the gate fail loudly when its input is malformed rather than skipping the
row".
