# Workflow: sesja eksploracyjna

## Cel

Ustrukturyzowane odkrywanie błędów i ryzyk w określonym czasie, bez predefiniowanych skryptów testowych. Efektem jest lista znalezionych bugów, obserwacji i pytań do zespołu.

## Kiedy używać

- Nowa funkcja do testowania przed napisaniem formalnych TC
- Brak dokumentacji — trzeba odkryć zachowanie
- Przed ważnym releasem — jako uzupełnienie regresji
- "Mam godzinę — co warto sprawdzić?"

## Narzędzia

- scrcpy + nagranie (dowód sesji)
- ADB logcat (w tle — bez aktywnego czytania)
- Notatnik / aplikacja do notatek
- AI (pomoc w charterze i analizie po sesji)

---

## Kroki

### Krok 1 — Przygotowanie (5 min)

Sformułuj charter sesji — jedno zdanie opisujące cel:
> "Eksplorowanie funkcji [X] w poszukiwaniu problemów z [Y]"

Przykłady:
- "Eksplorowanie formularza rejestracji w poszukiwaniu problemów z walidacją"
- "Eksplorowanie trybu offline w poszukiwaniu problemów z synchronizacją danych"
- "Eksplorowanie dostępności (a11y) ekranu logowania"

### Krok 2 — Kick-off (1 min)

```bash
# Uruchom nagranie
scrcpy --record session-$(date +%Y%m%d-%H%M%S).mp4

# Uruchom logcat w tle
adb logcat > session-log-$(date +%Y%m%d-%H%M%S).txt &
```

Ustaw timer na czas sesji (zwykle 45-90 minut).

### Krok 3 — Eksploracja

Stosuj heurystyki:
- **CRUD**: Create, Read, Update, Delete — sprawdź każdą operację
- **Granice**: puste pola, maksymalne długości, specjalne znaki
- **Przerwania**: połączenie telefoniczne, powiadomienie, obrót ekranu
- **Sieć**: wyłącz WiFi w środku akcji, przełącz na LTE
- **Uprawnienia**: odmów uprawnienia, które aplikacja prosi

Notuj na bieżąco:
- Znalezione bugi (krótki opis + czas na nagraniu)
- Pytania do PO/developera
- Obszary wymagające głębszego testu

### Krok 4 — Debrief (10 min po sesji)

Po sesji:
- [ ] Zatrzymaj nagranie i logcat
- [ ] Przejrzyj notatki i pogrupuj: bugi / pytania / obserwacje / ryzyka
- [ ] Priorytetyzuj bugi (Critical/High/Medium/Low)
- [ ] Otwórz tickety Jira dla bugów High+

Użyj AI do podsumowania:
```
Mam notatki z sesji eksploracyjnej. Pomóż mi:
1. Pogrupować obserwacje według priorytetu
2. Sformułować tytuły bugów do Jiry
3. Zaproponować obszary do kolejnej sesji

Notatki: [WKLEJ]
```

### Krok 5 — Dokumentacja sesji

```markdown
## Sesja eksploracyjna — [DATA]
Charter: [OPIS CELU]
Czas: [X] minut
Tester: [Imię]

### Znalezione bugi
- [LINK Jira] — krótki opis
- [LINK Jira] — krótki opis

### Obserwacje (nie bugi, ale warte uwagi)
- ...

### Pytania do zespołu
- ...

### Propozycja kolejnej sesji
- ...
```
