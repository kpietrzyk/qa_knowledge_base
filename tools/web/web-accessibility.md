# Web Accessibility Testing

## Kategoria

- Główna kategoria: `web-testing`
- Podkategoria: `accessibility`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Testowanie dostępności (a11y) sprawdza czy aplikacja webowa jest użyteczna dla osób z niepełnosprawnościami: wzrokowymi, motorycznymi, słuchowymi, poznawczymi. Standard WCAG 2.1 definiuje wymagania — wiele krajów i dużych korporacji wymaga zgodności.

Ten plik to przegląd podejścia i zestawu narzędzi — nie jedno narzędzie.

## Dlaczego tester powinien to umieć

- Coraz więcej firm wymaga testów dostępności w DoD
- Automatyczne narzędzia wykrywają tylko ~30% problemów WCAG — reszta wymaga testowania manualnego
- Bug dostępności może być severity Critical dla użytkownika z czytnikiem ekranu

---

## Narzędzie 1: axe DevTools (rozszerzenie Chrome/Firefox)

**Link:** https://www.deque.com/axe/

**Darmowe:** Tak (wersja podstawowa rozszerzenia)

**Poziom trudności:** Easy

Rozszerzenie przeglądarki od Deque. Po zainstalowaniu pojawia się w DevTools jako nowa zakładka. Skanuje stronę i pokazuje naruszeń WCAG z dokładnym opisem i linkiem do naprawy. Wykrywa więcej niż Lighthouse.

### Jak używać
1. Zainstaluj rozszerzenie: Chrome Web Store → „axe DevTools"
2. Otwórz DevTools (F12) → zakładka **axe DevTools**
3. Kliknij **Scan ALL of my page**
4. Przeglądaj wyniki: Critical → Serious → Moderate → Minor
5. Każde naruszenie ma: opis, element w HTML, jak naprawić

### Co wykrywa axe (wybór)
- missing `alt` na obrazkach
- insufficient color contrast
- form elements without labels
- ARIA misuse
- keyboard traps
- missing `lang` attribute na `<html>`

---

## Narzędzie 2: WAVE (Web Accessibility Evaluation Tool)

**Link:** https://wave.webaim.org/

**Darmowe:** Tak

**Poziom trudności:** Easy

WAVE WebAIM to narzędzie online + rozszerzenie Chrome. Nakłada ikonki bezpośrednio na stronę — czerwone błędy, żółte ostrzeżenia, zielone elementy struktury. Wizualny przegląd — dobry dla osób uczących się dostępności.

### Jak używać
- **Online:** Wejdź na wave.webaim.org → wpisz URL strony
- **Rozszerzenie:** Zainstaluj, otwórz stronę → kliknij ikonę WAVE → nakłada ikonki na stronę

---

## Narzędzie 3: Nawigacja klawiaturą (testowanie manualne)

**Darmowe:** Tak — zero narzędzi, tylko klawiatura

**Poziom trudności:** Easy

Najważniejszy test manualny dostępności. Użytkownicy z niepełnosprawnościami motorycznymi i czytniki ekranu używają tylko klawiatury.

### Workflow testu klawiaturą
```
1. Odłóż myszkę
2. Naciśnij Tab — każdy focusowalny element powinien otrzymać widoczny focus (outline)
3. Sprawdź kolejność — czy Tab przeskakuje po ekranie logicznie?
4. Enter / Spacja — czy aktywują przyciski, linki, checkboxy?
5. Escape — czy zamyka modale, dropdowny?
6. Strzałki — czy poruszają się po menu, listach, zakładkach?
```

### Typowe błędy klawiaturowe do znalezienia
- Focus trap: wchodzisz do modala i nie możesz wyjść Tabem
- Invisible focus: element jest sfocused ale brak wizualnego outline
- Skip link: brak linku „Przejdź do treści" na początku strony
- Tab order: logicznie 1 → 3 → 2 bo CSS zmienił układ wizualny
- Nie można zamknąć dropdownu przez Escape

