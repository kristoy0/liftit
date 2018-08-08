import click

from build import create_container


@click.group()
def cli():
    pass


@cli.command()
def build():
    create_container()


if __name__ == '__main__':
    cli()
