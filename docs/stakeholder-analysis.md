# Stakeholder Analysis: Typing Speed Test Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-002 | pending |

---

## Purpose

This analysis names the people the Typing Speed Test Desktop App affects, classifies them by power and interest, and records their concerns, so that every owner, reviewer and use case actor in the other documents uses a stable stakeholder ID. It follows the power/interest grid and maps each concern to a FURPS+ attribute (Functionality, Usability, Reliability, Performance, Supportability, plus implementation, interface, operations, packaging and legal constraints).

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Independent (Udemy course participant) | HIGH | HIGH | Manage Closely | A complete, correct and reviewable solution of the Day 86 assignment |
| S02 | Udemy course participants | Fellow learners who share code and compare solutions | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with clear function names, and instructions to run it |
| S03 | Repository visitors | People who browse the repository for ideas | Public readers of the git host | LOW | LOW | Monitor | A clear description, topics and README, and no runtime dependency |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** S01 decides scope, accepts every artifact and merges every pull request, and is the only person who works on the project every day.
- **Keep Informed (S02):** S02 cannot change the scope but reads the code closely and compares it with their own solution, so the README, the function names and the wiki matter to them.
- **Monitor (S03):** S03 reads the repository once, decides in a minute whether it is useful, and has no influence on the work; the description, topics and README serve them.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The application measures typing speed and accuracy correctly | Functionality |
| CN-002 | S01 | Every step is tracked as a branch and a pull request, and every artifact is reviewed | Supportability |
| CN-003 | S01 | The wiki exists in English, Danish and Bahasa Malaysia and shows what each step taught | Usability |
| CN-004 | S02 | The code is readable and uses clear function names | Supportability |
| CN-005 | S02 | The README explains how to create `.venv`, upgrade pip, run the program and run the tests | Usability |
| CN-006 | S02 | A screenshot shows the result of each build step | Usability |
| CN-007 | S03 | The repository has a clear description and topics | Usability |
| CN-008 | S03 | The repository needs no runtime dependency | Implementation |
| CN-009 | S01 | The timer is accurate and the window stays responsive while the user types | Reliability, Performance |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Pull request on the git host | One per milestone | Changes with the closing issue lines and the scan output | MIL-001 to MIL-006 |
| CR-002 | Summary in the session chat | At the end of each autonomous run | Merged pull requests, review verdicts, stand-in decisions | MIL-001 to MIL-006 |
| CR-003 | `README.md` | Updated in each step milestone | Run instructions and the step's screenshot | MIL-003 to MIL-006 |
| CR-004 | Wiki in English, Danish and Bahasa Malaysia | Updated in each step milestone | Step page with screenshot and what was learned | MIL-003 to MIL-006 |
| CR-005 | Repository description and topics | Once | Short description and topics | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 is author, owner and reviewer, so no independent review is possible | S01 | In autonomous mode each review is a stand-in review and says so on the record; S01 can challenge any record in the end-of-run summary |
| Three wiki languages increase the chance of inconsistent pages | S01, S02 | English is the authoritative text; a glossary of fixed terms per language; pages have the same structure |
| S02 wants plain function names, while clean architecture prefers names of the use case layer | S02, S01 (CN-004) | The presentation layer exposes `start_test`, `calculate_wpm`, `calculate_accuracy` and `save_high_score`; the dictionary records the pair of terms |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-009 | O1, O2 in [BC-001] |
| S01 | CN-002 | O7 in [BC-001] |
| S01 | CN-003 | O5 in [BC-001] |
| S02 | CN-004 | O3 in [BC-001] |
| S02 | CN-005 | O4 in [BC-001] |
| S02 | CN-006 | O5 in [BC-001] |
| S03 | CN-007 | O8 in [BC-001] |
| S03 | CN-008 | O6 in [BC-001] |

## Sign-Off

Reviewer: S01 (stand-in in autonomous mode; the review record states the mode). Accountable: S01.

---

[BC-001]: ./business-case.md
