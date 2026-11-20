"""@file typing_test.py
@brief One typing test: the sample text, the time allowed and what was typed.
"""

from dataclasses import dataclass

from typing_speed_test.domain.enums import TestState
from typing_speed_test.domain.sample_text import SampleText


@dataclass(frozen=True, slots=True)
class TypingTest:
    """@brief An immutable typing test; a change makes a new instance."""

    __test__ = False  # not a pytest class, despite the name

    sample_text: SampleText
    duration_seconds: int
    typed_text: str = ""
    started_at: float | None = None
    finished_at: float | None = None

    def state(self) -> TestState:
        """@brief Tell where the test is: ready, running or finished.

        @return FINISHED when it has an end time, RUNNING when it has a start
            time only, READY otherwise.
        """
        if self.finished_at is not None:
            return TestState.FINISHED
        if self.started_at is not None:
            return TestState.RUNNING
        return TestState.READY
