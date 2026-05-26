# HTTP Toolkit

## Kategoria

- Główna kategoria: `api-testing`
- Podkategoria: `http-proxy`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Przechwytywanie i modyfikowanie zapytań HTTP/HTTPS z aplikacji Android w czasie rzeczywistym — połączenie przez kod QR bez ręcznej instalacji certyfikatów, idealne do weryfikacji co aplikacja wysyła do API.

## Najlepsze zastosowania

- podglądanie wszystkich requestów HTTP/HTTPS wysyłanych przez aplikację mobilną
- mockowanie odpowiedzi API (np. zwróć błąd 500) bez modyfikacji backendu
- testowanie zachowania aplikacji przy problemach sieciowych
- weryfikacja czy aplikacja wysyła poprawne nagłówki autoryzacyjne
- debugowanie błędów API trudnych do odtworzenia w innych warunkach

## Kiedy używać

Używaj tego narzędzia wtedy, gdy aplikacja zachowuje się dziwnie i podejrzewasz problem po stronie API — chcesz zobaczyć dokładnie co telefon wysyła i co dostaje w odpowiedzi, bez dostępu do backendu ani narzędzi deweloperskich.

## Pierwszy praktyczny workflow

1. Pobierz i zainstaluj HTTP Toolkit z httptoolkit.com na komputerze (Windows/macOS/Linux).
2. Otwórz HTTP Toolkit > kliknij kafel `Android device via ADB` lub `Android device via QR code`.
3. Zeskanuj wyświetlony kod QR telefonem — HTTP Toolkit automatycznie konfiguruje proxy i certyfikat.
4. Otwórz testowaną aplikację na telefonie i wykonaj akcję (np. zaloguj się).
5. Wróć do HTTP Toolkit — wszystkie requesty pojawiają się na liście. Kliknij jeden, żeby zobaczyć nagłówki, body, odpowiedź. Kliknij prawym przyciskiem > `Mock response` żeby zwrócić inną odpowiedź.

## Następny krok

Użyj przechwyconych requestów w Postman lub Bruno — wklej URL, nagłówki i body, żeby odtworzyć i zmodyfikować zapytanie bez uruchamiania aplikacji mobilnej.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Android 7+ blokuje certyfikaty użytkownika w aplikacjach produkcyjnych — pełne przechwytywanie HTTPS działa pewnie tylko z buildami debug lub aplikacjami ze skonfigurowanym `network_security_config.xml`.

## Link

https://httptoolkit.com/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia HTTP Toolkit praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
