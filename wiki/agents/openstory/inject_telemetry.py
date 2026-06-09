#!/usr/bin/env python3
"""
inject_telemetry.py
-------------------
Inject agent_telemetry.json into agents_tab.html between the
/* TELEMETRY_DATA_START */ ... /* TELEMETRY_DATA_END */ markers.

C2A2 house rule: data is embedded at generation time (file:// can't fetch
a sibling JSON), not loaded at runtime. This is the surgical refresh step
for Phase B's scheduled re-extract: run the extractor, then this.

Usage:
  python3 inject_telemetry.py [--telemetry PATH] [--html PATH]
Defaults target the real-machine layout.
"""
import argparse
import json
import os
import re
import sys

HOME = os.path.expanduser("~")
VAULT = os.path.join(HOME, "Documents/Claude/Projects/RC Karpathy Wiki Project/wiki")
DEFAULT_TEL = os.path.join(VAULT, "agents/openstory/agent_telemetry.json")
DEFAULT_HTML = os.path.join(VAULT, "agents_tab.html")

START = "/* TELEMETRY_DATA_START */"
END = "/* TELEMETRY_DATA_END */"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--telemetry", default=DEFAULT_TEL)
    ap.add_argument("--html", default=DEFAULT_HTML)
    args = ap.parse_args()

    with open(args.telemetry) as f:
        data = json.load(f)          # validate JSON parses
    payload = json.dumps(data, separators=(",", ":"))

    with open(args.html) as f:
        html = f.read()

    if START not in html or END not in html:
        sys.exit("ERROR: markers not found in %s" % args.html)

    block = START + "\nconst TELEMETRY = " + payload + ";\n" + END
    # Non-greedy replace of everything between (and including) the markers.
    new_html = re.sub(re.escape(START) + r".*?" + re.escape(END), block,
                      html, count=1, flags=re.DOTALL)

    if new_html == html:
        print("No change (already current).")
    else:
        with open(args.html, "w") as f:
            f.write(new_html)
        print("Injected %d agents into %s" % (len(data.get("agents", {})), args.html))


if __name__ == "__main__":
    main()
