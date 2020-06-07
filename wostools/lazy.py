"""
The whole wostools thing.
"""

import itertools
import logging
from typing import Iterable, Tuple

from wostools.article import Article
from wostools.base import BaseCollection
from wostools.exceptions import InvalidReference

logger = logging.getLogger(__name__)


class LazyCollection(BaseCollection):
    """A collection of WOS text files.

    Args:
        filenames (str): Strings with the names of the files containing
            articles.
    """

    @property
    def _article_texts(self):
        """Iterates over all the single article texts in the colection.

        Returns:
            generator: A generator of strings with the text articles.
        """
        for filehandle in self._files:
            filehandle.seek(0)
            data = filehandle.read()
            filehandle.seek(0)
            for article_text in data.split("\n\n"):
                if article_text != "EF":
                    yield article_text

    def _articles(self) -> Iterable[Article]:
        for article_text in self._article_texts:
            yield Article.from_isi_text(article_text)

    @property
    def authors(self) -> Iterable[str]:
        """Iterates over all article authors, including duplicates

        Returns:
            generator: A generator with the authors (one by one) of the
                articles in the collection.
        """
        for article in self:
            yield from article.authors

    @property
    def coauthors(self) -> Iterable[Tuple[str, str]]:
        """Iterates over coauthor pairs.

        Returns:
            generator: A generator with the pair of coauthors of the articles
                in the collections.
        """
        for article in self._articles():
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
        for article in self:
            for reference in article.references:
                try:
                    yield (article, Article.from_isi_citation(reference))
                except InvalidReference:
                    logger.info(
                        f"Ignoring malformed reference '{reference}' from '{article.label}'"
                    )
