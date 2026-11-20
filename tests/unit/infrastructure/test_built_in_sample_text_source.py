"""@file test_built_in_sample_text_source.py
@brief Tests of BuiltInSampleTextSource.
"""

from typing_speed_test.infrastructure.built_in_sample_text_source import (
    BuiltInSampleTextSource,
)


def test_all_texts_gives_at_least_one_text() -> None:
    assert len(BuiltInSampleTextSource().all_texts()) >= 1


def test_all_texts_are_not_empty() -> None:
    assert all(text.text for text in BuiltInSampleTextSource().all_texts())


def test_random_text_is_one_of_all_texts() -> None:
    source = BuiltInSampleTextSource()
    assert source.random_text() in source.all_texts()
