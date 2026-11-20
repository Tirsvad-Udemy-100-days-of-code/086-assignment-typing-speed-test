"""@file capture_smoke.py
@brief Opens a small window on the virtual display and saves a screenshot of it.

The few lines that take the screenshot repeat those of tests/gui/screenshot.py on
purpose: this script runs as a plain file inside the container, where the tests
package is not on the import path.
"""

import os
import subprocess
import tkinter
from pathlib import Path

from typing_speed_test.constants import APP_NAME

## @brief Name of the PNG file the smoke run writes.
SMOKE_FILE_NAME = "harness-smoke.png"


def capture(window: tkinter.Tk, target: Path) -> None:
    """@brief Save a PNG of a window, cropped to the window, with ImageMagick.

    @param window The Tk window to capture, shown on the display named in DISPLAY.
    @param target Path of the PNG file to write.
    """
    window.update_idletasks()
    window.update()
    geometry = (
        f"{window.winfo_width()}x{window.winfo_height()}"
        f"+{window.winfo_rootx()}+{window.winfo_rooty()}"
    )
    # Fixed arguments, no shell; `import` is ImageMagick, installed in the image.
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


def main() -> None:
    """@brief Draw a small window and write its screenshot to SCREENSHOT_DIR."""
    folder = Path(os.environ.get("SCREENSHOT_DIR", "docs/screenshots"))
    folder.mkdir(parents=True, exist_ok=True)

    root = tkinter.Tk()
    root.title(APP_NAME)
    root.geometry("640x400+0+0")
    tkinter.Label(root, text="Docker harness works", font=("DejaVu Sans", 24)).pack(
        expand=True
    )
    capture(root, folder / SMOKE_FILE_NAME)
    root.destroy()


if __name__ == "__main__":
    main()
