# ADR-0002: Layered architecture with MVVM and the function names

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-012 | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The project is small, but the framework asks for the business rules to stay independent of the window and of the clock, and S02 wants readable code with clear function names (concern CN-004). Time is the hard part to test: a test that waits for 60 seconds is slow and flaky (risk in the Business Case). Options:

1. One script with the rules inside the window callbacks. Short, but the rules cannot be tested without a window, and tests would have to wait for real time.
2. Layers `domain`, `application`, `infrastructure` and `presentation` with Model-View-ViewModel (MVVM) in `presentation`, the clock and the high score store as ports.
3. The same layers with a separate `adapters` layer. Cleaner on paper, heavier for a project of this size.

## Decision

The source is laid out in the layers `domain`, `application`, `infrastructure` and `presentation` under `src/typing_speed_test/`, with MVVM in `presentation`, as the framework's default; the adapters are merged into `infrastructure`. The clock and the high score store are ports (protocols) of the application layer, and a fake clock is used in tests. The four names `start_test`, `calculate_wpm`, `calculate_accuracy` and `save_high_score` are the public operations of the use cases and the commands of the view model; the domain dictionary records the pair of Product Owner term and technical term. `constants.py` sits in the package root and is imported by every layer.

## Consequences

**Positive:**

- The rules are tested with fakes, without a window and without waiting.
- The import-linter contracts keep the dependency direction from drifting.
- S02 finds the function names in one place per layer.

**Negative:**

- More files than a single script, which a beginner may find heavy; the wiki step pages explain each layer when it is introduced.
- Mapping between view model data and domain objects adds small amounts of code.

## Affected Artifacts

- [BC-001] — objectives O1 and O3.
- [SA-001] — concern CN-004 of S02 and CN-009 of S01.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
