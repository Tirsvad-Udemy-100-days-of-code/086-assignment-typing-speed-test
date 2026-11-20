"""@file built_in_sample_text_source.py
@brief Adapter that gives the sample texts kept in the application.
"""

import random

from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.infrastructure.built_in_texts import BUILT_IN_TEXTS


class BuiltInSampleTextSource:
    """@brief Implements the SampleTextSource port with the built-in texts."""

    def all_texts(self) -> tuple[SampleText, ...]:
        """@brief Give every built-in sample text.

        @return The sample texts.
        """
        return tuple(SampleText(text) for text in BUILT_IN_TEXTS)

    def random_text(self) -> SampleText:
        """@brief Give one built-in sample text chosen at random.

        @return A sample text.
        """
        # Not a security use: the choice only varies the passage.
        return random.choice(self.all_texts())  # noqa: S311
