# Gateway 2: Design

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-006 | pending |

---

## Purpose

Decide whether the design of the use case "Take a typing test" is complete and accepted, so that the step gateways can write code from it: the use case, its screen wireframe, the domain model, the system sequence diagram, the operation contracts, the sequence diagram and the design class diagram.

## Deliverable

The accepted use case diagram, and the design artifacts of use case UC-001 in `docs/use-cases/uc-001/`, the project-level `docs/domain-model.md` and `docs/dcd.md`, the domain dictionary `docs/dictionary.md` with the function names, and the traceability matrix `docs/sqa/traceability-matrix.md`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The use case diagram, the use case and its design artifacts exist in the order UCD, UC, DM, SSD, OC, SD, DCD | Each has a review record with verdict Go and an `Accepted` row | Any is missing or not accepted |
| 2 | The operations of the sequence diagram cover `start_test`, `calculate_wpm`, `calculate_accuracy` and `save_high_score` | Each name appears in the operation contract and the dictionary | A name is missing |
| 3 | The project-level domain model and design class diagram contain the use case's additions | `docs/domain-model.md` and `docs/dcd.md` are `Accepted` with a Go review | Either is missing |
| 4 | The wireframe shows every screen state of the four steps | `wireframe.md` shows ready, typing, finished with result, and high scores states | A state is missing |
| 5 | The clock and the high score store are ports in the design | The design class diagram shows both as interfaces of the application layer | Either is missing |
| 6 | The traceability matrix lists every accepted artifact with its last review | No row has an empty "Last Reviewed" | An empty cell |
| 7 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The ADRs, the registry rows and the repository tooling exist before design documents are reviewed |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O3, O7 | [BC-001] |
| US-001.01 to US-001.06 | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22 — inside the Business Case window that ends 2026-11-27.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the use case diagram UCD | Draw the use case diagram with one actor, User, and the use case "Take a typing test", so the stories name an actor that the diagram defines. One actor and one use case mean no role matrix is needed. | No | US-001 |
| 2 | Write use case UC-001 and its wireframe | Write the fully dressed use case "Take a typing test" with its main scenario (read the text, type, see the result, try again, choose a text, see high scores) and extensions (time runs out, nothing typed, high score file unreadable). Draw the wireframe of the main window in its states, because the Product Owner gave none. | Yes | US-001.01 to US-001.06 |
| 3 | Write the use case domain model DM | Model the concepts of the use case: Sample Text, Typing Test, Keystroke, Result, Words per Minute, Accuracy and High Score. Keep it conceptual, with the Product Owner's terms. | No | UC-001 |
| 4 | Write the system sequence diagram SSD | Show the interaction between the user and the system for the main scenario and name the system operations. | No | UC-001 |
| 5 | Write the operation contracts OC | Specify pre- and postconditions of `start_test`, `calculate_wpm`, `calculate_accuracy` and `save_high_score`, and of the input and restart operations, in the technical vocabulary. | No | UC-001 |
| 6 | Write the sequence diagram SD | Show how the presentation, application and infrastructure layers collaborate for each operation, including the clock and the high score store as ports. | No | UC-001 |
| 7 | Write the design class diagram DCD and update the project models | Write the use case DCD and add its concepts and classes to the project-level `docs/domain-model.md` and `docs/dcd.md`. State that no entity relationship diagram is needed because the high scores are one small file, not a database. | No | UC-001 |
| 8 | Write the domain dictionary DICT | Record each pair of Product Owner term and technical term, including the four function names, so code and documents use one vocabulary. | No | BC-001 O3 |
| 9 | Write the traceability matrix TM | Link each concern, objective, story, use case, design artifact and review record, and keep the "Last Reviewed" column current. | No | BC-001 O7 |
| 10 | Run reviews and open the pull request for Gateway 2 | Review every artifact against its checklist, record the review records, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O7 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
