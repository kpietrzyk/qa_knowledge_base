# RAG Chunking Guide

## Czym jest chunking i dlaczego ma znaczenie?

RAG (Retrieval Augmented Generation) działa tak: system dzieli dokumenty na fragmenty ("chunks"), zamienia je na wektory (embeddings) i przy pytaniu wyszukuje najbardziej pasujące fragmenty. Jeśli chunk jest za duży — model dostaje za dużo kontekstu i "gubi się". Jeśli za mały — traci kontekst między sekcjami.

Ten przewodnik opisuje jak optymalnie podzielić pliki `.md` z tego repo dla lokalnego asystenta AI.

---

## Zalecane rozmiary chunków

| Typ dokumentu | Zalecany rozmiar | Dlaczego |
|---|---|---|
| Opis narzędzia (`tools/*.md`) | 300-500 tokenów na sekcję | Każda sekcja (`## Kiedy używać`, `## Workflow`) jest osobną jednostką semantyczną |
| Prompt (`prompts/*.md`) | Cały prompt jako 1 chunk | Prompt nie ma sensu bez pełnego kontekstu |
| Workflow (`workflows/*.md`) | 1 chunk na krok lub fazę | Kroki są sekwencyjne — zachowaj spójność |
| Checklista | Cały plik | Listy tracą sens po podziale |
| GLOSSARY.md | 1 chunk na definicję | Każdy termin jest niezależny |

---

## Strategia podziału plików narzędzi

Rekomendowana strategia: **podział po nagłówkach H2** (`##`)

```python
# Przykład pseudokodu podziału
sections_to_index = [
    "## Do czego służy",       # krótki opis — 1 chunk
    "## Kiedy używać",         # kontekst użycia — 1 chunk  
    "## Kiedy NIE używać",     # ważne dla trafności RAG
    "## Pierwszy praktyczny workflow",  # kroki — 1-2 chunki
    "## Troubleshooting",      # problemy — 1 chunk per problem
]

# Sekcje do pominięcia (nie dodają wartości semantycznej):
sections_to_skip = [
    "## Kategoria",           # metadane — dodaj do metadata, nie do tekstu
    "## Link",                # sam URL bez kontekstu
]
```

---

## Metadane (metadata) dla każdego chunku

Przy ładowaniu do bazy wektorowej (np. Chroma, Qdrant, pgvector) dołącz metadane:

```json
{
  "source_file": "tools/mobile/adb.md",
  "tool_name": "ADB",
  "category": "mobile-testing",
  "section": "Pierwszy praktyczny workflow",
  "difficulty": "medium",
  "free": true,
  "platform": ["Android"],
  "requires_code": false
}
```

Metadane umożliwiają filtrowanie: "pokaż tylko narzędzia darmowe dla Android" bez szukania po treści.

---

## Przykładowe konfiguracje

### LlamaIndex (Python)

```python
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import MarkdownNodeParser

# Wczytaj pliki narzędzi
documents = SimpleDirectoryReader(
    input_dir="tools/",
    recursive=True,
    required_exts=[".md"],
    exclude=["README.md"]
).load_data()

# Parser dzielący po nagłówkach H2
parser = MarkdownNodeParser()
nodes = parser.get_nodes_from_documents(documents)
```

### LangChain (Python)

```python
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter

# Nagłówki do podziału
headers_to_split_on = [
    ("#", "h1"),
    ("##", "h2"),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False
)
```

### Continue.dev (najprostsze użycie)

Nie potrzebujesz własnego RAG pipeline. Dodaj folder jako `@codebase` w Continue.dev:

```json
// ~/.continue/config.json
{
  "contextProviders": [
    {
      "name": "folder",
      "params": {
        "nRetrieve": 10,
        "nFinal": 3
      }
    }
  ]
}
```

Następnie w chacie: `@tools/mobile/adb.md jak zebrać logi do bug reportu?`

---

## Minimalne ustawienia jakości RAG

| Parametr | Zalecana wartość |
|---|---|
| Chunk overlap | 50-100 tokenów (zachowaj kontekst między sekcjami) |
| Embedding model | `text-embedding-3-small` (OpenAI) lub `nomic-embed-text` (lokalne) |
| Top-k retrieval | 3-5 dokumentów |
| Reranking | Zalecany przy >50 dokumentach |

---

## Testowanie jakości RAG

Przetestuj swój setup tymi pytaniami (oczekiwane źródła w nawiasach):

| Pytanie | Oczekiwane źródło |
|---|---|
| "Jak zebrać logi po crashu?" | `tools/mobile/adb.md`, `workflows/crash-analysis-android.md` |
| "Kiedy użyć Maestro zamiast Appium?" | `tools/mobile/maestro.md`, `TOOLS_RANKING.md` |
| "Jak podmienić response API?" | `tools/debugging/proxyman.md`, `workflows/bug-investigation-api.md` |
| "Jak wygenerować TC z User Story?" | `prompts/test-case-prompts.md`, `workflows/ai-assisted-test-design.md` |
| "Co to jest JWT?" | `GLOSSARY.md`, `tools/api/jwt-basics.md` |
