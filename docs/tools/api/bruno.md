# Bruno

## Kategoria

- Główna kategoria: `api-testing`
- Podkategoria: `api-client`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium-high`
- Wymaga kodowania: `False`

## Do czego służy

Gdy chcesz trzymać requesty API lokalnie i wersjonować je w Git.

## Najlepsze zastosowania

- API testing
- kolekcje w repo
- alternatywa dla Postmana

## Kiedy używać

Używaj tego narzędzia wtedy, gdy jego zastosowanie skraca drogę od obserwacji błędu do technicznego dowodu: logu, requestu, zrzutu, nagrania, testu automatycznego albo raportu.

## Pierwszy praktyczny workflow

1. Zainstaluj narzędzie.
2. Uruchom je na prostym przypadku testowym.
3. Zapisz wynik w bug report template.
4. Porównaj, czy narzędzie realnie skróciło pracę.
5. Dopiero wtedy dodaj je do stałego workflow.

## Co nowego (v4.x, 2026)

Bruno przestało być tylko "lekką alternatywą dla Postmana" — wersja 4.x dodała funkcje, które realnie zmieniają workflow:

- **Mock server** — lokalny serwer HTTP oparty o kolekcję, zwraca przykładowe odpowiedzi bez backendu (przydatne do testowania error states przed gotowym API).
- **Rich-text docs editor** — dokumentacja endpointów bez pisania Markdown ręcznie.
- **Typed variables** — zmienne przestały być tylko stringami.
- **AI w edytorze skryptów** (v4.0+) — generowanie testów/dokumentacji/skryptów, własny klucz API (OpenAI/Anthropic/kompatybilne), działa lokalnie.
- Global client certs, GCP Secret Manager, otwieranie wielu kolekcji z monorepo.

Link do changelogu: https://github.com/usebruno/bruno/releases

## Następny krok

Utwórz kolekcje dla logowania, profilu, zamówień i krytycznych endpointów. Jeśli masz Bruno 4.x, wypróbuj mock server do symulowania błędnych odpowiedzi API zamiast czekać na backendowca.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Zapisuj konfigurację w repo, jeśli narzędzie ma być używane przez zespół.
- Dla narzędzi AI: nie wklejaj poufnego kodu ani danych, jeśli polityka firmy tego zabrania.

## Link

https://github.com/usebruno/bruno

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Bruno praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
