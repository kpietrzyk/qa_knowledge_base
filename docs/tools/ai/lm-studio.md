# LM Studio

## Kategoria

- Główna kategoria: `ai-for-testing`
- Podkategoria: `local-llm`
- Darmowe: `True`
- Poziom trudności: `easy`
- Wartość dla manualnego testera: `high`
- Wartość dla automatyzacji: `medium`
- Wymaga kodowania: `False`

## Do czego służy

Graficzny interfejs do pobierania i uruchamiania lokalnych modeli LLM — alternatywa dla Ollamy z pełnym GUI zamiast terminala. Idealne dla testerów, którzy chcą lokalnego AI bez komend w terminalu.

## Różnica względem Ollamy

| | Ollama | LM Studio |
|---|---|---|
| Interfejs | Terminal (CLI) | Aplikacja desktopowa (GUI) |
| Trudność startu | Easy-medium | Easy |
| Integracje | REST API, Continue.dev | Wbudowany chat, REST API |
| Zarządzanie modelami | Komendy `ollama pull` | Klik w aplikacji |
| Platforma | macOS, Linux, Windows | macOS, Windows, Linux |

## Najlepsze zastosowania

- analiza logów crashu w wbudowanym chacie — bez terminala,
- bezpieczne (lokalne) generowanie przypadków testowych z wewnętrznych wymagań,
- pobieranie i testowanie różnych modeli LLM z interfejsem graficznym,
- uruchamianie lokalnego serwera API kompatybilnego z OpenAI (do integracji z innymi narzędziami),
- eksperymenty z promptami dla testerów nielubiących terminala.

## Kiedy używać

Używaj LM Studio zamiast Ollamy, gdy wolisz aplikację graficzną od terminala. Zasada jest ta sama — dane firmowe (logi, kod, requesty z tokenami) nie opuszczają Twojego komputera.

## Pierwszy praktyczny workflow

1. Pobierz LM Studio ze strony lmstudio.ai i zainstaluj.
2. W zakładce "Discover" wyszukaj model (np. `Llama 3`, `Mistral`, `Phi-3`).
3. Kliknij Download — model pobierze się lokalnie.
4. Przejdź do zakładki "Chat" i załaduj pobrany model.
5. Wklej logi lub wymagania i zacznij rozmowę — w pełni offline.

## Następny krok

Włącz wbudowany serwer lokalny (zakładka "Local Server") — udostępnia API kompatybilne z OpenAI, dzięki czemu możesz podłączyć LM Studio do Continue.dev lub własnych skryptów.

## Ryzyka i ograniczenia

- Nie traktuj narzędzia jako celu samego w sobie.
- Sprawdź licencję modelu przed użyciem komercyjnym.
- Lokalne modele są słabsze od GPT-4/Claude — weryfikuj odpowiedzi krytycznie.
- Wymagania sprzętowe: min. 8GB RAM; GPU (Apple Silicon lub NVIDIA) znacznie przyspiesza.
- Nie wysyłaj danych firmowych do zewnętrznych modeli — upewnij się, że model jest lokalny.

## Link

https://lmstudio.ai/

## Prompt AI do nauki narzędzia

```text
Jesteś seniorem QA Mobile. Naucz mnie LM Studio jako testera manualnego.
Kontekst: chcę lokalnego AI do analizy logów i generowania TC bez wysyłania danych do chmury.
Chcę wiedzieć:
1. jak zainstalować i wybrać dobry model dla QA,
2. jak prowadzić rozmowę z modelem (dobre vs złe prompty),
3. jak analizować logi z Logcata przez LM Studio,
4. jak porównać LM Studio z Ollamą — co kiedy wybrać,
5. jak używać lokalnego serwera API do integracji z innymi narzędziami.
```
