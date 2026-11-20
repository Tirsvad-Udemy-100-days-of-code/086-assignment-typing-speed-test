"""@file system_clock.py
@brief Adapter that tells the time from the operating system.
"""

import time
from datetime import date


class SystemClock:
    """@brief Implements the Clock port with the system clocks."""

    def now(self) -> float:
        """@brief Give a monotonic time, which a clock change cannot move back.

        @return Seconds from an arbitrary start.
        """
        return time.monotonic()

    def today(self) -> date:
        """@brief Give today's date.

        @return The local date today.
        """
        # A calendar day, not an instant, so a naive local date is right.
        return date.today()
