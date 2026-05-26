# Słownik QA — Praktyczny Przewodnik dla Juniorów

Terminy ułożone tematycznie. Ucz się całych kategorii naraz — mają wspólny kontekst.

---

## Terminy mobilne

| Termin | Wyjaśnienie | Przykład kontekstu |
|---|---|---|
| **APK** | Plik instalacyjny aplikacji Android (Android Package Kit). Odpowiednik .exe na Windowsie lub .ipa na iOS. | „Wyślij mi APK z ostatniego buildu, zainstaluję ręcznie przez ADB." |
| **ADB** | Android Debug Bridge — narzędzie linii komend do komunikacji z urządzeniem Android. Pozwala instalować APK, zbierać logi, nagrywać ekran. | `adb logcat -s "MyApp"` — logi tylko z naszej aplikacji |
| **logcat** | Strumień logów systemowych i aplikacyjnych w Androidzie. Twoim głównym źródłem danych technicznych przy debugowaniu. | „Odtwórz crash i wklej logcat z 30 sekund przed i po błędzie." |
| **ANR** | Application Not Responding — aplikacja Android przestała reagować na dotyk przez ponad 5 sekund. System proponuje wymuszenie zamknięcia. | „W logcat widzę ANR w wątku głównym — aplikacja zamroziła się przy ładowaniu listy." |
| **Crash** | Nagłe, niekontrolowane zakończenie działania aplikacji. Różni się od ANR — crash to awaria, ANR to zawieszenie. | „Crash reprodukuję po 3 kliknięciach Wstecz z ekranu płatności." |
| **Emulator** | Softwarowa symulacja urządzenia fizycznego — całe oprogramowanie. Android Studio AVD to emulator. Wolniejszy, ale elastyczny. | „Na emulatorze Pixel 5 API 33 crash nie reprodukuje — sprawdź na realu." |
| **Simulator** | Uproszczona symulacja środowiska (nie sprzętu). Xcode Simulator na iOS to simulator, nie emulator. Brak pełnego tłumaczenia kodu maszynowego. | „Na iPhone 15 Simulator gesty działają inaczej niż na realu — przetestuj na urządzeniu przed release." |
| **Deep link** | URL-like adres otwierający konkretny ekran w aplikacji. Format: `myapp://product/123` lub `https://myapp.com/product/123`. | „Testuj deep linki z powiadomień, emaili i SMS — każdy powinien otworzyć właściwy ekran." |
| **Push notification** | Wiadomość przesyłana przez serwer do aplikacji, wyświetlana nawet gdy aplikacja jest zamknięta. | „Sprawdź push notification gdy aplikacja jest: na pierwszym planie, w tle i całkowicie zamknięta." |
| **Certificate pinning** | Mechanizm bezpieczeństwa — aplikacja akceptuje tylko konkretny certyfikat SSL, nie dowolny z zaufanego CA. Utrudnia przechwytywanie requestów przez proxy. | „Proxy nie przechwytuje requestów — aplikacja ma certificate pinning. Potrzebujesz buildu testowego z wyłączonym pinningiem." |

---

## Terminy API

