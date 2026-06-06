#!/usr/bin/env python3
"""
generate_community_cards_data.py
Rebuilds wiki/community/data.js (the Cards directory dataset) as the union of:
  - the pristine bulk directory (the original 855 records), and
  - the 156 curated graph communities (curated_communities.json), transformed
    into the card schema and KEYED BY THEIR CC-xxx ids.

Keeping the CC-xxx ids makes the graph a literal id-subset of the cards (the
claim the "?" popover makes), and revives the deferred graph<->cards
cross-navigation hand-off, since both surfaces finally share a key.

Idempotent: the pristine 855 are snapshotted ONCE to data.base.json on first
run; every run rebuilds data.js from that snapshot + curated, so re-running
never double-appends. A curated community that duplicates a bulk record (by
url-host or normalized name) replaces the coarse bulk row with the richer
curated one.

Taxonomy: the 156 carry their real 8-type C2A2 taxonomy into the card Type
field (Tom's decision 2026-06-06) and are tagged Source_Directory =
"C2A2 curated (public web pages)" so they are isolable in the source facet.
app.js typeOrder must list those 8 types or the pills/heatmap drop them.

Consent: these records were seeded from publicly-available web pages WITHOUT
the communities' express consent; Verification_Method records that plainly.

Usage:
    python3 scripts/generate_community_cards_data.py
"""

import json
import re
from pathlib import Path
from urllib.parse import urlparse

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
COMMUNITY_DIR = REPO_ROOT / "wiki" / "community"
DATA_JS = COMMUNITY_DIR / "data.js"
BASE_JSON = COMMUNITY_DIR / "data.base.json"
CURATED_JSON = COMMUNITY_DIR / "curated_communities.json"

CURATED_SOURCE = "C2A2 curated (public web pages)"
CURATED_VERIFICATION = (
    "Curated from publicly-available web pages. Tool under construction; "
    "not yet confirmed by the community and seeded without its express consent."
)


def _parse_data_js(text):
    start = text.index("[")
    rows, _ = json.JSONDecoder().raw_decode(text[start:])
    return rows


def _host(url):
    try:
        return urlparse(url).netloc.lower().lstrip("www.")
    except Exception:
        return ""


def _norm(name):
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


def _norm_noparen(name):
    return _norm(re.sub(r"\(.*?\)", "", name or ""))


def _load_pristine_base():
    """The original bulk 855. Snapshot once to data.base.json, reuse thereafter."""
    if BASE_JSON.exists():
        return json.loads(BASE_JSON.read_text(encoding="utf-8"))
    rows = _parse_data_js(DATA_JS.read_text(encoding="utf-8"))
    base = [r for r in rows if not str(r.get("Community_ID", "")).startswith("CC-")]
    BASE_JSON.write_text(json.dumps(base, ensure_ascii=False, indent=0), encoding="utf-8")
    return base


def _curated_to_card(c):
    desc = c.get("description", "") or ""
    return {
        "Community_ID": c["community_id"],
        "Type": c.get("type", "Unspecified"),
        "Subtype": c.get("subtype", "") or "",
        "Community_Name": c.get("name", ""),
        "Country": c.get("country", "") or "Unspecified",
        "Country_Source": CURATED_SOURCE,
        "Verified_Link": c.get("url", "") or "",
        "Verified_Link_Host": _host(c.get("url", "")),
        "Email_Contact": "none located",
        "Email_Retrieval_Note": "Not collected for curated graph records.",
        "Narrative_Description": desc,
        "Narrative_Word_Count": len(desc.split()),
        "Narrative_Grounding": c.get("source", "") or "Publicly-available web pages.",
        "PRS_Triplet_Count": 1,
        "Problem_Statement": c.get("problem", "") or "",
        "Resource_Statement": c.get("resource", "") or "",
        "Solution_Statement": c.get("solution", "") or "",
        "prs_quality": c.get("prs_quality"),
        "Source_Directory": CURATED_SOURCE,
        "Source_Link": c.get("url", "") or "",
        "Verification_Method": CURATED_VERIFICATION,
    }


def main():
    base = _load_pristine_base()
    curated = json.loads(CURATED_JSON.read_text(encoding="utf-8"))

    # Index the curated communities' identity keys to find bulk duplicates.
    cur_hosts = {_host(c.get("url", "")) for c in curated if _host(c.get("url", ""))}
    cur_names = {_norm(c["name"]) for c in curated} | {_norm_noparen(c["name"]) for c in curated}

    kept_base, dropped = [], []
    for r in base:
        h = _host(r.get("Verified_Link", ""))
        n = _norm(r.get("Community_Name", ""))
        if (h and h in cur_hosts) or (n and n in cur_names):
            dropped.append(r.get("Community_Name", ""))
        else:
            kept_base.append(r)

    cards = kept_base + [_curated_to_card(c) for c in curated]

    DATA_JS.write_text(
        "window.COMMUNITY_DATA = " + json.dumps(cards, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    print("Pristine base:", len(base), "| dropped as curated-duplicates:", len(dropped))
    if dropped:
        print("  dropped:", "; ".join(dropped))
    print("Curated added:", len(curated), "| total cards:", len(cards))


if __name__ == "__main__":
    main()
