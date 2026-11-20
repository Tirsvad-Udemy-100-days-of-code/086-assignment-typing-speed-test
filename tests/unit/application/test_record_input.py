"""@file test_record_input.py
@brief Tests of the RecordInput use case, with a fake clock and no sleep.
"""

import pytest

from tests.fake_clock import FakeClock
from typing_speed_test.application.errors import NoActiveTestError
from typing_speed_test.application.test_session import TestSession
from typing_speed_test.application.use_cases.record_input import RecordInput
from typing_speed_test.constants import TEST_DURATION_SECONDS
from typing_speed_test.domain.enums import TestState
from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.domain.typing_test import TypingTest

TEXT = SampleText("abc")


def make_use_case(clock: FakeClock) -> tuple[RecordInput, TestSession]:
    session = TestSession()
    session.replace(TypingTest(TEXT, TEST_DURATION_SECONDS))
    return RecordInput(session, clock), session


def test_type_text_without_a_test_is_refused() -> None:
    use_case = RecordInput(TestSession(), FakeClock())
    with pytest.raises(NoActiveTestError):
        use_case.type_text("a")


def test_check_time_without_a_test_is_refused() -> None:
    use_case = RecordInput(TestSession(), FakeClock())
    with pytest.raises(NoActiveTestError):
        use_case.check_time()


def test_type_text_starts_the_clock_at_the_first_character() -> None:
    clock = FakeClock(now=10.0)
    use_case, _ = make_use_case(clock)
    test = use_case.type_text("a")
    assert test.started_at == 10.0
    assert test.state() is TestState.RUNNING


def test_type_text_keeps_the_changed_test_in_the_session() -> None:
    use_case, session = make_use_case(FakeClock())
    test = use_case.type_text("ab")
    assert session.current_test() is test


def test_type_text_finishes_when_the_text_is_complete() -> None:
    use_case, _ = make_use_case(FakeClock())
    assert use_case.type_text("abc").state() is TestState.FINISHED


def test_type_text_after_the_time_is_up_is_refused() -> None:
    clock = FakeClock()
    use_case, _ = make_use_case(clock)
    use_case.type_text("a")
    clock.advance(TEST_DURATION_SECONDS)
    test = use_case.type_text("ab")
    assert test.typed_text == "a"
    assert test.state() is TestState.FINISHED


def test_type_text_after_finish_changes_nothing() -> None:
    use_case, _ = make_use_case(FakeClock())
    finished = use_case.type_text("abc")
    assert use_case.type_text("") is finished


def test_check_time_finishes_a_running_test_when_time_is_up() -> None:
    clock = FakeClock()
    use_case, session = make_use_case(clock)
    use_case.type_text("a")
    clock.advance(TEST_DURATION_SECONDS)
    assert use_case.check_time().state() is TestState.FINISHED
    assert session.current_test().state() is TestState.FINISHED


def test_check_time_keeps_a_running_test_before_time_is_up() -> None:
    clock = FakeClock()
    use_case, _ = make_use_case(clock)
    use_case.type_text("a")
    clock.advance(TEST_DURATION_SECONDS - 1)
    assert use_case.check_time().state() is TestState.RUNNING
