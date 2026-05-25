# Comparison table

| Narzędzie | Kategoria | Darmowe | Kodowanie | Wartość manual QA | Wartość automatyzacji | Pierwszy sensowny krok |
|---|---|---:|---:|---|---|---|
| Android Studio / Emulator | mobile-testing | True | False | very high | medium | Połącz z ADB, Appium, Maestro albo Firebase Test Lab. |
| ADB | mobile-testing | True | False | very high | high | Naucz się komend: adb devices, adb install, adb logcat, adb shell, adb bugreport. |
| scrcpy | mobile-testing | True | False | high | low | Połącz z ADB, narzędziami do nagrywania i checklistą bug reportu. |
| Appium | mobile-automation | True | True | high | very high | Zacznij od prostych testów w Pythonie albo Javie, potem dodaj Page Object i Allure. |
| Appium MCP | ai-for-testing | True | True | medium-high | high | Uruchom lokalnie, połącz z emulatorem i testuj generowanie kroków na prostych ekranach. |
| Maestro | mobile-automation | True | False | very high | high | Napisz pierwsze flow YAML: launchApp, tapOn, inputText, assertVisible. |
| Playwright | web-automation | True | True | high | very high | Zacznij od Playwright Codegen i testów w TypeScript. |
| Playwright MCP | ai-for-testing | True | False | high | high | Połącz z Claude/Cursor/innym klientem MCP i zacznij od panelu testowego. |
| Browser Use | ai-for-testing | True | True | medium-high | high | Stosuj do paneli admina i procesów okołomobilnych, nie jako zamiennik stabilnej regresji. |
| Postman | api-testing | True | False | very high | high | Dodaj testy w zakładce Tests i uruchamiaj kolekcje w Newman. |
| Bruno | api-testing | True | False | high | medium-high | Utwórz kolekcje dla logowania, profilu, zamówień i krytycznych endpointów. |
| Hoppscotch | api-testing | True | False | medium-high | medium | Porównaj z Bruno/Postman pod kątem pracy zespołowej. |
| mitmproxy | debugging | True | False | high | medium | Skonfiguruj proxy na telefonie i zainstaluj certyfikat testowy. |
| Charles Proxy | debugging | False | False | very high | medium | Jeżeli budżet zerowy, zacznij od mitmproxy. |
| Fiddler Everywhere | debugging | False | False | high | medium | Porównaj koszty z Charles i darmowym mitmproxy. |
| Firebase Crashlytics | mobile-testing | True | False | high | medium | Łącz zgłoszenia z Jira i wersjami buildów. |
| Firebase Test Lab | mobile-testing | False | False | medium-high | high | Uruchom smoke test na kilku popularnych modelach Android. |
| Jira | test-management | True | False | very high | medium | Ustandaryzuj szablon bug reportu i pola Severity/Priority. |
| Xray | test-management | False | False | high | high | Porównaj z Zephyr, Qase, TestRail i Kiwi TCMS. |
| Kiwi TCMS | test-management | True | False | high | medium-high | Postaw demo w Dockerze i sprawdź workflow test case → test run → report. |
| TestLink | test-management | True | False | medium | low-medium | Najpierw porównaj z Kiwi TCMS, bo Kiwi zwykle będzie lepszym startem. |
| Allure Report | automation-reporting | True | True | medium | very high | Dodaj do Playwright/Appium/pytest/JUnit. |
| Sentry | debugging | True | False | high | medium | Połącz eventy z wersją aplikacji i zgłoszeniami w Jira. |
| GitHub Copilot | ai-for-testing | False | False | high | very high | Używaj go z checklistą bezpieczeństwa: nie akceptuj kodu bez zrozumienia. |
| Continue.dev | ai-for-testing | True | False | medium-high | high | Połącz z modelem Qwen/Coder przez Ollama i zacznij od generowania testów jednostkowych pomocniczych. |
| Roo Code / Cline | ai-for-testing | True | True | medium | very high | Zacznij od małego zadania: dodać jeden test, nie refaktor całego projektu. |
