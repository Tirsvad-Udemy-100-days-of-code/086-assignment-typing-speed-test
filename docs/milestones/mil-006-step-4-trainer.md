# Gateway 6: Step 4, trainer with samples and high scores

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-010 | [0f493f4] |

---

## Purpose

Decide whether step 4 is done and the project is complete: the application has at least five sample texts to choose from, keeps the ten best results between runs, and the documentation shows all four steps in three languages.

## Deliverable

A running trainer with `save_high_score`, a text chooser and a high score list, with unit, integration and graphical tests, two screenshots (the text chooser, and the high scores) in the README and the wiki, the step 4 wiki page and the reflection page in three languages, the complete README, and a verified clean-container run.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | At least five sample texts exist, and one is chosen at random at the start | A unit test counts the texts and a seeded choice test passes | Fewer than five texts |
| 2 | `save_high_score` keeps the ten best results, best first, and writes them to a file | Unit tests with a fake store and an integration test with a temporary folder pass | A test fails |
| 3 | A missing or corrupt high score file gives an empty list and no error | Integration tests for both cases pass | A crash |
| 4 | The graphical test shows the chooser and the high scores | The container test exits 0 and writes the screenshots | The test fails |
| 5 | The code follows the accepted design | The code review record states each class and operation traces to the design class diagram | A deviation is not recorded |
| 6 | Tests and static checks pass | `scripts/check.sh` exits 0, with 0 opengrep WARNING or ERROR findings | Any failure |
| 7 | The code review has a Go verdict | A review record against `QC-PY-001` with verdict Go | No-Go |
| 8 | Coverage of the domain and application layers | At least 85 percent line coverage | Below 85 percent |
| 9 | From a fresh clone to the running application | The README commands, run in a clean container, take at most six commands and the program starts | More commands or a failure |
| 10 | The README and every wiki language show all four steps | At least four step screenshots, and 18 wiki pages plus the reflection page in each language, with the sidebar and language links | A page or image is missing |
| 11 | The wiki follows its checklist | A review record against `QC-WIKI-001` | No-Go |
| 12 | The pull request is open with its closing issue lines and no failing check | Body lists one `Closes #N` per line | A check fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | The high score list stores finished results |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O3, O4, O5, O6 | [BC-001] |
| US-001.05 Choose a text sample, US-001.06 Keep and see high scores | [US-001] |
| US-001.07 Run the project from the README, US-001.08 Read what each step taught | [US-001] |
| Success criteria 1 to 9 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-26 — inside the Business Case window that ends 2026-11-27.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the sample texts and the text chooser | Add at least five sample texts to the built-in source, a random start choice, and a chooser in the window that is usable until a test has started. Test the choice with a seeded random source and the view model without a window. | Yes | UC-001, US-001.05 |
| 2 | Implement the high score rules and the save_high_score use case | Write the high score entity, the rule that keeps the ten best, and the `save_high_score` use case with the store port. Test it with a fake of the port. | Yes | UC-001, US-001.06 |
| 3 | Implement the high score file store | Write the adapter that reads and writes the high scores as JSON in the user's home folder, and returns an empty list for a missing or corrupt file. Test it with files in a temporary folder. | Yes | UC-001, US-001.06 |
| 4 | Show the high scores in the window | Add the high score list to the view and view model, updated when a test ends. Test the view model without a window. | Yes | UC-001, US-001.06 |
| 5 | Test the window and capture screenshots in Docker | Extend the graphical test in the Docker harness to choose a text, finish a test and show the list, and write `step-4-chooser.png` and `step-4-scores.png`. The environment is a Docker container (Linux). No host desktop is used. | Yes | UC-001, framework/process/gui-testing.md |
| 6 | Complete the README | Add the step 4 section and screenshots, and make the README the single place that shows the four steps in order, with the final run and test instructions. | No | BC-001 O4, O5 |
| 7 | Write the step 4 and reflection wiki pages and complete the wiki | Write `Step-4-Trainer` and `Reflection` in three languages: the screenshots and a section on what step 4 taught (persistence behind a port, tolerant file reading), and the assignment's reflection (approach, what was hard and easy, the biggest learning, what to do differently). Complete the home pages and sidebar, and review the wiki against its checklist. | No | BC-001 O5; US-001.08 |
| 8 | Verify the success criteria in a clean container | Clone the repository into a clean container, follow only the README, and record the result for each success criterion of the Business Case. | No | BC-001 Success Criteria |
| 9 | Run quality gates, code review and open the pull request for Gateway 6 | Run the local quality gate, review the code against the Python checklist and record it, resolve pending commit links, push the branch and open the pull request that closes the issues of this gateway. | No | BC-001 O7 |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[0f493f4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/0f493f4af963132d34a8a932f4984e783dc36894
