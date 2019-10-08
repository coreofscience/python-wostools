import click

import networkx

from wostools import CollectionLazy


@click.group()
def main():
    """
    A little cli for wos tools.
    """
    click.echo("Never fear wostools cli is here")


@main.command("citation-graph")
@click.argument("source", type=click.File("r"), nargs=-1)
@click.argument("output", type=click.File("w"), nargs=1)
def citation_graph(source, output):
    """
    Build a citation graph.
    """
    collection = CollectionLazy(*[f.name for f in source])
    graph = collection.to_graph()
    networkx.write_graphml(graph, output.name)
    click.echo(click.style(f"Graph successfuly written to {output.name}", fg="green"))
