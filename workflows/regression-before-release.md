# Workflow: regresja przed releasem

## Cel

W ograniczonym czasie (20-60 min) potwierdzić, że nowa wersja aplikacji nie zepsuła krytycznych funkcji. Nie jest to pełna regresja — to targeted smoke test oparty o ryzyko.

## Kiedy używać

Przed każdym releasem: przed wysłaniem buildu do review, przed publikacją w sklepie, przed deployem na staging/production.

## Narzędzia

- Urządzenie fizyczne lub emulator
- scrcpy (nagranie przebiegu)
- ADB (instalacja buildu)
- Checklista: `checklists/release-checklist.md`
- Jira (zgłoszenie znalezionych bugów)
- AI (szybka analiza logów przy błędzie)

---

## Kroki

### Krok 1 — Przygotowanie (5 min)

```bash
# Zainstaluj nowy build
adb install -r app-new-version.apk

# Sprawdź wersję
adb shell dumpsys package com.example.app | grep versionName
```

- Wyczyść dane aplikacji lub użyj czystego konta testowego
- Sprawdź changelog/diff — co się zmieniło? To najwyższe ryzyko.

### Krok 2 — Priorytety (co testować NAJPIERW)

1. **Zmienione obszary** (z changelog) — najwyższe ryzyko regresji
2. **Krytyczne ścieżki** (login, płatność, główna funkcja)
3. **Integracje** (API, powiadomienia, deep links)
4. **Fixes z poprzedniego sprintu** — czy bugi są naprawione?

### Krok 3 — Smoke test (15-30 min)

Przejdź checklistę `checklists/release-checklist.md`.

Minimalne kroki:
- [ ] Instalacja aplikacji (fresh install)
- [ ] Logowanie / rejestracja
- [ ] Główna funkcja (happy path)
- [ ] Kluczowe funkcje wymienione w changelog
- [ ] Wylogowanie
- [ ] Podstawowy test offline (wyłącz WiFi)

### Krok 4 — Decyzja

| Wynik | Decyzja |
|---|---|
| Brak krytycznych błędów | ✅ Release możliwy |
| Bug High na nowej funkcji | ⚠️ Zależy od decyzji PM — opisz ryzyko |
| Bug Critical (crash, brak loginu) | 🛑 Blokuj release, zgłoś natychmiast |
| Bug Medium/Low | 📝 Zgłoś, nie blokuj release — decyzja PM |

### Krok 5 — Dokumentacja

- Dołącz do ticketu release: "Regresja wykonana, znaleziono X bugów, Y blokujących"
- Krytyczne bugi linkuj do release ticketu

---

## Zasada minimalizmu

20 minut dobrego smoke testu > 2 godziny chaotycznego klikania.
Sprawdzaj to, co się zmieniło + to, co najważniejsze.
