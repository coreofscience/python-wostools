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
