"""Top-level package for Python WoS tools."""

__author__ = """Core of Science"""
__email__ = "dev@coreofscience.com"
__version__ = "3.0.2"

from wostools.article import Article
from wostools.cached import CachedCollection
from wostools.cached import CachedCollection as Collection

__all__ = ["CachedCollection", "Collection", "Article"]
