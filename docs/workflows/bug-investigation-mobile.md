# Workflow: analiza błędu w aplikacji mobilnej

## Cel

Ustalić dokładnie: co się stało, gdzie leży przyczyna (UI/backend/dane/sieć/urządzenie) i zebrać kompletne dowody techniczne do ticketu Jira.

## Kiedy używać

Zawsze, gdy reprodukujesz buga w aplikacji mobilnej i musisz go zgłosić.

## Narzędzia

- scrcpy (nagranie ekranu)
- ADB (logcat, screenrecord)
- Proxy: mitmproxy / HTTP Toolkit / Proxyman (analiza sieci)
- Jira (ticket)
- ChatGPT/Claude lub Ollama (analiza logów)

---

## Kroki

### Krok 1 — Przygotowanie

- [ ] Wyczyść logi: `adb logcat -c`
- [ ] Uruchom nagrywanie scrcpy: `scrcpy --record bug-$(date +%Y%m%d-%H%M%S).mp4`
- [ ] Uruchom proxy (mitmproxy lub HTTP Toolkit) i podłącz telefon
- [ ] Zanotuj: wersję aplikacji, model urządzenia, wersję OS, sieć (WiFi/LTE)

### Krok 2 — Reprodukcja błędu

- [ ] Odtwórz błąd dokładnie — krok po kroku
- [ ] Obserwuj jednocześnie: ekran + logi + proxy
- [ ] Zatrzymaj nagranie scrcpy po odtworzeniu

### Krok 3 — Zebranie dowodów

```bash
# Zapisz logi z momentu błędu
adb logcat -d > bug-log-$(date +%Y%m%d-%H%M%S).txt

# Pobierz nagranie (jeśli użyto adb screenrecord)
adb pull /sdcard/bug.mp4 .

# Screenshot stanu ekranu
adb shell screencap /sdcard/screen.png && adb pull /sdcard/screen.png .
```

Z proxy: zapisz request/response dla podejrzanego połączenia.

### Krok 4 — Analiza

Zadaj sobie pytania:

| Pytanie | Narzędzie |
|---|---|
| Czy błąd jest widoczny w logach? | logcat |
| Czy request wychodzi poprawnie? | proxy |
| Czy response serwera jest poprawny? | proxy |
| Czy błąd pojawia się na innym urządzeniu? | drugi telefon/emulator |
| Czy błąd jest w konkretnej wersji OS? | emulator z innym API level |

> Użyj AI do analizy logów: wklej fragment logcata do Ollamy lub Claude i zapytaj "co jest przyczyną błędu i co dołączyć do bug reportu?"

### Krok 5 — Sformułowanie hipotezy

Zanim wpiszesz do Jiry, odpowiedz:
- **Co** się stało? (symptom)
- **Gdzie** leży przyczyna? (UI / Backend / Dane / Sieć / Urządzenie)
- **Kiedy** się pojawia? (zawsze / sporadycznie / na konkretnych urządzeniach)
- **Czego** brakuje do potwierdzenia hipotezy?

### Krok 6 — Zgłoszenie w Jira

**Tytuł:** [Komponent] [Zachowanie] [Kontekst]
Przykład: `[Login] Aplikacja zamyka się po wpisaniu pustego hasła [Android 13, Pixel 6]`

**Minimalne dowody do załączenia:**
- [ ] Nagranie kroków (MP4 lub Loom)
- [ ] Screenshot stanu błędu (z adnotacjami Greenshot)
- [ ] Fragment logcata (tylko istotne linie, nie cały log)
- [ ] Request/response jeśli problem sieciowy
- [ ] Wersja apki, urządzenie, OS

---

## Typowe pułapki

- ❌ Zgłoszenie buga bez logów = "cannot reproduce" od developera
- ❌ Wklejenie całego logcata zamiast istotnego fragmentu
- ❌ Tytuł "aplikacja nie działa" zamiast konkretnego opisu
- ✅ Zawsze czyść logcat przed reprodukcją (`adb logcat -c`)
