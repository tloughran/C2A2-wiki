#!/usr/bin/env python3
"""
Extract structured temporal, connection, and SEMANTIC data from an Obsidian vault.

Goes deep: reads changelogs for narrative summaries, findings for intellectual content,
decisions for rationale, cross-program items for context. Produces rich JSON for
narrated visualization.

Usage:
    python3 extract_vault_data.py /path/to/vault > vault_data.json
"""

import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def extract_date_from_filename(filename):
    match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    return match.group(1) if match else None


def extract_date_from_mtime(filepath):
    mtime = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')


def extract_title(content):
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    for line in content.split('\n'):
        line = line.strip()
        if line and not line.startswith('---'):
            return line[:100]
    return "Untitled"


def extract_wikilinks(content):
    return list(set(re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]', content)))


def extract_references(content):
    patterns = [
        r'FINDING-\d+[a-z]?', r'CROSS-\d+', r'DECISION-\d+',
        r'OPEN-\d+', r'PRS-\d+', r'PREMISE-\d+',
        r'ASSUMPTION-\d+', r'PRESUMPTION-\d+', r'PROP-[\d-]+',
    ]
    refs = set()
    for p in patterns:
        refs.update(re.findall(p, content))
    return sorted(refs)


# Lastname → tradition wiki path. The bridge between architectural prose mentions
# and the canonical thinker page. Update this table when a new tradition is added.
THINKER_PATHS = {
    "Levin":         "traditions/levin/wiki.md",
    "Friston":       "traditions/friston/wiki.md",
    "Hoffman":       "traditions/hoffman/wiki.md",
    "Kastrup":       "traditions/kastrup/wiki.md",
    "McGilchrist":   "traditions/mcgilchrist/wiki.md",
    "Hawkins":       "traditions/hawkins/wiki.md",
    "Wolfram":       "traditions/wolfram/wiki.md",
    "Carroll":       "traditions/carroll/wiki.md",
    "Arkani-Hamed":  "traditions/arkanihamed/wiki.md",
    "Fredrickson":   "traditions/fredrickson/wiki.md",
    "Stump":         "traditions/stump/wiki.md",
    "MacIntyre":     "traditions/macintyre/wiki.md",
    "Rohr":          "traditions/rohr/wiki.md",
    "Wright":        "traditions/wright/wiki.md",
    "Loughran":      "traditions/loughran/wiki.md",
}


def extract_thinker_mentions(content):
    """Whole-word match each tradition surname; return distinct tradition paths
    mentioned in the file. This bridges architecture-prose ↔ tradition-wiki —
    the extractor's previous edge logic ('shared identifier' co-mentions) never
    crossed the namespace gap because tradition files use PRS-NN while
    architecture files use ASSUMPTION/PRESUMPTION/DECISION/etc."""
    mentioned = []
    for surname, path in THINKER_PATHS.items():
        if re.search(r'\b' + re.escape(surname) + r'\b', content):
            mentioned.append(path)
    return sorted(set(mentioned))


def get_directory_category(rel_path):
    parts = Path(rel_path).parts
    if len(parts) == 1:
        return "root"
    top = parts[0]
    if top == "traditions" and len(parts) >= 2:
        return f"traditions/{parts[1]}"
    if top == "inbox" and len(parts) >= 2 and parts[1] == "proposals":
        return f"inbox/proposals/{parts[2]}" if len(parts) >= 3 else "inbox/proposals"
    return top


# === SEMANTIC EXTRACTORS ===

def parse_changelogs(vault_path):
    """Read changelog files and extract narrative summaries + change entries."""
    changelog_dir = Path(vault_path) / "architecture" / "changelog"
    changelogs = {}
    if not changelog_dir.exists():
        return changelogs

    for f in sorted(changelog_dir.glob("*.md")):
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', f.name)
        if not date_match:
            continue
        date = date_match.group(1)
        content = f.read_text(encoding='utf-8', errors='replace')

        # Extract narrative summary (## Narrative Summary section)
        narrative = ""
        narr_match = re.search(r'## Narrative Summary\s*\n+(.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
        if narr_match:
            narrative = narr_match.group(1).strip()

        # Extract individual changes
        changes = []
        for ch_match in re.finditer(
            r'## (CHANGE-[\d-]+.*?)\n(.*?)(?=\n## |\n---|\Z)', content, re.DOTALL
        ):
            title = ch_match.group(1).strip()
            body = ch_match.group(2).strip()
            # Get first meaningful line as summary
            lines = [l.strip().lstrip('- ') for l in body.split('\n') if l.strip() and not l.strip().startswith('*')]
            summary = lines[0] if lines else ""
            changes.append({"title": title, "summary": summary, "full": body[:500]})

        changelogs[date] = {
            "narrative": narrative,
            "changes": changes,
            "change_count": len(changes),
        }

    return changelogs


def parse_findings(vault_path):
    """Read findings file and extract structured finding data."""
    findings_file = Path(vault_path) / "flags" / "pattern_detector_findings.md"
    findings = []
    if not findings_file.exists():
        return findings

    content = findings_file.read_text(encoding='utf-8', errors='replace')

    # Split on FINDING- entries
    for match in re.finditer(
        r'(FINDING-\d+[a-z]?):\s*\n(.*?)(?=\nFINDING-|\n---\s*\n(?=FINDING)|\Z)',
        content, re.DOTALL
    ):
        fid = match.group(1)
        body = match.group(2)

        # Extract fields
        programs = ""
        pm = re.search(r'Programs?:\s*(.+)', body)
        if pm:
            programs = pm.group(1).strip()

        eval_type = ""
        em = re.search(r'Evaluation type:\s*(.+)', body)
        if em:
            eval_type = em.group(1).strip()

        finding_text = ""
        fm = re.search(r'Finding:\s*(.+?)(?=\nConfidence:|\nRecommended|\n\[EVALUATED|\Z)', body, re.DOTALL)
        if fm:
            finding_text = fm.group(1).strip()

        confidence = ""
        cm = re.search(r'Confidence:\s*(.+)', body)
        if cm:
            confidence = cm.group(1).strip()

        date = ""
        dm = re.search(r'Date evaluated:\s*(.+)', body)
        if dm:
            date = dm.group(1).strip()

        # Create a short voice-friendly summary (first 2 sentences of finding)
        sentences = re.split(r'(?<=[.!?])\s+', finding_text)
        short = ' '.join(sentences[:2]) if sentences else finding_text[:200]

        findings.append({
            "id": fid,
            "date": date,
            "programs": programs,
            "type": eval_type,
            "finding": finding_text[:600],
            "short": short[:300],
            "confidence": confidence,
        })

    return findings


def parse_decisions(vault_path):
    """Read decisions file and extract structured decision data."""
    decisions_file = Path(vault_path) / "architecture" / "decisions.md"
    decisions = []
    if not decisions_file.exists():
        return decisions

    content = decisions_file.read_text(encoding='utf-8', errors='replace')

    for match in re.finditer(
        r'(DECISION-\d+):\s*\n(.*?)(?=\nDECISION-|\Z)',
        content, re.DOTALL
    ):
        did = match.group(1)
        body = match.group(2)

        date = ""
        dm = re.search(r'Date:\s*(.+)', body)
        if dm:
            date = dm.group(1).strip()

        title = ""
        tm = re.search(r'Title:\s*(.+)', body)
        if tm:
            title = tm.group(1).strip()

        summary = ""
        sm = re.search(r'Summary:\s*(.+?)(?=\n\s*\w+:|\Z)', body, re.DOTALL)
        if sm:
            summary = sm.group(1).strip()

        category = ""
        cm = re.search(r'Category:\s*(.+)', body)
        if cm:
            category = cm.group(1).strip()

        decisions.append({
            "id": did,
            "date": date,
            "title": title,
            "summary": summary[:400],
            "category": category,
        })

    return decisions


def parse_cross_connections(vault_path):
    """Read cross-program index and extract connection data."""
    cross_file = Path(vault_path) / "master" / "cross_program_index.md"
    crosses = []
    if not cross_file.exists():
        return crosses

    content = cross_file.read_text(encoding='utf-8', errors='replace')

    for match in re.finditer(
        r'(CROSS-\d+):\s*\n(.*?)(?=\nCROSS-|\n---\s*\n(?=CROSS)|\Z)',
        content, re.DOTALL
    ):
        cid = match.group(1)
        body = match.group(2)

        question = ""
        qm = re.search(r'Question/Insight:\s*(.+)', body)
        if qm:
            question = qm.group(1).strip()

        programs = ""
        pm = re.search(r'Programs involved:\s*(.+)', body)
        if pm:
            programs = pm.group(1).strip()

        nature = ""
        nm = re.search(r'Nature of connection:\s*(.+)', body)
        if nm:
            nature = nm.group(1).strip()

        notes = ""
        ntm = re.search(r'Notes:\s*(.+?)(?=\n\s*\w+:|\Z)', body, re.DOTALL)
        if ntm:
            notes = ntm.group(1).strip()

        crosses.append({
            "id": cid,
            "question": question,
            "programs": programs,
            "nature": nature,
            "notes": notes[:400],
        })

    return crosses


def parse_cowork_summary(vault_path):
    """Read the daily cowork-to-chat summaries for rich narrative."""
    sync_dir = Path(vault_path) / "architecture" / "daily_sync" / "cowork_to_chat"
    summaries = {}
    if not sync_dir.exists():
        return summaries

    for f in sorted(sync_dir.glob("*.md")):
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', f.name)
        if not date_match:
            continue
        date = date_match.group(1)
        content = f.read_text(encoding='utf-8', errors='replace')

        # Extract "What Was Accomplished" section
        accomplished = ""
        am = re.search(r'## What Was Accomplished.*?\n+(.*?)(?=\n## |\Z)', content, re.DOTALL)
        if am:
            accomplished = am.group(1).strip()

        # Extract "For Morning Discussion" items
        discussion = ""
        dm = re.search(r'## For Morning Discussion.*?\n+(.*?)(?=\n## |\Z)', content, re.DOTALL)
        if dm:
            discussion = dm.group(1).strip()

        summaries[date] = {
            "accomplished": accomplished[:800],
            "discussion": discussion[:600],
        }

    return summaries


def scan_vault(vault_path):
    """Scan vault for all markdown files with metadata."""
    vault = Path(vault_path)
    files = []
    for md_file in sorted(vault.rglob("*.md")):
        rel = md_file.relative_to(vault)
        if str(rel).startswith('.'):
            continue
        try:
            content = md_file.read_text(encoding='utf-8', errors='replace')
        except Exception:
            content = ""
        date = extract_date_from_filename(md_file.name)
        if not date:
            date = extract_date_from_mtime(str(md_file))
        files.append({
            "filepath": str(rel),
            "filename": md_file.name,
            "directory": get_directory_category(str(rel)),
            "date": date,
            "title": extract_title(content),
            "wikilinks": extract_wikilinks(content),
            "references": extract_references(content),
            # Computed on FULL content (before the [:1500] truncation that
            # follows) so prose mentions deep in long architecture docs still
            # produce edges to the named thinker's wiki page.
            "thinker_mentions": extract_thinker_mentions(content),
            "size_bytes": len(content.encode('utf-8')),
            "content": content[:1500],
        })
    return files


def build_timeline(files):
    by_date = defaultdict(list)
    for f in files:
        by_date[f["date"]].append(f)
    timeline = []
    cumulative = 0
    for date in sorted(by_date.keys()):
        day_files = by_date[date]
        cumulative += len(day_files)
        dir_counts = defaultdict(int)
        for f in day_files:
            dir_counts[f["directory"]] += 1
        new_refs = set()
        for f in day_files:
            new_refs.update(f["references"])
        timeline.append({
            "date": date,
            "files_added": len(day_files),
            "cumulative_files": cumulative,
            "directories": dict(dir_counts),
            "new_references": sorted(new_refs),
            "files": [f["filepath"] for f in day_files],
        })
    return timeline


def _tradition_of(filepath):
    """Return 'levin', 'friston', etc. for a tradition file; None otherwise."""
    parts = Path(filepath).parts
    if len(parts) >= 2 and parts[0] == "traditions":
        return parts[1]
    return None


def _bridge_class(source_fp, target_fp):
    """Classify the edge as 'cross' (endpoints in different top-level buckets)
    or 'same' (both in same bucket). Bucket = top-level directory category, with
    each tradition counting as its own bucket so e.g. levin → friston is cross.
    Used to drive the dash/solid line-style in the Sociogram."""
    s_cat = get_directory_category(source_fp)
    t_cat = get_directory_category(target_fp)
    return "same" if s_cat == t_cat else "cross"


def build_connections(files):
    name_to_path = {}
    for f in files:
        stem = Path(f["filename"]).stem
        if stem not in name_to_path:
            name_to_path[stem] = f["filepath"]
    wikilink_edges = []
    for f in files:
        for link in f["wikilinks"]:
            target = name_to_path.get(link)
            if target:
                wikilink_edges.append({
                    "source": f["filepath"], "target": target,
                    "type": "wikilink",
                    "bridge": _bridge_class(f["filepath"], target),
                })

    fp_set = {f["filepath"] for f in files}

    # PRS-DELTA (a) — sibling edges: traditions/<X>/prs_triplets.md ↔ traditions/<X>/wiki.md
    # Treat as wikilink type so they survive the 2500-edge cap. Brings the PRS
    # content layer into the Sociogram graph (it was previously degree 0–1 even
    # though it's the substantive triplet store).
    sibling_edges = []
    for f in files:
        trad = _tradition_of(f["filepath"])
        if trad and Path(f["filepath"]).name == "wiki.md":
            sibling = f"traditions/{trad}/prs_triplets.md"
            if sibling in fp_set:
                sibling_edges.append({
                    "source": f["filepath"], "target": sibling,
                    "type": "wikilink",
                    "subtype": "sibling",
                    "bridge": "same",
                })
    wikilink_edges.extend(sibling_edges)

    # Thinker-mention edges: bridge prose mentions of a surname back to the
    # tradition wiki page. Architecture/inbox/etc. → tradition is the dominant
    # path. Traditions are now ALSO allowed as sources, but only when targeting
    # a DIFFERENT tradition — that's the inter-tradition dialogue signal that
    # otherwise lived only as cross-arcs in the 3D PRS view.
    mention_edges = []
    for f in files:
        src_trad = _tradition_of(f["filepath"])
        for target in f.get("thinker_mentions", []):
            if target not in fp_set or target == f["filepath"]:
                continue
            tgt_trad = _tradition_of(target)
            # Skip same-tradition self-targeting (don't connect levin/wiki.md to
            # itself when it mentions "Levin"; don't connect levin/prs_triplets.md
            # to levin/wiki.md as a mention — sibling edge handles that).
            if src_trad and src_trad == tgt_trad:
                continue
            mention_edges.append({
                "source": f["filepath"], "target": target,
                "type": "thinker_mention",
                "bridge": _bridge_class(f["filepath"], target),
            })

    ref_to_files = defaultdict(list)
    for f in files:
        for ref in f["references"]:
            ref_to_files[ref].append(f["filepath"])
    reference_edges = []
    # Sliding window 25 (was 5) so tradition files (alphabetically late) actually
    # reach the architecture neighbors that share their IDs.
    for ref, ref_files in ref_to_files.items():
        if len(ref_files) > 1:
            for i in range(len(ref_files)):
                for j in range(i + 1, min(len(ref_files), i + 25)):
                    s, t = ref_files[i], ref_files[j]
                    reference_edges.append({
                        "source": s, "target": t,
                        "type": "shared_reference",
                        "reference": ref,
                        "bridge": _bridge_class(s, t),
                    })
    return {
        "wikilink_edges": wikilink_edges,
        "mention_edges": mention_edges,
        "reference_edges": reference_edges,
        "references_by_code": {k: v for k, v in sorted(ref_to_files.items())},
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_vault_data.py /path/to/vault", file=sys.stderr)
        sys.exit(1)

    vault_path = sys.argv[1]
    if not os.path.isdir(vault_path):
        print(f"Error: {vault_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    # Core scan
    files = scan_vault(vault_path)
    timeline = build_timeline(files)
    connections = build_connections(files)

    # SEMANTIC EXTRACTION — the deep stuff
    changelogs = parse_changelogs(vault_path)
    findings = parse_findings(vault_path)
    decisions = parse_decisions(vault_path)
    crosses = parse_cross_connections(vault_path)
    cowork_summaries = parse_cowork_summary(vault_path)

    # Metadata
    dates = [f["date"] for f in files]
    directories = sorted(set(f["directory"] for f in files))
    all_refs = set()
    for f in files:
        all_refs.update(f["references"])
    ref_type_counts = defaultdict(int)
    for ref in all_refs:
        ref_type_counts[ref.split('-')[0]] += 1

    output = {
        "metadata": {
            "extraction_date": datetime.now().isoformat(),
            "vault_path": vault_path,
            "total_files": len(files),
            "date_range": {
                "start": min(dates) if dates else None,
                "end": max(dates) if dates else None,
            },
            "directories": directories,
            "reference_type_counts": dict(ref_type_counts),
            "total_references": len(all_refs),
        },
        "files": files,
        "timeline": timeline,
        "connections": connections,
        # SEMANTIC CONTENT
        "changelogs": changelogs,
        "findings": findings,
        "decisions": decisions,
        "cross_connections": crosses,
        "cowork_summaries": cowork_summaries,
    }

    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
