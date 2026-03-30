"""kotti_file — file attachment add-on for Kotti CMS."""

from __future__ import annotations

__version__ = "0.1.0.dev0"


def kotti_configure(settings):
    """Add to your .ini file::

        kotti.configurators =
            kotti_file.kotti_configure

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """
    settings["pyramid.includes"] += " kotti_file"
    settings["kotti.available_types"] += " kotti_file.resources.File"
    settings["kotti.alembic_dirs"] += " kotti_file:alembic"


def includeme(config):
    """Pyramid include hook — wired automatically via :func:`kotti_configure`.

    Do NOT add to ``pyramid.includes`` directly.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """
    config.scan(__name__)
