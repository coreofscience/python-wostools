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

