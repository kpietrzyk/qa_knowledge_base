# Testomat.io

## Kategoria

- Główna kategoria: `test-management`
- Podkategoria: `test-case-management`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `very high`
- Wymaga kodowania: `False`

## Do czego służy

Łączy zarządzanie testami manualnymi z wynikami automatyzacji w jednym miejscu — importuje istniejące testy Playwright, Appium i Cypress bezpośrednio z repozytorium, bez ręcznego przepisywania.

## Najlepsze zastosowania

- ujednolicone raporty z testów manualnych i automatycznych w jednym widoku
- automatyczny import przypadków testowych z kodu Playwright, Cypress, Appium
- planowanie i wykonywanie przebiegów testowych (manualnych i mieszanych)
- śledzenie pokrycia funkcjonalności testami na poziomie historyjek
- integracja z CI/CD w celu automatycznego importu wyników po każdym buildie

## Kiedy używać

Używaj tego narzędzia wtedy, gdy zespół ma już testy automatyczne (np. Playwright), ale wyniki giną w logach CI — Testomat.io zbiera je w czytelny raport dostępny dla całego zespołu, łącznie z testerami manualnymi.

## Pierwszy praktyczny workflow

1. Załóż konto na testomat.io > utwórz nowy projekt.
2. Napisz kilka manualnych przypadków testowych bezpośrednio w interfejsie zakładka `Tests`.
3. Podłącz repozytorium z testami automatycznymi: `Settings` > `Integrations` > wybierz framework (Playwright/Appium/Cypress).
4. Uruchom import — Testomat.io wczyta nazwy testów z kodu i wyświetli je obok manualnych.
5. Utwórz `Test Plan` łączący testy manualne i automatyczne > uruchom i sprawdź ujednolicony raport.

## Następny krok

Skonfiguruj reporter Testomat.io w pipeline CI/CD — po każdym buildie wyniki automatycznie trafią do projektu i będą widoczne razem z historią poprzednich przebiegów.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — plan darmowy ograniczony do 3 użytkowników.
- Największa wartość pojawia się dopiero przy integracji z istniejącą automatyzacją — dla czysto manualnych zespołów Qase może być prostszym wyborem na start.

## Link

https://testomat.io/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Testomat.io praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
