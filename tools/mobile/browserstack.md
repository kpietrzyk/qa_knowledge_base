# BrowserStack

## Kategoria

- Główna kategoria: `mobile-testing`
- Podkategoria: `device-cloud`
- Darmowe: `False`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `very high`
- Wymaga kodowania: `False`

## Do czego służy

Testowanie aplikacji na prawdziwych fizycznych urządzeniach w chmurze — iPhone 15, Samsung Galaxy S24 i setkach innych modeli — bez potrzeby kupowania sprzętu.

## Najlepsze zastosowania

- testy manualne na prawdziwych urządzeniach (App Live) bez posiadania fizycznego telefonu
- uruchamianie testów Appium na realnych urządzeniach w CI/CD (App Automate)
- testowanie na konkretnych kombinacjach model + wersja OS nieosiągalnych inaczej
- nagrywanie sesji i zrzuty ekranu bezpośrednio z panelu
- testowanie geolokalizacji i lokalizacji językowej na urządzeniach z różnych regionów

## Kiedy używać

Używaj tego narzędzia wtedy, gdy potrzebujesz potwierdzić błąd na konkretnym modelu fizycznego urządzenia, którego nie masz w biurze, albo gdy klient zgłasza problem tylko na jednym telefonie i chcesz to szybko zreprodukować.

## Pierwszy praktyczny workflow

1. Załóż konto na browserstack.com i aktywuj trial (lub poproś o licencję firmową).
2. Wejdź w `App Live` > prześlij plik `.apk` lub `.ipa` przyciskiem `Upload`.
3. Wybierz urządzenie z listy (np. Samsung Galaxy S24, Android 14) > kliknij `Start`.
4. Przetestuj manualnie w oknie przeglądarki — możesz zmieniać lokalizację, obracać ekran, symulować połączenia.
5. Zrób zrzut ekranu lub nagraj sesję wideo > pobierz jako dowód do bug raportu.

## Następny krok

Skonfiguruj App Automate, żeby uruchamiać testy Appium na realnych urządzeniach — zamiast na emulatorze. Wystarczy zmienić `platformName` i dodać klucz BrowserStack do capabilities.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — koszt jest wysoki dla indywidualnych testerów, sprawdź czy firma ma licencję.
- Alternatywy warte porównania: Sauce Labs, LambdaTest — mogą być tańsze przy określonym użyciu.

## Link

https://www.browserstack.com/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia BrowserStack praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
