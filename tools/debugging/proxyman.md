# Proxyman

## Kategoria

- Główna kategoria: `debugging`
- Podkategoria: `proxy`
- Darmowe: `True` (plan basic; płatne dla zaawansowanych funkcji)
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Przechwytuje i wyświetla cały ruch HTTP/HTTPS aplikacji mobilnej — pozwala zobaczyć, jakie dane aplikacja wysyła do serwera i co serwer odpowiada. Na macOS uznawane za najwygodniejszy w obsłudze proxy.

## Najlepsze zastosowania

- podgląd requestów i odpowiedzi JSON w czasie rzeczywistym,
- edycja odpowiedzi serwera (Map Local / Map Remote) — testowanie błędów bez angażowania backendowca,
- mockowanie odpowiedzi (np. ujemne saldo, błąd 500, timeout),
- analiza SSL/HTTPS na urządzeniach fizycznych iOS i Android,
- weryfikacja payload — czy aplikacja wysyła poprawne dane do API.

## Kiedy używać

Używaj Proxymana wtedy, gdy chcesz ocenić, czy błąd leży w aplikacji (Frontend) czy na serwerze (Backend). Zamiast pytać backendowca o spreparowanie błędnych danych w bazie — sam podmień odpowiedź serwera w Proxymanie i sprawdź, jak aplikacja reaguje.

## Pierwszy praktyczny workflow

1. Zainstaluj Proxyman na macOS (brew install --cask proxyman lub ze strony).
2. Uruchom Proxyman — automatycznie ustawi się jako systemowy proxy.
3. Na telefonie iOS: zainstaluj certyfikat przez Settings > General > VPN & Device Management.
4. Na telefonie Android: skonfiguruj proxy Wi-Fi na IP komputera, port 9090.
5. Otwórz aplikację na telefonie — obserwuj requesty w Proxymanie w czasie rzeczywistym.

## Map Local — testowanie bez backendowca

1. Kliknij prawym przyciskiem na request w Proxymanie.
2. Wybierz Tools > Map Local.
3. Wskaż lokalny plik JSON z podmienioną odpowiedzią (np. ujemne saldo, brakujące pole).
4. Uruchom daną akcję w aplikacji mobilnej.
5. Obserwuj, jak frontend obsługuje niepoprawne dane.

## Następny krok

Naucz się generować "złe" JSONy za pomocą AI (patrz: prompty/api-testing-prompts.md) i wstrzykiwać je przez Map Local do testów error-state aplikacji.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Darmowy plan ma ograniczenia — sprawdź aktualne warunki na stronie.
- macOS-first — na Windows użyj Fiddler Everywhere lub mitmproxy.
- Android 7+ blokuje user certs domyślnie — wymaga debug build z `network_security_config.xml`.
- Nie wklejaj przechwyconego ruchu (tokenów, danych użytkowników) do publicznych narzędzi AI.

## Jak przygotować dane dla LLM

Gdy chcesz, aby AI pomogło Ci przeanalizować ruch lub wygenerować złe JSONy:

```text
Mam poniższy request i response z Proxymana. Pomóż mi:
1. Ocenić, czy błąd jest po stronie Frontend czy Backend
2. Wygenerować 3 zepsute wersje tego JSON do testowania przez Map Local
   (złe typy, brakujące pola, wartości graniczne)
3. Sformułować tytuł buga do Jiry

Request: [KLIKNIJ PRAWYM → COPY AS CURL i wklej]
Response: [WKLEJ BODY]
```

## Troubleshooting — najczęstsze problemy

| Problem | Przyczyna | Rozwiązanie |
|---|---|---|
| Nie widzę HTTPS | Certyfikat niezainstalowany | Proxyman → Certificate → Install certificate on this device |
| Android nie ufa certyfikatowi | Android 7+ blokuje user certs | Debug build z `network_security_config.xml` od dewelopera |
| iOS nie ufa certyfikatowi | Certyfikat niezaufany | Settings → General → VPN → zaufaj + włącz w Certificate Trust Settings |
| Telefon łączy się, ale nie przechwytuje | Różne sieci WiFi | Telefon i komputer muszą być w tej samej sieci WiFi |
| Map Local nie podmienia | Zła reguła URL pattern | Sprawdź, czy URL w regule Map Local pasuje dokładnie |
| Certificate pinning blokuje | Apka weryfikuje certyfikat | Tylko debug build — poproś dewelopera o wyłączenie pinning |

## Link

https://proxyman.io/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Proxyman praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych na macOS.
Chcę wiedzieć:
1. kiedy używać (vs mitmproxy vs Charles Proxy),
2. jak skonfigurować proxy na telefonie iOS i Android,
3. jak używać Map Local do podmieniana odpowiedzi serwera,
4. jak wygenerować broken JSON do testowania error states,
5. jak udokumentować znaleziony błąd API w raporcie buga,
6. jaki jest następny krok w kierunku automatyzacji testów API.
```
