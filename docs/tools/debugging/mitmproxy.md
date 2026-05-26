# mitmproxy

## Kategoria

- Główna kategoria: `debugging`
- Podkategoria: `proxy`
- Darmowe: `True`
- Poziom trudności: `medium-hard`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Darmowy proxy do przechwytywania i analizowania ruchu HTTP/HTTPS aplikacji mobilnych. Alternatywa open-source dla Charlesa i Fiddlera — działa w terminalu lub przez przeglądarkowy interfejs `mitmweb`.

## Najlepsze zastosowania

- przechwytywanie i analiza requestów mobilnych
- modyfikacja odpowiedzi serwera (mockowanie)
- skryptowanie ruchu w Pythonie (zaawansowane)
- testowanie bezpieczeństwa komunikacji sieciowej
- debug API na urządzeniach Android i iOS

## Kiedy używać

Używaj mitmproxy, gdy chcesz darmowego proxy bez ograniczeń trial. Szczególnie gdy chcesz skryptować ruch przez Python lub potrzebujesz narzędzia, które możesz wdrożyć na CI/CD. Dla codziennego użytku GUI wolisz Proxyman (macOS) lub HTTP Toolkit.

## Kiedy NIE używać

- Gdy potrzebujesz prostego GUI bez terminala → użyj HTTP Toolkit lub Proxyman
- Gdy aplikacja używa certificate pinning w produkcji → wymaga dodatkowych kroków
- Gdy testujesz iOS bez macOS → konfiguracja certyfikatu jest trudniejsza

## Pierwszy praktyczny workflow

1. Zainstaluj: `pip install mitmproxy` lub pobierz binarki ze strony
2. Uruchom interfejs webowy: `mitmweb --port 8080`
3. Na telefonie Android: Ustawienia → WiFi → Proxy → IP komputera, port 8080
4. Pobierz certyfikat: otwórz w przeglądarce telefonu `mitm.it` → zainstaluj certyfikat
5. Otwórz aplikację — obserwuj requesty w `http://127.0.0.1:8081`

## Jak przygotować dane dla LLM

Gdy chcesz, aby AI pomogło Ci zanalizować ruch sieciowy:

```bash
# Eksport do pliku HAR (czytelny przez AI)
mitmdump -w session.mitm
# Następnie: File > Export > HAR w mitmweb

# Lub skopiuj request jako cURL z mitmweb (prawy klik na request)
# i wklej do AI z promptem:
```

```text
Oto request/response z mitmproxy. Przeanalizuj:
1. Czy request wygląda poprawnie?
2. Czy response sugeruje błąd frontend czy backend?
3. Co dołączyć do bug reportu?

[WKLEJ SKOPIOWANY REQUEST/RESPONSE]
```

## Troubleshooting — najczęstsze problemy

| Problem | Przyczyna | Rozwiązanie |
|---|---|---|
| Nie widzę ruchu HTTPS | Certyfikat niezainstalowany | Otwórz `mitm.it` na telefonie i zainstaluj certyfikat dla systemu |
| Android 7+ blokuje certyfikat | Zmiany bezpieczeństwa Android N | Poproś dewelopera o `network_security_config.xml` w debug buildzie |
| iOS nie ufa certyfikatowi | Certyfikat nie jest "trusted" | Settings → General → VPN & Device Management → zaufaj certyfikatowi mitmproxy |
| Telefon ma internet, ale proxy nie przechwytuje | Zły adres IP w konfiguracji proxy | Sprawdź IP komputera: `ipconfig` (Windows) / `ifconfig` (Mac/Linux) |
| mitmweb nie uruchamia się | Port zajęty | Zmień port: `mitmweb --port 8082 --web-port 8083` |
| Certificate pinning blokuje ruch | Apka weryfikuje certyfikat serwera | Wymaga modyfikacji APK (Frida, apktool) — tylko dla debug buildów |

## Następny krok

Naucz się HTTP Toolkit jako prostszej alternatywy do codziennej pracy. Wróć do mitmproxy gdy będziesz chciał skryptować ruch przez Python (`mitmproxy addons`).

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — mitmproxy jest open-source (MIT).
- Android 7+ wymaga debug buildu z odpowiednią konfiguracją sieciową.
- Nie przechwytuj ruchu aplikacji produkcyjnych z danymi użytkowników — etyka i RODO.
- Nie wklejaj przechwyconych tokenów do publicznych narzędzi AI.

## Link

https://mitmproxy.org/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie mitmproxy praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. Jak skonfigurować proxy na Androidzie i iOS krok po kroku,
2. Jak zainstalować certyfikat SSL i co zrobić gdy Android 7+ blokuje,
3. Jak przechwycić request i zmodyfikować response (mock),
4. Jak wyeksportować ruch do HAR i przeanalizować przez AI,
5. Kiedy użyć mitmproxy a kiedy HTTP Toolkit lub Proxyman,
6. Jak zautomatyzować modyfikację ruchu przez Python addons.
```
