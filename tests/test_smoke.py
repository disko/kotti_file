"""Smoke tests for kotti_file."""

from kotti_file import includeme, kotti_configure


def test_kotti_configure_is_callable():
    assert callable(kotti_configure)


def test_includeme_is_callable():
    assert callable(includeme)


def test_kotti_configure_injects_settings():
    settings = {
        "pyramid.includes": "",
        "kotti.available_types": "kotti.resources.Document",
        "kotti.alembic_dirs": "kotti:alembic",
    }
    kotti_configure(settings)
    assert "kotti_file" in settings["pyramid.includes"]
    assert "kotti_file.resources.File" in settings["kotti.available_types"]
    assert "kotti_file:alembic" in settings["kotti.alembic_dirs"]
