# AI Risk Checklist dla QA

## Kategoria

- Główna kategoria: `ai-for-testing`
- Podkategoria: `ai-safety`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `high`
- Wymaga kodowania: `False`

## Do czego służy

Checklista ryzyk przy używaniu AI w pracy testera QA — zapobiega bezmyślnemu kopiowaniu outputu AI, chroni dane firmowe i zapewnia weryfikację generowanych artefaktów.

## Dlaczego potrzebujesz tej checklisty

AI jest narzędziem — jak każde narzędzie może być używane dobrze lub źle. Tester, który bezmyślnie kopiuje output AI, jest gorszy niż tester nieużywający AI wcale.

Każdy wygenerowany test case, każdy skrypt automatyzacji i każda analiza buga wychodzące z AI są Twoją odpowiedzialnością — nie odpowiedzialnością modelu.

---

## Przed użyciem AI — sprawdź

### Bezpieczeństwo danych
- [ ] Czy prompt zawiera dane poufne (tokeny, hasła, dane użytkowników, kod firmowy)?
- [ ] Czy używam publicznego modelu (ChatGPT, Claude) z danymi firmowymi? → użyj Ollamy/LM Studio
- [ ] Czy logcaty/requesty które wklejam zawierają tokeny produkcyjne?
- [ ] Czy polityka firmy pozwala na wysyłanie tego typu danych do zewnętrznych API?

### Jakość promptu
- [ ] Czy mój prompt zawiera wystarczający kontekst (platforma, typ apki, wymagania)?
- [ ] Czy podałem konkretny format oczekiwanego outputu?
- [ ] Czy testowałem prompt na kilku przypadkach zanim użyłem go w pracy?
- [ ] Czy prompt jest wystarczająco specyficzny dla tego projektu, nie ogólny?

---

## Po otrzymaniu outputu AI — sprawdź

### Weryfikacja merytoryczna
- [ ] Czy AI nie wymyśliło funkcji, których nie ma w specyfikacji?
- [ ] Czy wygenerowane TC pokrywają rzeczywiste ryzyko tej funkcji?
- [ ] Czy edge cases są realistyczne dla tej platformy/aplikacji?
- [ ] Czy AI nie pominęło żadnego oczywistego przypadku?
- [ ] Czy podane kroki reprodukcji są możliwe do wykonania w tej wersji aplikacji?

### Weryfikacja techniczna (dla kodu/skryptów)
- [ ] Czy wygenerowany kod jest uruchomiony i działa?
- [ ] Czy selektory istnieją w aplikacji (sprawdzone przez Appium Inspector / DevTools)?
- [ ] Czy asercje sprawdzają to, co powinny?
- [ ] Czy kod nie ma oczywistych błędów (błędna nazwa metody, zły typ danych)?
- [ ] Czy importy i zależności są poprawne dla aktualnej wersji narzędzia?

### Weryfikacja kontekstu biznesowego
- [ ] Czy AI zrozumiało intencję user story, nie tylko jej literę?
- [ ] Czy priorytety TC są zgodne z priorytetami biznesowymi projektu?
- [ ] Czy tester (Ty) jest w stanie wyjaśnić każdy wygenerowany TC własnymi słowami?
- [ ] Czy zakres testów jest zgodny z Definition of Done tego sprintu?

---

## Typowe pułapki AI w QA

| Pułapka | Objaw | Jak uniknąć |
|---|---|---|
| Halucynacje | AI opisuje funkcję, endpoint lub metodę, której nie ma | Zawsze weryfikuj vs specyfikacja i Swagger |
| Over-generation | 50 TC zamiast 10 naprawdę potrzebnych | Pytaj o priorytetyzację i smoke suite osobno |
| Generic tests | TC pasujące do każdej aplikacji, bez specyfiki projektu | Dodaj kontekst projektu, user stories i tech stack do promptu |
| Code that looks right | Skrypt działa wizualnie poprawnie ale failuje przy uruchomieniu | Uruchom każdy wygenerowany test lokalnie przed dodaniem do repo |
| Missing edge cases | AI skupia się na happy path i ignoruje warunki brzegowe | Explicite proś: „Dodaj edge cases dla mobile: offline, niska pamięć, przerwana sesja" |
| Stale knowledge | AI nie zna najnowszych wersji narzędzia lub API | Weryfikuj komendy i metody z oficjalną dokumentacją |
| Confidence bez podstaw | AI odpowiada pewnie na pytanie, na które nie ma odpowiedzi | Pytaj: „Czy jesteś pewny? Podaj źródło." |
| Nadmierne zaufanie do nazw selektorów | AI wymyśla resource-id które nie istnieją | Każdy selektor weryfikuj przez Appium Inspector lub DevTools |

---

## Złota zasada

> AI przyspiesza pracę testera — ale nie zastępuje myślenia testera.
> Tester odpowiada za jakość swojej pracy, niezależnie od tego, jakie narzędzia używa.

---

## Kiedy NIE używać AI do generowania TC

- Gdy nie rozumiesz wymagań samemu — AI wzmocni niejasność, nie rozwiąże jej
- Gdy nie możesz zweryfikować outputu (brak dostępu do apki, środowiska, spec)
- Gdy tempo pracy wymusza pominięcie weryfikacji — lepiej mniej TC, ale własnych i pewnych
- Gdy dane w promptach objęte są umową NDA i nie masz lokalnego modelu

---

## Wzorzec pracy z AI (dobry cykl)

```
1. Ty analizujesz wymagania i ryzyko
2. Ty piszesz prompt z kontekstem projektu
3. AI generuje draft TC / kod
4. Ty weryfikujesz każdy element
5. Ty modyfikujesz, uzupełniasz, priorytetyzujesz
6. Output jest Twój — nie AI
```

## Kiedy używać

Używaj tej checklisty zawsze, gdy korzystasz z AI w procesie testowania — zarówno do generowania TC, analizy logów, jak i pisania skryptów automatyzacji. Szczególnie ważna przy pracy z danymi firmowymi i kodem produkcyjnym.

## Link

https://github.com/kpietrzyk/qa_knowladge_base/blob/main/tools/ai/ai-risk-checklist.md

## Prompt AI do samej siebie

```text
Sprawdź mój output AI pod kątem ryzyk z tej checklisty:
1. Czy wygenerowane TC są realistyczne dla tej aplikacji?
2. Czy AI nie wymyśliło funkcji której nie ma w specyfikacji?
3. Czy edge cases są specyficzne dla mobile, czy generyczne?
4. Co powinienem dodać lub zmienić?

Output AI: [WKLEJ]
Specyfikacja / User Story: [WKLEJ]
```
