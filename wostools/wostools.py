"""
The whole wostools thing.
"""

import networkx as nx

import collections
import glob
import itertools
import re

from wostools.fields import preprocess, field_aliases


def popular(iterable, limit):
    """
    A little utility to compute popular values on an iterable.
    """
    return collections.Counter(iterable).most_common(limit)


def article_text_to_dict(article_text: str):
    """Translates an article text into a dict using the WoS field tags:
            http://wos-resources.roblib.upei.ca/WOK46/help/WOK/hft_wos.html

    Args:
        article_text (str): String with the text of the record for an article.

    Returns:
        dict: A dict where the keys are the Web of Science Field Tags and the
            values are the content of the passed article.
    """
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


class WosToolsError(Exception):
    """
    All the errors go here.
    """

    pass


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
        self._article_text = article_text
        self._data = article_text_to_dict(article_text)
        self._processed_data = preprocess(self._data)

    def __getattr__(self, name):
        if name not in self._processed_data:
            raise AttributeError(
                f"{self.__class__.__name__} does not have an attribute {name}"
            )
        return self._processed_data[name]

    @property
    def label(self):
        """Builds a label using the fields ["AU", "PY", "J9", "VL", "PG", "DI"].

        Returns:
            str: A label with those required fields separated by a comma.
        """

        fields_normalizers = {
            "AU": lambda au: au[0].replace(",", ""),
            "PY": lambda py: py[0],
            "J9": lambda j9: j9[0],
            "VL": lambda vl: f"V{vl[0]}",
            "PG": lambda pg: f"P{pg[0]}",
            "DI": lambda di: f"DOI {di[0]}",
        }

        normalized_fields = [
            normalizer(self._data[field])
            for field, normalizer in fields_normalizers.items()
            if self._data.get(field)
        ]

        label = ", ".join(normalized_fields)
        return label

    def __repr__(self):
        return self.label

    def keys(self):
        return self._data.keys()


class CollectionLazy(object):
    """A collection of WOS text files.

    Args:
        *filenames (str): Strings with the names of the files containing
            articles.
    """

    def __init__(self, *filenames):
        self.filenames = filenames

    @classmethod
    def from_glob(cls, pattern):
        """Creates a new collection from a pattern using glob.

        Args:
            pattern (str): String with the patter to be passed to glob.

        Returns:
            CollectionLazy: Collection with the articles by using the pattern.
        """
        return cls(*glob.glob(pattern))

    @property
    def __files(self):
        """Iterates over all files in the collection

        Returns:
            generator: A generator of stream files.
        """
        for filename in self.filenames:
            try:
                with open(filename) as filehandle:
                    yield filehandle
            except FileNotFoundError:
                raise WosToolsError(f"The file {filename} was not found")

    @property
    def __article_texts(self):
        """Iterates over all the single article texts in the colection.

        Returns:
            generator: A generator of strings with the text articles.
        """
        for filehandle in self.__files:
            data = filehandle.read()
            # TODO: error, why are we starting from 1 ?
            # for article_text in data.split("\n\n")[1:]:
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

    def to_graph(self):
        """Computes the graph for the articles in the collection.

        Returns:
            networkx.Graph: A graph for the articles in the collection. The nodes
                are computed by using the Article `label` property (it is
                supposed to be unique and it seems, as much as possible, to the
                cited references format). Also, the graph contains the whole
                information saved as attributes.
        """
        adjacency = [
            (article.label, citation)
            for article in self.articles
            for citation in article.references
        ]
        g = nx.DiGraph()
        g.add_edges_from(adjacency)
        for alias in field_aliases():
            attributes = {
                article.label: article._processed_data.get(alias, "")
                for article in self.articles
            }
            attributes = {
                label: "; ".join(value) if isinstance(value, list) else value
                for label, value in attributes.items()
            }
            nx.set_node_attributes(g, attributes, alias)
        return g
