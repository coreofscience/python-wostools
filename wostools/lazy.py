"""
The whole wostools thing.
"""

import collections
import glob
import itertools
import logging
import re
from typing import Callable, Dict, Iterable, Optional, Tuple, TypeVar, Union

from wostools.article import Article

logger = logging.getLogger(__name__)


class CollectionLazy(object):
    """A collection of WOS text files.

    Args:
        *filenames (str): Strings with the names of the files containing
            articles.
    """

    def __init__(self, *files):
        self._files = files
        for file in self._files:
            file.seek(0)

    @classmethod
    def from_glob(cls, pattern):
        """Creates a new collection from a pattern using glob.

        Args:
            pattern (str): String with the pattern to be passed to glob.

        Returns:
            CollectionLazy: Collection with the articles by using the pattern.
        """
        return cls.from_filenames(*glob.glob(pattern))

    @classmethod
    def from_filenames(cls, *filenames):
        """Creates a new collection from a list of filenames.

        Args:
            *filenames (str): String with the filename.

        Returns:
            CollectionLazy: Collection with the articles by reading the
                filenames.
        """
        files = [open(filename, encoding="utf-8-sig") for filename in filenames]
        return cls(*files)

    @property
    def files(self):
        """Iterates over all files in the collection

        Returns:
            generator: A generator of stream files.
        """
        yield from self._files

    @property
    def _article_texts(self):
        """Iterates over all the single article texts in the colection.

        Returns:
            generator: A generator of strings with the text articles.
        """
        for filehandle in self.files:
            filehandle.seek(0)
            data = filehandle.read()
            filehandle.seek(0)
            for article_text in data.split("\n\n"):
                if article_text != "EF":
                    yield article_text

    @property
    def _articles(self) -> Iterable[Article]:
        for article_text in self._article_texts:
            yield Article.from_isi_text(article_text)

    @property
    def articles(self) -> Iterable[Article]:
        """Iterates over all articles.

        Returns:
            generator: A generator of Articles according to the text articles.
        """
        for article in self._articles:
            yield article
            for reference in article.references:
                try:
                    yield Article.from_isi_citation(reference)
                except ValueError:
                    logger.warning(
                        f"Ignoring malformed reference {reference} from {article.label}"
                    )

    def __len__(self):
        return sum(1 for _ in self.articles)

    @property
    def authors(self) -> Iterable[str]:
        """Iterates over all article authors, including duplicates

        Returns:
            generator: A generator with the authors (one by one) of the
                articles in the collection.
        """
        for article in self.articles:
            yield from article.authors

    @property
    def coauthors(self) -> Iterable[Tuple[str, str]]:
        """Iterates over coauthor pairs.

        Returns:
            generator: A generator with the pair of coauthors of the articles
                in the collections.
        """
        for article in self._articles:
            yield from (
                (source, target)
                for source, target in itertools.combinations(sorted(article.authors), 2)
            )

    def citation_pairs(self) -> Iterable[Tuple[Article, Article]]:
        """Computes the citation pairs for the articles in the collection.

        Returns:
            genertator: A generator with the citation links: pairs of article
            labesl, where the firts element is the article which cites the
            second element.
        """
        for article in self._articles:
            for reference in article.references:
                try:
                    yield (article, Article.from_isi_citation(reference))
                except ValueError:
                    logger.warning(
                        f"Found a malformed reference from {article.label}: {reference}"
                    )
