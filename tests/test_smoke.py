"""Smoke tests for kotti_file."""

from kotti_file import includeme, kotti_configure


def test_kotti_configure_is_callable():
    """kotti_configure must be a callable (kotti configurator contract)."""
    assert callable(kotti_configure)


def test_includeme_is_callable():
    """includeme must be a callable (Pyramid include hook contract)."""
    assert callable(includeme)


def test_kotti_configure_injects_pyramid_include():
    """kotti_configure must append 'kotti_file' to pyramid.includes."""
    settings = {"pyramid.includes": ""}
    kotti_configure(settings)
    assert "kotti_file" in settings["pyramid.includes"]
