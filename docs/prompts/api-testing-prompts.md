# Prompty do testowania API

## Generowanie "złych" danych JSON (mock API testing)

```text
Mam poniższą strukturę JSON z API (lub dokumentacji Swagger/OpenAPI).
Wygeneruj 5 różnych zepsutych wersji tego JSON, które wstrzyknę przez proxy
(Proxyman / mitmproxy) do aplikacji mobilnej, aby przetestować jak frontend
obsługuje błędne odpowiedzi serwera.

Typy błędów do wygenerowania:
1. Brakujące wymagane pole (missing required field)
2. Zły typ danych (np. string zamiast int, null zamiast object)
3. Ekstremalnie długi string (10 000 znaków)
4. Wartości graniczne (ujemna liczba, 0, bardzo duża liczba)
5. Puste tablice i null zamiast obiektów

Dla każdego wariantu napisz: co zmieniłeś i jakiego zachowania UI się spodziewam.

JSON: [WKLEJ]
```

## Analiza request/response — ocena błędu

```text
Jesteś QA z doświadczeniem w API i mobile. Przeanalizuj ten request/response.

Wskaż:
1. Czy request wygląda poprawnie (metoda, nagłówki, payload)?
2. Czy response pasuje do oczekiwanego zachowania?
3. Gdzie leży błąd: Frontend (aplikacja) czy Backend (serwer)?
4. Jakie dodatkowe testy API warto wykonać?
5. Co dokładnie dołączyć do raportu buga (jakie pola, nagłówki, status code)?

Request: [WKLEJ]
Response: [WKLEJ]
```

## Generowanie danych testowych dla API

```text
Dla tego endpointa API wygeneruj kompletny zestaw danych testowych:

Endpoint: [METODA URL]
Parametry: [OPIS lub schema]
Autoryzacja: [Bearer/Basic/API Key/brak]

Wygeneruj:
1. Dane poprawne — happy path (minimum 2 warianty)
2. Dane niepoprawne — negative cases (złe typy, brakujące pola)
3. Dane graniczne — boundary values
4. Dane bezpieczeństwa — SQL injection pattern, XSS pattern, bardzo długie stringi
5. Scenariusz braku autoryzacji (brak tokenu, wygasły token, zły token)
```

## Zrozumienie odpowiedzi API (dla testera bez tła backendowego)

```text
Jestem testerem manualnym bez doświadczenia backendowego.
Wyjaśnij mi tę odpowiedź API prostym językiem:

1. Co oznacza ten status code w kontekście tej aplikacji?
2. Czy ta odpowiedź jest poprawna dla tego rodzaju requestu?
3. Na co zwrócić uwagę w nagłówkach (headers)?
4. Jakie pola w body są podejrzane lub nieoczekiwane?
5. Czy widzisz potencjalny bug — frontend, backend czy konfiguracja?

Request: [WKLEJ]
Response: [WKLEJ]
```

## Analiza logów z Logcata — dla bug reportu

```text
Oto fragment logów z Android Studio (Logcat) z momentu wywalenia się aplikacji.

Proszę o:
1. Zidentyfikowanie głównego błędu (Exception / Error)
2. Wskazanie pliku i linii kodu (jeśli widoczne w stack trace)
3. Prostego, 2-zdaniowego technicznego podsumowania do ticketu w Jirze
4. Informacji: błąd apki, systemu Android czy serwera?
5. Listy informacji, które warto dołączyć do bug reportu

Logi: [WKLEJ]
```

## Tworzenie scenariusza Maestro z opisu (mobile API + UI)

```text
Napisz prosty scenariusz testowy w formacie YAML dla narzędzia Maestro.

Aplikacja: [ID APLIKACJI, np. com.example.app]
Platforma: [Android/iOS]

Kroki do zautomatyzowania:
[LISTA KROKÓW]

Wymagania:
- Dodaj komentarze przy każdym kroku
- Użyj waitForAnimationToEnd przed interakcjami
- Dodaj assertVisible dla potwierdzenia sukcesu
- Użyj tapOn z tekstem (nie XPath) gdzie możliwe
```
