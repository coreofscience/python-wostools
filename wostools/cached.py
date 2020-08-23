"""
Collection with a nice cache.
"""

import itertools
import logging
from contextlib import suppress
from typing import Dict, Iterable, Iterator, Tuple

from wostools.article import Article
from wostools.base import BaseCollection
from wostools.exceptions import InvalidReference, MissingLabelFields

logger = logging.getLogger(__name__)


class CachedCollection(BaseCollection):
    """
    A collection of WOS text files.
    """

    def __init__(self, *files):
        super().__init__(*files)
        self._cache_key = None
        self._cache: Dict[str, Article] = {}
        self._preheat()

    def _articles(self) -> Iterable[Article]:
        for article_text in self._article_texts:
            yield Article.from_isi_text(article_text)

    def _add_article(self, article):
        label = article.label
        if label in self._cache:
            article = article.merge(self._cache[label])
        self._cache[label] = article

    def _preheat(self):
        # Preheat our cache
        key = ":".join(str(id(file) for file in self._files))
        if key == self._cache_key:
            return
        for article in self._articles():
            with suppress(MissingLabelFields):
                self._add_article(article)
                for reference in article.references:
                    try:
                        self._add_article(Article.from_isi_citation(reference))
                    except InvalidReference:
                        logger.info(
                            f"Ignoring malformed reference '{reference}' from '{article.label}'"
                        )
        self._cache_key = key

    def __iter__(self) -> Iterator[Article]:
        """Iterates over all articles.

        Returns:
            generator: A generator of Articles according to the text articles.
        """
        self._preheat()
        yield from self._cache.values()

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
        for article in self._cache.values():
            for reference in article.references:
                if reference in self._cache:
                    yield (article, self._cache[reference])
