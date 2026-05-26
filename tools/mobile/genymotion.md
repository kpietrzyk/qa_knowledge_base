# Genymotion

## Kategoria

- Główna kategoria: `mobile-testing`
- Podkategoria: `android-emulator`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium-high`
- Wymaga kodowania: `False`

## Do czego służy

Szybki emulator Androida z gotowymi profilami urządzeń, symulacją GPS i ograniczaniem przepustowości sieci — wyraźnie szybszy od domyślnego emulatora Android Studio.

## Najlepsze zastosowania

- testowanie na konkretnych modelach urządzeń (Samsung Galaxy S24, Pixel 8) bez fizycznego sprzętu
- symulacja lokalizacji GPS dla aplikacji map i dostawczych
- symulacja warunków sieciowych (3G, offline, wysokie opóźnienie)
- testowanie na wielu wersjach Androida jednocześnie
- integracja z ADB i scrcpy do pełnego workflow testowego

## Kiedy używać

Używaj tego narzędzia wtedy, gdy Android Studio Emulator działa za wolno albo chcesz szybko przełączać się między wieloma profilami urządzeń bez konfigurowania każdego ręcznie.

## Pierwszy praktyczny workflow

1. Pobierz i zainstaluj Genymotion Desktop z genymotion.com (wybierz plan Personal — darmowy).
2. Zaloguj się kontem Genymotion i zainstaluj VirtualBox (wymagany przez Genymotion).
3. W panelu kliknij `+` > wybierz urządzenie z katalogu (np. Google Pixel 8, Android 14) > `Install`.
4. Uruchom wirtualne urządzenie > skorzystaj z widgetu GPS (ikona satelity po prawej) i wpisz współrzędne testowe.
5. Otwórz widget Network (ikona sieci) > wybierz profil `3G` lub `No network` > sprawdź zachowanie aplikacji.

## Następny krok

Połącz Genymotion z ADB (`adb devices` wykryje emulator automatycznie) i scrcpy do nagrywania ekranu — otrzymasz kompletny zestaw do testów mobilnych bez fizycznego urządzenia.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — plan Personal jest tylko do niekomercyjnego użytku.
- Genymotion nie emuluje sprzętu tak wiernie jak fizyczne urządzenie — błędy związane z konkretnym GPU lub czujnikami wymagają prawdziwego telefonu.

## Link

https://www.genymotion.com/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Genymotion praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
