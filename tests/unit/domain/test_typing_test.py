"""@file test_typing_test.py
@brief Tests of TypingTest.
"""

from typing_speed_test.domain.enums import TestState
from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.domain.typing_test import TypingTest

SAMPLE = SampleText("abc")


def test_state_is_ready_without_times() -> None:
    assert TypingTest(SAMPLE, 60).state() is TestState.READY


def test_state_is_running_with_start_time() -> None:
    assert TypingTest(SAMPLE, 60, "a", started_at=1.0).state() is TestState.RUNNING


def test_state_is_finished_with_end_time() -> None:
    test = TypingTest(SAMPLE, 60, "abc", started_at=1.0, finished_at=5.0)
    assert test.state() is TestState.FINISHED


def test_new_test_has_empty_typed_text() -> None:
    assert TypingTest(SAMPLE, 60).typed_text == ""
