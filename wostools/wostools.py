"""
The whole wostools thing.
"""

import collections
import glob
import itertools
import re

from wostools.fields import preprocess


def popular(iterable, limit):
    """
    A little utility to compute popular values on an iterable.
    """
    return collections.Counter(iterable).most_common(limit)


def article_text_to_dict(article_text: str):
    """
    Translates an article text into a dict.
    """
    data = collections.defaultdict(list)
    field = ''
    for line in re.split(r'\n+', article_text):
        # Fix little bug with isi files
        if line.startswith('null'):
            line = line[4:]
        name = line[:2]
        value = line[3:]
        if not name.isspace():
            field = name
        if not field.isspace() and field != 'ER':
            data[field].append(value)
    return dict(data)


class WosToolsError(Exception):
    """
    All the errors go here.
    """
    pass


class Article(object):
    """
    Abstract a WOS article.
    """

    def __init__(self, article_text):
        self._article_text = article_text
        self._data = article_text_to_dict(article_text)
        self._processed_data = preprocess(self._data)

    def __getattr__(self, name):
        if name not in self._processed_data:
            raise AttributeError(
                f'{self.__class__.__name__} does not have an attribute {name}'
            )
        return self._processed_data[name]


    def __hasattr__(self, name):
        return name in self._data

    @property
    def label(self):
        fields_normalizers = {
            'AU': lambda au: au[0].replace(',', ''),
            'PY': lambda py: py[0],
            'J9': lambda j9: j9[0],
            'VL': lambda vl: f'V{vl[0]}',
            'PG': lambda pg: f'P{pg[0]}',
            'DI': lambda di: f'DOI {di[0]}',
        }
        normalized_fields = [
            normalizer(self._data[field])
            for field, normalizer in fields_normalizers.items()
            if self._data.get(field)
        ]
        label = ', '.join(normalized_fields)
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
                raise WosToolsError(f'The file {filename} was not found')

    @property
    def article_texts(self):
        """
        Iterates over all the single article texts in the colection.
        """
        for filehandle in self.files:
            data = filehandle.read()
            for article_text in data.split('\n\n')[1:]:
                if article_text == 'EF':
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
        authors = (
            article.AF
            for article in self.articles
            if hasattr(article, 'AF')
        )
        return itertools.chain(*authors)

    @property
    def coauthors(self):
        """
        Iterates over coauthor pairs.
        """
        authors_by_article = (
            article.AF
            for article in self.articles
            if hasattr(article, 'AF')
        )
        return itertools.chain(*(
            itertools.combinations(sorted(authors), 2)
            for authors in authors_by_article
        ))

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
        return {key: val/total for key, val in counters.items()}
