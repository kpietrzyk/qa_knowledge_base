# JWT — Podstawy dla Testera

## Kategoria

- Główna kategoria: `api-testing`
- Podkategoria: `authentication`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

JWT (JSON Web Token) to standard tokenu używanego do autoryzacji w API. Po zalogowaniu serwer zwraca token JWT, który klient dołącza do każdego kolejnego requestu. Tester musi umieć go odczytać — żeby sprawdzić co jest w środku, debugować błędy 401 i testować scenariusze autoryzacji.

**Dekodujesz JWT na jwt.io** — to darmowy, bezpieczny dekoder online (token nie jest wysyłany do serwera, dekodowanie jest lokalne).

## Anatomia JWT

JWT wygląda tak:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTYiLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHAiOjE3MTcwMDAwMDB9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

Trzy części oddzielone kropką:

| Część | Nazwa | Zawartość |
|---|---|---|
| `eyJhbGci...` | Header | Algorytm szyfrowania (HS256, RS256) |
| `eyJzdWIi...` | Payload | Dane użytkownika i metadane tokenu |
| `SflKxwRJ...` | Signature | Podpis kryptograficzny — weryfikuje autentyczność |

## Jak zdekodować JWT

1. Otwórz https://jwt.io/
2. Wklej token w pole po lewej
3. Przeczytaj zdekodowany Payload po prawej

**Skąd wziąć token?**
- Z response body endpointu logowania (`/api/login` → pole `token` lub `access_token`)
- Z nagłówka requestu w DevTools / Postmanie (`Authorization: Bearer TOKEN`)
- Z localStorage w DevTools przeglądarki (Application tab → Local Storage)

## Co sprawdzać w Payload JWT

### Kluczowe pola standardowe

| Pole | Znaczenie | Co testować |
|---|---|---|
| `exp` | Expiration time — timestamp (Unix) wygaśnięcia | Przelicz na datę: `new Date(exp * 1000)` |
| `iat` | Issued at — kiedy token został wystawiony | Porównaj z exp — jaki jest czas życia tokenu? |
| `sub` | Subject — ID użytkownika | Czy to właściwy user ID? |
| `email` | Email zalogowanego użytkownika | Czy zgadza się z kontem testowym? |
| `role` / `roles` | Rola/uprawnienia | Czy tester ma właściwą rolę dla scenariusza? |
| `iss` | Issuer — kto wystawił token | Czy to właściwe środowisko? (dev vs prod) |

### Przeliczanie exp na datę (szybko)
```
Timestamp exp: 1717000000
W przeglądarce: new Date(1717000000 * 1000).toLocaleString()
Lub wklej na: https://www.unixtimestamp.com/
```

## Typowe błędy JWT do testowania

| Scenariusz testowy | Jak przygotować | Oczekiwany wynik |
|---|---|---|
| Brak tokenu | Usuń nagłówek `Authorization` | 401 Unauthorized |
| Wygasły token | Użyj tokenu po upływie `exp` | 401 Unauthorized lub `Token expired` |
| Token z innego środowiska | Weź token z produkcji, użyj na dev | 401 lub inny błąd |
| Token innego użytkownika | Zaloguj się na konto A, używaj tokenu na zasobie konta B | 403 Forbidden |
| Zmodyfikowany token | Edytuj środkową część i użyj (podpis będzie nieprawidłowy) | 401 Invalid signature |
| Token z inną rolą | Użyj tokenu user na endpointach dostępnych tylko dla admin | 403 Forbidden |
| Pusty string jako token | `Authorization: Bearer ` (pusty) | 401 Unauthorized |

## Jak używać JWT w Postmanie

### Metoda 1: Ręczne ustawienie
```
1. W kolekcji → zakładka Authorization
2. Type: Bearer Token
3. Token: wklej token JWT
```

### Metoda 2: Automatyczne (po zalogowaniu)
```javascript
// W zakładce Tests requestu logowania:
const response = pm.response.json();
pm.environment.set("auth_token", response.token);
```
```
// W kolejnych requestach → Authorization → Bearer Token:
{{auth_token}}
```

### Metoda 3: W nagłówku (ręcznie)
```
Headers:
Authorization | Bearer eyJhbGci...TWÓJ_TOKEN
```

## Następny krok

Naucz się automatycznego odświeżania tokenów w Postmanie (Pre-request Script). Sprawdź też jak testować OAuth2 flow — gdy token pochodzi z zewnętrznego dostawcy (Google, Apple).

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- **Nigdy nie wklejaj tokenów produkcyjnych użytkowników do publicznych narzędzi online.** jwt.io dekoduje lokalnie w przeglądarce, ale zachowaj ostrożność z danymi produkcyjnymi.
- JWT nie jest szyfrowany (tylko zakodowany Base64) — każdy może odczytać payload. Dlatego nie powinien zawierać haseł.
- Podpis chroni przed modyfikacją, ale nie przed odczytaniem — JWT to autoryzacja, nie prywatność.
- Sprawdź licencję przed użyciem komercyjnym.

## Link

https://jwt.io/

## Prompt AI do nauki tematu

```text
Jesteś seniorem QA API. Naucz mnie JWT praktycznie dla manualnego testera.
Chcę wiedzieć:
1. Jak zdekodować JWT i co oznaczają poszczególne pola?
2. Jak sprawdzić czy token wygasł?
3. Jakie scenariusze testowe powinienem sprawdzić dla autoryzacji JWT?
4. Jak ustawić token JWT w Postmanie automatycznie po logowaniu?
5. Jakie są najczęstsze błędy implementacji JWT których szukam jako tester?
```
