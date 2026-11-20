"""@file test_typing_view_model.py
@brief Tests of TypingViewModel, with no window and a fake clock.
"""

from tests.fake_clock import FakeClock
from typing_speed_test.application.test_session import TestSession
from typing_speed_test.application.use_cases.record_input import RecordInput
from typing_speed_test.application.use_cases.start_test import StartTest
from typing_speed_test.constants import (
    STATUS_FINISHED_TEXT,
    TEST_DURATION_SECONDS,
)
from typing_speed_test.domain.enums import CharacterMark
from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.presentation.features.typing_test.typing_view_model import (
    TypingViewModel,
)

TEXT = SampleText("hello world")


class FakeSampleTextSource:
    def all_texts(self) -> tuple[SampleText, ...]:
        return (TEXT,)

    def random_text(self) -> SampleText:
        return TEXT


def make_view_model(clock: FakeClock | None = None) -> TypingViewModel:
    used_clock = clock if clock is not None else FakeClock()
    session = TestSession()
    return TypingViewModel(
        start_test_use_case=StartTest(FakeSampleTextSource(), session),
        record_input_use_case=RecordInput(session, used_clock),
        clock=used_clock,
    )


def test_texts_are_empty_before_a_test_starts() -> None:
    view_model = make_view_model()
    assert view_model.sample_text() == ""
    assert view_model.typed_text() == ""
    assert view_model.status_text() == ""
    assert view_model.marks() == ()
    assert view_model.remaining_seconds() == 0
    assert not view_model.is_locked()


def test_start_test_exposes_the_sample_text() -> None:
    view_model = make_view_model()
    view_model.start_test()
    assert view_model.sample_text() == "hello world"


def test_start_test_leaves_the_input_empty() -> None:
    view_model = make_view_model()
    view_model.start_test()
    assert view_model.typed_text() == ""


def test_status_text_names_the_length_and_the_hint() -> None:
    view_model = make_view_model()
    view_model.start_test()
    assert view_model.status_text() == (
        f"{TEST_DURATION_SECONDS} s - the time starts when you type"
    )


def test_type_text_exposes_the_marks() -> None:
    view_model = make_view_model()
    view_model.start_test()
    view_model.type_text("hx")
    assert view_model.typed_text() == "hx"
    assert view_model.marks()[:3] == (
        CharacterMark.CORRECT,
        CharacterMark.WRONG,
        CharacterMark.PENDING,
    )


def test_status_text_counts_down_while_running() -> None:
    clock = FakeClock()
    view_model = make_view_model(clock)
    view_model.start_test()
    view_model.type_text("h")
    clock.advance(20)
    view_model.check_time()
    assert view_model.status_text() == "40 s left"
    assert view_model.remaining_seconds() == 40


def test_status_text_rounds_the_countdown_up() -> None:
    clock = FakeClock()
    view_model = make_view_model(clock)
    view_model.start_test()
    view_model.type_text("h")
    clock.advance(20.5)
    assert view_model.status_text() == "40 s left"


def test_input_is_not_locked_while_running() -> None:
    view_model = make_view_model()
    view_model.start_test()
    view_model.type_text("h")
    assert not view_model.is_locked()


def test_input_is_locked_when_the_text_is_complete() -> None:
    view_model = make_view_model()
    view_model.start_test()
    view_model.type_text("hello world")
    assert view_model.is_locked()
    assert view_model.status_text() == STATUS_FINISHED_TEXT


def test_input_is_locked_when_the_time_is_up() -> None:
    clock = FakeClock()
    view_model = make_view_model(clock)
    view_model.start_test()
    view_model.type_text("h")
    clock.advance(TEST_DURATION_SECONDS)
    view_model.check_time()
    assert view_model.is_locked()
    assert view_model.remaining_seconds() == 0
