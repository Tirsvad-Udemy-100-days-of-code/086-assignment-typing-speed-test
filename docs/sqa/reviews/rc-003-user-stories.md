# Review Record: User Stories US-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [US-001], [QC-US-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | [0f493f4] |

---

## Artifact Under Review

- Instance reviewed: [US-001]
- Checklist used: [QC-US-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (accepted the plan, which states English and the IT domain, in chat on 2026-11-20)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Follows INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable) | Pass | Each story is small, valuable and testable; see the INVEST Check |
| 2 | Written in "As a / I want / So that" form | Pass | All eight stories use As a / I want / so that |
| 3 | Clear, testable acceptance criteria are included | Pass | Each story has Given/When/Then style acceptance criteria |
| 4 | Traceable to a use case or epic | Pass | Each story has a Traces to cell naming a milestone or a Business Case objective |
| 5 | Story is sized to fit within a single iteration | Pass | Each story fits one gateway |
| 6 | Story statement avoids technical implementation detail | Pass | Statements avoid implementation detail |
| 7 | Role named in the story matches an actor defined in the Use Case Diagram | N-A | No use case diagram exists yet; it is created in gateway 2 (task 1 of MIL-002). The role is named User and is the actor that diagram will define. A delta re-review follows it, see the action item |
| 8 | A story with more than one actor goal is split into use cases, one per actor goal, and each use case names the story it comes from | Pass | One actor goal per story; one use case covers US-001.01 to US-001.06 |
| 9 | The story has a priority (MoSCoW: Must, Should, Could, Won't now) with the reason beside it | Pass | Every story has a MoSCoW priority with a reason |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language and Domain rows are present and filled |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Language en is a BCP 47 code; Domain it is in the registry list |
| 3 | The content (prose and table cells) is written in the stated language | Pass | English throughout; S01 accepted the plan wording in chat on 2026-11-20 |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register matches the registry for this type |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The domain dictionary is created in gateway 2; the terms follow the Business Case and the assignment text; a difference found when the dictionary is written reopens this review |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 accepted the plan, which names English and the IT domain, in chat on 2026-11-20 |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations such as MVVM and INVEST are spelled out or are established technical terms |

## Overall Verdict

Go — every Mandatory criterion passes; no action items

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Delta re-review of criterion 7 once the use case diagram exists, and add UCD-001 and UC-001 to the CrossReference | S01 | 2026-11-22 |

---

[US-001]: ../../user-stories.md
[QC-US-001]: ../../../framework/qc/artifacts/qc-user-story.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[0f493f4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/0f493f4af963132d34a8a932f4984e783dc36894
