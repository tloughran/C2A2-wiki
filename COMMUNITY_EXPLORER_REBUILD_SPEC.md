# Community Explorer — Rebuild Spec (handoff)

**Date:** 2026-05-21
**Owner:** Tom Loughran
**Status:** Approved direction; build not started. Run as a fresh, focused session.
**Resume cue:** open a new Cowork thread and say *"resume the community explorer rebuild"* (or paste the path to this file). Memory entries `project_C2A2_community_explorer`, `project_C2A2_community_model`, and `project_C2A2_explorer_shell` carry the context.

---

## 1. Purpose — what this chapter is FOR

The Community Explorer is one chapter of the C2A2 ("align-with-small-communities") explorer. It is **an instrument communities use on themselves first**, not a directory to browse.

It helps a community clarify its own:

- **Goals**
- **Problems** it faces
- **Resources** it has / taps / needs
- **Solutions** it has effected / proposes

…held first and only for the community itself if it prefers, and exposed to others **only at its discretion**. The payoffs are (a) discovery — finding peers and being found — and (b) the ability to track progress and whether/how AI assistance helps them make it (the "Detector" half: measuring AI acceleration).

Community **exploration** and community **AI education** are both prerequisites for tracking meaningful AI acceleration; each is its own chapter tab with its own tools. This spec covers the Explorer chapter only.

Strategic placement: this is the **Pathway-20 (Institutional Scale) substrate** — "the Sociogram's nodes become communities rather than thinkers." It is NOT on the ISME critical path (ISME = July 8–10, 2026; critical path = pathways 00/01/02/03/08). Treat it as a portability proof-point and broker groundwork, not a deadline item.

---

## 2. Current state (what is already built and staged)

All staged in `wiki/community/` inside the C2A2-wiki repo. **Validated (`node --check` on all JS) but NOT pushed.** The current layout is the one we agreed reads as clunky/amateurish — the rebuild replaces the *shell*, reusing the *machinery*.

Files in `wiki/community/`:

- `index.html` — current single-page layout (to be rebuilt).
- `app.js` — faceted filtering engine + state + table/charts/detail. Contains the finished migration to the deterministic engine, the broker-ready `getKey()`/`callLLM()` seam, `enrichWithLLM()` (gpt-4o-mini, deterministic fallback), and a `cc:rows` CustomEvent dispatched at the end of `update()` carrying the current filtered slice.
- `ai-query-core.js` — fully client-side, zero-network deterministic NL query engine (`answerQueryLocally`, `runDatasetQuery`). No embeddings, no server.
- `search-core.js` — lexical term scoring.
- `data.js` — 855 community records embedded (`window.COMMUNITY_DATA`, `window.COMMUNITY_META`). ~1.9 MB.
- `styles.css` — re-skinned to C2A2 dark/gold (token swap + appended override layer). Original light theme saved as `styles.css.bak.lighttheme`.
- `community-views.js` — Map (Leaflet) + PRS Triplets views; listens for `cc:rows`; tab switching.
- `country_coordinates.js` — 89 country centroids + aliases (generated from the Streamlit `country_coordinates.py`).
- `*.bak.*` — safety backups (git-ignored).

Shell: `wiki/explorer.html` — the "Community Explorer" chapter tab is wired (promoted from stub; loads `community/index.html`; hides the Accelerator-Tools sub-tab row for this chapter; has a help-modal entry).

Source repo (separate): `~/Documents/Claude/Projects/c2a2-community-explorer/` — contains the **Streamlit twin** (`streamlit_app.py`, `platform_store.py`, `country_coordinates.py`) whose Map and PRS tabs we ported, plus git bundles. Left untouched.

Data schema (per record in `data.js`): `Community_ID, Type, Subtype, Community_Name, Country, Country_Source, Verified_Link, Verified_Link_Host, Email_Contact, Email_Retrieval_Note, Narrative_Description, Narrative_Word_Count, Problem_Statement, Resource_Statement, Solution_Statement, PRS_Triplet_Count, Source_Directory, Source_Link, Verification_Method, Narrative_Grounding`. Types: Academic, Corporate, Ideological.

---

## 3. Why rebuild (the verdict)

Keep the chapter, but only if rebuilt around its one distinctive asset — communities read through the Goals/Problems/Resources/Solutions lens. As a faceted CSV dashboard it adds nothing. The current page fails structurally: two competing stat bands up top; a heatmap + 2×2 chart wall as the front door; the communities and their PRS framings buried in a table + side panel; a fat left rail stacking dev-cruft (the agent-prompt stub, data-notes card). It reads like an admin template. The fix is to put the substance on the surface.

---

## 4. Target design

Approved concept (a desktop mockup was shown and accepted in the originating session):

- **Search/ask is the masthead and primary action** — the deterministic + BYOK-AI-enriched search, front and center.
- **Cards / Map / PRS / Overview are peer modes.** Default = Cards.
  - **Cards:** a responsive grid of community cards, each showing its P→R→S at a glance, Type-coded. The discovery + peer-finding surface.
  - **Map:** the existing Leaflet dark map (reuse `community-views.js` `renderMap`).
  - **PRS:** the existing PRS browser with focus filter (reuse `community-views.js` `renderPRS`).
  - **Overview:** where the heatmap + distribution charts move (available, not in the way).
