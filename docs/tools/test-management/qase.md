# Qase

## Kategoria

- Główna kategoria: `test-management`
- Podkategoria: `test-case-management`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `high`
- Wymaga kodowania: `False`

## Do czego służy

Nowoczesne chmurowe narzędzie do zarządzania przypadkami testowymi z czystym UI, integracją Jira i raportowaniem — najlepsza darmowa opcja dla małych zespołów QA (do 3 użytkowników).

## Najlepsze zastosowania

- tworzenie i organizowanie przypadków testowych w strukturze folderów
- planowanie i wykonywanie przebiegów testowych (test runs) z oznaczaniem pass/fail/skip
- tworzenie zgłoszeń błędów w Jira bezpośrednio z nieudanego przypadku testowego
- generowanie raportów wykonania testów dla zespołu i stakeholderów
- śledzenie historii wyników testów między wersjami aplikacji

## Kiedy używać

Używaj tego narzędzia wtedy, gdy potrzebujesz przejść od przypadków testowych w Excelu lub Confluence do dedykowanego narzędzia — Qase oferuje bezpłatny start dla małego zespołu z kompletną funkcjonalnością TMS.

## Pierwszy praktyczny workflow

1. Załóż konto na qase.io > utwórz nowy projekt (np. nazwa aplikacji mobilnej).
2. W zakładce `Test Cases` kliknij `+ Case` > wypełnij tytuł, opis, kroki i oczekiwany rezultat dla pierwszego przypadku.
3. Utwórz `Test Run` (zakładka `Test Runs`) > wybierz przypadki testowe do uruchomienia.
4. Wykonaj przebiegi ręcznie — oznaczaj każdy przypadek jako `Passed`, `Failed` lub `Skipped`.
5. Przy oznaczeniu `Failed` kliknij `Create defect` > jeśli Jira jest podłączona, błąd trafia automatycznie jako ticket z linkiem do przypadku testowego.

## Następny krok

Podłącz wyniki testów z Appium lub Playwright przez Qase API reporter — dzięki temu manualne i automatyczne wyniki będą widoczne razem w jednym raporcie.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — plan darmowy ograniczony do 3 użytkowników.
- Przypadki testowe bez regularnej aktualizacji szybko tracą wartość — zaplanuj czas na utrzymanie repozytorium testów.

## Link

https://qase.io/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Qase praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
