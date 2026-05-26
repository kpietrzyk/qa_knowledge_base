# Android Layout Inspector

## Kategoria

- Główna kategoria: `ui-inspection`
- Podkategoria: `layout-debugging`
- Darmowe: `True`
- Poziom trudności: `easy-medium`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `low`
- Wymaga kodowania: `False`

## Do czego służy

Android Layout Inspector pozwala kliknąć na dowolny element w działającej aplikacji Android i odczytać jego dokładne wartości: margin, padding, rozmiar czcionki, kolor — i porównać je z projektem w Figmie, podając konkretne liczby w bug raporcie.

## Najlepsze zastosowania

- Weryfikacja marginesów i paddingów względem projektu Figma (np. "margin wynosi 8px zamiast 16px")
- Sprawdzanie rozmiaru czcionki i line-height w rzeczywistej implementacji
- Znajdowanie nakładających się elementów niewidocznych gołym okiem
- Dokumentowanie błędów UI z precyzyjnymi danymi liczbowymi zamiast ogólnych opisów

## Kiedy używać

Używaj tego narzędzia wtedy, gdy widzisz, że coś "wygląda nie tak" w aplikacji Android i chcesz zamiast "przycisk wydaje się za mały" napisać w bug raporcie "przycisk ma height: 36dp zamiast wymaganych 48dp zgodnie z projektem Figma".

## Pierwszy praktyczny workflow

1. Otwórz Android Studio i podłącz urządzenie lub uruchom emulator z aplikacją testową.
2. W menu wybierz: View → Tool Windows → Layout Inspector.
3. Wybierz process swojej aplikacji z listy — Layout Inspector połączy się automatycznie.
4. Kliknij na element UI w podglądzie — w panelu po prawej zobaczysz jego właściwości.
5. Porównaj wartości (margin, padding, textSize) z danymi z Figma Dev Mode i zapisz różnicę.

## Następny krok

Naucz się używać trybu "Live Updates" w Layout Inspector, który odświeża dane w czasie rzeczywistym podczas interakcji z aplikacją — przydatne przy debugowaniu animacji i przejść między ekranami.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Layout Inspector wymaga Android Studio — nie działa jako samodzielne narzędzie.
- Wartości są w dp (density-independent pixels), nie px — przelicz zgodnie ze specyfikacją.
- Na starszych urządzeniach lub buildach produkcyjnych funkcja może być niedostępna.

## Link

https://developer.android.com/studio/debug/layout-inspector

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Android Layout Inspector praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
