import collections
import logging
import re
from typing import Any, List, Mapping, Optional, Set

from wostools.exceptions import InvalidIsiLine, InvalidReference, MissingLabelFields
from wostools.fields import parse_all

logger = logging.getLogger(__name__)

# The null part accounts for an ISI wok bug
ISI_LINE_PATTERN = re.compile(
    r"^(null|.)?((?P<field>[A-Z0-9]{2})|  )( (?P<value>.*))?$"
)

ISI_CITATION_PATTERN = re.compile(
    r"""^(?P<AU>[^,]+),[ ]          # First author
        (?P<PY>\d{4}),[ ]           # Publication year
        (?P<J9>[^,]+)               # Journal
        (,[ ]V(?P<VL>[\w\d-]+))?    # Volume
        (,[ ][Pp](?P<BP>\w+))?      # Start page
        (,[ ]DOI[ ](?P<DI>.+))?     # The all important DOI
        """,
    re.X,
)


class Article:
    def __init__(
        self,
        title: Optional[str],
        authors: List[str],
        year: Optional[int],
        journal: Optional[str],
        volume: Optional[str] = None,
        issue: Optional[str] = None,
        page: Optional[str] = None,
        doi: Optional[str] = None,
        references: Optional[List[str]] = None,
        keywords: Optional[List[str]] = None,
        sources: Optional[Set[str]] = None,
        extra: Optional[Mapping] = None,
    ):
        self.title: Optional[str] = title
        self.authors: List[str] = authors
        self.keywords: List[str] = keywords or []
        self.year: Optional[int] = year
        self.journal: Optional[str] = journal
        self.volume: Optional[str] = volume
        self.issue: Optional[str] = issue
        self.page: Optional[str] = page
        self.doi: Optional[str] = doi
        self.references: List[str] = references or []
        self.sources: Set[str] = sources or set()
        self.extra: Mapping[str, Any] = extra or {}

    @property
    def label(self) -> str:
        if self.doi:
            return self.doi
        return self._label()

    def _label(self, exclude_doi=False, lower_p=False) -> str:
        if not (self.authors and self.year and self.journal):
            raise MissingLabelFields(self)
        page_prefix = "p" if lower_p else "P"
        pieces = {
            "AU": self.authors[0].replace(",", ""),
            "PY": str(self.year),
            "J9": str(self.journal),
            "VL": f"V{self.volume}" if self.volume else None,
            "BP": f"{page_prefix}{self.page}" if self.page else None,
            "DI": f"DOI {self.doi}" if self.doi else None,
        }
        return ", ".join(value for value in pieces.values() if value)

    @property
    def labels(self) -> Set[str]:
        if not self.doi:
            return {self.label, self._label(lower_p=True)}
        return {
            self.doi,
            self.label,
            self._label(exclude_doi=True),
            self._label(lower_p=True),
            self._label(exclude_doi=True, lower_p=True),
        }

    def to_dict(self, simplified=True):
        """
        Transform the article into some key value pairs for easy transportation.
        """
        extra = (
            {
                "references": self.references,
                "extra": self.extra,
                "sources": list(self.sources),
            }
            if not simplified
            else {}
        )
        return {
            "title": self.title,
            "authors": self.authors,
            "keywords": self.keywords,
            "year": self.year,
            "journal": self.journal,
            "volume": self.volume,
            "issue": self.issue,
            "page": self.page,
            "doi": self.doi,
            **extra,
        }

    def merge(self, other: "Article") -> "Article":
        if other.label not in self.labels:
            logger.warning(
                "\n".join(
                    [
                        "Mixing articles with different labels might result in tragedy",
                        f"  mine:   {self.labels}",
                        f"  others: {other.label}",
                    ]
                )
            )
        return Article(
            title=self.title or other.title,
            authors=(
                self.authors
                + [author for author in other.authors if author not in self.authors]
            ),
            year=self.year or other.year,
            journal=self.journal or other.journal,
            volume=self.volume or other.volume,
            issue=self.issue or other.issue,
            page=self.page or other.page,
            doi=self.doi or other.doi,
            sources={*self.sources, *other.sources},
            extra={**self.extra, **other.extra},
            references=list({*self.references, *other.references}),
            keywords=list({*self.keywords, *other.keywords}),
        )

    @classmethod
    def from_isi_text(cls, raw: str) -> "Article":
        data = collections.defaultdict(list)
        field = None
        for line in raw.split("\n"):
            match = ISI_LINE_PATTERN.match(line)
            if not match:
                raise InvalidIsiLine(line)
            parsed = match.groupdict()
            field = parsed.get("field") or field
            if not field or "value" not in parsed or parsed["value"] is None:
                continue
            data[field].append(parsed["value"])
        processed = parse_all(dict(data))
        return cls(
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
            sources={raw},
        )

    @classmethod
    def from_isi_citation(cls, reference: str) -> "Article":
        match = ISI_CITATION_PATTERN.match(reference)
        if not match:
            raise InvalidReference(reference)
        data = {key: [value] for key, value in match.groupdict().items() if value}
        processed = parse_all(data)
        return cls(
            title=processed.get("title"),
            authors=processed.get("authors", []),
            year=processed.get("year"),
            journal=processed.get("source_abbreviation"),
            volume=processed.get("volume"),
            page=processed.get("beginning_page"),
            doi=processed.get("DOI"),
            extra=processed,
            sources={reference},
        )
