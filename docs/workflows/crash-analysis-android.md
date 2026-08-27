# Workflow: analiza crasha Android

## Cel

Zebrać kompletne dane techniczne po crashu lub ANR aplikacji Android i przygotować zgłoszenie, które można od razu wykorzystać do diagnozy.

## Kiedy używać

Gdy aplikacja Android nieoczekiwanie się zamknęła (crash) lub przestała reagować (ANR — Application Not Responding).

## Dane wejściowe

- wersja aplikacji i środowisko,
- urządzenie oraz wersja Androida,
- przybliżony czas zdarzenia,
- ostatnia wykonana akcja i dane testowe.

## Narzędzia

- [ADB](../tools/mobile/adb.md) — logcat i bugreport
- [Android Studio](../tools/mobile/android-studio-emulator.md) — Logcat w GUI
- [Firebase Crashlytics](../tools/mobile/firebase-crashlytics.md) — jeśli jest zatwierdzony i zintegrowany
- [Ollama](../tools/ai/ollama.md) — opcjonalna, lokalna analiza zanonimizowanych logów

---

## Kroki

### Krok 1 — Natychmiast po crashu

```powershell
$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'

# Zapisz logi (działaj szybko — logi są nadpisywane)
adb logcat -d | Out-File -Encoding utf8 "crash-$timestamp.txt"

# Lub zapisz bugreport (pełniejszy, ale większy plik)
adb bugreport "crash-bugreport-$timestamp.zip"
```

`bugreport` może zawierać dane użytkownika i konfigurację urządzenia. Zbieraj go tylko wtedy, gdy jest potrzebny, i przechowuj zgodnie z zasadami projektu.

### Krok 2 — Znajdź istotne linie

W pliku logcat szukaj:

- `FATAL EXCEPTION` — crash apki
- `ANR in com.yourapp` — zawieszenie
- `E/AndroidRuntime` — wyjątek runtime
- `W/System.err` — stack trace

Przykład stack trace do skopiowania do ticketu:

```text
E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.example.app, PID: 12345
    java.lang.NullPointerException: Attempt to invoke virtual method...
        at com.example.app.LoginActivity.onCreate(LoginActivity.java:45)
```

### Krok 3 — Analiza przez AI (bezpiecznie)

Po anonimizacji możesz użyć lokalnej Ollamy lub LM Studio:

```text
Oto fragment logcat z crashu aplikacji Android.
1. Co jest przyczyną błędu? (po ludzku, bez żargonu)
2. W którym miejscu kodu (plik, linia)?
3. Czy to błąd apki, systemu czy danych?
4. Co dołączyć do bug reportu?
Logi: [WKLEJ]
```

Nie wysyłaj logów aplikacji firmowej do usług chmurowych bez zatwierdzonej podstawy, konfiguracji retencji i zgody właściciela danych. Odpowiedź modelu jest hipotezą i wymaga potwierdzenia w stack trace lub kodzie.

### Krok 4 — Zebranie kontekstu

Do każdego crash reportu dodaj:

| Informacja | Jak zebrać |
| --- | --- |
| Wersja apki | Settings > About lub `adb shell dumpsys package com.app \| Select-String versionName` w PowerShell |
| Android version | `adb shell getprop ro.build.version.release` |
| Model urządzenia | `adb shell getprop ro.product.model` |
| Kroki do crasha | Twoje notatki lub nagranie scrcpy |
| Czy crash jest deterministyczny | Tak/Nie/Sporadycznie |

### Krok 5 — Zgłoszenie

**Tytuł:** `[CRASH] [Komponent] NullPointerException przy [akcji] [urządzenie/OS]`

**Dołącz:**

- [ ] Fragment logcata z `FATAL EXCEPTION` i stack trace (5-20 linii wokół błędu)
- [ ] Nagranie lub kroki do reprodukcji
- [ ] Wersja apki + urządzenie + OS
- [ ] Czy crash jest powtarzalny? Jak często?
- [ ] Timestamp i identyfikator zdarzenia z Crashlytics, jeśli jest dostępny
- [ ] Zanonimizowane dane wejściowe potrzebne do odtworzenia

---

## Rodzaje błędów Android — cheatsheet

| Błąd w logu | Co oznacza |
| --- | --- |
| `NullPointerException` | Kod próbuje użyć obiektu, który jest null |
| `OutOfMemoryError` | Brak pamięci — leak lub za duże dane |
| `NetworkOnMainThreadException` | Sieć na głównym wątku — błąd architektury |
| `ANR` | Aplikacja nie odpowiedziała w limicie właściwym dla danego typu ANR; input dispatch ma domyślnie 5 s na AOSP/Pixel, ale limity mogą różnić się zależnie od typu i OEM |
| `ClassCastException` | Zły typ danych — błąd w kodzie |
| `SecurityException` | Brakujące uprawnienie w manifeście |

Szczegóły typów i limitów: [oficjalna dokumentacja Android dotycząca ANR](https://developer.android.com/topic/performance/anrs/diagnose-and-fix-anrs).

## Wynik i kryteria zakończenia

Workflow jest zakończony, gdy zgłoszenie zawiera stack trace lub dowód ANR, timestamp, środowisko, kroki i informację o powtarzalności. Jeśli brakuje dowodu technicznego, zgłoszenie wskazuje brak i sposób jego zebrania.

## Prywatność i bezpieczeństwo

- Anonimizuj logi i bugreport przed udostępnieniem.
- Usuń tokeny, identyfikatory użytkownika, lokalizację, adresy i dane biznesowe.
- Ogranicz retencję dużych artefaktów i usuń je po zamknięciu analizy zgodnie z polityką projektu.
- Preferuj analizę lokalną; nie traktuj AI jako źródła prawdy.

## Powiązane materiały

- [Analiza błędu w aplikacji mobilnej](bug-investigation-mobile.md)
- [Szablon zgłoszenia błędu](../templates/bug-report-template.md)
- [Regresja przed releasem](regression-before-release.md)
