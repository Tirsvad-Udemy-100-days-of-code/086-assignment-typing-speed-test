"""@file test_system_clock.py
@brief Tests of SystemClock; no test sleeps.
"""

from datetime import date

from typing_speed_test.infrastructure.system_clock import SystemClock


def test_now_never_decreases() -> None:
    clock = SystemClock()
    readings = [clock.now() for _ in range(100)]
    assert readings == sorted(readings)


def test_today_is_a_date() -> None:
    assert isinstance(SystemClock().today(), date)
