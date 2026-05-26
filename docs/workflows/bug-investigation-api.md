# Workflow: analiza błędu API

## Cel

Określić, czy problem leży w aplikacji (Frontend), na serwerze (Backend), w danych, w autoryzacji, czy w konfiguracji środowiska. Zebrać dowody techniczne: request, response, kod odpowiedzi, nagłówki.

## Kiedy używać

Gdy aplikacja pokazuje błąd, pusty ekran, nieprawidłowe dane lub nie wykonuje akcji — a podejrzewasz, że to problem z komunikacją z serwerem.

## Narzędzia

- HTTP Toolkit / mitmproxy / Proxyman / Charles (przechwycenie ruchu)
- Postman / Bruno (ręczne odtworzenie requestu)
- ChatGPT/Claude lub Ollama (interpretacja response)

---

## Kroki

### Krok 1 — Przechwycenie ruchu

1. Uruchom proxy (HTTP Toolkit: QR → telefon, lub mitmproxy na porcie 8080)
2. Wykonaj akcję w aplikacji, która powoduje problem
3. Zidentyfikuj podejrzany request w proxy

### Krok 2 — Analiza requestu

Sprawdź kolejno:

| Co sprawdzić | Jak |
|---|---|
| Metoda HTTP | GET/POST/PUT/DELETE — czy poprawna? |
| URL | Czy endpoint jest poprawny? Czy nie ma literówki? |
| Nagłówki | Authorization, Content-Type, Accept |
| Body | Czy payload jest poprawnie sformatowany? |
| Token | Czy jest? Czy nie wygasł? |

### Krok 3 — Analiza response

| Status code | Co może oznaczać |
|---|---|
| 200 OK | Server odpowiedział — sprawdź body |
| 400 Bad Request | Problem po stronie requestu (dane, format) |
| 401 Unauthorized | Brak/zły/wygasły token |
| 403 Forbidden | Brak uprawnień do zasobu |
| 404 Not Found | Zły endpoint lub brak zasobu |
| 422 Unprocessable | Dane przeszły format, ale są logicznie złe |
| 500 Internal Server Error | Problem po stronie serwera |
| Timeout / brak response | Problem sieciowy lub zawieszenie serwera |

### Krok 4 — Odtworzenie w Postman/Bruno

1. Skopiuj request z proxy do Postmana/Bruno
2. Wykonaj ręcznie — czy błąd powtarza się?
3. Zmodyfikuj parametry — czy możesz zreprodukować i wyeliminować problem?

### Krok 5 — Wnioski i zgłoszenie

Po analizie możesz teraz powiedzieć:

- **Frontend bug**: request jest zły (zły format, brakujące pole, zły endpoint)
- **Backend bug**: request jest OK, ale response jest błędny lub server zwraca 5xx
- **Data bug**: dane w bazie są złe, choć komunikacja jest poprawna
- **Auth bug**: token wygasa zbyt szybko, nie jest odświeżany
- **Config bug**: zły URL, zły klucz API, brakująca konfiguracja środowiska

**Do Jiry dołącz:** request (bez tokenów produkcyjnych!), response, status code, środowisko (dev/staging/prod), kroki do reprodukcji.
