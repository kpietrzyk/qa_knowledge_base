# Prompty mobile QA

## Checklista mobilna dla funkcji

```text
Stwórz checklistę testów mobilnych dla: [FUNKCJONALNOŚĆ]

Kategorie:
□ Funkcjonalność (happy path, negatywne, edge cases)
□ UI/Figma (zgodność z projektem, marginesy, typografia)
□ Responsywność (różne rozmiary ekranu, orientacja)
□ Gesty (swipe, pinch, long press, scroll)
□ Sieć (online, offline, slow 3G, przełączenie WiFi↔LTE)
□ Przerwania (połączenie telefoniczne, push notification, alarm, zamknięcie apki)
□ Dostępność (TalkBack/VoiceOver, Dynamic Type, kontrast)
□ Wydajność (czas ładowania, przewijanie, zużycie baterii)
□ Lokalizacja (różne języki, formaty daty/waluty, RTL)
□ Bezpieczeństwo (sesja, uprawnienia, przechowywanie danych)
```

## TC z User Story (Android + iOS)

```text
Jesteś QA Engineerem mobilnym (Android+iOS). Na podstawie tej user story
wygeneruj przypadki testowe. Dla każdego podaj: ID, tytuł, warunek wstępny,
kroki, oczekiwany rezultat, typ (Pozytywny/Negatywny/Edge Case).

Uwzględnij:
- happy path,
- walidacja danych,
- brak sieci / timeout,
- przerwania (połączenie telefoniczne, powiadomienie),
- tryb offline,
- orientacja ekranu (portrait/landscape),
- Dynamic Type (duża czcionka),
- różne wersje OS (min. supported).

User Story: [WKLEJ]
```

## Analiza logcat / stack trace

```text
Jestem testerem manualnym. Wyjaśnij mi te logi:
1. Co poszło nie tak (bez developer-speak — po ludzku)
2. Który komponent zawinił (apka? system? sieć? backend?)
3. Błąd apki czy systemu Android?
4. Co dokładnie dołączyć do raportu buga
5. Czy mogę to odtworzyć bez dostępu do kodu źródłowego

Logi: [WKLEJ]
```

## Analiza request/response

```text
Jesteś QA z doświadczeniem w API i mobile. Przeanalizuj request/response.
Wskaż:
- czy request wygląda poprawnie,
- czy response pasuje do expected result,
- możliwe błędy backendu,
- możliwe błędy po stronie aplikacji,
- dodatkowe testy do wykonania.

Request/response: [WKLEJ]
```

## Testowanie eksploracyjne (charter)

```text
Jesteś ekspertem od exploratory testing mobilnego.
Aplikacja: [OPIS]
Platforma: [Android/iOS]
Czas sesji: [X godzin]

Podaj:
1. TOP 5 obszarów ryzyka
2. Charter eksploracyjny dla każdego obszaru
3. Heurystyki pasujące do tego kontekstu (SFDIPOT, CRUD, itp.)
4. Co sprawdzić pierwsze (highest risk)
5. Edge cases mobilne: gesty, przerwania, low memory, background/foreground switch
```

## Generowanie YAML Maestro

```text
Napisz test Maestro (YAML) dla: [SCENARIUSZ]

Aplikacja: [NAZWA]
Platforma: [Android/iOS]
Kroki do przetestowania: [LISTA KROKÓW]
Znane element IDs (opcjonalnie): [IDs]

Uwzględnij:
- waitForAnimationToEnd lub tapOn z timeout przed interakcją,
- asercję rezultatu (assertVisible),
- komentarze przy każdym kroku.
```

## Tłumaczenie na język biznesowy

```text
Znalazłem buga: [OPIS TECHNICZNY]

Przetłumacz na:
1. Opis dla managera (wpływ na użytkownika końcowego, bez żargonu)
2. Severity (Critical/High/Medium/Low) z uzasadnieniem
3. Konsekwencje biznesowe jeśli nie naprawione
4. Proponowany priorytet naprawy

Nie używaj terminów technicznych — piszz tak, jakby odbiorcem był PM bez tła IT.
```

## TC z kodu / dokumentacji (z dostępem do repo)

```text
Na podstawie tego fragmentu [kodu/dokumentacji/API spec]:
1. Zidentyfikuj edge cases warte przetestowania
2. Wskaż error paths (co może pójść nie tak)
3. Zaproponuj konkretne dane testowe (wartości graniczne, niepoprawne formaty)
4. Co testować manualnie przed automatyzacją

Fragment: [WKLEJ]
```

## Formatowanie bug reportu (z notatek)

```text
Na podstawie moich notatek stwórz profesjonalny raport buga do Jiry.

Format:
- Tytuł: [komponent] + [zachowanie] + [kontekst]
- Środowisko: OS / wersja apki / urządzenie / sieć
- Severity: [zaproponuj z uzasadnieniem]
- Kroki do reprodukcji (numerowane)
- Rezultat rzeczywisty
- Rezultat oczekiwany
- Kontekst / uwagi dodatkowe

Moje notatki: [WKLEJ]
```
