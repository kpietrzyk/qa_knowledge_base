# Katalon Studio

## Kategoria

- Główna kategoria: `mobile-automation`
- Podkategoria: `low-code-automation`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `medium-high`
- Wartość dla automatyzacji: `high`
- Wymaga kodowania: `False`

## Do czego służy

Nagrywanie i odtwarzanie testów automatycznych z interfejsem low-code — dobry pomost dla testerów manualnych, którzy chcą zacząć automatyzować bez pisania kodu od zera.

## Najlepsze zastosowania

- nagrywanie scenariuszy testowych i odtwarzanie ich bez kodowania
- inspekcja elementów mobilnych przez wbudowany Spy Mobile
- tworzenie zestawów regresyjnych dla aplikacji Android i iOS
- generowanie raportów HTML z wynikami testów
- integracja z Jira do automatycznego tworzenia bugów z failed testów

## Kiedy używać

Używaj tego narzędzia wtedy, gdy chcesz zacząć automatyzować testy mobilne, ale nie znasz jeszcze Javy ani Pythona — Katalon pozwala nagrać i uruchomić test w ciągu godziny bez pisania kodu.

## Pierwszy praktyczny workflow

1. Pobierz Katalon Studio z katalon.com i zainstaluj (Windows/macOS) — wymagane Java w tle, ale Katalon zarządza tym automatycznie.
2. Utwórz nowy projekt `Mobile` > podłącz telefon Android przez USB z włączonym debugowaniem USB.
3. Kliknij `Record Mobile` > wybierz urządzenie > aplikacja otwiera się automatycznie.
4. Wykonaj kroki testowe na urządzeniu — Katalon nagrywa każdą akcję jako krok w scenariuszu.
5. Zatrzymaj nagrywanie > dodaj asercję (`Verify Element Present` lub `Verify Text`) > uruchom test przyciskiem `Run`.

## Następny krok

Gdy opanujesz nagrywanie, przejdź do Appium dla większej elastyczności albo do Maestro dla prostszego podejścia opartego na YAML — oba dają więcej kontroli nad testami niż tryb nagrywania.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — plan darmowy ma ograniczenia funkcji i integracji.
- Testy nagrane bez zrozumienia selektorów są kruche — przy zmianach UI często wymagają ręcznej naprawy.

## Link

https://katalon.com/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Katalon Studio praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
