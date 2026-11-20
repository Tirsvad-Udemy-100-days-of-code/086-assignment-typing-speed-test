# Gateway 5: Step 3, result and restart

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-009 | pending |

---

## Purpose

Decide whether step 3 is done: when the test ends the window shows the words per minute and the accuracy, and the user can restart the test.

## Deliverable

A running application that reports `calculate_wpm` and `calculate_accuracy` and offers a restart button, with unit tests for known inputs, a graphical test, two screenshots (the result, and the restarted window) in the README and the wiki, and the step 3 wiki page in three languages.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `calculate_wpm` counts five correct characters as one word and divides by the elapsed minutes | 300 correct characters in 60 seconds give 60; 0 characters give 0; a test shorter than 60 seconds uses its real elapsed time | A result differs |
| 2 | `calculate_accuracy` returns the percentage of typed characters that are correct | Unit tests for all right, all wrong, mixed and empty input (100 percent defined as 0 for empty input) pass | A test fails |
| 3 | The restart resets the time, the input and the feedback and shows a text | A unit test of the view model and the graphical test pass | State remains from the earlier test |
| 4 | The code follows the accepted design | The code review record states each class and operation traces to the design class diagram | A deviation is not recorded |
| 5 | Tests and static checks pass | `scripts/check.sh` exits 0, with 0 opengrep WARNING or ERROR findings | Any failure |
| 6 | The code review has a Go verdict | A review record against `QC-PY-001` with verdict Go | No-Go |
| 7 | Two screenshots exist and are used | `docs/screenshots/step-3-*.png` are linked from `README.md` and from the three step 3 wiki pages | A link or language is missing |
| 8 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The result is computed from a finished test |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O3, O5 | [BC-001] |
| US-001.03 See words per minute and accuracy, US-001.04 Try again | [US-001] |
| US-001.08 Read what each step taught | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-25 — inside the Business Case window that ends 2026-11-27.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the result rules | Write the typing result in the domain with `calculate_wpm` and `calculate_accuracy`, using the five-characters-per-word constant from `constants.py`, and the use case that builds the result from a finished test. Test known inputs and the empty case. | Yes | UC-001, US-001.03 |
| 2 | Show the result in the view and view model | Show the words per minute, the accuracy and the number of correct and wrong characters when the test ends, and add the restart button with its view model command. Test the view model without a window. | Yes | UC-001, US-001.03, US-001.04 |
| 3 | Test the window and capture screenshots in Docker | Extend the graphical test in the Docker harness to finish a test, check the shown result, press restart, and write `step-3-result.png` and `step-3-restart.png`. The environment is a Docker container (Linux). No host desktop is used. | Yes | UC-001, framework/process/gui-testing.md |
| 4 | Update the README for step 3 | Add the step 3 section with both screenshots and how the words per minute are counted, and keep the table of contents current. | No | BC-001 O5 |
| 5 | Write the step 3 wiki pages in three languages | Write `Step-3-Result` in three languages with the screenshots and a section on what step 3 taught (the five-character word convention, pure functions that are easy to test, resetting state). Add them to the sidebar. | No | BC-001 O5; US-001.08 |
| 6 | Run quality gates, code review and open the pull request for Gateway 5 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O7 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
