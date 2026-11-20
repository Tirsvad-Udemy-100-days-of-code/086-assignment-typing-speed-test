"""@file typing_view_model.py
@brief What the main window shows, with no window library.
"""

from typing_speed_test.application.use_cases.start_test import StartTest
from typing_speed_test.constants import STATUS_READY_TEMPLATE
from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.domain.typing_test import TypingTest


class TypingViewModel:
    """@brief Holds the state of the window and calls the use cases."""

    def __init__(self, start_test_use_case: StartTest) -> None:
        """@brief Build the view model.

        @param start_test_use_case The use case that starts a test.
        """
        self._start_test_use_case = start_test_use_case
        self._test: TypingTest | None = None

    def start_test(self, sample_text: SampleText | None = None) -> TypingTest:
        """@brief Start a test and keep it for the window to show.

        @param sample_text The text to type, or None for a random one.
        @return The new test.
        """
        self._test = self._start_test_use_case.start_test(sample_text)
        return self._test

    def sample_text(self) -> str:
        """@brief Give the text to copy.

        @return The sample text, or an empty string before a test is started.
        """
        return "" if self._test is None else self._test.sample_text.text

    def typed_text(self) -> str:
        """@brief Give what was typed.

        @return The typed text, or an empty string before a test is started.
        """
        return "" if self._test is None else self._test.typed_text

    def status_text(self) -> str:
        """@brief Give the line shown under the input field.

        @return The test length and the hint that time starts at the first key.
        """
        if self._test is None:
            return ""
        return STATUS_READY_TEMPLATE.format(seconds=self._test.duration_seconds)
