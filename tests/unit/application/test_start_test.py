"""@file test_start_test.py
@brief Tests of the StartTest use case, with a fake text source.
"""

from typing_speed_test.application.test_session import TestSession
from typing_speed_test.application.use_cases.start_test import StartTest
from typing_speed_test.constants import TEST_DURATION_SECONDS
from typing_speed_test.domain.enums import TestState
from typing_speed_test.domain.sample_text import SampleText

RANDOM = SampleText("random text")
GIVEN = SampleText("given text")


class FakeSampleTextSource:
    def all_texts(self) -> tuple[SampleText, ...]:
        return (RANDOM,)

    def random_text(self) -> SampleText:
        return RANDOM


def test_start_test_without_text_takes_the_random_one() -> None:
    test = StartTest(FakeSampleTextSource(), TestSession()).start_test()
    assert test.sample_text == RANDOM


def test_start_test_uses_the_given_text() -> None:
    test = StartTest(FakeSampleTextSource(), TestSession()).start_test(GIVEN)
    assert test.sample_text == GIVEN


def test_start_test_returns_a_ready_test() -> None:
    test = StartTest(FakeSampleTextSource(), TestSession()).start_test()
    assert test.state() is TestState.READY
    assert test.duration_seconds == TEST_DURATION_SECONDS
    assert test.typed_text == ""
    assert test.started_at is None


def test_start_test_makes_the_test_current() -> None:
    session = TestSession()
    test = StartTest(FakeSampleTextSource(), session).start_test()
    assert session.current_test() is test


def test_start_test_drops_the_earlier_test() -> None:
    session = TestSession()
    use_case = StartTest(FakeSampleTextSource(), session)
    use_case.start_test(GIVEN)
    second = use_case.start_test()
    assert session.current_test() is second
