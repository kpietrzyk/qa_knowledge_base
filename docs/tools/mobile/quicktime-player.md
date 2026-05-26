# QuickTime Player

## Kategoria

- Główna kategoria: `mobile-testing`
- Podkategoria: `screen-recording`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `low`
- Wymaga kodowania: `False`

## Do czego służy

Nagrywanie ekranu iPhone przez kabel USB na macOS — najprostsza metoda uchwycenia kroków reprodukcji błędu iOS bez instalowania dodatkowego oprogramowania.

## Najlepsze zastosowania

- nagrywanie kroków reprodukcji błędu na fizycznym iPhone do bug raportu
- szybkie zrzuty ekranu iOS bezpośrednio na Mac
- nagrywanie sesji eksploracyjnych na rzeczywistym urządzeniu
- dokumentacja błędów wizualnych (animacje, przejścia, flagi UI)
- demonstracja błędu dla PM bez potrzeby oprogramowania do mirroringu

## Kiedy używać

Używaj tego narzędzia wtedy, gdy pracujesz na macOS, masz iPhone pod ręką i chcesz natychmiast nagrać reprodukcję błędu — bez konfiguracji, bez dodatkowych aplikacji, podłącz i nagrywaj.

## Pierwszy praktyczny workflow

1. Podłącz iPhone kablem USB do Maca — odblokuj telefon i potwierdź zaufanie komputerowi (`Ufaj temu komputerowi`).
2. Otwórz QuickTime Player (`Cmd+Space` > wpisz `QuickTime`).
3. Kliknij `File` > `New Movie Recording`.
4. Kliknij strzałkę obok czerwonego przycisku nagrywania > z listy wybierz swój iPhone jako źródło wideo i audio.
5. Kliknij `nagraj` > zreprodukuj błąd na telefonie > zatrzymaj nagranie > zapisz plik `.mov` i dołącz do bug raportu.

## Następny krok

Połącz nagrania z QuickTime z Loom — dodaj komentarz głosowy, który opisuje błąd, i wyślij link do zespołu zamiast ciężkiego pliku wideo.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Działa tylko na macOS — dla Androida użyj scrcpy i `adb shell screenrecord` zamiast tego narzędzia.

## Link

https://support.apple.com/guide/quicktime-player/welcome/mac

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia QuickTime Player praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
