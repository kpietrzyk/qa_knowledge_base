# Espresso

## Kategoria

- Główna kategoria: `mobile-automation`
- Podkategoria: `native-android-automation`
- Darmowe: `True`
- Poziom trudności: `hard`
- Wartość dla manualnego testera: `low`
- Wartość dla automatyzacji: `very high`
- Wymaga kodowania: `True`

## Do czego służy

Natywny framework do testów UI Androida wbudowany w Android SDK — najszybsze i najbardziej niezawodne testy automatyczne Androida, ale wymaga dostępu do kodu źródłowego aplikacji i znajomości Javy lub Kotlina.

## Najlepsze zastosowania

- testy regresji UI wbudowane bezpośrednio w projekt Android
- weryfikacja przepływów logowania, formularzy i nawigacji na poziomie kodu
- testy integracyjne między ekranami aplikacji
- automatyczne sprawdzanie stanów UI niemożliwych do odtworzenia przez scrcpy
- pipeline CI/CD z testami uruchamianymi przy każdym PR

## Kiedy używać

Używaj tego narzędzia wtedy, gdy jesteś testerem ściśle współpracującym z zespołem deweloperskim Android, masz dostęp do repozytorium kodu i chcesz pisać testy razem z deweloperami w tym samym projekcie.

## Pierwszy praktyczny workflow

1. Otwórz projekt Android w Android Studio > sprawdź czy folder `app/src/androidTest/` istnieje.
2. Dodaj zależność w `build.gradle`: `androidTestImplementation 'androidx.test.espresso:espresso-core:3.5.1'`.
3. Utwórz klasę testową w folderze `androidTest` z adnotacją `@RunWith(AndroidJUnit4::class)`.
4. Napisz prosty test: `onView(withId(R.id.button_login)).perform(click())` > `onView(withId(R.id.text_welcome)).check(matches(isDisplayed()))`.
5. Uruchom test prawym przyciskiem myszy na klasie > `Run` — test wykona się na podłączonym urządzeniu lub emulatorze.

## Następny krok

Naucz się najpierw Appium — daje te same możliwości testów UI Androida, ale jest niezależny od kodu aplikacji i nie wymaga Javy. Espresso to kolejny krok przy ścisłej współpracy z zespołem deweloperskim.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Wymaga dostępu do kodu źródłowego aplikacji — nie nadaje się do testów czarnoskrzynkowych (black-box testing).

## Link

https://developer.android.com/training/testing/espresso

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Espresso praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
