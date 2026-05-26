# Workflow: analiza crasha Android

## Cel

Zebrać kompletne dane techniczne po crashu aplikacji Android i zgłosić buga z stack trace, który developer może od razu użyć do debugowania.

## Kiedy używać

Gdy aplikacja Android nieoczekiwanie się zamknęła (crash) lub przestała reagować (ANR — Application Not Responding).

## Narzędzia

- ADB (logcat, bugreport)
- Android Studio (Logcat w GUI)
- Firebase Crashlytics (jeśli zintegrowane)
- AI (analiza logów)

---

## Kroki

### Krok 1 — Natychmiast po crashu

```bash
# Zapisz logi (działaj szybko — logi są nadpisywane)
adb logcat -d > crash-$(date +%Y%m%d-%H%M%S).txt

# Lub zapisz bugreport (pełniejszy, ale większy plik)
adb bugreport crash-bugreport.zip
```

### Krok 2 — Znajdź istotne linie

W pliku logcat szukaj:
- `FATAL EXCEPTION` — crash apki
- `ANR in com.yourapp` — zawieszenie
- `E/AndroidRuntime` — wyjątek runtime
- `W/System.err` — stack trace

Przykład stack trace do skopiowania do ticketu:
```
E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.example.app, PID: 12345
    java.lang.NullPointerException: Attempt to invoke virtual method...
        at com.example.app.LoginActivity.onCreate(LoginActivity.java:45)
```

### Krok 3 — Analiza przez AI (bezpiecznie)

Jeśli dane są firmowe → użyj **Ollamy lub LM Studio** (lokalnie):
```
Oto fragment logcat z crashu aplikacji Android.
1. Co jest przyczyną błędu? (po ludzku, bez żargonu)
2. W którym miejscu kodu (plik, linia)?
3. Czy to błąd apki, systemu czy danych?
4. Co dołączyć do bug reportu?
Logi: [WKLEJ]
```

Jeśli dane nie są poufne → możesz użyć Claude/ChatGPT.

### Krok 4 — Zebranie kontekstu

Do każdego crash reportu dodaj:

| Informacja | Jak zebrać |
|---|---|
| Wersja apki | Settings > About lub `adb shell dumpsys package com.app \| grep versionName` |
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

---

## Rodzaje błędów Android — cheatsheet

| Błąd w logu | Co oznacza |
|---|---|
| `NullPointerException` | Kod próbuje użyć obiektu, który jest null |
| `OutOfMemoryError` | Brak pamięci — leak lub za duże dane |
| `NetworkOnMainThreadException` | Sieć na głównym wątku — błąd architektury |
| `ANR` | Operacja blokowała UI > 5 sekund |
| `ClassCastException` | Zły typ danych — błąd w kodzie |
| `SecurityException` | Brakujące uprawnienie w manifeście |
