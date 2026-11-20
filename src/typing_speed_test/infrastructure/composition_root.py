"""@file composition_root.py
@brief The one place that builds the objects and joins them.
"""

from typing_speed_test.application.ports.clock import Clock
from typing_speed_test.application.test_session import TestSession
from typing_speed_test.application.use_cases.record_input import RecordInput
from typing_speed_test.application.use_cases.start_test import StartTest
from typing_speed_test.infrastructure.built_in_sample_text_source import (
    BuiltInSampleTextSource,
)
from typing_speed_test.infrastructure.system_clock import SystemClock
from typing_speed_test.presentation.features.typing_test.typing_view import (
    TypingView,
)
from typing_speed_test.presentation.features.typing_test.typing_view_model import (
    TypingViewModel,
)


class CompositionRoot:
    """@brief Wires the layers; nothing else names a concrete adapter."""

    def build(self, clock: Clock | None = None) -> TypingView:
        """@brief Build the main window with everything it needs.

        No window is opened until the view is asked to.

        @param clock The clock to use; the system clock when None. A test passes
            a fake so that no test waits for real time.
        @return The view, ready to run.
        """
        used_clock = clock if clock is not None else SystemClock()
        source = BuiltInSampleTextSource()
        session = TestSession()
        view_model = TypingViewModel(
            start_test_use_case=StartTest(source, session),
            record_input_use_case=RecordInput(session, used_clock),
            clock=used_clock,
        )
        return TypingView(view_model)
