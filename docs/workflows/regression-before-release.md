# Workflow: regresja przed releasem

## Cel

W ograniczonym czasie (20-60 min) ocenić, czy nowa wersja aplikacji nie zepsuła krytycznych funkcji. Nie jest to pełna regresja — to ukierunkowany smoke test oparty na ryzyku.

## Kiedy używać

Przed każdym releasem: przed wysłaniem buildu do review, przed publikacją w sklepie, przed deployem na staging/production.

## Dane wejściowe

- identyfikator buildu i środowisko,
- changelog oraz zakres zmian,
- lista naprawionych błędów i znanych ryzyk,
- urządzenia i konta testowe,
- osoba odpowiedzialna za decyzję go/no-go.

## Narzędzia

- Urządzenie fizyczne lub emulator
- [scrcpy](../tools/mobile/scrcpy.md) — nagranie przebiegu
- [ADB](../tools/mobile/adb.md) — instalacja i weryfikacja buildu
- [Checklista release](../checklists/release-checklist.md)
- [Jira](../tools/test-management/jira.md) lub inny system zgłoszeń
- [Ollama](../tools/ai/ollama.md) — opcjonalna, lokalna analiza zanonimizowanych logów

---

## Kroki

### Krok 1 — Przygotowanie (5 min)

Wybierz i zapisz typ instalacji. `adb install -r` zachowuje dane aplikacji, dlatego nie jest testem fresh install.

```powershell
$packageName = "com.example.app"

# Scenariusz A: upgrade z zachowaniem danych
adb install -r app-new-version.apk

# Scenariusz B: fresh install — usuwa lokalne dane aplikacji
adb uninstall $packageName
adb install app-new-version.apk

# Sprawdź wersję
adb shell dumpsys package $packageName | Select-String versionName
```

- Nie wykonuj `adb uninstall` na urządzeniu z potrzebnymi danymi bez kopii lub zgody właściciela.
- Dla fresh install użyj czystego konta testowego; dla upgrade zachowaj przygotowany stan z poprzedniej wersji.
- Sprawdź changelog/diff — co się zmieniło? To najwyższe ryzyko.
- Zapisz build ID, środowisko, urządzenie, konto testowe i zakres testu.

### Krok 2 — Priorytety (co testować NAJPIERW)

1. **Zmienione obszary** (z changelog) — najwyższe ryzyko regresji
2. **Krytyczne ścieżki** (login, płatność, główna funkcja)
3. **Integracje** (API, powiadomienia, deep links)
4. **Fixes z poprzedniego sprintu** — czy bugi są naprawione?

### Krok 3 — Smoke test (15-30 min)

Przejdź [checklistę release](../checklists/release-checklist.md).

Minimalne kroki:

- [ ] Instalacja aplikacji (fresh install)
- [ ] Upgrade z poprzedniej wspieranej wersji, jeśli dotyczy
- [ ] Logowanie / rejestracja
- [ ] Główna funkcja (happy path)
- [ ] Kluczowe funkcje wymienione w changelog
- [ ] Wylogowanie
- [ ] Podstawowy test offline (wyłącz WiFi)

### Krok 4 — Decyzja

| Wynik | Decyzja |
| --- | --- |
| Zakres wykonany, brak nieakceptowalnego ryzyka | ✅ Rekomenduj release |
| Niepełny zakres lub niepotwierdzone ryzyko | ⚠️ Decyzja warunkowa — opisz brakujące dowody |
| Crash, utrata danych, luka bezpieczeństwa lub niedostępna krytyczna ścieżka | 🛑 Rekomenduj blokadę release |
| Pozostałe błędy | 📝 Oceń wpływ biznesowy; sama etykieta severity nie rozstrzyga decyzji |

Ostateczną decyzję podejmuje wskazany właściciel release na podstawie dowodów i zaakceptowanego ryzyka.

### Krok 5 — Dokumentacja

- Dołącz do zgłoszenia release: build ID, środowisko, zakres, urządzenia, wynik, znalezione błędy i pominięte testy.
- Połącz wszystkie istotne błędy ze zgłoszeniem release.
- Zapisz rekomendację QA, decyzję właściciela release, osobę i timestamp.

---

## Zasada minimalizmu

20 minut dobrego smoke testu > 2 godziny chaotycznego klikania.

Sprawdzaj to, co się zmieniło + to, co najważniejsze.

## Wynik i kryteria zakończenia

Workflow kończy się udokumentowaną rekomendacją QA oraz decyzją go/no-go. Raport wskazuje wykonany i pominięty zakres, dowody, otwarte ryzyka oraz właściciela decyzji.

## Prywatność i bezpieczeństwo

- Używaj wyłącznie kont i danych testowych.
- Nie publikuj logów, nagrań ani screenshotów zawierających dane osobowe lub produkcyjne.
- Analizę AI wykonuj lokalnie po anonimizacji materiału.
- Artefakty release przechowuj zgodnie z polityką retencji projektu.

## Powiązane materiały

- [Checklista release](../checklists/release-checklist.md)
- [Analiza błędu w aplikacji mobilnej](bug-investigation-mobile.md)
- [Analiza crasha Android](crash-analysis-android.md)
