# Workflow: analiza błędu API

## Cel

Zawęzić problem do klienta, API, danych, autoryzacji, sieci lub konfiguracji środowiska. Zebrać dowody techniczne bez przypisywania właściciela wyłącznie na podstawie kodu HTTP.

## Kiedy używać

Gdy aplikacja pokazuje błąd, pusty ekran, nieprawidłowe dane lub nie wykonuje akcji — a podejrzewasz, że to problem z komunikacją z serwerem.

## Dane wejściowe

- środowisko i wersja aplikacji,
- akcja wywołująca problem,
- kontrakt API lub dokumentacja endpointu,
- kontrolowane konto i dane testowe.

## Narzędzia

- [HTTP Toolkit](../tools/api/http-toolkit.md), [mitmproxy](../tools/debugging/mitmproxy.md), [Proxyman](../tools/debugging/proxyman.md) lub Charles — przechwycenie ruchu
- [Postman](../tools/api/postman.md) lub [Bruno](../tools/api/bruno.md) — kontrolowane odtworzenie requestu
- [OpenAPI/Swagger](../tools/api/openapi-swagger.md) — porównanie z kontraktem
- [Ollama](../tools/ai/ollama.md) — opcjonalna, lokalna interpretacja zanonimizowanego response

---

## Kroki

### Krok 1 — Przechwycenie ruchu

1. Uruchom proxy w zatwierdzonym środowisku testowym.
2. Wykonaj akcję w aplikacji, która powoduje problem.
3. Zidentyfikuj podejrzany request i zapisz jego timestamp oraz correlation/request ID.
4. Utwórz zanonimizowaną kopię requestu i response do dalszej analizy.

### Krok 2 — Analiza requestu

Sprawdź kolejno:

| Co sprawdzić | Jak |
| --- | --- |
| Metoda HTTP | GET/POST/PUT/DELETE — czy poprawna? |
| URL | Czy endpoint jest poprawny? Czy nie ma literówki? |
| Nagłówki | Authorization, Content-Type, Accept |
| Body | Czy payload jest poprawnie sformatowany? |
| Token | Czy jest? Czy nie wygasł? |
| Kontrakt | Czy request spełnia aktualną specyfikację OpenAPI? |
| Identyfikator | Czy correlation/request ID pozwala znaleźć log serwera? |

### Krok 3 — Analiza response

| Status code | Co może oznaczać |
| --- | --- |
| 200 OK | Serwer odpowiedział — sprawdź body i reguły biznesowe |
| 400 Bad Request | Request został odrzucony — porównaj dane i format z kontraktem |
| 401 Unauthorized | Brak/zły/wygasły token |
| 403 Forbidden | Brak uprawnień do zasobu |
| 404 Not Found | Zły endpoint lub brak zasobu |
| 422 Unprocessable | Dane przeszły format, ale są logicznie złe |
| 500 Internal Server Error | Serwer nie obsłużył requestu — potrzebne są logi i correlation ID |
| Timeout / brak response | Sprawdź klienta, sieć, proxy, DNS i dostępność serwera |

### Krok 4 — Odtworzenie w Postman/Bruno

1. Skopiuj zanonimizowany request z proxy do Postmana/Bruno.
2. Wykonaj go na środowisku testowym — czy błąd się powtarza?
3. Porównaj wynik z kontraktem i znanym poprawnym requestem.
4. Zmieniaj po jednym parametrze, zapisując wpływ każdej zmiany.

### Krok 5 — Wnioski i zgłoszenie

Po analizie możesz teraz powiedzieć:

- **Błąd klienta**: request nie spełnia kontraktu lub klient błędnie interpretuje poprawny response.
- **Błąd API**: request spełnia kontrakt, ale response lub efekt operacji jest niezgodny z kontraktem.
- **Błąd danych**: komunikacja jest poprawna, ale dane źródłowe lub wynikowe są niepoprawne.
- **Błąd autoryzacji**: problem dotyczy tokenu, odświeżania sesji lub uprawnień.
- **Błąd konfiguracji**: klient korzysta ze złego endpointu lub konfiguracji środowiska.
- **Hipoteza niepotwierdzona**: brakuje logu serwera, kontraktu lub korelacji requestu.

Do systemu zgłoszeń dołącz: zanonimizowany request/response, status code, correlation ID, środowisko, timestamp, kroki reprodukcji, oczekiwany rezultat i poziom pewności hipotezy.

## Wynik i kryteria zakończenia

Workflow jest zakończony, gdy problem jest odtworzony albo opisano, dlaczego nie można go odtworzyć, a dowody pozwalają zespołowi sprawdzić hipotezę bez ponownego zbierania podstawowych danych.

## Prywatność i bezpieczeństwo

- Nie dołączaj tokenów, cookies, kluczy API, haseł, danych osobowych ani pełnych payloadów produkcyjnych.
- Nie odtwarzaj requestów modyfikujących dane na produkcji.
- Proxy konfiguruj tylko na kontrolowanym urządzeniu i zatwierdzonym środowisku.
- Dane wewnętrzne analizuj lokalnie; wynik AI traktuj jako wskazówkę, nie dowód.

## Powiązane materiały

- [Prompty do testowania API](../prompts/api-testing-prompts.md)
- [Szablon zgłoszenia błędu](../templates/bug-report-template.md)
- [Analiza błędu w aplikacji mobilnej](bug-investigation-mobile.md)
