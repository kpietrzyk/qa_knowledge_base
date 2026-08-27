# Workflow: analiza błędu w aplikacji mobilnej

## Cel

Ustalić dokładnie, co się stało, zawęzić obszar przyczyny (UI/API/dane/sieć/urządzenie) i zebrać kompletne dowody techniczne do zgłoszenia.

## Kiedy używać

Gdy reprodukujesz błąd w aplikacji mobilnej i musisz go przeanalizować lub zgłosić.

## Dane wejściowe

- build i środowisko testowe,
- konto oraz kontrolowane dane testowe,
- opis obserwowanego zachowania,
- urządzenie fizyczne lub emulator.

## Narzędzia

- [scrcpy](../tools/mobile/scrcpy.md) — nagranie ekranu
- [ADB](../tools/mobile/adb.md) — logcat, screenshot i dane urządzenia
- [mitmproxy](../tools/debugging/mitmproxy.md), [HTTP Toolkit](../tools/api/http-toolkit.md) lub [Proxyman](../tools/debugging/proxyman.md) — analiza sieci
- [Jira](../tools/test-management/jira.md) lub inny system zgłoszeń
- [Ollama](../tools/ai/ollama.md) — opcjonalna, lokalna analiza logów

---

## Kroki

### Krok 1 — Przygotowanie

- [ ] Uruchom proxy (mitmproxy lub HTTP Toolkit) i podłącz telefon
- [ ] Zanotuj: wersję aplikacji, model urządzenia, wersję OS, sieć (WiFi/LTE)
- [ ] Wyczyść logi: `adb logcat -c`
- [ ] W PowerShell ustaw identyfikator sesji: `$sessionId = Get-Date -Format 'yyyyMMdd-HHmmss'`
- [ ] Uruchom nagrywanie: `scrcpy --record="bug-$sessionId.mp4"`

### Krok 2 — Reprodukcja błędu

- [ ] Odtwórz błąd dokładnie — krok po kroku
- [ ] Obserwuj jednocześnie: ekran + logi + proxy
- [ ] Zatrzymaj nagranie scrcpy po odtworzeniu

### Krok 3 — Zebranie dowodów

```powershell
# Zapisz logi z momentu błędu
adb logcat -d | Out-File -Encoding utf8 "bug-log-$sessionId.txt"

# Pobierz nagranie (jeśli użyto adb screenrecord)
adb pull /sdcard/bug.mp4 .

# Screenshot stanu ekranu
adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png .
```

Z proxy zapisz zanonimizowany request/response dla podejrzanego połączenia.

### Krok 4 — Analiza

Zadaj sobie pytania:

| Pytanie | Narzędzie |
| --- | --- |
| Czy błąd jest widoczny w logach? | logcat |
| Czy request wychodzi poprawnie? | proxy |
| Czy response serwera jest poprawny? | proxy |
| Czy błąd pojawia się na innym urządzeniu? | drugi telefon/emulator |
| Czy błąd jest w konkretnej wersji OS? | emulator z innym API level |

> Opcjonalnie przeanalizuj zanonimizowany fragment logcata lokalnie w Ollamie. Wynik AI jest hipotezą — potwierdź go dowodami przed zgłoszeniem.

### Krok 5 — Sformułowanie hipotezy

Przed utworzeniem zgłoszenia odpowiedz:

- **Co** się stało? (symptom)
- **Gdzie** prawdopodobnie leży przyczyna? (UI / API / Dane / Sieć / Urządzenie)
- **Kiedy** się pojawia? (zawsze / sporadycznie / na konkretnych urządzeniach)
- **Czego** brakuje do potwierdzenia hipotezy?

### Krok 6 — Zgłoszenie błędu

**Tytuł:** `[Komponent] [Zachowanie] [Kontekst]`

Przykład: `[Login] Aplikacja zamyka się po wpisaniu pustego hasła [Android 13, Pixel 6]`

**Minimalne dowody do załączenia:**

- [ ] Nagranie kroków (MP4 lub Loom)
- [ ] Screenshot stanu błędu (z adnotacjami Greenshot)
- [ ] Fragment logcata (tylko istotne linie, nie cały log)
- [ ] Zanonimizowany request/response, jeśli problem jest sieciowy
- [ ] Wersja apki, urządzenie, OS
- [ ] Oczekiwany i rzeczywisty rezultat
- [ ] Hipoteza wyraźnie oznaczona jako potwierdzona lub niepotwierdzona

---

## Typowe pułapki

- ❌ Zgłoszenie buga bez logów = "cannot reproduce" od developera
- ❌ Wklejenie całego logcata zamiast istotnego fragmentu
- ❌ Tytuł "aplikacja nie działa" zamiast konkretnego opisu
- ✅ Zawsze czyść logcat przed reprodukcją (`adb logcat -c`)

## Wynik i kryteria zakończenia

Workflow jest zakończony, gdy zgłoszenie zawiera powtarzalne kroki, środowisko, oczekiwany i rzeczywisty rezultat oraz minimalny zestaw zanonimizowanych dowodów. Jeśli przyczyna nie jest potwierdzona, zgłoszenie zawiera hipotezę i brakujący dowód.

## Prywatność i bezpieczeństwo

- Przechwytuj ruch wyłącznie w zatwierdzonym środowisku testowym i na kontrolowanym koncie.
- Usuń tokeny, cookies, klucze API, dane osobowe i firmowe identyfikatory przed dołączeniem logów lub requestów.
- Nie omijaj TLS pinningu ani zabezpieczeń aplikacji bez wyraźnej zgody właściciela systemu.
- Dla danych wewnętrznych używaj lokalnego modelu; nie wysyłaj pełnych logów do usług chmurowych.

## Powiązane materiały

- [Szablon zgłoszenia błędu](../templates/bug-report-template.md)
- [Analiza błędu API](bug-investigation-api.md)
- [Analiza crasha Android](crash-analysis-android.md)
