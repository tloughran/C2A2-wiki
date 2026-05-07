# RC Karpathy Wiki Project — Claude Standing Instructions

## CONSTITUTIONAL RULE: No Blind Pushes to GitHub

**Before any `git push` to any GitHub repository, Claude must:**

1. Serve the affected HTML locally over HTTP (`python3 -m http.server 8080` from the `wiki/` folder, or equivalent)
2. Use the browser (via Claude-in-Chrome or computer-use screenshot) to visually verify the changed page loads and renders correctly
3. Report specific observations to the user ("ToC loads with N entries, article click works, no console errors")
4. Wait for explicit user sign-off before pushing

**This rule applies to:** C2A2-wiki, any Summa repository, and any other GitHub repo touched in this Claude account.

**Rationale:** We pushed `adbd456` without local HTTP review (2025-05-07) and the user reported unexpected behavior. A 30-second local check would have caught it.

---

## Wiki Narration Visualization

**Working URL (local):** `file:///Users/tomloughran/Documents/Claude/Projects/RC%20Karpathy%20Wiki%20Project/wiki/wiki_narration.html`

**Vault path:** `/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki/`

### Key Files (relative to vault root)
- `wiki_narration.html` — the generated visualization (self-contained, ~4MB)
- Source scripts are in the Cowork session at:
  - `wiki-narration/scripts/generate_visualization.py` — HTML generator
  - `wiki-narration/scripts/extract_vault_data.py` — vault data extractor
  - `validate-html/scripts/validate_html.py` — HTML validation (JS syntax, brace balance, data integrity)
  - `wiki-narration/SKILL.md` — skill definition
  - `validate-html/SKILL.md` — validation skill definition

### Regeneration Workflow
```bash
python3 extract_vault_data.py /path/to/vault > /tmp/vault_data.json
python3 generate_visualization.py /tmp/vault_data.json /path/to/wiki/wiki_narration.html
python3 validate_html.py /path/to/wiki/wiki_narration.html --source-data /tmp/vault_data.json
```

### Architecture
- D3.js v7 force-directed graph, dark theme (#0a0a0f)
- 1647 nodes (wiki files), ~3000 edges (wikilinks + shared references)
- Left panel: checkbox filters by tradition (14 thinkers) and structure group (10 categories)
- Upper-right: Hold Forces, Show Hover Names, Fit All
- Node click → right panel with rendered markdown; edge click → both panels
- 6 narration tracks assembled at load: History/Recent/Latest x Brief/Deep
- TTS: browser (Web Speech API) and OpenAI API backends
- Crash-proofing: node limit 2000, edge limit 3000, warnings at 80%

### Color Palette (muted)
- Levin #C45B5B, Friston #5A8EAF, Hoffman #C08B3E, Kastrup #8B5DAB
- McGilchrist #3D9E89, Hawkins #B87D3E, Wolfram #4A5E6D, Carroll #4E8A5E
- Arkani-Hamed #A85D3A, Fredrickson #C47A9A, Stump #A8923A
- Rohr #9A7A5A, Wright #5A72A8, Loughran #4A8A7A
- Master #C9A84C, Architecture #5B7FA5, Agents #8B6DAE

### Template Rules (critical for contributors)
- Python generator uses regular strings (NOT f-strings) for HTML template
- Data injection: `""" + json_var + """` concatenation only
- CSS/JS must use single braces `{` `}` — never `{{` `}}`
- Always validate with `node --check` on extracted JS before delivering

---

## Summa Explorer

- `summa_explorer.html` fetches `./vault/refs/summa_index.json` (relative, same repo)
- Vault data lives at `wiki/vault/` in C2A2-wiki repo
- `sync_vault.sh` + launchd agent at 21:00 daily keeps vault in sync from Summa 2026 project
- **Before pushing updates to summa_explorer.html or vault data:** verify locally via HTTP server
