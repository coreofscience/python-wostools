import pytest

from wostools.fields import joined, delimited, integer


def test_joined_joins_sequences():
    assert joined(["hello", "world"]) == "hello world"


def test_delimited_split_strings():
    assert delimited(["key; word;", "more; words"]) == ["key", "word", "more", "words"]


def test_delimited_split_strings_no_semi_at_the_end():
    assert delimited(["key; word", "more; words"]) == ["key", "word", "more", "words"]


def test_integer_integer_makes_an_integer():
    assert integer(["1"]) == 1


def test_integer_raises_if_more_than_one_value_is_passed():
    with pytest.raises(ValueError):
        integer(["", ""])
