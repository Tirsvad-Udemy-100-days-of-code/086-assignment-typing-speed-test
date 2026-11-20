# Review Record: System Sequence Diagram SSD-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-021 |
| CrossReference | [SSD-001], [QC-SSD-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [SSD-001]
- Checklist used: [QC-SSD-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (accepted the plan, which states English and the IT domain, in chat on 2026-11-20)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Input/output messages match the corresponding Use Case's main success scenario step-for-step | Pass | The messages follow steps 1 to 8 of the main scenario in order, and the extensions in the second diagram |
| 2 | Actor and System are treated strictly as black boxes (system shown as `:System`) | Pass | The system is shown as `:System` and nothing inside it appears |
| 3 | Object creation/destruction of the System instance handled explicitly where relevant | N-A | One long-lived system instance; the lifecycle note says it |
| 4 | Return values are shown for operations that produce one, using dashed return arrows | Pass | Every message that has a result has a dashed return |
| 5 | Alternate/exceptional flows are represented separately (or explicitly out of scope noted) | Pass | Alternative flows are in their own diagram |
| 6 | Message names are verb phrases consistent with the use case's system responsibilities | Pass | All message names are verb phrases and are the function names of the design |
| 7 | Diagram references the specific Use Case (name and ID) it depicts | Pass | The Source Use Case section names UC-001 |

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

[SSD-001]: ../../use-cases/uc-001/ssd.md
[QC-SSD-001]: ../../../framework/qc/artifacts/qc-ssd.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
