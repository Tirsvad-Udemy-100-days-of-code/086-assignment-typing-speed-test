# Domain Dictionary: Typing Speed Test Desktop App

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001], [DM-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-027 | [a388508] |

---

## Purpose and Scope

The Product Owner's language is English (`en`) and the domain is `it`, as the [registry][REG] says. The dictionary pairs each word of the Domain Model [DM-001] with the professional IT word used in the design artifacts, and fixes the four function names of the assignment in step with them. It covers every concept and the attributes that have an IT word of their own.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Accuracy | en | calculate_accuracy | The share of typed characters that are right, in percent. | UC | OC, SD, DCD |
| Date | en | achieved_on | The day on which a result was reached. | DM, UC | OC, SD, DCD |
| High score | en | HighScore | A result that is good enough to be kept among the ten best. | DM, UC | OC, SD, DCD |
| Remember a high score | en | save_high_score | Keep a result among the ten best for the next time. | UC | OC, SD, DCD |
| Result | en | TypingResult | How well someone did in one typing test, counted in right and wrong characters and the seconds used. | DM, UC | OC, SD, DCD |
| Right characters | en | correct_characters | The characters typed exactly as in the sample text. | DM, UC | OC, SD, DCD |
| Sample text | en | SampleText | A passage of ordinary writing that a person copies when practising typing. | DM, UC | OC, SD, DCD |
| Seconds used | en | elapsed_seconds | The time from the first typed character to the end of the test. | DM, UC | OC, SD, DCD |
| Start a test | en | start_test | Show a sample text and get ready to count the time. | UC | OC, SD, DCD |
| Time allowed | en | duration_seconds | How long a typing test lasts. | DM, UC | OC, SD, DCD |
| Typed wording | en | typed_text | What the person has typed so far. | DM, UC | OC, SD, DCD |
| Typing test | en | TypingTest | A timed attempt to copy a sample text as fast and as correctly as you can. | DM, UC | OC, SD, DCD |
| Wording | en | text | The words of a sample text. | DM, UC | OC, SD, DCD |
| Words per minute | en | calculate_wpm | The number of words typed right in one minute, five characters counting as one word. | UC | OC, SD, DCD |
| Wrong characters | en | wrong_characters | The characters typed differently from the sample text. | DM, UC | OC, SD, DCD |

## Rules

- The PO term is used in the Domain Model, the use cases and the user stories; the IT term is used in the Operation Contract, the Sequence Diagram and the Design Class Diagram.
- One IT term stands for one PO term, and the reverse. The rows are in ascending order of the PO term, ignoring case.
- The function names `start_test`, `calculate_wpm`, `calculate_accuracy` and `save_high_score` are system operations; they are written in the IT register and carry the IT terms in their parameters.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[REG]: ./artifact-registry.md
[DM-001]: ./use-cases/uc-001/dm.md
[a388508]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/a388508748c9a53f3406d8634714e2d0caba7220
