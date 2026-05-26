# Prompty dla testera QA

Prompty są podzielone według zadań. Najlepiej używać ich razem z kontekstem:

- wymaganie,
- screen,
- log,
- request/response,
- aktualny bug report,
- fragment kodu,
- oczekiwane zachowanie.

## Pliki promptów

| Plik | Zawartość |
|---|---|
| `test-case-prompts.md` | Generowanie TC z US, smoke suite, dane testowe, ocena pod automatyzację |
| `bug-report-prompts.md` | Formatowanie raportu, analiza braków, tłumaczenie na język biznesowy |
| `mobile-testing-prompts.md` | Checklista mobilna, TC mobile, logcat, YAML Maestro, eksploracja |
| `exploratory-testing-prompts.md` | Charter sesji, heurystyki, analiza ryzyk, AI sparring partner |
| `api-testing-prompts.md` | Generowanie broken JSON, analiza request/response, dane testowe API |
| `qa-copilot-prompts.md` | Prompty do pracy z Copilotem i narzędziami AI w IDE |

## Ważna zasada

AI generuje drafty — tester weryfikuje, uzupełnia i akceptuje.
Nie wklejaj danych objętych NDA do publicznych modeli AI (ChatGPT, Claude). Do pracy z danymi firmowymi używaj lokalnych modeli: Ollama lub LM Studio.
