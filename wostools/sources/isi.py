from typing import Iterable, TextIO
from wostools.article import Article


def _split(file) -> Iterable[str]:
    parts = file.read().split("\n\n")
    for part in parts:
        if part != "ER":
            yield part


def parse_file(file: TextIO) -> Iterable[Article]:
    for raw in _split(file):
        yield Article.from_isi_text(raw)


def parse_record(record: str) -> Article:
    """
    Transforms an isi record in text form into a fully concrete article.
    """
    return Article(
        title="hello",
        authors=[],
        year=1234,
        journal="el chule",
        sources={record},
    )
