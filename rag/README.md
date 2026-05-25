# RAG / AI-agent usage

Ten folder opisuje, jak używać repo jako bazy wiedzy dla lokalnego asystenta QA.

## Dlaczego Markdown + JSON?

- Markdown jest wygodny dla człowieka.
- JSON jest wygodny dla agenta.
- CSV jest wygodny do filtrowania i importu.

## Zalecenie do chunkowania

Chunkuj po nagłówkach drugiego poziomu `##`.
Nie wrzucaj całego repo jako jeden dokument.

## Minimalny prompt systemowy dla lokalnego asystenta QA

```text
Jesteś asystentem QA Mobile.
Odpowiadasz praktycznie i technicznie.
Gdy użytkownik pyta o narzędzie, podaj:
- kiedy użyć,
- pierwszy workflow,
- ograniczenia,
- następny krok automatyzacji.
Nie zmyślaj licencji ani cen. Jeśli nie wiesz, powiedz, że trzeba sprawdzić aktualne warunki.
```

## Tagowanie

Używaj pól z `datasets/tools-list.json`:
- category
- difficulty
- free
- requires_code
- manual_tester_value
- automation_value
