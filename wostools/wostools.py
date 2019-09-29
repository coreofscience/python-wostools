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
            It raises an error if those fields are not in the article. Finally,
            cnoverts that label to lower.
        
        Returns:
            str: A label with those required fields separated by a comma and 
                converted to lower.
        """

        required_fields = ["AU", "PY", "J9", "VL", "PG", "DI"]
        for field in required_fields:
            if field not in self._data:
                raise Exception(
                    "It is not possible to build the label because "
                    "this article does not have all the required fields: " + field
                )

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
            if self._data[field]
        ]

        label = ", ".join(normalized_fields).lower()
        return label


class CollectionLazy(object):
    """
    A collection of WOS text files.
    """

    def __init__(self, *filenames):
        self.filenames = filenames

    @classmethod
    def from_glob(cls, pattern):
        """
        Creates a new collection from a pattern using glob.
        """
        return cls(*glob.glob(pattern))

    @property
    def files(self):
        """
        Iterates over all files in the collection
        """
        for filename in self.filenames:
            try:
                with open(filename) as filehandle:
                    yield filehandle
            except FileNotFoundError:
                raise WosToolsError(f"The file {filename} was not found")

    @property
    def article_texts(self):
        """
        Iterates over all the single article texts in the colection.
        """
        for filehandle in self.files:
            data = filehandle.read()
            for article_text in data.split("\n\n")[1:]:
                if article_text == "EF":
                    continue
                yield article_text

    @property
    def articles(self):
        """
        Iterates over all articles.
        """
        for article_text in self.article_texts:
            yield Article(article_text)

    @property
    def authors(self):
        """
        Iterates over all article authors, including duplicates
        """
        authors = (article.AF for article in self.articles if hasattr(article, "AF"))
        return itertools.chain(*authors)

    @property
    def coauthors(self):
        """
        Iterates over coauthor pairs.
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

    def completeness(self, key=None):
        """
        Computes the completeness of the collection by key.
        """
        counters = collections.defaultdict(int)
        total = 0
        for article in self.articles:
            total += 1
            for key in article.keys():
                counters[key] += 1
        return {key: val / total for key, val in counters.items()}

    def to_graph(self):
        adjacency = [
            (article.label, citation)
            for article in self.articles
            for citation in article.references
        ]
        g = nx.Graph()
        g.add_edges_from(adjacency)
        for alias in field_aliases():
            attributes = {
                article.label: article._processed_data.get(alias, "")
                for article in self.articles
            }
            attributes = {
                label: ";".join(value) if isinstance(value, list) else value
                for label, value in attributes.items()
            }
            nx.set_node_attributes(g, attributes, alias)
        return g
