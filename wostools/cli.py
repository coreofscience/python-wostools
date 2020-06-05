import json
import logging

import click

from wostools import Collection


@click.group()
def main():
    """
    A little cli for wos tools.
    """
    logger = logging.getLogger("wostools")
    logger.setLevel(logging.ERROR)


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

    collection = Collection.from_filenames(*[f.name for f in sources])
    pairs = [
        (source.label, target.label) for source, target in collection.citation_pairs()
    ]

    json.dump(pairs, output, indent=2)
