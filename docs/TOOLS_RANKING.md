# Ranking narzędzi QA — od czego zacząć

> Jeśli nie wiesz od czego zacząć — zacznij od Tier 1. Dopiero po opanowaniu Tier 1 przejdź do Tier 2.

---

## Tier 1 — Naucz się najpierw (podstawy warsztatu testera)

Bez tych narzędzi nie jesteś w stanie technicznie udowodnić błędu i rozróżnić, gdzie leży problem.

| Narzędzie | Obszar | Dlaczego najpierw | Link |
|---|---|---|---|
| **ADB** | Android / mobile | Logi, instalacja APK, screenrecord — bez tego nie masz dowodów technicznych | [→](tools/mobile/adb.md) |
| **Android Studio / Emulator** | mobile | Testujesz na różnych wersjach OS i rozmiarach bez fizycznych urządzeń | [→](tools/mobile/android-studio-emulator.md) |
| **scrcpy** | mobile | Mirror Androida na komputerze, nagranie kroków buga w 10 sekund | [→](tools/mobile/scrcpy.md) |
| **Postman lub Bruno** | API testing | Testujesz backend niezależnie od UI — rozróżniasz błąd Frontend vs Backend | [→](tools/api/postman.md) |
| **mitmproxy lub HTTP Toolkit** | network proxy | Widzisz co apka wysyła do serwera i co dostaje — klucz do analizy API | [→](tools/debugging/mitmproxy.md) |
| **Jira** | test management | Bug reporty, workflow, sprinty — standard branżowy | [→](tools/test-management/jira.md) |
| **Browser DevTools** | web testing | Network tab, Console, Elements — bez tego nie tesztujesz webappów | [→](tools/web/browser-devtools.md) |

**Efekt po Tier 1:** Potrafisz technicznie udowodnić każdy bug, zebrać logi i requesty, rozróżnić problem UI/backend/sieć.

---

## Tier 2 — Następny poziom (po opanowaniu Tier 1)

Narzędzia, które przyspieszają workflow i otwierają automatyzację.

| Narzędzie | Obszar | Dlaczego teraz | Link |
|---|---|---|---|
| **Maestro** | mobile automation | Pierwszy test E2E bez ciężkiego frameworka — YAML, bez kodowania | [→](tools/mobile/maestro.md) |
| **Appium Inspector** | mobile automation | Znajdowanie selektorów do automatyzacji bez pisania kodu | [→](tools/mobile/appium-inspector.md) |
| **Playwright** | web automation | Automatyzacja paneli admina, webview, PWA | [→](tools/web/playwright.md) |
| **Allure Report** | automation reporting | Czytelne raporty z testów automatycznych | [→](tools/debugging/allure-report.md) |
| **Qase lub AgileTest** | test management | Nowoczesny TMS z integracją Jira, darmowy dla małych teamów | [→](tools/test-management/qase.md) |
| **Jam.dev** | bug reporting | 1 klik = nagranie + logi + Jira — zastępuje ręczne zbieranie dowodów | [→](tools/bug-reporting/jam.md) |
| **Firebase Crashlytics** | crash monitoring | Raporty o crashach z prawdziwych urządzeń i sesji | [→](tools/mobile/firebase-crashlytics.md) |
| **Figma Dev Mode** | UI inspection | Source of truth dla UI — porównujesz z implementacją | [→](tools/ui-inspection/figma-dev-mode.md) |

**Efekt po Tier 2:** Masz pierwsze testy automatyczne, czytelne raporty, szybki bug reporting i weryfikację UI vs projekt.

---

## Tier 3 — AI i eksperymenty agentowe

Narzędzia AI, które przyspieszają pracę. Wymagają już warsztatu z Tier 1+2, żeby ocenić jakość outputu.

| Narzędzie | Obszar | Kiedy używać | Link |
|---|---|---|---|
| **ChatGPT / Claude** | AI assistant | Generowanie TC, analiza logów, review bug reportów, wyjaśnienia | — |
| **Ollama / LM Studio** | local AI | Dane firmowe objęte NDA — analiza logów i kodu offline | [→](tools/ai/ollama.md) |
| **GitHub Copilot** | coding assistant | Pisanie i review testów automatycznych w IDE | [→](tools/ai/github-copilot.md) |
| **Continue.dev** | local AI coding | Lokalny asystent kodu w VS Code z własnym modelem | [→](tools/ai/continuedev.md) |
| **MaestroGPT** | AI YAML generation | Natural language → Maestro YAML flow | [→](tools/ai/maestrogpt.md) |
| **Playwright MCP** | AI web agent | Agent AI sterujący przeglądarką | [→](tools/ai/playwright-mcp.md) |
| **Appium MCP** | AI mobile agent | Eksperymenty z AI sterującym aplikacją mobilną | [→](tools/ai/appium-mcp.md) |
| **Testsigma** | AI test automation | AI generuje i wykonuje TC z Jiry — bez kodowania | [→](tools/ai/testsigma.md) |

**Efekt Tier 3:** AI przyspiesza projektowanie testów i analizę logów — ale Ty nadal kontrolujesz jakość.

---

## Tier 4 — Specjalistyczne (w zależności od projektu)

Potrzebujesz kiedy projekt tego wymaga — nie każdy tester musi znać wszystkie.

| Narzędzie | Kiedy potrzebujesz |
|---|---|
| Appium | Duży projekt mobile z pełną automatyzacją E2E |
| BrowserStack / Firebase Test Lab | Testy na fizycznych urządzeniach w chmurze |
| Espresso / XCUITest | Praca bezpośrednio z kodem apki (white-box) |
| Xcode Simulator | Testowanie iOS (wymaga macOS) |
| Sentry | Monitoring błędów produkcyjnych |
| Kiwi TCMS / TestLink | Self-hosted TMS dla firmy bez SaaS |
| Browser Use / Roo Code / Cline | Eksperymentalny agentic testing |

---

## Mapa zależności

```text
ADB ──────────────────────────────────────────► Appium
  └─► scrcpy                                      │
  └─► logcat ──► AI (analiza logów)               │
                                                   ▼
Postman / Bruno ──► mitmproxy ──────────────► HTTP Toolkit
                      │
                      └─► Proxyman (macOS)

Android Studio ──► Emulator ──► Maestro ──────► Appium Inspector
                                  │               │
                              MaestroGPT       selektory
                                                  │
Playwright ◄──────────────────────────────────────┘
    │
Playwright MCP ──► AI agent web

Ollama / LM Studio ──► Continue.dev ──► GitHub Copilot
```
