# Ścieżka: manual mobile QA → automatyzacja

## Jak korzystać z tej ścieżki

Każdy etap ma: **cel**, **narzędzia**, **mini-zadanie** i **rezultat do portfolio**.
Nie przeskakuj etapów — każdy buduje fundament pod następny.

---

## Etap 0 — Fundament: dobry bug report

**Cel:** Tester potrafi opisać błąd precyzyjnie, bez "nie działa" i "coś się stało".

**Narzędzia:**
- `templates/bug-report-template.md`
- `prompts/bug-report-prompts.md`

**Mini-zadanie:**
Zgłoś 3 bugi w dowolnej aplikacji, używając szablonu. Poproś kolegę lub AI o review każdego raportu.

**Rezultat do portfolio:**
3 przykładowe bug reporty w `portfolio-projects/01-bug-reports/`

---

## Etap 1 — Android toolbox: ADB + emulator + scrcpy

**Cel:** Tester potrafi technicznie udowodnić błąd — zebrać logi, nagranie i informacje o urządzeniu.

**Narzędzia:**
- [`tools/mobile/adb.md`](../tools/mobile/adb.md) ← zacznij tutaj
- [`tools/mobile/android-studio-emulator.md`](../tools/mobile/android-studio-emulator.md)
- [`tools/mobile/scrcpy.md`](../tools/mobile/scrcpy.md)

**Kluczowe komendy do opanowania:**
```bash
adb devices
adb logcat -c && adb logcat -d > log.txt
adb shell screenrecord /sdcard/bug.mp4 && adb pull /sdcard/bug.mp4 .
adb install -r app-debug.apk
adb shell getprop ro.product.model
```

**Mini-zadanie:**
1. Podłącz telefon lub uruchom emulator
2. Odtwórz dowolny bug w aplikacji
3. Zbierz: nagranie + logi + screenshot + informacje o urządzeniu
4. Dołącz to do bug reportu z Etapu 0

**Rezultat do portfolio:**
Bug report z logami ADB + nagraniem scrcpy jako dowód.

---

## Etap 2 — API: Postman / Bruno

**Cel:** Tester rozumie, czy problem leży w UI czy w backendzie. Potrafi ręcznie wykonać request.

**Narzędzia:**
- [`tools/api/postman.md`](../tools/api/postman.md) lub [`tools/api/bruno.md`](../tools/api/bruno.md)
- [`tools/api/openapi-swagger.md`](../tools/api/openapi-swagger.md)
- [`tools/api/jwt-basics.md`](../tools/api/jwt-basics.md)

**Kluczowe umiejętności:**
- Czytanie i wykonywanie requestów GET/POST/PUT/DELETE
- Rozumienie status codes (200, 400, 401, 404, 500)
- Ustawienie Authorization (Bearer token)
- Walidacja response body

**Mini-zadanie:**
1. Znajdź publiczne API (np. `jsonplaceholder.typicode.com` lub własne staging)
2. Wykonaj GET, POST, PUT, DELETE
3. Znajdź przypadek, gdzie response jest inny niż oczekiwany

**Rezultat do portfolio:**
Kolekcja Bruno w `portfolio-projects/02-api-testing/` z requestami i komentarzami.

---

## Etap 3 — Inspekcja sieci: mitmproxy / HTTP Toolkit

**Cel:** Tester widzi co aplikacja mobilna wysyła do serwera i co dostaje. Potrafi rozróżnić Frontend/Backend bug.

**Narzędzia:**
- [`tools/debugging/mitmproxy.md`](../tools/debugging/mitmproxy.md) lub [`tools/api/http-toolkit.md`](../tools/api/http-toolkit.md)
- [`workflows/bug-investigation-api.md`](../workflows/bug-investigation-api.md)

**Mini-zadanie:**
1. Skonfiguruj proxy na telefonie
2. Otwórz aplikację i wykonaj akcję (logowanie, ładowanie listy)
3. Znajdź request w proxy
4. Skopiuj request do Postmana/Bruno i odtwórz ręcznie
5. Zmodyfikuj response (np. podmień status 200 na 401) i sprawdź reakcję UI

**Rezultat do portfolio:**
Opis workflow API debugging z przykładowym requestem/response.

---

## Etap 4 — Pierwsza automatyzacja: Maestro

**Cel:** Tester pisze pierwszy działający test E2E bez kodowania (YAML).

**Narzędzia:**
- [`tools/mobile/maestro.md`](../tools/mobile/maestro.md)
- [`tools/ai/maestrogpt.md`](../tools/ai/maestrogpt.md)
- `examples/maestro/login-flow.yaml`
- `prompts/mobile-testing-prompts.md` → sekcja "Generowanie YAML Maestro"

