"""Tests for `wostools` package."""

from click.testing import CliRunner

from wostools import CollectionLazy
from wostools import cli
from wostools import Article
import pytest
import io


def test_article_label(article):
    """
    Test label value of article.
    """
    assert article.label == (
        "Wodarz S, 2017, J MAGN MAGN MATER, V430, P52, DOI 10.1016/j.jmmm.2017.01.061"
    )


def test_parsers(article):
    assert article.extra["PT"] == "J"
    assert article.authors == ["Wodarz, S", "Hasegawa, T", "Ishio, S", "Homma, T"]
    assert article.extra["AF"] == [
        "Wodarz, Siggi",
        "Hasegawa, Takashi",
        "Ishio, Shunji",
        "Homma, Takayuki",
    ]
    assert (
        article.title
        == "Structural control of ultra-fine CoPt nanodot arrays via electrodeposition process"
    )
    assert article.extra["SO"] == "JOURNAL OF MAGNETISM AND MAGNETIC MATERIALS"


def test_article_attributes(article):
    assert set(article.extra.keys()).issuperset(
        {
            "PT",
            "AU",
            "AF",
            "TI",
            "SO",
            "LA",
            "DT",
            "DE",
            "ID",
            "AB",
            "C1",
            "RP",
            "EM",
            "OI",
            "FU",
            "FX",
            "CR",
            "NR",
            "TC",
            "Z9",
            "U1",
            "U2",
            "PU",
            "PI",
            "PA",
            "SN",
            "EI",
            "J9",
            "JI",
            "PD",
            "PY",
            "VL",
            "BP",
            "EP",
            "DI",
            "PG",
            "WC",
            "SC",
            "GA",
            "UT",
        }
    )


def test_article_extra(article):
    data = article.extra
    assert data.get("AB") == data.get("abstract")
    assert data.get("AF") == data.get("author_full_names")
    assert data.get("AR") == data.get("article_number")
    assert data.get("AU") == data.get("authors")
    assert data.get("BA") == data.get("book_authors")
    assert data.get("BE") == data.get("editors")
    assert data.get("BF") == data.get("book_authors_full_name")
    assert data.get("BN") == data.get("international_standard_book_number")
    assert data.get("BP") == data.get("beginning_page")
    assert data.get("BS") == data.get("book_series_subtitle")
    assert data.get("C1") == data.get("author_address")
    assert data.get("CA") == data.get("group_authors")
    assert data.get("CL") == data.get("conference_location")
    assert data.get("CR") == data.get("cited_references")
    assert data.get("CR") == data.get("references")
    assert data.get("CR") == data.get("citations")
    assert data.get("CT") == data.get("conference_title")
    assert data.get("CY") == data.get("conference_date")
    assert data.get("DE") == data.get("author_keywords")
    assert data.get("DI") == data.get("digital_object_identifier")
    assert data.get("DT") == data.get("document_type")
    assert data.get("D2") == data.get("book_digital_object_identifier")
    assert data.get("ED") == data.get("editors")
    assert data.get("EM") == data.get("email_address")
    assert data.get("EI") == data.get("eissn")
    assert data.get("EP") == data.get("ending_page")
    assert data.get("FU") == data.get("funding_agency_and_grant_number")
    assert data.get("FX") == data.get("funding_text")
    assert data.get("GA") == data.get("document_delivery_number")
    assert data.get("GP") == data.get("book_group_authors")
    assert data.get("HO") == data.get("conference_host")
    assert data.get("ID") == data.get("keywords_plus")
    assert data.get("ID") == data.get("keywords")
    assert data.get("IS") == data.get("issue")
    assert data.get("J9") == data.get("source_abbreviation")
    assert data.get("JI") == data.get("iso_source_abbreviation")
    assert data.get("LA") == data.get("language")
    assert data.get("MA") == data.get("meeting_abstract")
    assert data.get("NR") == data.get("cited_reference_count")
    assert data.get("OI") == data.get("orcid_identifier")
    assert data.get("P2") == data.get("chapter_count")
    assert data.get("PA") == data.get("publisher_address")
    assert data.get("PD") == data.get("publication_date")
    assert data.get("PG") == data.get("page_count")
    assert data.get("PI") == data.get("publisher_city")
    assert data.get("PM") == data.get("pubmed_id")
    assert data.get("PN") == data.get("part_number")
    assert data.get("PT") == data.get("publication_type")
    assert data.get("PU") == data.get("publisher")
    assert data.get("PY") == data.get("year_published")
    assert data.get("RI") == data.get("researcherid_number")
    assert data.get("RP") == data.get("reprint_address")
    assert data.get("SC") == data.get("research_areas")
    assert data.get("SE") == data.get("book_series_title")
    assert data.get("SI") == data.get("special_issue")
    assert data.get("SN") == data.get("issn")
    assert data.get("SP") == data.get("conference_sponsors")
    assert data.get("SU") == data.get("supplement")
    assert data.get("TC") == data.get("wos_times_cited_count")
    assert data.get("TC") == data.get("wos_times_cited")
    assert data.get("TI") == data.get("title")
    assert data.get("U1") == data.get("usage_count")
    assert data.get("U2") == data.get("usage_count")
    assert data.get("UT") == data.get("unique_article_identifier")
    assert data.get("VL") == data.get("volume")
    assert data.get("WC") == data.get("web_of_science_categories")
    assert data.get("Z9") == data.get("total_times_cited_count")
    assert data.get("Z9") == data.get("times_cited")


