# AI tools for QA

AI w testowaniu ma największy sens w czterech miejscach:

1. Analiza wymagań i ryzyk.
2. Generowanie przypadków testowych.
3. Pomoc w automatyzacji.
4. Analiza logów, requestów i bug reportów.

AI nie powinno samodzielnie zatwierdzać jakości. Tester odpowiada za weryfikację, priorytety i kontekst biznesowy.

## Najlepszy start

- GitHub Copilot, jeśli firma już go daje.
- ChatGPT/Claude do analizy wymagań i tworzenia checklist.
- Continue.dev + lokalny model, jeśli prywatność jest ważna.
- Playwright MCP / Appium MCP do eksperymentów z agentami.

## ⚠️ Bezpieczeństwo danych firmowych

**Nie wklejaj do publicznych modeli AI (ChatGPT, Claude, Gemini):**
- kodu źródłowego objętego NDA,
- logów produkcyjnych z danymi użytkowników,
- requestów z tokenami autoryzacyjnymi,
- wewnętrznej dokumentacji technicznej.

**Używaj lokalnych modeli dla danych firmowych:**
- **Ollama** — lokalny LLM w terminalu (llama3, mistral, qwen2.5-coder)
- **LM Studio** — lokalny LLM z interfejsem graficznym

## Narzędzia w tej kategorii

| Narzędzie | Typ | Darmowe | Najlepsze do |
|---|---|---|---|
| GitHub Copilot | coding assistant | False | Pisanie testów, wyjaśnianie kodu |
| Continue.dev | local AI coding | True | Lokalny asystent w VS Code |
| Roo Code / Cline | agentic coding | True | Agent budujący testy w IDE |
| Testsigma | AI test automation | True (plan) | AI generuje i wykonuje TC z Jiry |
| MaestroGPT | AI YAML generator | True | Natural language → Maestro YAML |
| Playwright MCP | MCP web automation | True | AI agent sterujący przeglądarką |
| Appium MCP | MCP mobile automation | True | AI agent sterujący mobile |
| Browser Use | browser agent | True | AI automatyzujący procesy webowe |
| Ollama | local LLM | True | Bezpieczna analiza logów i kodu |
| LM Studio | local LLM GUI | True | Lokalny AI bez terminala |
