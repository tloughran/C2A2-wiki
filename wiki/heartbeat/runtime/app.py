#!/usr/bin/env python3
"""C2A2 Heartbeat Monitor

Reference implementation for a living agentic monitoring system:
- Polls configured sources on a heartbeat
- Summarizes new developments
- Applies risk and implication tags
- Serves a local dashboard and JSON API
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import secrets
import sqlite3
import threading
import time
from collections import Counter
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "data" / "heartbeat.db"
SOURCES_PATH = ROOT / "config" / "sources.json"
USER_AGENT = "C2A2Heartbeat/1.0 (+local reference implementation)"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def sentence_split(text: str) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def summarize(title: str, content: str, max_sentences: int = 2) -> str:
    content = strip_html(content)
    if not content:
        return title
    sents = sentence_split(content)
    if not sents:
        return content[:280]
    return " ".join(sents[:max_sentences])[:700]


RISK_RULES = {
    "capability_jump": [
        "agent", "autonomous", "frontier", "state-of-the-art", "sota", "general-purpose", "reasoning"
    ],
    "misuse_security": [
        "jailbreak", "exploit", "misuse", "phishing", "malware", "biosecurity", "cyber"
    ],
    "governance_policy": [
        "regulation", "policy", "compliance", "governance", "standard", "law", "audit"
    ],
    "market_platform": [
        "release", "launch", "integration", "partnership", "funding", "acquisition", "hiring"
    ],
}

C2A2_KEYWORDS = [
    "community", "education", "alignment", "governance", "trust", "formation", "agency", "misinformation"
]


def classify(text: str) -> Tuple[List[str], int]:
    t = text.lower()
    tags: List[str] = []
    for tag, kws in RISK_RULES.items():
        if any(kw in t for kw in kws):
            tags.append(tag)
    relevance = sum(1 for kw in C2A2_KEYWORDS if kw in t)
    return tags, relevance


def implications(tags: List[str], relevance: int) -> str:
    notes: List[str] = []
    if "capability_jump" in tags:
        notes.append("Reassess role boundaries and human override for community deployments.")
    if "misuse_security" in tags:
        notes.append("Prioritize provenance checks and misinformation/abuse response protocols.")
    if "governance_policy" in tags:
        notes.append("Update constitutional clauses and compliance mappings for community operators.")
    if "market_platform" in tags:
        notes.append("Monitor adoption pressure and revise formation cadence for tool onboarding.")
    if relevance >= 2:
        notes.append("High relevance to C2A2 operations; include in next leadership brief.")
    if not notes:
        notes.append("Track for context; no immediate governance action required.")
    return " ".join(notes)


def is_local_url(url: str) -> bool:
    if not url:
        return True
    try:
        parsed = urlparse(url)
    except Exception:  # noqa: BLE001
        return True
    if parsed.scheme in {"file", ""}:
        return True
    host = (parsed.hostname or "").lower()
    return host in {"localhost", "127.0.0.1", "::1"}


def is_citation_url(url: str) -> bool:
    if is_local_url(url):
        return False
    try:
        parsed = urlparse(url)
    except Exception:  # noqa: BLE001
        return False
    return parsed.scheme in {"http", "https"}


@dataclass
class Source:
    id: str
    name: str
    type: str
    url: str
    home_url: str = ""
    enabled: bool = True


class HeartbeatStore:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._lock = threading.Lock()
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS runs (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  started_at TEXT NOT NULL,
                  ended_at TEXT,
                  status TEXT NOT NULL,
                  message TEXT
                );

                CREATE TABLE IF NOT EXISTS events (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  source_id TEXT NOT NULL,
                  source_name TEXT NOT NULL,
                  item_id TEXT NOT NULL,
                  title TEXT NOT NULL,
                  url TEXT NOT NULL,
                  published_at TEXT,
                  summary TEXT,
                  tags_json TEXT NOT NULL,
                  relevance INTEGER NOT NULL DEFAULT 0,
                  implications TEXT,
                  first_seen_at TEXT NOT NULL,
                  UNIQUE(source_id, item_id)
                );

                CREATE TABLE IF NOT EXISTS run_sources (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  run_id INTEGER NOT NULL,
                  source_id TEXT NOT NULL,
                  source_name TEXT NOT NULL,
                  status TEXT NOT NULL,
                  checked INTEGER NOT NULL DEFAULT 0,
                  new_count INTEGER NOT NULL DEFAULT 0,
                  error TEXT,
                  recorded_at TEXT NOT NULL,
                  FOREIGN KEY(run_id) REFERENCES runs(id)
                );

                CREATE TABLE IF NOT EXISTS run_events (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  run_id INTEGER NOT NULL,
                  event_id INTEGER NOT NULL,
                  recorded_at TEXT NOT NULL,
                  FOREIGN KEY(run_id) REFERENCES runs(id),
                  FOREIGN KEY(event_id) REFERENCES events(id),
                  UNIQUE(run_id, event_id)
                );
                """
            )

    def start_run(self) -> int:
        with self._lock, self._connect() as conn:
            cur = conn.execute(
                "INSERT INTO runs(started_at, status) VALUES (?, ?)",
                (now_iso(), "running"),
            )
            return int(cur.lastrowid)

    def end_run(self, run_id: int, status: str, message: str = "") -> None:
        with self._lock, self._connect() as conn:
            conn.execute(
                "UPDATE runs SET ended_at=?, status=?, message=? WHERE id=?",
                (now_iso(), status, message, run_id),
            )

    def upsert_event(self, payload: Dict[str, object]) -> Optional[int]:
        with self._lock, self._connect() as conn:
            try:
                cur = conn.execute(
                    """
                    INSERT INTO events(
                      source_id, source_name, item_id, title, url, published_at,
                      summary, tags_json, relevance, implications, first_seen_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        payload["source_id"],
                        payload["source_name"],
                        payload["item_id"],
                        payload["title"],
                        payload["url"],
                        payload.get("published_at"),
                        payload.get("summary"),
                        json.dumps(payload.get("tags", [])),
                        int(payload.get("relevance", 0)),
                        payload.get("implications"),
                        now_iso(),
                    ),
                )
                return int(cur.lastrowid)
            except sqlite3.IntegrityError:
                return None

    def record_run_source(
        self,
        run_id: int,
        source_id: str,
        source_name: str,
        status: str,
        checked: int,
        new_count: int,
        error: str = "",
    ) -> None:
        with self._lock, self._connect() as conn:
            conn.execute(
                """
                INSERT INTO run_sources(
                  run_id, source_id, source_name, status, checked, new_count, error, recorded_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (run_id, source_id, source_name, status, checked, new_count, error, now_iso()),
            )

    def record_run_event(self, run_id: int, event_id: int) -> None:
        with self._lock, self._connect() as conn:
            conn.execute(
                """
                INSERT OR IGNORE INTO run_events(run_id, event_id, recorded_at)
                VALUES (?, ?, ?)
                """,
                (run_id, event_id, now_iso()),
            )

    def latest_run(self) -> Optional[Dict[str, object]]:
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM runs ORDER BY id DESC LIMIT 1").fetchone()
            return dict(row) if row else None

    def list_events(self, limit: int = 50) -> List[Dict[str, object]]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM events ORDER BY id DESC LIMIT ?", (limit,)
            ).fetchall()
            out = []
            for r in rows:
                d = dict(r)
                d["tags"] = json.loads(d.pop("tags_json", "[]"))
                out.append(d)
            return out

    def list_events_since(self, cutoff_dt: datetime, limit: int = 300) -> List[Dict[str, object]]:
        events = self.list_events(limit=limit)
        out: List[Dict[str, object]] = []
        for e in events:
            ts = e.get("first_seen_at")
            if not isinstance(ts, str):
                continue
            try:
                dt = datetime.fromisoformat(ts)
            except ValueError:
                continue
            if dt >= cutoff_dt:
                out.append(e)
        return out

    def digest(self, limit: int = 12) -> Dict[str, object]:
        events = self.list_events(limit=limit)
        lines = []
        for e in events:
            tags = ", ".join(e.get("tags", [])) or "none"
            lines.append(
                f"- {e['title']} ({e['source_name']})\\n"
                f"  Tags: {tags}; C2A2 relevance: {e['relevance']}\\n"
                f"  Implication: {e.get('implications', '')}"
            )
        return {
            "generated_at": now_iso(),
            "count": len(events),
            "items": events,
            "brief": "\n".join(lines),
        }

    def _summarize_window(self, events: List[Dict[str, object]]) -> str:
        if not events:
            return "No new events in this window."
        tag_counter = Counter()
        src_counter = Counter()
        for e in events:
            src_counter[e.get("source_name", "unknown")] += 1
            for t in e.get("tags", []):
                tag_counter[t] += 1
        top_tags = ", ".join([f"{k}({v})" for k, v in tag_counter.most_common(4)]) or "none"
        top_sources = ", ".join([f"{k}({v})" for k, v in src_counter.most_common(3)])
        high_rel = [e for e in events if int(e.get("relevance", 0)) >= 2]
        return (
            f"{len(events)} tracked updates. Top sources: {top_sources}. "
            f"Top risk themes: {top_tags}. "
            f"{len(high_rel)} items flagged high C2A2 relevance."
        )

    def latest_run_report(self) -> Dict[str, object]:
        run = self.latest_run()
        if not run:
            return {"window": "now", "summary": "No runs yet.", "sources": [], "top_stories": []}
        run_id = int(run["id"])
        with self._connect() as conn:
            src_rows = conn.execute(
                """
                SELECT source_id, source_name, status, checked, new_count, error
                FROM run_sources
                WHERE run_id=?
                ORDER BY source_name
                """,
                (run_id,),
            ).fetchall()
            story_rows = conn.execute(
                """
                SELECT e.*
                FROM run_events re
                JOIN events e ON e.id = re.event_id
                WHERE re.run_id=?
                ORDER BY e.relevance DESC, e.id DESC
                LIMIT 8
                """,
                (run_id,),
            ).fetchall()
        sources = [dict(r) for r in src_rows]
        stories = []
        for r in story_rows:
            d = dict(r)
            d["tags"] = json.loads(d.pop("tags_json", "[]"))
            stories.append(d)
        return {
            "window": "now",
            "run": run,
            "sources": sources,
            "top_stories": stories,
            "summary": self._summarize_window(stories),
        }

    def window_report(self, window: str) -> Dict[str, object]:
        if window == "now":
            return self.latest_run_report()
        hours_map = {"hourly": 1, "daily": 24, "weekly": 24 * 7}
        hours = hours_map.get(window, 24)
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        events = self.list_events_since(cutoff, limit=800)
        events_sorted = sorted(events, key=lambda e: int(e.get("relevance", 0)), reverse=True)
        top_stories = events_sorted[:10]

        # Source reach in window: reached if any non-error source poll occurred.
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT rs.source_id, rs.source_name, rs.status, rs.checked, rs.new_count, rs.error, r.started_at
                FROM run_sources rs
                JOIN runs r ON r.id = rs.run_id
                ORDER BY rs.id DESC
                """
            ).fetchall()
        source_latest: Dict[str, Dict[str, object]] = {}
        for r in rows:
            started = r["started_at"]
            try:
                started_dt = datetime.fromisoformat(started)
            except Exception:  # noqa: BLE001
                continue
            if started_dt < cutoff:
                continue
            sid = r["source_id"]
            if sid not in source_latest:
                source_latest[sid] = {
                    "source_id": sid,
                    "source_name": r["source_name"],
                    "status": r["status"],
                    "checked": r["checked"],
                    "new_count": r["new_count"],
                    "error": r["error"] or "",
                }
        return {
            "window": window,
            "cutoff": cutoff.isoformat(),
            "sources": list(source_latest.values()),
            "top_stories": top_stories,
            "summary": self._summarize_window(events),
            "count": len(events),
        }


class HeartbeatEngine:
    def __init__(self, store: HeartbeatStore, sources_path: Path):
        self.store = store
        self.sources_path = sources_path
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._interval_seconds = 60 * int(os.getenv("HEARTBEAT_MINUTES", "180"))

    def load_sources(self) -> List[Source]:
        raw = json.loads(self.sources_path.read_text())
        return [Source(**s) for s in raw if s.get("enabled", True)]

    def fetch_url(self, url: str) -> str:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        return data.decode("utf-8", errors="ignore")

    def parse_rss(self, src: Source) -> List[Dict[str, str]]:
        txt = self.fetch_url(src.url)
        root = ET.fromstring(txt)
        items = []
        for item in root.findall(".//item")[:25]:
            title = (item.findtext("title") or "Untitled").strip()
            link = (item.findtext("link") or "").strip()
            guid = (item.findtext("guid") or link or title).strip()
            description = (item.findtext("description") or "").strip()
            pub_date = (item.findtext("pubDate") or "").strip()
            if link:
                items.append(
                    {
                        "item_id": guid,
                        "title": title,
                        "url": link,
                        "content": description,
                        "published_at": pub_date,
                    }
                )
        return items

    def run_once(self) -> Dict[str, object]:
        run_id = self.store.start_run()
        added = 0
        checked = 0
        errors: List[str] = []
        source_reports: List[Dict[str, object]] = []
        try:
            for src in self.load_sources():
                src_checked = 0
                src_new = 0
                try:
                    if src.type != "rss":
                        source_reports.append(
                            {
                                "source_id": src.id,
                                "source_name": src.name,
                                "status": "skipped",
                                "checked": 0,
                                "new_count": 0,
                                "error": f"unsupported source type: {src.type}",
                            }
                        )
                        continue
                    items = self.parse_rss(src)
                    checked += len(items)
                    src_checked = len(items)
                    for it in items:
                        text_for_analysis = f"{it['title']} {it.get('content','')}"
                        tags, relevance = classify(text_for_analysis)
                        payload = {
                            "source_id": src.id,
                            "source_name": src.name,
                            "item_id": it["item_id"],
                            "title": it["title"],
                            "url": it["url"],
                            "published_at": it.get("published_at"),
                            "summary": summarize(it["title"], it.get("content", "")),
                            "tags": tags,
                            "relevance": relevance,
                            "implications": implications(tags, relevance),
                        }
                        event_id = self.store.upsert_event(payload)
                        if event_id is not None:
                            added += 1
                            src_new += 1
                            self.store.record_run_event(run_id, event_id)
                    source_reports.append(
                        {
                            "source_id": src.id,
                            "source_name": src.name,
                            "status": "ok",
                            "checked": src_checked,
                            "new_count": src_new,
                            "error": "",
                        }
                    )
                except (urllib.error.URLError, ET.ParseError, TimeoutError) as exc:
                    errors.append(f"{src.id}: {exc}")
                    source_reports.append(
                        {
                            "source_id": src.id,
                            "source_name": src.name,
                            "status": "error",
                            "checked": src_checked,
                            "new_count": src_new,
                            "error": str(exc),
                        }
                    )

            status = "ok" if not errors else "partial"
            msg = f"checked={checked}, new={added}" + (f"; errors={len(errors)}" if errors else "")
            for rep in source_reports:
                self.store.record_run_source(
                    run_id=run_id,
                    source_id=str(rep["source_id"]),
                    source_name=str(rep["source_name"]),
                    status=str(rep["status"]),
                    checked=int(rep["checked"]),
                    new_count=int(rep["new_count"]),
                    error=str(rep["error"]),
                )
            self.store.end_run(run_id, status, msg)
            return {
                "run_id": run_id,
                "status": status,
                "checked": checked,
                "new": added,
                "errors": errors,
                "sources": source_reports,
            }
        except Exception as exc:  # noqa: BLE001
            self.store.end_run(run_id, "error", str(exc))
            return {"run_id": run_id, "status": "error", "checked": checked, "new": added, "errors": [str(exc)]}

    def _loop(self) -> None:
        while self._running:
            self.run_once()
            for _ in range(int(self._interval_seconds)):
                if not self._running:
                    break
                time.sleep(1)

    def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=2)


class HeartbeatHandler(BaseHTTPRequestHandler):
    engine: HeartbeatEngine = None  # type: ignore[assignment]
    store: HeartbeatStore = None  # type: ignore[assignment]
    _rate_lock = threading.Lock()
    _rate_hits: Dict[Tuple[str, int], int] = {}
    _run_now_lock = threading.Lock()
    _run_now_active = False

    def _json(self, payload: Dict[str, object], status: int = 200) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _html(self, body: str, status: int = 200) -> None:
        out = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    def _extract_token(self, qs: Dict[str, List[str]]) -> str:
        qtok = (qs.get("token", [""])[0] or "").strip()
        if qtok:
            return qtok
        hdr = (self.headers.get("X-Heartbeat-Token", "") or "").strip()
        if hdr:
            return hdr
        auth = (self.headers.get("Authorization", "") or "").strip()
        if auth.lower().startswith("bearer "):
            return auth[7:].strip()
        return ""

    def _token_required(self) -> str:
        return (os.getenv("HEARTBEAT_ACCESS_TOKEN", "") or "").strip()

    def _is_authorized(self, qs: Dict[str, List[str]]) -> bool:
        required = self._token_required()
        if not required:
            return True
        provided = self._extract_token(qs)
        if not provided:
            return False
        return secrets.compare_digest(required, provided)

    def _rate_allowed(self) -> bool:
        per_min = int(os.getenv("HEARTBEAT_RATE_LIMIT_PER_MIN", "60"))
        if per_min <= 0:
            return True
        now_min = int(time.time() // 60)
        ip = self.client_address[0] if self.client_address else "unknown"
        key = (ip, now_min)
        with self._rate_lock:
            self._rate_hits = {k: v for k, v in self._rate_hits.items() if k[1] == now_min}
            n = int(self._rate_hits.get(key, 0))
            if n >= per_min:
                return False
            self._rate_hits[key] = n + 1
        return True

    def _source_url_map(self) -> Dict[str, Dict[str, str]]:
        out: Dict[str, Dict[str, str]] = {}
        try:
            for src in self.engine.load_sources():
                out[src.id] = {
                    "feed_url": src.url,
                    "home_url": src.home_url or src.url,
                }
        except Exception:  # noqa: BLE001
            return {}
        return out

    def _augment_report_for_citations(self, report: Dict[str, object]) -> Dict[str, object]:
        source_urls = self._source_url_map()
        citation_sources: List[Dict[str, str]] = []
        citation_story_links: List[Dict[str, str]] = []

        for s in report.get("sources", []):
            sid = str(s.get("source_id", ""))
            surls = source_urls.get(sid, {})
            home_url = str(surls.get("home_url", ""))
            feed_url = str(surls.get("feed_url", ""))
            s["source_url"] = home_url
            s["feed_url"] = feed_url
            s["citation_eligible"] = is_citation_url(home_url)
            if s["citation_eligible"]:
                citation_sources.append(
                    {
                        "source_id": sid,
                        "source_name": str(s.get("source_name", "")),
                        "source_url": home_url,
                    }
                )

        for e in report.get("top_stories", []):
            sid = str(e.get("source_id", ""))
            surls = source_urls.get(sid, {})
            home_url = str(surls.get("home_url", ""))
            e["source_url"] = home_url
            e["citation_eligible"] = is_citation_url(str(e.get("url", ""))) and is_citation_url(home_url)
            if e["citation_eligible"]:
                citation_story_links.append(
                    {
                        "title": str(e.get("title", "")),
                        "url": str(e.get("url", "")),
                        "source_name": str(e.get("source_name", "")),
                    }
                )

        report["citation_sources"] = citation_sources
        report["citation_story_links"] = citation_story_links
        return report

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        if not self._rate_allowed():
            self._json({"error": "rate limit exceeded"}, status=429)
            return
        if not self._is_authorized(qs):
            self._json({"error": "unauthorized"}, status=401)
            return

        if path == "/health":
            latest = self.store.latest_run()
            self._json({"ok": True, "latest_run": latest})
            return

        if path == "/api/events":
            limit = int(qs.get("limit", ["50"])[0])
            self._json({"events": self.store.list_events(limit=limit)})
            return

        if path == "/api/digest":
            window = (qs.get("window", ["now"])[0] or "now").strip().lower()
            if window not in {"now", "hourly", "daily", "weekly"}:
                self._json({"error": "invalid window", "allowed": ["now", "hourly", "daily", "weekly"]}, status=400)
                return
            self._json(self._augment_report_for_citations(self.store.window_report(window)))
            return

        if path == "/run-now":
            if os.getenv("HEARTBEAT_ENABLE_RUN_NOW", "0").strip() != "1":
                self._json({"error": "run-now disabled"}, status=403)
                return
            with self._run_now_lock:
                if self._run_now_active:
                    self._json({"error": "run already in progress"}, status=409)
                    return
                self._run_now_active = True
            try:
                result = self.engine.run_once()
            finally:
                with self._run_now_lock:
                    self._run_now_active = False
            self._json(result)
            return

        if path in ("/", "/dashboard"):
            latest = self.store.latest_run()
            window = (qs.get("window", ["now"])[0] or "now").strip().lower()
            if window not in {"now", "hourly", "daily", "weekly"}:
                window = "now"
            report = self._augment_report_for_citations(self.store.window_report(window))
            token = self._extract_token(qs)
            token_q = f"&token={html.escape(token)}" if token else ""

            source_rows = []
            for s in report.get("sources", []):
                status = str(s.get("status", "unknown"))
                source_name = html.escape(str(s.get("source_name", "")))
                source_url = str(s.get("source_url", ""))
                if not is_citation_url(source_url):
                    continue
                source_cell = (
                    f"<a href=\"{html.escape(source_url)}\" target=\"_blank\">{source_name}</a>"
                )
                source_rows.append(
                    "<tr>"
                    f"<td>{source_cell}</td>"
                    f"<td>{html.escape(status)}</td>"
                    f"<td>{int(s.get('checked', 0))}</td>"
                    f"<td>{int(s.get('new_count', 0))}</td>"
                    f"<td>{html.escape(str(s.get('error', '')))}</td>"
                    "</tr>"
                )

            story_rows = []
            for e in report.get("top_stories", []):
                if not bool(e.get("citation_eligible", False)):
                    continue
                tags = ", ".join(e.get("tags", [])) or "none"
                source_name = html.escape(str(e.get("source_name", "")))
                source_url = str(e.get("source_url", ""))
                source_cell = source_name
                if is_citation_url(source_url):
                    source_cell = f"<a href=\"{html.escape(source_url)}\" target=\"_blank\">{source_name}</a>"
                story_rows.append(
                    "<tr>"
                    f"<td>{html.escape(str(e.get('first_seen_at', '')))}</td>"
                    f"<td>{source_cell}</td>"
                    f"<td><a href=\"{html.escape(str(e.get('url', '')))}\" target=\"_blank\">{html.escape(str(e.get('title', '')))}</a></td>"
                    f"<td>{html.escape(tags)}</td>"
                    f"<td>{int(e.get('relevance', 0))}</td>"
                    f"<td>{html.escape(str(e.get('implications', '')))}</td>"
                    "</tr>"
                )

            links = []
            for w in ["now", "hourly", "daily", "weekly"]:
                cls = "tab active" if w == window else "tab"
                label = w.capitalize()
                links.append(f"<a class=\"{cls}\" href=\"/dashboard?window={w}{token_q}\">{label}</a>")
            latest_msg = "No runs yet" if not latest else f"Run #{latest['id']} | {latest['status']} | {latest.get('message','')}"
            body = f"""
