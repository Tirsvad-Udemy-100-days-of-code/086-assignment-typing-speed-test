"""@file typing_view.py
@brief The main window: draws what the view model holds and holds no rule.
"""

import tkinter

from typing_speed_test.constants import (
    APP_NAME,
    INPUT_FONT,
    SAMPLE_TEXT_FONT,
    SAMPLE_TEXT_WRAP_LENGTH,
    STATUS_FONT,
    WINDOW_HEIGHT,
    WINDOW_PADDING,
    WINDOW_WIDTH,
)
from typing_speed_test.presentation.features.typing_test.typing_view_model import (
    TypingViewModel,
)


class TypingView:
    """@brief The Tkinter main window of the typing test."""

    def __init__(self, view_model: TypingViewModel) -> None:
        """@brief Build the view; no window is opened yet.

        @param view_model What the window shows.
        """
        self._view_model = view_model
        self._input: tkinter.Entry | None = None

    def open_window(self) -> tkinter.Tk:
        """@brief Start a test and draw the window.

        @return The window, shown and not yet in its event loop.
        """
        self._view_model.start_test()
        root = tkinter.Tk()
        root.title(APP_NAME)
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        tkinter.Label(
            root,
            text=self._view_model.sample_text(),
            font=SAMPLE_TEXT_FONT,
            wraplength=SAMPLE_TEXT_WRAP_LENGTH,
            justify=tkinter.LEFT,
        ).pack(padx=WINDOW_PADDING, pady=WINDOW_PADDING, anchor=tkinter.W)
        self._input = tkinter.Entry(root, font=INPUT_FONT)
        self._input.insert(0, self._view_model.typed_text())
        self._input.pack(fill=tkinter.X, padx=WINDOW_PADDING)
        tkinter.Label(root, text=self._view_model.status_text(), font=STATUS_FONT).pack(
            padx=WINDOW_PADDING, pady=WINDOW_PADDING, anchor=tkinter.W
        )
        return root

    def focus_input(self) -> None:
        """@brief Put the keyboard focus in the input field."""
        if self._input is not None:
            self._input.focus_force()

    def run(self) -> None:
        """@brief Open the window and wait until it is closed."""
        root = self.open_window()
        self.focus_input()
        root.mainloop()
