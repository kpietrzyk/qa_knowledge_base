# Prompty do przypadków testowych

## TC z User Story (mobile, Android+iOS)

```text
Jesteś QA Engineerem mobilnym (Android+iOS). Na podstawie tej user story
wygeneruj przypadki testowe. Dla każdego podaj: ID, tytuł, warunek wstępny,
kroki, oczekiwany rezultat, typ (Pozytywny/Negatywny/Edge Case).

Uwzględnij:
- happy path,
- walidacja danych (puste pola, za długi tekst, złe formaty),
- brak sieci / timeout / powolne połączenie,
- przerwania (połączenie tel., powiadomienie push, alarm),
- tryb offline,
- orientacja ekranu (portrait i landscape),
- Dynamic Type (duży rozmiar czcionki),
- różne wersje OS (min. supported version).

User Story: [WKLEJ]
```

## Generowanie przypadków z wymagania

```text
Jesteś QA Engineerem. Na podstawie wymagania wygeneruj przypadki testowe.

Podziel na:
- happy path,
- negative cases,
- edge cases,
- permission cases,
- network cases (online/offline/slow),
- mobile-specific cases (orientation, gestures, interruptions),
- API/backend cases,
- accessibility basics,
- regression risks.

Wymaganie: [WKLEJ]
```

## TC z kodu / dokumentacji (z dostępem do repo)

```text
Na podstawie tego fragmentu [kodu/dokumentacji/API spec]:
1. Zidentyfikuj edge cases warte przetestowania
2. Wskaż error paths (co może pójść nie tak — wyjątki, błędy walidacji)
3. Zaproponuj konkretne dane testowe (wartości graniczne, niepoprawne formaty, null)
4. Podziel na: co testować manualnie vs co nadaje się do automatyzacji

Fragment: [WKLEJ]
```

## Redukcja do smoke testów przed releasem

```text
Z tej listy przypadków testowych wybierz minimalny smoke suite.
Założenie: mamy 20 minut na testy przed releasem mobilnym.

Podaj:
- testy krytyczne (must-run — bez nich nie releasujemy),
- testy opcjonalne (warto, jeśli starczy czasu),
- uzasadnienie wyboru.

Lista testów: [WKLEJ]
```

## Zamiana manual test case na automatyzację

```text
Przeanalizuj ten manualny przypadek testowy i oceń, czy nadaje się do automatyzacji.

Oceń:
1. Stabilność (czy UI jest stabilne, czy elementy mają selektory)
2. Wartość regresyjna (czy test warto uruchamiać przy każdym buildzie)
3. Trudność automatyzacji (łatwy/średni/trudny — uzasadnij)
4. Wymagane dane testowe (czy potrzebne są mock data lub test account)
5. Rekomendowane narzędzie: Maestro (YAML), Appium, Playwright czy API test

Test case: [WKLEJ]
```

## Generowanie danych testowych

```text
Wygeneruj zestaw danych testowych dla tego pola/formularza:

Typ pola: [np. email, numer telefonu, hasło, data urodzenia, kwota]
Wymagania walidacji (jeśli znasz): [OPIS]

Wygeneruj:
1. Dane poprawne (valid — happy path)
2. Dane niepoprawne (invalid — negative cases)
3. Wartości graniczne (boundary values)
4. Dane specjalne (emoji, spacje, SQL injection pattern, XSS pattern)
5. Dane dla lokalizacji (jeśli aplikacja jest wielojęzyczna)
```
