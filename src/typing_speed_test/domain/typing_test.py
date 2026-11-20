"""@file typing_test.py
@brief One typing test: the sample text, the time allowed and what was typed.
"""

from dataclasses import dataclass, replace

from typing_speed_test.domain.enums import CharacterMark, TestState
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

    def marks(self) -> tuple[CharacterMark, ...]:
        """@brief Tell how each character of the sample text was typed.

        @return One mark per sample character: CORRECT or WRONG for a typed
            character, PENDING for one not typed yet.
        """
        sample = self.sample_text.text
        return tuple(
            self._mark_at(index, sample_character)
            for index, sample_character in enumerate(sample)
        )

    def correct_characters(self) -> int:
        """@brief Count the typed characters that match the sample text.

        @return The number of CORRECT marks.
        """
        return self.marks().count(CharacterMark.CORRECT)

    def wrong_characters(self) -> int:
        """@brief Count the typed characters that differ from the sample text.

        @return The number of WRONG marks.
        """
        return self.marks().count(CharacterMark.WRONG)

    def elapsed_seconds(self, now: float) -> float:
        """@brief Tell how long the test has run, never more than the time allowed.

        @param now The current time in seconds.
        @return 0 before the first key; else the time from the first key to the
            end time (or to now while running), at most the duration.
        """
        if self.started_at is None:
            return 0.0
        end = self.finished_at if self.finished_at is not None else now
        return min(max(end - self.started_at, 0.0), float(self.duration_seconds))

    def remaining_seconds(self, now: float) -> float:
        """@brief Tell how much of the time allowed is left.

        @param now The current time in seconds.
        @return The duration less the elapsed time; never negative.
        """
        return max(self.duration_seconds - self.elapsed_seconds(now), 0.0)

    def with_typed_text(self, typed_text: str, now: float) -> "TypingTest":
        """@brief Take the text typed so far; deletions are allowed.

        Nothing changes when the test is finished. When the time allowed has
        run out, the test finishes and the new text is not taken. The first
        non-empty text starts the clock. Text beyond the sample length is cut.

        @param typed_text Everything typed so far.
        @param now The current time in seconds.
        @return The changed test, or this one when nothing changes.
        """
        if self.state() is TestState.FINISHED:
            return self
        if self._time_is_up(now):
            return self._finished_by_time()
        taken = typed_text[: len(self.sample_text.text)]
        started_at = self.started_at
        if started_at is None and taken:
            started_at = now
        finished_at = now if len(taken) == len(self.sample_text.text) else None
        return replace(
            self, typed_text=taken, started_at=started_at, finished_at=finished_at
        )

    def check_time(self, now: float) -> "TypingTest":
        """@brief Finish the test when the time allowed has run out.

        @param now The current time in seconds.
        @return The finished test when it was running and time is up, else this
            test.
        """
        if self.state() is TestState.RUNNING and self._time_is_up(now):
            return self._finished_by_time()
        return self

    def _mark_at(self, index: int, sample_character: str) -> CharacterMark:
        """@brief Mark one sample character against the typed text."""
        if index >= len(self.typed_text):
            return CharacterMark.PENDING
        if self.typed_text[index] == sample_character:
            return CharacterMark.CORRECT
        return CharacterMark.WRONG

    def _time_is_up(self, now: float) -> bool:
        """@brief Tell whether a started test has used all its time."""
        if self.started_at is None:
            return False
        return now - self.started_at >= self.duration_seconds

    def _finished_by_time(self) -> "TypingTest":
        """@brief Finish a started test at the moment its time ran out."""
        if self.started_at is None:
            return self
        return replace(self, finished_at=self.started_at + self.duration_seconds)
