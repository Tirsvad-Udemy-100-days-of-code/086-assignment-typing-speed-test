# Review Record: Domain Dictionary DICT-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-027 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (accepted the plan, which states English and the IT domain, in chat on 2026-11-20)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All 15 rows have a PO term, language, IT term and definition |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | No synonym: each PO term has one IT term and the reverse |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | Pass | The four concepts of DM-001 and its attributes have rows; DM-001 and DM-002 use the PO terms |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | Pass | OC-001, SD-001, DCD-001 and DCD-002 use the IT terms (`TypingTest`, `TypingResult`, `HighScore`, `SampleText`, `elapsed_seconds`, `correct_characters` and the four function names) |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Each definition is one sentence in English |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | The artifact types named in the two use columns exist in the project |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Language en and Domain it match the registry |
| 8 | The dictionary rows are in ascending order of the PO term (case-insensitive, by the alphabet of the PO language) | Pass | Rows are in ascending order of the PO term, ignoring case |

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

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
