import json

import click

from wostools import CollectionLazy
from wostools.fields import field_aliases, field_keys


@click.group()
def main():
    """
    A little cli for wos tools.
    """


@main.command("citation-pairs")
@click.argument("sources", type=click.File("r"), nargs=-1)
@click.option(
    "--output",
    type=click.File("w"),
    show_default=True,
    default="-",
    help="File to save json otuput.",
)
def citation_pairs(sources, output):
    """
    Build a collection by using the sources and print the citation pairs in json
    format or dumps them in the `output`.
    """
    if not len(sources) > 0:
        click.secho("You should give at least a file with documents.", fg="red")
        return

    collection = CollectionLazy.from_filenames(*[f.name for f in sources])
    pairs = list(collection.citation_pairs())

    json.dump(pairs, output, indent=2)


@main.command("to-json")
@click.argument("sources", type=click.File("r"), nargs=-1)
@click.option(
    "--output",
    type=click.File("w"),
    show_default=True,
    default="-",
    help="File to save json otuput.",
)
@click.option(
    "--raw",
    default=False,
    is_flag=True,
    show_default=True,
    help="Flag; If true, the fields are the field tags; If false, the fields are the aliases.",
)
def to_json(sources, output, raw):
    """
    Build a collection by using the sources and print the entries converted to
    to json format or dumps them in the `output`.
    """
    if not len(sources) > 0:
        click.secho("You should give at least a file with documents.", fg="red")
        return

    collection = CollectionLazy.from_filenames(*[f.name for f in sources])
    length = len(collection)
    output.write("[\n")
    for i, article in enumerate(collection.articles):
        fields = field_keys() if raw else field_aliases()

        text = json.dumps(
            {field: article.data[field] for field in fields if field in article},
            indent=2,
        )
        text = "  " + "\n  ".join(text.split("\n"))

        output.write(text)

        if i + 1 < length:
            output.write(",\n")
        else:
            output.write("\n")
    output.write("]")
