#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `wostools` package."""

from wostools import CollectionLazy


def test_collection():
    """
    Just kinda an end to end test.
    """
    collection = CollectionLazy('docs/examples/bit-pattern-savedrecs.txt')
    for article in collection.articles:
        assert article.TI


def test_article_label(article):
    """
    Test label value of article.
    """
    assert article.label == (
        'Wodarz S, 2017, JOURNAL OF MAGNETISM AND MAGNETIC MATERIALS, '
        'V430, P7, DOI 10.1016/j.jmmm.2017.01.061'
    )
