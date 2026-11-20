"""@file errors.py
@brief The refusals of the application layer.
"""


class NoActiveTestError(Exception):
    """@brief An operation needs a typing test, and none was started."""
