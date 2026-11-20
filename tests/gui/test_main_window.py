"""@file test_main_window.py
@brief Graphical test: opens the main window and writes two screenshots.

Runs only in the Docker harness:
`bash scripts/run-gui-tests.sh python -m pytest -m gui`.
"""

import pytest

from tests.gui.screenshot import take_screenshot
from typing_speed_test.infrastructure.composition_root import CompositionRoot

pytestmark = pytest.mark.gui


def test_window_opens_and_screenshots_are_written() -> None:
    view = CompositionRoot().build()
    root = view.open_window()
    try:
        window_file = take_screenshot(root, "step-1-window.png")
        view.focus_input()
        text_file = take_screenshot(root, "step-1-text.png")
    finally:
        root.destroy()
    assert window_file.is_file()
    assert text_file.is_file()
