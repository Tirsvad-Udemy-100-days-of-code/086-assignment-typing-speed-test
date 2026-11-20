# Gateway 4: Step 2, timer and live typing feedback

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-008 | [0f493f4] |

---

## Purpose

Decide whether step 2 is done: the time starts at the first typed character, the user sees which characters are right and wrong, and the test ends when the text is complete or the 60 seconds are over.

## Deliverable

A running application with a countdown and live feedback, with unit tests that use a fake clock (no test sleeps), a graphical test, two screenshots (typing with mistakes, and the finished state) in the README and the wiki, and the step 2 wiki page in three languages.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The time starts at the first character and not before | A unit test with a fake clock shows the start time is the time of the first input | The time starts at window open |
| 2 | The test ends at the end of the text or at 60 seconds, whichever comes first, and then locks the input | Unit tests for both endings pass | A test fails |
| 3 | Each typed character is marked right or wrong against the sample text | Unit tests for matching, wrong and deleted characters pass | A test fails |
| 4 | The code follows the accepted design | The code review record states each class and operation traces to the design class diagram | A deviation is not recorded |
| 5 | Tests and static checks pass | `scripts/check.sh` exits 0, with 0 opengrep WARNING or ERROR findings | Any failure |
| 6 | The code review has a Go verdict | A review record against `QC-PY-001` with verdict Go | No-Go |
| 7 | Tests need no real waiting | No test calls `sleep`; the clock is a port with a fake | A test sleeps |
| 8 | Two screenshots exist and are used | `docs/screenshots/step-2-*.png` are linked from `README.md` and from the three step 2 wiki pages | A link or language is missing |
| 9 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The step builds on the window and the ready test |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O3, O5 | [BC-001] |
| US-001.02 Type against a timer with live feedback | [US-001] |
| US-001.08 Read what each step taught | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-24 — inside the Business Case window that ends 2026-11-27.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the clock port and the typing rules | Write the clock port in the application layer and the typing test rules in the domain: start on the first character, compare each character with the sample, finish when the text is complete or the duration has passed. Test them with a fake clock. | Yes | UC-001, US-001.02 |
| 2 | Implement the system clock adapter | Write the adapter of the clock port that reads a monotonic time source, and test that it never goes backwards. | Yes | UC-001, US-001.02 |
| 3 | Add the typing input to the view and view model | Handle each key press in the input field, mark right and wrong characters with colour tags, show the countdown with a repeating timer callback, and lock the input when the test ends. The view model holds the rules; the view only draws. Test the view model with the fake clock. | Yes | UC-001, US-001.02 |
| 4 | Test the window and capture screenshots in Docker | Extend the graphical test in the Docker harness to type a text with a mistake and to let the test finish, and write `step-2-typing.png` and `step-2-finished.png`. The environment is a Docker container (Linux). No host desktop is used. | Yes | UC-001, framework/process/gui-testing.md |
| 5 | Update the README for step 2 | Add the step 2 section with both screenshots, and keep the table of contents current. | No | BC-001 O5 |
| 6 | Write the step 2 wiki pages in three languages | Write `Step-2-Timer-And-Typing` in three languages with the screenshots and a section on what step 2 taught (time as a port, tests without waiting, key events in Tkinter, a repeating `after` callback). Add them to the sidebar. | No | BC-001 O5; US-001.08 |
| 7 | Run quality gates, code review and open the pull request for Gateway 4 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O7 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[0f493f4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/0f493f4af963132d34a8a932f4984e783dc36894
