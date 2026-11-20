#!/usr/bin/env bash
# Local quality gate. Run it before every push.
#
# Usage:   bash scripts/check.sh
# Runs:    pytest with coverage (graphical tests are skipped here), ruff lint and
#          format check, mypy --strict, import-linter (when the project defines
#          contracts), and the opengrep scan with the rules in
#          config/opengrep-python.yml.
# Env:     OPENGREP   path of the opengrep program
#                     (default: ~/.opengrep/cli/latest/opengrep.exe, else `opengrep`)
# Exit:    0 every step passed; non-zero at the first step that failed
# Needs:   bash, a local .venv with `python -m pip install -e ".[dev]"` done
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if [[ -x .venv/Scripts/python.exe ]]; then
  py=".venv/Scripts/python.exe"
elif [[ -x .venv/bin/python ]]; then
  py=".venv/bin/python"
else
  echo "error: no .venv found; see README, section Setup" >&2
  exit 2
fi

opengrep="${OPENGREP:-$HOME/.opengrep/cli/latest/opengrep.exe}"
if [[ ! -x "$opengrep" ]]; then
  opengrep="$(command -v opengrep || true)"
fi
if [[ -z "$opengrep" ]]; then
  echo "error: opengrep not found; set OPENGREP to its path" >&2
  exit 2
fi

step() {
  echo
  echo "== $*"
}

step "pytest"
"$py" -m pytest -m "not gui" --cov --cov-report=term

step "coverage of domain and application (at least 85%)"
"$py" -m coverage report --include="src/typing_speed_test/domain/*,src/typing_speed_test/application/*" --fail-under=85

step "ruff lint"
"$py" -m ruff check .

step "ruff format"
"$py" -m ruff format --check .

step "mypy"
"$py" -m mypy

if grep -q '^\[tool.importlinter\]' pyproject.toml; then
  step "import-linter"
  "$py" -c "import sys; from importlinter.cli import lint_imports_command; sys.argv = ['lint-imports']; lint_imports_command()"
fi

step "opengrep"
"$opengrep" scan --config config/opengrep-python.yml --disable-version-check --error --quiet src tests

echo
echo "All checks passed."