**Mini-zadanie:**
1. Zainstaluj Maestro CLI: `curl -Ls "https://get.maestro.mobile.dev" | bash`
2. Napisz flow logowania (5-7 kroków)
3. Uruchom: `maestro test login-flow.yaml`
4. Popraw do momentu, gdy test przechodzi

**Przykładowy flow:**
```yaml
appId: com.example.app
---
- launchApp
- tapOn: "Zaloguj się"
- inputText:
    text: "test@example.com"
    id: "email_input"
- tapOn: "Zaloguj"
- assertVisible: "Strona główna"
```

**Rezultat do portfolio:**
3-5 działających Maestro flows w `examples/maestro/` z opisem w README.

---

## Etap 5 — Inspekcja selektorów: Appium Inspector

**Cel:** Tester potrafi znaleźć `resource-id`, `accessibility-id`, `xpath` do elementów UI — fundament każdej automatyzacji.

**Narzędzia:**
- [`tools/mobile/appium-inspector.md`](../tools/mobile/appium-inspector.md)
- [`tools/ui-inspection/uiautomatorviewer.md`](../tools/ui-inspection/uiautomatorviewer.md)

**Mini-zadanie:**
Podłącz Appium Inspector do działającej aplikacji. Znajdź resource-id dla 5 różnych elementów. Użyj tych selektorów do poprawienia Maestro flows z Etapu 4.

---

## Etap 6 — Web automation: Playwright

**Cel:** Tester automatyzuje panel admina, webview lub PWA.

**Narzędzia:**
- [`tools/web/playwright.md`](../tools/web/playwright.md)
- `examples/playwright/example.spec.ts`

**Mini-zadanie:**
1. `npm init playwright@latest`
2. Uruchom Codegen: `npx playwright codegen https://twoja-aplikacja.com`
3. Wygeneruj test logowania + jeden test głównej funkcji
4. Uruchom: `npx playwright test`
5. Otwórz HTML report

**Rezultat do portfolio:**
2-3 testy Playwright w `examples/playwright/` z opisem.

---

## Etap 7 — Poważna automatyzacja mobile: Appium

**Cel:** Tester pisze i uruchamia pełny test E2E mobile z kodem.

**Narzędzia:**
- [`tools/mobile/appium.md`](../tools/mobile/appium.md)
- [`tools/debugging/allure-report.md`](../tools/debugging/allure-report.md)

**Mini-zadanie:**
1. Zainstaluj Appium (`npm install -g appium`)
2. Zainstaluj driver: `appium driver install uiautomator2`
3. Napisz pierwszy test (logowanie) w Pythonie lub JavaScript
4. Dodaj raport Allure

**Rezultat do portfolio:**
Działający test Appium + raport Allure w `examples/appium/`.

---

## Etap 8 — AI jako asystent QA

**Cel:** AI przyspiesza projektowanie testów, analizę logów i review bug reportów — ale tester kontroluje jakość.

**Narzędzia:**
- `prompts/` ← wszystkie pliki
- [`tools/ai/ollama.md`](../tools/ai/ollama.md) — do danych firmowych
- [`tools/ai/ai-risk-checklist.md`](../tools/ai/ai-risk-checklist.md) ← przeczytaj zanim użyjesz AI

**Mini-zadanie:**
1. Wygeneruj TC z User Story używając promptu z `prompts/test-case-prompts.md`
2. Sprawdź output przez AI risk checklist
3. Uzupełnij o 3 TC, które AI pominęło
4. Użyj AI do analizy logcata z Etapu 1

**Zasada:**
AI generuje draft — Ty weryfikujesz, uzupełniasz i akceptujesz.

---

## Etap 9 — Portfolio project

**Cel:** Repo pokazuje realne umiejętności rekruterowi lub teamowi.

**Mini-zadanie:**
Stwórz w `portfolio-projects/` jeden kompletny projekt:
- Opis funkcji do przetestowania
- Checklist testowy
- 3 bug reporty z dowodami
- 5 Maestro flows (smoke test)
- Kolekcja API w Bruno
- Opis procesu testowania

**Przykładowa aplikacja do użycia:**
- `https://demo.realworld.io/` (webowa)
- `https://github.com/Microsoft/MSBuildSdks` (inne demo)
- Własna aplikacja jeśli masz dostęp

---

## Mapa czasu (orientacyjna)

| Etap | Czas nauki |
|---|---|
| 0 — Bug report | 1-2 dni |
| 1 — ADB + emulator + scrcpy | 3-5 dni |
| 2 — Postman / Bruno | 3-5 dni |
| 3 — Proxy | 2-3 dni |
| 4 — Maestro | 1 tydzień |
| 5 — Appium Inspector | 2-3 dni |
| 6 — Playwright | 1-2 tygodnie |
| 7 — Appium | 2-4 tygodnie |
| 8 — AI workflow | ciągły proces |
| 9 — Portfolio | 2-4 tygodnie |
