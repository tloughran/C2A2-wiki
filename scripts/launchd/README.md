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
