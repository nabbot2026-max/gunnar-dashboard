# OpenClaw Ops Kanban — Skynet Self-Development

## 🧊 Backlog
- [ ] **Pyenv + pipx realignment** — Install Python 3.12.x via pyenv and point pipx at it for future automation scripts. *(Ref: INFRA.md “Next actions”)*
- [ ] **Disk-usage watchdog** — launchd/cron job that pings WhatsApp if root volume >85%.
- [ ] **Full config snapshot & migration doc** — capture gateway config, API keys, and Tailscale notes for fast hardware swap.
- [ ] **Grant tracker throttle fix** — adjust Grants.gov spacing (≤5 req/min) + optional API key to stop 429 alerts.
- [ ] **Mission-control.json feed** — expose structured JSON for the dashboard so cards auto-refresh.

## ⚙️ In Progress
- [ ] **Homebrew baseline audit** — verify GNU coreutils/findutils/sed + wget installs, document versions, and script `brew bundle dump` for reproducibility.
- [ ] **Automation cron review** — confirm daily (RFP) and weekly (CCUS) jobs are present in OpenClaw cron, add health pings when a run misses twice.
- [ ] **RESTORE.md expansion** — extend workspace restore guide with GitHub/Drive steps + Tailscale/SSH checklist.

## ✅ Done / Live
- [x] **Node 22 + pnpm toolchain** — installed via Homebrew; ensures local script compatibility.
- [x] **Launchd gateway management** — `ai.openclaw.gateway` service running with `bind=loopback` + token auth.
- [x] **Haiku heartbeat + Brave search** — hourly heartbeat on Claude 3.5 Haiku and Brave/web_fetch wired for browsing.
- [x] **Automation runbook surfacing** — Ops Runbook in Mission Control reflects actual commands/log paths.
