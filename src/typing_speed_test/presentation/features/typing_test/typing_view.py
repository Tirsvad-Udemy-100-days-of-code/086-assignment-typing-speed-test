"""@file typing_view.py
@brief The main window: draws what the view model holds and holds no rule.
"""

import tkinter

from typing_speed_test.constants import (
    APP_NAME,
    COLOR_CORRECT_FOREGROUND,
    COLOR_PENDING_FOREGROUND,
    COLOR_SAMPLE_BACKGROUND,
    COLOR_WRONG_BACKGROUND,
    COLOR_WRONG_FOREGROUND,
    INPUT_FONT,
    SAMPLE_TEXT_FONT,
    SAMPLE_TEXT_HEIGHT_LINES,
    SAMPLE_TEXT_WIDTH_CHARS,
    STATUS_FONT,
    TAG_CORRECT,
    TAG_PENDING,
    TAG_WRONG,
    TIMER_INTERVAL_MS,
    WINDOW_HEIGHT,
    WINDOW_PADDING,
    WINDOW_WIDTH,
)
from typing_speed_test.domain.enums import CharacterMark
from typing_speed_test.presentation.features.typing_test.typing_view_model import (
    TypingViewModel,
)

_TAG_OF_MARK = {
    CharacterMark.CORRECT: TAG_CORRECT,
    CharacterMark.WRONG: TAG_WRONG,
    CharacterMark.PENDING: TAG_PENDING,
}


class TypingView:
    """@brief The Tkinter main window of the typing test."""

    def __init__(self, view_model: TypingViewModel) -> None:
        """@brief Build the view; no window is opened yet.

        @param view_model What the window shows.
        """
        self._view_model = view_model
        self._root: tkinter.Tk | None = None
        self._sample: tkinter.Text | None = None
        self._input: tkinter.Entry | None = None
        self._input_text: tkinter.StringVar | None = None
        self._status: tkinter.Label | None = None

    def open_window(self) -> tkinter.Tk:
        """@brief Start a test and draw the window.

        @return The window, shown and not yet in its event loop.
        """
        self._view_model.start_test()
        root = tkinter.Tk()
        self._root = root
        root.title(APP_NAME)
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self._sample = self._build_sample(root)
        self._input_text = tkinter.StringVar(root, self._view_model.typed_text())
        self._input = tkinter.Entry(
            root, font=INPUT_FONT, textvariable=self._input_text
        )
        self._input.pack(fill=tkinter.X, padx=WINDOW_PADDING)
        self._status = tkinter.Label(root, font=STATUS_FONT)
        self._status.pack(padx=WINDOW_PADDING, pady=WINDOW_PADDING, anchor=tkinter.W)
        self._input_text.trace_add("write", self._on_input_changed)
        self._render()
        root.after(TIMER_INTERVAL_MS, self._on_tick)
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

    def _build_sample(self, root: tkinter.Tk) -> tkinter.Text:
        """@brief Draw the sample text box with its colour tags."""
        sample = tkinter.Text(
            root,
            font=SAMPLE_TEXT_FONT,
            width=SAMPLE_TEXT_WIDTH_CHARS,
            height=SAMPLE_TEXT_HEIGHT_LINES,
            wrap=tkinter.WORD,
            background=COLOR_SAMPLE_BACKGROUND,
            relief=tkinter.FLAT,
        )
        sample.insert("1.0", self._view_model.sample_text())
        sample.tag_config(TAG_CORRECT, foreground=COLOR_CORRECT_FOREGROUND)
        sample.tag_config(
            TAG_WRONG,
            foreground=COLOR_WRONG_FOREGROUND,
            background=COLOR_WRONG_BACKGROUND,
        )
        sample.tag_config(TAG_PENDING, foreground=COLOR_PENDING_FOREGROUND)
        sample.configure(state=tkinter.DISABLED)
        sample.pack(padx=WINDOW_PADDING, pady=WINDOW_PADDING, anchor=tkinter.W)
        return sample

    def _on_input_changed(self, *_: str) -> None:
        """@brief Pass the changed input to the view model and redraw."""
        if self._input_text is None:
            return
        self._view_model.type_text(self._input_text.get())
        self._render()

    def _on_tick(self) -> None:
        """@brief Look at the clock, redraw, and ask for the next look."""
        if self._root is None:
            return
        self._view_model.check_time()
        self._render()
        if not self._view_model.is_locked():
            self._root.after(TIMER_INTERVAL_MS, self._on_tick)

    def _render(self) -> None:
        """@brief Draw the colours, the status line and the lock."""
        if (
            self._sample is None
            or self._input is None
            or self._input_text is None
            or self._status is None
        ):
            return
        self._draw_marks(self._sample)
        self._status.configure(text=self._view_model.status_text())
        if self._input_text.get() != self._view_model.typed_text():
            self._input_text.set(self._view_model.typed_text())
        locked = self._view_model.is_locked()
        self._input.configure(state=tkinter.DISABLED if locked else tkinter.NORMAL)

    def _draw_marks(self, sample: tkinter.Text) -> None:
        """@brief Tag every sample character as correct, wrong or pending."""
        for tag in (TAG_CORRECT, TAG_WRONG, TAG_PENDING):
            sample.tag_remove(tag, "1.0", tkinter.END)
        for index, mark in enumerate(self._view_model.marks()):
            sample.tag_add(_TAG_OF_MARK[mark], f"1.0+{index}c", f"1.0+{index + 1}c")
