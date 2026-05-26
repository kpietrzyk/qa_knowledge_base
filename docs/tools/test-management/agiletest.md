# AgileTest

## Kategoria

- Główna kategoria: `test-management`
- Podkategoria: `jira-native-tms`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Zarządzanie testami bezpośrednio wewnątrz Jiry — przypadki testowe połączone z historyjkami, przebiegi testowe powiązane ze sprintami, bez przełączania się między narzędziami.

## Najlepsze zastosowania

- tworzenie przypadków testowych bezpośrednio na poziomie historyjki Jira
- przebiegi testowe synchronizowane z tablicą sprintu
- automatyczne tworzenie bugów w Jira z nieudanego przypadku testowego z pełnym linkiem do testu
- śledzenie pokrycia wymagań testami w jednym projekcie Jira
- raporty wykonania testów widoczne w tym samym miejscu co backlog

## Kiedy używać

Używaj tego narzędzia wtedy, gdy cały zespół pracuje w Jirze i nie chcesz wprowadzać kolejnego osobnego narzędzia — AgileTest eliminuje przełączanie kontekstu między TMS a trackerem błędów.

## Pierwszy praktyczny workflow

1. Zainstaluj AgileTest z Atlassian Marketplace na swoim projekcie Jira (wersja Cloud lub Server).
2. Otwórz dowolną historyjkę użytkownika w Jira > kliknij zakładkę `Tests` w panelu bocznym.
3. Kliknij `Create Test Case` > wypełnij kroki i oczekiwany rezultat powiązany z historyjką.
4. Utwórz `Test Cycle` w menu AgileTest > dodaj powiązane przypadki testowe > przypisz do bieżącego sprintu.
5. Wykonaj przebiegi testowe > oznaczaj wyniki > przy błędzie kliknij `Create Bug` — Jira tworzy ticket automatycznie z linkiem do nieudanego testu.

## Następny krok

Gdy zespół urośnie lub potrzeba zaawansowanych raportów, porównaj z Xray — ma więcej funkcji (testy BDD, Gherkin, zaawansowane raportowanie), ale kosztuje więcej. AgileTest jest lepszym startem dla małych zespołów.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — plan darmowy do 10 użytkowników jest bardzo hojny, ale sprawdź aktualne warunki na Atlassian Marketplace.
- Silne uzależnienie od Jiry — migracja do innego TMS w przyszłości może być trudna.

## Link

https://marketplace.atlassian.com/apps/1222095/agiletest-test-management-for-jira

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia AgileTest praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
