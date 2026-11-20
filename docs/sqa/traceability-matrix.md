# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [US-001], [DM-002], [DCD-002] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted by the stand-in; the type has no checklist | pending |

---

## Purpose

Tracks backward and forward links between the artifact instances of the Typing Speed Test Desktop App, so that the traceability criterion of [BC-001] can be measured. A row is added or updated whenever an artifact is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | none | [SA-001], [US-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [US-001], [UC-001] | [RC-002] |
| [US-001] | US | en | it | [BC-001], [SA-001] | [UCD-001], [UC-001], [MIL-003] to [MIL-006] | [RC-028] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001] to [MIL-006] | [RC-004] |
| [MIL-001] to [MIL-006] | MIL | en | it | [PP-001], [US-001] | tasks as issues #1 to #54 | [RC-005] to [RC-010] |
| [ADR-0001] to [ADR-0004] | ADR | - | - | [BC-001] | source code, [DCD-002] | [RC-011] to [RC-014] |
| [UCD-001] | UCD | en | it | [US-001] | [UC-001] | [RC-018] |
| [UC-001] | UC | en | it | [UCD-001], [US-001] | [DM-001], [SSD-001] | [RC-019] |
| [DM-001] | DM | en | it | [UC-001] | [DM-002], [DICT-001], [SSD-001] | [RC-020] |
| [DICT-001] | DICT | en | it | [BC-001], [DM-001] | [OC-001], [SD-001], [DCD-001] | [RC-027] |
| [SSD-001] | SSD | en | it | [UC-001], [DM-001] | [OC-001] | [RC-021] |
| [OC-001] | OC | en | it | [SSD-001], [DM-001], [DICT-001] | [SD-001] | [RC-022] |
| [SD-001] | SD | en | it | [OC-001], [DICT-001] | [DCD-001] | [RC-023] |
| [DCD-001] | DCD | - | - | [DM-001], [SD-001] | [DCD-002], source code | [RC-024] |
| [DM-002] | DM | en | it | [DM-001] | [DCD-002] | [RC-025] |
| [DCD-002] | DCD | - | - | [DM-002], [DCD-001] | source code of milestones 3 to 6 | [RC-026] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [DM-001], [OC-001], [SD-001], [DCD-001] | [ADR-0001] | none yet; unit tests in milestones 3 to 6 | Covered |
| CN-002 | [PP-001], [MIL-001] to [MIL-006] | [ADR-0004] | none | Covered |
| CN-003 | [MIL-003] to [MIL-006] (wiki tasks) | none | none | Covered |
| CN-004 | [SD-001], [DCD-001], [DICT-001] | [ADR-0004] | none | Covered |
| CN-005 | [MIL-001], [MIL-006] (README tasks) | none | none | Covered |
| CN-006 | [MIL-003] to [MIL-006] (screenshot tasks) | [ADR-0003] | none | Covered |
| CN-007 | [MIL-001] (repository description and topics) | none | none | Covered |
| CN-008 | [DCD-001] | [ADR-0001] | none | Covered |
| CN-009 | [SD-001], [DCD-001] | [ADR-0002] | none yet; fake clock tests in milestone 4 | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | none | none found | [RC-027] | Closed | - |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[US-001]: ../user-stories.md
[PP-001]: ../project-plan.md
[UCD-001]: ../use-case-diagram.md
[UC-001]: ../use-cases/uc-001/uc.md
[DM-001]: ../use-cases/uc-001/dm.md
[SSD-001]: ../use-cases/uc-001/ssd.md
[OC-001]: ../use-cases/uc-001/oc.md
[SD-001]: ../use-cases/uc-001/sd.md
[DCD-001]: ../use-cases/uc-001/dcd.md
[DM-002]: ../domain-model.md
[DCD-002]: ../dcd.md
[DICT-001]: ../dictionary.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-003]: ../milestones/mil-003-step-1-window-and-text.md
[MIL-006]: ../milestones/mil-006-step-4-trainer.md
[ADR-0001]: ../adr/adr-0001-technology.md
[ADR-0002]: ../adr/adr-0002-architecture.md
[ADR-0003]: ../adr/adr-0003-gui-testing.md
[ADR-0004]: ../adr/adr-0004-conventions.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-user-stories.md
[RC-004]: ./reviews/rc-004-project-plan.md
[RC-005]: ./reviews/rc-005-mil-001-project-setup.md
[RC-006]: ./reviews/rc-006-mil-002-design.md
[RC-007]: ./reviews/rc-007-mil-003-step-1-window-and-text.md
[RC-008]: ./reviews/rc-008-mil-004-step-2-timer-and-typing.md
[RC-009]: ./reviews/rc-009-mil-005-step-3-result.md
[RC-010]: ./reviews/rc-010-mil-006-step-4-trainer.md
[RC-011]: ./reviews/rc-011-adr-0001-technology.md
[RC-012]: ./reviews/rc-012-adr-0002-architecture.md
[RC-013]: ./reviews/rc-013-adr-0003-gui-testing.md
[RC-014]: ./reviews/rc-014-adr-0004-conventions.md
[RC-015]: ./reviews/rc-015-mil-001-python-code.md
[RC-016]: ./reviews/rc-016-mil-001-shell-scripts.md
[RC-017]: ./reviews/rc-017-mil-001-yaml.md
[RC-018]: ./reviews/rc-018-use-case-diagram.md
[RC-019]: ./reviews/rc-019-use-case-uc-001.md
[RC-020]: ./reviews/rc-020-domain-model-uc-001.md
[RC-021]: ./reviews/rc-021-ssd-uc-001.md
[RC-022]: ./reviews/rc-022-oc-uc-001.md
[RC-023]: ./reviews/rc-023-sd-uc-001.md
[RC-024]: ./reviews/rc-024-dcd-uc-001.md
[RC-025]: ./reviews/rc-025-domain-model-project.md
[RC-026]: ./reviews/rc-026-dcd-project.md
[RC-027]: ./reviews/rc-027-dictionary.md
[RC-028]: ./reviews/rc-028-user-stories-delta.md
