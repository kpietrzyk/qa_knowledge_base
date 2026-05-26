# Xcode Accessibility Inspector

## Kategoria

- Główna kategoria: `ui-inspection`
- Podkategoria: `accessibility`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `low`
- Wymaga kodowania: `False`

## Do czego służy

Xcode Accessibility Inspector pozwala kliknąć na element w aplikacji iOS i sprawdzić jego etykietę VoiceOver, kolejność fokusa, rolę oraz spełnienie wymagań WCAG — bez uruchamiania VoiceOver na urządzeniu.

## Najlepsze zastosowania

- Weryfikacja etykiet VoiceOver (accessibilityLabel) na elementach interaktywnych
- Sprawdzanie kolejności fokusa przy nawigacji klawiaturą i VoiceOver
- Audit zgodności z WCAG 2.1 na poziomie pojedynczych elementów UI
- Znajdowanie elementów bez etykiety dostępności przed przekazaniem do użytkowników z niepełnosprawnościami

## Kiedy używać

Używaj tego narzędzia wtedy, gdy testujesz dostępność aplikacji iOS i chcesz sprawdzić, czy każdy przycisk, pole i element interaktywny ma poprawną etykietę VoiceOver oraz czy kolejność fokusa jest logiczna — bez potrzeby włączania VoiceOver na urządzeniu i ręcznego przechodzenia przez cały ekran.

## Pierwszy praktyczny workflow

1. Otwórz Xcode na macOS i uruchom aplikację na symulatorze lub podłączonym urządzeniu iOS.
2. Z menu Xcode wybierz: Xcode → Open Developer Tool → Accessibility Inspector.
3. W Accessibility Inspector wybierz urządzenie/symulator z listy rozwijanej.
4. Kliknij element w symulatorze lub użyj kursora w Accessibility Inspector — zobaczysz jego właściwości a11y.
5. Sprawdź: Label (etykieta), Value (wartość), Traits (rola), oraz czy Hint jest sensowny — udokumentuj braki w Jirze.

## Następny krok

Uruchom automatyczny audit: w Accessibility Inspector kliknij ikonę "Run Audit" — narzędzie wskaże elementy bez etykiet, zbyt małe touch targety i inne podstawowe problemy dostępności na całym ekranie.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Narzędzie jest dostępne wyłącznie na macOS z zainstalowanym Xcode — brak wersji Windows/Linux.
- Accessibility Inspector nie symuluje pełnego doświadczenia VoiceOver — zawsze testuj manualnie z VoiceOver włączonym na rzeczywistym urządzeniu.

## Link

https://developer.apple.com/documentation/accessibility/accessibility-inspector

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Xcode Accessibility Inspector praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
