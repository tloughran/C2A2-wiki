# Bug report: Stale `.claude/worktrees/` directories accumulate inside user project tree, never cleaned up

## Summary

Claude (running in Cowork mode on macOS) has left **three full git worktrees totaling 69 MB / 1,053 files** buried inside my project at `wiki/architecture/daily_sync/chat_to_cowork/.claude/worktrees/`. They were created on 2026-04-26, are still being silently modified as recently as 2026-05-02 (Obsidian plugin JS files are touched across all three), and have never been cleaned up despite the originating sessions ending days ago. They aren't tracked by git, but they appear in every directory scan, file watcher, search tool, and content extractor that walks the project tree — including my own Sociogram visualization, where they inflated the node count from ~600 to 1,647.

## What I observed

```
$ ls wiki/architecture/daily_sync/chat_to_cowork/.claude/worktrees/
angry-blackwell-693ab4/
laughing-elgamal-cb3896/
romantic-chandrasekhar-4cc309/

$ du -sh wiki/architecture/daily_sync/chat_to_cowork/.claude/worktrees/*
23M     angry-blackwell-693ab4/
23M     laughing-elgamal-cb3896/
23M     romantic-chandrasekhar-4cc309/

$ find wiki/architecture/daily_sync/chat_to_cowork/.claude/worktrees -type f | wc -l
1053
```

Each worktree contains a full copy of my wiki structure — Obsidian vault state, traditions, architecture docs, agents, every PRS triplet, the lot. Examples:

```
romantic-chandrasekhar-4cc309/C2A2_wiki_agent_exec_summary.md
romantic-chandrasekhar-4cc309/wiki/tools/generate_review_page.py
romantic-chandrasekhar-4cc309/wiki/inbox/2026-04-08_levin_bialik-podcast-cancer-alien-intelligence.md
... (351 files per worktree, identical across all three)
```

Mtimes show ongoing background activity — `wiki/.obsidian/plugins/obsidian-local-rest-api/main.js` was last touched on 2026-05-02 inside every one of the worktrees, despite the worktrees themselves being orphaned from any active session. It looks like Obsidian's local REST API plugin keeps syncing files into the inactive worktrees, which compounds the problem.

## What I expected

One of the following:

1. The worktrees should be deleted automatically when the session that created them ends.
2. The worktrees should live in a system-managed location (e.g., `~/.claude-cache/worktrees/` or `/tmp/`) rather than inside my project directory.
3. At minimum, the `.claude/worktrees/` path should be added to a generated `.gitignore` and Claude should warn the user during interactive cleanup.

Per the documentation I've seen for the Agent tool with `isolation: "worktree"`, "the worktree is automatically cleaned up if the agent makes no changes; otherwise the path and branch are returned in the result." That cleanup is clearly not happening for the case where changes were made — and the user has no obvious way to discover, list, or clean them.

## Impact

- **Disk bloat.** 69 MB on a single project, growing with each session that uses worktrees.
- **Tooling pollution.** Any tool that walks the tree (file watchers, search, content extractors, IDE indexers, my own Sociogram extractor) sees the stale duplicates as live data. In my case, the Sociogram showed 1,647 nodes when only ~600 were real project content — over half the visible weight of the visualization was junk.
- **Privacy risk.** While the worktrees themselves aren't tracked by git, a user running `git add .` to stage a casual edit could accidentally commit ~23 MB of file copies. Worse, the worktrees contain duplicates of every file in the project, so if the project has been scrubbed for sensitive content, the worktrees retain pre-scrub copies.
- **Debugging confusion.** I couldn't account for the file count of my project until I dug into the directory structure. Most non-developer users would never look in a hidden `.claude/` directory and would simply notice their disk is mysteriously full and their tools mysteriously slow.

## Reproduction (approximate, since these were created days ago)

This appears to happen when Claude (Cowork mode) launches sub-agents using `isolation: "worktree"`. From what I can tell, my use of Cowork over the period 2026-04-26 onward triggered three such worktrees, none of which were cleaned up.

I cannot give exact reproduction steps because I don't recall which specific Cowork sessions created these — that's part of the problem. There's no surfaced inventory of worktrees and no UI affordance to clean them up.

## Environment

- macOS (Mac mini)
- Cowork mode (Claude desktop app's local agent mode)
- Obsidian also running on the same vault (the REST API plugin appears to be touching files across all three worktrees)
- Project: a private/public hybrid wiki repo (github.com/tloughran/C2A2-wiki) — public since 2026-05-04

## Suggested fixes (in priority order)

1. **Surface a worktree inventory.** Provide a way for the user to see all `.claude/worktrees/` directories Claude has created, when, and which session.
2. **Auto-clean on session end** for worktrees with no uncommitted changes. For worktrees with changes, prompt the user before retaining.
3. **Move the default worktree location out of the user's project tree** to a system-managed cache, with symlinks or refs back into the project as needed.
4. **Stop auxiliary processes (Obsidian sync, file watchers) from touching files inside orphaned worktrees**, or at minimum exclude `.claude/worktrees/` from those processes by default.
5. **Auto-add `.claude/worktrees/` to the project's `.gitignore`** when first created, so a casual `git add .` can't accidentally stage ~70 MB of duplicates.

## Severity

Medium — silent, accumulating, hard to discover, with privacy implications when the project history is being scrubbed.

---
*Filed: [date]*
*Reporter: Tom Loughran (thomas.loughran@gmail.com)*
