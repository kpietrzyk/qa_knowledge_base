# Lighthouse

## Kategoria

- Główna kategoria: `web-testing`
- Podkategoria: `audit`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Lighthouse to narzędzie Google do automatycznego auditu aplikacji webowych. Wbudowane w Chrome DevTools — zero instalacji. W ciągu 30 sekund dostarcza raport z oceną aplikacji w 5 kategoriach: Performance, Accessibility, Best Practices, SEO i PWA.

Dla testera manualnego: gotowa lista konkretnych problemów z linkami do dokumentacji jak je naprawić.

## Najlepsze zastosowania

- szybki audit dostępności (WCAG) z listą konkretnych naruszeń
- sprawdzenie performance score przed i po wdrożeniu
- weryfikacja SEO pod kątem technicznym (meta tagi, robots.txt)
- audit PWA (manifest, Service Worker, offline)
- raport jako załącznik do buga lub test planu

## Kiedy używać

Uruchamiaj Lighthouse przy każdym nowym module lub przed release webowym. Szczególnie cenne przy testach dostępności — zamiast szukać problemów ręcznie, najpierw uruchom Lighthouse, napraw łatwe problemy, potem testuj manualnie trudniejsze.

**Uwaga:** Lighthouse analizuje jedną stronę naraz — uruchom osobno dla: strony głównej, logowania, kluczowych funkcji.

## Pierwsze 5 akcji

1. Otwórz Chrome DevTools (F12) → zakładka **Lighthouse**
2. Wybierz kategorie do sprawdzenia (wszystkie lub konkretne)
3. Wybierz tryb: **Mobile** lub **Desktop**
4. Kliknij **Analyze page load**
5. Przeczytaj raport — czerwone elementy to priorytety

## Jak czytać raport Lighthouse

| Kategoria | Co sprawdza | Na co zwrócić uwagę |
|---|---|---|
| **Performance** | Czas ładowania, Core Web Vitals (LCP, FID, CLS) | Score < 50 = poważny problem; sprawdź LCP > 2.5s |
| **Accessibility** | WCAG violations: kontrast, aria labels, kolejność nagłówków | Każdy błąd to konkretna naprawa z opisem |
| **Best Practices** | HTTPS, bezpieczeństwo, console errors | Console errors tutaj = błędy JavaScript |
| **SEO** | Meta tagi, robots.txt, linki, czytelność | Ważne dla publicznych stron |
| **PWA** | Manifest, Service Worker, możliwość dodania do ekranu | Tylko dla Progressive Web App |

## Accessibility audit — praktycznie

Lighthouse wykrywa automatycznie:
- brakujące alt teksty dla obrazków
- niewystarczający kontrast kolorów (ratio < 4.5:1 dla normalnego tekstu)
- formularze bez etykiet
- nieprawidłową kolejność nagłówków (H1 → H3 bez H2)
- brakujące atrybuty ARIA
- elementy nieinteraktywne bez focusability

**Lighthouse NIE wykryje:**
- problemów z nawigacją klawiaturą (Tab order testuj manualnie)
- błędnych opisów (alt="image1" jest technicznie poprawny, ale bezużyteczny)
- problemów z czytnikami ekranu (testuj NVDA/VoiceOver manualnie)

## Następny krok

Po Lighthouse przejdź do manualnych testów dostępności: nawigacja klawiaturą (Tab), test z czytnikiem ekranu (NVDA/VoiceOver), rozszerzenie axe DevTools do głębszego auditu. Patrz: `tools/web/web-accessibility.md`.

## Ryzyka i ograniczenia

- Wyniki różnią się w zależności od obciążenia sieci i komputera — uruchamiaj kilka razy, bierz średnią.
- Score 100 w Lighthouse ≠ aplikacja bez błędów dostępności — automatyczny audit wykrywa ~30% problemów WCAG.
- Wyniki w trybie Incognito są bardziej stabilne (brak rozszerzeń wpływających na performance).
- Lighthouse testuje cold load — pierwsze ładowanie, nie cached. Dodaj profil „Returning visitor" manualnie.
- Sprawdź licencję przed użyciem komercyjnym.

## Link

https://developer.chrome.com/docs/lighthouse/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Web. Naucz mnie Lighthouse praktycznie dla testera manualnego.
Chcę wiedzieć:
1. Jak uruchomić Lighthouse i co ustawić przed auditem?
2. Jak czytać raport Accessibility — które błędy są krytyczne?
3. Jak interpretować Core Web Vitals (LCP, FID, CLS)?
4. Co Lighthouse wykrywa, a czego nie wykryje i muszę testować manualnie?
5. Jak używać Lighthouse jako argument w bug reporcie?
```
