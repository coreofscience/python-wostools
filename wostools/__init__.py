"""Top-level package for Python WoS tools."""

__author__ = """Core of Science"""
__email__ = 'dev@coreofscience.com'
__version__ = '0.1.1'

from wostools.wostools import CollectionLazy, WosToolsError

__all__ = [
    'CollectionLazy',
    'WosToolsError'
]