| Termin | Wyjaśnienie | Przykład kontekstu |
|---|---|---|
| **Endpoint** | Konkretny URL API obsługujący daną operację. Składa się z adresu bazowego + ścieżki. | `POST /api/v1/users/login` — endpoint logowania |
| **Request** | Zapytanie wysyłane do serwera. Składa się z: metody HTTP, URL, nagłówków, opcjonalnego body. | „Wyślij request POST z credentials i sprawdź response." |
| **Response** | Odpowiedź serwera na request. Składa się z: status code, nagłówków, body (zwykle JSON). | „Response 200 z tokenem — logowanie działa. Response 401 — błędne hasło." |
| **Payload** | Dane przesyłane w body requestu lub response. Najczęściej JSON. | `{"email": "test@test.com", "password": "Test1234!"}` — payload logowania |
| **Status code** | Trzycyfrowy kod HTTP opisujący wynik requestu. 2xx = sukces, 4xx = błąd klienta, 5xx = błąd serwera. | „500 Internal Server Error — to błąd serwera, nie użytkownika — eskaluj do backendu." |
| **Token** | Ciąg znaków potwierdzający tożsamość zalogowanego użytkownika. Wysyłany w nagłówku każdego requestu po zalogowaniu. | `Authorization: Bearer eyJhbGci...` — nagłówek z tokenem |
| **JWT** | JSON Web Token — standard tokenu zawierający dane użytkownika zakodowane w Base64. Można zdekodować na jwt.io. | „Zdekoduj JWT i sprawdź pole `exp` — jeśli timestamp jest w przeszłości, token wygasł." |
| **REST** | Styl architektury API oparty na HTTP. Używa URL-i do zasobów i metod HTTP do operacji. Najpopularniejszy standard. | „Nasze API jest RESTowe: GET /users pobiera listę, POST /users tworzy użytkownika." |
| **JSON** | JavaScript Object Notation — lekki format wymiany danych, standard dla REST API. Czytelny dla człowieka. | `{"id": 42, "name": "Anna", "active": true}` |
| **GET** | Metoda HTTP do pobierania danych. Nie zmienia stanu serwera. Parametry w URL. | `GET /api/products?category=phones` — pobierz produkty z kategorii |
| **POST** | Metoda HTTP do tworzenia nowych zasobów lub wysyłania danych. Body w request. | `POST /api/orders` — utwórz nowe zamówienie |
| **PUT / PATCH** | PUT zastępuje cały zasób, PATCH aktualizuje wybrane pola. Oba modyfikują istniejące dane. | `PATCH /api/users/42` z `{"name": "Anna Nowak"}` — zmień tylko imię |
| **DELETE** | Metoda HTTP do usuwania zasobów. | `DELETE /api/sessions/abc123` — wyloguj / usuń sesję |
| **Header** | Metadane dołączane do requestu lub response. Zawierają tokeny, typ treści, language itp. | `Content-Type: application/json` — informuje serwer że wysyłamy JSON |
| **Authentication** | Weryfikacja tożsamości — „Kim jesteś?". Logowanie, token, sesja. | „Testuj autentykację: poprawne dane → token, błędne hasło → 401." |
| **Authorization** | Weryfikacja uprawnień — „Co możesz zrobić?". Następuje po autentykacji. | „User z rolą `viewer` nie może usuwać — testuj 403 Forbidden dla zabronionych akcji." |
| **Mock** | Fałszywy serwer lub obiekt zastępujący prawdziwy podczas testów. Zwraca zaprojektowane odpowiedzi. | „Użyj mocka API do testowania obsługi błędu 503 — nie czekaj na awarię produkcji." |
| **Stub** | Uproszczona implementacja zastępująca realny komponent — zwraca stałą wartość. Prostszy niż mock. | „Stub funkcji logowania zawsze zwraca sukces — izolujemy test od bazy danych." |

---

## Terminy automatyzacji

| Termin | Wyjaśnienie | Przykład kontekstu |
|---|---|---|
| **Selector / Locator** | Sposób identyfikacji elementu UI w kodzie testu. Może być: resource-id, XPath, CSS selector, tekst. | `By.id("com.app:id/login_button")` — selector Android |
| **Assertion** | Weryfikacja warunku w teście. Test failuje jeśli warunek jest fałszywy. | `assertVisible("Zalogowano pomyślnie")` — sprawdź czy komunikat jest widoczny |
| **Test suite** | Zbiór powiązanych test cases uruchamianych razem. | „Smoke suite zawiera 15 TC pokrywających krytyczne ścieżki aplikacji." |
| **Smoke test** | Minimimalny zestaw testów sprawdzający czy aplikacja w ogóle działa. Uruchamiany po każdym buildzie. | „Smoke test: logowanie, główny ekran, wylogowanie — trwa 5 minut." |
| **Regression testing** | Testy sprawdzające czy nowe zmiany nie zepsuły istniejącej funkcjonalności. | „Po wdrożeniu hotfixa uruchom regresję modułu płatności." |
| **Flaky test** | Test dający niepowtarzalne wyniki — raz przechodzi, raz failuje bez zmiany kodu. Zaufanie do suite spada. | „Ten test jest flaky — fails co 5 uruchomień przez timing issue. Dodaj explicit wait." |
| **CI/CD** | Continuous Integration / Continuous Delivery — automatyczny pipeline: kod → build → testy → deploy. | „Testy smoke uruchamiają się automatycznie w CI po każdym merge do main." |
| **YAML** | Format pliku konfiguracyjnego — czytelny, oparty na wcięciach. Używany przez Maestro, GitHub Actions. | Plik `.yaml` definiujący flow testowy Maestro lub pipeline CI/CD |

---

## Terminy procesowe QA

