"""@file sample_text.py
@brief The passage a person copies while typing.
"""

from dataclasses import dataclass

from typing_speed_test.domain.errors import EmptySampleTextError


@dataclass(frozen=True, slots=True)
class SampleText:
    """@brief One passage of writing; it is never empty."""

    text: str

    def __post_init__(self) -> None:
        """@brief Refuse an empty text.

        @throws EmptySampleTextError When the text holds no character.
        """
        if not self.text:
            raise EmptySampleTextError("A sample text must not be empty.")
