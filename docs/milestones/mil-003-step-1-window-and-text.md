# Gateway 3: Step 1, window and sample text

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-007 | pending |

---

## Purpose

Decide whether step 1 is done: the application opens a window, `start_test` chooses a sample text, and the window shows the text with an empty input field and a time that is not running yet.

## Deliverable

A running application that shows the sample text and an input field, with unit and graphical tests, two screenshots (the window as it opens, and the window with a sample text next to the keyboard focus) in the README and the wiki, and the step 1 wiki page in English, Danish and Bahasa Malaysia.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m typing_speed_test` opens the main window | The container graphical test exits 0 | The window does not open |
| 2 | `start_test` returns a test in the ready state with a sample text and no running time | Unit tests with a fake text source pass | A test fails |
| 3 | The code follows the accepted design | The code review record states each class and operation traces to the design class diagram | A deviation is not recorded |
| 4 | Tests and static checks pass | `scripts/check.sh` exits 0, with 0 opengrep WARNING or ERROR findings | Any failure |
| 5 | The code review has a Go verdict | A review record against `QC-PY-001` with verdict Go | No-Go |
| 6 | Two screenshots exist and are used | `docs/screenshots/step-1-*.png` are linked from `README.md` and from the three step 1 wiki pages | A link or language is missing |
| 7 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The code is written from the accepted design artifacts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O3, O5 | [BC-001] |
| US-001.01 Read a sample text | [US-001] |
| US-001.08 Read what each step taught | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-23 — inside the Business Case window that ends 2026-11-27.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the domain and the start_test use case | Write the sample text entity, the typing test in its ready state, the domain error for an empty text, and the `start_test` use case with the port it needs to get a text. Test the use case with a fake of the port, so no window is involved. | Yes | UC-001, US-001.01 |
| 2 | Implement the built-in text source | Write the adapter that gives the first sample text from a list kept in the infrastructure layer. More texts are added in step 4. Test it without a window. | Yes | UC-001, US-001.01 |
| 3 | Implement the main window and view model | Write the Tkinter main window with the sample text, the input field and the status line, and its view model that calls the use case. The view holds no rule, as the MVVM pattern requires. Test the view model without a window. | Yes | UC-001, US-001.01 |
| 4 | Add the composition root and entry point | Wire the layers once in one place and start the application with `python -m typing_speed_test`. | No | ADR-0002 |
| 5 | Test the window and capture screenshots in Docker | Run a graphical test in the Docker harness that opens the window and writes two screenshots, `step-1-window.png` and `step-1-text.png`, to `docs/screenshots/`. The environment is a Docker container (Linux). No host desktop is used. | Yes | UC-001, framework/process/gui-testing.md |
| 6 | Update the README for step 1 | Add the step 1 section with both screenshots and the command to run the program, and keep the table of contents current. | No | BC-001 O5 |
| 7 | Write the step 1 wiki pages in three languages | Write `Step-1-Window-And-Text`, `Step-1-Window-And-Text-da` and `Step-1-Window-And-Text-ms` with the screenshots and a section on what step 1 taught (a layered design, a port with a fake, a view that holds no rule). Add them to the sidebar. | No | BC-001 O5; US-001.08 |
| 8 | Run quality gates, code review and open the pull request for Gateway 3 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O7 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
