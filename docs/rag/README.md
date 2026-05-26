# RAG — Retrieval Augmented Generation

Ten katalog zawiera dane w formatach przyjaznych maszynom do użycia jako źródło wiedzy pod lokalnego asystenta AI (RAG pipeline) lub knowledge base.

## Co to jest RAG?

RAG (Retrieval Augmented Generation) to technika, w której model AI przed odpowiedzią przeszukuje bazę wiedzy i dołącza znalezione fragmenty do kontekstu. Zamiast pytać ChatGPT o ogólną wiedzę, pytasz go o wiedzę z TEGO repozytorium.

Efekt: odpowiedzi oparte na konkretnych narzędziach, procesach i standardach Twojego zespołu — nie generyczna wiedza z internetu.

## Jak używać tego repo jako RAG

### Opcja 1: Bezpośredni kontekst (najprostsza)

Skopiuj treść kilku plików .md do promptu jako kontekst:

```
Kontekst: [WKLEJ ZAWARTOŚĆ tools/mobile/adb.md]
Pytanie: Jak zebrać logi do bug reportu?
```

Działa z każdym modelem AI. Ograniczenie: token limit modelu (~20–100k tokenów).

### Opcja 2: Continue.dev z lokalnym modelem

1. Zainstaluj Continue.dev w VS Code
2. Skonfiguruj z Ollamą (`tools/ai/continuedev.md`, `tools/ai/ollama.md`)
3. Dodaj ten repo jako `@codebase` lub `@file`
4. Pytaj bezpośrednio: `@codebase jak użyć ADB do zebrania logów?`

Zaleta: dane zostają lokalnie. Patrz `tools/ai/continuedev.md`.

### Opcja 3: Własny RAG pipeline

Użyj pliku `qa-tools-index.json` jako źródła danych do indeksowania przez embeddings.

Kroki:
1. Wczytaj `qa-tools-index.json`
2. Wygeneruj embeddings (OpenAI, HuggingFace, Ollama embeddings)
3. Zapisz w bazie wektorowej (ChromaDB, FAISS, Qdrant)
4. Przy zapytaniu: znajdź top-k dokumentów → dodaj do promptu

## Pliki maszynowe

| Plik | Format | Zawartość |
|---|---|---|
| `qa-tools-index.json` | JSON Array | Lista narzędzi z metadanymi — gotowe do indeksowania |
| `qa-tool-schema.json` | JSON Schema | Schemat walidacji pojedynczego narzędzia |
| `../datasets/tools-list.json` | JSON | Pełny zestaw danych narzędzi |
| `../datasets/tools-list.csv` | CSV | Źródło prawdy — edytuj tutaj |

## Zalecenia do chunkowania

Chunkuj po nagłówkach drugiego poziomu `##` — każdy plik narzędzia ma spójne sekcje.

Nie wrzucaj całego repo jako jeden dokument — chunki ~500-1000 tokenów dają lepsze wyniki wyszukiwania.

Metadane do filtrowania:
- `category` — filtruj do kategorii (mobile/api/web)
- `difficulty` — dopasuj do poziomu użytkownika
- `free` — filtruj darmowe narzędzia
- `manual_tester_value` — priorytetyzuj dla testera manualnego

## Minimalny prompt systemowy dla lokalnego asystenta QA

```text
Jesteś asystentem QA Mobile.
Odpowiadasz praktycznie i technicznie.
Gdy użytkownik pyta o narzędzie, podaj:
- kiedy użyć,
- pierwszy workflow,
- ograniczenia,
- następny krok.
Nie zmyślaj licencji ani cen. Jeśli nie wiesz, powiedz, że trzeba sprawdzić aktualne warunki.
Odpowiadaj po polsku.
```

## Aktualizacja danych

Pliki JSON są generowane na podstawie `datasets/tools-list.csv`. Przy dodaniu nowego narzędzia:
1. Dodaj wiersz w `datasets/tools-list.csv`
2. Zaktualizuj `datasets/tools-list.json`
3. Zaktualizuj `rag/qa-tools-index.json`
4. Utwórz plik narzędzia w odpowiednim katalogu `tools/`
