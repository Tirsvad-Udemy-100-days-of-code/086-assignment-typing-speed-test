**English** · [Dansk](Setup-da) · [Bahasa Malaysia](Setup-ms)

# Setup

This page shows how to get the project running on your own machine. You need Python 3.13 or newer.

## Create the environment

Create a local virtual environment named `.venv` in the project folder, activate it, and upgrade pip:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

On Linux and macOS, activate it with `source .venv/bin/activate` instead.

## Install the project

```powershell
python -m pip install -e ".[dev]"
```

The command reads `pyproject.toml`. The program has no runtime dependency; the `dev` group adds the test and check tools.

## Run the application

With the environment active, start the program from the project folder (available from step 1):

```powershell
python -m typing_speed_test
```

## Run the tests

```powershell
python -m pytest
```

## What we gained in this step

- **One configuration file.** `pyproject.toml` holds the project name, the Python version it needs, its empty list of runtime dependencies and the settings of every tool.
- **A virtual environment.** `.venv` keeps the project's packages apart from the rest of the machine, so the project runs the same everywhere.
- **Tests from the first day.** A first test already checks the constants, so the habit of running `pytest` starts before any feature exists.
- **Constants in one place.** `constants.py` holds every fixed value, such as the 60 seconds of the test and the five characters of a word, so no number is repeated in the code.
- **Documented source.** Doxygen comments and a `Doxyfile` turn the comments into a browsable manual.
- **A quality gate.** `scripts/check.sh` runs tests, linter, type checker and a security scan before every push.
- **A safe place for graphical tests.** A Linux container with a virtual display runs the window tests and takes the screenshots, so the tests never take over your mouse and keyboard.
