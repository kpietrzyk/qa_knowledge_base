# Figma Dev Mode

## Kategoria

- Główna kategoria: `ui-inspection`
- Podkategoria: `design-reference`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `low`
- Wymaga kodowania: `False`

## Do czego służy

Figma Dev Mode (zakładka Inspect) to source of truth projektu — pozwala kliknąć na dowolny element w projekcie i odczytać jego dokładne wymiary, kolory, typografię i spacing, by porównać z implementacją w aplikacji mobilnej.

## Najlepsze zastosowania

- Odczytywanie dokładnych wartości marginesów, paddingów i rozmiarów z projektu designerskiego
- Weryfikacja kolorów (HEX/RGB) i typografii (font, size, weight, line-height) z projektu
- Sprawdzanie stanów elementów (default, pressed, disabled, error) zgodnie z projektem
- Tworzenie precyzyjnych bug reportów UI z liczbami zamiast opisów subiektywnych

## Kiedy używać

Używaj tego narzędzia wtedy, gdy chcesz sprawdzić, czy implementacja odpowiada projektowi — otwierasz Figmę, klikasz element, odczytujesz jego wartości i porównujesz z tym, co widzi Layout Inspector lub Xcode na urządzeniu. Różnica = bug UI z konkretnymi danymi.

## Pierwszy praktyczny workflow

1. Poproś designera lub PM o dostęp do projektu Figma (uprawnienie "can view" wystarczy).
2. Otwórz projekt Figma w przeglądarce lub aplikacji desktopowej.
3. Kliknij zakładkę "Dev Mode" lub "Inspect" po prawej stronie ekranu projektowego.
4. Kliknij element w projekcie — zobaczysz jego wymiary, kolory, font i spacing.
5. Porównaj odczytane wartości z aplikacją używając Layout Inspector (Android) lub Accessibility Inspector (iOS).

## Następny krok

Naucz się używać funkcji "Compare" w Figma Dev Mode — pozwala nałożyć projekt na screenshot aplikacji i wizualnie zobaczyć rozbieżności bez ręcznego porównywania liczb.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym.
- Figma Dev Mode w pełnym zakresie wymaga płatnego planu — w darmowym dostęp do Inspect jest ograniczony.
- Projekt w Figmie musi być aktualny — stary plik = porównujesz z przestarzałym projektem.
- Nie używaj Figmy jako jedynego źródła — weryfikuj z developerem, czy projekt był zaakceptowany.

## Link

https://www.figma.com/dev-mode

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia Figma Dev Mode praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
