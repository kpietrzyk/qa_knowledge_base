# Comparison table

## Mobile Testing & Emulators

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| Android Studio / Emulator | mobile-testing | True | False | very high | medium | Połącz z ADB, Appium, Maestro albo Firebase Test Lab. |
| Xcode Simulator | mobile-testing | True (macOS) | False | very high | medium | Połącz z Xcode Accessibility Inspector, testuj na różnych rozmiarach. |
| Genymotion Desktop | mobile-testing | True (personal) | False | high | medium-high | Połącz z ADB i scrcpy, używaj GPS widget do testów lokalizacji. |
| BrowserStack | mobile-testing | False (trial) | False | very high | very high | Uruchom App Live dla manualnych testów, App Automate dla automatyzacji. |
| ADB | mobile-testing | True | False | very high | high | Naucz się komend: adb devices, adb install, adb logcat, adb shell, adb bugreport. |
| scrcpy | mobile-testing | True | False | high | low | Połącz z ADB, narzędziami do nagrywania i checklistą bug reportu. |
| QuickTime Player | mobile-testing | True (macOS) | False | high | low | Nagraj reprodukcję buga na iPhonie przez USB. |
| OBS Studio | mobile-testing | True | False | high | low | Połącz z oknem scrcpy i dodaj mikrofon do sesji eksploracyjnych. |
| Vysor | mobile-testing | True (limited) | False | medium-high | low | Przejdź na scrcpy do codziennej pracy — jest szybszy i w pełni darmowy. |
| Firebase Crashlytics | mobile-testing | True | False | high | medium | Łącz zgłoszenia z Jira i wersjami buildów. |
| Firebase Test Lab | mobile-testing | False | False | medium-high | high | Uruchom smoke test na kilku popularnych modelach Android. |

## Mobile Automation

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| Maestro | mobile-automation | True | False | very high | high | Napisz pierwsze flow YAML: launchApp, tapOn, inputText, assertVisible. |
| Appium Inspector | mobile-automation | True | False | high | very high | Podłącz do serwera Appium, otwórz apkę, klikaj elementy i kopiuj selektory. |
| Appium | mobile-automation | True | True | high | very high | Zacznij od prostych testów w Pythonie albo Javie, potem dodaj Page Object i Allure. |
| Katalon Studio | mobile-automation | True (basic) | False | medium-high | high | Nagraj prosty flow, odtwórz, dodaj asercję. |
| Espresso | mobile-automation | True | True | low | very high | Zacznij od Appium (czarna skrzynka) — Espresso wymaga Javy/Kotlina i kodu apki. |
| XCUITest | mobile-automation | True (macOS) | True | low | very high | Dla czarnej skrzynki bez Swifta użyj Appium zamiast XCUITest. |
| Appium MCP | ai-for-testing | True | True | medium-high | high | Uruchom lokalnie, połącz z emulatorem i testuj generowanie kroków na prostych ekranach. |

## API Testing & Network Proxy

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| HTTP Toolkit | api-testing | True | False | very high | medium | Otwórz, wybierz Android, zeskanuj QR telefonem i obserwuj requesty. |
| Reqable | api-testing | True (plan) | False | high | medium | Uruchom w trybie capture, otwórz apkę mobilną i przechwytuj ruch. |
| Postman | api-testing | True (plan) | False | very high | high | Dodaj testy w zakładce Tests i uruchamiaj kolekcje w Newman. |
| Bruno | api-testing | True | False | high | medium-high | Utwórz kolekcje dla logowania, profilu, zamówień i krytycznych endpointów. |
| Hoppscotch | api-testing | True | False | medium-high | medium | Porównaj z Bruno/Postman pod kątem pracy zespołowej. |
| HTTP Toolkit | api-testing | True | False | very high | medium | Otwórz, wybierz Android, zeskanuj QR telefonem i obserwuj requesty. |
| mitmproxy | debugging | True | False | high | medium | Skonfiguruj proxy na telefonie i zainstaluj certyfikat testowy. |
| Charles Proxy | debugging | False | False | very high | medium | Jeżeli budżet zerowy, zacznij od mitmproxy lub HTTP Toolkit. |
| Proxyman | debugging | True (macOS) | False | very high | medium | Naucz się Map Local do podmiany odpowiedzi serwera bez angażowania backendowca. |
| Fiddler Everywhere | debugging | False | False | high | medium | Porównaj koszty z Charles i darmowym mitmproxy. |

