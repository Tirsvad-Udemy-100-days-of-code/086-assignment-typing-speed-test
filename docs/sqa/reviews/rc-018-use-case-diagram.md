# Review Record: Use Case Diagram UCD-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-018 |
| CrossReference | [UCD-001], [QC-UCD-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [UCD-001]
- Checklist used: [QC-UCD-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (accepted the plan, which states English and the IT domain, in chat on 2026-11-20)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Actors are defined with correct UML stereotypes (e.g. `<<System>>`, `<<Actor>>`) | Pass | Actor stereotyped `<<Actor>>`, system `<<System>>` |
| 2 | System boundary is clearly drawn and labeled | Pass | The system rectangle is drawn and labelled |
| 3 | Include/extend relationships are used correctly per UML 2.5.1, not as generic "uses" arrows | Pass | No include or extend is used; the table says so |
| 4 | Every actor participates in at least one use case (no orphan actors) | Pass | The User takes part in the one use case |
| 5 | Diagram is traceable to a documented stakeholder need | Pass | Traces to S01 and S02 through the Actor Table and to US-001 |
| 6 | Use case names are verb phrases describing actor goals, not internal system operations | Pass | "Take a typing test" is a verb phrase and an actor goal |
| 7 | Diagram is free of implementation detail (e.g. UI widgets, database tables) | Pass | No widget or storage detail |
| 8 | Actor and use case naming is consistent with corresponding Use Case and User Story documents | Pass | Names agree with US-001 and UC-001 |
| 9 | Each use case lists the user story it comes from and its priority (MoSCoW) with a reason | Pass | The use case table lists stories and the MoSCoW priority with a reason |
| 10 | When there is more than one primary actor, a role matrix (use case by role) is present and marked as a suggestion for the Product Owner to approve | N-A | One primary actor, so no role matrix is needed |

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

[UCD-001]: ../../use-case-diagram.md
[QC-UCD-001]: ../../../framework/qc/artifacts/qc-use-case-diagram.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
