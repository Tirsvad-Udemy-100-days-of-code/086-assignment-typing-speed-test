"""@file test_test_session.py
@brief Tests of TestSession.
"""

import pytest

from typing_speed_test.application.errors import NoActiveTestError
from typing_speed_test.application.test_session import TestSession
from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.domain.typing_test import TypingTest


def test_current_test_refuses_when_none_started() -> None:
    with pytest.raises(NoActiveTestError):
        TestSession().current_test()


def test_replace_makes_the_test_current() -> None:
    session = TestSession()
    test = TypingTest(SampleText("abc"), 60)
    session.replace(test)
    assert session.current_test() is test
