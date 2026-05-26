# OpenAPI / Swagger

## Kategoria

- Główna kategoria: `api-testing`
- Podkategoria: `api-documentation`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

OpenAPI to standard opisywania API (wcześniej znany jako Swagger). Swagger UI to interaktywna dokumentacja API wygenerowana z pliku OpenAPI spec — tester może czytać dokumentację i jednocześnie wykonywać prawdziwe requesty bezpośrednio w przeglądarce, bez Postmana.

Dla testera: zanim zaczniesz testować API, przeczytaj spec — dowiesz się co jest możliwe, jakie pola są wymagane i jakie są typy danych.

## Najlepsze zastosowania

- przeglądanie dostępnych endpointów i ich parametrów
- testowanie requestów API bez konfigurowania Postmana
- generowanie przypadków testowych na podstawie spec
- weryfikacja czy implementacja zgadza się ze spec
- użycie jako kontekst dla AI do generowania TC

## Kiedy używać

Na początku każdego projektu: poproś dewelopera o link do Swagger UI lub plik `openapi.yaml` / `openapi.json`. Wróć do spec gdy pojawia się bug — sprawdź czy serwer działa zgodnie z dokumentacją.

## Jak czytać spec API jako tester

### Anatomia endpointu w Swagger UI

```
POST /api/v1/users/login
├── Parameters (query params / path params)
├── Request Body
│   ├── Required: true/false
│   └── Schema: { email: string, password: string }
├── Responses
│   ├── 200: { token: string, user: object }
│   ├── 400: { error: "Invalid credentials" }
│   └── 429: { error: "Too many attempts" }
└── Authorization: bearer token (kłódka)
```

### Na co zwracać uwagę jako tester

| Element spec | Co to oznacza dla testów |
|---|---|
| `required: true` | Pole obowiązkowe → testuj wysłanie bez niego |
| `minLength / maxLength` | Ograniczenia długości → testuj wartości graniczne |
| `enum: ["active", "inactive"]` | Dozwolone wartości → testuj wartość spoza listy |
| `format: "email"` | Oczekiwany format → testuj błędny format |
| `nullable: true` | Pole może być null → testuj null |
| Kody 4xx w Responses | Opisane błędy → testuj każdy scenariusz błędu |

## Pierwsze 5 akcji w Swagger UI

1. Otwórz Swagger UI (zwykle: `https://api.example.com/docs` lub `/swagger`)
2. Kliknij endpoint → rozwiń → zapoznaj się z parametrami i schematem
3. Kliknij **Try it out** → wpisz dane → kliknij **Execute**
4. Sprawdź: Response code i Response body
5. Skopiuj Request URL i curl command → użyj w Postmanie

## Generowanie test cases z API spec

Dla każdego endpointu sprawdź te kategorie:

```
Pozytywne (Happy path):
- Poprawny request z wszystkimi wymaganymi polami → oczekiwany kod 2xx

Pola wymagane:
- Wyślij bez każdego wymaganego pola z osobna → oczekiwany 400

Walidacja wartości:
- Pusta wartość wymaganego pola → 400
- Za długa wartość (maxLength + 1) → 400
- Zły format (np. "not-an-email" zamiast email) → 400
- Wartość spoza enum → 400

Autoryzacja:
- Brak tokenu → 401
- Wygasły token → 401
- Token użytkownika bez uprawnień → 403

Zasoby:
- Nieistniejące ID → 404
- Zduplikowany zasób (jeśli unique) → 409

Serwer:
- Duże zapytanie / atak → sprawdź 429 (rate limiting)
```

## Jak użyć spec z AI do generowania TC

```text
Kontekst: Oto spec endpointu POST /api/v1/orders:
[WKLEJ JSON/YAML ENDPOINTU Z SWAGGERA]

Wygeneruj test cases dla tego endpointu jako tester manualny.
Uwzględnij: happy path, brakujące pola wymagane, walidację typów,
scenariusze autoryzacji i edge cases dla e-commerce.
Format: tabela | Tytuł TC | Metoda | Payload | Oczekiwany status | Oczekiwany wynik |
```

## Następny krok

Eksportuj spec do pliku `openapi.json` → zaimportuj do Postmana jako kolekcję. Postman wygeneruje gotowe requesty dla każdego endpointu.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Spec może być nieaktualna — zawsze weryfikuj rzeczywiste zachowanie API vs dokumentacja.
- Swagger UI z `Try it out` wykonuje PRAWDZIWE requesty — uważaj na operacje DELETE i POST w środowisku produkcyjnym.
- Brak spec? Poproś zespół — generowanie spec z kodu to standardowa praktyka (Springdoc, FastAPI, NestJS Swagger).

## Link

https://swagger.io/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA API. Naucz mnie używać Swagger UI i specyfikacji OpenAPI praktycznie.
Chcę wiedzieć:
1. Jak czytać specyfikację endpointu jako tester?
2. Jak używać "Try it out" do manualnego testowania API?
3. Jak generować test cases z API spec systematycznie?
4. Jak weryfikować czy implementacja jest zgodna ze spec?
5. Jak eksportować spec do Postmana?
```
