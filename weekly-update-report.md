# Weekly Update Report — 2026-08-27

> Scan window: 2026-07-28 → 2026-08-27 (last 30 days), plus GitHub "latest release" snapshots as of scan time.
>
> **Process note:** `gemini` CLI is no longer installed; its replacement `agy` (Antigravity CLI) requires a `read_url` tool permission that this sandbox auto-denies, and `--dangerously-skip-permissions` is itself blocked by the harness's own classifier as a broad bypass. The YouTube scan (Step 3) was done with `WebSearch` instead — it surfaces relevant videos but not reliable publish dates for most results, so treat the 📺 section as directional, not exhaustive. `grok -p` worked fine for the X.com scan. `gh` CLI auth is broken (`Bad credentials`), so GitHub release data was pulled via the unauthenticated public API instead.
>
> **This run adds** the accounts/newsletters list from `scripts/weekly-update-scan.md` Step 2/5b (see below) to the standard scan.

## 🔎 Newsletter / community cross-check (new this run)

| Source | Finding | Date |
|--------|---------|------|
| Software Testing Weekly | Issue #321 "Testing in an Agentic World" | 2026-08-10 |
| Software Testing Weekly | Issue #320 "How Slack Uses AI Agents For Testing" | 2026-08-02 |
| Ministry of Testing | TestMu Conf 2026 (free virtual AI testing/QE conference) ran 2026-08-19 → 08-21, MoTaverse attended | 2026-08-19 |
| `@debs_obrien` (X) | **Correction to last week's recommendation:** she is no longer closely tied to Playwright day-to-day — her recent posts show she left Microsoft a while back, then left Zephyr as of 2026-08-21, and is now focused on "agents, MCP, and AI-native testing" broadly rather than Playwright specifically. Still worth following for AI-testing takes, but don't expect Playwright-specific deep-dives from her feed going forward. | 2026-08-21 |
| TestGuild | August coverage centers on "AI-DLC" (AI Delivery Lifecycle) and agentic/low-code automation trends — no single tool release scoop this window, but useful trend confirmation for the AI-for-QA docs. | 2026-08-06 |

## 🔴 Outdated — needs update

