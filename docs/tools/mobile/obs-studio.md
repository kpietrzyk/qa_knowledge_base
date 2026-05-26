# OBS Studio

## Kategoria

- Główna kategoria: `mobile-testing`
- Podkategoria: `screen-recording`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `low`
- Wymaga kodowania: `False`

## Do czego służy

Profesjonalne nagrywanie sesji testowych z komentarzem głosowym i wieloma źródłami — ekran telefonu (przez scrcpy), notatki, kod w tle — idealne do demonstracji błędów dla PM lub dokumentacji eksploracyjnej.

## Najlepsze zastosowania

- nagrywanie sesji eksploracyjnych z komentarzem głosowym do dokumentacji
- demonstracja złożonych błędów dla PM z jednoczesnym widokiem telefonu i narzędzi
- rejestrowanie pełnego workflow: ekran telefonu + Jira + logcat w jednym oknie
- tworzenie materiałów szkoleniowych dla nowych testerów
- nagrywanie dowodów do raportów z audytów jakości

## Kiedy używać

Używaj tego narzędzia wtedy, gdy sam zrzut ekranu lub krótkie nagranie nie wystarczą — chcesz nagrać dłuższą sesję z wyjaśnieniem na głos, wiele widoków jednocześnie, albo przygotować materiał dla kogoś spoza zespołu QA.

## Pierwszy praktyczny workflow

1. Pobierz i zainstaluj OBS Studio z obsproject.com — dostępny na Windows, macOS, Linux.
2. Uruchom scrcpy na podłączonym telefonie Android — pojawi się okno z ekranem urządzenia.
3. W OBS kliknij `+` w panelu Sources > wybierz `Window Capture` > wskaż okno scrcpy.
4. Dodaj drugie źródło `Audio Input Capture` > wybierz mikrofon do komentarza głosowego.
5. Kliknij `Start Recording` > przeprowadź sesję testową > zatrzymaj > plik MP4 trafi do wskazanego folderu.

## Następny krok

Używaj OBS do dokumentowania całych sesji eksploracyjnych — nagrania stają się cennym materiałem podczas retrospektyw i przy onboardingu nowych testerów w projekcie.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- OBS generuje duże pliki — skonfiguruj kompresję (format MP4, encoder x264) żeby nagrania nie zajmowały gigabajtów.

## Link

https://obsproject.com/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia OBS Studio praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
