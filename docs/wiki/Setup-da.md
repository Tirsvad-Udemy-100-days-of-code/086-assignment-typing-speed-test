[English](Setup) · **Dansk** · [Bahasa Malaysia](Setup-ms)

# Opsætning

Denne side viser, hvordan du får projektet til at køre på din egen computer. Du skal bruge Python 3.13 eller nyere.

## Opret miljøet

Opret et lokalt virtuelt miljø med navnet `.venv` i projektmappen, aktivér det, og opgradér pip:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

På Linux og macOS aktiverer du det med `source .venv/bin/activate` i stedet.

## Installér projektet

```powershell
python -m pip install -e ".[dev]"
```

Kommandoen læser `pyproject.toml`. Programmet har ingen afhængigheder ved kørsel; gruppen `dev` tilføjer værktøjerne til test og kontrol.

## Kør programmet

Med miljøet aktivt starter du programmet fra projektmappen (fra trin 1):

```powershell
python -m typing_speed_test
```

## Kør testene

```powershell
python -m pytest
```

## Hvad vi fik ud af dette trin

- **Én konfigurationsfil.** `pyproject.toml` indeholder projektets navn, den Python-version det kræver, den tomme liste over afhængigheder ved kørsel og indstillingerne for alle værktøjer.
- **Et virtuelt miljø.** `.venv` holder projektets pakker adskilt fra resten af maskinen, så projektet kører ens overalt.
- **Tests fra første dag.** En første test kontrollerer allerede konstanterne, så vanen med at køre `pytest` begynder, før der findes nogen funktion.
- **Konstanter ét sted.** `constants.py` indeholder alle faste værdier, for eksempel testens 60 sekunder og de fem tegn i et ord, så intet tal gentages i koden.
- **Dokumenteret kildekode.** Doxygen-kommentarer og en `Doxyfile` gør kommentarerne til en manual, man kan bladre i.
- **En kvalitetsport.** `scripts/check.sh` kører test, linter, typekontrol og en sikkerhedsscanning før hver push.
- **Et sikkert sted til grafiske tests.** En Linux-container med en virtuel skærm kører vinduestestene og tager skærmbillederne, så testene aldrig overtager din mus og dit tastatur.
