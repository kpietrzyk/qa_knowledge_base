# Instabug

## Kategoria

- Główna kategoria: `bug-reporting`
- Podkategoria: `in-app-reporting`
- Darmowe: `False`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Instabug to SDK wbudowany przez developerów w build testowy aplikacji mobilnej — tester potrząsa telefonem, wypełnia formularz i wysyła raport z automatycznie zebranym logiem urządzenia, śladem nawigacji, requestami sieciowymi i zrzutem ekranu.

## Najlepsze zastosowania

- Raportowanie bugów bezpośrednio z urządzenia mobilnego bez podłączania do komputera
- Automatyczne zbieranie logów, trace nawigacji i danych sieciowych przy każdym raporcie
- Testowanie w terenie — testerzy bez wiedzy technicznej mogą wysyłać kompletne raporty
- Zbieranie feedbacku od testerów beta z pełnym kontekstem technicznym

## Kiedy używać

Używaj tego narzędzia wtedy, gdy team developerski osadził SDK Instabug w buildzie testowym i chcesz raportować bug bezpośrednio z aplikacji mobilnej — potrząśnięcie telefonem uruchamia formularz raportu, który automatycznie zawiera wszystkie dane techniczne potrzebne do reprodukcji.

## Pierwszy praktyczny workflow

1. Upewnij się, że developer osadził SDK Instabug w buildzie testowym (QA/debug build).
2. Zainstaluj build testowy na swoim urządzeniu.
3. Odtwórz buga w aplikacji, a następnie potrząśnij telefonem lub użyj przycisku raportu.
4. Uzupełnij formularz: opis problemu, kroki reprodukcji, oczekiwany vs. rzeczywisty wynik.
5. Wyślij raport — Instabug automatycznie dołącza logi, sieć i nawigację do ticketu.

## Następny krok

Poproś developera o skonfigurowanie integracji Instabug z Jirą lub Linear — wtedy raporty trafiają bezpośrednio do backlogu bez pośrednictwa.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Instabug wymaga integracji po stronie developera — tester samodzielnie nie zainstaluje SDK.
- Dostępny tylko w dedykowanym buildzie testowym, nie w wersji produkcyjnej.
- Plan darmowy/trial ma ograniczenia — weryfikuj z zespołem przed wdrożeniem.

## Link

https://instabug.com

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Instabug praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
