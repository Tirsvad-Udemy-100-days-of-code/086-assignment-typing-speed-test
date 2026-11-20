# ADR-0001: Technology: Tkinter, the standard library only, and Python 3.13 or newer

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-011 | [0f493f4] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The assignment asks for a Tkinter desktop application that measures typing speed. The Business Case wants no runtime dependency (objective O6) and the stakeholder S03 asks for none (concern CN-008). The program needs a window, a text input, a timer, and a small file for high scores. Options:

1. Tkinter with the standard library only. Tkinter has a text widget with tags (for right and wrong characters), a repeating timer callback (`after`), and the standard library has `json`, `pathlib` and `time`.
2. Tkinter with a third-party package for colours, themes or timing. It adds an install step for no need the assignment has.
3. A GUI toolkit such as PySide6. It adds a large dependency and a licence to explain.
4. A web interface served locally. It needs a browser and a server, and the assignment asks for a desktop program.

Python 3.13 is installed on the development machine, and the Product Owner asked for "greater than 3.13", read as 3.13 or newer. The project needs one file for configuration (`pyproject.toml`), a virtual environment (`venv`), pytest, and development tools that check style and types.

## Decision

The application uses Tkinter for the window and the standard library for everything else, so it has no runtime dependency; it requires Python 3.13 or newer (`requires-python = ">=3.13"`) and builds with setuptools from `pyproject.toml`. pytest, pytest-cov, ruff, mypy and import-linter are optional development dependencies in the `dev` group.

## Consequences

**Positive:**

- Nothing to install at run time beyond Python itself; S03's concern CN-008 is met fully.
- A fresh clone runs in a few commands, which supports success criterion 4.
- The standard library is stable, so the project keeps working on later Python versions.

**Negative:**

- Tkinter looks different on each operating system, so screenshots from the Linux container differ from the Windows look.
- No library helps with fonts or themes; the window stays plain.
- Some Linux distributions ship Python without Tkinter; the README names the requirement.

## Affected Artifacts

- [BC-001] — objective O6 and the assumption about the reading of "greater than 3.13".
- [SA-001] — concern CN-008 of S03.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[0f493f4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/0f493f4af963132d34a8a932f4984e783dc36894
