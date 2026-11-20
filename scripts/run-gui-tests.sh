#!/usr/bin/env bash
# Builds the Docker image and runs a command under a virtual display in a Linux
# container. Graphical tests and screenshots run only here, never on the host desktop.
#
# Usage:   bash scripts/run-gui-tests.sh [command [args...]]
#          default command: python docker/gui/capture_smoke.py
#          graphical tests:  bash scripts/run-gui-tests.sh python -m pytest -m gui
# Output:  screenshots in docs/screenshots/
# Exit:    the exit code of the command in the container
# Needs:   bash, Docker
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."
root="$(pwd -W 2>/dev/null || pwd)"
mkdir -p docs/screenshots
if [[ $# -eq 0 ]]; then
  set -- python docker/gui/capture_smoke.py
fi

docker build --quiet -t typing-speed-test-gui -f docker/gui/Dockerfile docker/gui
MSYS_NO_PATHCONV=1 docker run --rm --init \
  -v "$root:/src:ro" \
  -v "$root/docs/screenshots:/results" \
  -e SCREENSHOT_DIR=/results \
  typing-speed-test-gui bash /src/docker/gui/entrypoint.sh "$@"
