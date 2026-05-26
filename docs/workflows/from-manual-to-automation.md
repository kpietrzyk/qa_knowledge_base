# Workflow: od testu manualnego do automatycznego

## Cel

Podjąć decyzję, kiedy warto zautomatyzować test manualny, jak to zrobić, i co zrobić jako pierwszy krok.

## Kiedy automatyzować — 5 pytań

1. **Czy test wykonujesz częściej niż 1x/sprint?** → tak = kandydat do automatyzacji
2. **Czy kroki są deterministyczne (zawsze te same)?** → tak = łatwiejszy do automatyzacji
3. **Czy UI jest stabilne (elementy mają selektory)?** → tak = techniczne możliwe
4. **Czy wartość regresyjna jest wysoka?** → tak = warto inwestować czas
5. **Czy masz dostęp do kodu/repozytorium?** → tak = możesz też pisać testy API

Jeśli odpowiedź na ≥3 pytania to "tak" → automatyzuj.

---

## Ścieżka decyzji

```
Test manualny
    ↓
[Czy to mobile E2E?]
    ├── Tak → Maestro (brak kodu) lub Appium (z kodem)
    └── Nie
         ↓
    [Czy to web/admin panel?]
         ├── Tak → Playwright
         └── Nie
              ↓
         [Czy to test API?]
              ├── Tak → Postman/Newman lub Bruno
              └── Nie → Zostań przy manualnym + AI review
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

### Krok 3 — Wygeneruj YAML (opcja A: MaestroGPT)

Wklej do MaestroGPT lub użyj promptu:
```
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
- launchApp
- tapOn: "Zaloguj się"
- inputText:
    text: "test@example.com"
    id: "email_input"
- inputText:
    text: "Test1234!"
    id: "password_input"
- tapOn: "Zaloguj"
- assertVisible: "Strona główna"
```

### Krok 5 — Uruchom i popraw

```bash
maestro test login-flow.yaml
```

Popraw selektory jeśli test failuje (najczęstszy problem: zły resource-id lub brak waitForAnimationToEnd).

### Krok 6 — Dodaj do repo

Zapisz w `examples/maestro/` z opisem w komentarzu YAML.
Dodaj do CI/CD jako smoke test przy każdym buildzie.
