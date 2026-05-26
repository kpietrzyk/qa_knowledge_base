# Xcode Simulator

## Kategoria

- Główna kategoria: `mobile-testing`
- Podkategoria: `ios-simulator`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Testowanie aplikacji iOS na różnych modelach iPhone i iPad, wersjach systemu, ustawieniach Dynamic Type i układach z notchem lub Dynamic Island — bez potrzeby posiadania fizycznych urządzeń.

## Najlepsze zastosowania

- testowanie layoutu na różnych rozmiarach ekranu (iPhone SE, iPhone 15 Pro Max, iPad)
- symulacja lokalizacji GPS (trasa, konkretne współrzędne)
- testowanie dostępności (Dynamic Type, Voice Over preview)
- sprawdzanie różnych wersji iOS bez kupowania starych urządzeń
- szybkie zrzuty ekranu do bug reportów

## Kiedy używać

Używaj tego narzędzia wtedy, gdy chcesz sprawdzić zachowanie aplikacji iOS na konkretnym modelu lub wersji systemu, a nie masz dostępu do fizycznego urządzenia — albo gdy szybko zmieniasz rozmiar ekranu, żeby złapać błędy layoutu.

## Pierwszy praktyczny workflow

1. Otwórz Xcode > menu `Xcode` > `Open Developer Tool` > `Simulator`.
2. Wybierz urządzenie: `File` > `Open Simulator` > wskaż iPhone lub iPad z listy.
3. Uruchom aplikację: przeciągnij plik `.app` na okno Simulatora lub użyj `xcrun simctl install booted app.app`.
4. Zmień model w locie: `File` > `New Simulator` lub skrótem `Cmd+Shift+1..9`.
5. Zrób zrzut ekranu: `Cmd+S` — plik trafia automatycznie na pulpit.

## Następny krok

Połącz Simulator z Xcode Accessibility Inspector (`Xcode` > `Open Developer Tool` > `Accessibility Inspector`), żeby badać kontrast, etykiety VoiceOver i hierarchię elementów bez wychodzenia z macOS.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Simulator nie emuluje sensora TouchID/FaceID ani kamery — do tych testów potrzebne jest fizyczne urządzenie.
- Działa tylko na macOS z zainstalowanym Xcode — niedostępny na Windows i Linux.

## Link

https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Xcode Simulator praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
