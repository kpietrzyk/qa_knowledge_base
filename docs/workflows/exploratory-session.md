# Workflow: sesja eksploracyjna

## Cel

Ustrukturyzowane odkrywanie błędów i ryzyk w określonym czasie, bez predefiniowanych skryptów testowych. Efektem jest lista znalezionych bugów, obserwacji i pytań do zespołu.

## Kiedy używać

- Nowa funkcja do testowania przed napisaniem formalnych TC
- Brak dokumentacji — trzeba odkryć zachowanie
- Przed ważnym releasem — jako uzupełnienie regresji
- "Mam godzinę — co warto sprawdzić?"

## Dane wejściowe

- obszar lub ryzyko do zbadania,
- build i środowisko,
- dostępne wymagania oraz znane problemy,
- timebox i osoba odpowiedzialna za debrief.

## Narzędzia

- [scrcpy](../tools/mobile/scrcpy.md) — nagranie sesji
- [ADB](../tools/mobile/adb.md) — logcat w tle
- Notatnik / aplikacja do notatek
- [Ollama](../tools/ai/ollama.md) — opcjonalna, lokalna pomoc w charterze i podsumowaniu

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

```powershell
$sessionId = Get-Date -Format 'yyyyMMdd-HHmmss'

# Uruchom logcat w tle
$logcat = Start-Process adb `
  -ArgumentList "logcat" `
  -RedirectStandardOutput "session-log-$sessionId.txt" `
  -PassThru -NoNewWindow

# Nagrywaj do naciśnięcia Ctrl+C
scrcpy --record="session-$sessionId.mp4"

# Zatrzymaj proces logcat po sesji
Stop-Process -Id $logcat.Id
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
- Pokryte i pominięte obszary charteru

### Krok 4 — Debrief (10 min po sesji)

Po sesji:

- [ ] Zatrzymaj nagranie i logcat
- [ ] Przejrzyj notatki i pogrupuj: bugi / pytania / obserwacje / ryzyka
- [ ] Priorytetyzuj bugi (Critical/High/Medium/Low)
- [ ] Zarejestruj lub świadomie odrzuć każde znalezione ryzyko; nie pomijaj go wyłącznie z powodu niskiej severity
- [ ] Ustal właściciela pytań i dalszych działań

Opcjonalnie użyj lokalnego AI do przygotowania draftu podsumowania:

```text
Mam notatki z sesji eksploracyjnej. Pomóż mi:
1. Pogrupować obserwacje według priorytetu
2. Sformułować tytuły bugów do Jiry
3. Zaproponować obszary do kolejnej sesji

Notatki: [WKLEJ]
```

Przed użyciem usuń dane osobowe, tokeny, nazwy klientów i inne dane wewnętrzne. Zweryfikuj podsumowanie z oryginalnymi notatkami.

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

## Wynik i kryteria zakończenia

Workflow jest zakończony po debriefie, gdy zapisano charter, timebox, pokryty zakres, dowody, błędy, obserwacje, pytania, ryzyka i właścicieli kolejnych działań.

## Prywatność i bezpieczeństwo

- Używaj kont oraz danych testowych i nie nagrywaj danych osób trzecich.
- Przed udostępnieniem zanonimizuj nagrania, logi i notatki.
- Notatki wewnętrzne analizuj lokalnie; nie wysyłaj ich do modelu chmurowego bez zatwierdzonej zgody.
- Ustal retencję nagrań przed rozpoczęciem sesji.

## Powiązane materiały

- [Prompty do testów eksploracyjnych](../prompts/exploratory-testing-prompts.md)
- [Analiza błędu w aplikacji mobilnej](bug-investigation-mobile.md)
- [Regresja przed releasem](regression-before-release.md)
