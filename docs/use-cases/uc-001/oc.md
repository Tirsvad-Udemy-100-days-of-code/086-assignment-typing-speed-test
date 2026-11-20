# Operation Contracts: UC-001 Take a typing test

## Metadata
| Key | Value |
| --- | --- |
| ID | OC-001 |
| CrossReference | [SSD-001], [DM-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-022 | [a388508] |

---

Terms are the IT terms of [DICT-001]. The affected concepts are those of [DM-001]. The contracts trace to the messages of [SSD-001].

## Operation: list_sample_texts

**Signature:** `list_sample_texts() -> tuple[SampleText, ...]`

**Cross References:** SSD-001 message `list_sample_texts`; use case extension 2a; concept SampleText.

**Preconditions:**
- None: the operation can run in any state.

**Postconditions:**
- No instance was created, associated or modified.
- The returned tuple holds the SampleText instances that exist, at least five.

**Exceptions:**
- None.

## Operation: start_test

**Signature:** `start_test(sample_text: SampleText | None = None) -> TypingTest`

**Cross References:** SSD-001 message `start_test`; use case steps 1 and 2, extension 2a; concepts SampleText, TypingTest.

**Preconditions:**
- None: the operation can run in any state.

**Postconditions:**
- A TypingTest instance was created and associated with the given SampleText, or with one of the existing SampleText instances chosen at random when none was given.
- The duration_seconds of the TypingTest was set to 60, its typed_text to empty, and its started_at and finished_at were left unset, so its state is READY.
- Any earlier TypingTest was dropped.

**Exceptions:**
- The given SampleText is empty: no instance is created and the earlier TypingTest stays as it was.

## Operation: type_text

**Signature:** `type_text(typed_text: str) -> TypingTest`

**Cross References:** SSD-001 message `type_text`; use case steps 3 to 5, extensions 3a and 3b; concepts TypingTest, SampleText.

**Preconditions:**
- A TypingTest exists (a `start_test` has completed).

**Postconditions:**
- The typed_text of the TypingTest was modified to the given text, unless the TypingTest was FINISHED or its time allowed had already run out, in which case it was not changed.
- If the TypingTest was READY and the given text is not empty, its started_at was set to the time of this call and its state is RUNNING.
- If the typed_text now has as many characters as the SampleText, or the time allowed has run out, the finished_at was set and the state is FINISHED.
- The returned TypingTest tells each character of the typed_text as correct or wrong, and the time left.

**Exceptions:**
- No TypingTest exists: nothing changes and the message asks to start a test first.
- The TypingTest is FINISHED: nothing changes, the input is ignored.

## Operation: check_time

**Signature:** `check_time() -> TypingTest`

**Cross References:** SSD-001 message `check_time`; use case steps 4 and 5; concept TypingTest.

**Preconditions:**
- A TypingTest exists.

**Postconditions:**
- If the TypingTest was RUNNING and the time allowed has run out, its finished_at was set and its state is FINISHED; otherwise no instance was modified.
- The returned TypingTest holds the time left.

**Exceptions:**
- No TypingTest exists: nothing changes and the message asks to start a test first.

## Operation: calculate_wpm

**Signature:** `calculate_wpm(correct_characters: int, elapsed_seconds: float) -> float`

**Cross References:** SSD-001 message `calculate_wpm`; use case step 6, extension 6a; concept TypingResult.

**Preconditions:**
- The correct_characters is not negative and the elapsed_seconds is not negative; both come from a FINISHED TypingTest.

**Postconditions:**
- No instance was created, associated or modified.
- The returned number is the correct_characters divided by five (characters per word) divided by the elapsed_seconds in minutes; it is 0 when the elapsed_seconds is 0.

**Exceptions:**
- A negative argument: no value is returned and the message says which argument is wrong.

## Operation: calculate_accuracy

**Signature:** `calculate_accuracy(correct_characters: int, typed_characters: int) -> float`

**Cross References:** SSD-001 message `calculate_accuracy`; use case step 6, extension 6a; concept TypingResult.

**Preconditions:**
- The correct_characters is not negative and not greater than the typed_characters.

**Postconditions:**
- No instance was created, associated or modified.
- The returned number is the correct_characters divided by the typed_characters, in percent; it is 0 when the typed_characters is 0.

**Exceptions:**
- The arguments are negative or the correct_characters is greater than the typed_characters: no value is returned and the message says so.

## Operation: save_high_score

**Signature:** `save_high_score(result: TypingResult) -> HighScoreList`

**Cross References:** SSD-001 message `save_high_score`; use case step 7, extension 7b; concepts TypingResult, HighScore.

**Preconditions:**
- The result comes from a FINISHED TypingTest.

**Postconditions:**
- A HighScore instance was created for the result, with achieved_on set to today, and associated with the HighScoreList.
- The HighScoreList keeps the ten best HighScore instances, best words per minute first, a tie broken by the higher accuracy; a HighScore that falls below the tenth was dropped.
- The HighScoreList was stored for the next start.
- The returned HighScoreList holds the ten best.

**Exceptions:**
- The HighScoreList cannot be stored: the earlier HighScoreList stays as it was and the message says that the result could not be remembered (extension 7b).

## Operation: list_high_scores

**Signature:** `list_high_scores() -> HighScoreList`

**Cross References:** SSD-001 message `list_high_scores`; use case steps 2 and 7, extension 7a; concept HighScore.

**Preconditions:**
- None: the operation can run in any state.

**Postconditions:**
- No instance was created, associated or modified.
- The returned HighScoreList holds the stored HighScore instances, best first, or is empty.

**Exceptions:**
- The stored list is missing or cannot be read: the returned HighScoreList is empty and no message is shown (extension 7a).

---

[SSD-001]: ./ssd.md
[DICT-001]: ../../dictionary.md
[DM-001]: ./dm.md
[a388508]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/a388508748c9a53f3406d8634714e2d0caba7220
