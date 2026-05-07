#!/bin/bash
REPO="$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project"
python3 "$REPO/scripts/serve_wiki.py" &
sleep 1
open "http://localhost:8080/explorer.html"
