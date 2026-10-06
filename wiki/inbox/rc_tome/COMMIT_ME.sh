# Run on the Mac, in Terminal. Reviewed and signed off 2026-09-04.
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
rm -f .git/index.lock .git/index.lock.*            # stale locks left by the sandbox (cannot unlink there)
rm -rf wiki/inbox/rc_tome/_to_delete               # junk: an HEAD copy of the explorer + a duplicate proposal
git add wiki/rc_document_explorer.html wiki/inbox/rc_tome handoffs/explorer-roadmap.md SPEC_tome_extraction.md
git commit -m "Pilot Tome ToC v2: 7 parts / 40 chapters / 20 sections over verified unit extraction (A1)

Sweep found the explorer ToC reproduced ChatGPT export levels: 102 H1s, 87 of them
status lines; Hoffman/Wolfram/Hawkins/Carroll/Hossenfelder bios unheaded under Levin;
Kastrup/Deacon/Paper 2/Stump under one 27k-word H1. Seams are Tom's prompts, quoted per node.
Authored five-phase outline (p396-399) adopted as the Part layer. 65 wrapped headings
reconstituted; 79 apparatus headings collapsed per chapter; 26 ids added; body byte-identical.
All 613 old ToC hrefs still resolve. A1: 1,106 units, V1-V8 pass incl. falsifier.
Generators and CSVs in wiki/inbox/rc_tome/. Skill corpus-toc extracted.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_018ZMsKeNDkgEUnRJXSFMzxP"
git push
