# Gateway 1: Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-005 | pending |

---

## Purpose

Decide whether the repository, the tooling and the documentation skeleton are ready for design and coding: a reproducible Python 3.13 environment, the quality gates, the Docker harness for graphical tests, the README and the wiki skeleton, and the recorded technology decisions.

## Deliverable

A repository on the git host with a description and topics, containing `pyproject.toml` with no runtime dependency, `.gitignore`, `.editorconfig`, `Doxyfile`, the package skeleton with `constants.py`, a passing smoke test, a local quality gate script that runs opengrep, a Docker harness that captures a screenshot of an empty window, a `README.md` from the framework template, the wiki skeleton in English, Danish and Bahasa Malaysia, and the architecture decision records.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The repository has a description and at least five topics | The git host API returns both | Either is empty |
| 2 | A fresh `.venv` on Python 3.13 installs the project with `python -m pip install -e ".[dev]"` and the smoke test passes | `pytest` exits 0 | Install or test fails |
| 3 | `[project] dependencies` is empty | The list in `pyproject.toml` is empty | A runtime dependency is declared |
| 4 | Doxygen builds the documentation | `doxygen Doxyfile` reports 0 warnings | Any warning |
| 5 | The README and the editor configuration follow the framework | `check-readme.sh` and `check-editorconfig.sh` exit 0 | Either exits non-zero |
| 6 | The local quality gate passes | `scripts/check.sh` exits 0, including the opengrep scan with 0 WARNING or ERROR findings | Any finding or failure |
| 7 | The Docker harness works | The container run exits 0 and writes a screenshot file of an empty window to `docs/screenshots/` | No screenshot, or the host desktop was used |
| 8 | The wiki skeleton exists in three languages | `Home`, `Setup` and `_Sidebar` exist, with `-da` and `-ms` variants of the pages | A page of a language is missing |
| 9 | The baseline documents are accepted | BC-001, SA-001, US-001, PP-001 and MIL-001 to MIL-006 are `Accepted` with a Go review record each | A document is not accepted |
| 10 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway; follows the accepted Business Case, Stakeholder Analysis, Project Plan and this milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, O4, O5, O6, O7, O8 | [BC-001] |
| Success criteria 3, 7, 8 | [BC-001] |
| US-001.07 (run from the README), US-001.08 (wiki in my language) | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-21 — inside the Business Case window that ends 2026-11-27.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Review and accept the baseline documents | Review the Business Case, the Stakeholder Analysis, the user stories, the Project Plan and the six milestones against their checklists, record each review as an `RC-*` record, and set each row to `Accepted` on a Go. The reviews are stand-in reviews and say so. This is the acceptance the plan-first gate needs before any file goes under `src/` or `tests/`. | No | framework/process/plan-first-gate.md |
| 2 | Set repository description and topics | Set a one-sentence description and at least five topics (for example python, tkinter, typing-speed-test, desktop-app, udemy, 100-days-of-code) on the git host through its API, using the repository token from the personal `.env` file without printing or copying it. This gives repository visitors (S03) a clear first impression and meets objective O8. | No | BC-001 O8 |
| 3 | Create pyproject.toml | Declare the project with `requires-python = ">=3.13"`, the `src` layout, an empty list of runtime dependencies, and an optional `dev` group with pytest, pytest-cov, ruff, mypy and import-linter, plus their configuration. One file configures the whole project, as the Product Owner asked. | No | BC-001 O4, O6 |
| 4 | Add Python .gitignore | Add a Python `.gitignore` that also ignores `.venv`, `.env`, coverage output, Doxygen output and the prompt log folder when the repository is public. This keeps secrets and generated files out of the repository. | No | BC-001 O4 |
| 5 | Add .editorconfig and its check | Create the root `.editorconfig` from the framework baseline and make `check-editorconfig.sh` pass, so every editor formats files the same way. | No | AGENTS.md rule 10 |
| 6 | Create package skeleton and constants.py | Create `src/typing_speed_test/` with `__init__.py` and `constants.py` (application name, test duration in seconds, characters per word, number of high scores kept, high score file name), and `tests/unit/` with a first test of the constants. All constants live in one module, as the Product Owner asked. | No | BC-001 O3, O4 |
| 7 | Add Doxyfile and Doxygen comment style | Add a `Doxyfile` for Python that reads `src/` and writes to `build/doxygen/`, and define the Doxygen comment style used in source (documentation comments with `@brief`, `@param`, `@return`). A build with no warnings proves the style works. | No | BC-001 O3 |
| 8 | Write README.md from the framework template | Fill the framework README template: overview, requirements, setup with creating a local `.venv` and `python -m pip install --upgrade pip`, run, tests, license and the document appendix. Step screenshots are added by the step gateways. | No | BC-001 O4, O5 |
| 9 | Add local quality gate script with opengrep | Add `scripts/check.sh` that runs pytest, ruff, mypy, import-linter and the opengrep scan (`~/.opengrep/cli/latest/opengrep.exe`) with the rules in `config/opengrep-python.yml`, and fails on any finding. It is run before every push, as the Product Owner asked. | No | BC-001 O7 |
| 10 | Add Docker harness for GUI tests and screenshots | Add a Dockerfile and a run script that start the application under a virtual display (Xvfb) in a Linux container, run the graphical tests, and write screenshots to `docs/screenshots/`. This is the GUI test environment required by the framework: the host desktop is never used. The environment is a Docker container (Linux). No host desktop is used. | No | framework/process/gui-testing.md |
| 11 | Add wiki skeleton in three languages | Create `docs/wiki/` with `Home`, `Setup` and `_Sidebar`, in English and with `-da` (Danish) and `-ms` (Bahasa Malaysia) variants. Explain what the setup step taught. Check that the wiki is enabled for the repository. | No | BC-001 O5; US-001.08 |
| 12 | Install git hooks | Run the framework's hook installer, with the plan gate enabled, so commits on `main` are refused and the gate is enforced for `src/` and `tests/`, which keeps the one-branch-per-step discipline. | No | BC-001 O7 |
| 13 | Record the technology and process decisions as ADRs | Write four architecture decision records: Tkinter and the standard library only, with Python 3.13 or newer; layered architecture with MVVM and the function names; GUI tests and screenshots in Docker; and the artifact types that are skipped, with the reason, together with the Doxygen and wiki conventions. | No | BC-001 Assumptions |
| 14 | Run quality gates, code review and open the pull request for Gateway 1 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O7 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
