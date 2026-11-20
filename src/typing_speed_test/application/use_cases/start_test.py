"""@file start_test.py
@brief Use case that starts a new typing test.
"""

from typing_speed_test.application.ports.sample_text_source import SampleTextSource
from typing_speed_test.application.test_session import TestSession
from typing_speed_test.constants import TEST_DURATION_SECONDS
from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.domain.typing_test import TypingTest


class StartTest:
    """@brief Makes a ready typing test and keeps it as the current one."""

    __test__ = False  # not a pytest class, despite the name

    def __init__(self, source: SampleTextSource, session: TestSession) -> None:
        """@brief Build the use case.

        @param source Where a sample text is taken from when none is given.
        @param session Holds the current test.
        """
        self._source = source
        self._session = session

    def start_test(self, sample_text: SampleText | None = None) -> TypingTest:
        """@brief Start a test in the ready state, dropping any earlier test.

        @param sample_text The text to type, or None to take one at random.
        @return The new test, ready, with no start time.
        """
        text = sample_text if sample_text is not None else self._source.random_text()
        test = TypingTest(sample_text=text, duration_seconds=TEST_DURATION_SECONDS)
        self._session.replace(test)
        return test
