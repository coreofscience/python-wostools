"""
Configuration file for python-wostools tests.
"""

from wostools import Article

import pytest


@pytest.fixture()
def article():
    article_file = open('docs/examples/single-article.txt')
    article_text = article_file.read()
    return Article(article_text)
