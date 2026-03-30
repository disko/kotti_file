"""Smoke tests for kotti_file."""

from kotti_file import includeme


def test_includeme_is_callable():
    """includeme must be a callable (Pyramid include hook contract)."""
    assert callable(includeme)
