# Appium Inspector

## Kategoria

- Główna kategoria: `mobile-automation`
- Podkategoria: `element-inspector`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `very high`
- Wymaga kodowania: `False`

## Do czego służy

Wizualny interfejs graficzny do znajdowania selektorów elementów (resource-id, xpath, accessibility id) w działającej aplikacji mobilnej — pomost między testowaniem manualnym a automatyzacją.

## Najlepsze zastosowania

- znajdowanie selektorów elementów UI do skryptów Appium i przepływów Maestro
- wizualna eksploracja hierarchii elementów aplikacji
- weryfikacja atrybutów dostępności (accessibility id, content-desc)
- debugowanie testów automatycznych gdy selektor przestał działać
- nauka struktury aplikacji przed napisaniem pierwszego testu

## Kiedy używać

Używaj tego narzędzia wtedy, gdy zaczynasz pisać testy automatyczne i potrzebujesz znaleźć poprawny selektor elementu, albo gdy istniejący test przestał działać i chcesz sprawdzić czy element zmienił swój identyfikator w nowej wersji aplikacji.

## Pierwszy praktyczny workflow

1. Zainstaluj Appium Server: `npm install -g appium` oraz sterownik `appium driver install uiautomator2` (Android) lub `appium driver install xcuitest` (iOS).
2. Uruchom Appium Server: `appium` w terminalu — serwer startuje domyślnie na `http://localhost:4723`.
3. Pobierz i zainstaluj Appium Inspector z github.com/appium/appium-inspector.
4. W Appium Inspector wpisz adres serwera (`http://localhost:4723`) i `Desired Capabilities` (platformName, deviceName, app).
5. Kliknij `Start Session` > kliknij element w podglądzie zrzutu ekranu > skopiuj `resource-id` lub `accessibility id` do skryptu testowego.

## Następny krok

Użyj znalezionych selektorów w skryptach Appium (Python/JavaScript) lub przepływach Maestro YAML — Appium Inspector to punkt wejścia, który usuwa największą barierę wejścia do automatyzacji mobilnej.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Appium Inspector wymaga działającego serwera Appium — to oddzielna aplikacja, nie samodzielne narzędzie.

## Link

https://github.com/appium/appium-inspector

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Appium Inspector praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
