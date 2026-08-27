# Playwright

## Kategoria

- Główna kategoria: `web-automation`
- Podkategoria: `e2e`
- Darmowe: `True`
- Poziom trudności: `medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `very high`
- Wymaga kodowania: `True`

## Do czego służy

Gdy aplikacja mobilna ma panel admina, webview, PWA albo backendowe procesy webowe.

## Najlepsze zastosowania

- web
- mobile web
- PWA
- admin panel
- webview-adjacent testing

## Kiedy używać

Używaj tego narzędzia wtedy, gdy jego zastosowanie skraca drogę od obserwacji błędu do technicznego dowodu: logu, requestu, zrzutu, nagrania, testu automatycznego albo raportu.

## Pierwszy praktyczny workflow

1. Zainstaluj narzędzie.
2. Uruchom je na prostym przypadku testowym.
3. Zapisz wynik w bug report template.
4. Porównaj, czy narzędzie realnie skróciło pracę.
5. Dopiero wtedy dodaj je do stałego workflow.

## Co nowego (v1.60–1.62, 2026)

Playwright MCP (serwer + CLI) jest teraz **wbudowany** — nie trzeba już instalować go osobno, wystarczy `npx playwright mcp`. To pozwala agentom AI (Claude Code, Cursor itp.) sterować prawdziwą przeglądarką przez Playwrighta. Zobacz też `docs/tools/ai/playwright-mcp.md`. Inne nowości: wirtualny autentykator WebAuthn/passkey do testów logowania, bezpośrednie API do `page.localStorage`/`sessionStorage`, oraz `retryStrategy: 'isolated'` (powtórki na końcu, pojedynczo, zamiast od razu).

## Następny krok

Zacznij od Playwright Codegen i testów w TypeScript.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Zapisuj konfigurację w repo, jeśli narzędzie ma być używane przez zespół.
- Dla narzędzi AI: nie wklejaj poufnego kodu ani danych, jeśli polityka firmy tego zabrania.

## Link

https://github.com/microsoft/playwright

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Playwright praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
