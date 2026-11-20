#!/usr/bin/env bash
# Runs inside the container: copies the read-only project to /app, installs it into
# a fresh venv and runs the given command under a virtual display.
#
# Usage:   entrypoint.sh <command> [args...]
# Env:     SCREENSHOT_DIR  folder the command writes screenshots to (mounted from the host)
# Exit:    the exit code of the command
set -euo pipefail

mkdir -p /app
tar -C /src --exclude=.venv --exclude=.git --exclude=build --exclude=framework \
  --exclude=docs/ai-prompts -cf - . | tar -C /app -xf -
cd /app
python -m venv /venv
# shellcheck disable=SC1091
source /venv/bin/activate
python -m pip install --upgrade pip --quiet
python -m pip install -e ".[dev]" --quiet
xvfb-run -a -s "-screen 0 1280x800x24" "$@"
