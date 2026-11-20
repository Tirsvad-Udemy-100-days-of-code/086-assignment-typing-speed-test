"""@file record_input.py
@brief Use case that takes the typed text and watches the time.
"""

from typing_speed_test.application.ports.clock import Clock
from typing_speed_test.application.test_session import TestSession
from typing_speed_test.domain.typing_test import TypingTest


class RecordInput:
    """@brief Gives the typed text and the passing time to the current test."""

    def __init__(self, session: TestSession, clock: Clock) -> None:
        """@brief Build the use case.

        @param session Holds the current test.
        @param clock Tells the time.
        """
        self._session = session
        self._clock = clock

    def type_text(self, typed_text: str) -> TypingTest:
        """@brief Record what was typed so far.

        @param typed_text Everything typed so far.
        @return The changed current test.
        @throws NoActiveTestError When no test was started.
        """
        test = self._session.current_test()
        changed = test.with_typed_text(typed_text, self._clock.now())
        self._session.replace(changed)
        return changed

    def check_time(self) -> TypingTest:
        """@brief Finish the current test when its time has run out.

        @return The current test, finished when time is up.
        @throws NoActiveTestError When no test was started.
        """
        test = self._session.current_test()
        checked = test.check_time(self._clock.now())
        self._session.replace(checked)
        return checked
