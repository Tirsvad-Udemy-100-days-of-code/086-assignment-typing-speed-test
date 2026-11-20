"""@file screenshot.py
@brief Saves a cropped screenshot of a window shown on the virtual display.
"""

import os
import subprocess
import tkinter
from pathlib import Path

## @brief Environment variable that names the folder screenshots are written to.
SCREENSHOT_DIR_VARIABLE = "SCREENSHOT_DIR"

## @brief Folder screenshots are written to when the variable is not set.
DEFAULT_SCREENSHOT_DIR = "docs/screenshots"


def screenshot_folder() -> Path:
    """@brief Find the folder screenshots are written to.

    @return The folder in SCREENSHOT_DIR, or docs/screenshots when it is not set.
    """
    return Path(os.environ.get(SCREENSHOT_DIR_VARIABLE, DEFAULT_SCREENSHOT_DIR))


def take_screenshot(window: tkinter.Tk, name: str) -> Path:
    """@brief Save a PNG of a window, cropped to the window, with ImageMagick.

    The window must be shown on the display named in DISPLAY.

    @param window The Tk window to capture.
    @param name File name of the PNG, such as `main-window.png`.
    @return The path of the written file.
    """
    window.update_idletasks()
    window.update()
    geometry = (
        f"{window.winfo_width()}x{window.winfo_height()}"
        f"+{window.winfo_rootx()}+{window.winfo_rooty()}"
    )
    folder = screenshot_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / name
    subprocess.run(
        [
            "import",
            "-display",
            os.environ["DISPLAY"],
            "-window",
            "root",
            "-crop",
            geometry,
            "+repage",
            str(target),
        ],
        check=True,
    )
    return target
