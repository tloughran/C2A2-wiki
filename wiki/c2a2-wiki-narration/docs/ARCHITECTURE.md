# Architecture

## System Overview

The C2A2 Wiki Narration system is a three-stage pipeline that transforms an Obsidian vault into an interactive force-directed graph visualization with semantic narration.

## Pipeline Stages

### Stage 1: Data Extraction (`extract_vault_data.py`)

Scans the vault and extracts both structural and semantic data.

**Structural data**: file paths, dates (from filenames or mtime), wikilink relationships, shared reference codes (FINDING-*, CROSS-*, DECISION-*, etc.), directory categorization.

**Semantic data**: changelog narratives, pattern detector findings, architectural decisions, cross-program connection index, daily cowork-to-chat summaries.

Output: a single JSON file (~15MB for a 1,647-file vault).

### Stage 2: HTML Generation (`generate_visualization.py`)

Consumes the JSON and produces a self-contained HTML file with embedded D3.js v7, all data constants, CSS, and JavaScript.

Key subsystems in the generated HTML:

**Graph engine**: D3 force simulation with zoom, drag, and collision detection. Nodes are colored by group, sized by connection count (2-5px). Only visible nodes/edges exist in the DOM — `rebuildGraph()` tears down and recreates SVG elements on every filter change.

**Semantic narration engine**: Pre-indexes findings and cross-connections by tradition group. `generateContextNarration()` runs on every filter change and assembles a narrative from wiki overviews, relevant findings, and shared cross-program questions. The History/Recent/Latest timeline modes scope their content to visible groups.

**Search**: Full-text search across node content, findings, and cross-connections with visual highlighting of matching nodes.

**TTS**: Dual backend — Web Speech API (browser) and OpenAI API. Uses XMLHttpRequest instead of fetch for file:// CORS compatibility. Auto-falls back to browser voice on API error. Settings persisted in localStorage.

**Template strategy**: The Python generator builds HTML as a regular Python string using `""" + var + """` concatenation for data injection. This avoids f-string `{}` conflicts with CSS/JS braces. All CSS and JS use single braces only.

### Stage 3: Validation (`validate_html.py`)

Four checks run against the generated HTML:

1. **JS syntax** — extracts the script block and runs `node --check`
2. **Double-brace detection** — scans CSS and JS for `{{` or `}}` which would indicate template escaping errors
3. **CSS brace balance** — verifies matched `{` `}` pairs in the style block
4. **Data integrity** — if source JSON is provided, verifies node count and link count match expectations

## Data Model

### Nodes

Each node represents a markdown file in the vault:

- `id`: relative file path (unique identifier)
- `label`: extracted title (first `# ` heading or first line)
- `group`: color group key (e.g., `traditions/levin`, `architecture`)
- `color`: hex color from the palette
- `size`: 2-5px based on connection count
- `content`: first 1,500 characters of file content
- `date`: from filename pattern `YYYY-MM-DD` or file mtime
- `x`, `y`: position (pre-seeded by group, then refined by simulation)

### Links

Two types:

- **Wikilinks**: `[[Target]]` references between files. All kept.
- **Reference edges**: Files sharing the same reference code (FINDING-001, CROSS-003, etc.). Sorted by combined connectivity score, capped at 2,500.

### Semantic Indexes (built at load time)

- `FINDINGS_BY_GROUP`: maps group keys to relevant findings based on program name matching
- `CROSSES_BY_GROUP`: maps group keys to relevant cross-connections
- `GROUP_TO_PROGRAMS`: maps group keys to program name patterns for text matching

## Performance Constraints

- MAX_NODES: 2,000 (warning at 1,600)
- MAX_EDGES: 3,000 (warning at 2,500)
- Per-file content: 1,500 characters max
- Reference edges: 2,500 max (sorted by connectivity score)
- Force simulation: alphaDecay 0.05, theta 0.9 for Barnes-Hut approximation
