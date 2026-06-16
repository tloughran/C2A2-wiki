#!/usr/bin/env python3
"""
extract_agent_node_refs.py — Agent sociogram edge extractor (OpenStory -> C2A2).

Emits the data layer for subtab-2 (the agent sociogram). Three edge layers,
ALL edges emitted with weights and NO cap — the paradigm sociogram's Pass-A
visibility budget (top-N by score, grows with zoom) decides what renders at any
one time, so the dataset is allowed to grow almost without limit.

Layers
  1. coref_substrate : agent  -> wiki-node   (undirected in spirit; agent anchored
                       to each canonical vault file it referenced; weight = #refs)
  2. coref_projected : agentA <-> agentB      (weight = # canonical nodes both touched)
  3. flow            : agentA  -> agentB      (directed; A Write/Edit'd a file that B
                       later Read; weight = # such ordered file-handoffs)

Node ids match the paradigm graph exactly:
  - wiki nodes : relative filepath WITH .md  (e.g. "traditions/levin/wiki.md")
  - agent nodes: "agents/<taskId>"           (group "agents", color already in COLORS)

Refs resolve to the FULL canonical id (never the bare basename) so per-tradition
files (traditions/*/wiki.md) don't collapse. Tool-call file_path is absolute and
unambiguous; [[wikilinks]] and prose .md tokens fall back to first-match stem.

Safe by construction: opens the DB read-only (mode=ro). Reads the vault read-only.
House rules: regular strings only; intersect refs with the on-disk canonical set.
"""

import argparse
import collections
import json
import math
import os
import re
import sqlite3
import sys
import urllib.parse

HOME = os.path.expanduser("~")
DEFAULT_DB = os.path.join(HOME, "Documents/Non-Claude Projects/OpenStory/data/open-story.db")
DEFAULT_VAULT = os.path.join(HOME, "Documents/Claude/Projects/RC Karpathy Wiki Project/wiki")
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MAP = os.path.join(HERE, "agent_map.json")
DEFAULT_OUT = os.path.join(HERE, "agent_node_edges.json")

# Stable across both the real mac path and the sandbox mount path.
VAULT_MARKER = "Karpathy Wiki Project/wiki/"

FILE_TOOLS_WRITE = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
FILE_TOOLS_READ = {"Read"}
REF_SUBTYPES = (
    "message.assistant.tool_use",
    "message.user.prompt",
    "message.assistant.text",
    "message.assistant.thinking",
)
MD_TOKEN = re.compile(r'([A-Za-z0-9 _./\-]+?\.md)')
WIKILINK = re.compile(r'\[\[([^\]|#]+)')

# Single human/interactive actor node. Genuine human-prompted sessions (those
# without a scheduled-task label) collapse here. Continuation sessions are
# un-attributable (could belong to any prior session) so they are counted but
# NOT folded into the human node — surfaced in _meta, never silently guessed.
HUMAN_ID = "H-Admin-Interactive"
HUMAN_LABEL = "H-Admin / Interactive"
CONTINUATION_MARKERS = (
    "Continue from where you left off",
    "This session is being continued",
)


def connect_ro(db_path):
    if not os.path.exists(db_path):
        sys.exit("ERROR: DB not found: %s" % db_path)
    uri = "file:%s?mode=ro" % urllib.parse.quote(db_path)
    return sqlite3.connect(uri, uri=True)


def label_fragment(label):
    """The (possibly 50-char-truncated) task name from a session label."""
    if not label:
        return None
    m = re.search(r'name="([^"]*)', label)
    return m.group(1).strip() if m else None


def build_resolver(roster_ids):
    """frag -> (taskId | None, reason). Truncation cuts the tail, so a canonical
    id that uniquely startswith the fragment is the match."""
    ids = list(roster_ids)

    def resolve(frag):
        if not frag:
            return None, "no_label"
        if frag in roster_ids:
            return frag, "exact"
        hits = [t for t in ids if t.startswith(frag)]
        if len(hits) == 1:
            return hits[0], "prefix"
        if not hits:
            return None, "unmatched"
        return None, "ambiguous"

    return resolve


def scan_vault(vault):
    """Return (canonical set of rel ids w/ .md, stem->rel first-match map)."""
    canon = set()
    stem_to_rel = {}
    for root, _dirs, files in os.walk(vault):
        if os.sep + "." in root:
            continue
        for fn in files:
            if not fn.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), vault)
            if rel.startswith("."):
                continue
            canon.add(rel)
            stem = fn[:-3]
            stem_to_rel.setdefault(stem, rel)
    return canon, stem_to_rel