| Termin | Wyjaśnienie | Przykład kontekstu |
|---|---|---|
| **Bug report** | Formalne zgłoszenie błędu zawierające: tytuł, kroki reprodukcji, wynik aktualny, wynik oczekiwany, środowisko, załączniki. | „Bug report bez kroków reprodukcji to strata czasu dewelopera — zawsze podaj minimum 3 kroki." |
| **Severity** | Waga techniczna błędu — jak bardzo psuje aplikację. Niezależna od priorytetu biznesowego. | Severity Critical: crash przy każdym uruchomieniu. Severity Low: literówka w stopce. |
| **Priority** | Pilność naprawy błędu — kiedy powinno być naprawione. Decyzja biznesowa, nie techniczna. | „Bug z severity Low może mieć priority High, gdy dotyczy ekranu rejestracji." |
| **Test case (TC)** | Dokumentacja jednego scenariusza testowego: warunki wstępne, kroki, oczekiwany wynik. | „TC: Logowanie z poprawnym emailem i hasłem → oczekiwany wynik: ekran główny." |
| **Test plan** | Dokument opisujący zakres, podejście, zasoby i harmonogram testów dla projektu lub wersji. | „Test plan dla release 2.5 obejmuje: nowe funkcje, regresję płatności, testy na 3 urządzeniach." |
| **Exploratory testing** | Testowanie bez skryptów — tester jednocześnie uczy się, projektuje i wykonuje testy. Oparte na doświadczeniu. | „Po godzinie eksploracji modułu notyfikacji znalazłam 3 bugi nieobsłużone w TC." |
| **UAT** | User Acceptance Testing — testy akceptacyjne przez klienta lub end userów przed wdrożeniem produkcyjnym. | „UAT w piątek z klientem — przygotuj środowisko testowe i konta demo." |
| **Acceptance criteria** | Warunki, które muszą być spełnione żeby user story był uznany za ukończony. Część definicji „done". | „AC: użytkownik może zalogować się przez Google w maksymalnie 2 klikach." |
| **DoD** | Definition of Done — lista kryteriów, które muszą być spełnione zanim zadanie może być oznaczone jako ukończone. | DoD: kod zreview'owany, testy jednostkowe napisane, smoke test przeszedł, dokumentacja zaktualizowana. |

---

## Terminy proxy / sieciowe

| Termin | Wyjaśnienie | Przykład kontekstu |
|---|---|---|
| **Proxy** | Pośrednik sieciowy stojący między klientem a serwerem. Tester używa go do przechwytywania i analizowania requestów. | „Skonfiguruj proxy Charles/mitmproxy na port 8888, ustaw w telefonie ten sam port." |
| **SSL certificate** | Certyfikat kryptograficzny pozwalający na szyfrowanie HTTPS. Proxy instaluje własny certyfikat CA żeby odszyfrować ruch. | „Zainstaluj certyfikat CA mitmproxy w systemie żeby widzieć HTTPS jako plaintext." |
| **Request intercepting** | Przechwytywanie requestów sieciowych w locie — umożliwia podgląd, modyfikację lub odrzucenie requestów. | „Przechwyciłam request płatności i zmieniłam kwotę — serwer powinien odrzucić modyfikację." |
| **Traffic** | Wszystkie dane sieciowe przepływające między klientem a serwerem. | „Filtruj traffic po domenie `api.myapp.com` żeby widzieć tylko nasze requesty." |

---

## Terminy AI

| Termin | Wyjaśnienie | Przykład kontekstu |
|---|---|---|
| **LLM** | Large Language Model — duży model językowy (np. GPT-4, Claude, Llama). Bazowy mechanizm za ChatGPT, Copilot itp. | „Ollama uruchamia lokalny LLM bez wysyłania danych do chmury." |
| **Prompt** | Instrukcja/zapytanie podawane modelowi AI. Jakość prompta bezpośrednio wpływa na jakość odpowiedzi. | „Prompt zbyt ogólny → test cases pasujące do każdej aplikacji. Dodaj kontekst projektu." |
| **RAG** | Retrieval Augmented Generation — technika łącząca LLM z zewnętrzną bazą wiedzy. AI najpierw przeszukuje dokumenty, potem odpowiada. | „Ten repo jako RAG — AI odpowiada na pytania o narzędzia korzystając z naszych plików .md." |
| **Local model** | Model LLM uruchamiany lokalnie na własnym komputerze (Ollama, LM Studio). Dane nie opuszczają maszyny. | „Używam lokalnego modelu do analizy logów z tokenami produkcyjnymi — żadne dane nie idą do chmury." |
| **Hallucination** | Sytuacja gdy AI pewnie opisuje coś, czego nie ma — wymyśla funkcje, API, metody które nie istnieją. | „AI opisało endpoint `/api/users/batch-delete` — sprawdź w Swaggerze czy w ogóle istnieje." |
| **Token limit** | Maksymalna liczba tokenów (fragmentów tekstu) jaką model może przetworzyć w jednym zapytaniu. Zbyt długi kontekst → ucięcie lub pogorszone odpowiedzi. | „Logcat ma 50k linii — nie wklejaj całego do AI. Filtruj do 200 linii przed crashem." |
