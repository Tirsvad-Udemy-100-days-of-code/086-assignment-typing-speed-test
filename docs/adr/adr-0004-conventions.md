# ADR-0004: Documentation conventions and skipped artifact types

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0004 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-014 | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The framework offers many artifact types. A small learning project does not need all of them, and a skipped type needs a recorded reason. The Product Owner also asked for Doxygen comments in the source, a `Doxyfile`, and a wiki in English, Danish and Bahasa Malaysia with a screenshot and a "what we gained" section for each step. Options for the artifacts: write every type, or write the types that carry a decision for this project and skip the rest with a reason.

## Decision

These artifact types are skipped, each for the reason given: KPI, Business Model Canvas and BPMN, because the success criteria of the Business Case are measurable as they stand and the project has no commercial model or business process; Risk Analysis, because the idea is set by the course assignment and no belief needs a test before building; Governance, because one stakeholder decides and reviews and the framework's review process applies unchanged; Entity Relationship Diagram, because the high scores are one small JSON file and not a database; Architecture Description and Test Plan, because the decision records, the design class diagram and the Go/No-Go criteria of each milestone hold the same content for a project of this size; and a role matrix, because there is one actor and one use case. Source comments follow Doxygen: a module docstring starting with `@file` and `@brief`, and for each public class, function and constant a docstring or `##` comment with `@brief`, `@param` and `@return`. The `Doxyfile` fails the build on any warning. The wiki is kept in `docs/wiki/`, one page per step in each of English, Danish (`-da`) and Bahasa Malaysia (`-ms`), with the sidebar and language line the framework defines.

## Consequences

**Positive:**

- Review effort goes to the artifacts that change the code.
- Every skipped type has a reason a reader can challenge.
- The comment style produces a browsable manual with no extra tool in the runtime.

**Negative:**

- If the project grows (a database, more actors), the skipped types must be reconsidered and added.
- Three wiki languages triple the writing and review effort of every step page.

## Affected Artifacts

- [BC-001] — scope and objectives O3 and O5.
- [PP-001] — the plan relies on the skipped types not being scheduled.

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
