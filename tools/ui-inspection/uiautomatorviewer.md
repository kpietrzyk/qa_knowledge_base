# uiautomatorviewer

## Kategoria

- Główna kategoria: `ui-inspection`
- Podkategoria: `element-inspection`
- Darmowe: `True`
- Poziom trudności: `medium`
- Wartość dla manualnego testera: `medium-high`
- Wartość dla automatyzacji: `high`
- Wymaga kodowania: `False`

## Do czego służy

uiautomatorviewer robi zrzut ekranu działającej aplikacji Android i pokazuje hierarchię elementów UI wraz z ich atrybutami (resource-id, content-desc, xpath) — tester może znaleźć selektory potrzebne do skryptów Appium lub Maestro bez pisania kodu.

## Najlepsze zastosowania

- Znajdowanie resource-id i content-desc elementów do selektorów automatyzacji (Appium, Maestro)
- Weryfikacja czy elementy mają unikalne i sensowne identyfikatory
- Inspekcja hierarchii widoków w celu zrozumienia struktury ekranu
- Dokumentowanie brakujących lub niepoprawnych atrybutów a11y (content-desc) dla developera

## Kiedy używać

Używaj tego narzędzia wtedy, gdy zaczynasz przygodę z automatyzacją testów Android i potrzebujesz znaleźć selektory elementów (resource-id, xpath) dla swoich pierwszych skryptów Appium lub Maestro — albo gdy chcesz sprawdzić, czy developer nadał elementom sensowne identyfikatory ułatwiające automatyzację.

## Pierwszy praktyczny workflow

1. Upewnij się, że masz zainstalowany Android SDK — uiautomatorviewer jest w folderze `tools/` lub `tools/bin/`.
2. Podłącz urządzenie Android przez USB z włączonym debugowaniem USB lub uruchom emulator.
3. Przejdź do ekranu aplikacji, który chcesz zbadać.
4. W terminalu uruchom: `uiautomatorviewer` (ścieżka: `$ANDROID_HOME/tools/bin/uiautomatorviewer`).
5. Kliknij ikonę "Device Screenshot" (aparat) — zrzut załaduje hierarchię; kliknij element by zobaczyć jego resource-id, content-desc i bounds.

## Następny krok

uiautomatorviewer jest starszym narzędziem — naucz się używać nowszego Layout Inspector w Android Studio lub narzędzia `uiautomator dump` przez ADB, które generuje XML hierarchii bezpośrednio z wiersza poleceń.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- uiautomatorviewer jest narzędziem przestarzałym (legacy) — Google zaleca używanie Layout Inspector lub Appium Inspector jako alternatyw.
- Narzędzie działa tylko z Androidem — do iOS użyj Appium Inspector lub Accessibility Inspector w Xcode.
- Selektory xpath wygenerowane przez to narzędzie mogą być kruche — preferuj resource-id gdy dostępne.

## Link

https://developer.android.com/training/testing/other-components/ui-automator

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia uiautomatorviewer praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
