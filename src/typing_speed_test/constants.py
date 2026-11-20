"""@file constants.py
@brief Every constant of the application, defined once.
"""

from typing import Final

## @brief Name shown in the window title.
APP_NAME: Final[str] = "Typing Speed Test"

## @brief Length of one typing test, in seconds.
TEST_DURATION_SECONDS: Final[int] = 60

## @brief Characters that count as one word when speed is measured.
CHARACTERS_PER_WORD: Final[int] = 5

## @brief Seconds in one minute, used to turn a duration into words per minute.
SECONDS_PER_MINUTE: Final[int] = 60

## @brief Largest number of results the high score list keeps.
MAX_HIGH_SCORES: Final[int] = 10

## @brief Fewest sample texts the application must offer.
MINIMUM_SAMPLE_TEXTS: Final[int] = 5

## @brief Name of the folder in the user's home folder that holds the high scores.
HIGH_SCORE_FOLDER_NAME: Final[str] = ".typing_speed_test"

## @brief Name of the file that holds the high scores.
HIGH_SCORE_FILE_NAME: Final[str] = "high_scores.json"

## @brief Status line shown while the test is ready; `{seconds}` is the test length.
STATUS_READY_TEMPLATE: Final[str] = "{seconds} s - the time starts when you type"

## @brief Width of the main window, in pixels.
WINDOW_WIDTH: Final[int] = 720

## @brief Height of the main window, in pixels.
WINDOW_HEIGHT: Final[int] = 300

## @brief Space around the widgets of the main window, in pixels.
WINDOW_PADDING: Final[int] = 16

## @brief Font of the sample text, as family, size.
SAMPLE_TEXT_FONT: Final[tuple[str, int]] = ("DejaVu Sans", 16)

## @brief Font of the input field, as family, size.
INPUT_FONT: Final[tuple[str, int]] = ("DejaVu Sans", 16)

## @brief Font of the status line, as family, size.
STATUS_FONT: Final[tuple[str, int]] = ("DejaVu Sans", 12)

## @brief Width at which the sample text wraps, in pixels.
SAMPLE_TEXT_WRAP_LENGTH: Final[int] = 680
