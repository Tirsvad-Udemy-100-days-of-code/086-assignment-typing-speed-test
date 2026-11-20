# ADR-0003: GUI tests and screenshots in a Docker container

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0003 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Initial version<br>Accepted on Go in RC-013 | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The framework forbids testing or driving a graphical interface on the host desktop, because the test would take the user's mouse and keyboard (`framework/process/gui-testing.md`). The Product Owner needs a screenshot for each build step in the README and the wiki. The project must stay free of runtime dependencies, so a picture library is not wanted in the program. Options:

1. The host desktop. Forbidden by the framework.
2. Windows Sandbox. Isolated, but Windows only, and slower to script.
3. A Docker container with a virtual display (Xvfb) that runs the window test and takes the screenshot with ImageMagick (`import`) installed in the container image.
4. The same container, with a Python picture library installed in the project environment to grab the screen. It adds a dependency the program itself does not need.

## Decision

Graphical tests and screenshots run in a Linux Docker container under Xvfb, started by `scripts/run-gui-tests.sh`. Screenshots are taken with ImageMagick from the container image, called from the test with a list of arguments, so no dependency is added to the project. The test reports through an exit code and screenshot files written to `docs/screenshots/`. Unit and integration tests run on the host as usual.

## Consequences

**Positive:**

- The host desktop is never used, as the framework requires.
- The screenshots can be reproduced by anyone who has Docker.
- The project keeps zero runtime dependencies.

**Negative:**

- The first run builds the image, which takes minutes.
- Screenshots show the Linux look of Tkinter, not the Windows look; the README says so.
- Docker must be installed to refresh the screenshots.

## Affected Artifacts

- [BC-001] — objectives O5 and O6, and the risk about graphical tests.
- [PP-001] — the plan relies on the harness built in gateway 1.

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
