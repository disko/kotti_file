"""kotti_file — file attachment add-on for Kotti CMS."""

from __future__ import annotations

__version__ = "0.1.0.dev0"


def includeme(config):
    """Pyramid include hook.

    Add to your .ini file::

        pyramid.includes =
            kotti_file

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """
    config.scan(__name__)
