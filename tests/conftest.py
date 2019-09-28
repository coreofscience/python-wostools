"""
Configuration file for python-wostools tests.
"""

from wostools import Article

import pytest


@pytest.fixture
def article():
    with open("docs/examples/single-article.txt") as article_file:
        article_text = article_file.read()
    return Article(article_text)
