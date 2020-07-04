from copy import deepcopy
from dataclasses import dataclass
from typing import Optional

from pytest import fixture
from pytest_bdd import scenarios, given, then, when, parsers

from wostools.article import Article


@dataclass
class Context:
    article: Optional[Article]
    label: Optional[str] = None
    expected_label: Optional[str] = None
    error: Optional[Exception] = None


scenarios("features/article.feature")


@given("a complete article missing <field>", target_fixture="context")
@given(parsers.parse("a complete article missing {field:w}"), target_fixture="context")
def article_missing(field: str):
    article = Article(
        title=None, authors=["L, Robertson"], year=1999, journal="Science"
    )
    setattr(article, field, None)
    return Context(article=article)


@given("a complete article", target_fixture="context")
@given("an article with authors, year and journal", target_fixture="context")
def article_with_authors_year_and_journal():
    return Context(
        article=Article(
            title=None, authors=["L, Robertson"], year=1999, journal="Science"
        ),
        expected_label="L Robertson, 1999, Science",
    )


@given("theres a similar article that includes a doi", target_fixture="other")
def similar_article_with_doi(context: Context):
    assert context.article, "missing article to copy"
    article = deepcopy(context.article)
    article.doi = "somedoi/123"
    if context.expected_label:
        return Context(
            article=article,
            expected_label=", ".join([context.expected_label, article.doi]),
        )
    return Context(article=article)


@when("I compute the label for the article")
def compute_label_for_article(context: Context):
    assert context.article, "Missing article for this step"
    context.label = context.article.label


@when("I merge the two articles")
def merge_articles(context: Context, other: Context):
    assert context.article, "Missing article for this step"
    assert other.article, "Missing other article for this step"
    context.article = context.article.merge(other.article)
    context.expected_label = None


@when("I try to compute the label for the article")
def try_to_compute_label(context: Context):
    assert context.article, "Missing article for this step"
    try:
        context.label = context.article.label
    except Exception as e:
        context.error = e


@then("the label is a proper string")
def then_label_is_a_proper_string(context: Context):
    assert context.expected_label
    assert context.label
    assert context.label == context.expected_label


@then("the label contains the doi of the other")
def label_matches_other(context: Context, other: Context):
    assert context.label, "You didn't get a label in the then block"
    assert other.article and other.article.doi, "There's no doi in the other article"
    assert other.article.doi in context.label


@then("There's no error computing the label")
@then("there's no error computing the label")
def no_error_computing_label(context: Context):
    assert context.label
    assert not context.error


@then("There's an error computing the label")
def error_computing_label(context: Context):
    assert not context.label
    assert context.error
    assert isinstance(context.error, ValueError)


@then(parsers.parse("the article matches the {field:w} of the other"))
@then(parsers.parse("the article's {field:w} matches the other"))
def contais_others_field(context: Context, other: Context, field: str):
    assert context.article
    assert other.article
    assert getattr(context.article, field) == getattr(other.article, field)
