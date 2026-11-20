"""@file test_typing_window.py
@brief Graphical test: types a text with one mistake and writes two screenshots.

Runs only in the Docker harness:
`bash scripts/run-gui-tests.sh python -m pytest -m gui`.
The clock is a fake, so the test never waits for real time.
"""

import tkinter

import pytest

from tests.fake_clock import FakeClock
from tests.gui.screenshot import take_screenshot
from typing_speed_test.constants import TEST_DURATION_SECONDS, TIMER_INTERVAL_MS
from typing_speed_test.infrastructure.built_in_texts import BUILT_IN_TEXTS
from typing_speed_test.infrastructure.composition_root import CompositionRoot

pytestmark = pytest.mark.gui

## @brief Characters typed before the screenshot in the middle of the test.
PARTIAL_LENGTH = 40

## @brief Seconds that passed before the screenshot in the middle of the test.
SECONDS_BEFORE_PARTIAL = 18

## @brief Index of the one wrong character in the typed text.
MISTAKE_INDEX = 12


def typed_with_one_mistake() -> str:
    sample = BUILT_IN_TEXTS[0]
    wrong = "#" if sample[MISTAKE_INDEX] != "#" else "%"
    return sample[:MISTAKE_INDEX] + wrong + sample[MISTAKE_INDEX + 1 :]


def find_widget(root: tkinter.Tk, kind: type[tkinter.Widget]) -> tkinter.Widget:
    return next(child for child in root.winfo_children() if isinstance(child, kind))


def type_into(root: tkinter.Tk, entry: tkinter.Entry, text: str) -> None:
    root.setvar(str(entry.cget("textvariable")), text)
    root.update()


def test_typing_with_a_mistake_and_finishing_write_screenshots() -> None:
    clock = FakeClock(now=1000.0)
    view = CompositionRoot().build(clock)
    root = view.open_window()
    try:
        entry = find_widget(root, tkinter.Entry)
        assert isinstance(entry, tkinter.Entry)
        text = typed_with_one_mistake()
        type_into(root, entry, text[:1])
        clock.advance(SECONDS_BEFORE_PARTIAL)
        type_into(root, entry, text[:PARTIAL_LENGTH])
        view.focus_input()
        middle_file = take_screenshot(root, "step-2-typing.png")
        assert str(entry.cget("state")) == tkinter.NORMAL
        clock.advance(TIMER_INTERVAL_MS / 1000)
        type_into(root, entry, text)
        finished_file = take_screenshot(root, "step-2-finished.png")
        assert str(entry.cget("state")) == tkinter.DISABLED
    finally:
        root.destroy()
    assert middle_file.is_file()
    assert finished_file.is_file()
    assert SECONDS_BEFORE_PARTIAL < TEST_DURATION_SECONDS
