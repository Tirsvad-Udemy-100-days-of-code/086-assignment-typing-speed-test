# Review Record: YAML files of gateway 1

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-017 |
| CrossReference | [MIL-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | Stand-in for S01 | Review record; mode autonomous, not independent | [0f493f4] |

---

## Artifact Under Review

- Instance reviewed: [MIL-001]
- Checklist used: [QC-YML-001]
- Scope: full review of `config/opengrep-python.yml` and `.yamllint.yml`
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is a stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | yamllint 1.32.0 (cytopia/yamllint image) parses both files and finds no duplicate keys |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | 2-space indentation, LF, final newline, no trailing spaces; yamllint passes |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `.yamllint.yml` is committed next to the code; no `disable` comment |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | No ambiguous scalar; strings are plain text without `: ` or ` #` |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | No language-specific tags |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret; the rule `python-no-hardcoded-secret` only detects secrets |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | No embedded program text |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | The repeated `languages: [python]` key is the rule schema of the tool, not a duplicated block that an anchor could replace |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors or aliases |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | N-A | opengrep validates the rules on every scan |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | The header comment says what the file is for and which tool reads it |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | Keys follow opengrep's own names; kebab-case ids |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | N-A | No multi-line scalar needs a chomping indicator |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `opengrep-python.yml`, lower case kebab-case |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | `scripts/check.sh` runs the scan on every push |

## Overall Verdict

Go — every Mandatory criterion passes; no action items

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-20 |

---

[MIL-001]: ../../milestones/mil-001-project-setup.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[0f493f4]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/086-assignment-typing-speed-test/commit/0f493f4af963132d34a8a932f4984e783dc36894
