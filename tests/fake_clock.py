"""@file fake_clock.py
@brief A clock the test moves by hand, so no test waits for real time.
"""

from datetime import date


class FakeClock:
    """@brief Implements the Clock port with a time the test sets."""

    def __init__(self, now: float = 0.0, today: date = date(2026, 1, 1)) -> None:
        """@brief Build the clock.

        @param now The time in seconds to start at.
        @param today The date to report.
        """
        self._now = now
        self._today = today

    def now(self) -> float:
        """@brief Give the time the test set.

        @return Seconds.
        """
        return self._now

    def today(self) -> date:
        """@brief Give the date the test set.

        @return The date.
        """
        return self._today

    def advance(self, seconds: float) -> None:
        """@brief Move the time forward.

        @param seconds How far to move.
        """
        self._now += seconds
