"""@file errors.py
@brief The refusals of the domain.
"""


class DomainError(Exception):
    """@brief Base of every error the domain rules raise."""


class EmptySampleTextError(DomainError):
    """@brief A sample text was empty."""
