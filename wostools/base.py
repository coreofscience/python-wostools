"""
Base collection for a shared API.
"""

import glob
import logging
from typing import Iterable, Iterator, TextIO, Tuple

from wostools.article import Article
from wostools.exceptions import InvalidReference, WosToolsError
from wostools.sources import isi, scopus

logger = logging.getLogger(__name__)


class BaseCollection:
    """
    A collection of WOS text files.
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
            BaseCollection: Collection with the articles by using the pattern.
        """
        return cls.from_filenames(*glob.glob(pattern))

    @classmethod
    def from_filenames(cls, *filenames):
        """Creates a new collection from a list of filenames.

        Args:
            filenames (str): String with the filename.

        Returns:
            BaseCollection: Collection with the articles by reading the
                filenames.
        """
        files = [open(filename, encoding="utf-8-sig") for filename in filenames]
        return cls(*files)

    @property
    def _iter_files(self) -> Iterable[TextIO]:
        """Iterates over all the single article texts in the colection.

        Returns:
            generator: A generator of strings with the text articles.
        """
        for filehandle in self._files:
            filehandle.seek(0)
            yield filehandle
            filehandle.seek(0)

    def _articles(self) -> Iterable[Article]:
        for file in self._iter_files:
            try:
                yield from isi.parse_file(file)
            except WosToolsError:
                yield from scopus.parse_file(file)

    def __iter__(self) -> Iterator[Article]:
        """
        Should iterate over all articles known in the collection.
        """
        for article in self._articles():
            yield article
            for reference in article.references:
                try:
                    yield Article.from_isi_citation(reference)
                except InvalidReference:
                    logger.info(
                        f"Ignoring malformed reference '{reference}' from '{article.label}'"
                    )

    def __len__(self):
        return sum(1 for _ in self)

    @property
    def authors(self) -> Iterable[str]:
        """Iterates over all article authors, including duplicates

        Returns:
            generator: A generator with the authors (one by one) of the
                articles in the collection.
        """
        raise NotImplementedError("Sub classes should know how to iterate over authors")

    @property
    def coauthors(self) -> Iterable[Tuple[str, str]]:
        """Iterates over coauthor pairs.

        Returns:
            generator: A generator with the pair of coauthors of the articles
            in the collections.
        """
        raise NotImplementedError(
            "Sub classes should know how to iterate over coauthors"
        )

    @property
    def citation_pairs(self) -> Iterable[Tuple[Article, Article]]:
        """
        Computes the citation pairs for the articles in the collection.

        Returns:
            genertator: A generator with the citation links: pairs of article
            labesl, where the firts element is the article which cites the
            second element.
        """
        raise NotImplementedError(
            "Sub classes should know how to iterate over citation pairs"
        )
