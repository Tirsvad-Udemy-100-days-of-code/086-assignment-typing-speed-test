"""@file typing_view_model.py
@brief What the main window shows, with no window library.
"""

import math

from typing_speed_test.application.ports.clock import Clock
from typing_speed_test.application.use_cases.record_input import RecordInput
from typing_speed_test.application.use_cases.start_test import StartTest
from typing_speed_test.constants import (
    STATUS_FINISHED_TEXT,
    STATUS_READY_TEMPLATE,
    STATUS_RUNNING_TEMPLATE,
)
from typing_speed_test.domain.enums import CharacterMark, TestState
from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.domain.typing_test import TypingTest


class TypingViewModel:
    """@brief Holds the state of the window and calls the use cases."""

    def __init__(
        self,
        start_test_use_case: StartTest,
        record_input_use_case: RecordInput,
        clock: Clock,
    ) -> None:
        """@brief Build the view model.

        @param start_test_use_case The use case that starts a test.
        @param record_input_use_case The use case that takes typed text and time.
        @param clock Tells the time, to work out the time left.
        """
        self._start_test_use_case = start_test_use_case
        self._record_input_use_case = record_input_use_case
        self._clock = clock
        self._test: TypingTest | None = None

    def start_test(self, sample_text: SampleText | None = None) -> TypingTest:
        """@brief Start a test and keep it for the window to show.

        @param sample_text The text to type, or None for a random one.
        @return The new test.
        """
        self._test = self._start_test_use_case.start_test(sample_text)
        return self._test

    def type_text(self, typed_text: str) -> TypingTest:
        """@brief Pass the typed text on and keep the changed test.

        @param typed_text Everything typed so far.
        @return The changed test.
        """
        self._test = self._record_input_use_case.type_text(typed_text)
        return self._test

    def check_time(self) -> TypingTest:
        """@brief Look at the clock and keep the test, finished when time is up.

        @return The checked test.
        """
        self._test = self._record_input_use_case.check_time()
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

    def marks(self) -> tuple[CharacterMark, ...]:
        """@brief Give the mark of each sample character.

        @return One mark per sample character, or nothing before a test starts.
        """
        return () if self._test is None else self._test.marks()

    def remaining_seconds(self) -> float:
        """@brief Give the time left.

        @return Seconds left, or 0 before a test is started.
        """
        if self._test is None:
            return 0.0
        return self._test.remaining_seconds(self._clock.now())

    def is_locked(self) -> bool:
        """@brief Tell whether the input must refuse more typing.

        @return True when the test is finished.
        """
        return self._test is not None and self._test.state() is TestState.FINISHED

    def status_text(self) -> str:
        """@brief Give the line shown under the input field.

        @return The hint before the first key, the countdown while running, and
            a closing line when the test has ended.
        """
        if self._test is None:
            return ""
        state = self._test.state()
        if state is TestState.READY:
            return STATUS_READY_TEMPLATE.format(seconds=self._test.duration_seconds)
        if state is TestState.RUNNING:
            seconds = math.ceil(self.remaining_seconds())
            return STATUS_RUNNING_TEMPLATE.format(seconds=seconds)
        return STATUS_FINISHED_TEXT
