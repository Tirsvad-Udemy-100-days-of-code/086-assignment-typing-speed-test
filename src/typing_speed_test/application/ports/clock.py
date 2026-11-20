"""@file clock.py
@brief Port that tells the time.
"""

from datetime import date
from typing import Protocol


class Clock(Protocol):
    """@brief Where the current time comes from."""

    def now(self) -> float:
        """@brief Give a steadily increasing time in seconds.

        @return Seconds from an arbitrary start; it never goes back.
        """
        ...

    def today(self) -> date:
        """@brief Give today's calendar date.

        @return The date today.
        """
        ...
