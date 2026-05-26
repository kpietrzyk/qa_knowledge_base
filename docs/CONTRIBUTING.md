# Contributing — jak współtworzyć to repozytorium

Dziękujemy za chęć wkładu! To repo rośnie dzięki praktycznym doświadczeniom testerów.

---

## Jak mogę pomóc?

### 1. Zgłoś błąd lub nieaktualną informację

Jeśli narzędzie zmieniło cenę, licencję, nazwę lub funkcjonalność:
- Otwórz Issue na GitHubie
- Opisz: co jest nieaktualne, jaka jest aktualna informacja, źródło

### 2. Dodaj nowe narzędzie

1. Sprawdź, czy narzędzie nie jest już opisane w `tools/`
2. Skopiuj szablon z `templates/tool-template.md` (jeśli istnieje) lub wzoruj się na istniejącym pliku (np. `tools/mobile/adb.md`)
3. Wypełnij **wszystkie sekcje** — szczególnie "Kiedy używać" i "Kiedy NIE używać"
4. Dodaj narzędzie do `datasets/tools-list.csv` i `datasets/comparison-table.md`
5. Stwórz Pull Request

### 3. Popraw istniejący opis narzędzia

- Preferuj konkretne kroki zamiast ogólnych opisów
- Dodaj sekcję "Kiedy NIE używać" jeśli jej brakuje
- Jeśli znasz narzędzie w praktyce — dodaj workflow z realnego projektu

### 4. Dodaj prompt

- Dodaj do odpowiedniego pliku w `prompts/`
- Prompt powinien mieć: kontekst, konkretne pytania, `[WKLEJ]` w miejscach do uzupełnienia
- Przetestuj prompt przed dodaniem

### 5. Dodaj workflow

- Plik w `workflows/`
- Format: cel → kiedy używać → narzędzia → kroki (numerowane) → pułapki
- Bazuj na realnym procesie, nie teorii

---

## Standardy jakości

### Każdy plik narzędzia powinien mieć:

```markdown
## Kategoria (metadane)
## Do czego służy (1-2 zdania)
## Najlepsze zastosowania (lista)
## Kiedy używać (konkretny kontekst)
## Kiedy NIE używać (ważne!)
## Pierwszy praktyczny workflow (numerowane kroki)
## Następny krok (co dalej)
## Ryzyka i ograniczenia
## Link (oficjalne źródło)
## Prompt AI do nauki narzędzia
```

### Zasady treści:

- ✅ Konkretne komendy, kroki, przykłady
- ✅ "Kiedy NIE używać" — często ważniejsze niż "kiedy używać"
- ✅ Aktualna informacja o licencji (darmowe / freemium / płatne)
- ❌ Nie kopiuj dokumentacji narzędzia — podaj link
- ❌ Nie pisz "jest świetny" — opisz konkretną wartość dla testera
- ❌ Nie dodawaj narzędzi bez praktycznej wartości dla QA

### Informacje o cenach:

Ceny się zmieniają. Używaj:
- `True` — w pełni darmowe lub open-source
- `True (plan)` — jest darmowy plan z limitami
- `False` — płatne
- `False (trial)` — jest trial, potem płatne

Zawsze dodaj `license_note` z aktualną informacją.

---

## Języki

- Pliki dokumentacyjne: **polski**
- Kod (YAML, JSON, Python, TS): angielski (komentarze mogą być polskie)
- Nazwy plików i folderów: angielski (kebab-case)

---

## Czego NIE dodajemy

- Narzędzi czysto developerskich bez wartości dla QA
- Przestarzałych narzędzi bez aktywnego developmentu
- Narzędzi, których nie można zweryfikować praktycznie
- Treści promocyjnych lub sponsorowanych
