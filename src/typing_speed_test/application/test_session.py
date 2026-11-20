"""@file test_session.py
@brief Holds the typing test that is current.
"""

from typing_speed_test.application.errors import NoActiveTestError
from typing_speed_test.domain.typing_test import TypingTest


class TestSession:
    """@brief The one place that keeps the current typing test."""

    __test__ = False  # not a pytest class, despite the name

    def __init__(self) -> None:
        """@brief Start with no test."""
        self._current: TypingTest | None = None

    def current_test(self) -> TypingTest:
        """@brief Give the current typing test.

        @return The current test.
        @throws NoActiveTestError When no test was started.
        """
        if self._current is None:
            raise NoActiveTestError("Start a test first.")
        return self._current

    def replace(self, test: TypingTest) -> None:
        """@brief Make a test the current one and drop the earlier one.

        @param test The new current test.
        """
        self._current = test
