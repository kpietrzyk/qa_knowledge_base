# Weekly QA Knowledge Base Update Scan

You are acting as a research assistant for the `kpietrzyk/qa_knowledge_base` repository — a practical QA knowledge base for mobile testers focused on automation and AI tools.

## Your Task

Scan the web, X.com (via Grok CLI), and YouTube (via Gemini CLI) for updates relevant to tools documented in this repo. Then compile a structured update report and save it as `weekly-update-report.md` in the repo root.

---

## Step 1 — Check available CLIs

Before using Grok or Gemini, check their syntax:
```
grok --help
gemini --help
```

---

## Step 2 — Scan X.com via Grok CLI

Use Grok to search X.com for recent posts and announcements about each tool category. Run separate queries for each group:

- Mobile testing: `Appium OR Maestro OR XCUITest OR Espresso OR BrowserStack new release update 2026`
- API testing: `Postman OR Bruno OR Hoppscotch update release 2026`
- Proxy/Debugging: `mitmproxy OR Proxyman OR "Charles Proxy" update 2026`
- Web testing: `Playwright release update 2026`
- AI for QA: `"GitHub Copilot" OR "Continue.dev" OR Ollama OR "Browser Use" OR "Playwright MCP" update 2026`
- Test management: `Jira OR Qase OR Testomat OR Xray update release 2026`

For each query note: tool name, what changed, source URL, date.

---

## Step 3 — Scan YouTube via Gemini CLI

Use Gemini to find recent YouTube videos (last 30 days) about tools in this repo:

- `Appium tutorial 2026 new features`
- `Playwright new features 2026`
- `Maestro mobile testing 2026`
- `AI QA testing tools 2026`
- `Bruno API testing 2026`

For each result note: video title, channel, date, what tool it covers, why it's relevant.

---

## Step 4 — Scan GitHub Releases

Fetch the latest release for each of these GitHub repos and note version + changelog summary:

- https://github.com/appium/appium/releases/latest
- https://github.com/mobile-dev-inc/maestro/releases/latest
- https://github.com/usebruno/bruno/releases/latest
- https://github.com/microsoft/playwright/releases/latest
- https://github.com/mitmproxy/mitmproxy/releases/latest

---

## Step 5 — Scan official blogs / RSS

Fetch and skim these pages for news published in the last 30 days:

- https://blog.postman.com
- https://www.browserstack.com/blog
- https://firebase.google.com/support/release-notes/android
- https://playwright.dev/blog

---

## Step 6 — Cross-reference with repo content

Read the relevant `.md` files in `docs/tools/` to understand what version or information is currently documented. For each finding from steps 2–5, check if our docs are outdated or missing something important.

---

## Step 7 — Write the report

Save a file `weekly-update-report.md` in the repo root with this structure:

```markdown
# Weekly Update Report — [DATE]

## 🔴 Outdated — needs update
| Tool | Our current info | What changed | Source |
|------|-----------------|--------------|--------|
| ... | ... | ... | ... |

## 🟡 New content worth adding
| Topic | Why it's relevant | Source |
|-------|------------------|--------|
| ... | ... | ... |

## 🟢 No changes detected
- Tool A — still current
- Tool B — still current

## 📺 Noteworthy YouTube content
| Video | Channel | Date | Relevant to |
|-------|---------|------|-------------|
| ... | ... | ... | ... |

## 🐦 X.com highlights
| Post summary | Tool | Date |
|-------------|------|------|
| ... | ... | ... |
```

---

## Final Note

Do NOT make changes to any documentation files. Only write `weekly-update-report.md`. The human will review the report and decide what to update.
