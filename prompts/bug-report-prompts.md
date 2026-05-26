# Prompty do bug reportów

## Formatowanie bug reportu z notatek

```text
Na podstawie moich notatek stwórz profesjonalny raport buga do Jiry.

Format:
- Tytuł: [komponent] + [zachowanie] + [kontekst]
- Środowisko: OS / wersja apki / urządzenie / sieć
- Severity: [zaproponuj z uzasadnieniem]
- Kroki do reprodukcji (numerowane, jednoznaczne)
- Rezultat rzeczywisty
- Rezultat oczekiwany
- Kontekst / uwagi dodatkowe

Moje notatki: [WKLEJ]
```

## Poprawa istniejącego zgłoszenia

```text
Jesteś seniorem QA. Popraw mój bug report tak, aby developer mógł szybko odtworzyć błąd.

Zachowaj:
- krótki tytuł,
- środowisko,
- preconditions,
- kroki reprodukcji,
- actual result,
- expected result,
- severity,
- priority,
- dowody,
- sugestię obszaru technicznego.

Mój bug report: [WKLEJ]
```

## Analiza braków w zgłoszeniu

```text
Przeanalizuj ten bug report i wypisz, czego brakuje, zanim zgłoszę go w Jira.
Oceń:
1. czy kroki są jednoznaczne (czy można odtworzyć krok po kroku),
2. czy expected result jest jasno opisany,
3. czy są dowody (screenshot, nagranie, logi),
4. czy da się odtworzyć błąd bez dodatkowych pytań,
5. jakie logi/requesty warto dołączyć do tego konkretnego błędu.

Bug report: [WKLEJ]
```

## Zgłoszenie błędu mobilnego (szablon z polami)

```text
Stwórz profesjonalny bug report dla aplikacji mobilnej na podstawie tych danych:

Aplikacja: [NAZWA]
Wersja: [X.X.X]
Platforma: [Android X.X / iOS X.X]
Urządzenie: [MODEL]
Typ sieci: [WiFi/LTE/offline]
Kroki do reprodukcji: [LISTA]
Co się stało (actual): [OPIS]
Co powinno się stać (expected): [OPIS]
Logi: [WKLEJ lub "brak"]
Request/response: [WKLEJ lub "brak"]
Nagranie/screen: [LINK lub "brak"]
```

## Tłumaczenie buga na język biznesowy

```text
Znalazłem buga technicznego: [OPIS]

Przetłumacz na:
1. Opis dla managera (wpływ na użytkownika końcowego, bez żargonu IT)
2. Severity (Critical/High/Medium/Low) z uzasadnieniem
3. Konsekwencje biznesowe, jeśli nie naprawione w tym sprincie
4. Proponowany priorytet naprawy

Pisz tak, jakby odbiorcą był Product Manager bez tła technicznego.
```

## Analiza logcat dla bug reportu

```text
Jestem testerem manualnym. Wyjaśnij mi te logi z logcata:
1. Co poszło nie tak (po ludzku, bez developer-speak)
2. Który komponent zawinił (apka? system? sieć? backend?)
3. Czy to błąd apki czy systemu Android?
4. Co dokładnie dołączyć do raportu buga (jakie fragmenty logów)
5. Czy mogę to odtworzyć bez dostępu do kodu źródłowego

Logi: [WKLEJ]
```
