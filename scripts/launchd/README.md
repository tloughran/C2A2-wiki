# launchd agents

Canonical copies of the launchd property lists that drive this system's local
automation. The plists here are the source of truth; `~/Library/LaunchAgents/`
holds installed copies.

Every `ProgramArguments` path points at this repo's `scripts/` directory in the
**primary** working tree:

    /Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/scripts

That tree stays on `main` permanently, which is what makes the path safe to hard-code.
Do not repoint an agent at a feature worktree — those are transient, and a job that
outlives one starts failing silently.

One exception: `com.tomloughran.openstory.nats` runs the Homebrew `nats-server`
binary directly, with the OpenStory checkout as its working directory. It exists so
the message bus outlives a backend restart — it used to be a `disown`ed child of
`openstory-backend.sh`, which meant launchd stopping the backend killed NATS and the
respawn then raced a cold bus.

## Agents

| Plist | Runs | Cadence |
|---|---|---|
| `com.tomloughran.openstory.nats` | `nats-server -c deploy/nats-local.conf` | RunAtLoad + KeepAlive |
| `com.tomloughran.openstory.backend` | `openstory-backend.sh` | RunAtLoad + KeepAlive |
| `com.tomloughran.openstory.watchdog` | `openstory-watchdog.sh` | every 300s |
| `com.tomloughran.openstory.bridge` | `openstory-bridge.sh` | every 600s |
| `com.tomloughran.openstory.ui` | `openstory-ui.sh` | RunAtLoad + KeepAlive (optional) |
| `com.tomloughran.openstory-version-check` | `openstory-version-check.sh` | Mon 05:35 |
| `com.c2a2.metabolism-publish` | `../publish_metabolism.sh` | weekly |
| `com.tloughran.summa-vault-sync` | `sync_vault.sh` | daily 21:00 |
| `com.tloughran.summa-weekly-review` | weekly review | weekly |
| `com.c2a2.scheduled-commit-check` | `check_scheduled_commits.sh` (runs the commit check **and** the stall check) | daily 05:45 |
| `com.c2a2.unattended-permissions` | `ensure_unattended_permissions.sh` — re-applies `permissionMode` to the daily run, which the Claude desktop app strips whenever it rewrites its registry from memory | RunAtLoad + every 600s |

## Two rules that are not optional

Both of these produced jobs that were dead for weeks while every place a human
would look said nothing at all.

**1. Never point `ProgramArguments` at `/usr/bin/python3`. Use `/bin/bash` + a
`.sh` wrapper that calls python3.** macOS TCC gates `~/Documents` read access
per-executable. `/bin/bash` holds the grant; the CommandLineTools python3 shim
does not, so under launchd it cannot open a script that lives in this repo:

    can't open file '.../scripts/foo.py': [Errno 1] Operation not permitted

Running the same `.py` from a Terminal shell does **not** reproduce this — the
shell carries its own grant. The only honest test is `launchctl kickstart`.
Killed `com.c2a2.scheduled-commit-check` (2 days) and
`com.tloughran.summa-weekly-review` (2+ weeks).

**2. `StandardOutPath`/`StandardErrorPath` must live in `~/Library/Logs/`, never
inside `~/Documents/`.** Any file under `~/Documents` that a sandboxed process
touches gets a `com.apple.macl` extended attribute stamped on it. launchd then
cannot open that file, and the job fails with **`last exit code = 78: EX_CONFIG`
before the program ever starts** — so the log stays empty and there is no error
message anywhere. Check with `xattr <logfile>`.

Stripping the attribute is not a fix: the scheduled tasks mount `~/Documents`,
so the next sandboxed read re-stamps it. Only the location fixes it — which is
why `~/Library/Logs` works. This is what killed `com.tloughran.summa-vault-sync`
(11 days, no vault published), `com.tloughran.summa-weekly-review` and
`com.c2a2.metabolism-publish`.

A job whose log path is fine but whose exit code is 78 is telling you about
`macl`, not about your script.

## Install or reinstall one

    L=com.tomloughran.openstory.watchdog
    cp "scripts/launchd/$L.plist" "$HOME/Library/LaunchAgents/$L.plist"
    launchctl bootout "gui/$(id -u)/$L" 2>/dev/null
    launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/$L.plist"
    launchctl print "gui/$(id -u)/$L" | head -20

## After editing any plist here

`plutil -lint` it before installing. A malformed plist fails to bootstrap and the
job just never runs, with no error anywhere you would normally look.

    plutil -lint scripts/launchd/*.plist

## History

Added 2026-07-20. Before that, five of these scripts were unversioned: three loose in
`~/Documents/`, one in `~/.local/bin/`, and `openstory-bridge.sh` inside the upstream
OpenStory checkout, where it was untracked and exposed to upstream pulls even though
its plist comment claimed it was version-controlled. Logs are deliberately left in
`~/Library/Logs/` and are not part of this repo.
