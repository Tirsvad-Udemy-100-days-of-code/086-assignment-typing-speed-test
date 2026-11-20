"""@file sample_text_source.py
@brief Port that gives the sample texts.
"""

from typing import Protocol

from typing_speed_test.domain.sample_text import SampleText


class SampleTextSource(Protocol):
    """@brief Where the sample texts come from."""

    def all_texts(self) -> tuple[SampleText, ...]:
        """@brief Give every sample text.

        @return The sample texts.
        """
        ...

    def random_text(self) -> SampleText:
        """@brief Give one sample text chosen at random.

        @return A sample text.
        """
        ...