---

## Narzędzie 4: NVDA (czytnik ekranu, Windows)

**Link:** https://www.nvaccess.org/

**Darmowe:** Tak (donacja opcjonalna)

**Poziom trudności:** Medium

NVDA (NonVisual Desktop Access) to popularny darmowy czytnik ekranu na Windows. Czytniki ekranu używają API dostępności przeglądarki — testowanie z NVDA wykrywa problemy, których żadne automatyczne narzędzie nie znajdzie.

### Skróty klawiaturowe NVDA w przeglądarce
| Skrót | Akcja |
|---|---|
| NVDA + Spacja | Włącz/wyłącz tryb browse/focus |
| Tab | Przejdź do następnego elementu interaktywnego |
| H | Następny nagłówek |
| B | Następny przycisk |
| F | Następne pole formularza |
| Strzałki | Czytaj linię po linii |

### Na co zwracać uwagę
- Czy NVDA czyta tytuł strony po załadowaniu?
- Czy przyciski są opisane (nie „button" ale „Zaloguj się — przycisk")?
- Czy komunikaty błędów są ogłaszane po wysłaniu formularza?
- Czy obrazki mają sensowne `alt` teksty?

**Na macOS/iOS:** VoiceOver — wbudowany, włącz przez Cmd+F5.

---

## Narzędzie 5: Contrast checkers

**Linki:**
- https://webaim.org/resources/contrastchecker/ (online)
- https://colour.adobe.com/create/color-contrast-analyzer (Adobe)
- axe DevTools (wykrywa automatycznie)

**Darmowe:** Tak

**Wymagania WCAG:**
- Tekst normalny (< 18px): ratio ≥ **4.5:1**
- Tekst duży (≥ 18px lub 14px bold): ratio ≥ **3:1**
- Elementy UI, ikony: ratio ≥ **3:1**

### Jak sprawdzić kontrast
1. Znajdź kolor tekstu i tła (przez DevTools → Computed → color)
2. Wklej wartości HEX do webaim.org/resources/contrastchecker
3. Narzędzie powie czy spełnia AA (minimum) i AAA (optymalny)

---

## Minimalny workflow testów dostępności

```
1. Uruchom axe DevTools → usuń Critical i Serious
2. Sprawdź Lighthouse Accessibility Score → powinno być ≥ 90
3. Przetestuj klawiaturą: Tab przez cały ekran, Enter na przyciskach, Escape z modali
4. Sprawdź kontrast na primary text i CTA buttons
5. Sprawdź alt teksty: obrazki treściowe mają opis, dekoracyjne mają alt=""
```

## Następny krok

Po podstawowym audycie axe + klawiatura: przetestuj z NVDA lub VoiceOver na krytycznych ścieżkach (logowanie, checkout, formularze). Dodaj wyniki do `checklists/accessibility-basic-checklist.md`.

## Ryzyka i ograniczenia

- Automatyczne narzędzia wykrywają ok. 30-40% problemów WCAG — manualne testowanie jest niezbędne.
- Wyniki axe i WAVE mogą się różnić — używaj obu dla pełniejszego obrazu.
- NVDA + Chrome = najlepsza kombinacja dla testów. NVDA + Edge też działa dobrze.
- Dostępność to proces, nie jednorazowy audit — testuj po każdej zmianie UI.
- Sprawdź licencję przed użyciem komercyjnym.

## Link

https://www.deque.com/axe/

## Prompt AI do nauki tematu

```text
Jesteś seniorem QA Web specjalizującym się w dostępności. Naucz mnie testować dostępność praktycznie.
Chcę wiedzieć:
1. Jak zainstalować i używać axe DevTools do znalezienia pierwszych błędów?
2. Jak przetestować nawigację klawiaturą krok po kroku?
3. Jakie są najczęstsze problemy WCAG w aplikacjach webowych?
4. Jak sprawdzić kontrast kolorów?
5. Jak napisać bug report dla błędu dostępności?
```
