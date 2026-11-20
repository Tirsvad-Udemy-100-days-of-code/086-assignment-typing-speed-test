# Use Case UC-001: Take a typing test

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-019 | pending |

---

## Format and Level

Format: Fully Dressed. Level: user-goal.

## Scope

The Typing Speed Test Desktop App, seen as a black box.

## Primary Actor

User (S01, S02), as named in [UCD-001].

## Stakeholders and Interests

- S01 wants a correct, reviewable solution of the assignment: the speed and the accuracy are counted the way the assignment says.
- S02 wants the four functions `start_test`, `calculate_wpm`, `calculate_accuracy` and `save_high_score` to be easy to find and follow.
- S03 wants a result that can be seen at a glance in the screenshots.

## Preconditions

The application is installed and started. Python 3.13 or newer is installed.

## Postconditions (Success Guarantee)

The User has seen a sample text, typed it against the clock, and seen the words per minute, the accuracy and the number of right and wrong characters. A result that is among the ten best is remembered for the next time the application starts.

## Main Success Scenario

1. The User asks to start a typing test, or the application is started.
2. The system shows the ten best results so far, a sample text and the time allowed. The time is not running.
3. The User types the sample text. The time starts with the first typed character.
4. The system shows each typed character as right or wrong, and the time left, while the User types.
5. The system ends the test when the whole text is typed or the time allowed has run out.
6. The system shows the words per minute, the accuracy, and the number of right and wrong characters.
7. The system remembers the result if it is among the ten best, and shows the updated list.
8. The User may ask to try again. The scenario continues at step 1.

## Extensions

- 2a. The User chooses another sample text before typing the first character: the system shows the chosen text. The scenario continues at step 3.
- 3a. The User types nothing: the time does not start and the test does not end. The scenario stays at step 3.
- 3b. The User deletes typed characters: the typed characters are shown again as right or wrong, and the characters typed so far are counted again. The scenario continues at step 4.
- 6a. No right characters were typed: the system shows 0 words per minute and 0 percent accuracy. The scenario continues at step 7.
- 7a. The remembered results are missing or cannot be read when the application starts: the system starts with an empty list and says nothing more. The scenario continues at step 2.
- 7b. The result cannot be remembered: the system shows the result and says that it could not be remembered. The scenario continues at step 8.

## Special Requirements and Business Rules

- Step 2: at least five sample texts exist; one is chosen at random when the test starts. The time allowed is 60 seconds.
- Step 3: the time starts with the first typed character, never before.
- Step 6: five characters count as one word. The words per minute is the number of right characters divided by five, divided by the minutes used. The accuracy is the number of right characters divided by the number of typed characters, in percent.
- Step 7: the list keeps the ten best results, best words per minute first; a tie is broken by the higher accuracy.
- The screen design is in the wireframe `wireframe.md` of this folder.

## Open Issues

None.

---

[UCD-001]: ../../use-case-diagram.md
[US-001]: ../../user-stories.md
[SA-001]: ../../stakeholder-analysis.md
