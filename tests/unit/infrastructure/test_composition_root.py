"""@file test_composition_root.py
@brief Test that the composition root builds without opening a window.
"""

from tests.fake_clock import FakeClock
from typing_speed_test.infrastructure.composition_root import CompositionRoot
from typing_speed_test.presentation.features.typing_test.typing_view import (
    TypingView,
)


def test_build_gives_a_view() -> None:
    assert isinstance(CompositionRoot().build(), TypingView)


def test_build_accepts_a_fake_clock() -> None:
    assert isinstance(CompositionRoot().build(FakeClock()), TypingView)
