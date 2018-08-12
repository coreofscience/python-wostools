import click


@click.group()
def main():
    """
    A little cli for wos tools.
    """
    click.echo('Never fear wostools cli is here')


@main.command('citation-graph')
@click.argument('source', type=click.File('r'), nargs=-1)
@click.argument('output', type=click.File('w'), nargs=1)
def citation_graph(source, target):
    pass

