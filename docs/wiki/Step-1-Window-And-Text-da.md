[English](Step-1-Window-And-Text) · **Dansk** · [Bahasa Malaysia](Step-1-Window-And-Text-ms)

# Trin 1: vindue og eksempeltekst

Programmet åbner et vindue, `start_test` vælger en eksempeltekst, og vinduet viser teksten med et tomt indtastningsfelt. Tiden løber ikke, før du skriver, så du kan læse teksten først.

![Vinduet, når det åbner](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-1-window.png)

![Indtastningsfeltet har fokus](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/raw/branch/main/docs/screenshots/step-1-text.png)

## Kør det

```bash
python -m typing_speed_test
```

## Hvad trin 1 lærte os

- **Et lagdelt design.** Reglerne ligger i pakkerne `domain` og `application`. Vinduet ligger i `presentation` og kender ingen regel. Pakken `infrastructure` rummer listen af tekster.
- **En port med en falsk udgave.** Use casen beder en `SampleTextSource` om en tekst. Den rigtige kilde er en liste af tekster; testene bruger en falsk, så der hverken skal bruges et vindue eller tilfældighed.
- **En visning uden regler.** `TypingViewModel` giver vinduet teksten og statuslinjen. Den importerer ikke Tkinter, så en almindelig test kan kontrollere den.

Trinnets filer: `start_test.py`, `typing_view_model.py`, `typing_view.py`, `composition_root.py`.

[Home-da](Home-da) · [Setup-da](Setup-da)
