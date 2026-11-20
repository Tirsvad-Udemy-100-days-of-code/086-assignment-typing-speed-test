"""@file enums.py
@brief Enumerations of the domain: the states of a test and the mark of a character.
"""

from enum import Enum, auto


class TestState(Enum):
    """@brief Where a typing test is in its life."""

    __test__ = False  # not a pytest class, despite the name

    READY = auto()
    RUNNING = auto()
    FINISHED = auto()


class CharacterMark(Enum):
    """@brief How one character of the sample text compares with the typed text."""

    CORRECT = auto()
    WRONG = auto()
    PENDING = auto()
