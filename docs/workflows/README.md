# Workflow testera QA

Workflow to proces — sekwencja kroków, narzędzi i decyzji, która prowadzi od obserwacji problemu do zamkniętego zgłoszenia lub uruchomionego testu automatycznego.

## Dlaczego workflows są ważniejsze niż lista narzędzi

Znajomość narzędzi bez procesu = posiadanie skalpela bez wiedzy chirurga.

Workflow pokazuje:

- w jakiej kolejności używać narzędzi,
- kiedy przejść do kolejnego kroku,
- jak połączyć ADB + proxy + bug report w jedną procedurę,
- jak tester myśli, a nie tylko jakie ma narzędzia.

## Dostępne workflows

| Workflow | Kiedy używać | Typowy wynik |
| --- | --- | --- |
| [Analiza błędu w aplikacji mobilnej](bug-investigation-mobile.md) | Odtworzenie i udokumentowanie błędu mobilnego | Gotowe zgłoszenie z dowodami |
| [Analiza błędu API](bug-investigation-api.md) | Rozdzielenie problemu UI, API, danych, autoryzacji i konfiguracji | Hipoteza oparta na request/response |
| [Analiza crasha Android](crash-analysis-android.md) | Aplikacja zamknęła się lub przestała odpowiadać | Stack trace, kontekst i zgłoszenie |
| [Regresja przed releasem](regression-before-release.md) | Ocena ryzyka przed wydaniem wersji | Udokumentowana rekomendacja go/no-go |
| [Sesja eksploracyjna](exploratory-session.md) | Odkrywanie ryzyk bez gotowego skryptu | Błędy, obserwacje i pytania |
| [Projektowanie testów z pomocą AI](ai-assisted-test-design.md) | Przygotowanie draftu testów z wymagania | Zweryfikowane testy z traceability |
| [Od testu manualnego do automatycznego](from-manual-to-automation.md) | Ocena opłacalności i wybór właściwej warstwy testu | Kandydat automatyzacji lub decyzja o pozostawieniu testu manualnego |
