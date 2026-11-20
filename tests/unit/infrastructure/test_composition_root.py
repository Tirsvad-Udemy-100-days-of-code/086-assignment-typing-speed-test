"""@file test_composition_root.py
@brief Test that the composition root builds without opening a window.
"""

from typing_speed_test.infrastructure.composition_root import CompositionRoot
from typing_speed_test.presentation.features.typing_test.typing_view import (
    TypingView,
)


def test_build_gives_a_view() -> None:
    assert isinstance(CompositionRoot().build(), TypingView)
