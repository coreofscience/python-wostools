from collections import defaultdict
import re
from typing import Dict, Iterable, List, Optional, TextIO, Tuple, Type

from bibtexparser.bparser import BibTexParser

from wostools.article import Article
from wostools.exceptions import InvalidScopusFile


def _size(file) -> int:
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    return size


def _int_or_nothing(raw: Optional[List[str]]) -> Optional[int]:
    if not raw:
        return None
    try:
        return int(raw[0])
    except TypeError:
        return None


def _joined(raw: Optional[List[str]]) -> Optional[str]:
    if not raw:
        return None
    return " ".join(raw)


def _find_volume_info(ref: str) -> Tuple[Dict[str, str], str]:
    volume_pattern = re.compile(r"(?P<volume>\d+)( \((?P<issue>.+?)\))?")
    page_pattern = re.compile(r"(pp?\. (?P<page>\w+)(-[^,\s]+)?)")
    page = page_pattern.search(ref)
    last_index = 0
    if page:
        last_index = page.lastindex or 0
        first, *_ = ref.split(page.group())
        volume = volume_pattern.search(first)
    else:
        volume = volume_pattern.search(ref)
        if volume:
            last_index = volume.lastindex or 0

    if not page and not volume:
        return {}, ref

    data = {}
    if page:
        data.update(page.groupdict())
    if volume:
        data.update(volume.groupdict())

    if "volume" in data and data["volume"]:
        data["volume"] = f"V{data['volume']}"
    if "page" in data and data["page"]:
        data["page"] = f"P{data['page']}"

    return data, ref[last_index:]


def _find_doi(ref: str) -> Tuple[Optional[str], str]:
    pattern = re.compile(
        r"((doi.org\/)|(aps.org\/doi\/)|(DOI:?)) ?(?P<doi>[^\s,;:]{5,})", re.I
    )
    result = re.search(pattern, ref)
    if result is None or "doi" not in result.groupdict():
        return None, ref
    doi = result.groupdict()["doi"]
    return f"DOI {doi}", ref[result.lastindex :]


def _scopus_ref_to_isi(scopusref: str) -> str:
    authors, year, rest = re.split(r"(\(\d{4}\))", scopusref, maxsplit=1)
    first_name, last_name, *_ = authors.split(", ")
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


def parse_references(refs: List[str]) -> List[str]:
    if not refs:
        return []
    result = []
    for ref in refs:
        try:
            result.append(_scopus_ref_to_isi(ref))
        except (KeyError, IndexError, TypeError, ValueError) as e:
            continue
    return result


def ris_to_dict(record: str) -> Dict[str, List[str]]:
    RIS_PATTERN = re.compile(r"^(((?P<key>[A-Z0-9]{2}))[ ]{2}-[ ]{1})?(?P<value>(.*))$")
    parsed = defaultdict(list)
    current = None

    for line in record.split("\n"):
        match = RIS_PATTERN.match(line)
        if not match:
            raise InvalidScopusFile()
        data = match.groupdict()
        key = data.get("key")
        value = data.get("value")
        if "ER" in data:
            break
        if key:
            if key == "N1" and value and ":" in value:
                label, value = value.split(":", 1)
                value = value.strip()
                current = f"{key}:{label.strip()}"
            else:
                current = data["key"]
        if value and current:
            parsed[current].append(data.get("value", ""))
    return dict(parsed)


def parse_record(record: str) -> Article:
    data = ris_to_dict(record)
    return Article(
        title=_joined(data.get("TI")),
        authors=data.get("AU", []),
        year=_int_or_nothing(data.get("PY")),
        journal=_joined(data.get("J2")),
        volume=_joined(data.get("VL")),
        issue=_joined(data.get("IS")),
        page=_joined(data.get("SP")),
        doi=_joined(data.get("DO")),
        keywords=data.get("KW"),
        references=parse_references(data.get("N1:References", [])),
        sources={"scopus"},
        extra=data,
    )


def parse_file(file: TextIO) -> Iterable[Article]:
    if not _size(file):
        return []
    for item in file.read().split("\n\n"):
        if item.isspace():
            continue
        article = parse_record(item.strip())
        yield article
