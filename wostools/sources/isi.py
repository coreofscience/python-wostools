import collections
import re
from typing import Iterable, TextIO
from wostools.exceptions import InvalidIsiLine
from wostools.article import Article
from wostools.fields import parse_all

ISI_LINE_PATTERN = re.compile(
    r"^(null|.)?((?P<field>[A-Z0-9]{2})|  )( (?P<value>.*))?$"
)

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
    data = collections.defaultdict(list)
    field = None
    for line in record.split("\n"):
        match = ISI_LINE_PATTERN.match(line)
        if not match:
            raise InvalidIsiLine(line)
        parsed = match.groupdict()
        field = parsed.get("field") or field
        if not field or "value" not in parsed or parsed["value"] is None:
            continue
        data[field].append(parsed["value"])
    processed = parse_all(dict(data))

    # TODO: think what we lose without sub-classing.
    return Article(
        title=processed.get("title"),
        authors=processed.get("authors", []),
        year=processed.get("year"),
        journal=processed.get("source_abbreviation"),
        volume=processed.get("volume"),
        issue=processed.get("issue"),
        page=processed.get("beginning_page"),
        doi=processed.get("DOI"),
        references=processed.get("references"),
        keywords=processed.get("keywords"),
        extra=processed,
        sources={record},
    )
