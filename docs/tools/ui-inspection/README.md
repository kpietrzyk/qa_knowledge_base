# Inspekcja UI & Dostępność

Narzędzia do weryfikacji implementacji UI względem projektu Figma oraz testowania dostępności.

## Dlaczego to ważne

"Wygląda dobrze" to za mało. Tester powinien podać liczbę: margin jest 8px zamiast 16px.

## Narzędzia w tej kategorii

- **Android Layout Inspector** — sprawdź margin/padding/font w uruchomionej aplikacji Android
- **Xcode Accessibility Inspector** — VoiceOver labels, kolejność fokusa, a11y WCAG (iOS)
- **Figma Dev Mode** — source of truth: kolory, wymiary, spacing z projektu
- **Accessibility Scanner** — szybki audit Android: kontrast, target size, opisy elementów
- **uiautomatorviewer** — znajdowanie resource-id / xpath do selektorów automatyzacji

## Relacja z Figmą

Figma Dev Mode (Inspect) → dane projektowe → Layout Inspector → dane implementacji → różnica = bug UI.
