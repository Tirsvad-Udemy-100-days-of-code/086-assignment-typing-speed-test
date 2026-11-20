[English](Step-2-Timer-And-Typing) · **Dansk** · [Bahasa Malaysia](Step-2-Timer-And-Typing-ms)

# Trin 2: timer og indtastning

Tiden starter med det første tegn, du skriver, og ikke når vinduet åbner. Mens du skriver, bliver rigtige tegn grønne og forkerte tegn røde i eksempelteksten, og statuslinjen tæller ned fra 60 sekunder. Testen slutter, når du har skrevet hele teksten, eller tiden er gået, og indtastningen låses.

![Indtastning med én fejl og 42 sekunder tilbage](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-2-typing.png)

![Testen er slut, og indtastningen er låst](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-2-finished.png)

## Kør det

```bash
python -m typing_speed_test
```

## Hvad trin 2 lærte os

- **Tid som en port.** Domænet læser aldrig et ur. `RecordInput` spørger en `Clock`-port om tiden og giver den videre, så en test bruger et falsk ur og aldrig sover.
- **Reglerne i værdiobjektet.** `TypingTest.with_typed_text` markerer hvert tegn, sætter starten ved det første input og afslutter testen. Hver ændring giver en ny test.
- **Tastehændelser i Tkinter.** Et spor på inputvariablen melder hver ændring, så det virker lige så godt at slette et tegn som at skrive et.
- **Et gentaget `after`-kald.** Vinduet kalder `check_time` hver 200 ms, så nedtællingen bevæger sig uden en tråd, og vinduet svarer stadig.

Trinnets filer: `typing_test.py`, `clock.py`, `record_input.py`, `system_clock.py`, `typing_view.py`.

[Home-da](Home-da) · [Setup-da](Setup-da)
