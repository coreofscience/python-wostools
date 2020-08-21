"""Top-level package for Python WoS tools."""

__author__ = """Core of Science"""
__email__ = "dev@coreofscience.com"
__version__ = "2.0.6"

from wostools.article import Article
from wostools.lazy import LazyCollection
from wostools.cached import CachedCollection

__all__ = ["CachedCollection", "LazyCollection", "Article"]