<!doctype html>
<html>
<head>
  <meta charset=\"utf-8\" />
  <title>C2A2 Heartbeat Monitor</title>
  <meta http-equiv=\"refresh\" content=\"60\" />
  <style>
    body {{ font-family: -apple-system, sans-serif; margin: 24px; }}
    .meta {{ margin-bottom: 12px; }}
    .btn {{ display:inline-block; padding:8px 12px; background:#0b57d0; color:#fff; text-decoration:none; border-radius:6px; margin-right:8px; }}
    .tabs {{ margin: 16px 0; }}
    .tab {{ display:inline-block; padding:6px 10px; border:1px solid #bbb; border-radius:999px; text-decoration:none; color:#222; margin-right:6px; }}
    .tab.active {{ background:#222; color:#fff; border-color:#222; }}
    .summary {{ background:#f7f8fa; border:1px solid #ddd; border-radius:8px; padding:10px 12px; margin: 10px 0 16px; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 12px; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; vertical-align: top; }}
    th {{ background: #f5f5f5; text-align: left; }}
    h2 {{ margin-top: 24px; }}
  </style>
</head>
<body>
  <h1>C2A2 Heartbeat Monitor (Reference)</h1>
  <div class=\"meta\">{html.escape(latest_msg)}</div>
  <a class=\"btn\" href=\"/run-now?token={html.escape(token)}\">Run heartbeat now</a>
  <a class=\"btn\" href=\"/api/digest?window={window}{token_q}\">View report JSON</a>
  <a class=\"btn\" href=\"/health?token={html.escape(token)}\">Health</a>
  <div class=\"tabs\">{''.join(links)}</div>
  <div class=\"summary\"><strong>Window:</strong> {html.escape(window)} | <strong>Summary:</strong> {html.escape(str(report.get('summary', '')))}</div>
  <p>Heartbeat polls configured sources, verifies reach status, and reports top stories plus C2A2-relevant implications by time window.</p>
  <h2>Source Reach</h2>
  <table>
    <thead>
      <tr><th>Source</th><th>Status</th><th>Checked</th><th>New</th><th>Error</th></tr>
    </thead>
    <tbody>
      {''.join(source_rows) if source_rows else '<tr><td colspan="5">No source checks in this window.</td></tr>'}
    </tbody>
  </table>
  <h2>Top Stories</h2>
  <table>
    <thead>
      <tr><th>First Seen (UTC)</th><th>Source</th><th>Title</th><th>Tags</th><th>Relevance</th><th>C2A2 Implication</th></tr>
    </thead>
    <tbody>
      {''.join(story_rows) if story_rows else '<tr><td colspan="6">No stories in this window.</td></tr>'}
    </tbody>
  </table>
</body>
</html>
"""
            self._html(body)
            return

        self._json({"error": "Not found"}, status=404)


class LocalThreadingHTTPServer(ThreadingHTTPServer):
    """ThreadingHTTPServer without reverse-DNS lookup during local bind."""

    def server_bind(self) -> None:
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()
        host, port = self.server_address[:2]
        self.server_name = str(host)
        self.server_port = int(port)


def run_server(host: str, port: int, bootstrap: bool = True) -> None:
    store = HeartbeatStore(DB_PATH)
    engine = HeartbeatEngine(store, SOURCES_PATH)
    HeartbeatHandler.engine = engine
    HeartbeatHandler.store = store

    if bootstrap:
        engine.run_once()
    engine.start()

    server = LocalThreadingHTTPServer((host, port), HeartbeatHandler)
    print(f"C2A2 heartbeat server running at http://{host}:{port}")
    print("Endpoints: /dashboard, /run-now, /api/events, /api/digest, /health")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        engine.stop()
        server.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the C2A2 heartbeat monitor service")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8787)
    parser.add_argument("--no-bootstrap", action="store_true", help="do not run initial heartbeat cycle on startup")
    args = parser.parse_args()
    run_server(args.host, args.port, bootstrap=not args.no_bootstrap)


if __name__ == "__main__":
    main()
