# Review Record: Python source of gateway 4

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-030 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | [be04771] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001]
- Scope: full review of the code of MIL-004 in `src/typing_speed_test/` and `tests/`
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | PEP 8 casing throughout; new constants in `constants.py` in UPPER_SNAKE |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names follow the dictionary: `Clock`, `RecordInput`, `with_typed_text`, `remaining_seconds` |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass; no new suppression |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `NoActiveTestError` is raised when no test exists; no bare except |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default; no shadowed builtin |
| 7 | Files, locks and connections are managed with context managers | N-A | No file or connection is opened in this gateway |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every new module, class and function has a Doxygen `@brief` |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print and no logging |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | Classes and operations trace to docs/dcd.md. Deviations recorded: (1) `TypingViewModel(start_test_use_case, record_input_use_case, clock)` takes the clock, because `remaining_seconds(now)` needs the time. (2) `CompositionRoot.build(clock=None)` accepts a clock, so the GUI test passes a fake one. (3) `with_typed_text` cuts the typed text to the sample length. (4) The test is finished when the typed length equals the sample length, right or wrong. (5) On time out `finished_at` is `started_at + duration`, so `elapsed_seconds` is exactly the duration. (6) After time out `with_typed_text` refuses the new text and finishes the test, as the contract says. (7) `elapsed_seconds` is capped at the duration and `remaining_seconds` is never negative. (8) The sample text is a disabled `Text` widget with colour tags. (9) `TypingResult`, `Scoring`, the high score classes and `ListSampleTexts` come in steps 3 and 4 |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 71 tests named for behaviour, with a shared fake clock; nothing sleeps; two GUI tests in Docker |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes without `Any` |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []` |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each constant defined once; the shared `FakeClock` is in `tests/fake_clock.py` |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Imports point inward; 2 contracts kept; domain and application import no window library |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change per class; the view only draws what the view model returns |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers and `presentation/features/typing_test/` unchanged in shape |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Names are English, lower case, `_` and `.` only |

## Overall Verdict

Go — every Mandatory criterion passes; no action items

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-20 |

---

[MIL-004]: ../../milestones/mil-004-step-2-timer-and-typing.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[be04771]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/be047713fb8bc760120809b392bad161f8cb5a7b
