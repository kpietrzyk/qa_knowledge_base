# QA Tools Knowledge Base

Praktyczna baza wiedzy o narzędziach QA, szczególnie dla **manualnego testera aplikacji mobilnych**, który chce wejść w automatyzację i rozsądnie używać AI.

> ⚠️ **Uwaga:** Nazwa repozytorium zawiera literówkę (`knowladge` zamiast `knowledge`) — zostanie poprawiona w kolejnej wersji.

---

## Dla kogo jest to repozytorium?

To repo jest dla:
- **manualnych testerów aplikacji mobilnych** (Android / iOS),
- **testerów webowych** testujących panele admin, PWA, webview,
- **juniorów i mid-level QA** budujących portfolio na GitHub,
- osób, które **znają podstawy QA i chcą wejść w automatyzację**,
- testerów, którzy chcą **używać AI bez bezmyślnego kopiowania** odpowiedzi.

## Czego to repozytorium NIE robi

- ❌ Nie zastępuje doświadczenia testera.
- ❌ Nie uczy całej teorii ISTQB od zera.
- ❌ Nie jest rankingiem sponsorowanych narzędzi.
- ❌ Nie gwarantuje, że każde narzędzie jest darmowe komercyjnie — **licencję trzeba sprawdzić** przed użyciem w firmie.
- ❌ Nie zastępuje weryfikacji przez testera — AI generuje drafty, nie gotowe rozwiązania.

---

## Najważniejsza zasada

To repozytorium nie ma być encyklopedią. Ma praktycznie odpowiadać na pytania:

1. Do czego służy dane narzędzie?
2. Kiedy manualny tester aplikacji mobilnych powinien go użyć?
3. Czy narzędzie jest darmowe?
4. Czy wymaga kodowania?
5. Jaki jest pierwszy praktyczny krok?
6. Jak AI może pomóc w pracy z tym narzędziem?
7. Jaki jest następny krok w stronę automatyzacji?

---

## Główna oś repozytorium

```text
wymaganie → ryzyko → przypadki testowe → test manualny → dowody → bug report
     → analiza API/logów → regresja → automatyzacja → raport
```

To jest proces pracy testera QA. Każde narzędzie w tym repo służy do jednego lub kilku etapów tego procesu.

---

## Struktura repozytorium

```text
qa_knowladge_base/
├── README.md                    ← ten plik
├── GLOSSARY.md                  ← słownik terminów dla juniorów
├── TOOLS_RANKING.md             ← od czego zacząć (Tier 1/2/3)
├── CONTRIBUTING.md              ← jak współtworzyć repo
├── roadmap.md                   ← plan rozbudowy
├── SOURCES.md                   ← źródła i weryfikacja
│
├── tools/                       ← opisy narzędzi według kategorii
│   ├── mobile/                  ← Android, iOS, ADB, scrcpy, Appium, Maestro...
│   ├── api/                     ← Postman, Bruno, HTTP Toolkit, Reqable...
│   ├── web/                     ← Playwright, DevTools, Lighthouse...
│   ├── ai/                      ← Copilot, Ollama, LM Studio, MCP...
│   ├── debugging/               ← proxy, crash reporting, monitoring
│   ├── test-management/         ← Jira, Qase, AgileTest, Kiwi TCMS...
│   ├── bug-reporting/           ← Jam, Greenshot, Loom, Instabug...
│   └── ui-inspection/           ← Layout Inspector, Figma Dev Mode, a11y...
│
├── workflows/                   ← 🆕 procesy krok po kroku
│   ├── bug-investigation-mobile.md
│   ├── bug-investigation-api.md
│   ├── crash-analysis-android.md
│   ├── regression-before-release.md
│   ├── exploratory-session.md
│   ├── ai-assisted-test-design.md
│   └── from-manual-to-automation.md
│
├── prompts/                     ← gotowe prompty AI dla testera
├── checklists/                  ← checklisty mobilne, release, security, a11y
├── templates/                   ← szablony bug reportu, test case, test plan
├── learning-paths/              ← ścieżki nauki od manual do automation
├── datasets/                    ← CSV/JSON z danymi o narzędziach
├── rag/                         ← dane maszynowe pod lokalnego asystenta AI
└── examples/                    ← przykładowy kod (Appium, Maestro, Playwright)
```

---

## Szybki start — od czego zacząć?

→ Przeczytaj [`TOOLS_RANKING.md`](TOOLS_RANKING.md) — tabela Tier 1/2/3

→ Przeczytaj [`learning-paths/manual-mobile-qa-to-automation.md`](learning-paths/manual-mobile-qa-to-automation.md)

→ Przejrzyj [`workflows/`](workflows/) — gotowe procesy testowania

→ Użyj [`prompts/`](prompts/) — gotowe prompty AI do codziennej pracy

---

## Status repozytorium

| Obszar | Status |
|---|---|
| Opisy narzędzi (50+) | ✅ |
| Prompty AI | ✅ |
| Checklisty | ✅ |
| Szablony | ✅ |
| Workflows | ✅ |
| Ścieżki nauki | ✅ |
| Datasets (CSV/JSON) | ✅ |
| RAG (schema + index) | ✅ |
| Portfolio projects | 🔄 W planach |
| Skills cards | 🔄 W planach |

**Ostatnia aktualizacja:** 2026-05-26
