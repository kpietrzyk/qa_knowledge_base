# Roadmap repozytorium

## Etap 1 — manual mobile QA toolbox

Cel: tester potrafi samodzielnie zebrać dowody błędu.

- ADB
- Android Studio Emulator
- scrcpy
- logcat
- screen recording
- bug report template
- release checklist
- mobile app checklist

## Etap 2 — API i debugowanie sieci

Cel: tester rozumie, czy problem jest w UI, backendzie, danych czy sieci.

- Postman / Bruno
- HTTP Toolkit / mitmproxy / Charles Proxy
- analiza request/response
- status codes
- tokeny, nagłówki, payload
- podstawowe mockowanie

## Etap 3 — pierwsza automatyzacja

Cel: zamiana powtarzalnych smoke/regression testów w automaty.

- Maestro dla szybkiego startu
- Playwright dla paneli web/admin/PWA
- Appium dla docelowego mobile E2E
- Allure dla raportów

## Etap 4 — AI-assisted QA

Cel: AI przyspiesza pracę, ale tester nadal kontroluje jakość.

- generowanie przypadków testowych (TC z US)
- analiza wymagań i ryzyk
- review bug reportów
- pomoc w locatorach (Appium Inspector)
- generowanie pierwszych testów (MaestroGPT)
- analiza logów i stack trace
- tworzenie checklist

## Etap 5 — portfolio

Cel: repo pokazuje realne umiejętności.

- przykładowe testy Maestro
- przykładowe testy Playwright
- przykładowy bug report
- przykładowa kolekcja API
- opis procesu testowania aplikacji mobilnej

---

## Roadmapa czasowa: Manual → Automatyzacja

### Tydzień 1 — Optymalizacja manual workflow

| Narzędzie | Cel |
|---|---|
| scrcpy + ADB | Mirror Android, nagranie kroków buga, logi |
| HTTP Toolkit | Inspekcja requestów API bez konfiguracji |
| Qase lub AgileTest | TMS z integracją Jira |
| Jam.dev | Bug reporting: 1 klik = nagranie + logi + Jira |
| Figma Dev Mode | Weryfikacja UI relative do projektu |

### Miesiąc 1 — AI jako asystent testera

| Działanie | Narzędzie |
|---|---|
| TC z user stories | ChatGPT / Claude z prompty z tego repo |
| Bug report review | ChatGPT / Claude |
| Analiza logcat | ChatGPT / Claude |
| Własna biblioteka promptów | Fork `qa-prompt-library` na GitHub |
| Manualne testowanie API | Bruno lub Postman |

### Miesiąc 2–3 — Pierwsze testy automatyczne

| Działanie | Narzędzie |
|---|---|
| Pierwsze flow YAML | Maestro CLI + Maestro Studio |
| Generowanie flow z opisu | MaestroGPT |
| 3–5 smoke tests kluczowych flow | Maestro |
| Inspekcja selektorów | Appium Inspector |
| Wyszukiwanie resource-id | uiautomatorviewer |

### Miesiąc 4–6 — Stabilna automatyzacja

| Działanie | Narzędzie |
|---|---|
| 10–20 Maestro flows + CI/CD | Maestro + GitHub Actions |
| Pierwsze skrypty API | Postman/Newman lub Bruno |
| Pierwsze skrypty Appium | Python lub JavaScript |
| Asystent przy kodowaniu | GitHub Copilot |
| Testy dostępności a11y | Accessibility Scanner + Xcode Inspector |
