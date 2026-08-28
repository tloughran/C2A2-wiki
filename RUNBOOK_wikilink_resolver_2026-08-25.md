# RUNBOOK — wikilink resolver + what came out of the lift-z resume

**Session:** 2026-08-24 evening → 08-25 (Cowork, cloud)
**State:** code written, tested, measured. **Nothing committed. Nothing regenerated.**
**Branch:** `claude/wikilink-resolver-fix` — worktree `.claude/worktrees/wikilink-resolver/`, off `main` @ `7fe274c`

---

## 1. Run this first

```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
less handoffs/wikilink-resolver.diff
```

```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/.claude/worktrees/wikilink-resolver/wiki/c2a2-wiki-narration/scripts"
python3 test_wikilink_resolver.py
```

Expect **33 assertions, all ok**. Then commit two files only:

```
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/.claude/worktrees/wikilink-resolver"
git add wiki/c2a2-wiki-narration/scripts/extract_vault_data.py
git add wiki/c2a2-wiki-narration/scripts/test_wikilink_resolver.py
git commit -m "Fix wikilink resolver: path-qualified, thinker-name, and ambiguous-stem handling"
```

**Do not regen blind.** This is a pipeline change — PRS 3D, review log, metabolism and the
commentary apparatus all consume these edges. **Diff the consumer outputs, not just the
Sociogram.**

---

## 2. What the fix is

The shipped resolver keyed on bare filename **stem, first-wins**, looked up against the raw
inner text of the link. It silently dropped **41% of every wikilink in the vault** — 317 of
776 pairs:

| failure | dropped |
|---|---|
| path-qualified — `[[traditions/friston/wiki\|Friston]]` matched no stem | 96 |
| surname — `[[Kastrup]]`, `[[Friston]]`; `THINKER_PATHS` had the mapping, only the *mention* path used it | 127 occurrences |
| stem collisions — `wiki` and `prs_triplets` collide **15 ways each** | 14 ambiguous |

New order: exact relpath → relpath+`.md` → thinker name → **unique** stem → refuse.

**The trap, demonstrated:** stripping a path-qualified link to its stem routes **all fifteen**
`[[traditions/X/wiki]]` to `traditions/arkanihamed/wiki.md` — first alphabetically. A silent
drop becomes a silent 15-way misroute. Test §2 and §5 exist to make that unrepeatable, and
they fail against both the old resolver and the naive fix.

Also in the diff: self-targets suppressed (new with surname resolution), and mention edges
de-duplicated against authored pairs so one bracketed `[[Kastrup]]` can't fire at `type_w`
3.0 *and* 2.0.

## 3. Measured, old vs new, same vault, prediction registered beforehand

| | predicted | actual | |
|---|---|---|---|
| resolved pairs | 640 / 776 | 666 / 803 | ✅ newer vault, per-category match |
| wikilink edges | +181 | **+179** (500 → 679) | ✅ |
| files `bridge_authored` ≥ 1 | 38 | **37** | ✅ |
| max / levels | 15 / 11 | **15 / 11** | ✅ exact |
| nodes / reference edges | unchanged | unchanged | ✅ |
| mention edges | unchanged | **−146** | ⚠️ **prediction broken openly** — the de-dup you approved, not in the original prediction |

Net **+33 edges** on ~229,000. Misroute falsifier **passed**: inbound authored links land on
all 15 traditions, no concentration.

---

## 4. The two findings that matter more than the fix

**`bridge_authored` is retired as a Z-axis candidate.** 711 vault files carry a
`## Cross-Tradition Signals` section and hold **54 bracketed links** between them. People
write cross-tradition judgment as **prose**, not brackets. Fixed, the axis reaches 1.0%
off-floor — structural, not a bug.

**The asserted layer already exists, in the other pipeline.** Community Interactions →
Level 2 is built from `prototypes/signals_grown.json`: **1,152 dated, weighted, pair-typed
cross-tradition assertions with prose justification**, 82 of 105 pairs, 250 source cards.
The Sociogram contains **zero** of them. That is what the lift probe was actually looking
for. Wiring settled: `card → tradition A` + `card → tradition B`.
→ `handoffs/level2-signal-edges.md`

---

## 5. Corrected tonight — MacIntyre stays OPEN

I claimed his thinness was confirmed by two independent pipelines. **Wrong twice.** Level-2
harvests the same vault cards the Sociogram reads — different *pipeline*, same *corpus*. And
normalised, he isn't thin:

```
thinker         files  signals   sig/file
Wolfram           523      223      0.43
Friston           766      260      0.34
Levin             977      296      0.30
Loughran          279       30      0.11
MacIntyre         271       16      0.06   <- 5x worse than next lowest
```

271 files discuss him — level with Loughran (279). He's an outlier in **conversion**, not
presence: un-harvested material, not an absent thinker. 3RV named in **29 of 271** (11%),
already in `works_cited.json` (1990, verified).

Agent noted, not built → `handoffs/macintyre-crosslink-agent.md`, falsifier registered:
sig/file should climb toward ~0.30 after harvest; if it stays at 0.06 with 3RV cross-linked,
*that's* the real corpus finding.

**Method rule now on file:** "two pipelines agree" is not evidence about vault content when
both read the same prose. Independent about *extraction* only.

---

## 6. Open, in order

1. Review diff → commit → regen → **diff consumer outputs** → push
2. Level-2 signal edges — specced, `type_w` above 3.0 or they're invisible
3. MacIntyre 3RV cross-link agent — noted, unscoped
4. `validate_html.py` hardcoded `/tmp/_validate_html_js.js` — **still live for main's regen**
5. Untyped edges (4,089, 3.3%) still unnamed; `bridge_raw` silently includes them
6. Summa filter checkbox — needs the console probe at the moment of failure

**Stale correction:** `main` is `7fe274c`, not `2303e8a`.
**Budget:** session ran well past the 30k ceiling. Start Level-2 fresh from its handoff.
