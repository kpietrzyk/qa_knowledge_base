# ADB (Android Debug Bridge)

## Kategoria

- Główna kategoria: `mobile-testing`
- Podkategoria: `debugging`
- Darmowe: `True`
- Poziom trudności: `medium`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `high`
- Wymaga kodowania: `False`

## Do czego służy

Narzędzie wiersza poleceń do komunikacji z urządzeniem Android przez USB lub WiFi. Pozwala zbierać logi, nagrywać ekran, instalować APK i pobierać dane diagnostyczne — wszystko, czego potrzebujesz do technicznego udokumentowania błędu.

## Najlepsze zastosowania

- zbieranie logcat (logi aplikacji i systemu Android)
- nagrywanie ekranu do bug reportu
- instalacja i odinstalowanie APK
- zrzuty ekranu z terminala
- pobieranie pełnych raportów diagnostycznych
- symulacja akcji systemowych (force-stop, intencje)

## Kiedy używać

Używaj ADB zawsze, gdy musisz zebrać techniczne dowody błędu w aplikacji Android: logi z momentu crasha, nagranie kroków reprodukcji, stan urządzenia. ADB to różnica między "aplikacja się zamknęła" a "FATAL EXCEPTION w LoginActivity.java:45 — NullPointerException".

## Kiedy NIE używać

- Do testowania iOS — iOS ma własne narzędzia (Xcode, idevicesyslog)
- Jako jedynego narzędzia do proxy/inspekcji sieci — do tego użyj mitmproxy lub HTTP Toolkit
- Gdy potrzebujesz GUI — użyj Android Studio Logcat lub scrcpy

## Instalacja

ADB jest częścią **Android SDK Platform Tools**:
1. Pobierz ze strony: https://developer.android.com/tools/releases/platform-tools
2. Lub przez Android Studio: SDK Manager → SDK Tools → Android SDK Platform Tools
3. Dodaj do PATH (opcjonalnie, ale wygodne)
4. Na telefonie: Ustawienia → O telefonie → kliknij 7x "Numer kompilacji" → USB Debugging → ON

Weryfikacja: `adb devices` — powinien pokazać podłączone urządzenie.

## Workflow: zebranie dowodów do bug reportu

```bash
# Krok 1 — upewnij się, że urządzenie jest widoczne
adb devices

# Krok 2 — wyczyść stare logi (przed reprodukcją błędu!)
adb logcat -c

# Krok 3 — uruchom nagrywanie ekranu
adb shell screenrecord /sdcard/bug-$(date +%Y%m%d-%H%M%S).mp4

# Krok 4 — odtwórz błąd na telefonie (CTRL+C zatrzymuje nagranie po max 3 min)

# Krok 5 — zapisz logi natychmiast po błędzie
adb logcat -d > bug-log-$(date +%Y%m%d-%H%M%S).txt

# Krok 6 — pobierz nagranie na komputer
adb pull /sdcard/bug-*.mp4 .

# Krok 7 — zrób screenshot stanu ekranu
adb shell screencap /sdcard/screen.png && adb pull /sdcard/screen.png .
```

**Do Jiry dołącz:** nagranie MP4 + plik log (tylko istotny fragment) + screenshot + wersję apki + model urządzenia.

## Cheat Sheet — 15 komend, które tester powinien znać

```bash
# === URZĄDZENIA ===
adb devices                                      # lista podłączonych urządzeń
adb -s DEVICE_ID shell                           # połącz z konkretnym urządzeniem

# === LOGI ===
adb logcat                                       # logi na żywo (CTRL+C = stop)
adb logcat -c                                    # wyczyść bufor logów
adb logcat -d > log.txt                          # zapisz aktualne logi do pliku
adb logcat *:E                                   # tylko błędy (Error level)
adb logcat | grep "com.twoja.aplikacja"          # filtruj po nazwie pakietu

# === NAGRYWANIE I SCREENSHOTY ===
adb shell screenrecord /sdcard/bug.mp4           # nagraj ekran (max 3 min)
adb shell screencap /sdcard/screen.png           # zrzut ekranu
adb pull /sdcard/bug.mp4 .                       # pobierz plik na komputer
adb pull /sdcard/screen.png .                    # pobierz screenshot

# === APLIKACJE ===
adb install app-debug.apk                        # instalacja nowego APK
adb install -r app-debug.apk                     # reinstalacja (zachowaj dane)
adb uninstall com.example.app                    # odinstalowanie
adb shell am force-stop com.example.app          # wymuś zamknięcie aplikacji
adb shell pm clear com.example.app               # wyczyść dane aplikacji (reset stanu)

# === INFORMACJE O URZĄDZENIU ===
adb shell getprop ro.build.version.release       # wersja Android
adb shell getprop ro.build.version.sdk           # API level (np. 33 = Android 13)
adb shell getprop ro.product.model               # model urządzenia
adb shell dumpsys package com.example.app | grep versionName  # wersja apki
adb bugreport bugreport.zip                      # pełny raport diagnostyczny
```

## Jak odczytać logcat przy crashu

Szukaj tych słów kluczowych:
```
FATAL EXCEPTION   ← crash apki
ANR in            ← aplikacja nie odpowiada (App Not Responding)
E/AndroidRuntime  ← wyjątek runtime
NullPointerException, OutOfMemoryError, NetworkOnMainThreadException
```

Przykład fragmentu do skopiowania do ticketu:
```
E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.example.app, PID: 12345
    java.lang.NullPointerException: Attempt to invoke...
        at com.example.app.LoginActivity.onCreate(LoginActivity.java:45)
```
Tylko te kilka linii — nie cały log.

## Następny krok

Połącz ADB ze scrcpy dla wygodnego nagrywania ekranu. Następnie naucz się mitmproxy lub HTTP Toolkit, żeby zbierać jednocześnie logi Android I requesty sieciowe.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — ADB jest częścią Android SDK, licencja Google.
- Wymagane włączenie USB Debugging na telefonie — pamiętaj, żeby wyłączyć po testach.
- ADB przez WiFi (`adb connect IP:5555`) jest wolniejszy i mniej stabilny niż USB.
- Logcat zapisuje ograniczoną historię — zawsze czyść logcat PRZED reprodukcją buga.

## Link

https://developer.android.com/tools/adb

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia ADB praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. Jak zebrać logi do bug reportu (krok po kroku),
2. Jak nagrać ekran i pobrać plik na komputer,
3. Jak zainstalować nową wersję APK i wyczyścić dane,
4. Jak odczytać FATAL EXCEPTION w logcacie i co skopiować do Jiry,
5. Jakie informacje o urządzeniu dołączyć do każdego bug reportu,
6. Jak połączyć ADB z automatyzacją (Maestro, Appium).
```
