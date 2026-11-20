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

## @brief Width of the sample text box, in characters.
SAMPLE_TEXT_WIDTH_CHARS: Final[int] = 60

## @brief Height of the sample text box, in lines.
SAMPLE_TEXT_HEIGHT_LINES: Final[int] = 4

## @brief Status line while the test runs; `{seconds}` is the whole seconds left.
STATUS_RUNNING_TEMPLATE: Final[str] = "{seconds} s left"

## @brief Status line when the test has ended.
STATUS_FINISHED_TEXT: Final[str] = "Time is up or the text is complete - finished"

## @brief Milliseconds between two looks at the clock while a test runs.
TIMER_INTERVAL_MS: Final[int] = 200

## @brief Name of the text tag of a correctly typed character.
TAG_CORRECT: Final[str] = "correct"

## @brief Name of the text tag of a wrongly typed character.
TAG_WRONG: Final[str] = "wrong"

## @brief Name of the text tag of a character not typed yet.
TAG_PENDING: Final[str] = "pending"

## @brief Text colour of a correctly typed character.
COLOR_CORRECT_FOREGROUND: Final[str] = "#1b7f1b"

## @brief Text colour of a wrongly typed character.
COLOR_WRONG_FOREGROUND: Final[str] = "#b00020"

## @brief Background colour of a wrongly typed character.
COLOR_WRONG_BACKGROUND: Final[str] = "#f9d6d9"

## @brief Text colour of a character not typed yet.
COLOR_PENDING_FOREGROUND: Final[str] = "#555555"

## @brief Background colour of the sample text box.
COLOR_SAMPLE_BACKGROUND: Final[str] = "#f4f4f4"
