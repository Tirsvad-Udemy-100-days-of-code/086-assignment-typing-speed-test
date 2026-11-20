# Review Record: Shell scripts of gateway 1

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [MIL-001], [QC-SH-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-001]
- Checklist used: [QC-SH-001]
- Scope: full review of `scripts/check.sh`, `scripts/run-gui-tests.sh` and `docker/gui/entrypoint.sh`
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Starts with `#!/usr/bin/env bash` and `set -euo pipefail` (or a comment explains the exception) | Pass | All three scripts start with `#!/usr/bin/env bash` and `set -euo pipefail` |
| 2 | Every expansion is quoted; lists are arrays; tests use `[[ ]]` and `$(...)` | Pass | Expansions quoted; `shellcheck` finds nothing |
| 3 | Names follow the conventions: `kebab-case.sh` files, `snake_case` functions and variables, `UPPER_SNAKE` constants and environment variables | Pass | `check.sh`, `run-gui-tests.sh`, `entrypoint.sh` are kebab-case; variables lower case |
| 4 | Passes `shellcheck` and `bash -n` with no unexplained `disable` comments | Pass | shellcheck 0.11.0 and `bash -n` pass; no `disable` comment except the source hint in `entrypoint.sh` |
| 5 | Errors go to standard error with an `error:` message and a non-zero exit code; bad or missing arguments print a usage line | Pass | Failure paths print `error:` to standard error and exit 2 (missing `.venv`, missing opengrep); the scripts take no required argument |
| 6 | Temporary files use `mktemp` with a `trap ... EXIT` cleanup; no fixed `/tmp` names | N-A | No temporary file is used |
| 7 | No secret is written in the script, echoed, or put on a command line; secrets come from the environment or a gitignored file | Pass | No secret is read, written or echoed |
| 8 | A script that changes state outside its own directory defaults to a dry run or needs an explicit flag, and says so in its header | Pass | `run-gui-tests.sh` writes only to `docs/screenshots/` and builds a local image; the header says so. `check.sh` changes nothing |
| 9 | A header comment states purpose, usage, options, environment variables and exit codes | Pass | Each header states purpose, usage, environment, exit code and needs |
| 10 | The script implements a task or design it cites; deviations are recorded | Pass | They implement MIL-001 tasks 8 and 9 |
| 11 | Behaviour is tested for success, failure and any disabled or bypass path | Pass | Recorded run: success path `scripts/check.sh` exits 0 with the opengrep scan; failure path with an invalid OPENGREP path and no opengrep on the path prints `error: opengrep not found` and exits 2; `run-gui-tests.sh` produced `docs/screenshots/harness-smoke.png` |
| 12 | Formatted with `shfmt` (or the project's formatter) | Pass | `shfmt` v3.14.1 reports no difference |
| 13 | Safe to re-run: a second run does not duplicate or corrupt what the first did | Pass | A second run repeats the same checks and rebuilds the same image |
| 14 | Bash version and external tools it needs are stated; GNU-only options are named | Pass | Bash, Docker and the `.venv` are named under Needs |
| 15 | A command sequence, constant, path or message used more than once is defined once (a function, a variable or a sourced helper); a helper is shared between scripts only where it expresses the same knowledge | Pass | No command sequence is repeated between the scripts |

## Overall Verdict

Go — every Mandatory criterion passes; no action items

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-20 |

---

[MIL-001]: ../../milestones/mil-001-project-setup.md
[QC-SH-001]: ../../../framework/qc/code/qc-programming-shell.md
