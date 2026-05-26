# MaestroGPT

## Kategoria

- Główna kategoria: `ai-for-testing`
- Podkategoria: `ai-yaml-generator`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `very high`
- Wartość dla automatyzacji: `high`
- Wymaga kodowania: `False`

## Do czego służy

Opisujesz kroki testowe w naturalnym języku, MaestroGPT generuje gotowy plik YAML dla Maestro — najlepszy punkt wejścia do mobilnej automatyzacji bez pisania kodu.

## Najlepsze zastosowania

- generowanie pierwszych przepływów Maestro z opisu po polsku lub angielsku
- szybkie prototypowanie testów automatycznych bez znajomości składni YAML
- nauka struktury Maestro na przykładach generowanych przez AI
- automatyzacja prostych powtarzalnych scenariuszy (logowanie, rejestracja, checkout)
- obniżenie bariery wejścia do automatyzacji dla testerów manualnych

## Kiedy używać

Używaj tego narzędzia wtedy, gdy masz gotowy scenariusz testowy w głowie lub w Jirze i chcesz szybko zobaczyć czy Maestro da radę go zautomatyzować — zamiast uczyć się składni YAML od zera, opisz co chcesz, a AI wygeneruje szkielet.

## Pierwszy praktyczny workflow

1. Zainstaluj Maestro lokalnie: `curl -Ls "https://get.maestro.mobile.dev" | bash` (macOS/Linux) lub postępuj według instrukcji dla Windows.
2. Zaloguj się do Maestro Studio na maestro.mobile.dev lub użyj komendy `maestro studio` w terminalu.
3. W polu tekstowym wpisz opis testu po angielsku: np. `Open app, tap Login button, enter email test@test.com, enter password 123456, tap Submit, verify Home screen is visible`.
4. MaestroGPT generuje plik YAML — przejrzyj go i sprawdź czy selektory (text, id) zgadzają się z Twoją aplikacją.
5. Zapisz plik jako `login_test.yaml` > uruchom: `maestro test login_test.yaml` — obserwuj wynik na podłączonym urządzeniu lub emulatorze.

## Następny krok

Naucz się podstawowej edycji YAML Maestro — dodawanie asercji (`assertVisible`), obsługi warunków (`runFlow`) i zmiennych środowiskowych. To pozwoli poprawiać i rozszerzać wygenerowane przez AI przepływy.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję przed użyciem komercyjnym — Maestro Studio (chmura z MaestroGPT) może mieć płatne plany; lokalne Maestro jest darmowe i open source.
- AI nie zna Twojej konkretnej aplikacji — wygenerowane selektory (np. nazwy przycisków) wymagają weryfikacji i często ręcznej poprawki.

## Link

https://maestro.mobile.dev/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie narzędzia MaestroGPT praktycznie.
Kontekst: jestem manualnym testerem aplikacji mobilnych.
Chcę wiedzieć:
1. kiedy używać,
2. jak zainstalować,
3. pierwsze 5 komend / akcji,
4. typowe błędy początkujących,
5. jak użyć tego narzędzia w realnym bug reporcie,
6. jaki jest następny krok automatyzacji.
```
