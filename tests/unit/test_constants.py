"""@file test_constants.py
@brief Tests of the shared constants.
"""

from pathlib import Path

from typing_speed_test import constants


def test_app_name_is_not_empty() -> None:
    assert constants.APP_NAME.strip() != ""


def test_numeric_constants_are_positive() -> None:
    assert constants.TEST_DURATION_SECONDS > 0
    assert constants.CHARACTERS_PER_WORD > 0
    assert constants.SECONDS_PER_MINUTE > 0
    assert constants.MAX_HIGH_SCORES > 0
    assert constants.MINIMUM_SAMPLE_TEXTS > 0


def test_one_minute_has_sixty_seconds() -> None:
    assert constants.SECONDS_PER_MINUTE == 60


def test_high_score_file_name_ends_with_json() -> None:
    assert constants.HIGH_SCORE_FILE_NAME.endswith(".json")


def test_high_score_names_are_single_path_parts() -> None:
    for name in (constants.HIGH_SCORE_FOLDER_NAME, constants.HIGH_SCORE_FILE_NAME):
        assert Path(name).name == name


def test_high_score_folder_is_hidden() -> None:
    assert constants.HIGH_SCORE_FOLDER_NAME.startswith(".")