def test_article_properties(article):
    assert isinstance(article.extra, dict)


def test_collection_from_filenames(collection_many_documents):
    for article in collection_many_documents.articles:
        assert isinstance(article, Article)

    for file in collection_many_documents.files:
        assert hasattr(file, "read")
        assert isinstance(file, (io.StringIO, io.TextIOWrapper))
        assert file.tell() == 0


def test_collection_from_glob():
    collection = CollectionLazy.from_glob("docs/examples/*.txt")
    for article in collection.articles:
        assert isinstance(article, Article)

    assert len(list(collection.articles)) == 13892

    for file in collection.files:
        assert hasattr(file, "read")
        assert isinstance(file, (io.StringIO, io.TextIOWrapper))
        assert file.tell() == 0


def test_collection_from_streams(filename_single_document):
    with open(filename_single_document) as file:
        _ = file.read()

        collection = CollectionLazy(file)
        for article in collection.articles:
            assert isinstance(article, Article)

        for file in collection.files:
            assert hasattr(file, "read")
            assert isinstance(file, (io.StringIO, io.TextIOWrapper))
            assert file.tell() == 0


def test_collection_with_duplicated(filename_single_document, filename_many_documents):
    collection = CollectionLazy.from_filenames(
        filename_single_document, filename_single_document, filename_single_document
    )
    assert len(list(collection.files)) == 3
    assert len(list(collection.articles)) == 87

    collection = CollectionLazy.from_filenames(
        filename_many_documents, filename_many_documents, filename_many_documents
    )
    assert len(list(collection.files)) == 3
    assert len(list(collection.articles)) == 41589


def test_collection_authors(collection_single_document):
    authors = collection_single_document.authors
    assert next(authors) == "Wodarz, S"
    assert next(authors) == "Hasegawa, T"
    assert next(authors) == "Ishio, S"
    assert next(authors) == "Homma, T"


def test_collection_coauthors(collection_single_document):
    coauthors = collection_single_document.coauthors
    assert next(coauthors) == ("Hasegawa, T", "Homma, T")
    assert next(coauthors) == ("Hasegawa, T", "Ishio, S")
    assert next(coauthors) == ("Hasegawa, T", "Wodarz, S")
    assert next(coauthors) == ("Homma, T", "Ishio, S")
    assert next(coauthors) == ("Homma, T", "Wodarz, S")
    assert next(coauthors) == ("Ishio, S", "Wodarz, S")


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "A little cli for wos tools" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_command_line_interface_citation_pairs(filename_single_document):
    runner = CliRunner()
    result = runner.invoke(cli.citation_pairs)
    assert result.exit_code == 0
    assert "You should give at least a file with documents." in result.output

    result = runner.invoke(cli.citation_pairs, filename_single_document)
    assert (
        "Wodarz S, 2017, J MAGN MAGN MATER, V430, P52, DOI 10.1016/j.jmmm.2017.01.061"
        in result.output
    )