- **Filters collapse to a slim chip row** (Type chips, Country, +Filter, active-filter chips). Kill the fat left rail.
- **Click a card → a reader** (drawer or panel) = the GPRS self-articulation profile (see §5).
- **Cut the user-facing dev surfaces** (agent-prompt stub, data-notes card) — move to a dev/export menu if kept at all.
- **Skin:** C2A2 dark `#0a0a0f` / panels `#15151f` / gold `#C9A84C`, Georgia for display headings, generous whitespace. Reads as family with the Sociogram and Connectome.

---

## 5. The GPRS schema (the spine)

Records have **two states**, and every field must be marked which (Pathway 14 honesty layer):

- **Inferred seed** — the scraped/working description we already have. The 855 records are all this state today.
- **Community-claimed** — articulated/edited by the community itself.

Schema to present in the reader (richer than the current P/R/S triplet):

- **Goals** — *new field; empty/inferred to start.*
- **Problems** — seed from `Problem_Statement`.
- **Resources** — split into **have / tap / need**. Seed `Resource_Statement` into one bucket (probably "have"); the others start empty/inferred.
- **Solutions** — split into **effected / proposed**. Seed `Solution_Statement`; sub-split starts inferred.
- Plus provenance (`Source_Directory`, `Source_Link`, `Verification_Method`, `Narrative_Grounding`) and `Verified_Link`.

---

## 6. Build plan (tasks #16–#19 in the tracker)

**Chosen scope:** discovery redesign + GPRS reader presentation now (real, using the 855 as clearly-labeled inferred seed); claim/visibility + progress as **designed-in, non-persistent stubs** (no backend yet). The two alternatives considered were "add local (localStorage) claim/edit too" and "discovery redesign only" — default to the middle path unless Tom redirects.

1. **Rebuild the chapter shell** — search-first masthead; Cards/Map/PRS/Overview modes; slim filter chips; one slim stat line. Reuse the engine (do not rewrite filtering/search/map/prs). Acceptance: loads in the shell iframe, dark/gold, no chart-wall front door.
2. **GPRS self-articulation reader** — card click opens the Goals · Problems · Resources(have/tap/need) · Solutions(effected/proposed) profile, each field marked inferred vs claimed, with provenance + link. Acceptance: reader renders the fuller schema from a record; inferred badges visible.
3. **Card-forward discovery + peer-finding** — cards as default canvas; analytics moved to Overview. Acceptance: Cards is the landing view; Overview holds heatmap + charts.
4. **Claim/visibility + progress stubs** — "this is our community — claim & refine" affordance, visibility control (self/peers/public), per-community progress strip (snapshots over time, mark where AI was applied). Non-persistent, architected for the broker to drop in. Acceptance: affordances visible and coherent; clearly marked as not-yet-persistent.

---

## 7. What carries forward unchanged (do not rewrite)

- `ai-query-core.js`, `search-core.js`, `data.js` — as-is.
- `app.js` filtering/state/search + the broker-ready seam + `enrichWithLLM` + the `cc:rows` dispatch — reuse; the new shell consumes `cc:rows` exactly as `community-views.js` does.
- `community-views.js` map + PRS renderers + `country_coordinates.js` — reuse for the Map and PRS modes.
- The chapter-tab wiring in `wiki/explorer.html` — already done.

The rebuild is the shell (`index.html` structure + `styles.css` layout) + the new GPRS reader + the new card grid + the claim/visibility/progress stubs.

---

## 8. Constraints & conventions

- **Broker-ready, no client keys long-term.** Pathway 00 (settled, ISME-critical) forbids client-side API keys on the public page. The current BYOK-in-`localStorage` (`tts_api_key`) is a pre-broker stopgap. Keep ALL key/LLM access behind the single `getKey()`/`callLLM()` seam so the broker swaps in with no caller changes. This chapter is the first broker-ready tab.
- **Honesty layer.** Mark inferred-seed vs community-claimed everywhere (Pathway 14).
- **No backend yet** → claim/visibility/progress are stubs. Real persistence + selective per-peer sharing arrive with the broker (Pathways 19/20).
- **CSS:** dark/gold tokens already in `styles.css :root`. Single braces in any generator; validate JS with `node --check`.
- **Constitutional rule — no blind pushes.** Before any `git push`: serve `wiki/` over `python3 -m http.server 8080`, review `http://localhost:8080/explorer.html` (the full shell, not `community/index.html` alone), report observations, get Tom's explicit sign-off, THEN push. Sandbox cannot push; Tom pushes from his Mac.
- **Push sequencing:** hold the push. The rebuild supersedes the current layout — push the redesigned chapter once it's reviewed, not the current clunky version. Stage everything in `wiki/community/`.
- **Obsidian caution:** edits to `wiki/**` while Obsidian is open can revert; reload-without-saving, verify from disk.

---

## 9. Key paths

- Deployment chapter: `~/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/community/`
- Shell: `~/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/explorer.html`
- Streamlit twin (Map/PRS source of truth): `~/Documents/Claude/Projects/c2a2-community-explorer/streamlit_app.py`
- Repo: `github.com/tloughran/C2A2-wiki` (public, branch `main`); served via GitHub Pages.

---

## 10. Deferred / dev-track (out of scope for the first rebuild)

- A separate **"Discuss"** chat mode (vs. search).
- Real **web-grounding** for the AI (needs the broker; `database_plus_web`).
- Standardize/rename the shared key beyond the misnomer `tts_api_key` (with migration).
- Fold the `styles.css` override layer into base rules.
- Roll the same search(+discuss) + broker-ready pattern across the other tabs.
- The **Community AI Education** chapter (its own tab/tools).
- Real persistence + selective per-peer sharing + progress/AI-acceleration measurement (broker era).
