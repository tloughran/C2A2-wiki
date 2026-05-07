#!/usr/bin/env python3
"""
serve_wiki.py — HTTP server for the C2A2 wiki with /api/approve endpoint.

Replaces `python3 -m http.server 8080` in launch_summa.command.
Serves files from the wiki/ directory AND handles the weekly review approval POST.

Usage:
    python3 serve_wiki.py [--port 8080] [--vault PATH]

The /api/approve endpoint accepts:
    POST /api/approve
    Content-Type: application/json
    {"week": "2026-W20", "days": [46,47,...], "reviewer": "Tom Loughran",
     "timestamp": "2026-05-10T20:15:00", "qc_status": "pass"}

Appends an approval row to <vault>/_index/QC log.md.
"""

import argparse
import datetime
import http.server
import json
import os
import socketserver
import sys


DEFAULT_PORT  = 8080
DEFAULT_VAULT = os.path.expanduser(
    "~/Documents/Claude/Projects/Summa 2026 in a Year/vault")
DEFAULT_WIKI  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root / wiki/../


def write_approval(vault_dir, payload):
    """Append an approval row to _index/QC log.md."""
    qc_log = os.path.join(vault_dir, "_index", "QC log.md")
    week    = payload.get("week", "?")
    days    = payload.get("days", [])
    reviewer = payload.get("reviewer", "Tom Loughran")
    ts      = payload.get("timestamp", datetime.datetime.now().isoformat()[:19])
    status  = payload.get("qc_status", "pass")

    day_str = f"Days {days[0]}–{days[-1]}" if days else "?"
    note    = f"Weekly review approved by {reviewer}: {day_str}, QC {status}"
    row     = f"| {ts} | week | {week} | {week} | {note} |\n"

    with open(qc_log, "a", encoding="utf-8") as f:
        f.write(row)


class WikiHandler(http.server.SimpleHTTPRequestHandler):

    vault_dir = DEFAULT_VAULT

    def do_POST(self):
        if self.path == "/api/approve":
            try:
                length  = int(self.headers.get("Content-Length", 0))
                body    = self.rfile.read(length)
                payload = json.loads(body)
                write_approval(self.vault_dir, payload)
                self._json_response(200, {"ok": True, "recorded": payload.get("week")})
            except Exception as e:
                self._json_response(500, {"ok": False, "error": str(e)})
        else:
            self._json_response(404, {"ok": False, "error": "not found"})

    def _json_response(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Suppress routine GET noise; keep errors
        if args and str(args[1]) not in ("200", "304"):
            super().log_message(fmt, *args)


def main():
    parser = argparse.ArgumentParser(description="C2A2 wiki HTTP server")
    parser.add_argument("--port",  type=int, default=DEFAULT_PORT)
    parser.add_argument("--vault", default=DEFAULT_VAULT,
                        help="Path to Summa 2026 vault (for QC log writes)")
    parser.add_argument("--wiki",  default=None,
                        help="Directory to serve (default: wiki/ alongside this script)")
    args = parser.parse_args()

    vault_dir = os.path.expanduser(args.vault)
    wiki_dir  = os.path.expanduser(args.wiki) if args.wiki else \
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "wiki")

    if not os.path.isdir(wiki_dir):
        print(f"ERROR: wiki directory not found: {wiki_dir}", file=sys.stderr)
        sys.exit(1)
    if not os.path.isdir(vault_dir):
        print(f"WARNING: vault not found at {vault_dir} — approvals will fail", file=sys.stderr)

    WikiHandler.vault_dir = vault_dir
    os.chdir(wiki_dir)

    with socketserver.TCPServer(("", args.port), WikiHandler) as httpd:
        print(f"C2A2 wiki server running at http://localhost:{args.port}/explorer.html")
        print(f"Serving:  {wiki_dir}")
        print(f"Vault:    {vault_dir}")
        print(f"Press Ctrl-C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
