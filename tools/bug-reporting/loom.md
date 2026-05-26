# Loom

## Kategoria

- Główna kategoria: `bug-reporting`
- Podkategoria: `screen-recording`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `low`
- Wymaga kodowania: `False`

## Do czego służy

Loom nagrywa ekran z komentarzem głosowym i generuje link do wideo — zamiast pisać długi opis buga w Jirze, nagrywasz 2-minutowe wideo pokazujące problem z własnym wyjaśnieniem głosowym.

## Najlepsze zastosowania

- Dokumentowanie złożonych bugów wymagających narracji ("kliknij tutaj, potem tutaj, i wtedy...")
- Nagrania dla developerów, którzy mają trudność z odtworzeniem problemu
- Przekazywanie kontekstu biznesowego buga bez pisania ścian tekstu
- Raportowanie błędów UX i flow aplikacji mobilnej przez nagranie ekranu telefonu

## Kiedy używać

Używaj tego narzędzia wtedy, gdy bug jest trudny do opisania tekstem — wymaga pokazania sekwencji kroków, animacji lub zachowania aplikacji w czasie — i wolisz nagrać 90-sekundowe wideo z własnym komentarzem niż pisać 10-punktowy opis kroków reprodukcji.

## Pierwszy praktyczny workflow

1. Zarejestruj się na loom.com i zainstaluj aplikację desktopową lub rozszerzenie przeglądarki.
2. Kliknij ikonę Loom i wybierz tryb nagrania: ekran + kamera lub tylko ekran.
3. Odtwórz kroki prowadzące do buga, komentując głosem co robisz i czego oczekujesz.
4. Zatrzymaj nagranie — Loom automatycznie wygeneruje link do wideo.
5. Wklej link do opisu ticketu w Jirze jako "Video evidence" zamiast lub obok opisu tekstowego.

## Następny krok

Naucz się przycinać nagrania w edytorze Loom, by usuwać ciszę na początku i końcu — krótsze wideo = developer szybciej obejrzy cały dowód.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Darmowy plan ogranicza liczbę nagrań do 25 — przy intensywnym testowaniu szybko wyczerpiesz limit.
- Loom nie zbiera automatycznie logów ani danych sieciowych — to tylko nagranie wideo z głosem.
- Wideo z danymi użytkowników musi być udostępniane wyłącznie wewnętrznie.

## Link

https://www.loom.com

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Loom praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
