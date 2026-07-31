#!/usr/bin/env python3
"""Build wiki/interT_study.html from its markdown sources.

Why this exists
---------------
The page renders markdown client-side out of `<script type="text/markdown">`
blocks, so the markdown lived in the HTML as a hand-pasted copy of the file in
`openstory-legibility/`. Two copies, no build step, and by 2026-07-31 they had
drifted in both directions at once: the HTML had a byline the markdown lacked,
and the markdown had two content blocks -- the "What we find, in brief"
paragraph in section 1 and the human-arm numbers in Appendix E -- that had gone
missing from the published page. Nobody edited them out on purpose; a paste
went stale.

So the HTML is now a function of the markdown, and `--check` fails loudly if
the file on disk is not what the sources build to. Adding the replication
doubled the number of copies at risk, which is what forced the issue.

Usage
-----
    python3 scripts/build_study.py              # write wiki/interT_study.html
    python3 scripts/build_study.py --check      # exit 1 if on-disk output is stale
"""
import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHELL = ROOT / "wiki" / "study_shell.html"
OUT = ROOT / "wiki" / "interT_study.html"

# Order here is tab order; the first entry is what opens by default.
DOCS = [
    {
        "key": "study",
        "label": "Study",
        "src": "openstory-legibility/study_interT_dialogue_c2a2.md",
    },
    {
        "key": "replication",
        "label": "Replication N=38",
        "src": "openstory-legibility/replication_rung1_N38.md",
    },
]


def build() -> str:
    shell = SHELL.read_text()

    buttons, blocks = [], []
    for i, d in enumerate(DOCS):
        md = (ROOT / d["src"]).read_text()
        # A literal </script> in the markdown would close the block early and
        # silently truncate the document in the browser. Refuse rather than ship it.
        if "</script>" in md.lower():
            sys.exit(f"ERROR: {d['src']} contains a literal </script>; "
                     "it cannot be embedded in a text/markdown block.")
        cls = ' class="active"' if i == 0 else ""
        buttons.append(f'<button data-doc="{d["key"]}"{cls}>{d["label"]}</button>')
        blocks.append(
            f'<script type="text/markdown" id="doc-{d["key"]}">\n{md.rstrip()}\n</script>'
        )

    html = shell.replace("__TAB_BUTTONS__", "".join(buttons))
    html = html.replace("__DOC_BLOCKS__", "\n\n".join(blocks))

    if "__" in html and any(t in html for t in ("__TAB_BUTTONS__", "__DOC_BLOCKS__")):
        sys.exit("ERROR: a template placeholder survived substitution.")
    return html


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="do not write; exit non-zero if the built output differs from disk")
    args = ap.parse_args()

    html = build()

    if args.check:
        if not OUT.exists():
            print(f"STALE: {OUT.relative_to(ROOT)} does not exist", file=sys.stderr)
            return 1
        if OUT.read_text() != html:
            print(f"STALE: {OUT.relative_to(ROOT)} differs from what its markdown "
                  f"sources build to. Run: python3 scripts/build_study.py", file=sys.stderr)
            return 1
        print(f"OK: {OUT.relative_to(ROOT)} matches its {len(DOCS)} markdown sources")
        return 0

    OUT.write_text(html)
    print(f"wrote {OUT.relative_to(ROOT)}  ({len(html):,} bytes, {len(DOCS)} documents)")
    for d in DOCS:
        print(f"  {d['key']:12s} {d['src']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
