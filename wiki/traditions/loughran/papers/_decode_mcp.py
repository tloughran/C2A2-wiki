#!/usr/bin/env python3
"""Decode an MCP drive download JSON file (base64 content) into a binary file."""
import sys, json, base64, os

src = sys.argv[1]
dest = sys.argv[2]

with open(src) as f:
    obj = json.load(f)

# obj has {content, id, mimeType, title}
data = base64.b64decode(obj["content"])
with open(dest, "wb") as f:
    f.write(data)

print(f"Wrote {len(data)} bytes to {dest}")
print(f"mimeType: {obj.get('mimeType')}")
print(f"title: {obj.get('title')}")
print(f"magic: {data[:5]!r}")
