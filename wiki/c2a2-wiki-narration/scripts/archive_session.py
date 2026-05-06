#!/usr/bin/env python3
"""
archive_session.py — Convert a Cowork session JSONL transcript into a clean
markdown archive that survives across sessions.

Usage:
    python3 archive_session.py [--latest | --jsonl PATH | --session UUID] [--out DIR]

Defaults:
    --latest                 Find the most recently modified Cowork session JSONL.
    --out wiki/session-archive    relative to the project root.

Produces:
    wiki/session-archive/YYYY-MM-DD-<slug>.md   Clean transcript
    wiki/session-archive/SESSIONS.md            Index, newest first

Drops:
    System reminders, tool calls, tool results, queue ops, raw JSON noise.

Keeps:
    User prose, Claude prose, timestamps.

Run after closing a session (or on a daily cron) so the conversation
is recoverable as plain markdown the next time you open Cowork.
"""
import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Where Cowork stashes session JSONL transcripts.
# First entry is the macOS host path; second is the Cowork Linux sandbox bind-mount.
HOSTLOOP_GLOBS = [
    "/var/folders/*/*/T/claude-hostloop-plugins/*/projects/*/*.jsonl",
    "/sessions/*/mnt/.claude/projects/*/*.jsonl",
]


def _all_jsonl_paths():
    seen = []
    for pattern in HOSTLOOP_GLOBS:
        seen.extend(glob.glob(pattern))
    return seen

SYSTEM_REMINDER_RE = re.compile(r"<system-reminder>.*?</system-reminder>", re.DOTALL)
UPLOADED_FILES_RE = re.compile(r"<uploaded_files>.*?</uploaded_files>", re.DOTALL)
COMMAND_TAGS_RE = re.compile(
    r"<(command-name|command-message|command-args|local-command-stdout|local-command-stderr)>"
    r".*?</\1>",
    re.DOTALL,
)


def find_latest_jsonl():
    paths = _all_jsonl_paths()
    if not paths:
        return None
    return max(paths, key=lambda p: os.path.getmtime(p))


def find_jsonl_for_session(session_uuid):
    for p in _all_jsonl_paths():
        if session_uuid in p or Path(p).stem == session_uuid:
            return p
    return None


def clean_user_text(text):
    if not text:
        return ""
    text = SYSTEM_REMINDER_RE.sub("", text)
    text = UPLOADED_FILES_RE.sub("", text)
    text = COMMAND_TAGS_RE.sub("", text)
    return text.strip()


def extract_text_blocks(content):
    """Walk a content list (assistant or tool-bearing user) and keep only text."""
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    chunks = []
    for block in content:
        if not isinstance(block, dict):
            continue
        if block.get("type") == "text":
            chunks.append(block.get("text", ""))
    return "\n".join(chunks)


def parse_jsonl(path):
    """Yield (role, timestamp, text) for each meaningful conversational turn."""
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            if obj.get("type") not in ("user", "assistant"):
                continue

            msg = obj.get("message", {}) or {}
            role = msg.get("role")
            ts = obj.get("timestamp", "")
            content = msg.get("content")

            # Tool-result-only user messages: skip wholesale
            if role == "user" and isinstance(content, list):
                if all(
                    isinstance(b, dict) and b.get("type") == "tool_result"
                    for b in content
                ):
                    continue
                text = clean_user_text(extract_text_blocks(content))
            elif role == "user":
                text = clean_user_text(content)
            elif role == "assistant":
                text = extract_text_blocks(content).strip()
            else:
                continue

            if not text:
                continue
            yield role, ts, text


def slugify(text, max_len=50):
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text or "")
    text = re.sub(r"\s+", "-", text.strip()).lower()
    return text[:max_len].strip("-") or "untitled"


def first_user_topic(turns):
    for role, _, text in turns:
        if role == "user":
            first_line = next((ln for ln in text.split("\n") if ln.strip()), "")
            return first_line[:80] or "untitled"
    return "untitled"


def render_markdown(turns, session_id, jsonl_path, topic):
    if turns and turns[0][1]:
        first_ts = turns[0][1][:10]
    else:
        first_ts = datetime.now().strftime("%Y-%m-%d")
    out = []
    out.append(f"# Session — {first_ts} — {topic}")
    out.append("")
    out.append(f"_Session id: `{session_id}`_  ")
    out.append(f"_Source: `{jsonl_path}`_  ")
    out.append(f"_Turns: {len(turns)}_")
    out.append("")
    out.append("---")
    out.append("")
    for role, ts, text in turns:
        ts_short = ts[:19].replace("T", " ") if ts else ""
        speaker = "Tom" if role == "user" else "Claude"
        out.append(f"## {speaker} — {ts_short}")
        out.append("")
        out.append(text)
        out.append("")
    return "\n".join(out)


def append_index(index_path, fname, first_ts, topic, turn_count):
    line = f"- `{first_ts}` [{topic}](./{fname}) — {turn_count} turns"
    if not index_path.exists():
        header = "# Session Archive Index\n\nMost recent first.\n\n"
        index_path.write_text(header + line + "\n")
        return
    txt = index_path.read_text()
    # Insert the new line right after the "Most recent first." header.
    marker = "Most recent first.\n\n"
    if marker in txt:
        head, tail = txt.split(marker, 1)
        index_path.write_text(head + marker + line + "\n" + tail)
    else:
        index_path.write_text(txt.rstrip() + "\n" + line + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = parser.add_mutually_exclusive_group()
    src.add_argument("--latest", action="store_true", help="archive the most recently modified session (default)")
    src.add_argument("--jsonl", help="path to a specific JSONL transcript")
    src.add_argument("--session", help="session UUID to archive")
    parser.add_argument("--out", default="wiki/session-archive", help="output directory (relative to --project-root)")
    parser.add_argument("--project-root", default=".", help="project root (default: cwd)")
    args = parser.parse_args()

    if args.jsonl:
        jsonl = args.jsonl
    elif args.session:
        jsonl = find_jsonl_for_session(args.session)
    else:
        jsonl = find_latest_jsonl()

    if not jsonl or not Path(jsonl).exists():
        print("Could not locate a session JSONL transcript.", file=sys.stderr)
        for p in HOSTLOOP_GLOBS:
            print(f"  Looked in: {p}", file=sys.stderr)
        sys.exit(1)

    print(f"Reading: {jsonl}")
    session_id = Path(jsonl).stem
    turns = list(parse_jsonl(jsonl))
    print(f"  {len(turns)} conversational turns extracted")

    if not turns:
        print("Nothing to archive (transcript has no conversational content).", file=sys.stderr)
        sys.exit(2)

    out_dir = Path(args.project_root) / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    first_ts = (turns[0][1][:10] if turns[0][1] else datetime.now().strftime("%Y-%m-%d"))
    topic = first_user_topic(turns)
    slug = slugify(topic)
    fname = f"{first_ts}-{slug}.md"
    out_path = out_dir / fname

    md = render_markdown(turns, session_id, jsonl, topic)
    out_path.write_text(md)
    print(f"Wrote: {out_path}  ({len(md):,} bytes)")

    index_path = out_dir / "SESSIONS.md"
    append_index(index_path, fname, first_ts, topic, len(turns))
    print(f"Updated index: {index_path}")
    print("Done.")


if __name__ == "__main__":
    main()