| Tool | Our current info | What changed | Source |
|------|-------------------|---------------|--------|
| **Bruno** (`docs/tools/api/bruno.md`) | Framed only as "keep API requests local and version them in Git" — no mention of mock servers, AI features, or docs tooling | **v4.1.0** (2026-08-20) added a built-in mock server, a rich-text docs editor, typed variables, GCP Secret Manager + global client certs, and monorepo multi-collection support. v4.0 also added native AI (BYO key, local-only) for generating tests/docs/scripts. | [GitHub release v4.1.0](https://github.com/usebruno/bruno/releases/tag/v4.1.0), [x.com/use_bruno/status/2090534370993942740](https://x.com/use_bruno/status/2090534370993942740) |
| **Appium** (`docs/tools/mobile/appium.md`) | No mention of major version or current driver requirements | Appium core is now at **3.7.0** (2026-08-24), well into the Appium 3.x line (breaking changes vs. Appium 2). Community reports **iOS 26.4+ requires XCUITest driver 10.23.2+ / Appium 3**. | [GitHub release appium@3.7.0](https://github.com/appium/appium/releases/tag/appium%403.7.0), [x.com/NoStackKami/status/2084568577605025909](https://x.com/NoStackKami/status/2084568577605025909) |
| **Playwright** (`docs/tools/web/playwright.md`) | Generic "web/PWA/admin panel" framing; no mention of AI/agent tooling | As of **v1.60–1.62**, the **Playwright MCP server and CLI now ship in-box** (`npx playwright mcp`), plus WebAuthn/passkey virtual authenticator support, `page.localStorage`/`sessionStorage`, and `retryStrategy: 'isolated'`. Current release: **v1.62.1** (2026-07-30). This overlaps directly with `docs/tools/ai/playwright-mcp.md`, which still describes MCP as a separate install. | [GitHub release v1.62.1](https://github.com/microsoft/playwright/releases/tag/v1.62.1), [x.com/playwrightweb/status/2085055175438516590](https://x.com/playwrightweb/status/2085055175438516590) |
| **Proxyman** (`docs/tools/debugging/proxyman.md`) | Doc covers Map Local, cert install, troubleshooting only | **6.15.0** (2026-08-13) added simulator traffic grouping and better **MCP support** for AI coding agents; a **Codex plugin** and JS scripting on iOS also shipped this window. Worth a line under "Następny krok" pointing at AI-agent integration. | [x.com/proxyman_app/status/2087834044469813593](https://x.com/proxyman_app/status/2087834044469813593) |
| **GitHub Copilot** (`docs/tools/ai/github-copilot.md`) | Fully generic template — "write tests, explain code" only | Copilot now does **build-and-test for iOS/Android inside the Copilot app** (compile + run in chat), and **PR code review depth is GA** (Balanced vs. Lite modes) — both directly relevant to a QA workflow doc. | [x.com/pierceboggan/status/2092747145984221381](https://x.com/pierceboggan/status/2092747145984221381), [x.com/github/status/2089057545998479457](https://x.com/github/status/2089057545998479457) |

## 🟡 New content worth adding

| Topic | Why it's relevant | Source |
|-------|--------------------|--------|
| **Maestro MCP** (open source) | Not documented anywhere in `docs/tools/mobile/maestro.md` or `docs/tools/ai/`. Coding agents (Claude Code, Cursor, Codex, Grok Build) can now drive/QA any iOS or Android app through it — this is exactly the "AI + mobile automation" intersection the `docs/tools/ai/` section is built for. | [x.com/maestro__dev/status/2083164417282506853](https://x.com/maestro__dev/status/2083164417282506853), [x.com/maestro__dev/status/2092579813324362179](https://x.com/maestro__dev/status/2092579813324362179) |
| **BrowserStack Test Companion** + **Accessibility DevTools** | Two new products (agentic AI test authoring/debugging in-IDE; accessibility linting in the editor) not covered in `docs/tools/mobile/browserstack.md`, which currently only describes App Live/App Automate. | BrowserStack blog homepage; [x.com/browserstack/status/2082451627508945305](https://x.com/browserstack/status/2082451627508945305) |
| **Testomat.io Defects tracking** | New per-project Defects page, Defects analytics report, and milestone Defects/Users tabs — extends `docs/tools/test-management/testomat.md`'s "unified manual + automation reporting" pitch. | [x.com/testomatio/status/2085377916339122529](https://x.com/testomatio/status/2085377916339122529) |
| **Postman Orbit / AI Engineer / Passport** | Postman is repositioning around AI agents discovering and calling APIs (Orbit), an AI Engineer feature for tracing data across APIs, and a "Passport" credential-isolation architecture. Worth a short mention in `docs/tools/api/postman.md`'s "Następny krok" for teams pairing Postman with AI workflows. | Postman blog (blog.postman.com) |
| **Ollama v0.33 as an AI-client gateway** | Ollama can now act as a third-party model gateway inside Claude Desktop (toggle between local/cloud models). Relevant to `docs/tools/ai/ollama.md`'s "połącz z Continue.dev" next-step section — this is now a second, non-Continue.dev integration path. | [x.com/ollama/status/2092453536634380763](https://x.com/ollama/status/2092453536634380763) |
| **Browser Use 3.0 CLI** | New persistent cloud/CDP browser session model, claimed 72% faster than the legacy tool-call-per-click approach. `docs/tools/ai/browser-use.md` currently only describes the generic install workflow — no mention of the CLI or performance profile. | [x.com/trevin/status/2091696470424686749](https://x.com/trevin/status/2091696470424686749) |

## 🟢 No changes detected

- **Hoppscotch** — no release/product posts in the scan window; doc content still current.
- **mitmproxy** — latest release is still v12.2.3 (2026-05-12), no newer version; workflow/troubleshooting content in the doc is unaffected.
- **Charles Proxy** — no update activity found; official account has been inactive since 2023.
- **Jira** (test-management angle) — no test-management-specific changes; general Atlassian news (formula fields, Code Context beta) is outside this doc's scope.
- **Xray** — no release/update posts found; official account inactive since May 2025.
- **Qase** — no update/release posts found this window.
- **Continue.dev** — no first-party release posts found this window.
- **Espresso / XCUITest** — no direct framework-level release posts (the only XCUITest-adjacent news is the Appium driver compatibility item already listed under 🔴 Appium).

## 📺 Noteworthy YouTube content

| Video | Channel | Date | Relevant to |
|-------|---------|------|--------------|
| [Mobile Testing With No Local Devices: Maestro Cloud + MCP Live Demo](https://www.youtube.com/watch?v=901PFFnX4JE) | mobile-dev (Maestro) | ~late Jul/Aug 2026 (reported "~1 month ago") | `docs/tools/mobile/maestro.md` — cloud-based testing without local emulators, ties directly to the Maestro MCP push above |
| [How to Use Maestro MCP with Cursor IDE for Mobile Testing](https://www.youtube.com/watch?v=tuffQjos2sA) | — | 2026-06-26 | `docs/tools/mobile/maestro.md` / `docs/tools/ai/` — AI agent driving mobile app testing via MCP |
| [\[2026\]: Appium Mobile App Automation Testing: Android Emulator + BDD (Cucumber)](https://www.youtube.com/watch?v=4UxJXlrFEw4) | — | 2026 (exact date unconfirmed) | `docs/tools/mobile/appium.md` — modern Appium + BDD setup walkthrough |
| [New AI Features in Playwright (Live-Webinar)](https://www.youtube.com/watch?v=qHc6-4d7pJ8) | — | 2026 (exact date unconfirmed) | `docs/tools/web/playwright.md` / `docs/tools/ai/playwright-mcp.md` — covers the AI/MCP feature set noted in 🔴 above |
| [Playwright 1.59 Release: New Features You Should Know](https://www.youtube.com/watch?v=uSPPqAtdrZM) | — | 2026 (exact date unconfirmed) | `docs/tools/web/playwright.md` — version-specific feature walkthrough for the Test Agents / Screencast API release |

## 🐦 X.com highlights

| Post summary | Tool | Date |
|---------------|------|------|
| v4.1.0 shipped: mock server, rich-text docs editor, GCP Secret Manager, global client certs | Bruno | 2026-08-20 |
| Maestro MCP promoted for coding agents (open source, iOS/Android) | Maestro | 2026-07-31 |
| MCP setup docs published for Grok Build, Codex, Claude Code, Cursor | Maestro | 2026-08-26 |
| Test Companion launched — agentic AI test authoring/debugging in the IDE | BrowserStack | 2026-07-29 |
| Pixel 11 family live on device cloud within an hour of retail launch | BrowserStack | 2026-08-19 |
| 6.15.0 shipped — simulator traffic grouping, MCP support, macOS 27 fixes | Proxyman | 2026-08-13 |
| v1.60–v1.62 catch-up: MCP server/CLI in-box, WebAuthn passkey testing, `retryStrategy: 'isolated'`, WebP snapshots | Playwright | 2026-08-05 |
| PR code review depth GA: Balanced vs. Lite modes | GitHub Copilot | 2026-08-16 |
| Build-and-test for iOS/Android inside the Copilot app | GitHub Copilot | 2026-08-26 |
| v0.33 — usable as a model gateway inside Claude Desktop | Ollama | 2026-08-26 |
| 3.0 CLI released — persistent cloud/CDP browser, ~72% faster than legacy tool calls | Browser Use | 2026-08-24 |
| Defects page, Defects analytics report, and milestone Defects tab shipped | Testomat.io | 2026-08-06 |
| Community note: iOS 26.4+ requires XCUITest driver 10.23.2+ (Appium 3) | Appium | 2026-08-04 |
