# User Stories: Typing Speed Test Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [BC-001], [MIL-003], [MIL-004], [MIL-005], [MIL-006] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-003 | pending |

---

## Purpose and Scope

The stories cover the epic "Test and train my typing speed" of [BC-001]: the four build steps of the application, and two stories about reading and running the repository. The actor of the application stories is the user of the program, who is S01 and any participant (S02) who runs the code; the actor is named `User`. One use case, UC-001 "Take a typing test", covers stories US-001.01 to US-001.06. Stories US-001.07 and US-001.08 are not goals of an actor of the system; they stay plain tasks.

## Story List

### US-001.01 — Read a sample text

**As a** User, **I want** to see a sample text in the window, **so that** I know what to type.

**Acceptance Criteria**

- Given the program starts, then the window shows a sample text and an empty input field.
- Given the window is open, then the time is not running until I start typing.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-003] | fits one iteration | none | Must | Every other story needs a sample text (dependency) |

### US-001.02 — Type against a timer with live feedback

**As a** User, **I want** the timer to start when I type the first character, and to see which characters are right and wrong while I type, **so that** I can correct my rhythm.

**Acceptance Criteria**

- Given the window is open, when I type the first character, then a 60 second countdown starts.
- Given I am typing, then characters that match the sample are marked correct and the others are marked wrong.
- Given I have typed the whole text or the 60 seconds are over, then the test ends and the input is locked.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-004] | fits one iteration | none | Must | Core goal of the assignment (BC-001 O1) |

### US-001.03 — See words per minute and accuracy

**As a** User, **I want** to see my words per minute and my accuracy when the test ends, **so that** I know how fast and how precise I am.

**Acceptance Criteria**

- Given the test has ended, then the window shows words per minute, accuracy in percent, and the number of correct and wrong characters.
- Given I typed 300 correct characters in 60 seconds, then the result is 60 words per minute (five characters per word).
- Given I typed nothing, then the result is 0 words per minute and the program does not fail.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-005] | fits one iteration | none | Must | The assignment asks for the words per minute (BC-001 O1) |

### US-001.04 — Try again

**As a** User, **I want** to restart the test, **so that** I can improve my result.

**Acceptance Criteria**

- Given a test is running or has ended, when I press the restart button, then the timer is reset, the input is empty and a sample text is shown.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-005] | fits one iteration | none | Must | Practice needs repetition (BC-001 O2) |

### US-001.05 — Choose a text sample

**As a** User, **I want** to choose among several sample texts, **so that** I do not practise the same sentence every time.

**Acceptance Criteria**

- Given the window is open, then at least five sample texts are available and one is chosen at random at the start.
- Given a test has not started, when I choose another text, then the new text is shown.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-006] | fits one iteration | none | Should | The assignment suggests more samples as an extension (BC-001 O2) |

### US-001.06 — Keep and see high scores

**As a** User, **I want** my best results to be kept between runs and shown in the window, **so that** I can see my progress.

**Acceptance Criteria**

- Given a test has ended, then the result is stored in a high score list of at most ten entries, best first.
- Given I close and start the program again, then the high scores are still shown.
- Given the stored file is missing or unreadable, then the program starts with an empty list and shows no error.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-006] | fits one iteration | none | Should | The assignment suggests high scores as an extension (BC-001 O2) |

### US-001.07 — Run the project from the README

**As a** participant (S02), **I want** the README to tell me how to create `.venv`, upgrade pip, run the program and run the tests, **so that** I can run the solution on my machine.

**Acceptance Criteria**

- Given a fresh clone, when I follow the README, then the program starts and the tests pass.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [BC-001] O4 | fits one iteration | none | Must | S02 concern CN-005; a plain task, not a goal of an actor of the system |

### US-001.08 — Read what each step taught

**As a** participant (S02), **I want** a wiki page per build step in English, Danish or Bahasa Malaysia, with a screenshot, **so that** I learn what the step added.

**Acceptance Criteria**

- Given a build step is done, then a wiki page exists in the three languages with the step's screenshot and a section on what the step taught.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [BC-001] O5 | fits one iteration | none | Must | S01 concern CN-003; a plain task, not a goal of an actor of the system |

## INVEST Check

Each story is Independent (US-001.02 needs US-001.01 only as a window), Negotiable, Valuable, Estimable, Small and Testable. US-001.03 and US-001.04 are bundled in one gateway; they stay separate stories because each has its own acceptance criteria.

---

[BC-001]: ./business-case.md
[MIL-003]: ./milestones/mil-003-step-1-window-and-text.md
[MIL-004]: ./milestones/mil-004-step-2-timer-and-typing.md
[MIL-005]: ./milestones/mil-005-step-3-result.md
[MIL-006]: ./milestones/mil-006-step-4-trainer.md
