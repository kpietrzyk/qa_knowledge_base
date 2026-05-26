# XCUITest

## Kategoria

- Główna kategoria: `mobile-automation`
- Podkategoria: `native-ios-automation`
- Darmowe: `True`
- Poziom trudności: `medium-hard`
- Wartość dla manualnego testera: `low`
- Wartość dla automatyzacji: `very high`
- Wymaga kodowania: `True`

## Do czego służy

Natywny framework Apple do testów UI aplikacji iOS — nagrywanie interakcji w Xcode i edycja kodu Swift, najszybsze i najbardziej wiarygodne testy iOS, ale wymaga dostępu do kodu i macOS.

## Najlepsze zastosowania

- testy regresji UI wbudowane w projekt Xcode obok kodu aplikacji
- weryfikacja przepływów nawigacji, formularzy i alertów na iOS
- testy integracyjne uruchamiane automatycznie przy każdym PR w CI/CD
- sprawdzanie zachowania aplikacji na różnych rozmiarach ekranu w Simulatorze
- testowanie gestów (swipe, pinch, long press) na poziomie kodu

## Kiedy używać

Używaj tego narzędzia wtedy, gdy jesteś testerem współpracującym z zespołem iOS w Xcode, masz dostęp do repozytorium Swift i chcesz pisać lub utrzymywać testy razem z deweloperami w tym samym projekcie.

## Pierwszy praktyczny workflow

1. Otwórz projekt w Xcode > sprawdź czy istnieje target `UITests` w nawigatorze projektu.
2. Otwórz plik testowy z sufiksem `UITests.swift` w folderze `UITests`.
3. W ciele funkcji testowej kliknij czerwony przycisk `Record` na dole ekranu Xcode.
4. Wykonaj kroki w Simulatorze — Xcode automatycznie generuje kod Swift dla każdej akcji.
5. Zatrzymaj nagrywanie > dodaj ręcznie asercję: `XCTAssertTrue(app.buttons["Zaloguj"].exists)` > uruchom test (`Cmd+U`).

## Następny krok

Dla testów iOS bez kodu Swift i bez dostępu do źródeł użyj Appium z driverem XCUITest — daje podobne możliwości w Pythonie lub JavaScript i nie wymaga otwierania Xcode przez każdego w zespole.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Wymaga macOS z Xcode i znajomości Swift — nie nadaje się dla testerów bez dostępu do kodu źródłowego iOS.

## Link

https://developer.apple.com/documentation/xctest

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia XCUITest praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
