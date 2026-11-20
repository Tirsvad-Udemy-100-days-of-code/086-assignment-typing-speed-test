"""@file composition_root.py
@brief The one place that builds the objects and joins them.
"""

from typing_speed_test.application.test_session import TestSession
from typing_speed_test.application.use_cases.start_test import StartTest
from typing_speed_test.infrastructure.built_in_sample_text_source import (
    BuiltInSampleTextSource,
)
from typing_speed_test.presentation.features.typing_test.typing_view import (
    TypingView,
)
from typing_speed_test.presentation.features.typing_test.typing_view_model import (
    TypingViewModel,
)


class CompositionRoot:
    """@brief Wires the layers; nothing else names a concrete adapter."""

    def build(self) -> TypingView:
        """@brief Build the main window with everything it needs.

        No window is opened until the view is asked to.

        @return The view, ready to run.
        """
        source = BuiltInSampleTextSource()
        session = TestSession()
        view_model = TypingViewModel(start_test_use_case=StartTest(source, session))
        return TypingView(view_model)
