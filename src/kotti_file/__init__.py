"""kotti_file — file attachment add-on for Kotti CMS."""

from __future__ import annotations

__version__ = "0.1.0.dev0"


def kotti_configure(settings):
    """Add a line like this to your .ini file::

        kotti.configurators =
            kotti_file.kotti_configure

    to enable the ``kotti_file`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """
    settings["pyramid.includes"] += " kotti_file"


def includeme(config):
    """Pyramid include hook — called automatically when ``kotti_file``
    appears in ``pyramid.includes`` (wired by :func:`kotti_configure`).

    Do NOT add this to ``pyramid.includes`` directly; use
    ``kotti.configurators = kotti_file.kotti_configure`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """
    config.scan(__name__)
