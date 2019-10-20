import click
from wostools import CollectionLazy
from wostools.fields import FIELDS
import json


@click.group()
def main():
    """
    A little cli for wos tools.
    """


@main.command("citation-pairs")
@click.argument("sources", type=click.File("r"), nargs=-1)
@click.option("--output", type=click.File("w"), show_default=True, default=None)
def citation_pairs(sources, output):
    """
    Build a collection by using the sources and print the citation pairs in json
    format or dumps them in the `output`.
    """
    if not len(sources) > 0:
        click.secho("You should give at least a file with documents.", fg="red")
        return

    collection = CollectionLazy.from_filenames(*[f.name for f in sources])
    pairs = collection.citation_pairs()

    if not output:
        print(json.dumps(pairs, indent=2))
    else:
        json.dump(pairs, output, indent=2)


@main.command("to-json")
@click.argument("sources", type=click.File("r"), nargs=-1)
@click.option(
    "--output", type=click.File("w"), show_default=True, default="output.json"
)
def to_json(sources, output):
    """
    Build a collection by using the sources and print the entries converted to
    to json format or dumps them in the `output`.
    """
    if not len(sources) > 0:
        click.secho("You should give at least a file with documents.", fg="red")
        return

    click.secho(f"Extracting documents into the file `{output.name}` ...", fg="green")
    collection = CollectionLazy.from_filenames(*[f.name for f in sources])
    lenght = collection.lenght
    fields = sorted(FIELDS.keys())
    output.write("[\n")
    for i, article in enumerate(collection.articles):
        text = json.dumps(
            {field: article.data[field] for field in fields if field in article},
            indent=2,
        )
        text = "  " + "\n  ".join(text.split("\n"))

        output.write(text)

        if i + 1 < lenght:
            output.write(",\n")
        else:
            output.write("\n")
    output.write("]")

    click.secho(f"Extraction completed  =)", fg="green")
