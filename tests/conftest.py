"""@file conftest.py
@brief Skips graphical tests unless a display is set (the Docker harness sets it).
"""

import os

import pytest


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """@brief Skip every test marked `gui` when DISPLAY is not set.

    @param items The collected tests.
    """
    if os.environ.get("DISPLAY"):
        return
    skip = pytest.mark.skip(
        reason="no DISPLAY: graphical tests run in the Docker harness"
    )
    for item in items:
        if "gui" in item.keywords:
            item.add_marker(skip)
