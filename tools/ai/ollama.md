# Ollama

## Kategoria

- Główna kategoria: `ai-for-testing`
- Podkategoria: `local-llm`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Uruchamia duże modele językowe (LLM) lokalnie na Twoim komputerze — całkowicie offline, bez wysyłania danych do chmury. Kluczowe narzędzie dla testerów pracujących z kodem firmowym, logami i danymi objętymi NDA.

## Dlaczego lokalny LLM dla QA?

Wklejanie kodu źródłowego, logów z crashem czy danych konfiguracyjnych do publicznego ChatGPT lub Claude to potencjalne naruszenie NDA i polityki bezpieczeństwa firmy. Ollama rozwiązuje ten problem — AI działa wyłącznie na Twoim sprzęcie.

## Najlepsze zastosowania

- analiza logów z crashem (Logcat, stack trace) — bezpieczne wklejanie danych firmowych,
- interpretacja plików konfiguracyjnych JSON/YAML z projektu,
- generowanie przypadków testowych z wymagań wewnętrznych,
- review własnych bug reportów przed wysłaniem,
- eksperymenty z promptami bez kosztów i limitów API.

## Kiedy używać

Używaj Ollamy zawsze wtedy, gdy chcesz skorzystać z AI, ale nie możesz lub nie powinieneś wysyłać danych do zewnętrznych serwisów. Typowe przypadki: logi produkcyjne, tokeny sesji w requestach, wewnętrzna dokumentacja techniczna, kody źródłowe objęte NDA.

## Pierwszy praktyczny workflow

1. Zainstaluj Ollama: `curl -fsSL https://ollama.com/install.sh | sh` (macOS/Linux) lub pobierz ze strony (Windows).
2. Pobierz model: `ollama pull llama3` (lub `mistral`, `qwen2.5-coder` dla kodu).
3. Uruchom interaktywny czat: `ollama run llama3`.
4. Wklej logi z crasha i zapytaj: "Wyjaśnij ten błąd i co dołączyć do bug reportu".
5. Zakończ sesję: `/bye` — model działa w pełni offline.

## Polecane modele dla QA

| Model | Rozmiar | Najlepszy do |
|---|---|---|
| `llama3` | ~4GB | ogólne pytania, analiza tekstu |
| `mistral` | ~4GB | analiza logów, wyjaśnienia |
| `qwen2.5-coder` | ~4GB | analiza kodu, YAML, JSON |
| `phi3` | ~2GB | szybkie odpowiedzi na słabszym sprzęcie |

## Następny krok

Połącz Ollamę z Continue.dev w VS Code — lokalny AI-asystent bezpośrednio w edytorze kodu testów.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję modelu przed użyciem komercyjnym (każdy model ma osobną licencję).
- Lokalne modele są słabsze od GPT-4/Claude — weryfikuj odpowiedzi krytycznie.
- Wymagania sprzętowe: min. 8GB RAM, lepiej 16GB; GPU przyspiesza generowanie.
- Nie zastępuje oceny i doświadczenia testera — to narzędzie wspomagające.

## Link

https://ollama.com/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie używać Ollamy praktycznie jako testera.
Kontekst: jestem manualnym testerem aplikacji mobilnych, mam dostęp do logów i kodu.
Chcę wiedzieć:
1. kiedy używać lokalnego modelu zamiast ChatGPT/Claude,
2. jak zainstalować i uruchomić pierwszy model,
3. jakie modele są najlepsze do analizy logów i generowania TC,
4. jak sformułować dobry prompt do analizy logcata,
5. jak połączyć Ollamę z Continue.dev w VS Code,
6. jakie są ograniczenia lokalnych modeli vs cloud AI.
```
