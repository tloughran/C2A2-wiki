# C2A2 Wiki Narration Visualization

Interactive D3.js force-directed graph visualization for the C2A2 Obsidian vault — a multi-tradition intellectual exploration spanning 14 thinkers across philosophy, neuroscience, physics, and theology.

## What This Is

A self-contained HTML visualization that renders ~1,647 wiki files as an interactive node graph with:

- **Dynamic semantic narration** — auto-generates overviews based on which thinkers/groups are selected
- **Cross-connection discovery** — surfaces shared questions and findings between thinkers
- **Search** — query across files, findings, and cross-connections with highlighted results
- **Timeline modes** — History/Recent/Latest narration scoped to visible groups
- **TTS** — browser (Web Speech API) and OpenAI API backends with auto-fallback
- **Full interactivity** — click nodes to read wiki pages, click edges to compare connected pages, drag to rearrange, zoom/pan, resizable panels

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js (for validation only)
- An Obsidian vault in the C2A2 format

### Generate the Visualization

```bash
# 1. Extract data from your vault
python3 scripts/extract_vault_data.py /path/to/vault > /tmp/vault_data.json

# 2. Generate the HTML
python3 scripts/generate_visualization.py /tmp/vault_data.json output/wiki_narration.html

# 3. Validate (optional but recommended)
python3 scripts/validate_html.py output/wiki_narration.html --source-data /tmp/vault_data.json

# 4. Open in browser
open output/wiki_narration.html
```

### Use the Pre-built Version

If you just want to view the visualization without regenerating:

```bash
open output/wiki_narration.html
```

## File Structure

```
c2a2-wiki-narration/
  README.md                          — this file
  scripts/
    extract_vault_data.py            — vault data extractor (semantic + structural)
    generate_visualization.py        — HTML generator (D3.js, narration engine, TTS)
    validate_html.py                 — 4-check validator (JS syntax, braces, data integrity)
  output/
    wiki_narration.html              — generated visualization (~4MB, self-contained)
  docs/
    ARCHITECTURE.md                  — technical architecture and design decisions
    CONTRIBUTING.md                  — template rules, color palette, how to modify
```

## Architecture

### Data Pipeline

```
Obsidian Vault → extract_vault_data.py → vault_data.json → generate_visualization.py → wiki_narration.html
```

### Key Design Decisions

- **Self-contained HTML**: No external dependencies at runtime except D3.js CDN. Works from `file://`.
- **Python string templates**: The generator uses regular strings with `""" + var + """` concatenation. Never f-strings, never double braces in CSS/JS.
- **Performance**: Only visible nodes/edges exist in the DOM. Force simulation runs on the active subset only. Reference edges capped at 2,500 by connectivity score.
- **Crash-proofing**: MAX_NODES=2,000, MAX_EDGES=3,000 with warnings at 80%.

### Color Palette (muted)

| Thinker       | Color   | Key              |
|---------------|---------|------------------|
| Levin         | #C45B5B | traditions/levin |
| Friston       | #5A8EAF | traditions/friston |
| Hoffman       | #C08B3E | traditions/hoffman |
| Kastrup       | #8B5DAB | traditions/kastrup |
| McGilchrist   | #3D9E89 | traditions/mcgilchrist |
| Hawkins       | #B87D3E | traditions/hawkins |
| Wolfram       | #4A5E6D | traditions/wolfram |
| Carroll       | #4E8A5E | traditions/carroll |
| Arkani-Hamed  | #A85D3A | traditions/arkanihamed |
| Fredrickson   | #C47A9A | traditions/fredrickson |
| Stump         | #A8923A | traditions/stump |
| Rohr          | #9A7A5A | traditions/rohr |
| Wright        | #5A72A8 | traditions/wright |
| Loughran      | #4A8A7A | traditions/loughran |

### Semantic Data Sources

The extractor pulls from:

- **File content** (truncated to 1,500 chars per file)
- **Changelogs** — narrative summaries of daily changes
- **Findings** — pattern detector results with cross-program analysis
- **Decisions** — architectural decision records
- **Cross-connections** — inter-program questions and insights
- **Cowork summaries** — daily session accomplishments and discussion points

## Template Rules (Critical for Contributors)

1. The Python generator uses **regular strings** (NOT f-strings) for the HTML template
2. Data injection: `""" + json_var + """` concatenation only
3. CSS/JS must use **single braces** `{` `}` — never `{{` `}}`
4. Always validate with `node --check` on extracted JS before delivering
5. `\n` in Python strings becomes a literal newline — use `\\n` for JS regex patterns

## License

Private project. All rights reserved.
