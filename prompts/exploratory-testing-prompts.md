# Prompty do exploratory testing

## Charter sesji eksploracyjnej (mobile)

```text
Jesteś ekspertem od exploratory testing mobilnego.

Aplikacja: [OPIS]
Platforma: [Android/iOS/oba]
Czas sesji: [X godzin]

Podaj:
1. TOP 5 obszarów ryzyka dla tej aplikacji
2. Charter eksploracyjny dla każdego obszaru (cel + zakres + czas)
3. Heurystyki pasujące do kontekstu (np. SFDIPOT, CRUD, HICCUP)
4. Co sprawdzić pierwsze (highest risk first)
5. Edge cases mobilne: gesty, przerwania, low memory, background/foreground switch, zmiany uprawnień w trakcie działania
```

## Session Based Testing — karta sesji

```text
Przygotuj kartę sesji eksploracyjnej dla funkcji: [FUNKCJA]

Uwzględnij:
- cel sesji (co chcemy odkryć),
- zakres (co testujemy, czego NIE testujemy),
- ryzyka i obszary ryzyka,
- dane testowe potrzebne do sesji,
- heurystyki do zastosowania,
- notatki do zebrania podczas sesji,
- potencjalne typy bugów do wyłapania,
- pytania do Product Ownera po sesji.
```

## Heurystyki dla aplikacji mobilnej

```text
Zaproponuj heurystyki testowe dla aplikacji mobilnej: [OPIS APLIKACJI]

Uwzględnij w swoich propozycjach:
- CRUD (Create, Read, Update, Delete — wszystkie operacje na danych)
- Permissions (uprawnienia: kamera, lokalizacja, powiadomienia, kontakty)
- Interruptions (połączenia, alarmy, rozładowanie baterii, utrata sieci)
- Network conditions (offline, slow 3G, przełączenie WiFi↔LTE w trakcie)
- Data consistency (synchronizacja, konflikty, limity pól)
- Device constraints (mała pamięć, stara wersja OS, mały ekran)
- Security basics (dane w pamięci, logi, uprawnienia, sesja)
- Accessibility (TalkBack, Dynamic Type, kontrast kolorów)
```

## Analiza ryzyk przed testem

```text
Przed testem tej funkcji pomóż mi ocenić ryzyka:

Funkcja: [OPIS]
Aplikacja: [OPIS]
Ostatnie zmiany w kodzie (jeśli znasz): [OPIS lub "brak info"]

Podaj:
1. Obszary najwyższego ryzyka (gdzie najczęściej pojawiają się bugi tego typu)
2. Zależności (co jeszcze może się zepsuć przez tę zmianę — regression risk)
3. Konfiguracje krytyczne do sprawdzenia (OS wersje, urządzenia, sieci)
4. Pytania do developera przed testem
5. Minimalny zestaw testów smoke dla tej funkcji
```

## Co jeszcze sprawdzić? (AI jako sparring partner)

```text
Testuję funkcję: [OPIS]
Przetestowałem już: [LISTA WYKONANYCH TESTÓW]
Znalazłem bugi: [LISTA lub "brak"]

Jako doświadczony QA:
1. Co jeszcze powinienem sprawdzić, czego mogłem nie zauważyć?
2. Jakie edge cases są typowe dla tego rodzaju funkcji?
3. Czy jest coś specyficznego dla mobile, o czym mógłbym zapomnieć?
4. Zaproponuj 3 testy, które mają największą szansę znaleźć nowe bugi.
```
