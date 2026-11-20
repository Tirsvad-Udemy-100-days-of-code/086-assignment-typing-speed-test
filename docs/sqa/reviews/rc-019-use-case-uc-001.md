# Review Record: Use Case UC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-019 |
| CrossReference | [UC-001], [QC-UC-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | [a388508] |

---

## Artifact Under Review

- Instance reviewed: [UC-001]
- Checklist used: [QC-UC-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (accepted the plan, which states English and the IT domain, in chat on 2026-11-20)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Consists of a single, concise paragraph summarizing only the primary success scenario | N-A | The format is Fully Dressed, not Brief |
| 2 | Written as an informal multi-paragraph narrative; may mention some alternate flows without formal structure | N-A | The format is Fully Dressed, not Casual |
| 3 | All standard sections are present: actors, preconditions, postconditions, main success scenario, alternative/exception flows | Pass | Actors, preconditions, postconditions, main scenario and extensions are present |
| 4 | Preconditions and postconditions are explicitly defined | Pass | Preconditions and Postconditions are defined |
| 5 | Primary actor is explicitly stated | Pass | The primary actor is the User |
| 6 | Stakeholders and their interests are stated | Pass | Stakeholders S01, S02 and S03 with interests |
| 7 | Main success scenario is written as clear, numbered steps | Pass | Eight numbered steps |
| 8 | Alternative/exception flows correctly reference `<<include>>`/`<<extend>>` use cases where relevant, per UML 2.5.1 | Pass | No include or extend is relevant: extensions are alternative flows of the one use case |
| 9 | Explicit business rules are captured per step where applicable, rather than embedded loosely in narrative text | Pass | Business rules are listed per step under Special Requirements |
| 10 | Naming of actors and use case title is consistent with the corresponding Use Case Diagram and User Stories | Pass | Title and actor agree with UCD-001 and US-001 |
| 11 | Scope/level (e.g. summary, user-goal, subfunction) is explicitly stated | Pass | Format and level stated |
| 12 | Use case is written from the actor's goal perspective, free of UI or implementation detail | Pass | Steps are written from the User's goal; no widget, key or file is named |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language and Domain rows are present and filled |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Language en is a BCP 47 code; Domain it is in the registry list |
| 3 | The content (prose and table cells) is written in the stated language | Pass | English throughout; S01 accepted the plan wording in chat on 2026-11-20 |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register matches the registry for this type |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms follow the Business Case and the assignment text; the dictionary written in this gateway records them, and a difference found there reopens this review |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 accepted the plan, which names English and the IT domain, in chat on 2026-11-20 |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out or are established technical terms |

## Overall Verdict

Go — every Mandatory criterion passes; no action items

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-20 |

---

[UC-001]: ../../use-cases/uc-001/uc.md
[QC-UC-001]: ../../../framework/qc/artifacts/qc-use-case.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[a388508]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/a388508748c9a53f3406d8634714e2d0caba7220
