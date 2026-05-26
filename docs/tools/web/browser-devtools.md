# Browser DevTools

## Kategoria

- Główna kategoria: `web-testing`
- Podkategoria: `debugging`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Wbudowane narzędzie developerskie przeglądarki (Chrome, Firefox, Safari) — pozwala testerowi zobaczyć co dzieje się "pod maską" aplikacji webowej: requesty sieciowe, błędy JavaScript, zasoby strony, wydajność.

Odpowiednik ADB logcat + Charles Proxy dla aplikacji webowych — wszystko w jednym miejscu, zero instalacji.

## Najlepsze zastosowania

- analiza requestów API (Network tab) — jak aplikacja mobilna z ADB/proxy
- odczyt błędów JavaScript (Console tab)
- inspekcja elementów UI (Elements tab) — sprawdzanie CSS, marginesów, fontów
- symulacja urządzeń mobilnych (Device Toolbar)
- sprawdzanie localStorage, cookies, sessionStorage (Application tab)
- audit wydajności i dostępności (Lighthouse tab)

## Kiedy używać

Gdy testujesz aplikację webową, panel admina lub PWA i chcesz zobaczyć requesty, błędy w konsoli lub sprawdzić wartości elementów CSS bez narzędzi zewnętrznych.

Otwórz DevTools na początku każdej sesji testowej — nie dopiero gdy coś idzie nie tak.

## Pierwsze 5 akcji

1. Otwórz DevTools: **F12** lub **Ctrl+Shift+I** (Cmd+Option+I na Mac)
2. Network tab → odśwież stronę → obserwuj requesty
3. Console tab → sprawdź czerwone błędy JavaScript
4. Elements tab → kliknij prawym na element → Inspect
5. Device Toolbar (**Ctrl+Shift+M**) → symulacja iPhone/Android

## Najważniejsze zakładki dla testera

| Zakładka | Co sprawdzasz | Kluczowy skrót |
|---|---|---|
| **Network** | Requesty API, status codes, czas ładowania, payload | Filtr: XHR/Fetch dla API |
| **Console** | Błędy JS, ostrzeżenia, logi debug, wyjątki | `console.error` → czerwony |
| **Elements** | HTML, CSS, marginesy, czcionki, wartości dp | Prawy klik → Inspect |
| **Application** | localStorage, sessionStorage, cookies, Service Workers | Źródło danych sesji |
| **Performance** | Czas renderowania, Frame rate, bottlenecki | Nagraj i analizuj |
| **Lighthouse** | Audit: performance, accessibility, SEO, PWA | Generate report |
| **Sources** | JavaScript source maps, breakpointy | Dla zaawansowanych |

## Praktyczne workflow dla testera

### Analiza błędu API
```
1. Otwórz Network tab
2. Odśwież stronę lub wykonaj akcję
3. Filtruj po: XHR / Fetch
4. Kliknij request → zakładka Response
5. Sprawdź: status code, body odpowiedzi
6. Zakładka Headers → Authorization header (token)
7. Prawy klik na request → Copy → Copy as cURL → wklej do Postmana
```

### Weryfikacja błędu UI (marginesy, kolory)
```
1. Kliknij prawym na element → Inspect
2. Panel Styles po prawej → sprawdź margin/padding
3. Zakładka Computed → rzeczywiste obliczone wartości
4. Porównaj z projektem w Figma Dev Mode
5. Zrób screenshot z otwartym panelem Elements → dołącz do buga
```

### Sprawdzenie localStorage / cookies
```
1. Application tab → Storage → Local Storage
2. Wybierz domenę aplikacji
3. Sprawdź wartości: sesja, preferencje, cache
4. Możesz ręcznie edytować lub usuwać wartości → testuj obsługę braku sesji
```

## Następny krok

Naucz się filtrowania w Network tab (XHR/Fetch dla API) i kopiowania requestów jako cURL do Postmana. Następnie zainstaluj axe DevTools do testów dostępności.

## Ryzyka i ograniczenia

- DevTools są specyficzne dla przeglądarki — Chrome DevTools ≠ Firefox DevTools (szczególnie zakładka Performance).
- Niektóre informacje są niedostępne bez source maps (minifikowany kod → trudne debugowanie JS).
- Device Toolbar symuluje rozmiar ekranu, ale nie dotyk ani performancę mobilną — testuj na realnych urządzeniach.
- Console.log może być wyłączony w buildach produkcyjnych — puste Console ≠ brak błędów.

## Link

https://developer.chrome.com/docs/devtools/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Web. Naucz mnie Browser DevTools praktycznie dla testera manualnego.
Chcę wiedzieć:
1. Jak analizować requesty API w Network tab?
2. Jak odczytać i zrozumieć błędy w Console?
3. Jak sprawdzić wartości CSS elementu w Elements tab?
4. Jak symulować urządzenia mobilne?
5. Jak skopiować request z DevTools do Postmana?
```
