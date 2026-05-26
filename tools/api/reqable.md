# Reqable

## Kategoria

- Główna kategoria: `api-testing`
- Podkategoria: `all-in-one-api-client`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Klient API i proxy HTTP w jednej aplikacji desktopowej — łączy funkcje Postmana (ręczne wysyłanie requestów) z funkcjami Charles Proxy (przechwytywanie ruchu aplikacji) plus widok diff do porównywania dwóch odpowiedzi.

## Najlepsze zastosowania

- przechwytywanie ruchu HTTP/HTTPS z aplikacji mobilnych (jak Charles Proxy)
- ręczne wysyłanie i modyfikowanie requestów API (jak Postman)
- porównywanie odpowiedzi API z dwóch środowisk (diff view)
- testowanie WebSocket i HTTP/2 (lepsza obsługa niż w Postmanie)
- zastąpienie Charlesa i Postmana jednym narzędziem

## Kiedy używać

Używaj tego narzędzia wtedy, gdy potrzebujesz zarówno przechwycić ruch z aplikacji mobilnej jak i ręcznie modyfikować requesty — zamiast otwierać dwa oddzielne narzędzia (Charles + Postman), Reqable łączy obie funkcje w jednym oknie.

## Pierwszy praktyczny workflow

1. Pobierz Reqable z reqable.com i zainstaluj na komputerze (Windows/macOS/Linux).
2. Przejdź do trybu `Capture` > zainstaluj certyfikat CA Reqable na urządzeniu mobilnym według instrukcji w aplikacji.
3. Skonfiguruj proxy na telefonie (adres IP komputera, port Reqable) > otwórz aplikację mobilną.
4. Obserwuj przychodzące requesty w trybie Capture — kliknij dowolny, żeby zobaczyć szczegóły.
5. Kliknij prawym przyciskiem na przechwycony request > `Send to API Client` > zmodyfikuj i wyślij ponownie z panelu API.

## Następny krok

Porównaj Reqable z Bruno jako głównym klientem API do codziennej pracy — Bruno jest lepszy do testów lokalnych przechowywanych w repo, Reqable góruje jako zamiennik Charles Proxy.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — Reqable to stosunkowo nowe narzędzie, sprawdź aktualne warunki cenowe przed wdrożeniem w zespole.
- Mniejsza społeczność i ekosystem pluginów niż Postman — może brakować niektórych integracji.

## Link

https://reqable.com/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Reqable praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
