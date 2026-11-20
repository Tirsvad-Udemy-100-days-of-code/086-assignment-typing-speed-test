# Review Record: Domain Model DM-001 of UC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-020 |
| CrossReference | [DM-001], [QC-DM-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [DM-001]
- Checklist used: [QC-DM-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (accepted the plan, which states English and the IT domain, in chat on 2026-11-20)
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Uses ubiquitous/business language throughout; no technical or implementation jargon (e.g. no "table", "class", "pointer") | Pass | Everyday words only; no table, class or pointer |
| 2 | Multiplicities on associations are correct and complete (e.g. `1..*`, `0..1`) | Pass | Multiplicities on all three associations |
| 3 | No operation/method signatures shown — attributes and associations only | Pass | No operation is shown |
| 4 | Associations are named with an unambiguous reading direction | Pass | Each association has a name and a reading direction |
| 5 | Generalization/specialization used correctly, reflecting true "is-a" relationships, not misused for code reuse | N-A | No generalization is used |
| 6 | Every concept traces to a noun phrase found in the use cases or glossary | Pass | Each concept has a source noun phrase in the use case |
| 7 | Attributes are simple domain data (no foreign-key-like references or object pointers modeled as attributes) | Pass | Attributes are simple data |
| 8 | The Purpose names the concerns (`CN-NNN`) the Domain Model answers and the stakeholders it serves, so its viewpoint is stated | Pass | The Purpose names CN-001 and CN-009 and S01 and S02 |
| 9 | No technical solution names: only conceptual classes of the Product Owner's world, never a file, an environment variable, a setting source, a database, a table, an API, a service, a cache or any other mechanism | Pass | No file, setting, database or mechanism is named |
| 10 | No empty concept: every concept has at least one attribute and at least one association | Pass | Every concept has an attribute and an association |
| 11 | A Domain Model written for one use case reuses the concepts, attributes, associations and names of the project Domain Model, and its additions and changes are added to the project Domain Model | Pass | No project-level Domain Model exists yet, so there is nothing to reuse; the model is added to it in this gateway |
| 12 | The software is a black box and a normal person can read the model: no concept or attribute exists only because the software exists (a run, command, option, mode, step, exit code, log, session, question, prompt, summary or other screen or tool element); no attribute is computed from other concepts, and none is an identifier or a storage type; every concept in the Concept Table has a one-sentence definition in everyday words with no IT term | Pass | Every concept has a one-sentence definition in everyday words; the measures that are computed (words per minute, accuracy) are not attributes |

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

[DM-001]: ../../use-cases/uc-001/dm.md
[QC-DM-001]: ../../../framework/qc/artifacts/qc-domain-model.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