## Bug Reporting & Adnotacje

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| Jam | bug-reporting | True (plan) | False | very high | low | Połącz z Jirą i ustaw jako domyślne narzędzie do raportowania bugów. |
| Bird Eats Bug | bug-reporting | True (plan) | False | high | low | Porównaj z Jam.dev pod kątem integracji z Jirą. |
| Greenshot | bug-reporting | True | False | high | low | Używaj razem z bug report template dla kompletnych zgłoszeń. |
| Loom | bug-reporting | True (25 nagrań) | False | high | low | Combine z Jam dla bugów wymagających i kontekstu technicznego i opisu kroków. |
| Instabug | bug-reporting | False (trial) | False | very high | medium | Połącz raporty z Jirą i ustandaryzuj severity w zespole. |

## UI Inspection & Dostępność

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| Figma Dev Mode | ui-inspection | True (read-only) | False | very high | low | Otwórz Inspect panel i sprawdź wartości dp/sp względem implementacji. |
| Android Layout Inspector | ui-inspection | True | False | very high | medium | Uruchom apkę, otwórz Layout Inspector w Android Studio, klikaj elementy. |
| Xcode Accessibility Inspector | ui-inspection | True (macOS) | False | high | medium | Otwórz na symulatorze i sprawdź VoiceOver labels wszystkich elementów. |
| Accessibility Scanner | ui-inspection | True | False | high | low | Zainstaluj, uruchom na ekranie apki i przejrzyj raport problemów. |
| uiautomatorviewer | ui-inspection | True | False | medium-high | high | Użyj Appium Inspector — nowocześniejsza alternatywa z lepszym UX. |

## Test Management

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| Jira | test-management | True (plan) | False | very high | medium | Ustandaryzuj szablon bug reportu i pola Severity/Priority. |
| Qase | test-management | True (≤3 users) | False | very high | high | Stwórz projekt, dodaj test cases, wykonaj pierwszy test run. |
| AgileTest | test-management | True (≤10 users) | False | very high | medium | W Jirze, stwórz test case i połącz ze story w bieżącym sprincie. |
| Testomat.io | test-management | True (≤3 users) | False | high | very high | Stwórz projekt, importuj testy automatyczne z repo, dodaj manualne. |
| Xray | test-management | False | False | high | high | Porównaj z Zephyr, Qase, TestRail i Kiwi TCMS. |
| Kiwi TCMS | test-management | True (self-host) | False | high | medium-high | Postaw demo w Dockerze i sprawdź workflow test case → test run → report. |
| TestLink | test-management | True (self-host) | False | medium | low-medium | Najpierw porównaj z Kiwi TCMS, bo Kiwi zwykle będzie lepszym startem. |

## Web Automation

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| Playwright | web-automation | True | True | high | very high | Zacznij od Playwright Codegen i testów w TypeScript. |
| Playwright MCP | ai-for-testing | True | False | high | high | Połącz z Claude/Cursor/innym klientem MCP i zacznij od panelu testowego. |

## AI dla QA

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| MaestroGPT | ai-for-testing | True | False | very high | high | Opisz test po polsku, przejrzyj wygenerowany YAML, uruchom. |
| Testsigma | ai-for-testing | True (plan) | False | high | very high | Połącz z Jirą, wygeneruj TC ze sprintu, review i uruchom. |
| Ollama | ai-for-testing | True | False | high | medium | Pobierz model llama3 lub mistral i wklej logi z crasha do bezpiecznej analizy. |
| LM Studio | ai-for-testing | True | False | high | medium | Pobierz model przez GUI, wklej logi lub wymagania i zacznij rozmowę offline. |
| GitHub Copilot | ai-for-testing | False | False | high | very high | Używaj go z checklistą bezpieczeństwa: nie akceptuj kodu bez zrozumienia. |
| Continue.dev | ai-for-testing | True | False | medium-high | high | Połącz z modelem Qwen/Coder przez Ollama i zacznij od generowania testów pomocniczych. |
| Roo Code / Cline | ai-for-testing | True | True | medium | very high | Zacznij od małego zadania: dodać jeden test, nie refaktor całego projektu. |
| Browser Use | ai-for-testing | True | True | medium-high | high | Stosuj do paneli admina, nie jako zamiennik stabilnej regresji. |

## Debugging & Monitoring

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| Sentry | debugging | True (plan) | False | high | medium | Połącz eventy z wersją aplikacji i zgłoszeniami w Jira. |
| Allure Report | automation-reporting | True | True | medium | very high | Dodaj do Playwright/Appium/pytest/JUnit. |