def abs_to_rel(path):
    if VAULT_MARKER in path:
        return path.split(VAULT_MARKER, 1)[1]
    return None


def resolve_ref(token, canon, stem_to_rel):
    """Resolve a raw .md token (abs path, rel path, or bare name) to a canonical
    rel id, or None. Full-path forms win; bare names fall back to stem map."""
    token = token.strip().strip('"').strip("'")
    rel = abs_to_rel(token)
    if rel and rel in canon:
        return rel
    if token in canon:
        return token
    base = os.path.basename(token)
    stem = base[:-3] if base.endswith(".md") else base
    return stem_to_rel.get(stem)


def iter_refs_from_payload(subtype, payload_json, canon, stem_to_rel):
    """Yield (canonical_rel_id, op) where op in {'r','w',None}. op is set only for
    file-tool calls (drives the flow layer); None = a plain co-reference mention."""
    try:
        d = json.loads(payload_json)
    except Exception:
        return
    if subtype == "message.assistant.tool_use":
        content = (d.get("data", {}).get("raw", {})
                   .get("message", {}).get("content", []))
        for blk in content:
            if not isinstance(blk, dict) or blk.get("type") != "tool_use":
                continue
            name = blk.get("name", "")
            inp = blk.get("input", {}) or {}
            fp = inp.get("file_path") or inp.get("path") or ""
            if fp:
                rel = resolve_ref(fp, canon, stem_to_rel)
                if rel:
                    op = "w" if name in FILE_TOOLS_WRITE else ("r" if name in FILE_TOOLS_READ else None)
                    yield rel, op
            # Any other .md tokens in the tool args -> plain co-reference.
            for tok in MD_TOKEN.findall(json.dumps(inp)):
                rel = resolve_ref(tok, canon, stem_to_rel)
                if rel:
                    yield rel, None
    else:
        blob = json.dumps(d.get("data", {}))
        for tok in MD_TOKEN.findall(blob):
            rel = resolve_ref(tok, canon, stem_to_rel)
            if rel:
                yield rel, None
        for stem in WIKILINK.findall(blob):
            rel = stem_to_rel.get(stem.strip())
            if rel:
                yield rel, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--vault", default=DEFAULT_VAULT)
    ap.add_argument("--map", default=DEFAULT_MAP)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    agent_map = json.load(open(args.map, encoding="utf-8"))
    roster = {a["taskId"]: a for a in agent_map["agents"]}
    resolve = build_resolver(set(roster))

    canon, stem_to_rel = scan_vault(args.vault)
    sys.stderr.write("vault canonical nodes: %d\n" % len(canon))

    con = connect_ro(args.db)
    c = con.cursor()

    # 1) session_id -> canonical taskId
    sid_to_task = {}
    cap_reason = collections.Counter()
    human_sessions = 0
    unattributed_continuations = 0
    for sid, label in c.execute("SELECT id, label FROM sessions"):
        tid, reason = resolve(label_fragment(label))
        cap_reason[reason] += 1
        if tid:
            sid_to_task[sid] = tid
            continue
        # No scheduled-task label: human-interactive vs. un-attributable continuation.
        lab = (label or "").strip()
        if (not lab) or any(lab.startswith(m) for m in CONTINUATION_MARKERS):
            unattributed_continuations += 1
        else:
            sid_to_task[sid] = HUMAN_ID
            human_sessions += 1

    # 2) walk ref-bearing events for mapped sessions
    per_agent_nodes = collections.defaultdict(collections.Counter)  # taskId -> {rel: count}
    file_ops = collections.defaultdict(list)                        # rel -> [(ts, taskId, op)]
    agent_events = collections.Counter()
    agent_sessions = collections.defaultdict(set)
    scanned = 0

    placeholders = ",".join("?" * len(REF_SUBTYPES))
    q = ("SELECT session_id, subtype, timestamp, payload FROM events "
         "WHERE subtype IN (%s)" % placeholders)
    for sid, subtype, ts, payload in c.execute(q, REF_SUBTYPES):
        tid = sid_to_task.get(sid)
        if not tid:
            continue
        scanned += 1
        agent_events[tid] += 1
        agent_sessions[tid].add(sid)
        for rel, op in iter_refs_from_payload(subtype, payload, canon, stem_to_rel):
            per_agent_nodes[tid][rel] += 1
            if op in ("r", "w") and ts:
                file_ops[rel].append((ts, tid, op))
    con.close()

    # 3) agent nodes
    agent_nodes = []
    for tid in sorted(per_agent_nodes, key=lambda t: -agent_events[t]):
        a = roster.get(tid, {})
        is_human = (tid == HUMAN_ID)
        agent_nodes.append({
            "id": "agents/" + tid,
            "taskId": tid,
            "label": HUMAN_LABEL if is_human else tid,
            "group": "agents",
            "kind": "human" if is_human else "scheduled",
            "category": "human" if is_human else a.get("category", "unknown"),
            "sessions": len(agent_sessions[tid]),
            "events": agent_events[tid],
            "node_refs": len(per_agent_nodes[tid]),
        })

    # 4) coref_substrate: agent -> each canonical node it touched
    coref_substrate = []
    for tid, refs in per_agent_nodes.items():
        src = "agents/" + tid
        for rel, w in refs.items():
            coref_substrate.append({"source": src, "target": rel, "weight": w})

    # 5) coref_projected: agentA <-> agentB shared-node count (A<B)
    sets = {t: set(refs) for t, refs in per_agent_nodes.items()}
    tids = sorted(sets)
    coref_projected = []
    for i in range(len(tids)):
        for j in range(i + 1, len(tids)):
            shared = sets[tids[i]] & sets[tids[j]]
            if shared:
                coref_projected.append({
                    "source": "agents/" + tids[i],
                    "target": "agents/" + tids[j],
                    "weight": len(shared),
                })

    # 6) flow: A wrote file X, B read X later (directed A->B), weight = handoffs
    flow_w = collections.Counter()
    for rel, ops in file_ops.items():
        ops.sort()  # ISO-8601 'Z' strings sort chronologically
        writers_before = {}  # taskId -> earliest write ts seen so far
        for ts, tid, op in ops:
            if op == "w":
                writers_before.setdefault(tid, ts)
            elif op == "r":
                for wtid in writers_before:
                    if wtid != tid:
                        flow_w[(wtid, tid)] += 1
    flow = [{"source": "agents/" + a, "target": "agents/" + b, "weight": w}
            for (a, b), w in flow_w.items()]

    out = {
        "_meta": {
            "generated_from": "extract_agent_node_refs.py",
            "db_path": args.db,
            "vault": args.vault,
            "canonical_nodes": len(canon),
            "roster_size": len(roster),
            "roster_captured": len([t for t in per_agent_nodes if t != HUMAN_ID]),
            "human_node": HUMAN_ID in per_agent_nodes,
            "human_sessions": human_sessions,
            "unattributed_continuations": unattributed_continuations,
            "sessions_mapped": len(sid_to_task),
            "events_scanned": scanned,
            "session_resolution": dict(cap_reason),
            "layers": {
                "coref_substrate": len(coref_substrate),
                "coref_projected": len(coref_projected),
                "flow": len(flow),
            },
            "note": "ALL edges emitted; visibility budget handled by the paradigm renderer.",
        },
        "agent_nodes": agent_nodes,
        "coref_substrate": coref_substrate,
        "coref_projected": coref_projected,
        "flow": flow,
    }
    json.dump(out, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # ---- checkpoint report to stderr ----
    e = sys.stderr.write
    e("\n=== AGENT SOCIOGRAM EXTRACT ===\n")
    e("roster captured: %d/%d   sessions mapped: %d   events scanned: %d\n"
      % (len([t for t in per_agent_nodes if t != HUMAN_ID]), len(roster),
         len(sid_to_task), scanned))
    e("human node: %s  (human sessions=%d, unattributed continuations=%d)\n"
      % (HUMAN_ID in per_agent_nodes, human_sessions, unattributed_continuations))
    e("session resolution: %s\n" % dict(cap_reason))
    e("LAYER EDGE COUNTS:  substrate=%d  projected=%d  flow=%d\n"
      % (len(coref_substrate), len(coref_projected), len(flow)))
    deg = collections.Counter()
    for ed in coref_substrate:
        deg[ed["source"]] += 1
    e("substrate per-agent node-degree (top 10): %s\n"
      % deg.most_common(10))
    e("projected top pairs: %s\n"
      % sorted(coref_projected, key=lambda x: -x["weight"])[:8])
    e("flow top edges: %s\n"
      % sorted(flow, key=lambda x: -x["weight"])[:8])
    hid = "agents/" + HUMAN_ID
    h_flow = sorted([x for x in flow if hid in (x["source"], x["target"])],
                    key=lambda x: -x["weight"])[:6]
    h_proj = sorted([x for x in coref_projected if hid in (x["source"], x["target"])],
                    key=lambda x: -x["weight"])[:6]
    e("HUMAN flow edges (top): %s\n" % h_flow)
    e("HUMAN projected edges (top): %s\n" % h_proj)
    e("wrote: %s\n" % args.out)


if __name__ == "__main__":
    main()
