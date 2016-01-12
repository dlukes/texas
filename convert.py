import click
import logging


@click.command()
@click.option("--log", help="logging verbosity", default="DEBUG",
              type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]))
@click.argument("input", type=click.File("r"))
def cli(log, input):
    """Convert Texas Czech EAF transcript to conform to Lida Cope's guidelines.

    Our changes to the original guidelines:

    \b
    - + instead of – (dash)
    - ;l instead of ł
    - ;L instead of Ł

    """
    logging.basicConfig(level=log)
    click.echo("This works.")
