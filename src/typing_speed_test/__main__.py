"""@file __main__.py
@brief Entry point: `python -m typing_speed_test` opens the main window.
"""

from typing_speed_test.infrastructure.composition_root import CompositionRoot


def main() -> None:
    """@brief Build the application and run its window."""
    CompositionRoot().build().run()


if __name__ == "__main__":
    main()
