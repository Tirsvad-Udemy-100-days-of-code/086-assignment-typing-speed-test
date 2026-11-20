"""@file test_sample_text.py
@brief Tests of SampleText.
"""

import pytest

from typing_speed_test.domain.errors import DomainError, EmptySampleTextError
from typing_speed_test.domain.sample_text import SampleText


def test_sample_text_keeps_its_text() -> None:
    assert SampleText("abc").text == "abc"


def test_sample_text_refuses_empty_text() -> None:
    with pytest.raises(EmptySampleTextError):
        SampleText("")


def test_empty_sample_text_error_is_a_domain_error() -> None:
    assert issubclass(EmptySampleTextError, DomainError)
