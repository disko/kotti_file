"""kotti_file — file attachment add-on for Kotti CMS."""

from __future__ import annotations

__version__ = "0.1.0.dev0"


def includeme(config):
    """Pyramid include hook — called by ``config.include('kotti_file')``."""
    config.scan(__name__)
