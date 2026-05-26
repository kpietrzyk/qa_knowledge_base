# Workflow: projektowanie testów z pomocą AI

## Cel

Użyć AI do przyspieszenia projektowania przypadków testowych — od User Story do gotowej listy TC w 15-20 minut zamiast 1-2 godzin.

## Ważna zasada

AI generuje **draft** — tester weryfikuje, uzupełnia i akceptuje. AI nie zna kontekstu biznesowego, nie wie o specyficznych błędach z przeszłości i nie rozumie priorytetu z perspektywy PM.

## Kiedy używać

- Nowa User Story w sprincie
- Brak czasu na ręczne projektowanie TC
- Chcesz sprawdzić, czy czegoś nie pominąłeś
- Analiza wymagań przed testem

---

## Kroki

### Krok 1 — Przygotuj input

Zbierz:
- User Story (z Jiry lub dokumentacji)
- Definicję done (DoD) jeśli jest
- Link do ekranu w Figmie (opcjonalnie)
- Informację o platformie (Android / iOS / Web)

### Krok 2 — Wygeneruj TC przez AI

Użyj promptu z `prompts/test-case-prompts.md`:
```
Jesteś QA Engineerem mobilnym (Android+iOS). Na podstawie tej user story
wygeneruj przypadki testowe. Dla każdego podaj: ID, tytuł, warunek wstępny,
kroki, oczekiwany rezultat, typ (Pozytywny/Negatywny/Edge Case).

Uwzględnij: happy path, walidacja, brak sieci, przerwania, offline,
orientacja ekranu, Dynamic Type.

User Story: [WKLEJ]
```

### Krok 3 — Review output AI

Po otrzymaniu listy TC:
- [ ] Czy happy path jest pokryty?
- [ ] Czy negatywne przypadki są realistyczne?
- [ ] Czy edge cases pasują do kontekstu tej apki?
- [ ] Czy AI nie wymyśliło funkcji, której nie ma w US?
- [ ] Czy brakuje TC specyficznych dla Twojego projektu?

### Krok 4 — Uzupełnij z wiedzy własnej

Dodaj TC, które AI pominęło:
- Błędy znane z historii projektu
- Specyfika urządzeń używanych przez użytkowników
- Integracje z innymi modułami
- Szczególne wymagania biznesowe

### Krok 5 — Priorytetyzacja

Podziel TC na:
- **Must run** (smoke) — każdy build
- **Should run** (regresja) — każdy sprint
- **Nice to have** (pełna regresja) — przed releasem

### Krok 6 — Import do TMS

Wklej do Qase / AgileTest / Kiwi TCMS / Jira.
Dodaj tagi: `mobile`, `android`, `ios`, `api`, `smoke`, `regression`.

---

## Wskazówki dla lepszego outputu AI

| Zamiast | Lepiej |
|---|---|
| "Wygeneruj testy dla logowania" | "Wygeneruj TC dla logowania emailem w apce Android, gdzie token JWT wygasa po 15 min" |
| Ogólny prompt bez kontekstu | Wklej fragment US + DoD + platformę |
| Akceptuj output bez review | Zawsze przejrzyj i uzupełnij |
| Jeden duży prompt | Kilka mniejszych (osobno happy path, osobno negatywne) |
