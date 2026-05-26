# Accessibility Scanner

## Kategoria

- Główna kategoria: `ui-inspection`
- Podkategoria: `accessibility`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `low`
- Wymaga kodowania: `False`

## Do czego służy

Accessibility Scanner to aplikacja Google instalowana na urządzeniu Android, która analizuje aktualnie wyświetlany ekran i wskazuje konkretne problemy dostępności: zbyt niski kontrast, zbyt małe touch targety i brakujące opisy elementów.

## Najlepsze zastosowania

- Szybki audit dostępności każdego ekranu aplikacji Android bez wiedzy technicznej
- Znajdowanie elementów z niewystarczającym kontrastem kolorów (poniżej WCAG 4.5:1)
- Identyfikacja przycisków i pól mniejszych niż wymagane 48x48dp touch target
- Dokumentowanie problemów a11y z konkretnymi sugestiami poprawek dla developera

## Kiedy używać

Używaj tego narzędzia wtedy, gdy testujesz nowy ekran lub nową funkcjonalność w aplikacji Android i chcesz w 2 minuty sprawdzić, czy nie ma podstawowych problemów dostępności — zamiast ręcznie mierzyć kontrast i rozmiary elementów, Scanner robi to automatycznie i pokazuje wyniki na ekranie.

## Pierwszy praktyczny workflow

1. Zainstaluj aplikację "Accessibility Scanner" ze sklepu Google Play na urządzeniu testowym.
2. Włącz Scanner w ustawieniach dostępności urządzenia (Ustawienia → Dostępność → Accessibility Scanner).
3. Otwórz testowaną aplikację i przejdź do ekranu, który chcesz sprawdzić.
4. Naciśnij pływający przycisk Scanner — narzędzie przeanalizuje aktualny widok.
5. Przejrzyj wykryte problemy, rób screenshoty i dodaj do Jiry z opisem każdego naruszenia.

## Następny krok

Połącz wyniki Accessibility Scanner z ręcznym testem TalkBack — scanner wykrywa problemy techniczne, ale tylko ręczny test z TalkBack pokaże, czy przepływ nawigacji jest zrozumiały dla użytkownika z niepełnosprawnością wzroku.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Scanner wykrywa tylko automatycznie sprawdzalne problemy — nie zastępuje manualnego testu z TalkBack.
- Działa wyłącznie na Android — do iOS użyj Xcode Accessibility Inspector.
- Niektóre fałszywe alarmy mogą się pojawić — weryfikuj wyniki kontekstualnie.

## Link

https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Accessibility Scanner praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
