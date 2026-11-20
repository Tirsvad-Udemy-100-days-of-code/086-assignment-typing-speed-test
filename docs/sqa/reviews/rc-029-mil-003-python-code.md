# Review Record: Python source of gateway 3

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-029 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | [beefe6c] |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: [QC-PY-001]
- Scope: full review of the code of MIL-003 in `src/typing_speed_test/` and `tests/`
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case modules and functions, PascalCase classes, UPPER_SNAKE constants in `constants.py` |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names follow the dictionary: `SampleText`, `TypingTest`, `start_test`, `duration_seconds` |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass; the one `# noqa: S311` on `random.choice` says why (a text pick, not a secret) |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated, including `-> None` |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `EmptySampleTextError` is raised on an empty text; no bare except exists |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default argument; no shadowed builtin |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened in this gateway |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class and function has a Doxygen `@brief` |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print and no logging |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | Classes trace to docs/dcd.md. Deviations recorded: (1) the import-linter contract now orders infrastructure above presentation, because `CompositionRoot` (Infrastructure in the DCD) builds `TypingView`; presentation still cannot import infrastructure. (2) `TypingView` has `open_window` and `focus_input` beside `run`, so the composition root opens no window and the GUI test can capture screenshots. (3) `TypingViewModel` has `sample_text`, `typed_text` and `status_text`. (4) `ListSampleTexts`, the typing methods of `TypingTest`, `Clock`, `RecordInput`, `TypingResult` and the high score classes are left to later gateways (steps 2 to 4) |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 28 unit tests named for behaviour, with fakes, no network and no order dependence; one GUI test in Docker |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes without `Any` |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; the dev group is unchanged |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each constant is defined once in `constants.py` |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Imports point inward under the contract; `domain` and `application` import no window library; 2 contracts kept |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change per class; `TypingViewModel` forwards, `StartTest` orders the steps |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | The four layer packages hold the code; `presentation/features/typing_test/` groups the window |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Names are English, lower case, `_` and `.` only |

## Overall Verdict

Go — every Mandatory criterion passes; no action items

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-20 |

---

[MIL-003]: ../../milestones/mil-003-step-1-window-and-text.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[beefe6c]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/beefe6c8697bf2dc6ea4a4c09caae4a1f468ca9d
