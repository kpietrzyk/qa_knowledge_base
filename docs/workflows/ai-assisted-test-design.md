# Workflow: projektowanie testów z pomocą AI

## Cel

Użyć AI do przyspieszenia przygotowania draftu przypadków testowych, zachowując kontrolę testera, traceability i zgodność z wymaganiami.

## Ważna zasada

AI generuje **draft** — tester weryfikuje, uzupełnia i akceptuje. AI nie zna kontekstu biznesowego, nie wie o specyficznych błędach z przeszłości i nie rozumie priorytetu z perspektywy PM.

## Dane wejściowe

- wymaganie lub User Story z trwałym ID,
- kryteria akceptacji i reguły biznesowe,
- definicja done, jeśli wnosi dodatkowe ograniczenia,
- platforma, zakres i ryzyka,
- zatwierdzone, zanonimizowane dane testowe.

## Kiedy używać

- Nowa User Story w sprincie
- Brak czasu na ręczne projektowanie TC
- Chcesz sprawdzić, czy czegoś nie pominąłeś
- Analiza wymagań przed testem

## Narzędzia

- [Ollama](../tools/ai/ollama.md) lub inny zatwierdzony lokalny model
- [Prompty do projektowania testów](../prompts/test-case-prompts.md)
- System zarządzania testami, np. [Kiwi TCMS](../tools/test-management/kiwi-tcms.md), [Qase](../tools/test-management/qase.md) lub Jira
- [Checklista ryzyk AI](../tools/ai/ai-risk-checklist.md)

---

## Kroki

### Krok 1 — Przygotuj input

Sprawdź, czy wejście zawiera:

- ID i aktualną wersję wymagania,
- kryteria akceptacji oraz jawne reguły biznesowe,
- platformę i wspierane wersje systemu,
- zależności, integracje i obszary poza zakresem,
- oczekiwany format oraz ID wynikowych testów.

Braki zapisz jako pytania lub założenia. Nie pozwalaj AI uzupełniać ich bez oznaczenia.

### Krok 2 — Wygeneruj TC przez AI

Użyj [promptu do projektowania testów](../prompts/test-case-prompts.md):

```text
Jesteś QA Engineerem mobilnym (Android+iOS). Na podstawie tej user story
przygotuj draft przypadków testowych. Dla każdego podaj: ID testu, ID kryterium
akceptacji, tytuł, warunek wstępny, kroki, oczekiwany rezultat, priorytet i typ.

Uwzględnij: happy path, walidacja, brak sieci, przerwania, offline,
orientacja ekranu, Dynamic Type.

Oddziel fakty od założeń. Nie wymyślaj brakujących funkcji; wypisz pytania.

ID wymagania: [ID]
User Story i kryteria akceptacji: [WKLEJ]
```

### Krok 3 — Review output AI

Po otrzymaniu listy TC:

- [ ] Czy happy path jest pokryty?
- [ ] Czy negatywne przypadki są realistyczne?
- [ ] Czy edge cases pasują do kontekstu tej apki?
- [ ] Czy AI nie wymyśliło funkcji, której nie ma w US?
- [ ] Czy brakuje TC specyficznych dla Twojego projektu?
- [ ] Czy każdy test wskazuje wymaganie lub kryterium akceptacji?
- [ ] Czy założenia i pytania są jawnie oznaczone?
- [ ] Czy żaden test nie zawiera danych produkcyjnych lub sekretów?

### Krok 4 — Uzupełnij z wiedzy własnej

Dodaj TC, które AI pominęło:

- Błędy znane z historii projektu
- Specyfika urządzeń używanych przez użytkowników
- Integracje z innymi modułami
- Szczególne wymagania biznesowe

### Krok 5 — Priorytetyzacja

Podziel TC na:

- **Must run** (smoke) — każdy build
- **Should run** (regresja) — każdy sprint
- **Nice to have** (pełna regresja) — przed releasem

### Krok 6 — Import do TMS

Zaimportuj zatwierdzone testy do używanego systemu zarządzania testami. Zachowaj ID wymagania, ID testu, status review i właściciela. Dodaj odpowiednie tagi, np. `mobile`, `android`, `ios`, `api`, `smoke`, `regression`.

---

## Wskazówki dla lepszego outputu AI

| Zamiast | Lepiej |
| --- | --- |
| "Wygeneruj testy dla logowania" | "Wygeneruj TC dla logowania emailem w apce Android, gdzie token JWT wygasa po 15 min" |
| Ogólny prompt bez kontekstu | Wklej fragment US + DoD + platformę |
| Akceptuj output bez review | Zawsze przejrzyj i uzupełnij |
| Jeden duży prompt | Kilka mniejszych (osobno happy path, osobno negatywne) |

## Wynik i kryteria zakończenia

Workflow jest zakończony, gdy każdy zaakceptowany test ma unikalne ID, źródłowe wymaganie lub kryterium akceptacji, priorytet, właściciela review i status. Założenia pozostają jawne, a niepotwierdzone testy nie trafiają do bazowej regresji.

## Prywatność i bezpieczeństwo

- Dla materiałów wewnętrznych używaj zatwierdzonego lokalnego modelu.
- Usuń dane osobowe, sekrety, tokeny, nazwy klientów i poufne szczegóły biznesowe.
- Nie traktuj odpowiedzi AI jako wymagania ani oczekiwanego rezultatu bez potwierdzenia w źródle.
- Zachowaj referencję do wersji wymagania, ale nie przechowuj niepotrzebnych kopii poufnej treści w promptach.

## Powiązane materiały

- [Prompty do projektowania testów](../prompts/test-case-prompts.md)
- [Checklista ryzyk AI](../tools/ai/ai-risk-checklist.md)
- [Od testu manualnego do automatycznego](from-manual-to-automation.md)
