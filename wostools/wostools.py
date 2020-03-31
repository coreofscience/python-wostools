"""
The whole wostools thing.
"""

import collections
import glob
import itertools
import re
from typing import Dict, Callable, Optional, Tuple, TypeVar, Iterable

from wostools.fields import preprocess


LABEL_ATTRIBUTES = {
    "AU": lambda au: au[0].replace(",", ""),
    "PY": lambda py: py[0],
    "J9": lambda j9: j9[0],
    "VL": lambda vl: f"V{vl[0]}",
    "BP": lambda bp: f"P{bp[0]}",
    "DI": lambda di: f"DOI {di[0]}",
}


_T = TypeVar("T")
_V = TypeVar("V")


class WosToolsError(Exception):
    """
    All the errors go here.
    """

    pass


def parse_label(label: str) -> Dict:
    pattern = re.compile(
        r"""^(?P<AU>[^,]+)?,[ ]         # First author
            (?P<PY>\d{4})?,[ ]          # Publication year
            (?P<J9>[^,]+)?              # Journal
            (,[ ]V(?P<VL>[\w\d-]+))?    # Volume
            (,[ ][Pp](?P<BP>\d+))?      # Start page
            (,[ ]DOI[ ](?P<DI>.+))?     # The all important DOI
            """,
        re.X,
    )

    default_value = {attr: 0 if attr == "PY" else None for attr in LABEL_ATTRIBUTES}

    match_result = pattern.match(label)
    if match_result:
        match_dict = match_result.groupdict()
        match_dict["PY"] = int(match_dict["PY"] or 0)
        return match_dict
    else:
        return default_value


class Article(object):
    """
    Abstract a WoS article. It creates some structures to manage the data
        related to an article. All the fields could be called as attributes.
        Finally, it contains a method to return a sanitized (and hope unique)
        label.

    Args:
        article_text (str): A string containing the record for a WoS article.
    """

    def __init__(self, article_text):
        if article_text.startswith("FN"):
            article_text = "\n".join(article_text.split("\n")[2:])

        self.__article_text = article_text
        self.__raw_data = Article.__article_text_to_dict(article_text)
        self.__processed_data = preprocess(self.__raw_data)

    def __getattr__(self, name):
        if name not in self.__processed_data:
            raise AttributeError(
                f"{self.__class__.__name__} does not have an attribute {name}"
            )
        return self.__processed_data[name]

    @property
    def label_attrs(self):
        return {attr: self.__processed_data.get(attr) for attr in LABEL_ATTRIBUTES}

    @property
    def label(self):
        """Builds a label using the fields ["AU", "PY", "J9", "VL", "PG", "DI"].

        Returns:
            str: A label with those required fields separated by a comma.
        """

        normalized_fields = [
            normalizer(self.__raw_data[field])
            for field, normalizer in LABEL_ATTRIBUTES.items()
            if self.__raw_data.get(field)
        ]

        label = ", ".join(normalized_fields)
        return label

    def __repr__(self):
        return self.label

    def keys(self):
        return self.__raw_data.keys()

    @property
    def text(self):
        return self.__article_text

    @property
    def raw_data(self):
        return self.__raw_data

    @property
    def data(self):
        return self.__processed_data

    @staticmethod
    def __article_text_to_dict(article_text: str):
        """Translates an article text into a dict using the WoS field tags:
                http://wos-resources.roblib.upei.ca/WOK46/help/WOK/hft_wos.html

        Args:
            article_text (str): String with the text of the record for an article.

        Returns:
            dict: A dict where the keys are the Web of Science Field Tags and the
                values are the content of the passed article.
        """

        if article_text.startswith("FN"):
            article_text = "\n".join(article_text.split("\n")[2:])

        # Fix little bug with isi files
        if article_text.startswith("null"):
            article_text = article_text[4:]

        data = collections.defaultdict(list)
        field = ""
        for line in re.split(r"\n+", article_text):
            name = line[:2]
            value = line[3:]

            if not name.isspace():
                field = name

            if field != "ER":
                data[field].append(value)
        return dict(data)

    def __contains__(self, value):
        return value in self.__processed_data


class CollectionLazy(object):
    """A collection of WOS text files.

    Args:
        *filenames (str): Strings with the names of the files containing
            articles.
    """

    def __init__(self, *files):
        self.__files = files
        for file in self.__files:
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
        files = []
        for filename in filenames:
            try:
                files.append(open(filename, encoding="utf-8-sig"))
            except FileNotFoundError:
                raise WosToolsError(f"The file {filename} was not found")
        return cls(*files)

    @property
    def files(self):
        """Iterates over all files in the collection

        Returns:
            generator: A generator of stream files.
        """
        for filehandle in self.__files:
            yield filehandle

    @property
    def __article_texts(self):
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
    def articles(self):
        """Iterates over all articles.

        Returns:
            generator: A generator of Articles according to the text articles.
        """
        uniques = set()
        for article_text in self.__article_texts:
            article = Article(article_text)
            if article.label not in uniques:
                uniques.add(article.label)
                yield article
            else:
                continue

    def __len__(self):
        count = 0
        for _ in self.articles:
            count += 1
        return count

    @property
    def authors(self):
        """Iterates over all article authors, including duplicates

        Returns:
            generator: A generator with the authors (one by one) of the
                articles in the collection.
        """
        authors = (article.AF for article in self.articles if hasattr(article, "AF"))
        return itertools.chain(*authors)

    @property
    def coauthors(self):
        """Iterates over coauthor pairs.

        Returns:
            generator: A generator with the pair of coauthors of the articles
                in the collections.
        """
        authors_by_article = (
            article.AF for article in self.articles if hasattr(article, "AF")
        )
        return itertools.chain(
            *(
                itertools.combinations(sorted(authors), 2)
                for authors in authors_by_article
            )
        )

    def completeness(self):
        """Computes the completeness of the collection by key.

        Returns:
            dict: A dictionary where the keys are strings corresponding to the
                WoS field tags and the values are the ratio between the articles
                containing that field and the total number of articles. E.g., if
                all the articles contain the field AF, the completeness for the
                tag AF is 1. On the other hand, e.g., if the half of the articles
                contain the tag DI while the other half do not, the completeness
                for the tag DI is 0.5.
        """
        counters = collections.defaultdict(int)
        total = 0
        for article in self.articles:
            total += 1
            for key in article.keys():
                counters[key] += 1
        return {key: val / total for key, val in counters.items()}

    @staticmethod
    def metadata_pair_parser(
        article: Article, reference: str
    ) -> Tuple[Tuple[str, Dict], Tuple[str, Dict]]:
        """
        Convenience function to pass to `citation_pairs` so that we get in 
        each side of a citation the respective labels and attributes.
        """
        return (
            (article.label, article.label_attrs),
            (reference, parse_label(reference)),
        )

    def citation_pairs(
        self, pair_parser: Optional[Callable[[Article, str], Tuple[_T, _V]]] = None
    ) -> Iterable[Tuple[_T, _V]]:
        """Computes the citation pairs for the articles in the collection.

        Returns:
            genertator: A generator with the citation links: pairs of article
            labesl, where the firts element is the article which cites the
            second element.
        """
        if pair_parser is None:
            pair_parser = lambda a, r: (a.label, r)
        yield from (
            pair_parser(article, reference)
            for article in self.articles
            for reference in article.references
        )
