# Contributing

## Modifying the Visualization

### Template Rules (CRITICAL)

The HTML generator (`generate_visualization.py`) builds the entire HTML document as a Python string. These rules prevent template injection bugs:

1. **Never use f-strings.** The HTML template is a regular triple-quoted string.
2. **Data injection**: Use `""" + json_var + """` concatenation only.
3. **Single braces only** in CSS and JS: `{` and `}`. Never `{{` or `}}`.
4. **Escape `\n` for JS regex**: In the Python string, `\n` becomes a literal newline. Write `\\n` to produce `\n` in the JS output.
5. **Always validate** after any change: `python3 scripts/validate_html.py output/wiki_narration.html`

### Adding a New Thinker/Tradition

1. Add the color to the `COLORS` dict in `generate_visualization.py`
2. Add the tradition directory to the vault (e.g., `traditions/newthinker/wiki.md`)
3. The extractor and generator will pick it up automatically
4. The semantic narration engine will auto-index any findings or cross-connections that mention the new program name

### Modifying the Color Palette

Colors are defined in the `COLORS` dict at the top of `generate_visualization.py`. Use muted, desaturated tones — the dark background (#0a0a0f) makes saturated colors harsh.

### Adding New Semantic Data Sources

1. Add a parser function in `extract_vault_data.py` (follow the pattern of `parse_findings()`)
2. Add the data to the output dict in `main()`
3. In `generate_visualization.py`, serialize it as a JS constant and inject it into the HTML
4. Use it in the narration engine (`generateContextNarration()` or `buildNarrationTracks()`)

## Development Workflow

```bash
# Edit generate_visualization.py
# Then regenerate + validate:
python3 scripts/extract_vault_data.py /path/to/vault > /tmp/vault_data.json
python3 scripts/generate_visualization.py /tmp/vault_data.json output/wiki_narration.html
python3 scripts/validate_html.py output/wiki_narration.html --source-data /tmp/vault_data.json

# Open to verify
open output/wiki_narration.html
```

## Testing

The validator checks four things:

1. **JS syntax**: Extracts the `<script>` block and runs `node --check`
2. **Double braces**: Scans for `{{` or `}}` in CSS/JS (template escaping bugs)
3. **CSS brace balance**: Ensures all `{` have matching `}`
4. **Data integrity**: Node/link counts match source data (if provided)

Always run the validator before committing changes.
