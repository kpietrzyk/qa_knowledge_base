# Jam

## Kategoria

- Główna kategoria: `bug-reporting`
- Podkategoria: `screen-recording`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `low`
- Wymaga kodowania: `False`

## Do czego służy

Jam pozwala jednym kliknięciem nagrać bug report zawierający wideo, logi konsoli, requesty sieciowe i dane urządzenia — bez żadnej konfiguracji. Wynik trafia bezpośrednio do Jiry lub Slacka jako gotowy ticket.

## Najlepsze zastosowania

- Natychmiastowy bug report z wideo + logami bez przełączania okien
- Dołączanie network trace do raportu bez otwierania DevTools
- Tworzenie ticketów w Jirze z pełnym kontekstem technicznym jednym klikiem
- Dokumentowanie kroków reprodukcji dla błędów wizualnych w aplikacjach mobilnych (przez przeglądarkę)

## Kiedy używać

Używaj tego narzędzia wtedy, gdy znajdziesz buga i chcesz natychmiast zebrać wszystkie dowody techniczne bez ręcznego kopiowania logów, nagrywania osobno ekranu i opisywania kroków — Jam robi to wszystko jednocześnie w jednym kliknięciu.

## Pierwszy praktyczny workflow

1. Zainstaluj rozszerzenie Jam do Chrome/Edge ze strony jam.dev.
2. Połącz konto z Jirą lub Slackiem w ustawieniach rozszerzenia.
3. Odtwórz buga w przeglądarce, a następnie kliknij ikonę Jam na pasku narzędzi.
4. Zatrzymaj nagranie — Jam automatycznie dołącza logi konsoli i requesty sieciowe.
5. Uzupełnij tytuł i opis, wybierz projekt Jira i wyślij gotowy ticket.

## Następny krok

Naucz się filtrować logi konsoli w nagraniu Jama, by w bug reporcie pokazać tylko błędy (czerwone linie) zamiast całego szumu.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Jam działa w przeglądarce — nie nagrywa natywnych aplikacji mobilnych (tylko web/PWA).
- Darmowy plan ma limit nagrań miesięcznie — sprawdź aktualne limity na stronie.
- Nie wklejaj ekranów z danymi wrażliwymi użytkowników bez anonimizacji.

## Link

https://jam.dev

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Jam praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
