"""@file test_typing_view_model.py
@brief Tests of TypingViewModel, with no window.
"""

from typing_speed_test.application.test_session import TestSession
from typing_speed_test.application.use_cases.start_test import StartTest
from typing_speed_test.constants import TEST_DURATION_SECONDS
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


def make_view_model() -> TypingViewModel:
    use_case = StartTest(FakeSampleTextSource(), TestSession())
    return TypingViewModel(start_test_use_case=use_case)


def test_texts_are_empty_before_a_test_starts() -> None:
    view_model = make_view_model()
    assert view_model.sample_text() == ""
    assert view_model.typed_text() == ""
    assert view_model.status_text() == ""


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
