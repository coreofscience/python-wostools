import logging
import re
from typing import Dict, Iterable, List, Optional, Tuple, Type

from bibtexparser.bparser import BibTexParser

from wostools.article import Article
from wostools.exceptions import InvalidScopusFile


def _size(file) -> int:
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    return size


def _int_or_nothing(value: Optional[str]) -> Optional[int]:
    if not value:
        return None
    try:
        return int(value)
    except TypeError:
        return None


def _parse_page(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    first, *_ = value.split("-")
    return first


def _find_volume_info(ref: str) -> Tuple[Dict[str, str], str]:
    pattern = re.compile(
        "(?P<volume>\d+)( \((?P<issue>.+)\))?(, pp?\. (?P<page>\w+)(-\w+)?)?"
    )
    result = re.search(pattern, ref)
    if result is None:
        return {}, ref
    data = result.groupdict()
    if "volume" in data and data["volume"]:
        data["volume"] = f"V{data['volume']}"
    if "page" in data and data["page"]:
        data["page"] = f"P{data['page']}"
    return data, ref[result.lastindex :]


def _find_doi(ref: str) -> Tuple[Optional[str], str]:
    pattern = re.compile(
        r"((DOI:?)|(doi.org\/)|(aps.org\/doi\/)) ?(?P<doi>[^\s,]+)", re.I
    )
    result = re.search(pattern, ref)
    if result is None or "doi" not in result.groupdict():
        if "doi" in ref.lower():
            print("doi not found in", ref, result)
        return None, ref
    return f"DOI {result.groupdict()['doi']}", ref[result.lastindex :]


def _scopus_ref_to_isi(scopusref: str) -> str:
    authors, year, rest = re.split(r"(\(\d{4}\))", scopusref, maxsplit=1)
    first_name, last_name, *_ = authors.split(", ")
    # NOTE: The title might be between the authors and the year.
    year = year[1:-1]
    journal, rest = rest.split(", ", 1)
    volume_info, rest = _find_volume_info(rest)
    doi, _ = _find_doi(scopusref)
    parts = {
        "author": f"{first_name} {last_name.replace(' ', '').replace('.', '')}",
        "yaer": year,
        "journal": journal.strip().replace(".", "").upper()
        if not journal.isspace()
        else None,
        "volume": volume_info.get("volume"),
        "page": volume_info.get("page"),
        "doi": doi,
    }
    return ", ".join(val for val in parts.values() if val is not None)


def parse_references(refstring: Optional[str]) -> List[str]:
    if not refstring:
        return []
    result = []
    for ref in refstring.split(";"):
        try:
            result.append(_scopus_ref_to_isi(ref))
        except (KeyError, IndexError, TypeError, ValueError) as e:
            pass
            # print(f"ignoring {ref}", e)
    return result


def parse_file(file) -> Iterable[Article]:
    if not _size(file):
        return []

    parser = BibTexParser()
    bibliography = parser.parse_file(file)

    if not bibliography:
        raise InvalidScopusFile()

    if any(entry.get("source") != "Scopus" for entry in bibliography):
        logging.warn("This bib file doesn't come from scopus.")

    if any("abbrev_source_title" not in entry for entry in bibliography):
        logging.warn(
            "Source abreviation not found, maximum compatibility not guaranteed"
        )

    for entry in bibliography:
        yield Article(
            title=entry.get("title"),
            authors=entry.get("author", "").split(" and "),
            year=_int_or_nothing(entry.get("year")),
            journal=entry.get("abbrev_source_title", entry.get("journal")),
            volume=entry.get("volume"),
            issue=entry.get("number"),
            page=_parse_page(entry.get("pages")),
            doi=entry.get("doi"),
            keywords=entry.get("author_keywords"),
            references=parse_references(entry.get("references")),
            sources={entry.get("source")},
            extra=entry,
        )


if __name__ == "__main__":
    with open("refs.txt") as refs:
        data = [line.strip() for line in refs]
    cit = [ref for line in data for ref in parse_references(line)]
    print(sum("doi" in ref or "DOI" in ref for ref in data))
    print(sum("DOI" in ref for ref in cit))

    with open("translated.txt", "w") as refs:
        refs.write("\n".join(cit))

    _scopus_ref_to_isi(
        "Terris, B.D., Folks, L., Weller, D., Baglin, J.E.E., Kellock, A.J., Rothuizen, H., Vettiger, P., Ion beam patterning of magnetic films using stencil masks (1999) Appl. Phys. Lett., 75 (2), pp. 403-405. , July"
    )

