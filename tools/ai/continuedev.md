# Continue.dev

## Kategoria

- Główna kategoria: `ai-for-testing`
- Podkategoria: `local-ai-coding`
- Darmowe: `True`
- Poziom trudności: `medium`
- Wartość dla manualnego testera: `medium-high`
- Wartość dla automatyzacji: `high`
- Wymaga kodowania: `False`

## Do czego służy

Gdy chcesz używać lokalnego LLM do pracy z testami i repozytorium.

## Najlepsze zastosowania

- lokalny asystent kodu
- Ollama
- VS Code
- repo context

## Kiedy używać

Używaj tego narzędzia wtedy, gdy jego zastosowanie skraca drogę od obserwacji błędu do technicznego dowodu: logu, requestu, zrzutu, nagrania, testu automatycznego albo raportu.

## Pierwszy praktyczny workflow

1. Zainstaluj narzędzie.
2. Uruchom je na prostym przypadku testowym.
3. Zapisz wynik w bug report template.
4. Porównaj, czy narzędzie realnie skróciło pracę.
5. Dopiero wtedy dodaj je do stałego workflow.

## Następny krok

Połącz z modelem Qwen/Coder przez Ollama i zacznij od generowania testów jednostkowych pomocniczych.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Zapisuj konfigurację w repo, jeśli narzędzie ma być używane przez zespół.
- Dla narzędzi AI: nie wklejaj poufnego kodu ani danych, jeśli polityka firmy tego zabrania.

## Link

https://github.com/continuedev/continue

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Continue.dev praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
