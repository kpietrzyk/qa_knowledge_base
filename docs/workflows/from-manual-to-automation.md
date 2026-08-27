# Workflow: od testu manualnego do automatycznego

## Cel

Podjąć decyzję, kiedy warto zautomatyzować test manualny, jak to zrobić, i co zrobić jako pierwszy krok.

## Kiedy używać

Gdy scenariusz jest wykonywany regularnie, ma wartość regresyjną albo blokuje szybki feedback, a zespół rozważa jego automatyzację.

## Dane wejściowe

- manualny scenariusz z oczekiwanym rezultatem,
- częstotliwość wykonania i wpływ biznesowy,
- dostępne warstwy systemu oraz selektory/interfejsy,
- sposób przygotowania danych i środowiska,
- właściciel utrzymania testu.

## Kryteria decyzji

Oceń łącznie:

- częstotliwość i koszt ręcznego wykonania,
- ryzyko biznesowe oraz szybkość potrzebnego feedbacku,
- deterministyczność scenariusza i kontrolę danych,
- stabilność testowanego interfejsu,
- koszt implementacji, diagnostyki i utrzymania,
- możliwość pokrycia ryzyka niżej niż przez UI,
- właściciela i budżet na naprawę testu.

Automatyzuj, gdy oczekiwana wartość przewyższa koszt utrzymania i istnieje stabilny oracle. Pojedynczy próg liczby odpowiedzi „tak” nie zastępuje tej decyzji.

## Narzędzia

- [Maestro](../tools/mobile/maestro.md) — proste przepływy E2E w deklaratywnym YAML
- [Appium](../tools/mobile/appium.md) — rozbudowane testy mobilne w kodzie
- [Playwright](../tools/web/playwright.md) — web i panele administracyjne
- [Bruno](../tools/api/bruno.md) lub [Postman](../tools/api/postman.md) — testy i kolekcje API
- [Appium Inspector](../tools/mobile/appium-inspector.md) lub [uiautomatorviewer](../tools/ui-inspection/uiautomatorviewer.md) — inspekcja selektorów

---

## Ścieżka decyzji

```text
Test manualny
    ↓
[Czy ryzyko można pokryć niżej niż przez UI?]
    ├── Tak → preferuj test jednostkowy, komponentowy, kontraktowy lub API
    └── Nie
         ↓
    [Czy wymagany jest przepływ użytkownika mobile E2E?]
         ├── Tak → Maestro (prosty flow) lub Appium (większa kontrola)
         └── Nie
              ↓
         [Czy to web/admin panel?]
              ├── Tak → Playwright
              └── Nie → pozostaw test manualny lub eksploracyjny i zapisz powód
```

---

## Krok po kroku: manual test → Maestro YAML

### Krok 1 — Napisz kroki manualnie

```markdown
1. Otwórz aplikację
2. Kliknij "Zaloguj się"
3. Wpisz email: test@example.com
4. Wpisz hasło: Test1234!
5. Kliknij przycisk "Zaloguj"
6. Sprawdź, czy widoczny jest tekst "Strona główna"
```

### Krok 2 — Znajdź selektory

Użyj **Appium Inspector** lub **uiautomatorviewer**:

- Kliknij element w apce → skopiuj `resource-id` lub `accessibility-id`
- Preferuj stabilne identyfikatory dostępności; nie opieraj krytycznego flow wyłącznie na współrzędnych.

### Krok 3 — Przygotuj draft YAML

Napisz flow ręcznie lub przygotuj draft w zatwierdzonym lokalnym modelu:

```text
Napisz test Maestro YAML dla:
- appId: com.example.app
- kroki: [WKLEJ KROKI]
- element IDs (jeśli znasz): [WKLEJ]
Dodaj asercje i komentarze.
```

### Krok 4 — Wygeneruj YAML (opcja B: ręcznie)

```yaml
appId: com.example.app
---
- launchApp:
    clearState: true
- tapOn:
    id: "email_input"
- inputText: "test@example.com"
- tapOn:
    id: "password_input"
- inputText:
    text: "Test1234!"
    label: "Wpisz hasło konta testowego"
- tapOn:
    id: "login_button"
- assertVisible:
    id: "home_screen"
```

`inputText` wpisuje tekst do aktualnie aktywnego pola. Selektor `id` należy umieścić w poprzedzającym `tapOn`, a nie w `inputText`.

### Krok 5 — Uruchom i popraw

```powershell
maestro test login-flow.yaml
```

Przy błędzie najpierw sprawdź stan aplikacji, dane i selektory. Nie ukrywaj niestabilności przez bezwarunkowe retry lub długie sleep.

### Krok 6 — Dodaj do repo

Zapisz flow w `examples/maestro/` z krótkim opisem celu, wymagania i danych. Do CI dodawaj mały, stabilny zestaw smoke z artefaktami błędu; pozostałe testy uruchamiaj zgodnie z kosztem i ryzykiem.

## Wynik i kryteria zakończenia

Workflow jest zakończony, gdy istnieje udokumentowana decyzja: zautomatyzować na wybranej warstwie albo pozostawić manualnie. Test automatyczny ma właściciela, powiązane wymaganie, kontrolowane dane, jednoznaczne asercje i powtarzalny wynik na czystym środowisku.

## Prywatność i bezpieczeństwo

- Używaj wyłącznie kont i danych testowych; nie zapisuj prawdziwych haseł w repozytorium.
- Przekazuj sekrety przez mechanizm CI lub lokalne zmienne środowiskowe ignorowane przez Git.
- Kod lub wymagania wewnętrzne wysyłaj tylko do zatwierdzonych narzędzi; preferuj model lokalny.
- Ogranicz screenshoty, logi i nagrania testowe do danych potrzebnych do diagnozy.

## Powiązane materiały

- [Przykładowy flow Maestro w repozytorium](https://github.com/kpietrzyk/qa_knowledge_base/blob/main/examples/maestro/login-flow.yaml)
- [Projektowanie testów z pomocą AI](ai-assisted-test-design.md)
- [Regresja przed releasem](regression-before-release.md)
