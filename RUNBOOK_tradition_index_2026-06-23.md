# Runbook — Create the Tradition Index (reconnect the 15 orphaned hub pages)

**Author:** Sewing Agent bootstrap follow-up · 2026-06-23
**For:** an agent run inside the *RC Karpathy Wiki Project*
**Type:** surgical, append-only-style content addition (one new file + one one-line edit)
**Est. scope:** 2 file writes, ~10 minutes, fully reversible via git.

---

## Goal

Each of the 15 `traditions/<thinker>/wiki.md` hub pages currently receives **zero `[[wikilink]]` backlinks** — bridges and agents reference them only in backticks/prose, and link to `prs_triplets` instead. Create a single **tradition index** that links to all 15 hubs with real wikilinks, and link the index itself from the master wiki so it isn't a new orphan. This converts 15 orphans → connected and gives the graph a clean tradition-level entry point.

## Why this is the fix (context, do not re-derive)

- Confirmed 2026-06-23: only **one** genuine `[[wikilink]]` to any tradition hub exists in the entire vault (`[[traditions/carroll/wiki|Carroll Tradition Wiki]]`).
- The hubs link *outward* (to `prs_triplets`, bridges) but nothing links *in*.
- One index page is the highest-leverage, lowest-risk reconnection available.

---

## Assumptions (verify; stop and report if any fail)

1. All 15 files `traditions/<thinker>/wiki.md` exist (thinkers: arkanihamed, carroll, fredrickson, friston, hawkins, hoffman, kastrup, levin, loughran, macintyre, mcgilchrist, rohr, stump, wolfram, wright).
2. The vault wikilink convention is **path-qualified with alias**: `[[traditions/<thinker>/wiki|Display Name]]` (matches the dominant existing form, e.g. `[[traditions/kastrup/prs_triplets|Kastrup PRS]]`).
3. `master/C2A2_master_wiki.md` exists and is a reasonable, already-reachable page to link the index from. (If it isn't reachable, use `master/cross_program_index.md` instead and note the substitution.)

---

## Step 1 — Create `traditions/_index.md`

Write this file verbatim (display names are the H1 titles already in each hub):

```markdown
# Tradition Index

Entry point to all 15 thinker-tradition wikis in the C2A2 program. Each links to
that tradition's maintained hub page (`wiki.md`). Created 2026-06-23 to reconnect
the tradition hubs into the wikilink graph.

## Traditions

- [[traditions/arkanihamed/wiki|Nima Arkani-Hamed]]
- [[traditions/carroll/wiki|Sean Carroll]]
- [[traditions/fredrickson/wiki|Barbara Fredrickson]]
- [[traditions/friston/wiki|Karl Friston]]
- [[traditions/hawkins/wiki|Jeff Hawkins]]
- [[traditions/hoffman/wiki|Donald Hoffman]]
- [[traditions/kastrup/wiki|Bernardo Kastrup]]
- [[traditions/levin/wiki|Michael Levin]]
- [[traditions/loughran/wiki|Tom Loughran]]
- [[traditions/macintyre/wiki|Alasdair MacIntyre]]
- [[traditions/mcgilchrist/wiki|Iain McGilchrist]]
- [[traditions/rohr/wiki|Richard Rohr]]
- [[traditions/stump/wiki|Eleonore Stump]]
- [[traditions/wolfram/wiki|Stephen Wolfram]]
- [[traditions/wright/wiki|N.T. Wright]]
```

Before writing, re-read each hub's H1 (`grep -m1 '^# ' traditions/<t>/wiki.md`) and
use the actual title's person-name as the alias if any differs from the list above.
Conformance to existing titles > the names printed here.

## Step 2 — Link the index from the master wiki (so it isn't a new orphan)

Append one line to `master/C2A2_master_wiki.md`, under an existing relevant
section (or a new `## Traditions` heading if none fits):

```markdown
- See the [[traditions/_index|Tradition Index]] for all 15 thinker-tradition wikis.
```

Do not reformat or otherwise touch the rest of that file (surgical change only).

---

## Step 3 — Verify (success criteria — loop until all pass)

Run a backlink check that resolves **path-qualified** wikilinks (basename-only
resolution will give wrong results — this was a real bug found 2026-06-23):

```bash
cd "<vault root>/wiki"
python3 - <<'EOF'
import os,re
V="."
def npath(s): return re.sub(r'[\s_]+',' ',s.strip().lower()).strip('/')
files=[os.path.join(r,f) for r,_,fs in os.walk(V) for f in fs if f.endswith(".md")]
path={}
for p in files: path.setdefault(npath(os.path.splitext(os.path.relpath(p,V))[0]),p)
WL=re.compile(r'\[\[([^\]]+)\]\]')
back={p:set() for p in files}
for p in files:
    for m in WL.finditer(open(p,encoding="utf-8",errors="replace").read()):
        t=m.group(1).split("|")[0].split("#")[0].strip()
        tgt=path.get(npath(t))
        if tgt and tgt!=p: back[tgt].add(p)
hubs=[f"./traditions/{t}/wiki.md" for t in ["arkanihamed","carroll","fredrickson","friston","hawkins","hoffman","kastrup","levin","loughran","macintyre","mcgilchrist","rohr","stump","wolfram","wright"]]
print("Hubs with >=1 backlink:", sum(1 for h in hubs if len(back.get(h,()))>=1), "/ 15")
idx="./traditions/_index.md"
print("Index backlinks:", len(back.get(idx,())))
EOF
```

**Pass when:** `Hubs with >=1 backlink: 15 / 15` AND `Index backlinks: >= 1`.
If either fails, the most likely cause is an alias/path typo in Step 1 — fix and re-run.

---

## Constraints & notes

- **Surgical:** create one file, add one line. Do not refactor or reformat adjacent content. Match existing wikilink style.
- **Reversible:** all changes are git-tracked; revert with `git checkout` if needed.
- **This edits vault content, not the HTML visualization.** If you regenerate `wiki_narration.html` / `explorer.html` afterward, the project's standing rule applies: serve locally over HTTP and visually verify `http://localhost:8080/explorer.html` **before any `git push`**. This runbook itself does not push.
- **Optional enhancement (not required, skip unless asked):** add a reciprocal `[[traditions/_index|Tradition Index]]` line at the top of each hub's `wiki.md`. That makes the index a true bidirectional hub but touches 15 files — do it as a separate, explicitly-approved pass, not here.
```
