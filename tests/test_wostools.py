"""Tests for `wostools` package."""

from click.testing import CliRunner

from wostools import CollectionLazy
from wostools import cli


def test_collection():
    """
    Just kinda an end to end test.
    """
    collection = CollectionLazy.from_filenames(
        "docs/examples/bit-pattern-savedrecs.txt"
    )
    for article in collection.articles:
        assert article.TI


def test_article_label(article):
    """
    Test label value of article.
    """
    assert article.label == (
        "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061"
    )


def test_aliases(article):
    assert article.TI == article.title


def test_parsers(article):
    assert article.year_published == 2017
    assert article.beginning_page == "52"


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "A little cli for wos tools" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
